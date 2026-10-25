#!/usr/bin/env bash
# 01편 v6 (2026-10-25): v5's video on the owner's new recordings 1-8 ("녹음본 1~8번까지 내가 속도를 약간 올려서
# 녹음해왔음. 이 녹음본으로 적용해줘."). The recordings are joined, the sigh before '내가 연락을 너무 재촉하는 것처럼' is
# taken out and the pauses are shortened by the v2 rules; every subtitle line is aligned again; the music and sound
# effects follow the new times; the pictures are v5's plan (credits_v6.md). Run from anywhere with VIDEO_ROOT set,
# after run_v5.sh (the owner's photos, stock and music are there). The recordings come only as chat attachments and are
# not committed (the operator's voice): put them in work/rec_v6/in/rec1.m4a .. rec8.m4a first, in the owner's order.
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
W="$VR/work"; V="$W/v6"; R="$W/rec_v6"
mkdir -p "$V" "$R/wav" "$VR/out"
cd "$VR"                                   # ctc_align.py reads models/ relative to VIDEO_ROOT

# 1. the recordings: 48 kHz mono WAV (both channels carry the same sound), recognised once each (whisper large-v3)
for i in 1 2 3 4 5 6 7 8; do
  ffmpeg -v error -y -i "$R/in/rec$i.m4a" -ac 1 -ar 48000 -c:a pcm_f32le "$R/wav/part$i.wav"
  "$PY" -I "$SC/transcribe.py" "$R/wav/part$i.wav" "$R/part${i}_words.json" 4 > "$R/part${i}_asr.log"
done

# 2. joined narration (0.20 s lead-in, 0.50 s between recordings) and the v6 subtitles
"$PY" -I "$E/join_narration_v6.py" "$R/wav" "$V/joined.wav" "$V/join_log.json"
"$PY" -I "$SC/make_lines.py" "$E" subtitles_v6.txt lines_v6.json
"$PY" -I -c "
import json; L=json.load(open('$E/lines_v6.json'))
json.dump([{'id':o['id'],'text':o['spoken']} for o in L], open('$V/units_disp.json','w'), ensure_ascii=False, indent=1)"
WORDS=$(python3 -I -c "
import json; d=json.load(open('$V/join_log.json')); print(' '.join(f\"$R/part{p['part']}_words.json:{p['start']}\" for p in d['parts']))")

# 3. line starts on the joined narration (to tell sentence, section and in-line pauses apart, as v2 did)
"$PY" -I "$SC/align_words.py" "$V/units_disp.json" "$V/align_rough.json" $WORDS
"$PY" -I "$SC/onsets.py" "$V/joined.wav" "$V/align_rough.json" "$V/onsets_j.json"
"$PY" -I -c "
import json; say={o['id']:o['say'] for o in json.load(open('$E/lines_v6.json'))}
U=json.load(open('$V/onsets_j.json'))
for u in U: u['shown']=u['text']; u['text']=say[u['id']]
json.dump(U, open('$V/onsets_say_j.json','w'), ensure_ascii=False, indent=1)"
"$PY" -I "$SC/ctc_align.py" "$V/joined.wav" "$V/onsets_say_j.json" models/w2v_ko "$V/align_ctc_j.json"
"$PY" -I "$SC/onsets_v2.py" "$V/joined.wav" "$V/align_ctc_j.json" "$E/lines_v6.json" "$V/onsets_v2_j.json"

# 4. the narration: sigh out (sigh_v6.json), pauses shortened, 3 s after the last word, -14 LUFS
"$PY" -I "$E/edit_narration_v6.py" "$V/joined.wav" "$E/lines_v6.json" "$V/onsets_v2_j.json" "$E/sigh_v6.json" \
  "$V/narration.wav" "$V/timemap.json" "$E/edit_log_v6.json"

# 5. line times on the edited narration (as run_v2.sh step 3), then make_align_v6.py
"$PY" -I "$SC/map_words.py" "$V/timemap.json" "$V/words.json" $WORDS
"$PY" -I "$SC/align_words.py" "$V/units_disp.json" "$V/align.json" "$V/words.json:0"
"$PY" -I "$SC/onsets.py" "$V/narration.wav" "$V/align.json" "$V/onsets.json"
"$PY" -I -c "
import json; say={o['id']:o['say'] for o in json.load(open('$E/lines_v6.json'))}
U=json.load(open('$V/onsets.json'))
for u in U: u['shown']=u['text']; u['text']=say[u['id']]
json.dump(U, open('$V/onsets_say.json','w'), ensure_ascii=False, indent=1)"
"$PY" -I "$SC/ctc_align.py" "$V/narration.wav" "$V/onsets_say.json" models/w2v_ko "$V/align_ctc.json"
"$PY" -I "$SC/onsets_v2.py" "$V/narration.wav" "$V/align_ctc.json" "$E/lines_v6.json" "$V/onsets_v2.json"
"$PY" -I "$E/make_align_v6.py" "$E" "$V/onsets_v2.json" "$V/onsets_v2_j.json" "$V/timemap.json"

# 6. sound: v3 music and v4 effects on the v6 times, mix at -14 LUFS
"$E/make_audio_v6.sh"

# 7. pictures (v5's plan, every clip a v4 clip), timeline, render, then the sound (AAC 320 kbps, no -shortest)
"$PY" -I "$E/build_spec_v6.py" "$E" "$VR"
"$E/fetch_stock.sh" v6
"$PY" -I "$SC/build_timeline.py" "$V/spec_abs.json" "$E/lines_align_v6.json" "$V/final_audio.wav" "$V/timeline.json" \
  "$E/lines_align_v6.json" > "$V/timeline.log"
"$PY" -I "$SC/fit_clips.py" "$V/timeline.json"
"$PY" "$SC/render_parallel.py" "$V/timeline.json" "$VR/out/01_v6_video.mp4" 3 --video-only
ffmpeg -v error -y -i "$VR/out/01_v6_video.mp4" -i "$V/final_audio.wav" -map 0:v -map 1:a -c:v copy \
  -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart "$VR/out/01_불안형_답장_v6.mp4"
