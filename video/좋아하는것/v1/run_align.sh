set -euo pipefail
cd /tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep4/v1
/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/venv/bin/python -I "/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep3/tools/F의연애/영상/scripts/align_words.py" units_disp.json align.json ../rec/part1_words.json:0 ../rec/part2_words.json:210.71733333333333:0:44.25
/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/venv/bin/python -I "/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep3/tools/F의연애/영상/scripts/onsets.py" rec.wav align.json onsets.json
/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/venv/bin/python -I -c "
import json; L={o['id']:o for o in json.load(open('lines.json'))}
U=json.load(open('onsets.json'))
for u in U: u['shown']=L[u['id']]['text']; u['text']=L[u['id']]['say']
json.dump(U, open('onsets_say.json','w'), ensure_ascii=False, indent=1)"
(cd /tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad && /tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/venv/bin/python -I "/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep3/tools/F의연애/영상/scripts/ctc_align.py" /tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep4/v1/rec.wav /tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep4/v1/onsets_say.json models/w2v_ko /tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep4/v1/align_ctc.json)
/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/venv/bin/python -I "/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep3/tools/F의연애/영상/scripts/onsets_v2.py" /tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/ep4/v1/rec.wav align_ctc.json lines.json onsets_v2.json
echo ALIGN_DONE
