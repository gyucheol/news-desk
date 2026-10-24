#!/usr/bin/env bash
# Sound for 01편 v2 (2026-10-24): music (-36 LUFS, one constant gain per track, 3 s crossfades) + sound effects under
# the narration v2 (edit_narration_v2.py, -14 LUFS), then the mix at -14 LUFS (mix_audio.py: one constant gain and a
# peak limiter). Needs work/v2/narration.wav and the music/sfx files from fetch_stock.sh. Run with VIDEO_ROOT set.
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"; V="$VR/work/v2"
T=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$V/narration.wav")
cd "$VR"    # the music plan keeps track paths relative to VIDEO_ROOT
python3 -I "$E/make_bgm_segments_v2.py" "$E" "$T"
"$PY" -I "$SC/bgm_sequence.py" "$E/bgm_segments_v2.json" "$T" "$V/bgm.wav" --lufs -36 --fade-out 3.0 --constant
"$PY" -I "$E/make_sfx_v2.py" "$E" "$VR" "$T" "$V/sfx.wav" "$E/sfx_log_v2.json"
ffmpeg -v error -y -i "$V/bgm.wav" -i "$V/sfx.wav" -filter_complex \
  "[0:a]aresample=48000,aformat=channel_layouts=stereo[a];[1:a]aresample=48000,aformat=channel_layouts=stereo[b];[a][b]amix=inputs=2:duration=first:normalize=0[m]" \
  -map "[m]" -c:a pcm_f32le "$V/bed.wav"
"$PY" -I "$SC/mix_audio.py" "$V/narration.wav" "$V/bed.wav" "$V/final_audio.wav"
