#!/usr/bin/env bash
# Download the stock clips and music used in sample30 (Mixkit, Free licenses verified 2026-10-22).
# A handful of individual files, not a bulk download. Output: ../work/stock/full/, ../work/stock/music/
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p work/stock/full work/stock/music
for id in 31411 28899 4548 51394 4701 4511 4333 144; do
  [ -s work/stock/full/$id.mp4 ] || curl -sSf -A "Mozilla/5.0" -o work/stock/full/$id.mp4 "https://assets.mixkit.co/videos/$id/$id-1080.mp4"
  sleep 1
done
[ -s work/stock/full/99909.mp4 ] || curl -sSf -A "Mozilla/5.0" -o work/stock/full/99909.mp4 \
  "https://assets.mixkit.co/active_storage/video_items/99909/1717715134/99909-video-1080.mp4" || \
  echo "99909: URL changed - see https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/"
[ -s work/stock/music/614.mp3 ] || curl -sSf -A "Mozilla/5.0" -o work/stock/music/614.mp3 "https://assets.mixkit.co/music/614/614.mp3"
ls -la work/stock/full work/stock/music
