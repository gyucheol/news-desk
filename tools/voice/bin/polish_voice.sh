#!/usr/bin/env bash
# polish_voice.sh - conservative clean-up chain for spoken-voice recordings.
#
# decode (any format) -> 48 kHz float -> high-pass [-> de-hum] -> pre-level
# -> noise reduction (dfn | rnn | afftdn | nr | none) with wet/dry mix
# [-> de-ess] -> gentle compression [-> trim leading/trailing silence]
# -> two-pass loudness normalisation with true-peak limiting
# -> 48 kHz 24-bit WAV + AAC .m4a (or MP3). The input is never modified and
# existing outputs are never overwritten.
set -euo pipefail

BIN_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
VT_DIR="$(dirname "$BIN_DIR")"
PY="${VT_PY:-$VT_DIR/venv/bin/python}"
PY311="${VT_PY311:-$VT_DIR/venv311/bin/python}"
RNN_DIR="${VT_RNN_DIR:-$VT_DIR/downloads/arnndn-models}"
DFN_DIR="${VT_DFN_DIR:-$VT_DIR/downloads/dfn3-model/DeepFilterNet3}"

# ---------------- defaults ----------------
DENOISE=auto        # auto = dfn if installed, else afftdn
STRENGTH=1.0        # wet/dry mix of the denoiser output (1 = fully processed)
ATTEN_LIM=24        # dfn: max noise attenuation in dB (0 = unlimited); 24 tested best
RNN_MODEL=std       # arnndn model: std|sh|bd|cb|lq|mp
AFFTDN_NR=24        # afftdn: noise reduction (dB)
AFFTDN_NF=-40       # afftdn: initial noise floor (dB), tracked afterwards
NR_PROP=0.5         # noisereduce: prop_decrease
HP=80               # high-pass cut-off in Hz (0 = off)
DEHUM=0             # mains hum notch: 0 (off), 50 or 60 Hz (+4 harmonics)
DEESS=0             # de-esser intensity 0..1 (0 = off)
COMP=1              # gentle compressor on/off
TARGET=-16          # integrated loudness target (LUFS)
TP=-1.5             # true-peak ceiling (dBTP)
DUALMONO=0          # measure mono as dual-mono (+3 dB, "as heard on stereo")
TRIM=0              # trim leading/trailing silence only
STEREO=0            # keep stereo (default: mono downmix)
CHANNEL=""          # left|right: use only one input channel
FORMAT=m4a          # compact output: m4a (AAC) or mp3
BITRATE=""          # compact output bitrate (default 128k mono / 192k stereo)
OUTDIR=""
NAME=""
START=""
DURATION=""
KEEP_WORK=0
STOP_AFTER=""       # debug: stop after "denoise" and write <name>_denoised.wav
PRELEVEL=-23        # internal working level (LUFS) before denoise/compression

usage() {
  cat <<'EOF'
Usage: polish_voice.sh [options] INPUT_FILE

Output (never overwrites anything; a numeric suffix is added if needed):
  <outdir>/<name>.wav   48 kHz, 24-bit PCM
  <outdir>/<name>.m4a   AAC (or .mp3 with --format mp3)
  <outdir>/<name>_report.txt

Options:
  -o, --outdir DIR       output directory (default: <input dir>/polished)
  -n, --name NAME        output base name (default: <input name>_polished)
  -d, --denoise M        dfn (DeepFilterNet3, AI) | rnn (RNNoise/arnndn, AI) |
                         afftdn (classic FFT denoiser) | nr (noisereduce) | none
                         (default: dfn if installed, otherwise afftdn)
  -s, --strength X       0..1 blend of denoised with original (default 1.0)
      --atten-lim DB     dfn: limit noise attenuation to DB (default 24; 0 = unlimited)
      --rnn-model M      rnn: std|sh|bd|cb|lq|mp (default std)
      --afftdn-nr DB     afftdn: noise reduction in dB (default 24)
      --afftdn-nf DB     afftdn: initial noise floor in dB (default -40)
      --nr-prop X        nr: prop_decrease 0..1 (default 0.5)
      --hp HZ            high-pass cut-off (default 80, 0 = off)
      --dehum 50|60      notch mains hum + 4 harmonics (Korea 60 Hz). Can thin low male
                         voices; DFN already removes hum, so normally leave off
      --deess [X]        enable de-esser, intensity X (default 0.5 when given)
      --no-comp          disable the gentle compressor
  -t, --target LUFS      loudness target: -16 (default), -14, -23, or any value
      --tp DBTP          true-peak ceiling (default -1.5)
      --dual-mono        measure mono loudness as dual-mono (stereo playback)
      --trim             trim leading/trailing silence (never inside speech)
      --stereo           keep stereo instead of mono downmix
      --channel L|R      use only the left or right input channel
      --format m4a|mp3   compact output format (default m4a)
      --bitrate RATE     compact output bitrate (default 128k mono, 192k stereo)
      --start S          process from S seconds (preview/excerpt)
      --duration S       process only S seconds (preview/excerpt)
      --keep-work        keep intermediate WAV files
  -h, --help             show this help
EOF
}

