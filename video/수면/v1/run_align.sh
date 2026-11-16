set -euo pipefail
# 수면 편: 받아쓰기 낱말 -> 자막 줄 대략 시각 -> 음절 모델로 목소리 시작 시각(04편과 같은 도구)
S=${S:?set S (scratchpad: venv/, models/, ep4/tools/scripts/)}
W="$(pwd)"   # 작업 폴더(sleep/v1)에서 실행
$S/venv/bin/python -I "$S/ep4/tools/scripts/align_words.py" units.json align.json rec/rec_words_seg.json:0   # rec_words_seg.json = rec/words.json을 한 덩어리 구간 꼴로 바꾼 것
$S/venv/bin/python -I "$S/ep4/tools/scripts/onsets.py" rec/rec.wav align.json onsets.json
$S/venv/bin/python -I -c "
import json; L={o['id']:o for o in json.load(open('lines.json'))}
U=json.load(open('onsets.json'))
for u in U: u['shown']=L[u['id']]['text']; u['text']=L[u['id']]['say']
json.dump(U, open('onsets_say.json','w'), ensure_ascii=False, indent=1)"
(cd $S && $S/venv/bin/python -I "$S/ep4/tools/scripts/ctc_align.py" $W/rec/rec.wav $W/onsets_say.json models/w2v_ko $W/align_ctc.json)
$S/venv/bin/python -I "$S/ep4/tools/scripts/onsets_v2.py" rec/rec.wav align_ctc.json lines.json onsets_v2.json
echo ALIGN_DONE
