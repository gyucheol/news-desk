import json, glob, runpy, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
W = json.load(open(f'{H}/../../win/W12.json'))
order = [c['c'] for c in W['clusters']]
n = {c['c']: len(c['items']) for c in W['clusters']}
got = {}
for p in sorted(glob.glob(f'{H}/p*.py')):
    for x in runpy.run_path(p)['L']:
        got[x['c']] = x
out = []
for c in order:
    if c in got:
        x = got[c]
        x['vc'] = [dict(zip(('ind','node','f','dir','k','t'), v)) for v in x['vc']]
        out.append(x)
json.dump(out, open(f'{H}/../../wout/W12.json', 'w'), ensure_ascii=False, indent=1)
for x in out:
    one = re.sub(r' \((제목 기준|채널 전언)\)$', '', x['one'])
    print(x['c'], n[x['c']], 'T', len(x['title']), 'O', len(one), 'vc', [len(v['t']) for v in x['vc']])
print(len(out))