die() { echo "polish_voice: error: $*" >&2; exit 1; }
log() { echo "[polish_voice] $*" >&2; }
now() { date +%s.%N; }
fcalc() { awk "BEGIN{ printf \"%.6f\", $* }"; }
fmt1() { awk -v v="$1" 'BEGIN{ if (v=="" || v ~ /inf|nan/) print "n/a"; else printf "%.1f", v }'; }

# ---------------- argument parsing ----------------
INPUT=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    -o|--outdir) OUTDIR="$2"; shift 2;;
    -n|--name) NAME="$2"; shift 2;;
    -d|--denoise) DENOISE="$2"; shift 2;;
    -s|--strength) STRENGTH="$2"; shift 2;;
    --atten-lim) ATTEN_LIM="$2"; shift 2;;
    --rnn-model) RNN_MODEL="$2"; shift 2;;
    --afftdn-nr) AFFTDN_NR="$2"; shift 2;;
    --afftdn-nf) AFFTDN_NF="$2"; shift 2;;
    --nr-prop) NR_PROP="$2"; shift 2;;
    --hp) HP="$2"; shift 2;;
    --dehum) DEHUM="$2"; shift 2;;
    --deess)
      if [[ $# -ge 2 && "$2" =~ ^[0-9.]+$ ]]; then DEESS="$2"; shift 2; else DEESS=0.5; shift; fi;;
    --no-comp) COMP=0; shift;;
    -t|--target) TARGET="$2"; shift 2;;
    --tp) TP="$2"; shift 2;;
    --dual-mono) DUALMONO=1; shift;;
    --trim) TRIM=1; shift;;
    --stereo) STEREO=1; shift;;
    --channel) CHANNEL="$2"; shift 2;;
    --format) FORMAT="$2"; shift 2;;
    --bitrate) BITRATE="$2"; shift 2;;
    --start) START="$2"; shift 2;;
    --duration) DURATION="$2"; shift 2;;
    --keep-work) KEEP_WORK=1; shift;;
    --stop-after) STOP_AFTER="$2"; shift 2;;
    -h|--help) usage; exit 0;;
    --) shift; INPUT="${1:-}"; shift || true;;
    -*) die "unknown option: $1 (see --help)";;
    *) [[ -z "$INPUT" ]] || die "only one input file is supported"; INPUT="$1"; shift;;
  esac
done
[[ -n "$INPUT" ]] || { usage; exit 2; }
[[ -f "$INPUT" && -r "$INPUT" ]] || die "cannot read input file: $INPUT"
command -v ffmpeg >/dev/null || die "ffmpeg not found"
num='^-?[0-9]+([.][0-9]+)?$'
for v in "$STRENGTH" "$TARGET" "$TP" "$HP" "$AFFTDN_NR" "$AFFTDN_NF" "$NR_PROP" "$DEESS"; do
  [[ "$v" =~ $num ]] || die "not a number: $v"
