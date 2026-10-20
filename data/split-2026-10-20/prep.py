"""안 읽은 문서(보호 제외)의 기사를 줄 단위로 펼쳐 사건별 분류 입력(in/G*.tsv)을 만든다.
사용: python3 -I prep.py <DB 사본>  → lines.json(키→원문 정보), in/G1..G6.tsv"""
import json, re, sys, os
from datetime import datetime
DB = sys.argv[1]
r = json.load(open(f'{DB}/data/users/me/reads.json'))['ids']
q = json.load(open(f'{DB}/data/users/me/detailReq.json')); PR = set(q['ids']) | set(q['sent'])
import glob
U = []
for p in sorted(glob.glob(f'{DB}/news/*.json')):
    d = json.load(open(p))
    t = datetime.fromisoformat(d.get('updatedAt') or d['published']).timestamp() * 1000
    rd = r.get(d['id'])
    if rd is not None and rd >= t: continue
    if d.get('detail') or d.get('insight2') or d['id'] in PR: continue
    U.append(d)
G = {
 'G1': 'n-tg-0276 n-tg-0193 n-tg-0157 n-tg-0313 n-bbg-0357 n-tg-0056 n-bbg-0015 n-tg-0054 n-bbg-0022 n-bbg-0024',
 'G2': 'n-tg-0121 n-bbg-0353 n-tg-0314 n-bbg-0058 n-bbg-0100 n-rtr-0282 n-rtr-0033 n-rtr-0201 n-tg-0315 n-bbg-0352 n-tg-0256 n-bbg-0354 n-bbg-0350',
 'G3': 'n-tg-0294 n-tg-0118 n-tg-0210 n-tg-0311 n-tg-0233 n-tg-0136 n-tg-0292 n-rtr-0351 n-rtr-0358 n-bbg-0362 n-rtr-0364 n-tg-0312 n-rtr-0360 n-bbg-0103 n-tg-0316 n-bbg-0338 n-tg-0307 n-rtr-0181',
 'G4': 'n-bbg-0052 n-bbg-0111 n-tg-0201 n-bbg-0104 n-rtr-0314 n-bbg-0177 n-bbg-0359 n-bbg-0234 n-tg-0327',
 'G5': 'n-tg-0277 n-tg-0132 n-bbg-0116 n-rtr-0236 n-rtr-0362 n-tg-0325 n-tg-0326 n-tg-0317 n-bbg-0313 n-bbg-0233 n-bbg-0120 n-bbg-0361 n-rtr-0363 n-rtr-0056 n-rtr-0331 n-tg-0318 n-rtr-0118 n-bbg-0358 n-bbg-0363 n-bbg-0316 n-rtr-0024 n-rtr-0217 n-bbg-0122 n-bbg-0360 n-bbg-0280 n-rtr-0337',
}
grp = {i: g for g, s in G.items() for i in s.split()}
G2IND = {'petchem', 'gas', 'coal', 'drilling', 'oil', 'agri'}
G4IND = {'jpins'}
for d in U:
    if d['id'] in grp: continue
    i0 = (d.get('inds') or ['x'])[0]
    grp[d['id']] = 'G2' if i0 in G2IND else 'G4' if i0 in G4IND else 'G6'
clean = lambda s: re.sub(r'\s+', ' ', (s or '').replace('{{', '').replace('}}', '')).strip()
lines, out = {}, {g: [] for g in ['G1', 'G2', 'G3', 'G4', 'G5', 'G6']}
k = 0
for d in sorted(U, key=lambda d: d['id']):
    its = d.get('items') or []
    if its:
        for j, it in enumerate(its):
            k += 1; key = f'a{k:04d}'
            lines[key] = {'doc': d['id'], 'j': j, 'd': it.get('d', ''), 'o': it.get('o', ''), 't': clean(it.get('t')), 's': clean(it.get('s')), 'u': it['u']}
    else:
        k += 1; key = f'a{k:04d}'
        lines[key] = {'doc': d['id'], 'j': -1, 'd': d['published'][:10], 'o': d.get('source', ''), 't': clean(d.get('headline')), 's': '', 'u': d.get('url', '')}
for key, x in lines.items():
    g = grp[x['doc']]
    out[g].append(f"{key}\t{x['doc']}\t{x['d']}\t{x['o']}\t{x['t']}\t{x['s']}")
json.dump(lines, open('lines.json', 'w'), ensure_ascii=False, indent=0)
json.dump({'unread': [d['id'] for d in U], 'group': grp}, open('scope.json', 'w'), ensure_ascii=False, indent=0)
for g, L in out.items():
    open(f'in/{g}.tsv', 'w').write('키\t원 문서\t날짜\t출처\t제목\t원문별 한줄(s)\n' + '\n'.join(L) + '\n')
    print(g, len(L), len({l.split('\t')[1] for l in L}))
print('total', len(lines), 'docs', len(U))
