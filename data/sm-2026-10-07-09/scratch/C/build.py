import json,collections
B='/home/user/news-desk/data/sm-2026-10-07-09/'
rows={int(l.split('\t')[0]):l.rstrip('\n').split('\t') for l in open(B+'keep.tsv')}
th={}
for l in open(B+'scratch/C/themes.tsv'):
    k,n,f,a=l.rstrip('\n').split('\t'); th[k]=(n,f,a)
cl=[]
for l in open(B+'scratch/C/groups.tsv'):
    k,v=l.rstrip('\n').split('\t'); n,f,a=th[k]
    cl.append(dict(theme=n,field=f,attachTo=a,lines=sorted(map(int,v.split()))))
for fn in ['singles1.tsv','singles2.tsv']:
    for l in open(B+'scratch/C/'+fn):
        p=l.rstrip('\n').split('\t'); ln=int(p[0])
        cl.append(dict(theme=p[1],field=rows[ln][1],attachTo=p[2] if len(p)>2 else '',lines=[ln]))
drop=[dict(line=int(l.split('\t')[0]),reason=l.rstrip('\n').split('\t')[1]) for l in open(B+'scratch/C/drops.tsv')]
cl.sort(key=lambda c:(-len(c['lines']),c['lines'][0]))
out=[]
for i,c in enumerate(cl,1): out.append(dict(cid='C%03d'%i,**c))
fields={r[1] for r in rows.values()}
assert all(c['field'] in fields for c in out),[c for c in out if c['field'] not in fields]
allL=[x for c in out for x in c['lines']]+[d['line'] for d in drop]
cnt=collections.Counter(allL)
print('missing',sorted(set(rows)-set(cnt)),'dup',[k for k,v in cnt.items() if v>1],'extra',sorted(set(cnt)-set(rows)))
json.dump(dict(clusters=out,drop=drop),open(B+'clusters.json','w'),ensure_ascii=False,indent=1)
print('clusters',len(out),'singles',sum(len(c['lines'])==1 for c in out),'attach',sum(bool(c['attachTo']) for c in out),'drop',len(drop),'max',max(len(c['lines']) for c in out))
