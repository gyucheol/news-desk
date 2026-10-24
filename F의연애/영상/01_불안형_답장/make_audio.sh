#!/usr/bin/env bash
# Sound for 01편 (2026-10-24): music (-36 LUFS, 3 s crossfades) + sound effects under the narration (-14 LUFS).
# Needs work/narration.wav (edit_narration.py) and the music/sfx files from fetch_stock.sh. Run with VIDEO_ROOT set.
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"; W="$VR/work"
T=723.608   # edit_log.json total
cd "$VR"    # bgm_segments.json keeps track paths relative to VIDEO_ROOT
python3 -I "$E/make_bgm_segments.py" "$E" "$VR" $T > /dev/null
"$PY" -I "$SC/bgm_sequence.py" "$E/bgm_segments.json" $T "$W/bgm.wav" --lufs -36 --fade-out 3.0
"$PY" -I "$E/make_sfx.py" "$E" "$VR" $T "$W/sfx.wav"
ffmpeg -v error -y -i "$W/bgm.wav" -i "$W/sfx.wav" -filter_complex \
  "[0:a]aresample=48000,aformat=channel_layouts=stereo[a];[1:a]aresample=48000,aformat=channel_layouts=stereo[b];[a][b]amix=inputs=2:duration=first:normalize=0[m]" \
  -map "[m]" -c:a pcm_f32le "$W/bed.wav"
"$PY" -I "$SC/mix_audio.py" "$W/narration.wav" "$W/bed.wav" "$W/final_audio.wav"
