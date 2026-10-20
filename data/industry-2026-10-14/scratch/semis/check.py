"""out/<id>.json 형식·강조 검사 (BUILD.md 3-4단계용). 사용: python3 -I check.py <out.json> <news.tsv> <map.tsv>"""
import json, re, sys, collections

p, newsf, mapf = sys.argv[1], sys.argv[2], sys.argv[3]
d = json.load(open(p, encoding='utf-8'))
P, W = [], []
LBL = re.compile(r'\s*\[(사실|귀납|연역|유추|추측)[^\]]*\]\s*\.?\s*$')
strip = lambda s: s.replace('{{', '').replace('}}', '')

def hl(name, s, lo=None, hi=None):
    if s is None: return
    raw = s
    s = LBL.sub('', s)
    if raw.count('{{') != raw.count('}}') or re.search(r'\{\{[^}]*\{\{', raw) or '{{}}' in raw:
        P.append(f'{name}: 괄호 짝')
    marks = re.findall(r'\{\{(.+?)\}\}', s)
    n = len(strip(s)); h = sum(len(m) for m in marks)
    for m in marks:
        if m != m.strip(): P.append(f'{name}: 공백 시작/끝 "{m}"')
        if re.search(r'\[(사실|귀납|연역|유추|추측)', m): P.append(f'{name}: 꼬리표 강조 "{m}"')
        if m.count('(') != m.count(')'): W.append(f'{name}: 괄호 안 닫힘 "{m}"')
        if len(m) > 30: W.append(f'{name}: 덩어리 김({len(m)}) "{m}"')
        if re.match(r'^[,.)·]|[,(]$', m): W.append(f'{name}: 문장부호 시작/끝 "{m}"')
    if re.search(r'\}\}\{\{', raw): W.append(f'{name}: 강조가 붙어 있음')
    r = h / max(1, n)
    if lo is not None and n >= 20 and not (lo <= r <= hi): W.append(f'{name}: 강조 비율 {r:.0%}')
    return r

def nohl(name, s):
    if s and ('{{' in s or '}}' in s): P.append(f'{name}: 강조 금지 칸에 강조')

# 최상위
for k in ['id', 'name', 'short', 'icon', 'order', 'asOf', 'rev', 'summary', 'intro', 'nodes', 'cycle', 'industryState', 'insight', 'flows', 'gaps', 'history']:
    if k not in d: P.append(f'필드 없음: {k}')
if len(d['short']) > 6: P.append('short 6자 초과')
if d['insight'] != {} or d['flows'] != []: P.append('insight/flows 형식')
hl('summary', d['summary'], 0.45, 0.70)
ns = len(re.findall(r'[.!?](?=\s|$)', strip(LBL.sub('', d['summary']))))
print('summary 문장 수', ns)

it = d['intro']
rat = {}
for k in ['what', 'money', 'drivers']:
    rat[k] = hl('intro.' + k, it[k], 0.50, 0.65)
    print(f'intro.{k} 문장 수', len(re.findall(r'[.!?](?=\s|$)', strip(it[k]))), f'강조 {rat[k]:.0%}')
for i, w in enumerate(it['watch']):
    for f in ['n', 'why', 'where']:
        if not w.get(f): P.append(f'watch{i}.{f} 없음')
        nohl(f'watch{i}.{f}', w.get(f))
for i, x in enumerate(it['players']):
    for f in ['n', 't', 'm', 'role']:
        if f not in x: P.append(f'players{i}.{f} 없음')
        nohl(f'players{i}.{f}', x.get(f))
names = [n['name'] for n in d['nodes']]
for i, r in enumerate(it['reading']):
    nohl(f'reading{i}.news', r['news'])
    rr = hl(f'reading{i}.means', r['means'], 0.50, 0.65)
    print(f'reading{i} 강조 {rr:.0%}')
    if not any(nm in strip(r['means']) for nm in names): P.append(f'reading{i}: 노드 이름 없음')
for i, t in enumerate(it['terms']):
    nohl(f'terms{i}', t['k']); nohl(f'terms{i}', t['v'])
cnt = {k: len(it[k]) for k in ['watch', 'players', 'reading', 'terms']}
print('intro 개수', cnt)
for k, (a, b) in {'watch': (3, 5), 'players': (5, 8), 'reading': (3, 5), 'terms': (3, 6)}.items():
    if not a <= cnt[k] <= b: P.append(f'intro.{k} 개수 {cnt[k]}')

