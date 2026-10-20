"""여러 줄 요약 검사: python3 -I mcheck.py <이름>"""
import json, re, sys, os
H = os.path.dirname(os.path.abspath(__file__)); name = sys.argv[1]
I = json.load(open(f'{H}/in/{name}.json')); O = json.load(open(f'{H}/out/{name}.json'))
TAIL = {'title': ' (제목 기준)', 'channel': ' (채널 전언)'}
P = []
if [x['id'] for x in O] != [x['id'] for x in I]: P.append('id 순서·누락 다름')
src = {x['id']: x for x in I}
nums = lambda t: set(re.findall(r'\d+(?:[.,]\d+)*', t))
for x in O:
    d = src.get(x['id']); w = x['id']
    if not d: continue
    one = x.get('one', '')
    if '{{' in one or '**' in one or '|' in one: P.append(f'{w} 금지 문자')
    tail = TAIL.get(d['basis'], '')
    if tail and not one.endswith(tail): P.append(f'{w} 꼬리 없음({tail.strip()})')
    body = one[:-len(tail)] if tail and one.endswith(tail) else one
    L = body.split('\n')
    lo, hi = (2, 3) if d['n'] <= 1 else (3, 7)
    if not lo <= len(L) <= hi: P.append(f'{w} 줄 수 {len(L)}(기사 {d["n"]}건: {lo}~{hi})')
    if L and L[0].startswith('·'): P.append(f'{w} 첫 줄은 개요(· 없이)')
    if L and not 30 <= len(L[0]) <= 100: P.append(f'{w} 첫 줄 {len(L[0])}자')
    for k, l in enumerate(L[1:], 2):
        if not l.startswith('· '): P.append(f'{w} {k}줄 · 로 시작 안 함')
        if not 20 <= len(l) <= 100: P.append(f'{w} {k}줄 {len(l)}자')
    for k, l in enumerate(L, 1):
        if not l.rstrip().endswith('다'): P.append(f'{w} {k}줄 끝맺음')
    miss = nums(d['one']) - nums(one)
    if miss: P.append(f'{w} 빠진 숫자 {sorted(miss)[:8]}')
print('문서', len(O), '/', len(I), '문제', len(P))
for p in P[:60]: print(' -', p)
