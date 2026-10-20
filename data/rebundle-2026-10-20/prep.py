"""안 읽은 문서(보호 제외)의 기사를 줄 단위로 펼쳐 주제별 묶기 입력(in/G*.tsv)을 만든다.
사용: python3 -I prep.py <DB 사본>  → lines.json, scope.json, in/G1..G3.tsv"""
import json, re, sys, glob, collections
from datetime import datetime
DB = sys.argv[1]
r = json.load(open(f'{DB}/data/users/me/reads.json'))['ids']
q = json.load(open(f'{DB}/data/users/me/detailReq.json')); PR = set(q['ids']) | set(q['sent'])
U = []
for p in sorted(glob.glob(f'{DB}/news/*.json')):
    d = json.load(open(p))
    t = datetime.fromisoformat(d.get('updatedAt') or d['published']).timestamp() * 1000
    if r.get(d['id']) is not None and r[d['id']] >= t: continue
    if d.get('detail') or d.get('insight2') or d['id'] in PR: continue
    U.append(d)
GEO = {'oil', 'gas', 'coal', 'drilling', 'petchem', 'shipping', 'agri', 'aero', 'uranium', 'power', 'utilities'}
MAC = {'macro', 'fin', 'jpins', 'realestate', 'semis', 'tech'}
def grp(d):
    i = d.get('inds') or ['x']
    txt = (d.get('title') or d.get('headline') or '') + ' '.join(it.get('t', '') for it in d.get('items') or [])
    if re.search(r'이란|후티|호르무즈|이스라엘|사우디|러시아|우크라|젤렌스키|푸틴|크렘린|예멘|홍해|중동', txt): return 'G1'
    if i[0] in GEO: return 'G1'
    if i[0] in MAC: return 'G2'
    return 'G3'
clean = lambda s: re.sub(r'\s+', ' ', (s or '').replace('{{', '').replace('}}', '')).strip()
lines, out, k = {}, collections.defaultdict(list), 0
for d in sorted(U, key=lambda d: d['id']):
    g = grp(d); its = d.get('items') or []
    rows = [(j, it.get('d', ''), it.get('o', ''), clean(it.get('t')), clean(it.get('s')), it['u']) for j, it in enumerate(its)] or \
           [(-1, d['published'][:10], d.get('source', ''), clean(d.get('headline')), '', d.get('url', ''))]
    if len(its) == 1 and not rows[0][4]: rows = [(0, its[0].get('d', ''), its[0].get('o', ''), clean(its[0].get('t')), clean(d.get('one')), its[0]['u'])]
    for j, dd, o, t, s, u in rows:
        k += 1; key = f'b{k:04d}'
        lines[key] = {'doc': d['id'], 'j': j, 'd': dd, 'o': o, 't': t, 's': s, 'u': u, 'g': g}
        out[g].append(f"{key}\t{d['id']}\t{dd}\t{o}\t{t}\t{s}")
json.dump(lines, open('lines.json', 'w'), ensure_ascii=False, indent=0)
json.dump({'unread': [d['id'] for d in U]}, open('scope.json', 'w'), ensure_ascii=False, indent=0)
for g in sorted(out):
    open(f'in/{g}.tsv', 'w').write('키\t지금 문서\t날짜\t출처\t제목\t원문별 한줄(s)\n' + '\n'.join(sorted(out[g], key=lambda l: (l.split('\t')[2], l))) + '\n')
    print(g, len(out[g]))
print('docs', len(U), 'articles', len(lines))
