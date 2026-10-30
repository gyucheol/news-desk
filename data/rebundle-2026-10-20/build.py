"""주제별로 다시 묶은 묶음(plan.json + wout/W*.json)을 뉴스 문서로 조립한다. DB에 쓰지 않는다.
사용: python3 -I build_split.py <DB 사본> <오늘 YYYY-MM-DD>
- 작성(write) 묶음마다 문서 하나. 원 문서 id는 그 문서 기사를 가장 많이 가진 묶음이 이어받고(1:1),
  나머지 묶음은 새 id(첫 기사의 출처 n-tg/n-bbg/n-rtr/n-fed, progressV4.newsSeq 다음 번호).
- 어느 묶음도 이어받지 않은 원 문서는 삭제(deletes.txt).
- newsSeen*·chains의 문서 id는 기사 주소로 새 문서에 다시 연결(주소가 없으면 그 원 문서를 이어받은 문서, 없으면 기사를 가장 많이 받은 문서).
결과: newsdocs/<id>.json, deletes.txt, idmap.json, meta_out/*.json(바뀐 것만), chains_out/*.json(바뀐 것만)"""
import json, glob, os, re, sys, collections
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', 'tools'))
from bundle_attach import now_kst
DB, TODAY = sys.argv[1:3]
NOW = now_kst()
lines = json.load(open('lines.json')); plan = json.load(open('plan.json'))
scope = json.load(open('scope.json'))
W = {}
for p in sorted(glob.glob('wout/W*.json')):
    for x in json.load(open(p)): W[x['c']] = x
P = []
wr = [p for p in plan if p['mode'] == 'write']
for p in wr:
    if p['c'] not in W: P.append(f"작성 결과 없음 {p['c']}")
if P: print('\n'.join(P[:30])); sys.exit(1)
prog = json.load(open(f'{DB}/meta/progressV4.json')); seq = dict(prog['newsSeq'])
orig = {i: json.load(open(f'{DB}/news/{i}.json')) for i in {d for p in wr for d in p['docs']}}
for i in orig: assert i in scope['unread'], i
SRCN = {'bbg': '블룸버그', 'rtr': '로이터', 'tg': '텔레그램', 'fed': '연준 공식'}
clean = lambda s: (s or '').replace('{{', '').replace('}}', '')
def skind(u, o):
    if 't.me/' in u or o.startswith('텔레그램'): return 'tg'
    if 'bloomberg.com' in u or o.startswith('블룸버그'): return 'bbg'
    if 'reuters.com' in u or o.startswith('로이터'): return 'rtr'
    if o.startswith('연준'): return 'fed'
    return 'bbg' if o == '블룸버그' else 'rtr'

# 1) 원 문서 id 이어받기: (원 문서, 묶음) 쌍을 그 문서 기사 수가 많은 순으로 1:1 배정
pairs = []
for p in wr:
    cnt = collections.Counter(lines[k]['doc'] for k in p['m'])
    for d, n in cnt.items(): pairs.append((-n, d, p['c']))
pairs.sort()
keep_of, cl_id = {}, {}
for _, d, c in pairs:
    if d in keep_of or c in cl_id: continue
    keep_of[d] = c; cl_id[c] = d
# 2) 새 id
for p in sorted(wr, key=lambda p: p['c']):
    if p['c'] in cl_id: continue
    k0 = p['m'][0]; sk = skind(lines[k0]['u'], lines[k0]['o'])
    seq[sk] = seq.get(sk, 0) + 1; cl_id[p['c']] = f'n-{sk}-{seq[sk]:04d}'
deletes = sorted(set(orig) - set(keep_of))

# 3) 문서 조립
srcmap = {}
for i, d in orig.items():
    for j, s in enumerate(d.get('src') or []): srcmap[f'{i}#S{j+1}'] = {'o': s.get('o', ''), 'd': s.get('d', ''), 'u': s.get('u', '')}
docs, url2doc = {}, {}
for p in wr:
    x = W[p['c']]; did = cl_id[p['c']]; n = len(p['m'])
    its = []
    for k in p['m']:
        L = lines[k]; it = {'t': L['t'], 'o': L['o'], 'd': L['d'], 'u': L['u']}
        s = L['s'] or (x.get('s_add') or {}).get(L['u'], '')
        if n > 1 and s: it['s'] = s
        its.append(it); url2doc[L['u']] = did
    src = [srcmap[s] for s in x.get('src', []) if s in srcmap]
    k0 = p['m'][0]; sk = skind(lines[k0]['u'], lines[k0]['o'])
    if did in orig:
        d = json.loads(json.dumps(orig[did]))
        for f in ('added', 'channel'): d.pop(f, None)
        if d.get('format') == 'sum1': d.update({'cycles': [], 'tags': [], 'incentive': ''})  # 옛 단건 형식의 {{ }} 필드 정리
    else:
        primary = orig[p['docs'][0]]
        d = {'id': did, 'num': int(did[-4:]), 'key': f"rebundle-{p['c']}-{TODAY}", 'feed': 'v5', 'format': 'one1',
             'published': primary['published'], 'origTitle': '', 'cycles': [], 'tags': [], 'insight': {}, 'incentive': ''}
    if sk == 'tg' and not src:
        pass
    d.update({'format': 'one1', 'feed': 'v5', 'source': SRCN[sk], 'url': its[0]['u'], 'processed': TODAY, 'updatedAt': NOW,
              'title': x['title'], 'headline': x['title'], 'one': x['one'], 'facts': x['facts'], 'basis': x['basis'], 'check': x['check'],
              'src': src, 'items': its, 'inds': x.get('inds', []), 'nodes': x.get('nodes', []), 'vc': x.get('vc', [])})
    if sk == 'tg': d['channel'] = its[0]['o'].replace('텔레그램 ', '', 1)
    if x.get('fed'): d['fed'] = x['fed']
    else: d.pop('fed', None)
    if 'macro/semis' in d['nodes']: d['ind'] = 'semis'
    elif d.get('ind') == 'semis': d.pop('ind')
    docs[did] = d
    s = json.dumps(d, ensure_ascii=False)
    if '{{' in json.dumps({k: d[k] for k in ('title', 'one', 'facts', 'items', 'check')}, ensure_ascii=False): P.append(f'{did} 강조 남음')
    if len(s.encode()) > 200000: P.append(f'{did} 크기 {len(s.encode())}')