done
[[ -z "$ATTEN_LIM" || "$ATTEN_LIM" =~ $num ]] || die "--atten-lim must be a number"
awk -v s="$STRENGTH" 'BEGIN{exit !(s>=0 && s<=1)}' || die "--strength must be within 0..1"
awk -v t="$TP" 'BEGIN{exit !(t<=0 && t>=-9)}' || die "--tp must be within -9..0"
awk -v t="$TARGET" 'BEGIN{exit !(t<=-5 && t>=-40)}' || die "--target must be within -40..-5"
[[ "$DEHUM" =~ ^(0|50|60)$ ]] || die "--dehum must be 50 or 60"
[[ "$FORMAT" =~ ^(m4a|mp3)$ ]] || die "--format must be m4a or mp3"
case "${CHANNEL,,}" in ""|l|left|r|right) ;; *) die "--channel must be left or right";; esac
if [[ "$DENOISE" == auto ]]; then
  if [[ -x "$PY311" && -f "$DFN_DIR/config.ini" ]]; then DENOISE=dfn; else DENOISE=afftdn; fi
fi
case "$DENOISE" in
  dfn) [[ -x "$PY311" && -f "$DFN_DIR/config.ini" ]] || die "DeepFilterNet not installed ($PY311, $DFN_DIR)";;
  rnn) [[ -f "$RNN_DIR/$RNN_MODEL.rnnn" ]] || die "RNNoise model not found: $RNN_DIR/$RNN_MODEL.rnnn";;
  nr) [[ -x "$PY" ]] || die "python venv not found: $PY";;
  afftdn|none) ;;
  *) die "unknown --denoise method: $DENOISE";;
esac

# ---------------- output paths (never overwrite) ----------------
IN_ABS="$(readlink -f "$INPUT")"
IN_BASE="$(basename "$IN_ABS")"; IN_STEM="${IN_BASE%.*}"
[[ -n "$OUTDIR" ]] || OUTDIR="$(dirname "$IN_ABS")/polished"
[[ -n "$NAME" ]] || NAME="${IN_STEM}_polished"
mkdir -p "$OUTDIR"
OUTDIR="$(readlink -f "$OUTDIR")"
CEXT="$FORMAT"
stem="$OUTDIR/$NAME"; k=1
while [[ -e "$stem.wav" || -e "$stem.$CEXT" || -e "${stem}_report.txt" || -e "${stem}_denoised.wav" ]]; do
  k=$((k+1)); stem="$OUTDIR/${NAME}_$k"
done
OUT_WAV="$stem.wav"; OUT_C="$stem.$CEXT"; OUT_REP="${stem}_report.txt"
for o in "$OUT_WAV" "$OUT_C"; do [[ "$o" != "$IN_ABS" ]] || die "output would overwrite the input"; done

W="$(mktemp -d "$OUTDIR/.polish_work.XXXXXX")"
cleanup() { if [[ "$KEEP_WORK" == 1 ]]; then log "work files kept in $W"; else rm -rf "$W"; fi; }
trap cleanup EXIT

# ---------------- helpers ----------------
measure() {  # FILE -> "I LRA TP"
  local dm=""; [[ "$DUALMONO" == 1 ]] && dm=":dualmono=true"
  ffmpeg -nostdin -hide_banner -nostats -i "$1" -filter_complex "ebur128=peak=true:framelog=quiet$dm" \
    -f null - 2>&1 | awk '/Summary:/{s=1} s&&$1=="I:"{i=$2} s&&$1=="LRA:"{l=$2} s&&$1=="Peak:"{p=$2} END{print i, l, p}'
}
ff() { ffmpeg -nostdin -hide_banner -v error -y "$@"; }
duration_of() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }

T0=$(now)
# ---------------- 1. decode ----------------
read -r SRC_CODEC SRC_SR SRC_CH < <(ffprobe -v error -select_streams a:0 \
  -show_entries stream=codec_name,sample_rate,channels -of csv=p=0 "$IN_ABS" | head -1 | tr ',' ' ') \
  || die "no audio stream found in $INPUT"
