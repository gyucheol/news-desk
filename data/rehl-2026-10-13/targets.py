import json,glob,sys
from datetime import datetime
D=sys.argv[1];R=json.load(open(sys.argv[2]))['ids']
T=[];nd=0;units=0;chars=0;det=[]
for f in sorted(glob.glob(D+'/*.json')):
    d=json.load(open(f))
    if not (isinstance(d.get('one'),str) and d['one'].strip()): continue
    u=d.get('updatedAt');t=datetime.fromisoformat(u).timestamp()*1000 if u else 0
    if d['id'] in R and R[d['id']]>=t: continue
    T.append(d['id'])
    xs=[d['title'],d['one']]+([d['added']] if d.get('added') else [])+[it['s'] for it in d.get('items',[]) if it.get('s')]
    units+=len(xs);chars+=sum(len(x) for x in xs)
    if d.get('detail') or d.get('insight2'): det.append(d['id'])
print('targets',len(T),'units',units,'chars',chars,'with detail/insight2',det)
json.dump(T,open('hl/targets.json','w'))
