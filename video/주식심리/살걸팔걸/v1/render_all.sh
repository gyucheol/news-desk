#!/usr/bin/env bash
# 살걸·팔걸 편 v1: 화면 렌더링(3 프로세스) -> 소리 붙이기 -> 장면 점검 시트 (run_v1.sh 6~7단계와 같음)
set -euo pipefail
S=/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad
W="$S/salgeol/v1"; SC="$S/ep4/tools/scripts"; PY="$S/venv/bin/python"
cd "$W"
date -u +"render start %H:%M:%S"
(cd "$S" && VIDEO_ROOT="$S" "$PY" "$SC/render_parallel.py" "$W/timeline.json" "$W/salgeol_video.mp4" 3 --video-only)
date -u +"render done %H:%M:%S"
ffmpeg -v error -y -i salgeol_video.mp4 -i audio/final_audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 \
  -movflags +faststart 살걸팔걸_v1.mp4
date -u +"mux done %H:%M:%S"
mkdir -p chk/scenes
"$PY" -I scene_sheet.py 살걸팔걸_v1.mp4 chk/scenes
date -u +"sheets done %H:%M:%S"
