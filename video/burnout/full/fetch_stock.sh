#!/usr/bin/env bash
# Download the stock clips and music used in the full burnout episode, v5 (2026-10-23): 62 clips, 1 clip for a still,
# 8 tracks (Mixkit; every item page showed the Free license, checked 2026-10-22; 4801, 42834, 31416, 41192 on
# 2026-10-23). Individual files for this one video, not a bulk download.
# Output: ../work/stock/full/, ../work/stock/music/, ../work/stock/stills/ (the news photo of U233, cut from 41192)
set -euo pipefail
cd "$(dirname "$0")/.."            # video/burnout (since v2 this line read cd "./..", a shell-expansion slip)
mkdir -p work/stock/full work/stock/music work/stock/stills
get() {  # get <file> <url> [item page shown if the URL has changed]
  [ -s "$1" ] && return 0
  curl -sSf -A "Mozilla/5.0" -o "$1" "$2" || { rm -f "$1"; echo "failed: $1 ${3:-}"; }
  sleep 1
}
for id in 144 313 425 914 1013 1086 1623 1958 1967 2707 3428 3461 3977 4333 4397 4500 4511 4513 4548 4607 4701 4720 4766 4779 4801 4872 4893 4908 4915 8744 10395 21587 26090 28886 28893 28899 31411 31412 31413 31415 31416 39841 41192 42653 42655 42666 42834 42896 44579 50112 50133 50753 50754 50931 50956 51394 52452; do
  get work/stock/full/$id.mp4 "https://assets.mixkit.co/videos/$id/$id-1080.mp4"
done
get work/stock/full/99890.mp4 "https://assets.mixkit.co/active_storage/video_items/99890/1717186770/99890-video-1080.mp4" "https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/"
get work/stock/full/99909.mp4 "https://assets.mixkit.co/active_storage/video_items/99909/1717715134/99909-video-1080.mp4" "https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/"
get work/stock/full/99910.mp4 "https://assets.mixkit.co/active_storage/video_items/99910/1717715178/99910-video-1080.mp4" "https://mixkit.co/free-stock-video/beside-a-modern-laptop-the-hands-write-a-note-on-99910/"
get work/stock/full/100050.mp4 "https://assets.mixkit.co/active_storage/video_items/100050/1719877463/100050-video-1080.mp4" "https://mixkit.co/free-stock-video/woman-smiling-at-her-phone-on-a-cozy-couch-100050/"
get work/stock/full/100252.mp4 "https://assets.mixkit.co/active_storage/video_items/100252/1722543012/100252-video-1080.mp4" "https://mixkit.co/free-stock-video/pouring-tea-into-a-cup-on-a-rustic-table-setting-100252/"
get work/stock/full/100831.mp4 "https://assets.mixkit.co/umf3x8cqtqa7myln265ut0rmvcf7" "https://mixkit.co/free-stock-video/sky-transitioning-from-night-to-sunrise-100831/"
for id in 614 168 520 184 22 601 148 684; do
  get work/stock/music/$id.mp3 "https://assets.mixkit.co/music/$id/$id.mp3"
done
# v5: the news photo behind 작년 12월 / 31살 직장인 / 박 모 씨 (spec N01) is one frame of 41192 at 7.4 s
[ -s work/stock/stills/41192_7.4.png ] || ffmpeg -v error -y -ss 7.4 -i work/stock/full/41192.mp4 -frames:v 1 work/stock/stills/41192_7.4.png
ls work/stock/full | wc -l; ls work/stock/music work/stock/stills