# 노드
ids = [n['id'] for n in d['nodes']]
if len(ids) != len(set(ids)): P.append('노드 id 중복')
if not 5 <= len(ids) <= 9: P.append(f'노드 수 {len(ids)}')
for n in d['nodes']:
    nid = n['id']
    if not re.fullmatch(r'[a-z]{2,12}', nid): P.append(f'{nid}: id 형식')
    if len(n['short']) > 6: P.append(f'{nid}: short 6자 초과 {n["short"]}')
    if 'stage' in n and n['stage'] is not None and not 1 <= n['stage'] <= 8: P.append(f'{nid}: stage 범위')
    hl(f'{nid}.role', n['role'], 0.40, 0.70)
    hl(f'{nid}.bottleneck', n['bottleneck'], 0.40, 0.70)
    if not 2 <= len(n['indicators']) <= 3: P.append(f'{nid}: indicators {len(n["indicators"])}')
    if not 2 <= len(n['companies']) <= 5: P.append(f'{nid}: companies {len(n["companies"])}')
    for c in n['companies']:
        for f in ['n', 't', 'm', 'note']:
            if f not in c: P.append(f'{nid}: company {f} 없음')
        hl(f'{nid}.co.{c["n"]}', c['note'])
    for l in n.get('links', []):
        if not re.fullmatch(r'[a-z]+/[a-z]+', l.get('to', '')): P.append(f'{nid}: link 형식 {l}')
        nohl(f'{nid}.link', l.get('why'))
    if len(n.get('state', [])) > 3: P.append(f'{nid}: state 3개 초과')
    for s in n.get('state', []):
        for f in ['d', 'o', 't', 'u']:
            if not s.get(f): P.append(f'{nid}: state {f} 없음')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', s.get('d', '')): P.append(f'{nid}: state 날짜 형식 {s.get("d")}')
        if not re.search(r'\[(사실|귀납|연역|유추|추측)\]\s*$', s['t']): W.append(f'{nid}: state 꼬리표 없음')
        hl(f'{nid}.state', s['t'], 0.35, 0.75)

# 국면
cy = d['cycle']
if not (isinstance(cy['stage'], int) and 1 <= cy['stage'] <= 8): P.append('cycle.stage 범위')
if cy['conf'] not in ('높음', '중간', '낮음'): P.append('cycle.conf')
if not 2 <= len(cy['why']) <= 4: P.append(f'cycle.why {len(cy["why"])}줄')
for i, w in enumerate(cy['why']):
    if not w.get('src'): P.append(f'why{i}: src 없음')
    for s in w.get('src', []):
        if not s.get('o') or not s.get('u'): P.append(f'why{i}: src o·u 없음')
        if not re.fullmatch(r'\d{4}-\d{2}-\d{2}', s.get('d', '')): P.append(f'why{i}: src 날짜 형식')
    if not re.search(r'\[(사실|귀납|연역|유추|추측)\]\s*$', w['t']): P.append(f'why{i}: 꼬리표 없음')
    hl(f'why{i}', w['t'], 0.40, 0.70)
hl('next', cy['next'], 0.40, 0.70)
if not 3 <= len(cy['watch']) <= 5: P.append('cycle.watch 개수')
for sp in cy.get('split', []):
    if not 1 <= sp['stage'] <= 8: P.append('split stage')
    for x in sp['nodes']:
        if x not in ids: P.append(f'split 노드 없음 {x}')
if not 2 <= len(d['industryState']) <= 5: P.append('industryState 개수')
for s in d['industryState']:
    if s['kind'] not in ('price', 'supply', 'demand', 'capex', 'policy'): P.append('industryState kind')
    for f in ['d', 'o', 't', 'u']:
        if not s.get(f): P.append(f'industryState {f} 없음')
    nohl('industryState', s['t'])

# 뉴스가 모두 노드에 붙는지(scratch 지도)
news = [l.rstrip('\n').split('\t') for l in open(newsf, encoding='utf-8') if l.strip()]
mp = [l.rstrip('\n').split('\t') for l in open(mapf, encoding='utf-8') if l.strip()]
keys = [n[1] if n[1] != '(되살릴 기사)' else n[3] for n in news]
m = {a: b for a, b in mp}
miss = [k for k in keys if k not in m]
bad = [v for v in m.values() if v not in ids]
print('뉴스', len(keys), '지도', len(m), '빠짐', len(miss), '없는 노드', bad, collections.Counter(m.values()))
if miss or bad: P.append('뉴스 지도 불일치')

# 링크 대상 확인(기존 페이지·같은 묶음 새 페이지)
print('links', [(n['id'], l['to']) for n in d['nodes'] for l in n.get('links', [])])
print('PROBLEMS', len(P)); [print(' !', x) for x in P]
print('WARN', len(W)); [print(' ~', x) for x in W]
