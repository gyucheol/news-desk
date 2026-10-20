import json,sys
rows=[l.rstrip('\n').split('\t') for l in open('in/G6.tsv',encoding='utf-8',errors='replace')][1:]
date={r[0]:r[2] for r in rows}
out=[]
for i,l in enumerate(open('scratch/G6/groups.txt',encoding='utf-8')):
    l=l.strip()
    if not l: continue
    lab,ks=l.split('|'); ks=ks.split()
    ks.sort(key=lambda k:(date[k],k))
    out.append({"c":"G6-%03d"%(len(out)+1),"label":lab,"m":ks})
json.dump(out,open('clusters/G6.json','w',encoding='utf-8'),ensure_ascii=False,indent=1)
for x in out:
    n=len(x['label'])
    if n<15 or n>40: print('len',n,x['label'])
