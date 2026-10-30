import json,glob,os
H='/home/user/news-desk/data/rebundle-2026-10-20'
W=json.load(open(f'{H}/win/W01.json'))
parts={}
for p in sorted(glob.glob(f'{H}/scratch/W01/parts/*.json')):
    for x in json.load(open(p)): parts[x['c']]=x
out=[parts[c['c']] for c in W['clusters'] if c['c'] in parts]
json.dump(out,open(f'{H}/wout/W01.json','w'),ensure_ascii=False,indent=1)
cl={c['c']:c for c in W['clusters']}
for x in out:
    tail={'title':' (제목 기준)','channel':' (채널 전언)'}.get(x['basis'],'')
    core=x['one'][:-len(tail)] if tail and x['one'].endswith(tail) else x['one']
    print(x['c'],'title',len(x['title']),'one',len(core),'items',len(cl[x['c']]['items']))
    for u,s in x.get('s_add',{}).items():
        if not (45<=len(s)<=110 and s.endswith('다')): print('  s_add bad',len(s),s[:30])
        if u not in {it['u'] for it in cl[x['c']]['items']}: print('  s_add url missing')
    for v in x['vc']:
        if not 12<=len(v['t'])<=45: print('  vc t',len(v['t']),v['t'])
    empt=[it['u'] for it in cl[x['c']]['items'] if not it['s']]
    if len(cl[x['c']]['items'])>1 and set(empt)-set(x.get('s_add',{})): print('  s_add missing for',set(empt)-set(x.get('s_add',{})))
print(len(out),'written')
