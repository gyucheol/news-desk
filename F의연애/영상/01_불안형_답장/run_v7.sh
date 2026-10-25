#!/usr/bin/env bash
# 01편 v7 (2026-10-25): v6 with the owner's v7 list 1-12 (credits_v7.md). Run from anywhere with VIDEO_ROOT set, after
# run_v6.sh (v7 starts from the v6 narration, work/v6/narration.wav, and its syllable alignment, work/v6/align_ctc.json;
# the owner's photos, stock and music are there from run_v5.sh/run_v6.sh).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
V="$VR/work/v7"
mkdir -p "$V" "$VR/work/owner_v7" "$VR/out"

# 1. the narration: v6's without '밤 11시 50분 … 나란히 떠 있습니다.' (list 4), and the v7 subtitles
"$PY" -I "$E/edit_narration_v7.py" "$VR/work/v6/narration.wav" "$E/lines_v6.json" "$E/lines_align_v6.json" \
  "$V/narration.wav" "$E/edit_log_v7.json"
"$PY" -I "$SC/make_lines.py" "$E" subtitles_v7.txt lines_v7.json

# 2. line times: v6's, moved; the second parts of the two split lines found on the v7 narration (onsets_v2.py)
"$PY" -I "$E/make_align_v7.py" ctc "$E" "$VR/work/v6/align_ctc.json" "$V/align_ctc.json"
"$PY" -I "$SC/onsets_v2.py" "$V/narration.wav" "$V/align_ctc.json" "$E/lines_v7.json" "$V/onsets_v2.json"
"$PY" -I "$E/make_align_v7.py" final "$E" "$V/onsets_v2.json"

# 3. sound: the v3 music and the effects left in v7 on the v7 times, mix at -14 LUFS
"$E/make_audio_v7.sh"

# 4. pictures: photo 7 with the typed words softened (list 10), the v7 plan, timeline, render, then the sound
"$PY" -I "$E/make_photos_v7.py" "$VR/work/owner_v3/07.png" "$VR/work/owner_v7/07.png"
"$PY" -I "$E/build_spec_v7.py" "$E" "$VR"
"$E/fetch_stock.sh" v7
"$PY" -I "$SC/build_timeline.py" "$V/spec_abs.json" "$E/lines_align_v7.json" "$V/final_audio.wav" "$V/timeline.json" \
  "$E/lines_align_v7.json" > "$V/timeline.log"
"$PY" -I "$SC/fit_clips.py" "$V/timeline.json"
cd "$VR"
"$PY" "$SC/render_parallel.py" "$V/timeline.json" "$VR/out/01_v7_video.mp4" 3 --video-only
ffmpeg -v error -y -i "$VR/out/01_v7_video.mp4" -i "$V/final_audio.wav" -map 0:v -map 1:a -c:v copy \
  -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart "$VR/out/01_불안형_답장_v7.mp4"
