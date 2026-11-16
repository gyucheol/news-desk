"""clusters_G1.json + clusters_G1b.json(add·새 묶음) + clusters_G2a.json + clusters_G2b.json → clusters.json.
같은 기존 문서(attachTo)를 고른 묶음이 여럿이면 하나로 합친다(줄·core 합침, 앞선 cid 유지). keep.tsv의 모든 줄이 한 번씩 들어갔는지 확인."""
import json
c1 = json.load(open('clusters_G1.json')); b = json.load(open('clusters_G1b.json'))
cl = {x['cid']: dict(x) for x in c1['clusters']}; drop = list(c1['drop'])
for a in b.get('add', []):
    x = cl[a['cid']]; x['lines'] = x['lines'] + a['lines']
    x['core'] = (x.get('core') or []) + [c for c in a.get('core_add') or [] if c not in (x.get('core') or [])]
for x in b.get('clusters', []): cl[x['cid']] = dict(x)
drop += b.get('drop', [])
for g in ('G2a', 'G2b'):
    c = json.load(open(f'clusters_{g}.json'))
    for x in c['clusters']: cl[x['cid']] = dict(x)
    drop += c['drop']
by = {}
for cid in list(cl):
    t = cl[cid].get('attachTo')
    if not t: continue
    if t in by:
        k = cl[by[t]]; x = cl.pop(cid)
        k['lines'] = k['lines'] + x['lines']; k['core'] = (k.get('core') or []) + [c for c in x.get('core') or [] if c not in (k.get('core') or [])]
        k['theme'] = k['theme'] if x['theme'] in k['theme'] else k['theme'] + '·' + x['theme']
        print('합침', by[t], '+', cid, '→', t)
    else: by[t] = cid
keep = {int(l.split('\t')[0]) for l in open('keep.tsv')}
used = [l for x in cl.values() for l in x['lines']] + [d['line'] for d in drop]
assert len(used) == len(set(used)), '중복 줄'
miss = keep - set(used); extra = set(used) - keep
print('묶음', len(cl), 'attach', sum(1 for x in cl.values() if x.get('attachTo')), 'drop', len(drop), '누락', sorted(miss)[:20], '남는 줄', sorted(extra)[:20])
json.dump({'clusters': list(cl.values()), 'drop': drop}, open('clusters.json', 'w'), ensure_ascii=False, indent=1)
