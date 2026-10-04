import json, glob, re, os, sys
NODES = {'uranium': 'build conversion enrichment fabrication mining operators physical policy',
 'drilling': 'capex fpso octg osv rigs services subsea yards',
 'gas': 'demand liquefaction midstream regas shipping trade upstream',
 'coal': 'logistics met policy power steel thermal trade',
 'power': 'demand developers gen grid market modules polysilicon storage wind',
 'petchem': 'commodity cracker demand feedstock policy specialty',
 'jpins': 'assets capital demand rates regulation reinsurance securities underwriting',
 'beauty': 'brands channels exports materials odm packaging',
 'macro': 'cb rates fiscal inflation growth semis fx liquidity commodity geo'}
NODES = {k: set(v.split()) for k, v in NODES.items()}
MAXST = {'macro': 4}  # 매크로는 성장·물가 4국면(1 골디락스 2 과열·긴축 3 스태그플레이션 4 침체·완화), 나머지는 자본순환 8국면
LBL = re.compile(r'\[(사실|귀납|연역|유추|추측)[^\]]*\]\s*$'); RUN = re.compile(r'\S{41,}')
KEYLINE = re.compile(r'^[^:{}\[\]]{1,8}:\s')
def chk(w, s, label=True):
    P = []
    if not isinstance(s, str): return [w + ':문자열 아님']
    if '|' in s or '**' in s: P.append('금지문자')
    if s.count('{{') != s.count('}}') or re.search(r'\{\{[^}]*\{\{', s) or '{{}}' in s: P.append('강조짝')
    m = RUN.search(s)
    if m and not m.group(0).startswith('http'): P.append('40자')
    if label and not LBL.search(s): P.append('레이블없음:' + s[-14:])
    return [w + ':' + p for p in P]
seen_urls = set()
if os.path.exists('seen.txt'):
    for l in open('seen.txt'):
        if ' | ' in l: seen_urls.add(l.rsplit(' | ', 1)[1].strip())
verbose = '-v' in sys.argv
allP = []; W = []; n = 0; rows = []
for p in sorted(glob.glob('cards/*.json')):
    k = os.path.basename(p)[:-5]; c = json.load(open(p)); P = []; n += 1
    if c.get('key') != k: P.append('key 불일치')
    miss = [f for f in ['source', 'published', 'url', 'inds', 'nodes', 'headline', 'facts', 'tags', 'cycles', 'incentive', 'check', 'src'] if f not in c]
    if miss: allP.append(f'{k}: 필드없음 {miss}'); continue
    src = c['source']
    if src not in ('텔레그램', '블룸버그', '로이터'): P.append('source')
    if src == '텔레그램':
        if not c.get('channel'): P.append('channel 없음')
        if not re.match(r'^\d{4}-\d\d-\d\dT\d\d:\d\d:\d\d\+09:00$', c['published']): P.append('published는 한국 시간 +09:00')
    elif not re.match(r'^\d{4}-\d\d-\d\d', c['published']): P.append('published 날짜')
    if not c['inds'] or any(i not in NODES for i in c['inds']): P.append('inds')
    P += chk('headline', c['headline'], label=False)
    if not (3 <= len(c['facts']) <= 6): P.append(f'facts {len(c["facts"])}줄(3~6)')
    for i, x in enumerate(c['facts']):
        P += chk(f'facts{i}', x)
        if isinstance(x, str) and not KEYLINE.match(x): P.append(f'facts{i}:항목명(1~8자+콜론) 없음')
    if not c['facts'] or not c['facts'][0].startswith('무엇이:'): P.append('첫줄 무엇이 아님')
    if len(c['tags']) > 3: P.append('tags 3개 초과')
    for x in c['tags']:
        P += chk('tag', x['t'])
        if not (0 <= x['s'] <= 7): P.append('tag s')
    if not c['cycles']: P.append('cycles 없음')
    for x in c['cycles']:
        P += chk('cyc', x['why'])
        if x['ind'] not in NODES or not (1 <= x['stage'] <= MAXST.get(x['ind'], 8)): P.append('cycles ind/stage')
        elif x['ind'] not in c['inds']: P.append('cycles 산업이 inds에 없음 ' + x['ind'])
    P += chk('incentive', c['incentive'])
    if c['check']: P += chk('check', c['check'])
    for nd in c['nodes']:
        a, _, b = nd.partition('/')
        if a not in NODES or b not in NODES[a]: P.append('노드 ' + nd)
        elif a not in c['inds']: P.append('노드 산업이 inds에 없음 ' + nd)
    if c.get('insight'): P.append('insight는 비워 둠')
    if src in ('블룸버그', '로이터') and '원문 미확인' not in c['check'] and '사용자 제공' not in c['check']: P.append('원문 미확인(또는 사용자 제공) 표기 없음')
    if not c['src'] or not c['src'][0].get('u'): P.append('src')
    if c.get('dupOf') and '이미 다룬 사건(' not in c['facts'][0]: P.append('dupOf인데 첫 줄에 이미 다룬 사건 표기 없음')
    if c['url'] in seen_urls and not c.get('dupOf'): W.append(f'{k}: 이미 다룬 주소(seen) — 중복이면 빼거나 dupOf')
    body = ' '.join(c['facts']); hl = sum(len(x) for x in re.findall(r'\{\{(.+?)\}\}', body)); tot = len(body.replace('{{', '').replace('}}', '')) or 1
    if hl / tot < 0.18: W.append(f'{k}: 강조 적음 {hl / tot:.2f}')
    rows.append(f"{k} {src} {c['published'][:16]} f={len(c['facts'])} cyc={[(x['ind'], x['stage']) for x in c['cycles']]} hl={hl / tot:.2f}")
    allP += [f'{k}: {x}' for x in P]
if verbose: print('\n'.join(rows))
print('cards', n, 'PROBLEMS', len(allP), 'WARN', len(W))
for x in allP: print(' -', x)
for x in W: print(' ~', x)
