#!/usr/bin/env bash
# Download the stock clips and music used in the full burnout episode (Mixkit; every item page showed the Free license, checked 2026-10-22).
# Individual files for this one video, not a bulk download. Output: ../work/stock/full/, ../work/stock/music/
set -euo pipefail
cd "$(dirname "$0")/.."
mkdir -p work/stock/full work/stock/music
get() {  # get <file> <url> [item page shown if the URL has changed]
  [ -s "$1" ] && return 0
  curl -sSf -A "Mozilla/5.0" -o "$1" "$2" || { rm -f "$1"; echo "failed: $1 ${3:-}"; }
  sleep 1
}
for id in 31411 28899 4548 51394 4701 4511 4333 144 1623 4872 3428 26091 31413 42653 50931 42896 4513 10395 42343 3429 28886 4779 39841 44579 3461 31414 425 28893 1967 4766 4607 8744 2707 21587 50956 50133 1964 4835 914 4915 50753 50754 26090 42666 4908 4720 31412 4893 313 4500 42655 1958 1013 31415 26089 3977 50112 52452 4397 1086; do
  get work/stock/full/$id.mp4 "https://assets.mixkit.co/videos/$id/$id-1080.mp4"
done
get work/stock/full/99909.mp4 "https://assets.mixkit.co/active_storage/video_items/99909/1717715134/99909-video-1080.mp4" "https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/"
get work/stock/full/100050.mp4 "https://assets.mixkit.co/active_storage/video_items/100050/1719877463/100050-video-1080.mp4" "https://mixkit.co/free-stock-video/woman-smiling-at-her-phone-on-a-cozy-couch-100050/"
get work/stock/full/99890.mp4 "https://assets.mixkit.co/active_storage/video_items/99890/1717186770/99890-video-1080.mp4" "https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/"
get work/stock/full/100252.mp4 "https://assets.mixkit.co/active_storage/video_items/100252/1722543012/100252-video-1080.mp4" "https://mixkit.co/free-stock-video/pouring-tea-into-a-cup-on-a-rustic-table-setting-100252/"
get work/stock/full/99910.mp4 "https://assets.mixkit.co/active_storage/video_items/99910/1717715178/99910-video-1080.mp4" "https://mixkit.co/free-stock-video/beside-a-modern-laptop-the-hands-write-a-note-on-99910/"
get work/stock/full/100831.mp4 "https://assets.mixkit.co/umf3x8cqtqa7myln265ut0rmvcf7" "https://mixkit.co/free-stock-video/sky-transitioning-from-night-to-sunrise-100831/"
for id in 614 168 520 184 22 601 148 684; do
  get work/stock/music/$id.mp3 "https://assets.mixkit.co/music/$id/$id.mp3"
done
ls work/stock/full | wc -l; ls work/stock/music
