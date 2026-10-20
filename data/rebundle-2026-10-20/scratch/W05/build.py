import json, importlib.util
B='/home/user/news-desk/data/rebundle-2026-10-20/'
out=[]
for i in range(1,7):
    sp=importlib.util.spec_from_file_location(f'p{i}', f'{B}scratch/W05/p{i}.py'); m=importlib.util.module_from_spec(sp); sp.loader.exec_module(m); out+=m.OUT
W=json.load(open(B+'win/W05.json')); order=[c['c'] for c in W['clusters']]
d={x['c']:x for x in out}; out=[d[c] for c in order if c in d]
json.dump(out, open(B+'wout/W05.json','w'), ensure_ascii=False, indent=1)
for x in out:
    t=' (채널 전언)' if x['basis']=='channel' else (' (제목 기준)' if x['basis']=='title' else '')
    print(x['c'], len(x['title']), len(x['one'])-len(t))
