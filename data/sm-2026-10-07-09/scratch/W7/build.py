import json,glob,sys
base='/home/user/news-desk/data/sm-2026-10-07-09/'
items=[];skipped=[]
for f in sorted(glob.glob(base+'scratch/W7/b*.json')):
    items+=json.load(open(f))
for f in sorted(glob.glob(base+'scratch/W7/s*.json')):
    skipped+=json.load(open(f))
s,w=int(sys.argv[1]),int(sys.argv[2])
json.dump({"agent":"W7","searches_used":s,"fetches_used":w,"items":items,"skipped":skipped},open(base+'out2/W7.json','w'),ensure_ascii=False,indent=1)
import re
print(len(items),[ (x['cid'],len(re.sub(r' \(제목 기준\)$','',x['one']))) for x in items])
