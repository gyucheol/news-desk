set -e
S=/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad
cd $S/salgeol/v1
for n in 1 2 3; do
  VIDEO_ROOT=$S $S/venv/bin/python -I $S/ep4/tools/scripts/transcribe.py rec/part$n.wav rec/part${n}_words_seg.json 4 > rec/tr_part$n.log 2>&1
done
echo TR_DONE
