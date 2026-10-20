import json,glob,os,re
H='/home/user/news-desk/data/rebundle-2026-10-20'
W=json.load(open(H+'/win/W03.json'))
E={}
for f in sorted(glob.glob(H+'/scratch/W03/e*.py')):
    ns={}; exec(open(f).read(),ns); 
    for x in ns['E']: E[x['c']]=x
out=[E[c['c']] for c in W['clusters'] if c['c'] in E]
json.dump(out,open(H+'/wout/W03.json','w'),ensure_ascii=False,indent=1)
for x in out:
    t=x['one']
    for tl in (' (제목 기준)',' (채널 전언)'):
        if t.endswith(tl): t=t[:-len(tl)]
    print(x['c'],'title',len(x['title']),'one',len(t))
