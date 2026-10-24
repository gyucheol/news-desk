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
        word, _, page = q.partition("@")          # F의 연애 (2026-10-24): "texting@2" reads the second result page
        subprocess.run(["curl", "-s", "-L", "-m", "30", "-A", "Mozilla/5.0", "-o", p,
                        f"https://mixkit.co/free-stock-video/discover/{word}/" + (f"?page={page}" if page else "")],
                       check=False)
        time.sleep(3)
    s = open(p, encoding="utf-8", errors="ignore").read()
    # cards are <div class="item-grid-card"> or, on newer pages, <div class="item-grid-card item-grid-card--show-meta">
    # (2026-10-23: splitting on the first form only dropped every card of those pages, e.g. exhausted, nap, sofa)
    cards = re.split(r'<div class="item-grid-card(?: [^"_]*)?"', s)[1:]
    for c in cards:
        m = re.search(r'data-algolia-analytics-object-id="video-(\d+)"', c)
        if not m:
            continue
        vid = m.group(1)
        title = (re.search(r'overlay-video-title">\s*(.*?)\s*</span>', c, flags=re.S)
                 or re.search(r'item-grid-card__title">\s*<a [^>]*>(.*?)</a>', c, flags=re.S)
                 or re.search(r'overlay-link">\s*(.*?)\s*</a>', c, flags=re.S))
        link = re.search(r'href="(/free-stock-video/[^"]+)"', c)
        thumb = re.search(r'<img src="([^"]+)"', c)
        video = re.search(r'<video src="([^"]+)"', c)          # newer cards carry a hashed preview address
        v = allv.setdefault(vid, {"id": vid, "queries": []})
        v.update({"title": html.unescape(title.group(1).strip()) if title else "",
                  "url": "https://mixkit.co" + link.group(1) if link else "",
                  "thumb": thumb.group(1) if thumb else "",
                  "preview": video.group(1) if video else f"https://assets.mixkit.co/videos/{vid}/{vid}-360.mp4",
                  # portrait clips: old cards carry a --vertical class, new ones only a tall thumbnail (460x818)
                  "vertical": "item-grid-video-player--vertical" in c[:600] or bool(
                      (d := re.search(r'<img [^>]*width="(\d+)" height="(\d+)"', c)) and int(d.group(2)) > int(d.group(1)))})
        if q not in v["queries"]:
            v["queries"].append(q)
json.dump(list(allv.values()), open(idx_path, "w"), ensure_ascii=False, indent=1)
for q in queries:
    hits = [v for v in allv.values() if q in v["queries"] and not v["vertical"]]
    print(f"== {q}: {len(hits)} horizontal")
    for v in hits:
        print(f'   {v["id"]:>6}  {v["title"][:80]}')
