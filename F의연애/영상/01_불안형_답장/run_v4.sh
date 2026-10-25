#!/usr/bin/env bash
# 01편 v4 (2026-10-25, the owner's v4 list 1-52): v3 with the sigh before '내가 연락을 너무 재촉하는 것처럼' cut from the
# narration, no yellow words, lines moved to or from the centre, the previous shot running on under the chat lines
# and other centre lines, the owner's photos placed again where the list says, the chat screens lined up, and one
# sound effect less (credits_v4.md). Run from anywhere with VIDEO_ROOT set, after run_v3.sh (v4 uses
# work/v2/narration.wav, work/owner_v3/NN.png and the v3 stock and music).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
W="$VR/work"; V="$W/v4"
mkdir -p "$V" "$VR/out"

# 1. narration: the v2 narration with the sigh cut (every time after it is 0.527 s earlier, cut_v4.json)
"$PY" -I "$E/edit_narration_v4.py" "$W/v2/narration.wav" "$V/narration.wav" "$V/cut_v4.json"

# 2. subtitles v4 (subtitles_v4.txt -> lines_v4.json) and their times: v3's checked times moved by the cut
"$PY" -I "$SC/make_lines.py" "$E" subtitles_v4.txt lines_v4.json
"$PY" -I "$E/make_align_v4.py" "$E" "$V/cut_v4.json"

# 3. the scene plan (the stock and music are v3's)
"$PY" -I "$E/build_spec_v4.py" "$E" "$VR"
"$E/fetch_stock.sh" v4

# 4. sound: v4 narration, v3 music, v4 effects, mix (-14 LUFS)
"$E/make_audio_v4.sh"

# 5. timeline, picture (render.py loads the icon modules next to it: no -I), then the sound once (AAC 320 kbps; no
#    -shortest: the sound is a few ms shorter than the last frame and -shortest dropped that frame in v3)
"$PY" -I "$SC/build_timeline.py" "$V/spec_abs.json" "$E/lines_align_v4.json" "$V/final_audio.wav" "$V/timeline.json" \
  "$E/lines_align_v4.json" > "$V/timeline.log"
"$PY" -I "$SC/fit_clips.py" "$V/timeline.json"
(cd "$VR" && "$PY" "$SC/render_parallel.py" "$V/timeline.json" "$VR/out/01_v4_video.mp4" 3 --video-only)
ffmpeg -v error -y -i "$VR/out/01_v4_video.mp4" -i "$V/final_audio.wav" -map 0:v -map 1:a -c:v copy \
  -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart "$VR/out/01_불안형_답장_v4.mp4"
