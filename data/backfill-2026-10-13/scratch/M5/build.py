import json, glob, sys, os
B='/home/user/news-desk/data/backfill-2026-10-13'
src=json.load(open(B+'/in/M5.json',encoding='utf-8')); S={d['id']:d for d in src}
def wrap(t, ph):
    spans=[]
    for p in ph:
        i=t.find(p)
        assert i>=0, (t[:30], p)
        for a,b in spans: assert i+len(p)<=a or i>=b, ('overlap',p)
        spans.append((i,i+len(p)))
    for a,b in sorted(spans, reverse=True): t=t[:a]+'{{'+t[a:b]+'}}'+t[b:]
    return t
D=[]
for f in sorted(glob.glob(os.path.dirname(__file__)+'/part*.py')):
    g={}; exec(open(f,encoding='utf-8').read(), g); D+=g['D']
out=[]
for d in D:
    s=S[d['id']]
    o={'id':d['id'],'title':wrap(s['title'],d['t']),'one':wrap(s['one'],d['o'])}
    if 'items' in s:
        o['added']=d['a']
        assert len(d['s'])==len(s['items']), (d['id'],len(d['s']),len(s['items']))
        o['items']=[{'u':x['u'],'s':y} for x,y in zip(s['items'],d['s'])]
    out.append(o)
json.dump({'docs':out},open(B+'/out/M5.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('saved',len(out))
