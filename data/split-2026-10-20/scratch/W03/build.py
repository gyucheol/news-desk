import json, re, sys, os
H = '/home/user/news-desk/data/split-2026-10-20'
W = json.load(open(f'{H}/win/W03.json'))
n = {c['c']: len(c['items']) for c in W['clusters']}
order = [c['c'] for c in W['clusters']]
L = []
for f in sys.argv[1:]:
    g = {}; exec(open(f'{H}/scratch/W03/{f}').read(), g)
    L += g.get('A', []) + g.get('B', []) + g.get('C', [])
by = {x['c']: x for x in L}
out = [by[c] for c in order if c in by]
for x in out:
    core = re.sub(r' \((제목 기준|채널 전언)\)$', '', x['one'])
    print(x['c'], n[x['c']], 'title', len(x['title']), 'one', len(core), [len(v['t']) for v in x['vc']])
json.dump(out, open(f'{H}/wout/W03.json', 'w'), ensure_ascii=False, indent=1)
print('saved', len(out))
