"""산업 페이지 JSON 형식·강조 점검 (BUILD.md 2·3절 기준).
사용: python3 check.py <out/<id>.json> [허용 링크 ...]
"""
import json, re, sys, os

path = sys.argv[1]
allowed_links = set(sys.argv[2:])
d = json.load(open(path, encoding='utf-8'))
errs, warns = [], []

def E(m): errs.append(m)
def W(m): warns.append(m)

DATE = re.compile(r'^\d{4}-\d{2}-\d{2}$')
for k in ['id', 'name', 'short', 'icon', 'order', 'asOf', 'rev', 'summary', 'intro', 'nodes', 'cycle', 'industryState', 'insight', 'flows', 'gaps', 'history']:
    if k not in d: E(f'top key missing: {k}')
if len(d.get('short', '')) > 6: E(f"industry short >6: {d['short']}")
if d.get('insight') != {}: E('insight must be {}')
if d.get('flows') != []: E('flows must be []')

# --- emphasis helpers
CH = re.compile(r'\{\{(.*?)\}\}')
def emph_check(where, s, lo=0.50, hi=0.65, need=True):
    if s.count('{{') != s.count('}}'): E(f'{where}: unbalanced braces')
    chunks = CH.findall(s)
    if need and not chunks: E(f'{where}: no emphasis'); return
    if not need and chunks: E(f'{where}: emphasis not allowed'); return
    for c in chunks:
        if '{' in c or '}' in c: E(f'{where}: nested braces in {c!r}')
        if not c.strip(): E(f'{where}: empty chunk')
        if c != c.strip(): E(f'{where}: chunk has edge space {c!r}')
        if c and c[0] in ',.\'"·' or c and c[-1] in ',.\'"·': E(f'{where}: punctuation at chunk edge {c!r}')
        if len(c) > 30: E(f'{where}: chunk >30 chars ({len(c)}) {c!r}')
        if c[-1:] in ('은', '는', '을', '를', '와', '과') and len(c) > 1: W(f'{where}: chunk ends with particle-like char {c!r}')
    if not need: return
    plain = s.replace('{{', '').replace('}}', '')
    tot = len(plain.replace(' ', ''))
    em = sum(len(c.replace(' ', '')) for c in chunks)
    r = em / tot if tot else 0
    tot2 = len(plain); em2 = sum(len(c) for c in chunks); r2 = em2 / tot2 if tot2 else 0
    flag = '' if lo <= r <= hi else '  <-- OUT'
    ratios.append((where, r, r2))
    if flag: W(f'{where}: ratio {r:.2f} (with spaces {r2:.2f}){flag}')

ratios = []
emph_check('summary', d['summary'])
it = d['intro']
for k in ['what', 'money', 'drivers']:
    emph_check(f'intro.{k}', it[k])
if not 3 <= len(it['watch']) <= 5: E('watch count')
if not 5 <= len(it['players']) <= 8: E('players count')
if not 3 <= len(it['reading']) <= 5: E('reading count')
if not 3 <= len(it['terms']) <= 6: E('terms count')
for i, w in enumerate(it['watch']):
    for k in ['n', 'why', 'where']:
        if k not in w: E(f'watch[{i}] missing {k}')
        emph_check(f'watch[{i}].{k}', w.get(k, ''), need=False)
for i, p in enumerate(it['players']):
    for k in ['n', 't', 'm', 'role']:
        if k not in p: E(f'players[{i}] missing {k}')
        emph_check(f'players[{i}].{k}', str(p.get(k, '')), need=False)
for i, t in enumerate(it['terms']):
    for k in ['k', 'v']:
        if k not in t: E(f'terms[{i}] missing {k}')
        emph_check(f'terms[{i}].{k}', t.get(k, ''), need=False)
names = [n['name'] for n in d['nodes']]
for i, r in enumerate(it['reading']):
    emph_check(f'reading[{i}].means', r['means'])
    emph_check(f'reading[{i}].news', r['news'], need=False)
    plain = r['means'].replace('{{', '').replace('}}', '')
    if not any(nm in plain for nm in names): E(f'reading[{i}].means has no node name')

