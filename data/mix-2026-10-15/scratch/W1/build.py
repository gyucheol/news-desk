import json, re, sys
B = '/home/user/news-desk/data/mix-2026-10-15/bundle/W1.md'
OUT = '/home/user/news-desk/data/mix-2026-10-15/out2/W1.json'
txt = open(B, encoding='utf-8').read()
clusters = {}
cur = None
for line in txt.splitlines():
    m = re.match(r'^## (G\d-\d+) .*attachTo: "([^"]*)"', line)
    if m:
        cur = m.group(1); clusters[cur] = {'attach': m.group(2), 'items': []}; continue
    m = re.match(r'^### (.*) · (\d\d)-(\d\d) [0-9:]+ KST · (\S+)$', line)
    if m and cur:
        src = m.group(1).strip()
        o = src if src in ('블룸버그', '로이터') else src
        clusters[cur]['items'].append({'o': o, 'd': '2026-%s-%s' % (m.group(2), m.group(3)), 'u': m.group(4)})

D = json.load(open(sys.argv[1], encoding='utf-8'))
items = []
for c in D['items']:
    cid = c['cid']; meta = clusters[cid]
    c['attachTo'] = meta['attach']
    ts = c.pop('ts')
    assert len(ts) == len(meta['items']), (cid, len(ts), len(meta['items']))
    its = []
    for (t, s), b in zip(ts, meta['items']):
        it = {'t': t, 'o': b['o'], 'd': b['d'], 'u': b['u']}
        if s: it['s'] = s
        its.append(it)
    c['items'] = its
    # fed u by index
    for f in c.get('fed', []):
        if isinstance(f['u'], int):
            f['u'] = meta['items'][f['u']]['u']
    items.append(c)
out = {'agent': 'W1', 'searches_used': D['searches_used'], 'fetches_used': D['fetches_used'], 'items': items, 'skipped': D.get('skipped', [])}
json.dump(out, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

tail = re.compile(r' \((제목 기준|채널 전언)\)$')
def L(x): return len(tail.sub('', x))
bad = []
for c in items:
    multi = len(c['items']) > 1 or c['attachTo']
    lo, hi = (90, 160) if multi else (80, 130)
    if not (20 <= len(c['title']) <= 50): bad.append((c['cid'], 'title', len(c['title'])))
    if not (lo <= L(c['one']) <= hi): bad.append((c['cid'], 'one', L(c['one'])))
    if not c['one'].rstrip(' (제목 기준)(채널 전언)').endswith('다') and not tail.sub('', c['one']).endswith('다'): bad.append((c['cid'], 'one-end'))
    if not (2 <= len(c['facts']) <= 5): bad.append((c['cid'], 'facts n'))
    for f in c['facts']:
        if '|' in f or '**' in f or not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f): bad.append((c['cid'], 'fact', f[:30]))
    if not c['facts'][0].startswith('무엇이:'): bad.append((c['cid'], 'fact0'))
    if multi:
        a = c.get('added', '')
        if not (60 <= L(a) <= 140): bad.append((c['cid'], 'added', L(a)))
    for it in c['items']:
        if not (25 <= len(it['t']) <= 60): bad.append((c['cid'], 'item t', len(it['t']), it['t']))
        if multi:
            s = it.get('s', '')
            if not (45 <= L(s) <= 110) or not tail.sub('', s).endswith('다'): bad.append((c['cid'], 'item s', L(s), s[:40]))
    for v in c['vc']:
        if not (12 <= len(v['t']) <= 45): bad.append((c['cid'], 'vc t', len(v['t']), v['t']))
    for f in c.get('fed', []):
        if not (20 <= len(f['t']) <= 70) or not f['t'].endswith('다'): bad.append((c['cid'], 'fed t', len(f['t']), f['t']))
    s = json.dumps(c, ensure_ascii=False)
    if '{{' in s or '**' in s: bad.append((c['cid'], 'emph'))
for b in bad: print(b)
print('items', len(items), 'bad', len(bad))
