# Mixkit helper shared by several agents at once (03편 v1, 2026-10-29).
# Every request to mixkit.co waits for a shared lock so that requests from all agents together are at least 3.2 s
# apart (shorter gaps brought Cloudflare 429 pages before). Files are cached; nothing is fetched twice.
#
# usage (run with the scratchpad venv python, -I):
#   mk.py search WORD[@PAGE] ...      one word per query (multi-word queries return 0 results); prints horizontal hits
#   mk.py lic ID [ID ...]             license from the item page (JSON-LD copyrightNotice). Use only "Free" items.
#   mk.py prev ID [ID ...]            360p preview -> stock/prev/ID.mp4, prints duration
#   mk.py strip ID [N]                N frames (default 8) of the preview with times -> stock/prev/ID_strip.jpg (view it)
#   mk.py frame ID SEC                one full-size frame of the 1080p file (after get) -> stock/prev/ID_SEC.jpg
#   mk.py get ID [ID ...]             1080p original -> stock/full/ID.mp4 (reuses scratchpad/stock/full/ID.mp4 if there)
import fcntl, html, json, os, re, subprocess, sys, time

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))   # .../ep3/v3/stock
SEARCH, ITEMS, PREV, FULL = (os.path.join(ROOT, d) for d in ("search", "items", "prev", "full"))
OLD_FULL = os.path.abspath(os.path.join(ROOT, "..", "..", "..", "stock", "full"))   # burnout originals
LOCK = os.path.join(ROOT, "tools", ".lock")
STAMP = os.path.join(ROOT, "tools", ".last")
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0 Safari/537.36"
GAP_PAGE, GAP_ASSET = 3.2, 1.0
for d in (SEARCH, ITEMS, PREV, FULL):
    os.makedirs(d, exist_ok=True)


def fetch(url, out, gap):
    """curl url -> out, holding the shared lock while waiting for the gap. Retries 429/403/empty with backoff."""
    for attempt in range(5):
        with open(LOCK, "a+") as lk:
            fcntl.flock(lk, fcntl.LOCK_EX)
            try:
                last = float(open(STAMP).read().strip() or 0)
            except Exception:
                last = 0.0
            wait = last + gap - time.time()
            if wait > 0:
                time.sleep(wait)
            open(STAMP, "w").write(str(time.time()))
            fcntl.flock(lk, fcntl.LOCK_UN)
        tmp = out + ".part"
        r = subprocess.run(["curl", "-s", "-L", "-m", "300", "-A", UA, "-w", "%{http_code}", "-o", tmp, url],
                           capture_output=True, text=True)
        code = r.stdout.strip()
        ok = code == "200" and os.path.exists(tmp) and os.path.getsize(tmp) > 1000
        if ok and out.endswith(".html"):
            s = open(tmp, encoding="utf-8", errors="ignore").read(4000)
            if "Just a moment" in s or "cf-chl" in s:
                ok = False
        if ok:
            os.replace(tmp, out)
            return True
        if os.path.exists(tmp):
            os.remove(tmp)
        if code == "404":
            return False
        time.sleep(10 * (attempt + 1))
    return False


def load_index():
    p = os.path.join(SEARCH, "index.json")
    return {v["id"]: v for v in json.load(open(p))} if os.path.exists(p) and os.path.getsize(p) > 2 else {}


def save_index(allv):
    p = os.path.join(SEARCH, "index.json")
    with open(LOCK + "i", "a+") as lk:
        fcntl.flock(lk, fcntl.LOCK_EX)
        cur = load_index()
        for k, v in allv.items():
            if k in cur:
                q = sorted(set(cur[k].get("queries", [])) | set(v.get("queries", [])))
                cur[k].update(v); cur[k]["queries"] = q
            else:
                cur[k] = v
        json.dump(list(cur.values()), open(p + ".tmp", "w"), ensure_ascii=False, indent=1)
        os.replace(p + ".tmp", p)
        fcntl.flock(lk, fcntl.LOCK_UN)


def parse_cards(s, q, allv):
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
        video = re.search(r'<video src="([^"]+)"', c)
        d = re.search(r'<img [^>]*width="(\d+)" height="(\d+)"', c)
        v = allv.setdefault(vid, {"id": vid, "queries": []})
        v.update({"title": html.unescape(title.group(1).strip()) if title else "",
                  "url": "https://mixkit.co" + link.group(1) if link else "",
                  "preview": video.group(1) if video else f"https://assets.mixkit.co/videos/{vid}/{vid}-360.mp4",
                  "vertical": "item-grid-video-player--vertical" in c[:600] or bool(d and int(d.group(2)) > int(d.group(1)))})
        if q not in v["queries"]:
            v["queries"].append(q)


def cmd_search(qs):
    allv = load_index()
    for q in qs:
        word, _, page = q.partition("@")
        p = os.path.join(SEARCH, f"q_{q}.html")
        if not os.path.exists(p):
            fetch(f"https://mixkit.co/free-stock-video/discover/{word}/" + (f"?page={page}" if page else ""), p, GAP_PAGE)
        if not os.path.exists(p):
            print(f"== {q}: fetch failed"); continue
        parse_cards(open(p, encoding="utf-8", errors="ignore").read(), q, allv)
    save_index(allv)
    for q in qs:
        hits = [v for v in allv.values() if q in v["queries"] and not v["vertical"]]
        print(f"== {q}: {len(hits)} horizontal")
        for v in hits:
            print(f'   {v["id"]:>6}  {v["title"][:90]}')