SRC_DUR="$(duration_of "$IN_ABS" | awk '{printf "%.2f", $1}' || echo "?")"
log "input: $IN_BASE  codec=$SRC_CODEC ${SRC_SR}Hz ch=$SRC_CH dur=${SRC_DUR}s"
CH_AF=""
case "${CHANNEL,,}" in l|left) CH_AF="pan=mono|c0=c0,";; r|right) CH_AF="pan=mono|c0=c1,";; esac
if [[ "$STEREO" == 1 && -z "$CH_AF" && "${SRC_CH:-1}" -ge 2 ]]; then AC=2; else AC=1; fi
seek=(); [[ -n "$START" ]] && seek+=(-ss "$START"); [[ -n "$DURATION" ]] && seek+=(-t "$DURATION")
ff "${seek[@]}" -i "$IN_ABS" -map 0:a:0 -vn \
  -af "${CH_AF}aresample=48000:resampler=soxr:precision=28,aformat=sample_fmts=flt" \
  -ac "$AC" -c:a pcm_f32le "$W/00_decoded.wav" || die "decoding failed"
read -r IN_I IN_LRA IN_TP < <(measure "$W/00_decoded.wav")
DUR="$(duration_of "$W/00_decoded.wav" | awk '{printf "%.2f", $1}')"
T1=$(now)

# ---------------- 2. high-pass, de-hum, pre-level ----------------
PRE_AF="anull"
[[ "$HP" != 0 ]] && PRE_AF="highpass=f=${HP}:poles=2"
if [[ "$DEHUM" != 0 ]]; then
  for h in 1 2 3 4 5; do PRE_AF+=",bandreject=f=$((DEHUM*h)):t=q:w=8"; done
fi
read -r PI _ _ < <(ffmpeg -nostdin -hide_banner -nostats -i "$W/00_decoded.wav" \
  -filter_complex "$PRE_AF,ebur128=framelog=quiet" -f null - 2>&1 | awk '/Summary:/{s=1} s&&$1=="I:"{print $2}')
if awk -v i="${PI:--70}" 'BEGIN{exit !(i>-69)}'; then
  PRE_G=$(awk -v t="$PRELEVEL" -v i="$PI" 'BEGIN{g=t-i; if(g>40)g=40; if(g<-20)g=-20; printf "%.2f", g}')
else
  PRE_G=0; log "warning: input is (nearly) silent; no pre-gain applied"
fi
ff -i "$W/00_decoded.wav" -af "$PRE_AF,volume=${PRE_G}dB" -c:a pcm_f32le "$W/01_pre.wav"
T2=$(now)

# ---------------- 3. noise reduction ----------------
DN_DESC="$DENOISE"
case "$DENOISE" in
  none) cp "$W/01_pre.wav" "$W/02_dn.wav";;
  afftdn)  # afftdn delays by 1200 samples at 48 kHz: pad, then trim
    DN_DESC="afftdn nr=$AFFTDN_NR nf=$AFFTDN_NF tn=1"
    ff -i "$W/01_pre.wav" -af "apad=pad_len=1200,afftdn=nr=${AFFTDN_NR}:nf=${AFFTDN_NF}:tn=1,atrim=start_sample=1200,asetpts=N/SR/TB" \
      -c:a pcm_f32le "$W/02_dn.wav";;
  rnn)  # arnndn delays by 480 samples (one 10 ms frame): pad, then trim
    DN_DESC="arnndn model=$RNN_MODEL"
    ff -i "$W/01_pre.wav" -af "apad=pad_len=480,arnndn=m='$RNN_DIR/$RNN_MODEL.rnnn',atrim=start_sample=480,asetpts=N/SR/TB" \
      -c:a pcm_f32le "$W/02_dn.wav";;
  dfn)
    DN_DESC="DeepFilterNet3${ATTEN_LIM:+ atten_lim=${ATTEN_LIM}dB}"
    "$PY311" -I "$BIN_DIR/dfn_enhance.py" "$W/01_pre.wav" "$W/02_dn.wav" --model-dir "$DFN_DIR" \
      --chunk-s "${VT_DFN_CHUNK_S:-120}" ${ATTEN_LIM:+--atten-lim "$ATTEN_LIM"} \
      2> >(grep -v "not a git repository" >&2) || die "DeepFilterNet failed";;
  nr)
    DN_DESC="noisereduce prop=$NR_PROP"
    "$PY" -I "$BIN_DIR/nr_enhance.py" "$W/01_pre.wav" "$W/02_dn.wav" --prop "$NR_PROP" || die "noisereduce failed";;
