"""W6 parts -> out2/W6.json, with rule checks (lengths, vc nodes, bundle URLs)."""
import json, re, os, sys

H = '/home/user/news-desk/data/mix-2026-11-16'
P = f'{H}/scratch/W6/parts'
TAILS = {'title': ' (제목 기준)', 'channel': ' (채널 전언)'}

items = []
for fn in sorted(os.listdir(P)):
    if fn.endswith('.json'):
        items += json.load(open(f'{P}/{fn}'))

# nodes.md: industry -> node ids
nodes = {}
cur = None
for line in open('/home/user/news-desk/tools/industry/nodes.md'):
    m = re.match(r'^## (\w+) — ', line)
    if m:
        cur = m.group(1); nodes[cur] = set(); continue
    m = re.match(r'^- (\w+) — ', line)
    if m and cur:
        nodes[cur].add(m.group(1))
OLD9 = {'uranium', 'drilling', 'gas', 'coal', 'power', 'petchem', 'jpins', 'beauty', 'macro'}

# bundle URLs per cluster
bundle = open(f'{H}/bundle/W6.md').read()
burls = {}
for sec in re.split(r'\n## ', bundle)[1:]:
    cid = sec.split()[0]
    burls[cid] = re.findall(r'^### .*? · (https?://\S+)$', sec, re.M)

meta = json.load(open(f'{H}/bundle/W6.meta.json'))
warn = []
def w(msg): warn.append(msg)
strip = lambda s: next((s[:-len(t)] for t in TAILS.values() if s.endswith(t)), s)

out_items = []
for x in items:
    cid = x['cid']; m = meta[cid]
    one = '\n'.join(x.pop('one_lines'))
    x['one'] = one
    t = x['title']
    if not 20 <= len(t) <= 70: w(f'{cid} title {len(t)}')
    L = strip(one).split('\n')
    if not 40 <= len(L[0]) <= 90: w(f'{cid} L1 {len(L[0])}')
    for i, l in enumerate(L[1:], 2):
        if not 25 <= len(l) <= 90: w(f'{cid} L{i} {len(l)}: {l[:30]}')
    for f in x['facts']:
        if '|' in f or '**' in f: w(f'{cid} fact forbidden char')
        if not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f): w(f'{cid} fact tag end: {f[-20:]}')
    if not 2 <= len(x['facts']) <= 5: w(f'{cid} facts n {len(x["facts"])}')
    if x['attachTo'] != m['attachTo']: w(f'{cid} attachTo mismatch')
    if x['attachTo']:
        a = x.get('added', '')
        if not 40 <= len(strip(a)) <= 140: w(f'{cid} added {len(strip(a))}')
        if not strip(a).endswith('내용이 추가됨'): w(f'{cid} added form')
    elif 'added' in x: w(f'{cid} added without attach')
    for ind in x['inds']:
        if ind not in nodes: w(f'{cid} ind {ind} unknown')
    for n in x['nodes']:
        i, nd = n.split('/')
        if i not in OLD9 or nd not in nodes.get(i, ()): w(f'{cid} node {n} bad')
        if i not in x['inds']: w(f'{cid} node ind {i} not in inds')
    for v in x['vc']:
        if v['ind'] not in nodes or v['node'] not in nodes[v['ind']]: w(f'{cid} vc {v["ind"]}/{v["node"]} bad')
        if v['f'] not in ('공급', '수요', '가격', '-') or v['dir'] not in ('up', 'down', 'flat', 'mixed') or v['k'] not in ('실제', '예상'):
            w(f'{cid} vc enum')
        if not 12 <= len(v['t']) <= 45: w(f'{cid} vc t {len(v["t"])}')
    if not 1 <= len(x['vc']) <= 3: w(f'{cid} vc n')
    us = [it['u'] for it in x['items']]
    if us != burls[cid]: w(f'{cid} item urls differ from bundle: {set(burls[cid]) ^ set(us)}')
    multi = m['n'] > 1 or m['attachTo']
    for it in x['items']:
        if not 25 <= len(it['t']) <= 60: w(f'{cid} item t {len(it["t"])}: {it["t"]}')
        if multi:
            s = strip(it.get('s', ''))
            if not 45 <= len(s) <= 110: w(f'{cid} s {len(s)}: {s[:30]}')
            if not s.endswith('다'): w(f'{cid} s end')
        elif 's' in it: w(f'{cid} s on single')
    for fd in x.get('fed', []):
        if not 20 <= len(fd['t']) <= 70: w(f'{cid} fed t {len(fd["t"])}')
        if fd['u'] not in us: w(f'{cid} fed u not in items')
    blob = json.dumps(x, ensure_ascii=False)
    if '{{' in blob or '**' in blob: w(f'{cid} emphasis')
    for k in ('title', 'one', 'added'):
        if '|' in x.get(k, ''): w(f'{cid} pipe in {k}')
    order = ['cid', 'attachTo', 'title', 'one', 'facts', 'basis', 'check', 'src', 'inds', 'nodes', 'vc', 'fed', 'added', 'items']
    out_items.append({k: x[k] for k in order if k in x})

missing = set(meta) - {x['cid'] for x in out_items}
if missing: w(f'missing {sorted(missing)}')
out = {'agent': 'W6', 'searches_used': 16, 'fetches_used': 7, 'items': out_items, 'skipped': []}
json.dump(out, open(f'{H}/out2/W6.json', 'w'), ensure_ascii=False, indent=1)
print('items', len(out_items), 'warnings', len(warn))
for x in warn: print(' -', x)
