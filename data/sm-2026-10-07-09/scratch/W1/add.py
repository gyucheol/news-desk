import json,sys,os,re
out='/home/user/news-desk/data/sm-2026-10-07-09/out2/W1.json'
d=json.load(open(out)) if os.path.exists(out) else {"agent":"W1","searches_used":0,"fetches_used":0,"items":[],"skipped":[]}
new=json.load(open(sys.argv[1]))
d['searches_used']=new.get('searches_used',d['searches_used']); d['fetches_used']=new.get('fetches_used',d['fetches_used'])
ids={x['cid'] for x in d['items']}|{x['cid'] for x in d['skipped']}
for x in new.get('items',[]):
    if x['cid'] not in ids: d['items'].append(x)
for x in new.get('skipped',[]):
    if x['cid'] not in ids: d['skipped'].append(x)
json.dump(d,open(out,'w'),ensure_ascii=False,indent=1)
print(len(d['items']),len(d['skipped']),[(x['cid'],len(x['title']),len(re.sub(r' \(제목 기준\)$','',x['one']))) for x in new.get('items',[])])
