"""Validate an industry page JSON against BUILD.md section 2/3 rules and GUIDE-short emphasis rules.
usage: python3 -I check.py <page.json> [--map news_map.tsv] [--known other_page.json ...] [-v]
"""
import json, re, sys, glob, os

args = sys.argv[1:]
path = args[0]
verbose = '-v' in args
mapfile = args[args.index('--map') + 1] if '--map' in args else None
known_pages = []
if '--known' in args:
    i = args.index('--known') + 1
    while i < len(args) and not args[i].startswith('-'):
        known_pages.append(args[i]); i += 1

P, W = [], []
d = json.load(open(path))
print('json.load OK:', path)

# ---------- known node ids for links ----------
known = {}
for f in glob.glob('/home/user/news-desk/work/live14/chains/*.json'):
    x = json.load(open(f)); known[x['id']] = {n['id'] for n in x['nodes']}
for f in known_pages + [path]:
    x = json.load(open(f)); known[x['id']] = {n['id'] for n in x['nodes']}

# ---------- top-level ----------
need = ['id', 'name', 'short', 'icon', 'order', 'asOf', 'rev', 'summary', 'intro', 'nodes', 'cycle',
        'industryState', 'insight', 'flows', 'gaps', 'history']
for k in need:
    if k not in d: P.append(f'top: missing {k}')
if len(d.get('short', '')) > 6: P.append(f"top short >6: {d['short']}")
if d.get('insight') != {}: P.append('insight must be {}')
if d.get('flows') != []: P.append('flows must be []')
if d.get('asOf') != '2026-10-14' or d.get('rev') != '2026-10-14': P.append('asOf/rev')

intro = d['intro']
for k, lo, hi in [('watch', 3, 5), ('players', 5, 8), ('reading', 3, 5), ('terms', 3, 6)]:
    n = len(intro.get(k, []))
    if not lo <= n <= hi: P.append(f'intro.{k} count {n} not in {lo}-{hi}')
for w in intro['watch']:
    for k in ('n', 'why', 'where'):
        if not w.get(k): P.append(f'watch missing {k}')
for p in intro['players']:
    for k in ('n', 't', 'm', 'role'):
        if k not in p: P.append(f'player missing {k}: {p}')
OKM = {'NYSE', 'NASDAQ', 'KRX', 'TSE', 'HKEX', 'SSE', 'SZSE', 'SGX', 'private'}

# ---------- nodes ----------
nodes = d['nodes']
if not 5 <= len(nodes) <= 9: P.append(f'nodes count {len(nodes)}')
ids = [n['id'] for n in nodes]
if len(ids) != len(set(ids)): P.append(f'duplicate node ids {ids}')
for n in nodes:
    nid = n['id']
    if not re.fullmatch(r'[a-z]{2,12}', nid): P.append(f'bad node id {nid}')
    if len(n.get('short', '')) > 6: P.append(f'{nid} short >6: {n["short"]}')
    for k in ('name', 'short', 'role', 'bottleneck', 'indicators', 'companies'):
        if k not in n: P.append(f'{nid} missing {k}')
    if 'stage' in n and n['stage'] is not None and n['stage'] not in range(1, 9): P.append(f'{nid} stage {n["stage"]}')
    if not 2 <= len(n['indicators']) <= 3: P.append(f'{nid} indicators {len(n["indicators"])}')
    if not 2 <= len(n['companies']) <= 5: P.append(f'{nid} companies {len(n["companies"])}')
    if len(n.get('state', [])) > 3: P.append(f'{nid} state >3')
    for c in n['companies']:
        for k in ('n', 't', 'm', 'note'):
            if k not in c: P.append(f'{nid} company missing {k}')
        if c['m'] not in OKM: W.append(f'{nid} company market label "{c["m"]}" ({c["n"]})')
    for l in n.get('links', []):
        to = l.get('to')
        if to:
            ind, _, nd = to.partition('/')
            if ind not in known or nd not in known[ind]: P.append(f'{nid} link target unknown {to}')
        if not l.get('why'): P.append(f'{nid} link missing why')
    for s in n.get('state', []):
        for k in ('d', 'o', 't', 'u'):
            if not s.get(k): P.append(f'{nid} state missing {k}')
        if not re.fullmatch(r'\d{4}-\d{2}(-\d{2})?', s.get('d', '')): P.append(f'{nid} state bad date {s.get("d")}')
    # role 1~2 sentences, bottleneck 1 sentence
    def sentences(t):
        t = re.sub(r'\[[^\]]+\]', '', t.replace('{{', '').replace('}}', ''))
        return [x for x in re.split(r'(?<=[다요])\.\s*', t) if x.strip()]
    if not 1 <= len(sentences(n['role'])) <= 2: P.append(f'{nid} role sentences {len(sentences(n["role"]))}')
    if len(sentences(n['bottleneck'])) != 1: P.append(f'{nid} bottleneck sentences {len(sentences(n["bottleneck"]))}')
