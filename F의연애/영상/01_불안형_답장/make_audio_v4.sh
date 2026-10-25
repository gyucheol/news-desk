#!/usr/bin/env bash
# Sound for 01편 v4 (2026-10-25): the v4 narration (work/v4/narration.wav = the v2 narration with the sigh before
# '내가 연락을 너무 재촉하는 것처럼' cut, edit_narration_v4.py, -14 LUFS) + v3's music (bgm_plan_v3.json, -36 LUFS, one
# constant gain per track, 3 s crossfades, placed on the v4 times) + the sound effects (make_sfx_v4.py: v3's without the
# pop at '뭐 할껀 없어'), then the mix at -14 LUFS (mix_audio.py: one constant gain and a peak limiter).
# Run with VIDEO_ROOT set, after edit_narration_v4.py (run_v4.sh step 1).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
N="$VR/work/v4/narration.wav"; V="$VR/work/v4"
mkdir -p "$V"
T=$(ffprobe -v error -show_entries format=duration -of csv=p=0 "$N")
cd "$VR"    # the music plan keeps track paths relative to VIDEO_ROOT
python3 -I "$E/make_bgm_segments_v4.py" "$E" "$T"
"$PY" -I "$SC/bgm_sequence.py" "$E/bgm_segments_v4.json" "$T" "$V/bgm.wav" --lufs -36 --fade-out 3.0 --constant
"$PY" -I "$E/make_sfx_v4.py" "$E" "$VR" "$T" "$V/sfx.wav" "$E/sfx_log_v4.json"
ffmpeg -v error -y -i "$V/bgm.wav" -i "$V/sfx.wav" -filter_complex \
  "[0:a]aresample=48000,aformat=channel_layouts=stereo[a];[1:a]aresample=48000,aformat=channel_layouts=stereo[b];[a][b]amix=inputs=2:duration=first:normalize=0[m]" \
  -map "[m]" -c:a pcm_f32le "$V/bed.wav"
"$PY" -I "$SC/mix_audio.py" "$N" "$V/bed.wav" "$V/final_audio.wav"