# 4) 원 문서 → 대표 새 문서 (주소로 못 찾을 때)
most = {}
for i in orig:
    c = collections.Counter(url2doc[lines[k]['u']] for k in lines if lines[k]['doc'] == i)
    most[i] = keep_of.get(i) and cl_id[keep_of[i]] or c.most_common(1)[0][0]
def remap(nid, u):
    if nid not in orig: return nid
    if u and u in url2doc: return url2doc[u]
    return most[nid]

# 5) newsSeen*
os.makedirs('meta_out', exist_ok=True); os.makedirs('chains_out', exist_ok=True); os.makedirs('newsdocs', exist_ok=True)
for f in glob.glob('meta_out/*.json') + glob.glob('chains_out/*.json') + glob.glob('newsdocs/*.json'): os.remove(f)
nseen = 0
for pth in sorted(glob.glob(f'{DB}/meta/newsSeen*.json')):
    m = json.load(open(pth)); ch = 0; out = []
    for l in m['lines']:
        a = l.split(' ', 2)
        if len(a) == 3 and a[1] in orig:
            u = l.rsplit(' | ', 1)[-1].strip(); nid = remap(a[1], u)
            if nid != a[1]: l = f'{a[0]} {nid} {a[2]}'; ch += 1
        out.append(l)
    if ch:
        m['lines'] = out; m['updated'] = TODAY
        json.dump(m, open(f'meta_out/{os.path.basename(pth)}', 'w'), ensure_ascii=False); nseen += ch
# 6) chains
nch = 0
def walk(o):
    global cnt
    if isinstance(o, dict):
        if isinstance(o.get('nid'), str) and o['nid'] in orig:
            nn = remap(o['nid'], o.get('u', ''))
            if nn != o['nid']: o['nid'] = nn; cnt += 1
        for v in o.values(): walk(v)
    elif isinstance(o, list):
        for v in o: walk(v)
for pth in sorted(glob.glob(f'{DB}/chains/*.json')):
    c = json.load(open(pth)); cnt = 0; walk(c)
    s = json.dumps(c, ensure_ascii=False)
    for i in deletes:
        if re.search(re.escape(i) + r'(?!\d)', s): P.append(f'{os.path.basename(pth)} 삭제 문서 {i} 글자로 남음')
    if cnt:
        json.dump(c, open(f'chains_out/{os.path.basename(pth)}', 'w'), ensure_ascii=False); nch += cnt

# 7) progressV4
bas = collections.Counter(d['basis'] for d in docs.values())
nnew = len([d for d in docs if d not in orig])
summary = (f'{TODAY}: 사용자 요청(같은 주제로 묶되 한줄 요약에 모든 핵심 사건을 숫자까지)으로 안 읽은 문서 {len(orig)}건(기사 {sum(len(p["m"]) for p in wr)}건)을 주제별로 다시 묶음'
           f'(data/rebundle-2026-10-20): 문서 {len(docs)}건(원 id 이어받음 {len(docs) - nnew}, 새 {nnew}), 삭제 {len(deletes)}. '
           f'verified {bas["verified"]}, partial {bas["partial"]}, channel {bas["channel"]}, title {bas["title"]}')
prog['newsSeq'] = seq; prog['log'] = (prog['log'] + [{'d': TODAY, 't': summary}])[-60:]
json.dump(prog, open('meta_out/progressV4.json', 'w'), ensure_ascii=False, indent=1)
for i, d in docs.items(): json.dump(d, open(f'newsdocs/{i}.json', 'w'), ensure_ascii=False, indent=1)
open('deletes.txt', 'w').write(''.join(f'{i}\n' for i in deletes))
json.dump({'cluster_doc': cl_id, 'url_doc': url2doc, 'most': most, 'deletes': deletes}, open('idmap.json', 'w'), ensure_ascii=False, indent=0)
print('PROBLEMS', len(P)); [print(' -', p) for p in P[:40]]
print(summary); print('newsSeen 줄 바꿈', nseen, 'chains 연결 바꿈', nch, 'seq', seq)
print('bytes', sum(os.path.getsize(f) for f in glob.glob('newsdocs/*.json')))
