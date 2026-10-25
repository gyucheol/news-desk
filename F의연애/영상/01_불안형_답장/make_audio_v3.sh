#!/usr/bin/env bash
# Sound for 01편 v3 (2026-10-25): the v3 music (bgm_plan_v3.json, -36 LUFS, one constant gain per track, 3 s
# crossfades) + the v2 sound effects (make_sfx_v3.py) under the v2 narration (work/v2/narration.wav, -14 LUFS), then
# the mix at -14 LUFS (mix_audio.py: one constant gain and a peak limiter). Run with VIDEO_ROOT set.
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
N="$VR/work/v2/narration.wav"; V="$VR/work/v3"
mkdir -p "$V"
T=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$N")
cd "$VR"    # the music plan keeps track paths relative to VIDEO_ROOT
python3 -I "$E/make_bgm_segments_v3.py" "$E" "$T"
"$PY" -I "$SC/bgm_sequence.py" "$E/bgm_segments_v3.json" "$T" "$V/bgm.wav" --lufs -36 --fade-out 3.0 --constant
"$PY" -I "$E/make_sfx_v3.py" "$E" "$VR" "$T" "$V/sfx.wav" "$E/sfx_log_v3.json"
ffmpeg -v error -y -i "$V/bgm.wav" -i "$V/sfx.wav" -filter_complex \
  "[0:a]aresample=48000,aformat=channel_layouts=stereo[a];[1:a]aresample=48000,aformat=channel_layouts=stereo[b];[a][b]amix=inputs=2:duration=first:normalize=0[m]" \
  -map "[m]" -c:a pcm_f32le "$V/bed.wav"
"$PY" -I "$SC/mix_audio.py" "$N" "$V/bed.wav" "$V/final_audio.wav"
