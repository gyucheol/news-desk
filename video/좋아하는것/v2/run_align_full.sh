set -euo pipefail
cd .
$S/venv/bin/python -I "$S/ep4/tools/scripts/align_words.py" units_full.json align_full.json ../rec/part1_words.json:0 ../rec/part2_words.json:210.71733333333333 ../rec/part3_words.json:434.30466666666666
$S/venv/bin/python -I "$S/ep4/tools/scripts/onsets.py" rec_full.wav align_full.json onsets_full.json
$S/venv/bin/python -I -c "
import json; L={o['id']:o for o in json.load(open('lines_full.json'))}
U=json.load(open('onsets_full.json'))
for u in U: u['shown']=L[u['id']]['text']; u['text']=L[u['id']]['say']
json.dump(U, open('onsets_say_full.json','w'), ensure_ascii=False, indent=1)"
(cd $S && $S/venv/bin/python -I "$S/ep4/tools/scripts/ctc_align.py" ./rec_full.wav ./onsets_say_full.json models/w2v_ko ./align_ctc_full.json)
$S/venv/bin/python -I "$S/ep4/tools/scripts/onsets_v2.py" ./rec_full.wav align_ctc_full.json lines_full.json onsets_v2_full.json
echo ALIGN_DONE
