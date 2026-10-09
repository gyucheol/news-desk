import json, glob, sys, re
d = "/home/user/news-desk/data/sm-2026-10-07-09/scratch/W10/"
s, f = int(sys.argv[1]), int(sys.argv[2])
out = {"agent": "W10", "searches_used": s, "fetches_used": f, "items": [], "skipped": []}
for p in sorted(glob.glob(d + "p*.json")):
    j = json.load(open(p))
    out["items"] += j.get("items", [])
    out["skipped"] += j.get("skipped", [])
o = "/home/user/news-desk/data/sm-2026-10-07-09/out2/W10.json"
json.dump(out, open(o, "w"), ensure_ascii=False, indent=1)
print(len(out["items"]), len(out["skipped"]), [(x["cid"], len(re.sub(r" \(제목 기준\)$", "", x["one"])), len(x["title"])) for x in out["items"]])
