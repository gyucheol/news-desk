import json,glob,re
H='/home/user/news-desk/data/rebundle-2026-10-20'
W=json.load(open(H+'/win/W02.json'))
out=[]
for i,c in enumerate(W['clusters']):
    try: x=json.load(open(f'{H}/scratch/W02/c/{i:02d}.json'))
    except FileNotFoundError: break
    assert x['c']==c['c'],(i,x['c'],c['c'])
    out.append(x)
json.dump(out,open(H+'/wout/W02.json','w'),ensure_ascii=False,indent=1)
for x in out:
    t=re.sub(r' \((제목 기준|채널 전언)\)$','',x['one']); print(x['c'],len(x['title']),len(t))
