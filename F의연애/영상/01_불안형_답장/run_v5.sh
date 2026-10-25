#!/usr/bin/env bash
# 01편 v5 (2026-10-25, the owner's v5 request): v4 with the owner's second set of AI photos (29) on the lines their
# script marks "<대사>(N)", and photo 27 softened under centre text at both of its places (credits_v5.md). The
# narration, music and effects are v4's (work/v4/final_audio.wav), so run this after run_v4.sh. Run from anywhere with
# VIDEO_ROOT set. The owner's photos come only as chat attachments and are not committed: put the 29 webp files in
# work/owner_v5/raw/ first, named b<message>_<index>_<first 8 of md5>.webp (credits_v5.md 3장).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
W="$VR/work"; V="$W/v5"
mkdir -p "$V" "$VR/out"

# 1. the owner's photos: the white star mark off (owner_wm_remove.py), the black bars of photos 4 and 21 off, numbered
#    by what each photo shows (make_photos_v5.py)
"$PY" -I "$SC/owner_wm_remove.py" "$W/owner_v5/raw" "$V/wm_alpha.npy" "$W/owner_v5/clean" "$V/wm_sheet.png"
"$PY" -I "$E/make_photos_v5.py" "$W/owner_v5/clean" "$W/owner_v5"

# 2. subtitles v5 (subtitles_v5.txt: four lines moved to the centre) with v4's checked times
"$PY" -I "$SC/make_lines.py" "$E" subtitles_v5.txt lines_v5.json
"$PY" -I "$E/make_align_v5.py" "$E"

# 3. the scene plan (every clip is a v4 clip)
"$PY" -I "$E/build_spec_v5.py" "$E" "$VR"
"$E/fetch_stock.sh" v5

# 4. timeline, picture (render.py loads the icon modules next to it: no -I), then v4's sound (AAC 320 kbps, no -shortest)
"$PY" -I "$SC/build_timeline.py" "$V/spec_abs.json" "$E/lines_align_v5.json" "$W/v4/final_audio.wav" "$V/timeline.json" \
  "$E/lines_align_v5.json" > "$V/timeline.log"
"$PY" -I "$SC/fit_clips.py" "$V/timeline.json"
(cd "$VR" && "$PY" "$SC/render_parallel.py" "$V/timeline.json" "$VR/out/01_v5_video.mp4" 3 --video-only)
ffmpeg -v error -y -i "$VR/out/01_v5_video.mp4" -i "$W/v4/final_audio.wav" -map 0:v -map 1:a -c:v copy \
  -c:a aac -b:a 320k -ar 48000 -ac 2 -movflags +faststart "$VR/out/01_불안형_답장_v5.mp4"