esac
if [[ "$DENOISE" != none && -x "$PY" ]]; then
  LAG=$("$PY" -I "$BIN_DIR/vt_util.py" lag "$W/01_pre.wav" "$W/02_dn.wav" 2>/dev/null || echo "?")
  [[ "$LAG" == 0 ]] || log "warning: denoised signal appears shifted by $LAG samples vs. input"
fi
if awk -v s="$STRENGTH" 'BEGIN{exit !(s<1)}'; then
  DRY=$(fcalc "1-$STRENGTH")
  ff -i "$W/02_dn.wav" -i "$W/01_pre.wav" \
    -filter_complex "[0:a][1:a]amix=inputs=2:weights='$STRENGTH $DRY':normalize=0:duration=first" \
    -c:a pcm_f32le "$W/03_mix.wav"
  DN_DESC+=" mix=$STRENGTH"
else
  mv "$W/02_dn.wav" "$W/03_mix.wav"
fi
T3=$(now)
if [[ "$STOP_AFTER" == denoise ]]; then
  ff -i "$W/03_mix.wav" -c:a pcm_f32le "${stem}_denoised.wav"
  log "stopped after denoise: ${stem}_denoised.wav"; exit 0
fi

# ---------------- 4. de-ess, compression ----------------
DYN_AF="anull"
[[ "$DEESS" != 0 ]] && DYN_AF+=",deesser=i=${DEESS}:m=0.5:f=0.5:s=o"
[[ "$COMP" == 1 ]] && DYN_AF+=",acompressor=threshold=-26dB:ratio=2:attack=20:release=250:knee=4:makeup=1:detection=rms:link=average"
ff -i "$W/03_mix.wav" -af "$DYN_AF" -c:a pcm_f32le "$W/04_dyn.wav"
T4=$(now)

# ---------------- 5. optional trim (leading/trailing only) ----------------
TRIM_DESC="off"
if [[ "$TRIM" == 1 ]]; then
  [[ -x "$PY" ]] || die "--trim needs the python venv ($PY)"
  B=$("$PY" -I "$BIN_DIR/vt_util.py" trim-bounds "$W/04_dyn.wav")
  if [[ "$B" == none ]]; then
    TRIM_DESC="nothing to trim"; mv "$W/04_dyn.wav" "$W/05_trim.wav"
  else
    read -r TS TE <<<"$B"
    FO=$(fcalc "$TE-$TS-0.03")
    ff -i "$W/04_dyn.wav" -af "atrim=start=$TS:end=$TE,asetpts=N/SR/TB,afade=t=in:d=0.015,afade=t=out:st=$FO:d=0.03" \
      -c:a pcm_f32le "$W/05_trim.wav"
    TRIM_DESC="kept ${TS}s..${TE}s of ${DUR}s"
  fi
else
  mv "$W/04_dyn.wav" "$W/05_trim.wav"
fi
T5=$(now)

