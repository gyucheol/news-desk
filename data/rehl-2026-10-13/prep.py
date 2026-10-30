import json,sys,re
D=sys.argv[1];T=json.load(open('hl/targets.json'))
strip=lambda s:s.replace('{{','').replace('}}','')
units=[]  # (doc, path(list), kind, text)
SKIPK={'k','tone','id','tag','label','kicker','here','updated','tk','px'}
def walk(doc,obj,path,kind):
    if isinstance(obj,str):
        if len(strip(obj))>=6: units.append((doc,path,kind,strip(obj)))
    elif isinstance(obj,list):
        for i,x in enumerate(obj): walk(doc,x,path+[i],kind)
    elif isinstance(obj,dict):
        if obj.get('k') in ('h3','h4','src','legend'): return
        for k,v in obj.items():
            if k in SKIPK: continue
            if k=='kv':  # [[key,val]]: 값만
                for i,p in enumerate(v): walk(doc,p[1],path+[k,i,1],kind)
                continue
            walk(doc,v,path+[k],kind)
for i in T:
    d=json.load(open(f'{D}/{i}.json'))
    units.append((i,['title'],'제목',strip(d['title'])))
    units.append((i,['one'],'한줄 요약',strip(d['one'])))
    if d.get('added'): units.append((i,['added'],'더해진 내용',strip(d['added'])))
    for j,it in enumerate(d.get('items',[])):
        if it.get('s'): units.append((i,['items',j,'s'],'원문 요약',strip(it['s'])))
    if d.get('detail'): walk(i,d['detail']['blocks'],['detail','blocks'],'자세한 정리')
    if d.get('insight2'): walk(i,d['insight2']['parts'],['insight2','parts'],'투자 인사이트')
assert all('\n' not in u[3] for u in units)
# 묶음: 문서를 쪼개지 않고 약 2만 자씩
B=[];cur=[];n=0
for u in units:
    if cur and cur[-1][0]!=u[0] and n>19000: B.append(cur);cur=[];n=0
    cur.append(u);n+=len(u[3])
B.append(cur)
M=[]
for bi,b in enumerate(B,1):
    L=[];prev=None
    for u in b:
        k=len(M);M.append({'doc':u[0],'path':u[1],'text':u[3],'batch':bi})
        if u[0]!=prev: L.append(f'## {u[0]}');prev=u[0]
        L.append(f'@@ {k} {u[2]}');L.append(u[3])
    open(f'hl/in/b{bi:02d}.txt','w').write('\n'.join(L)+'\n')
json.dump(M,open('hl/map.json','w'),ensure_ascii=False)
print(len(units),'units',len(B),'batches',[len(b) for b in B])
