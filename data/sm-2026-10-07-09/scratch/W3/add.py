import json,sys
out='/home/user/news-desk/data/sm-2026-10-07-09/out2/W3.json'
d=json.load(open(out)); a=json.load(open(sys.argv[1]))
ids={x['cid'] for x in d['items']}|{x['cid'] for x in d['skipped']}
for x in a.get('items',[]):
    if x['cid'] not in ids: d['items'].append(x)
for x in a.get('skipped',[]):
    if x['cid'] not in ids: d['skipped'].append(x)
d['searches_used']=int(sys.argv[2]); d['fetches_used']=int(sys.argv[3])
json.dump(d,open(out,'w'),ensure_ascii=False,indent=1)
print(len(d['items']),len(d['skipped']))
