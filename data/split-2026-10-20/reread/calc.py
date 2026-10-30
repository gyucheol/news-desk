"""나누기 전 문서에서 사용자가 이미 읽은 기사를 찾는다.
기사가 원 문서에 붙은 시각 = 이전 회차 저장본(data/*/newsdocs) 가운데 그 기사가 처음 들어 있던 저장본의 updatedAt(없으면 published).
읽음 = reads[원 문서] >= 붙은 시각. 결과: reread/item_read.json, reread/docs.json"""
import json, glob, os, collections
from datetime import datetime
R = '/home/user/news-desk'
B = f'{R}/work/live32'  # 나누기 전 사본
reads = json.load(open(f'{B}/data/users/me/reads.json'))['ids']
lines = json.load(open(f'{R}/data/split-2026-10-20/lines.json'))
idmap = json.load(open(f'{R}/data/split-2026-10-20/idmap.json'))
ms = lambda s: datetime.fromisoformat(s if 'T' in s else s + 'T00:00:00+09:00').timestamp() * 1000
snaps = collections.defaultdict(list)  # doc -> [(time, set(urls))]
for p in glob.glob(f'{R}/data/*/newsdocs/*.json'):
    if '/split-2026-10-20/' in p: continue
    d = json.load(open(p)); t = d.get('updatedAt') or d.get('published')
    if not t: continue
    us = {it['u'] for it in d.get('items') or []} or {d.get('url')}
    snaps[d['id']].append((ms(t), us, p))
# 현재(나누기 전) 문서도 하나의 저장본으로
for i in {x['doc'] for x in lines.values()}:
    d = json.load(open(f'{B}/news/{i}.json'))
    us = {it['u'] for it in d.get('items') or []} or {d.get('url')}
    snaps[i].append((ms(d.get('updatedAt') or d['published']), us, 'live32'))
# 합치기(10월 9일·20일)로 흡수된 문서: 그 문서에서 읽은 기사도 읽은 것으로
absorbed = collections.defaultdict(list)
for f in ('merge-2026-10-09', 'merge-2026-10-20'):
    for g in json.load(open(f'{R}/data/{f}/merged.json')): absorbed[g['keep']] += g['absorb']
def anc(d, seen=None):
    seen = seen or set()
    for a in absorbed.get(d, []):
        if a not in seen: seen.add(a); anc(a, seen)
    return seen
res, via = {}, collections.Counter()
for k, x in lines.items():
    D, u = x['doc'], x['u']
    at = min(t for t, us, _ in snaps[D] if u in us)
    rd = reads.get(D); read = bool(rd) and rd >= at
    if not read:
        for C in anc(D):
            ts = [t for t, us, _ in snaps[C] if u in us]
            if ts and reads.get(C) and reads[C] >= min(ts): read = True; via[C] += 1; break
    res[k] = {'doc': D, 'u': u, 'attach': at, 'read': read}
json.dump(res, open(f'{R}/data/split-2026-10-20/reread/item_read.json', 'w'), indent=0)
# 새 문서별
u2d = idmap['url_doc']
by = collections.defaultdict(list)
for k, r in res.items():
    nd = u2d.get(r['u'])
    if nd: by[nd].append(r['read'])
full = sorted(d for d, v in by.items() if all(v)); part = sorted(d for d, v in by.items() if any(v) and not all(v))
json.dump({'full': full, 'part': part, 'part_counts': {d: [sum(by[d]), len(by[d])] for d in part}}, open(f'{R}/data/split-2026-10-20/reread/docs.json', 'w'), indent=0)
print('흡수 문서 경유', sum(via.values()), dict(via)); print('기사', len(res), '읽었던 기사', sum(r['read'] for r in res.values()))
print('원 문서 중 읽음 기록 있음', len({r['doc'] for r in res.values() if reads.get(r['doc'])}))
print('새 문서', len(by), '모두 읽은 기사', len(full), '일부만', len(part), '안 읽음', len(by) - len(full) - len(part))
