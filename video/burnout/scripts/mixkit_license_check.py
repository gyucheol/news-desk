# Verify each Mixkit item's license on its own page (JSON-LD copyrightNotice + license URL).
# usage: mixkit_license_check.py index.json outdir id1,id2,...
import json, os, re, subprocess, sys, time
idx = {v["id"]: v for v in json.load(open(sys.argv[1]))}
out, ids = sys.argv[2], sys.argv[3].split(",")
os.makedirs(out, exist_ok=True)
res = []
for vid in ids:
    url = idx[vid]["url"]; p = f"{out}/item_{vid}.html"
    if not os.path.exists(p):
        subprocess.run(["curl", "-s", "-L", "-m", "30", "-A", "Mozilla/5.0", "-o", p, url], check=False); time.sleep(1.5)
    s = open(p, encoding="utf-8", errors="ignore").read()
    notice, lic, content = None, None, None
    for blk in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', s, flags=re.S):
        try:
            d = json.loads(blk)
        except Exception:
            continue
        for n in (d.get("@graph", [d]) if isinstance(d, dict) else d):
            if isinstance(n, dict) and n.get("@type") == "VideoObject" and vid in n.get("@id", "") + n.get("contentUrl", ""):
                notice, lic, content = n.get("copyrightNotice"), n.get("license"), n.get("contentUrl")
    badge = "Restricted" if re.search(r"Restricted License", s) and not re.search(r"Free License", s) else None
    res.append({"id": vid, "title": idx[vid]["title"], "url": url, "copyrightNotice": notice, "license": lic,
                "contentUrl": content, "page_mentions_restricted": bool(re.search(r"videoRestricted|Restricted License", s))})
    print(f'{vid:>6} notice={notice} license={lic} content={content} restricted_mention={res[-1]["page_mentions_restricted"]}  {idx[vid]["title"][:50]}')
json.dump(res, open(f"{out}/license_check.json", "w"), ensure_ascii=False, indent=1)
