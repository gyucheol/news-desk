# onsets_v2.json -> onsets_v3.json: 음절 모델 재확인(ctc_recheck.py, recheck_all.json)에서 틀린 줄만 손으로 고침.
#  V105 '2016년 프리드먼과 캐머러는': 첫 낱말 '이천십육 년' 뒤의 쉼(190.45~190.85) 뒤를 시작으로 잡아 1.08초 늦었음.
#        제약 없는 음절 맞춤의 첫 음절 189.60초, 소리 크기로 목소리 시작 189.58초 -> 189.58.
#  (V154는 0.15초 차이였지만 'ㅊ' 소리가 284.05초에 시작해서 지금 값이 맞음)
import json
FIX = {"V105": 189.58}
O = json.load(open('onsets_v2.json', encoding='utf-8'))
for o in O:
    if o['id'] in FIX:
        o['start_before_fix'] = o['start']; o['start'] = FIX[o['id']]; o['timing'] = 'fixed (ctc_recheck)'
json.dump(O, open('onsets_v3.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
st = [o['start'] for o in O]
assert all(b > a for a, b in zip(st, st[1:])), 'starts not increasing'
print('fixed', list(FIX), '| starts increasing')
