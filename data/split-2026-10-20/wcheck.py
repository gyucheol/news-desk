"""2단계 작성 결과 검사: python3 -I wcheck.py <이름>  (win/<이름>.json ↔ wout/<이름>.json)"""
import json, re, sys, os, glob
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', '..')
name = sys.argv[1]
W = json.load(open(f'{H}/win/{name}.json')); O = json.load(open(f'{H}/wout/{name}.json'))
VCN = json.load(open(f'{R}/tools/industry/nodes.json'))
OLD9 = {'uranium': 'mining conversion enrichment fabrication physical operators build policy', 'drilling': 'rigs capex services subsea fpso osv octg yards',
        'gas': 'upstream midstream liquefaction shipping regas trade demand', 'coal': 'thermal met logistics trade power steel policy',
        'power': 'demand gen grid storage wind modules polysilicon developers market', 'petchem': 'feedstock cracker commodity specialty demand policy',
        'jpins': 'underwriting reinsurance assets rates capital securities regulation demand', 'beauty': 'brands odm materials packaging channels exports',
        'macro': 'cb rates fiscal inflation growth fx liquidity commodity geo semis'}
OLD9 = {k: v.split() for k, v in OLD9.items()}
IND = set(VCN) | set(OLD9)
FED_KIND = ('발언', '연설', '인터뷰', '증언', '성명·의사록', '조사·보고서', '인사·독립성', '감독·규제', '관련 뉴스')
TAILS = {'title': ' (제목 기준)', 'channel': ' (채널 전언)'}
P = []
cl = {c['c']: c for c in W['clusters']}
srckeys = {s['k'] for d in W['docs'].values() for s in d.get('src', [])}
got = [x.get('c') for x in O]
if got != [c['c'] for c in W['clusters']]: P.append(f"순서·누락: 입력 {len(cl)} 출력 {len(O)} 빠짐 {sorted(set(cl)-set(got))[:10]} 남음 {sorted(set(got)-set(cl))[:5]}")
for x in O:
    w = x.get('c'); c = cl.get(w)
    if not c: continue
    n = len(c['items'])
    for k in ('title', 'one', 'facts', 'basis', 'check', 'inds', 'nodes', 'vc'):
        if k not in x: P.append(f'{w} {k} 없음')
    if any(k not in x for k in ('title', 'one', 'facts', 'basis')): continue
    allt = ' '.join([x['title'], x['one'], x.get('check', '')] + x['facts'])
    if '{{' in allt or '**' in allt or '|' in allt: P.append(f'{w} 금지 문자')
    if not 15 <= len(x['title']) <= 55: P.append(f"{w} title {len(x['title'])}자")
    tail = TAILS.get(x['basis'], '')
    one = x['one']
    if tail and not one.endswith(tail): P.append(f"{w} basis {x['basis']} 꼬리 없음")
    core = one[:-len(tail)] if tail and one.endswith(tail) else one
    if any(core.endswith(t) for t in TAILS.values()): P.append(f'{w} 꼬리가 basis와 다름')
    lo, hi = (80, 130) if n == 1 else (90, 160)
    if not lo - 5 <= len(core) <= hi + 5: P.append(f'{w} one {len(core)}자(기사 {n}건: {lo}~{hi})')
    if not core.endswith('다'): P.append(f'{w} one 끝맺음')
    if not 2 <= len(x['facts']) <= 5: P.append(f"{w} facts {len(x['facts'])}줄")
    if x['facts'] and not x['facts'][0].startswith('무엇이:'): P.append(f'{w} 첫 사실 줄이 무엇이: 아님')
    for f in x['facts']:
        if not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f.strip()): P.append(f'{w} 꼬리표 없는 사실 …{f[-15:]}')
    if x['basis'] not in ('verified', 'partial', 'title', 'channel'): P.append(f"{w} basis {x['basis']}")
    if x['basis'] in ('verified', 'partial') and not x.get('src'): P.append(f'{w} verified·partial인데 src 없음')
    for s in x.get('src', []):
        if s not in srckeys: P.append(f'{w} 없는 src 키 {s}')
    if x['basis'] == 'channel' and not any(it['o'].startswith('텔레그램') for it in c['items']): P.append(f'{w} channel인데 텔레그램 기사 없음')
    for nd in x.get('nodes', []):
        i, _, k = nd.partition('/')
        if k not in OLD9.get(i, []): P.append(f'{w} node {nd}(예전 9개 산업 노드만)')
        if i not in x.get('inds', []): P.append(f'{w} inds에 {i} 없음')
    for i in x.get('inds', []):
        if i not in IND: P.append(f'{w} ind {i}')
    vc = x.get('vc')
    if not isinstance(vc, list) or not 1 <= len(vc) <= 3: P.append(f'{w} vc 개수')
    else:
        for v in vc:
            i, nn = v.get('ind'), v.get('node')
            if i not in VCN: P.append(f'{w} vc 산업 {i}')
            elif nn not in VCN[i]: P.append(f'{w} vc 노드 {i}/{nn}')
            if v.get('f') not in ('공급', '수요', '가격', '-'): P.append(f"{w} vc f {v.get('f')}")
            if v.get('dir') not in ('up', 'down', 'flat', 'mixed'): P.append(f"{w} vc dir {v.get('dir')}")
            if v.get('k') not in ('실제', '예상'): P.append(f"{w} vc k {v.get('k')}")
            if not 8 <= len(v.get('t', '')) <= 60: P.append(f"{w} vc t {len(v.get('t', ''))}자")
    fed = x.get('fed')
    if fed:
        us = {it['u'] for it in c['items']}
        if 'macro' not in x.get('inds', []) or 'macro/cb' not in x.get('nodes', []): P.append(f'{w} fed인데 macro·macro/cb 없음')
        if not any(v.get('ind') == 'macro' and v.get('node') == 'cb' for v in vc or []): P.append(f'{w} fed인데 vc macro/cb 없음')
        for f in fed:
            if f.get('kind') not in FED_KIND: P.append(f"{w} fed kind {f.get('kind')}")
            if f.get('stance', '') not in ('매파', '비둘기파', '중립', ''): P.append(f"{w} fed stance")
            if not f.get('who') or not f.get('role'): P.append(f'{w} fed who·role 없음')
            if f.get('u') not in us: P.append(f'{w} fed 주소가 묶음 기사에 없음')
            t = f.get('t', '')
            if not 15 <= len(t) <= 80 or not t.endswith('다'): P.append(f'{w} fed t {len(t)}자')
print('묶음', len(O), '/', len(cl), '문제', len(P))
for p in P[:60]: print(' -', p)
