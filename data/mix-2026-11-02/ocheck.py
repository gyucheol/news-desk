"""작성 결과 여러 줄 요약 검사: python3 -I ocheck.py W1  (bundle/W1.meta.json ↔ out2/W1.json)"""
import json, re, sys, os
H = os.path.dirname(os.path.abspath(__file__)); name = sys.argv[1]
M = json.load(open(f'{H}/bundle/{name}.meta.json')); O = json.load(open(f'{H}/out2/{name}.json'))
TAIL = {'title': ' (제목 기준)', 'channel': ' (채널 전언)'}
nums = lambda t: set(x.replace(',', '') for x in re.findall(r'\d+(?:[.,]\d+)*', t))
P = []; done = {x['cid'] for x in O.get('items', [])} | {x['cid'] for x in O.get('skipped', [])}
miss = set(M) - done
if miss: P.append(f'빠진 묶음 {sorted(miss)}')
for x in O.get('items', []):
    w = x['cid']; m = M.get(w)
    if not m: P.append(f'{w} 묶음 파일에 없음'); continue
    one = x.get('one', ''); t = x.get('title', '')
    if not 15 <= len(t) <= 75: P.append(f'{w} title {len(t)}자')
    if '{{' in one + t or '**' in one + t or '|' in one + t: P.append(f'{w} 금지 문자')
    tail = TAIL.get(x.get('basis'), '')
    if tail and not one.endswith(tail): P.append(f'{w} 꼬리 없음({tail.strip()})')
    body = one[:-len(tail)] if tail and one.endswith(tail) else one
    if any(body.endswith(v) for v in TAIL.values()): P.append(f'{w} 꼬리가 basis와 다름')
    L = body.split('\n')
    lo, hi = (2, 3) if m['n'] <= 1 and not m['attachTo'] else (3, 7)
    if not lo <= len(L) <= hi: P.append(f'{w} 줄 수 {len(L)}({lo}~{hi})')
    if L and L[0].startswith('·'): P.append(f'{w} 첫 줄은 개요(· 없이)')
    if L and not 30 <= len(L[0]) <= 100: P.append(f'{w} 첫 줄 {len(L[0])}자')
    for k, l in enumerate(L[1:], 2):
        if not l.startswith('· '): P.append(f'{w} {k}줄 · 로 시작 안 함')
        if not 20 <= len(l) <= 100: P.append(f'{w} {k}줄 {len(l)}자')
    for k, l in enumerate(L, 1):
        if not l.rstrip().endswith('다'): P.append(f'{w} {k}줄 끝맺음')
    lost = nums(' '.join(m['core'])) - nums(one + ' ' + t + ' ' + ' '.join(x.get('facts', [])))
    if lost: P.append(f'{w} core 숫자가 요약·사실에 없음 {sorted(lost)[:6]} (글과 달라 일부러 뺐으면 보고)')
    if m['old_one']:
        lost2 = nums(m['old_one']) - nums(one + ' ' + ' '.join(x.get('facts', [])))
        if lost2: P.append(f'{w} 기존 한줄 숫자 빠짐 {sorted(lost2)[:6]}')
print('묶음', len(O.get('items', [])), '건너뜀', len(O.get('skipped', [])), '/', len(M), '문제', len(P))
for p in P[:60]: print(' -', p)
