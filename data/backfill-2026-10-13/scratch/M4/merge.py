import json,glob,os
src=json.load(open('in/M4.json'))
parts={}
for f in sorted(glob.glob('scratch/M4/p_*.json')):
    for d in json.load(open(f)): parts[d['id']]=d
docs=[]
for s in src:
    if s['id'] not in parts: continue
    d=parts[s['id']]
    o={'id':s['id'],'title':d['title'],'one':d['one'],'added':d['added'],
       'items':[{'u':x['u'],'s':d['s'][k] if k<len(d['s']) else ''} for k,x in enumerate(s['items'])]}
    docs.append(o)
os.makedirs('out',exist_ok=True)
json.dump({'docs':docs},open('out/M4.json','w'),ensure_ascii=False,indent=1)
print('saved',len(docs))
