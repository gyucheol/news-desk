# Mixkit search (few pages, polite 2 s delay): parse item cards -> id, title, link, thumb, 360p preview, vertical.
# License is NOT on the card; verify each chosen item on its own page (mixkit_license_check.py).
# usage: mixkit_search.py outdir query1 query2 ...   (query: words joined by '-')
import json, os, re, sys, time, subprocess, html
out, queries = sys.argv[1], sys.argv[2:]
os.makedirs(out, exist_ok=True)
idx_path = f"{out}/index.json"
allv = {v["id"]: v for v in json.load(open(idx_path))} if os.path.exists(idx_path) and os.path.getsize(idx_path) > 2 else {}
for q in queries:
    p = f"{out}/q_{q}.html"
    if not os.path.exists(p):
        subprocess.run(["curl", "-s", "-L", "-m", "30", "-A", "Mozilla/5.0", "-o", p,
                        f"https://mixkit.co/free-stock-video/discover/{q}/"], check=False)
        time.sleep(2)
    s = open(p, encoding="utf-8", errors="ignore").read()
    cards = s.split('<div class="item-grid-card"')[1:]
    for c in cards:
        m = re.search(r'data-algolia-analytics-object-id="video-(\d+)"', c)
        if not m:
            continue
        vid = m.group(1)
        title = re.search(r'overlay-video-title">\s*(.*?)\s*</span>', c, flags=re.S)
        link = re.search(r'href="(/free-stock-video/[^"]+)"', c)
        thumb = re.search(r'<img src="([^"]+)"', c)
        v = allv.setdefault(vid, {"id": vid, "queries": []})
        v.update({"title": html.unescape(title.group(1).strip()) if title else "",
                  "url": "https://mixkit.co" + link.group(1) if link else "",
                  "thumb": thumb.group(1) if thumb else "",
                  "preview": f"https://assets.mixkit.co/videos/{vid}/{vid}-360.mp4",
                  "vertical": "item-grid-video-player--vertical" in c[:600]})
        if q not in v["queries"]:
            v["queries"].append(q)
json.dump(list(allv.values()), open(idx_path, "w"), ensure_ascii=False, indent=1)
for q in queries:
    hits = [v for v in allv.values() if q in v["queries"] and not v["vertical"]]
    print(f"== {q}: {len(hits)} horizontal")
    for v in hits:
        print(f'   {v["id"]:>6}  {v["title"][:80]}')
