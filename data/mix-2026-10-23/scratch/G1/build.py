import json,sys,importlib.util,os
d='/home/user/news-desk/data/mix-2026-10-23/scratch/G1'
sys.path.insert(0,d)
allc=[];drop=[]
import part1; allc+=part1.C1
if os.path.exists(d+'/part2.py'):
    import part2; allc+=part2.C2; drop+=part2.DROP
allc.sort(key=lambda c:-len(c[4]))
out={"clusters":[{"cid":f"G1-{i+1:03d}","theme":t,"field":f,"attachTo":a,"core":c,"lines":l} for i,(t,f,a,c,l) in enumerate(allc)],
     "drop":[{"line":x,"reason":r} for x,r in drop]}
json.dump(out,open('/home/user/news-desk/data/mix-2026-10-23/clusters_G1.json','w'),ensure_ascii=False,indent=1)
print(len(out['clusters']),'clusters',len(drop),'drops')
