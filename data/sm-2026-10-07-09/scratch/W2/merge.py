import json,glob,re,sys
d={"agent":"W2","searches_used":0,"fetches_used":0,"items":[],"skipped":[]}
for f in sorted(glob.glob(sys.argv[1]+'/b*.json')):
    b=json.load(open(f)); d['searches_used']+=b['searches']; d['fetches_used']+=b['fetches']
    d['items']+=b['items']; d['skipped']+=b['skipped']
json.dump(d,open(sys.argv[2],'w'),ensure_ascii=False,indent=1)
for x in d['items']:
    print(x['cid'],len(x['title']),len(re.sub(r' \(제목 기준\)$','',x['one'])),len(x['items']),[len(i['t']) for i in x['items'] if not 25<=len(i['t'])<=60])
print(d['searches_used'],d['fetches_used'],len(d['skipped']))
