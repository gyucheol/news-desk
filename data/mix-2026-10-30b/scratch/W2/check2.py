"""mk_mix_ml.py의 check()를 DB 없이 흉내: python3 -I check2.py"""
import json, re
H = '/home/user/news-desk/data/mix-2026-10-30b'
O = json.load(open(f'{H}/out2/W2.json'))
VCN = json.load(open('/home/user/news-desk/tools/industry/nodes.json'))
LEG = {'macro', 'uranium', 'drilling', 'gas', 'coal', 'power', 'petchem', 'jpins', 'beauty'}
NEWIND = {'tech', 'auto', 'aero', 'agri', 'consumer', 'shipping', 'realestate', 'industrial', 'metals', 'oil', 'semis', 'utilities'}
when = {}
for l in open(f'{H}/all.tsv'):
    x = l.rstrip('\n').split('\t'); when[x[4]] = x[2]
P = []
used = set()
for x in O['items']:
    w = x['cid']; its = x['items']
    for v in x['vc']:
        if v['ind'] not in VCN or v['node'] not in VCN[v['ind']]: P.append(f'{w} vc 노드 {v}')
        if v['f'] not in ('공급', '수요', '가격', '-') or v['dir'] not in ('up', 'down', 'flat', 'mixed') or v['k'] not in ('실제', '예상'): P.append(f'{w} vc 값')
        if not 8 <= len(v['t']) <= 60 or any(c in v['t'] for c in '{}.\'"'): P.append(f'{w} vc t {v["t"]}')
    if len({(v['ind'], v['node'], v['f']) for v in x['vc']}) != len(x['vc']): P.append(f'{w} vc 같은 노드·f 중복')
    for nd in x['nodes']:
        i, _, k = nd.partition('/')
        if i not in LEG or k not in VCN.get(i, []): P.append(f'{w} node {nd}')
        if i not in x['inds']: P.append(f'{w} inds에 {i} 없음')
    for i in x['inds']:
        if i not in LEG and i not in NEWIND: P.append(f'{w} ind {i}')
    for s in [x['title'], x['one'], x['check']] + x['facts'] + [x.get('added', '')] + [it['t'] + it.get('s', '') for it in its]:
        if '|' in s or '**' in s or '{{' in s: P.append(f'{w} 금지 문자')
    for f in x['facts']:
        if not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f.strip()): P.append(f'{w} 꼬리표 {f[-15:]}')
    if not 2 <= len(x['facts']) <= 5: P.append(f'{w} 사실 줄 수 {len(x["facts"])}')
    if x['basis'] in ('verified', 'partial') and not x['src']: P.append(f'{w} 독립 출처 없음')
    if x['attachTo']:
        a = re.sub(r' \((제목 기준|채널 전언)\)$', '', x.get('added', ''))
        if not (40 <= len(a) <= 140 and a.endswith('내용이 추가됨') and ' — ' in a): P.append(f'{w} added 형식')
        if x['basis'] == 'title' and not x['added'].endswith(' (제목 기준)'): P.append(f'{w} added 꼬리')
    elif x.get('added'): P.append(f'{w} 새 문서에 added')
    multi = len(its) > 1 or bool(x['attachTo'])
    for it in its:
        if it['u'] not in when: P.append(f'{w} 주소 후보에 없음 {it["u"]}')
        if it['u'] in used: P.append(f'{w} 주소 중복')
        used.add(it['u'])
        if multi:
            s = re.sub(r' \((제목 기준|채널 전언)\)$', '', it.get('s', ''))
            if not (45 <= len(s) <= 110 and s.endswith('다')): P.append(f'{w} s {len(s)}')
            if it['o'] == '블룸버그' and x['basis'] == 'title' and not it['s'].endswith(' (제목 기준)'): P.append(f'{w} s 꼬리')
        elif it.get('s'): P.append(f'{w} 한 건짜리에 s')
        if not 25 <= len(it['t']) <= 60: P.append(f'{w} item t {len(it["t"])}')
        if it['d'] != '2026-' + when.get(it['u'], '')[:5]: P.append(f'{w} 날짜 {it["d"]} {when.get(it["u"])}')
    ts = [when[it['u']] for it in its]
    if ts != sorted(ts): P.append(f'{w} 시각 순서')
    for f in x.get('fed') or []:
        if 'macro' not in x['inds'] or 'macro/cb' not in x['nodes'] or not any(v['ind'] == 'macro' and v['node'] == 'cb' for v in x['vc']): P.append(f'{w} fed 조건')
        if f['u'] not in {it['u'] for it in its} or not 15 <= len(f['t']) <= 80 or not f['t'].endswith('다'): P.append(f'{w} fed 항목')
print('문제', len(P)); [print(' -', p) for p in P]