def item_page(vid):
    p = os.path.join(ITEMS, f"item_{vid}.html")
    if not os.path.exists(p):
        url = load_index().get(vid, {}).get("url") or f"https://mixkit.co/free-stock-video/x-{vid}/"
        fetch(url, p, GAP_PAGE)
    return open(p, encoding="utf-8", errors="ignore").read() if os.path.exists(p) else ""


def lic(vid):
    s = item_page(vid)
    res = {"id": vid, "copyrightNotice": None, "license": None, "contentUrl": None, "name": None, "duration": None,
           "width": None, "height": None, "url": load_index().get(vid, {}).get("url")}
    for blk in re.findall(r'<script[^>]*ld\+json[^>]*>(.*?)</script>', s, flags=re.S):
        try:
            d = json.loads(blk)
        except Exception:
            continue
        for n in (d.get("@graph", [d]) if isinstance(d, dict) else d):
            if isinstance(n, dict) and n.get("@type") == "VideoObject" and vid in (n.get("@id", "") + n.get("contentUrl", "") + n.get("url", "") + json.dumps(n)[:3000]):
                res.update({"copyrightNotice": n.get("copyrightNotice"), "license": n.get("license"),
                            "contentUrl": n.get("contentUrl"), "name": n.get("name"), "duration": n.get("duration"),
                            "width": n.get("width"), "height": n.get("height"), "url": n.get("url") or res["url"]})
    res["page_mentions_restricted"] = bool(re.search(r"videoRestricted|Restricted License", s))
    res["free"] = (res["copyrightNotice"] or "").strip().lower().startswith("free") and "restricted" not in (res["copyrightNotice"] or "").lower()
    res["checked"] = time.strftime("%Y-%m-%d")
    json.dump(res, open(os.path.join(ITEMS, f"lic_{vid}.json"), "w"), ensure_ascii=False, indent=1)
    return res


def cmd_lic(ids):
    for vid in ids:
        r = lic(vid)
        print(f'{vid:>6} FREE={r["free"]} notice={r["copyrightNotice"]!r} dur={r["duration"]} {r["width"]}x{r["height"]} '
              f'restricted_mention={r["page_mentions_restricted"]} | {r["name"]}')


def probe(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                        "stream=width,height:format=duration", "-of", "json", p], capture_output=True, text=True)
    try:
        j = json.loads(r.stdout)
        return float(j["format"]["duration"]), j["streams"][0]["width"], j["streams"][0]["height"]
    except Exception:
        return None, None, None


def cmd_prev(ids):
    for vid in ids:
        p = os.path.join(PREV, f"{vid}.mp4")
        if not os.path.exists(p):
            url = load_index().get(vid, {}).get("preview") or f"https://assets.mixkit.co/videos/{vid}/{vid}-360.mp4"
            if not fetch(url, p, GAP_ASSET):
                fetch(f"https://assets.mixkit.co/videos/{vid}/{vid}-360.mp4", p, GAP_ASSET)
        print(vid, probe(p) if os.path.exists(p) else "no preview")


def cmd_strip(vid, n=8):
    from PIL import Image, ImageDraw
    p = os.path.join(PREV, f"{vid}.mp4")
    if not os.path.exists(p):
        cmd_prev([vid])
    dur, w, h = probe(p)
    if not dur:
        print("no preview"); return
    ims = []
    for k in range(n):
        t = dur * (k + 0.5) / n
        r = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", p, "-frames:v", "1", "-vf", "scale=320:-2",
                            "-f", "image2pipe", "-vcodec", "png", "-"], capture_output=True)
        from io import BytesIO
        try:
            im = Image.open(BytesIO(r.stdout)).convert("RGB")
        except Exception:
            continue
        ImageDraw.Draw(im).text((4, 4), f"{t:.1f}s", fill=(255, 255, 0))
        ims.append(im)
    if not ims:
        print("no frames"); return
    cols = 4
    W, H = ims[0].size
    sheet = Image.new("RGB", (cols * W, ((len(ims) + cols - 1) // cols) * H))
    for k, im in enumerate(ims):
        sheet.paste(im, ((k % cols) * W, (k // cols) * H))
    out = os.path.join(PREV, f"{vid}_strip.jpg")
    sheet.save(out, quality=80)
    print(out, f"duration {dur:.1f}s")


def cmd_get(ids):
    for vid in ids:
        out = os.path.join(FULL, f"{vid}.mp4")
        old = os.path.join(OLD_FULL, f"{vid}.mp4")
        if not os.path.exists(out) and os.path.exists(old):
            os.symlink(old, out)
        if not os.path.exists(out):
            r = lic(vid)
            cands = [f"https://assets.mixkit.co/videos/{vid}/{vid}-1080.mp4"]
            cu = r.get("contentUrl") or ""
            if cu and "1080" in cu:
                cands.insert(0, cu)
            elif cu:
                cands.append(cu)
            cands.append(f"https://assets.mixkit.co/videos/{vid}/{vid}-720.mp4")
            for u in cands:
                if fetch(u, out, GAP_ASSET):
                    break
        print(vid, probe(out) if os.path.exists(out) else "download failed")


def cmd_frame(vid, sec):
    p = os.path.join(FULL, f"{vid}.mp4")
    out = os.path.join(PREV, f"{vid}_{sec}.jpg")
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(sec), "-i", p, "-frames:v", "1", out])
    print(out)


if __name__ == "__main__":
    c, a = sys.argv[1], sys.argv[2:]
    {"search": lambda: cmd_search(a), "lic": lambda: cmd_lic(a), "prev": lambda: cmd_prev(a),
     "strip": lambda: cmd_strip(a[0], int(a[1]) if len(a) > 1 else 8), "get": lambda: cmd_get(a),
     "frame": lambda: cmd_frame(a[0], a[1])}[c]()
