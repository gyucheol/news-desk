#!/usr/bin/env bash
# speedup_voice.sh - speed up a spoken-voice recording without changing the pitch
# and level it for YouTube (optional clean-up with --clean). Works on audio files
# and on videos (a video is sped up by the same factor so picture and sound stay in sync).
#
# Usage: speedup_voice.sh [options] -o OUTDIR INPUT
#   -s SPEED      tempo factor (default 1.2; 0.5-2.0)
#   -t LUFS       final loudness, measured as stereo playback (default -14)
#   --clean       add clean-up (denoise / high-pass / compression). Off by default:
#                 the user chose speed + loudness only (no tone or noise changes).
#   --plain       no clean-up (the default; kept for compatibility)
#   --rb          time-stretch with rubberband instead of atempo (WSOLA)
#   --preset P    x264 preset for video output (default veryfast; same CRF quality, bigger file)
#   --af CHAIN    extra ffmpeg audio filters (e.g. tone EQ) applied before the speed change
#   -o OUTDIR     output directory (required). The input is never modified.
set -euo pipefail

BIN_DIR="$(cd "$(dirname "$(readlink -f "${BASH_SOURCE[0]}")")" && pwd)"
POLISH="$BIN_DIR/polish_voice.sh"

SPEED=1.2; TARGET=-14; PLAIN=1; ENGINE=atempo; PRESET=veryfast; OUTDIR=""; EXTRA_AF=""
while [[ $# -gt 0 ]]; do
  case "$1" in
    -s) SPEED="$2"; shift 2;;
    -t) TARGET="$2"; shift 2;;
    --plain) PLAIN=1; shift;;
    --clean) PLAIN=0; shift;;
    --rb) ENGINE=rubberband; shift;;
    --preset) PRESET="$2"; shift 2;;
    --af) EXTRA_AF="$2"; shift 2;;
    -o) OUTDIR="$2"; shift 2;;
    -h|--help) sed -n '2,15p' "$0"; exit 0;;
    -*) echo "unknown option: $1" >&2; exit 2;;
    *) break;;
  esac
done
IN="${1:-}"
if [[ -z "$IN" || ! -f "$IN" || -z "$OUTDIR" ]]; then
  echo "usage: $(basename "$0") [-s 1.2] [-t -14] [--plain] [--rb] -o OUTDIR INPUT" >&2; exit 2
fi
awk -v s="$SPEED" 'BEGIN{exit !(s>=0.5 && s<=2.0)}' || { echo "speed must be 0.5-2.0" >&2; exit 2; }

mkdir -p "$OUTDIR"
WORK="$(mktemp -d "$OUTDIR/.work.XXXXXX")"
trap 'rm -rf -- "${WORK:?}"' EXIT

# Output name that never overwrites an existing file.
base="$(basename "${IN%.*}")_x${SPEED}"
name="$base"; k=2
while [[ -e "$OUTDIR/$name.wav" || -e "$OUTDIR/$name.m4a" || -e "$OUTDIR/$name.mp4" ]]; do name="${base}_$k"; k=$((k+1)); done

has_video=0
if ffprobe -v error -select_streams v:0 -show_entries stream=codec_type -of csv=p=0 "$IN" | grep -q video; then
  # Ignore embedded cover art (attached pictures) in audio files.
  pic="$(ffprobe -v error -select_streams v:0 -show_entries stream_disposition=attached_pic -of csv=p=0 "$IN" || true)"
  [[ "$pic" == *1* ]] || has_video=1
fi

t0=$(date +%s)
# 1) Clean-up chain (or plain decode). Level is fixed again after the speed change.
if [[ $PLAIN == 1 ]]; then
  ffmpeg -v error -i "$IN" -vn -ac 1 -ar 48000 -c:a pcm_f32le "$WORK/a.wav"
else
  "$POLISH" -t -23 -o "$WORK" -n a "$IN" > "$WORK/polish_log.txt" 2>&1 || { cat "$WORK/polish_log.txt" >&2; exit 1; }
fi

# 1b) Optional extra filters (e.g. tone EQ), still at the original speed.
if [[ -n "$EXTRA_AF" ]]; then
  ffmpeg -v error -i "$WORK/a.wav" -af "$EXTRA_AF" -c:a pcm_f32le "$WORK/a_eq.wav"
  mv -- "$WORK/a_eq.wav" "$WORK/a.wav"
fi

# 2) Speed change with pitch preserved.
if [[ $ENGINE == atempo ]]; then AF="atempo=$SPEED"; else AF="rubberband=tempo=$SPEED"; fi
ffmpeg -v error -i "$WORK/a.wav" -af "$AF" -c:a pcm_f32le "$WORK/b.wav"

# 3) Final loudness (measured as heard on stereo) with true-peak limiting.
"$POLISH" -d none --hp 0 --no-comp --dual-mono -t "$TARGET" -o "$WORK" -n c "$WORK/b.wav" > "$WORK/final_log.txt" 2>&1 \
  || { cat "$WORK/final_log.txt" >&2; exit 1; }

# 4) Deliverables: stereo (dual-mono) WAV + AAC, and the sped-up video if the input had one.
ffmpeg -v error -i "$WORK/c.wav" -af "pan=stereo|c0=c0|c1=c0" -c:a pcm_s24le "$OUTDIR/$name.wav"
ffmpeg -v error -i "$OUTDIR/$name.wav" -c:a aac -b:a 192k -movflags +faststart "$OUTDIR/$name.m4a"
if [[ $has_video == 1 ]]; then
  fps="$(ffprobe -v error -select_streams v:0 -show_entries stream=avg_frame_rate -of csv=p=0 "$IN")"
  [[ -z "$fps" || "$fps" == 0/0 ]] && fps="$(ffprobe -v error -select_streams v:0 -show_entries stream=r_frame_rate -of csv=p=0 "$IN")"
  ffmpeg -v error -i "$IN" -i "$OUTDIR/$name.wav" -map 0:v:0 -map 1:a:0 \
    -filter:v "setpts=PTS/$SPEED" -r "$fps" -c:v libx264 -preset "$PRESET" -crf 18 -pix_fmt yuv420p \
    -c:a aac -b:a 192k -movflags +faststart -shortest "$OUTDIR/$name.mp4"
fi
t1=$(date +%s)

dur() { ffprobe -v error -show_entries format=duration -of csv=p=0 "$1"; }
loud() { ffmpeg -hide_banner -nostats -i "$1" -map 0:a:0 -af ebur128=peak=true -f null - 2>&1 | awk '/I:/{i=$2} /Peak:/{p=$2} END{printf "%s LUFS, true peak %s dBTP", i, p}'; }
echo "input   : $IN ($(printf '%.1f' "$(dur "$IN")") s)"
echo "settings: speed x$SPEED ($ENGINE), clean-up $([[ $PLAIN == 1 ]] && echo off || echo on), target $TARGET LUFS${EXTRA_AF:+, extra filters: $EXTRA_AF}"
for f in "$OUTDIR/$name.wav" "$OUTDIR/$name.m4a" $([[ $has_video == 1 ]] && echo "$OUTDIR/$name.mp4"); do
  echo "output  : $f ($(printf '%.2f' "$(dur "$f")") s; $(loud "$f"))"
done
echo "time    : $((t1 - t0)) s"
