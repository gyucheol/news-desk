import json, sys, glob, os
base = os.path.dirname(os.path.abspath(sys.argv[1]))
src = json.load(open(sys.argv[1], encoding='utf-8'))
order = [d['id'] for d in src]
docs = {}
for f in sorted(glob.glob(os.path.join(sys.argv[2], 'd_*.json'))):
    for d in json.load(open(f, encoding='utf-8')):
        docs[d['id']] = d
srcmap = {d['id']: d for d in src}
out = []
for i in order:
    if i not in docs: continue
    d = docs[i]
    o = {'id': i, 'title': d['title'], 'one': d['one']}
    if 'items' in srcmap[i]:
        o['added'] = d['added']
        us = [x['u'] for x in srcmap[i]['items']]
        o['items'] = [{'u': u, 's': s} for u, s in zip(us, d['s'])]
        if len(d['s']) != len(us): print('COUNT MISMATCH', i, len(d['s']), len(us))
    out.append(o)
json.dump({'docs': out}, open(sys.argv[3], 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('wrote', len(out))