# ---------------- 6. two-pass loudness normalisation ----------------
read -r M_I _ _ < <(measure "$W/05_trim.wav")
awk -v i="${M_I:--70}" 'BEGIN{exit !(i>-69)}' || die "processed signal is silent; nothing to normalise"
GAIN=$(fcalc "$TARGET-($M_I)")
LIM=$(fcalc "$TP-0.5")
for pass in 1 2 3; do
  ff -i "$W/05_trim.wav" -af "volume=${GAIN}dB,aresample=192000:resampler=soxr,alimiter=limit=${LIM}dB:attack=5:release=60:level=disabled:latency=1:asc=1,aresample=48000:resampler=soxr" \
    -c:a pcm_f32le "$W/06_norm.wav"
  read -r N_I N_LRA N_TP < <(measure "$W/06_norm.wav")
  DI=$(fcalc "$TARGET-($N_I)")
  OVER=$(awk -v p="$N_TP" -v t="$TP" 'BEGIN{d=p-t; printf "%.3f", (d>0?d:0)}')
  if awk -v d="$DI" -v o="$OVER" 'BEGIN{exit !((d<0.1 && d>-0.1) && o==0)}'; then break; fi
  GAIN=$(fcalc "$GAIN+$DI"); LIM=$(fcalc "$LIM-$OVER-0.1")
done
T6=$(now)

# ---------------- 7. outputs ----------------
ff -i "$W/06_norm.wav" -c:a pcm_s24le -ar 48000 "$OUT_WAV"
if [[ -z "$BITRATE" ]]; then if [[ "$AC" == 2 ]]; then BITRATE=192k; else BITRATE=128k; fi; fi
if [[ "$FORMAT" == m4a ]]; then
  ff -i "$W/06_norm.wav" -c:a aac -b:a "$BITRATE" -movflags +faststart "$OUT_C"
else
  ff -i "$W/06_norm.wav" -c:a libmp3lame -b:a "$BITRATE" "$OUT_C"
fi
read -r O_I O_LRA O_TP < <(measure "$OUT_WAV")
read -r C_I C_LRA C_TP < <(measure "$OUT_C")
T7=$(now)

TOTAL=$(fcalc "$T7-$T0")
PERMIN=$(awk -v t="$TOTAL" -v d="$DUR" 'BEGIN{printf "%.1f", (d>0? t/d*60 : 0)}')
{
  echo "polish_voice report"
  echo "input       : $IN_ABS"
  echo "              codec=$SRC_CODEC ${SRC_SR}Hz ch=$SRC_CH; processed ${DUR}s as $AC ch @48 kHz${START:+ from ${START}s}"
  echo "chain       : hp=${HP}Hz dehum=${DEHUM} pre-gain=${PRE_G}dB | denoise: $DN_DESC |"
  echo "              deess=${DEESS} comp=${COMP} | trim: $TRIM_DESC |"
  echo "              loudness target ${TARGET} LUFS, ceiling ${TP} dBTP (gain $(fmt1 "$GAIN") dB, limiter $(fmt1 "$LIM") dB)$([[ $DUALMONO == 1 ]] && echo ', dual-mono')"
  printf '%-14s %10s %10s %10s\n' "" "I (LUFS)" "LRA (LU)" "TP (dBTP)"
  printf '%-14s %10s %10s %10s\n' "before" "$(fmt1 "$IN_I")" "$(fmt1 "$IN_LRA")" "$(fmt1 "$IN_TP")"
  printf '%-14s %10s %10s %10s\n' "after (.wav)" "$(fmt1 "$O_I")" "$(fmt1 "$O_LRA")" "$(fmt1 "$O_TP")"
  printf '%-14s %10s %10s %10s\n' "after (.$CEXT)" "$(fmt1 "$C_I")" "$(fmt1 "$C_LRA")" "$(fmt1 "$C_TP")"
  awk -v a="$T1" -v b="$T2" -v c="$T3" -v d="$T4" -v e="$T5" -v f="$T6" -v g="$T7" -v z="$T0" \
    'BEGIN{printf "time (s)    : decode %.1f, pre %.1f, denoise %.1f, dyn %.1f, trim %.1f, loudness %.1f, encode %.1f\n", a-z,b-a,c-b,d-c,e-d,f-e,g-f}'
  echo "total       : ${TOTAL%.*}s wall for ${DUR}s audio (${PERMIN}s per audio-minute)"
  echo "outputs     : $OUT_WAV"
  echo "              $OUT_C"
} | tee "$OUT_REP"
