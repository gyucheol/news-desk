# 03편 v2 (2026-10-30 사용자 수정 요청) 자막 위치 바꾸기: lines_v3.json -> lines_r2.json
# - "다큐멘터리를 본 뒤에는 평균 약 12분을 버텼지만 / 수학 문제를 푼 뒤에는 약 9분에 멈췄습니다."(V123~V126): 가운데로
# - "지금 막힌 곳은 ~ 아닙니다. 지친 몸으로 ~ 단계입니다."(V183~V188): 아래로
# usage: pos_r2.py [lines_in.json] [lines_out.json]
import json, sys
src = sys.argv[1] if len(sys.argv) > 1 else 'lines_v3.json'
dst = sys.argv[2] if len(sys.argv) > 2 else 'lines_r2.json'
POS = {**{f'V{n}': 'c' for n in range(123, 127)}, **{f'V{n}': 'b' for n in range(183, 189)}}
WANT = {'V123': '다큐멘터리를 본 뒤에는', 'V126': '약 9분에 멈췄습니다.', 'V183': '지금 막힌 곳은', 'V188': '단계입니다.'}
L = json.load(open(src, encoding='utf-8'))
by = {l['id']: l for l in L}
for k, v in WANT.items():
    assert by[k]['text'] == v, (k, by[k]['text'])
n = 0
for l in L:
    if l['id'] in POS and l['pos'] != POS[l['id']]:
        l['pos'] = POS[l['id']]; n += 1
json.dump(L, open(dst, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(dst, n, 'lines moved')
