#!/usr/bin/env bash
# Stock clips and music for 01편 (Mixkit; each video's licence was read on its item page as "Free" on 2026-10-24,
# credits.md). Individual files for this one video, not a bulk download. Run with VIDEO_ROOT set.
# v2 (2026-10-24): "fetch_stock.sh v2" takes the clips of spec_v2.json and the music of bgm_plan_v2.json (run_v2.sh).
# v3 (2026-10-25): "fetch_stock.sh v3" takes the clips of spec_v3.json and the music of bgm_plan_v3.json (run_v3.sh).
# v4 (2026-10-25): "fetch_stock.sh v4" takes the clips of spec_v4.json and, as v3, the music of bgm_plan_v3.json.
# v5 (2026-10-25): "fetch_stock.sh v5" takes the clips of spec_v5.json (all of them v4 clips) and the v3 music.
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"
SPEC="$E/spec.json"; [ "${1:-}" = v2 ] && SPEC="$E/spec_v2.json"; [ "${1:-}" = v3 ] && SPEC="$E/spec_v3.json"; [ "${1:-}" = v4 ] && SPEC="$E/spec_v4.json"; [ "${1:-}" = v5 ] && SPEC="$E/spec_v5.json"
mkdir -p "$VR/work/stock/full" "$VR/work/stock/music" "$VR/work/stock/sfx"
get() {  # get <file> <url> [fallback url]
  [ -s "$1" ] && return 0
  curl -sSf -A "Mozilla/5.0" -o "$1" "$2" 2>/dev/null || { [ -n "${3:-}" ] && curl -sSf -A "Mozilla/5.0" -o "$1" "$3"; } \
    || { rm -f "$1"; echo "failed: $1"; }
  sleep 1
}
for id in $(python3 -I -c "
import json; sp = json.load(open('$SPEC'))
print(' '.join(sorted({s['src'].split('/')[-1][:-4].rstrip('p') for s in sp['scenes'] if s['type'] == 'video'}, key=int)))"); do  # 39789p -> 39789
  case $id in
    100050) get "$VR/work/stock/full/$id.mp4" https://assets.mixkit.co/active_storage/video_items/100050/1719877463/100050-video-1080.mp4 https://assets.mixkit.co/active_storage/video_items/100050/1719877463/100050-video-720.mp4 ;;
    100053) get "$VR/work/stock/full/$id.mp4" https://assets.mixkit.co/active_storage/video_items/100053/1719877679/100053-video-1080.mp4 https://assets.mixkit.co/active_storage/video_items/100053/1719877679/100053-video-720.mp4 ;;
    99890)  get "$VR/work/stock/full/$id.mp4" https://assets.mixkit.co/active_storage/video_items/99890/1717186770/99890-video-1080.mp4 https://assets.mixkit.co/active_storage/video_items/99890/1717186770/99890-video-720.mp4 ;;
    100530) get "$VR/work/stock/full/$id.mp4" https://assets.mixkit.co/active_storage/video_items/100530/1725383823/100530-video-1080.mp4 https://assets.mixkit.co/active_storage/video_items/100530/1725383823/100530-video-720.mp4 ;;
    100067) get "$VR/work/stock/full/$id.mp4" https://assets.mixkit.co/active_storage/video_items/100067/1719879296/100067-video-1080.mp4 https://assets.mixkit.co/active_storage/video_items/100067/1719879296/100067-video-720.mp4 ;;
    101412) get "$VR/work/stock/full/$id.mp4" https://assets.mixkit.co/velf42fpvovrylmrk7nh31o1i87u ;;
    101233) get "$VR/work/stock/full/$id.mp4" https://assets.mixkit.co/0drms4nl2c7hmg5b2towk3wsm2zf ;;
    *)      get "$VR/work/stock/full/$id.mp4" "https://assets.mixkit.co/videos/$id/$id-1080.mp4" "https://assets.mixkit.co/videos/$id/$id-720.mp4" ;;
  esac
done
MUSIC="493 41 615 168 681 310 713 682 1081"
[ "${1:-}" = v2 ] && MUSIC=$(python3 -I -c "import json; print(' '.join(p['mixkit'] for p in json.load(open('$E/bgm_plan_v2.json'))))")
[ "${1:-}" = v3 -o "${1:-}" = v4 -o "${1:-}" = v5 ] && MUSIC=$(python3 -I -c "import json; print(' '.join(sorted({p['mixkit'] for p in json.load(open('$E/bgm_plan_v3.json'))})))")
for id in $MUSIC; do
  get "$VR/work/stock/music/$id.mp3" "https://assets.mixkit.co/music/$id/$id.mp3"
done
for id in 2354 2357 1395 1050 2365; do
  get "$VR/work/stock/sfx/$id.mp3" "https://assets.mixkit.co/active_storage/sfx/$id/$id-preview.mp3"
done
"$E/prep_patches.sh"   # copies with a logo painted out (39789p)
ls "$VR/work/stock/full" | wc -l