for p in intro['players']:
    if p['m'] not in OKM: W.append(f'player market label "{p["m"]}" ({p["n"]})')

# ---------- cycle ----------
cy = d['cycle']
if cy.get('stage') not in range(1, 9): P.append(f'cycle.stage {cy.get("stage")}')
if cy.get('conf') not in ('높음', '중간', '낮음'): P.append('cycle.conf')
if not 2 <= len(cy.get('why', [])) <= 4: P.append(f'cycle.why count {len(cy.get("why", []))}')
for w in cy['why']:
    if not w.get('src'): P.append('why without src')
    for s in w['src']:
        if not s.get('o') or not s.get('u'): P.append(f'why src missing o/u: {s}')
    if not re.search(r'\[(사실|귀납|유추|추측)\]', w['t']): P.append(f'why missing tag: {w["t"][:30]}')
if not 3 <= len(cy.get('watch', [])) <= 5: P.append('cycle.watch count')
for sp in cy.get('split', []):
    if sp['stage'] not in range(1, 9): P.append('split stage')
    for x in sp['nodes']:
        if x not in ids: P.append(f'split node unknown {x}')

# ---------- industryState ----------
if not 2 <= len(d['industryState']) <= 5: P.append(f'industryState count {len(d["industryState"])}')
for s in d['industryState']:
    if s.get('kind') not in ('price', 'supply', 'demand', 'capex', 'policy'): P.append(f'industryState kind {s.get("kind")}')
    for k in ('d', 'o', 't', 'u'):
        if not s.get(k): P.append(f'industryState missing {k}')

# ---------- banned / suspicious domains ----------
BANNED = ['bloomberg.com', 'reuters.com', 'bnnbloomberg', 'usnews.com', 'msn.com', 'finance.yahoo', 'marketscreener.com']
def walk(o, pth=''):
    if isinstance(o, dict):
        for k, v in o.items(): yield from walk(v, f'{pth}.{k}')
    elif isinstance(o, list):
        for i, v in enumerate(o): yield from walk(v, f'{pth}[{i}]')
    else:
        yield pth, o
for pth, v in walk(d):
    if isinstance(v, str) and v.startswith('http'):
        for b in BANNED:
            if b in v: P.append(f'banned domain {b} at {pth}: {v}')
        if 'investing.com' in v or 'tradingview.com' in v: W.append(f'check byline (investing/tradingview) {pth}: {v}')

# ---------- emphasis ----------
LBL = re.compile(r'\s*\[(사실|귀납|연역|유추|추측)[^\]]*\]\s*\.?\s*$')
strip = lambda s: s.replace('{{', '').replace('}}', '')
JOSA = set('은는이가을를에의와과도로만')
EMPH = []  # (name, text) must carry emphasis
NOEMPH = []  # must not
EMPH.append(('summary', d['summary']))
for k in ('what', 'money', 'drivers'): EMPH.append((f'intro.{k}', intro[k]))
for i, r in enumerate(intro['reading']): EMPH.append((f'reading{i}.means', r['means'])); NOEMPH.append((f'reading{i}.news', r['news']))
for k in ('watch', 'players', 'terms'):
    for i, x in enumerate(intro[k]):
        for kk, vv in x.items(): NOEMPH.append((f'intro.{k}{i}.{kk}', vv))
for n in nodes:
    EMPH.append((f'{n["id"]}.role', n['role'])); EMPH.append((f'{n["id"]}.bottleneck', n['bottleneck']))
    for i, c in enumerate(n['companies']): EMPH.append((f'{n["id"]}.co{i}', c['note']))
    for i, s in enumerate(n.get('state', [])): EMPH.append((f'{n["id"]}.state{i}', s['t']))
    for i, x in enumerate(n['indicators']): NOEMPH.append((f'{n["id"]}.ind{i}', x['n'] + ' ' + x['src']))
    for i, x in enumerate(n.get('links', [])): NOEMPH.append((f'{n["id"]}.link{i}', x['why']))
    NOEMPH.append((f'{n["id"]}.name', n['name'])); NOEMPH.append((f'{n["id"]}.stageNote', n.get('stageNote', '')))
