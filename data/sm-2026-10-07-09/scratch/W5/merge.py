import json, re, sys, os
out = '/home/user/news-desk/data/sm-2026-10-07-09/out2/W5.json'
d = json.load(open(out)) if os.path.exists(out) else {"agent": "W5", "searches_used": 0, "fetches_used": 0, "items": [], "skipped": []}
p = json.load(open(sys.argv[1]))
have = {x['cid'] for x in d['items']} | {x['cid'] for x in d['skipped']}
d['items'] += [x for x in p.get('items', []) if x['cid'] not in have]
d['skipped'] += [x for x in p.get('skipped', []) if x['cid'] not in have]
d['searches_used'] = int(sys.argv[2]); d['fetches_used'] = int(sys.argv[3])
json.dump(d, open(out, 'w'), ensure_ascii=False, indent=1)
print(len(d['items']), [(x['cid'], len(re.sub(r' \(제목 기준\)$', '', x['one'])), len(x['title'])) for x in d['items']])
