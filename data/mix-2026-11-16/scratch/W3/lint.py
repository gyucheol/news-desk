"""WRITE.md 길이·형식 규칙 점검 (ocheck보다 엄격한 권장 범위)"""
import json, re, sys
H = '/home/user/news-desk/data/mix-2026-11-16'
O = json.load(open(f'{H}/out2/W3.json', encoding='utf-8'))
NODES = {}
cur = None
for line in open('/home/user/news-desk/tools/industry/nodes.md', encoding='utf-8'):
    m = re.match(r'^## (\w+) — ', line)
    if m: cur = m.group(1); NODES[cur] = set(); continue
    m = re.match(r'^- (\w+) — ', line)
    if m and cur: NODES[cur].add(m.group(1))
OLD9 = {'uranium', 'drilling', 'gas', 'coal', 'power', 'petchem', 'jpins', 'beauty', 'macro'}
TAILS = (' (제목 기준)', ' (채널 전언)')
TAGS = ('[사실]', '[채널]', '[제목]', '[추론]', '[미확인]')
P = []
def strip_tail(s):
    for t in TAILS:
        if s.endswith(t): return s[:-len(t)]
    return s
for x in O['items']:
    w = x['cid']
    if not 20 <= len(x['title']) <= 70: P.append(f"{w} title {len(x['title'])}")
    L = strip_tail(x['one']).split('\n')
    if not 40 <= len(L[0]) <= 90: P.append(f"{w} L1 {len(L[0])}: {L[0]}")
    for i, l in enumerate(L[1:], 2):
        if not 25 <= len(l) <= 90: P.append(f"{w} L{i} {len(l)}: {l}")
    f = x['facts']
    if not 2 <= len(f) <= 5: P.append(f"{w} facts {len(f)}")
    if not f[0].startswith('무엇이:'): P.append(f"{w} facts[0]")
    for k in f:
        if not k.endswith(TAGS): P.append(f"{w} fact tag: {k[-12:]}")
        if '|' in k or '**' in k: P.append(f"{w} fact char")
    for it in x['items']:
        if not 25 <= len(it['t']) <= 60: P.append(f"{w} item t {len(it['t'])}: {it['t']}")
        if 's' in it:
            s = strip_tail(it['s'])
            if not 45 <= len(s) <= 110: P.append(f"{w} s {len(s)}: {s}")
            if not s.endswith('다'): P.append(f"{w} s end: {s[-10:]}")
    if x.get('added') is not None:
        a = x['added']
        if not 40 <= len(a) <= 140: P.append(f"{w} added {len(a)}")
        if ' — ' not in a or '내용이 추가됨' not in a: P.append(f"{w} added form")
    for v in x['vc']:
        if v['ind'] not in NODES or v['node'] not in NODES[v['ind']]: P.append(f"{w} vc node {v['ind']}/{v['node']}")
        if v['f'] not in ('공급', '수요', '가격', '-') or v['dir'] not in ('up', 'down', 'flat', 'mixed') or v['k'] not in ('실제', '예상'):
            P.append(f"{w} vc enum {v}")
        if v['f'] == '-' and v['dir'] != 'flat': P.append(f"{w} vc - not flat")
        if not 12 <= len(v['t']) <= 45: P.append(f"{w} vc t {len(v['t'])}: {v['t']}")
        if v['ind'] not in x['inds']: P.append(f"{w} vc ind {v['ind']} not in inds (참고)")
    for n in x['nodes']:
        i, nd = n.split('/')
        if i not in OLD9 or nd not in NODES.get(i, ()): P.append(f"{w} node {n}")
        if i not in x['inds']: P.append(f"{w} node ind {i} not in inds")
    for fd in x.get('fed', []):
        if not 20 <= len(fd['t']) <= 70 or not fd['t'].endswith('다'): P.append(f"{w} fed t {len(fd['t'])}")
        if fd['u'] not in [it['u'] for it in x['items']]: P.append(f"{w} fed u")
    blob = json.dumps(x, ensure_ascii=False)
    if '{{' in blob or '**' in blob: P.append(f"{w} 강조 문자")
    if '|' in x['title'] + x['one'] + ''.join(i.get('s', '') for i in x['items']) + x.get('added', ''): P.append(f"{w} | 문자")
print('lint 문제', len(P))
for p in P: print(' -', p)