for i, w in enumerate(cy['why']): EMPH.append((f'why{i}', w['t']))
EMPH.append(('next', cy['next']))
for i, s in enumerate(d['industryState']): NOEMPH.append((f'industryState{i}', s['t']))
NOEMPH.append(('gaps', d['gaps']))
for x in cy['watch']: NOEMPH.append(('cycle.watch', x))

for name, s in NOEMPH:
    if '{{' in s or '}}' in s: P.append(f'{name}: emphasis not allowed')

tot = hl = 0
for name, sraw in EMPH:
    s = LBL.sub('', sraw)
    marks = re.findall(r'\{\{(.+?)\}\}', s)
    plain = strip(s); n = len(plain); h = sum(len(m) for m in marks); tot += n; hl += h
    if sraw.count('{{') != sraw.count('}}') or re.search(r'\{\{[^}]*\{\{', sraw) or re.search(r'\}\}[^{]*\}\}', sraw) or '{{}}' in sraw or re.search(r'(?<!\{)\{(?!\{)|(?<!\})\}(?!\})', sraw):
        P.append(f'{name}: 괄호 짝')
    for m in marks:
        if m != m.strip(): P.append(f'{name}: 공백 시작/끝 "{m}"')
        if re.search(r'\[(사실|귀납|연역|유추|추측)', m): P.append(f'{name}: 꼬리표 강조 "{m}"')
        if m.count('(') != m.count(')'): W.append(f'{name}: 괄호 안 닫힘 "{m}"')
        if len(m) > 30: W.append(f'{name}: 덩어리 김({len(m)}) "{m}"')
        if re.match(r"^[,.)·'\"]|[,('\"]$", m): W.append(f'{name}: 문장부호 시작/끝 "{m}"')
        if len(m) == 1 and m in JOSA: W.append(f'{name}: 조사 한 글자 "{m}"')
    if re.search(r'\}\}\{\{', sraw): W.append(f'{name}: 강조가 붙어 있음')
    if not marks and n >= 10: W.append(f'{name}: 강조 없음')
    elif n >= 24 and h / n < 0.30: W.append(f'{name}: 강조 적음 {h/n:.0%}')
    elif n >= 30 and h / n > 0.86: W.append(f'{name}: 강조 많음 {h/n:.0%}')
    if verbose: print(f'[{name} {h/max(1,n):.0%}]')
print(f'emphasis ratio overall {hl/max(1,tot):.0%} over {len(EMPH)} units')
grp = {}
for name, sraw in EMPH:
    g = name.split('.')[0] if name.startswith(('intro', 'summary', 'next')) else ('reading' if name.startswith('reading') else ('why' if name.startswith('why') else 'nodes'))
    s = LBL.sub('', sraw); marks = re.findall(r'\{\{(.+?)\}\}', s); plain = strip(s)
    a = grp.setdefault(g, [0, 0]); a[0] += sum(len(m) for m in marks); a[1] += len(plain)
print('  by group:', {k: f'{v[0]/max(1,v[1]):.0%}' for k, v in grp.items()})

# ---------- news coverage map ----------
if mapfile:
    m = {}
    for line in open(mapfile):
        if line.strip() and not line.startswith('#'):
            a = line.rstrip('\n').split('\t'); m[a[0]] = a[1]
    tsv = f'/home/user/news-desk/data/industry-2026-10-14/news/{d["id"]}.tsv'
    rows = [l.rstrip('\n').split('\t') for l in open(tsv) if l.strip()]
    miss = 0
    for r in rows:
        key = r[1] if r[1] != '(되살릴 기사)' else r[2][:60]
        node = m.get(key)
        if node is None or node not in ids:
            miss += 1; P.append(f'news not mapped: {key} -> {node}')
    cnt = {}
    for v in m.values(): cnt[v] = cnt.get(v, 0) + 1
    print(f'news rows {len(rows)}, unmapped {miss}; per node {cnt}')

print(f'PROBLEMS {len(P)}  WARN {len(W)}')
for x in P: print(' !', x)
for x in W: print(' ~', x)
