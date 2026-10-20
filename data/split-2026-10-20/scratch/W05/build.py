import json, os, sys, runpy
H = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(H, '..', '..', 'wout', 'W05.json')
allx = []
for i in range(1, 7):
    p = os.path.join(H, f'b{i}.py')
    if os.path.exists(p):
        allx += runpy.run_path(p)['B']
TAILS = (' (제목 기준)', ' (채널 전언)')
for x in allx:
    core = x['one']
    for t in TAILS:
        if core.endswith(t): core = core[:-len(t)]
    print(x['c'], 'T', len(x['title']), 'O', len(core), 'F', len(x['facts']), [len(v['t']) for v in x['vc']])
json.dump(allx, open(OUT, 'w'), ensure_ascii=False, indent=1)
print('saved', len(allx))
