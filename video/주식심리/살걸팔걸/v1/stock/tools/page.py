# group B helper: fetch real page N of a Mixkit listing (mk.py's WORD@PAGE goes to /discover/WORD/?page=N,
# which 301-redirects to /free-stock-video/WORD/ and drops the page). Uses mk.fetch, so the shared lock/gap apply.
# usage: page.py WORD~N ...
import os, re, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "tools"))
import mk
allv = mk.load_index()
qs = sys.argv[1:]
for q in qs:
    word, _, page = q.partition("~")
    p = os.path.join(mk.SEARCH, f"q_{word}~{page}.html")
    if not os.path.exists(p):
        base = f"https://mixkit.co/free-stock-video/{word}/"
        p1 = os.path.join(mk.SEARCH, f"q_{word}.html")
        if os.path.exists(p1):
            m = re.search(r'aria-label="Go to page 2" href="([^"?]+)\?page=2"', open(p1, encoding="utf-8", errors="ignore").read())
            if m:
                base = "https://mixkit.co" + m.group(1)
        mk.fetch(f"{base}?page={page}", p, mk.GAP_PAGE)
    if not os.path.exists(p):
        print(f"== {q}: fetch failed"); continue
    s = open(p, encoding="utf-8", errors="ignore").read()
    cur = re.search(r'pagination__link--current" aria-label="Go to page (\d+)"', s)
    if not cur or cur.group(1) != page:
        print(f"== {q}: page check failed (current={cur.group(1) if cur else None})"); continue
    mk.parse_cards(s, q, allv)
mk.save_index(allv)
for q in qs:
    hits = [v for v in allv.values() if q in v["queries"] and not v["vertical"]]
    print(f"== {q}: {len(hits)} horizontal")
    for v in hits:
        print(f'   {v["id"]:>6}  {v["title"][:90]}')
