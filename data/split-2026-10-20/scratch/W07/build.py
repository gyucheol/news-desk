import json,glob,os,sys
H='/home/user/news-desk/data/split-2026-10-20'
W=json.load(open(H+'/win/W07.json'))
got={}
for f in sorted(glob.glob(H+'/scratch/W07/parts/*.json')):
    for x in json.load(open(f)): got[x['c']]=x
out=[got[c['c']] for c in W['clusters'] if c['c'] in got]
json.dump(out,open(H+'/wout/W07.json','w'),ensure_ascii=False,indent=1)
print(len(out))
TAILS={'title':' (제목 기준)','channel':' (채널 전언)'}
for x in out:
    n=len([c for c in W['clusters'] if c['c']==x['c']][0]['items'])
    one=x['one']; t=TAILS.get(x['basis'],'')
    core=one[:-len(t)] if t and one.endswith(t) else one
    print(x['c'],'n',n,'title',len(x['title']),'one',len(core),[len(v['t']) for v in x['vc']])