# --- nodes
ids = [n['id'] for n in d['nodes']]
if len(ids) != len(set(ids)): E(f'duplicate node ids {ids}')
if not 5 <= len(ids) <= 9: E(f'node count {len(ids)}')
for n in d['nodes']:
    nid = n['id']
    if not re.fullmatch(r'[a-z]{2,12}', nid): E(f'bad node id {nid}')
    if len(n.get('short', '')) > 6: E(f"{nid}: short >6 {n.get('short')}")
    for k in ['name', 'short', 'role', 'bottleneck', 'indicators', 'companies', 'state']:
        if k not in n: E(f'{nid}: missing {k}')
    emph_check(f'{nid}.role', n['role'])
    emph_check(f'{nid}.bottleneck', n['bottleneck'], lo=0.40, hi=0.70)
    if 'stage' in n and n['stage'] is not None and not (1 <= n['stage'] <= 8): E(f'{nid}: bad stage')
    if not 2 <= len(n['indicators']) <= 3: E(f'{nid}: indicators count {len(n["indicators"])}')
    for x in n['indicators']:
        if set(x) != {'n', 'src'}: E(f'{nid}: indicator keys {set(x)}')
    if not 2 <= len(n['companies']) <= 5: E(f'{nid}: companies count {len(n["companies"])}')
    for c in n['companies']:
        for k in ['n', 't', 'm', 'note']:
            if k not in c: E(f'{nid}: company missing {k}')
        emph_check(f"{nid}.company[{c['n']}]", c['note'], lo=0.40, hi=0.75)
    for l in n.get('links', []):
        if l.get('to') not in allowed_links: E(f"{nid}: link not allowed {l.get('to')}")
        if not l.get('why'): E(f'{nid}: link without why')
    if len(n['state']) > 3: E(f'{nid}: state >3')
    for i, s in enumerate(n['state']):
        for k in ['d', 'o', 't', 'u']:
            if not s.get(k): E(f'{nid}.state[{i}] missing {k}')
        if not DATE.match(s.get('d', '')): E(f'{nid}.state[{i}] bad date {s.get("d")}')
        if not re.search(r'\[(사실|귀납|유추|추측|연역)\]', s['t']): W(f'{nid}.state[{i}] no tag')
        emph_check(f'{nid}.state[{i}]', s['t'], lo=0.40, hi=0.75)

# --- cycle
c = d['cycle']
if not (isinstance(c['stage'], int) and 1 <= c['stage'] <= 8): E('cycle.stage out of range')
if c['conf'] not in ('높음', '중간', '낮음'): E('cycle.conf')
if not 2 <= len(c['why']) <= 4: E('cycle.why count')
for i, w in enumerate(c['why']):
    if not w.get('src'): E(f'cycle.why[{i}] no src')
    for s in w.get('src', []):
        if not s.get('o') or not s.get('u'): E(f'cycle.why[{i}] src missing o/u')
        if not DATE.match(s.get('d', '')): E(f'cycle.why[{i}] src bad date')
    if not re.search(r'\[(사실|귀납|유추|추측|연역)\]', w['t']): E(f'cycle.why[{i}] no tag')
    emph_check(f'cycle.why[{i}]', w['t'])
emph_check('cycle.next', c['next'])
if not re.search(r'\[(유추|추측|귀납|사실)\]', c['next']): E('cycle.next no tag')
if not 3 <= len(c['watch']) <= 5: E('cycle.watch count')
for sp in c.get('split', []):
    if not 1 <= sp['stage'] <= 8: E('split stage')
    for x in sp['nodes']:
        if x not in ids: E(f'split node unknown {x}')

# --- industryState
if not 2 <= len(d['industryState']) <= 5: E('industryState count')
for i, s in enumerate(d['industryState']):
    for k in ['d', 'kind', 'o', 't', 'u']:
        if not s.get(k): E(f'industryState[{i}] missing {k}')
    if s.get('kind') not in ('price', 'supply', 'demand', 'capex', 'policy'): E(f'industryState[{i}] kind {s.get("kind")}')
    if not DATE.match(s.get('d', '')): E(f'industryState[{i}] bad date')

# --- forbidden domains in any u (cited only from desk news is allowed but flagged)
txt = json.dumps(d, ensure_ascii=False)
for m in re.findall(r'"u": "([^"]+)"', txt):
    if 'reuters.com' in m or 'bloomberg.com' in m: W(f'desk-news URL cited (not opened): {m[:90]}')

print('NODES:', ids)
print('cycle:', c['stage'], c['conf'], 'split:', [(s['stage'], s['nodes']) for s in c.get('split', [])])
print('--- ratios (no-space, with-space)')
for w, r, r2 in ratios:
    print(f'{r:.2f} {r2:.2f}  {w}')
print('--- ERRORS', len(errs))
for e in errs: print('E', e)
print('--- WARNINGS', len(warns))
for w in warns: print('W', w)
