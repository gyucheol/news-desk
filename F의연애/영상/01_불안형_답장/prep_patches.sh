#!/usr/bin/env bash
# Clips patched from the Mixkit originals that fetch_stock.sh downloads (F의 연애 01, 2026-10-24). Run with VIDEO_ROOT set.
# 39789p: 39789 from 0 to 5.6 s with the Apple logo on the phone back painted out (scene "9시 반이 되자,").
#   Start point (1566, 875) was read off the first frame by eye; logo_patch.py tracks it from there (lowest match 0.95)
#   and writes a check sheet next to the clip (39789p.mp4.png).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"
F="$VR/work/stock/full"
[ -s "$F/39789p.mp4" ] || "$VR/venv/bin/python" -I "$E/../scripts/logo_patch.py" "$F/39789.mp4" 0.0 5.6 1566 875 "$F/39789p.mp4" 30 20
