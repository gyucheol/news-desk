"""VC.md 3절 확인: json.load, 입력 id 전부, ind·node가 nodes.md에 있음, f·dir·k 값, t 길이(12~45자).
덧붙여: 같은 뉴스 안 같은 노드·같은 f 중복, 항목 수 1~3, t 금지 문자(강조·꼬리표·따옴표·끝 마침표, 숫자 사이가 아닌 '.').
사용: python3 -I validate.py <news-desk 루트>"""
import json, re, sys
from collections import Counter

ROOT = sys.argv[1]
BASE = f'{ROOT}/data/industry-2026-10-14/vc'
P = []

# nodes.md 파싱
nodes, cur = {}, None
for line in open(f'{ROOT}/tools/industry/nodes.md', encoding='utf-8'):
    m = re.match(r'^## ([a-z]+) — ', line)
    if m:
        cur = m.group(1); nodes[cur] = set(); continue
    m = re.match(r'^- ([a-z0-9]+) — ', line)
    if m and cur:
        nodes[cur].add(m.group(1))
# nodes.json 과 교차 확인
nj = {k: set(v) for k, v in json.load(open(f'{ROOT}/tools/industry/nodes.json', encoding='utf-8')).items()}
if nj != nodes: P.append('nodes.md 와 nodes.json 이 다름')

ids = [json.loads(l)['id'] for l in open(f'{BASE}/in2.jsonl', encoding='utf-8') if l.strip()]
out = json.load(open(f'{BASE}/out2.json', encoding='utf-8'))

if set(ids) - set(out): P.append(f'빠진 id {sorted(set(ids) - set(out))}')
if set(out) - set(ids): P.append(f'입력에 없는 id {sorted(set(out) - set(ids))}')

F, D, K = {'공급', '수요', '가격', '-'}, {'up', 'down', 'flat', 'mixed'}, {'실제', '예상'}
BAD = ['{{', '}}', '[', ']', '"', "'", '‘', '’', '“', '”', '「', '」', '『', '』', '(', ')']
cf, lens = Counter(), []
for i, items in out.items():
    if not isinstance(items, list) or not 1 <= len(items) <= 3: P.append(f'{i} 항목 수 {len(items) if isinstance(items, list) else items}')
    seen = set()
    for x in items:
        if set(x) != {'ind', 'node', 'f', 'dir', 'k', 't'}: P.append(f'{i} 키 {sorted(x)}')
        if x.get('ind') not in nodes: P.append(f'{i} ind {x.get("ind")}')
        elif x.get('node') not in nodes[x['ind']]: P.append(f'{i} node {x["ind"]}/{x.get("node")}')
        if x.get('f') not in F: P.append(f'{i} f {x.get("f")}')
        if x.get('dir') not in D: P.append(f'{i} dir {x.get("dir")}')
        if x.get('k') not in K: P.append(f'{i} k {x.get("k")}')
        if x.get('f') == '-' and x.get('dir') != 'flat': P.append(f'{i} f=- 인데 dir {x.get("dir")}')
        key = (x.get('ind'), x.get('node'), x.get('f'))
        if key in seen: P.append(f'{i} 같은 노드·f 중복 {key}')
        seen.add(key)
        t = x.get('t', '')
        lens.append(len(t))
        if not 12 <= len(t) <= 45: P.append(f'{i} t 길이 {len(t)}: {t}')
        for b in BAD:
            if b in t: P.append(f'{i} t 금지 문자 {b!r}: {t}')
        if t.rstrip().endswith('.') or re.search(r'(?<!\d)\.|\.(?!\d)', t): P.append(f'{i} t 마침표: {t}')
        if t != t.strip(): P.append(f'{i} t 앞뒤 공백')
        if not re.search(r'[가-힣]', t): P.append(f'{i} t 한국어 아님')
        cf[x.get('f')] += 1

print('PROBLEMS', len(P))
for p in P: print(' -', p)
print('docs', len(out), 'items', sum(len(v) for v in out.values()))
print('f', dict(cf))
print('dir', dict(Counter(x['dir'] for v in out.values() for x in v)))
print('k', dict(Counter(x['k'] for v in out.values() for x in v)))
print('per-doc', dict(Counter(len(v) for v in out.values())))
print('t len min/max', min(lens), max(lens))
