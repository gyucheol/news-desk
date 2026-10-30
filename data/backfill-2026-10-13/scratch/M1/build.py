import json,os,sys,re
B='/home/user/news-desk/data/backfill-2026-10-13/'
src=json.load(open(B+'in/M1.json'))
out=[]
for d in src:
    p=B+'scratch/M1/docs/'+d['id']+'.json'
    if not os.path.exists(p): continue
    x=json.load(open(p))
    o={'id':d['id'],'title':x['title'],'one':x['one']}
    if 'items' in d:
        o['added']=x['added']
        assert len(x['s'])==len(d['items']),(d['id'],len(x['s']),len(d['items']))
        o['items']=[{'u':i['u'],'s':s} for i,s in zip(d['items'],x['s'])]
    out.append(o)
json.dump({'docs':out},open(B+'out/M1.json','w'),ensure_ascii=False,indent=1)
print('wrote',len(out))
