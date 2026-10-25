#!/usr/bin/env bash
# Sound for 01편 v6 (2026-10-25): the v6 narration (work/v6/narration.wav: the owner's new recordings 1-8, joined and
# edited by join_narration_v6.py and edit_narration_v6.py, -14 LUFS) + the v3 music (bgm_plan_v3.json, -36 LUFS, one
# constant gain per track, 3 s crossfades) and v4's sound effects, both placed on the v6 times, then the mix at
# -14 LUFS (mix_audio.py: one constant gain and a peak limiter). Run with VIDEO_ROOT set (run_v6.sh step 4).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
N="$VR/work/v6/narration.wav"; V="$VR/work/v6"
mkdir -p "$V"
T=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$N")
cd "$VR"    # the music plan keeps track paths relative to VIDEO_ROOT
python3 -I "$E/make_bgm_segments_v6.py" "$E" "$T"
"$PY" -I "$SC/bgm_sequence.py" "$E/bgm_segments_v6.json" "$T" "$V/bgm.wav" --lufs -36 --fade-out 3.0 --constant
"$PY" -I "$E/make_sfx_v6.py" "$E" "$VR" "$T" "$V/sfx.wav" "$E/sfx_log_v6.json"
ffmpeg -v error -y -i "$V/bgm.wav" -i "$V/sfx.wav" -filter_complex \
  "[0:a]aresample=48000,aformat=channel_layouts=stereo[a];[1:a]aresample=48000,aformat=channel_layouts=stereo[b];[a][b]amix=inputs=2:duration=first:normalize=0[m]" \
  -map "[m]" -c:a pcm_f32le "$V/bed.wav"
"$PY" -I "$SC/mix_audio.py" "$N" "$V/bed.wav" "$V/final_audio.wav"
