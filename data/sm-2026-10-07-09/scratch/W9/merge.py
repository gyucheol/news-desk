import json, glob, re, sys
base = '/home/user/news-desk/data/sm-2026-10-07-09/'
s, f = int(sys.argv[1]), int(sys.argv[2])
out = {"agent": "W9", "searches_used": s, "fetches_used": f, "items": [], "skipped": []}
for p in sorted(glob.glob(base + 'scratch/W9/p*.json')):
    d = json.load(open(p))
    out["items"] += d["items"]; out["skipped"] += d["skipped"]
json.dump(out, open(base + 'out2/W9.json', 'w'), ensure_ascii=False, indent=1)
print(len(out['items']), len(out['skipped']))
for x in out['items']:
    n = len(re.sub(r' \(제목 기준\)$', '', x['one']))
    print(x['cid'], len(x['title']), n, len(x['items']))
