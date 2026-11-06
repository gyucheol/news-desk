set -euo pipefail
# 살걸·팔걸 편: 받아쓰기 낱말 -> 자막 줄 대략 시각 -> 음절 모델로 목소리 시작 시각(수면 편과 같은 도구)
# 이은 녹음(rec/rec.wav)에서 각 파일의 시작: 1편 0, 2편 171.5333, 3편 355.26 (rec/join.json)
# 받아쓰기 낱말은 숫자·알파벳을 한글 읽기로 바꾼 것(ko_words.py -> rec/part*_words_ko.json)
# 받아쓰기가 지어낸 곳은 뺌: 1편 끝 170.82~171.06('주가가 가장 높은 종목이 아닌가?', 음절 모델로 말 없음 확인),
#   2편 87.26~87.66('상처를 겪었습니다', 실제로는 '상철은' 한 번뿐)
S=/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad
W=$S/salgeol/v1
cd $W
$S/venv/bin/python -I "$S/ep4/tools/scripts/align_words.py" units.json align.json \
  rec/part1_words_ko.json:0:0:170.8 rec/part2_words_ko.json:171.5333:0:87.2 rec/part2_words_ko.json:171.5333:87.67:999 \
  rec/part3_words_ko.json:355.26
$S/venv/bin/python -I "$S/ep4/tools/scripts/onsets.py" rec/rec.wav align.json onsets.json
$S/venv/bin/python -I -c "
import json; L={o['id']:o for o in json.load(open('lines.json'))}
U=json.load(open('onsets.json'))
for u in U: u['shown']=L[u['id']]['text']; u['text']=L[u['id']]['say']
json.dump(U, open('onsets_say.json','w'), ensure_ascii=False, indent=1)"
(cd $S && $S/venv/bin/python -I "$S/ep4/tools/scripts/ctc_align.py" $W/rec/rec.wav $W/onsets_say.json models/w2v_ko $W/align_ctc.json)
$S/venv/bin/python -I "$S/ep4/tools/scripts/onsets_v2.py" rec/rec.wav align_ctc.json lines.json onsets_v2.json
echo ALIGN_DONE
