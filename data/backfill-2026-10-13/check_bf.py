"""안 읽은 기존 뉴스 보강 결과 검사. 사용: python3 -I check_bf.py <in/이름.json> <out/이름.json>"""
import json, re, sys
src = {d['id']: d for d in json.load(open(sys.argv[1], encoding='utf-8'))}
out = json.load(open(sys.argv[2], encoding='utf-8'))['docs']
P = []
HL = re.compile(r'\{\{([^{}]+)\}\}')
TAIL = re.compile(r' \((제목 기준|채널 전언)\)$')
plain = lambda s: s.replace('{{', '').replace('}}', '')

def hl(w, s, lo, hi):
    ms = HL.findall(s)
    if not lo <= len(ms) <= hi: P.append(f'{w}: 강조 {len(ms)}곳({lo}~{hi})')
    if '{' in HL.sub('', s) or '}' in HL.sub('', s): P.append(f'{w}: 강조 괄호 짝')
    for m in ms:
        if not 2 <= len(m) <= 20: P.append(f'{w}: 강조 길이 {len(m)} "{m[:12]}"')
        if TAIL.search(' ' + m.strip()) or m.strip() in ('제목 기준', '채널 전언'): P.append(f'{w}: 꼬리를 강조함')

def line(w, s, lo, hi, nlo, nhi):
    hl(w, s, nlo, nhi)
    core = TAIL.sub('', plain(s))
    if not lo <= len(core) <= hi: P.append(f'{w}: {len(core)}자({lo}~{hi})')
    if not core.endswith('다'): P.append(f'{w}: 끝맺음')
    if '|' in s or '**' in s: P.append(f'{w}: 금지 문자')

seen = set()
for d in out:
    i = d.get('id'); s = src.get(i)
    if not s: P.append(f'{i}: 입력에 없는 id'); continue
    seen.add(i)
    for f, lo, hi in (('title', 1, 2), ('one', 2, 4)):
        v = d.get(f, '')
        if plain(v) != s[f]: P.append(f'{i}.{f}: 강조 말고 글자가 바뀜')
        hl(f'{i}.{f}', v, lo, hi)
    if 'items' in s:
        line(f'{i}.added', d.get('added', ''), 60, 140, 1, 3)
        its = d.get('items') or []
        if [x.get('u') for x in its] != [x['u'] for x in s['items']]: P.append(f'{i}.items: 원문 주소·순서가 입력과 다름')
        for k, x in enumerate(its):
            line(f'{i}.items[{k}].s', x.get('s', ''), 45, 110, 1, 2)
    elif d.get('added') or d.get('items'): P.append(f'{i}: 한 건짜리 문서에 added·items')
miss = [i for i in src if i not in seen]
if miss: P.append(f'빠진 문서 {len(miss)}: ' + ', '.join(miss[:8]))
print('PROBLEMS', len(P)); [print(' -', p) for p in P[:80]]
ns = sum(len(d.get('items') or []) for d in out)
nt = sum(1 for d in out for x in d.get('items') or [] if x.get('s', '').endswith('(제목 기준)'))
print('docs', len(out), '/', len(src), 'items s', ns, 'title-basis', nt)
