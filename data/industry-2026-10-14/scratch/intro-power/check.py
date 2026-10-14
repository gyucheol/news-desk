import json, re, sys
ROOT = "/home/user/news-desk"
JOSA = set('은는이가을를에의와과도로만')
def strip(s): return s.replace('{{', '').replace('}}', '')
def sentences(s):
    p = strip(s)
    return [x for x in re.split(r'(?<=[.!?])\s+', p.strip()) if x]
def check(ind):
    out = json.load(open(f"{ROOT}/data/industry-2026-10-14/intro/{ind}.json", encoding="utf-8"))
    page = json.load(open(f"{ROOT}/work/live14/chains/{ind}.json", encoding="utf-8"))
    P, W = [], []
    assert out["id"] == ind, "id mismatch"
    it = out["intro"]
    need = ["what", "money", "drivers", "watch", "players", "reading", "terms"]
    for k in need:
        if k not in it: P.append(f"missing field {k}")
    extra = set(it) - set(need)
    if extra: P.append(f"extra fields {extra}")
    if set(out) != {"id", "intro", "missing"}: P.append(f"top-level keys {set(out)}")
    rng = {"what": (2, 3), "money": (2, 3), "drivers": (3, 4)}
    for k, (a, b) in rng.items():
        n = len(sentences(it[k]))
        if not a <= n <= b: P.append(f"{k}: {n} sentences (want {a}-{b})")
    cnt = {"watch": (3, 5), "players": (5, 8), "reading": (3, 5), "terms": (3, 6)}
    for k, (a, b) in cnt.items():
        n = len(it[k])
        if not a <= n <= b: P.append(f"{k}: {n} items (want {a}-{b})")
    keys = {"watch": {"n", "why", "where"}, "players": {"n", "t", "m", "role"}, "reading": {"news", "means"}, "terms": {"k", "v"}}
    for k, ks in keys.items():
        for i, x in enumerate(it[k]):
            if set(x) != ks: P.append(f"{k}[{i}] keys {set(x)}")
            for kk, vv in x.items():
                if not isinstance(vv, str) or (not vv.strip() and not (k == "players" and kk == "t")): P.append(f"{k}[{i}].{kk} empty/non-str")
    for i, x in enumerate(out["missing"]):
        if set(x) != {"news", "suggest"}: P.append(f"missing[{i}] keys {set(x)}")
    # no emphasis where forbidden
    for k in ["watch", "players", "terms"]:
        if "{{" in json.dumps(it[k], ensure_ascii=False) or "}}" in json.dumps(it[k], ensure_ascii=False): P.append(f"{k}: has emphasis")
    for i, x in enumerate(it["reading"]):
        if "{{" in x["news"]: P.append(f"reading[{i}].news has emphasis")
    if "{{" in json.dumps(out["missing"], ensure_ascii=False): P.append("missing has emphasis")
    # emphasis units
    units = [("what", it["what"]), ("money", it["money"]), ("drivers", it["drivers"])] + [(f"means{i}", x["means"]) for i, x in enumerate(it["reading"])]
    tot = hl = 0
    rows = []
    for name, s in units:
        if s.count('{{') != s.count('}}') or re.search(r'\{\{[^}]*\{\{', s) or re.search(r'\}\}[^{]*\}\}', s) or '{{}}' in s or re.search(r'(?<!\{)\{(?!\{)|(?<!\})\}(?!\})', s):
            P.append(f"{name}: bracket pairing")
        marks = re.findall(r'\{\{(.+?)\}\}', s)
        plain = strip(s); n = len(plain); h = sum(len(m) for m in marks)
        tot += n; hl += h
        r = h / max(1, n)
        rows.append((name, n, r))
        if not (0.50 <= r <= 0.65): W.append(f"{name}: ratio {r:.0%}")
        for m in marks:
            if m != m.strip(): P.append(f"{name}: space edge '{m}'")
            if len(m) > 30: W.append(f"{name}: long chunk {len(m)} '{m}'")
            if re.match(r'^[,.)·]|[,(·]$', m): W.append(f"{name}: punct edge '{m}'")
            if m.count('(') != m.count(')'): W.append(f"{name}: paren '{m}'")
            if len(m) == 1 and m in JOSA: W.append(f"{name}: josa only '{m}'")
        if re.search(r'\}\}\{\{', s): W.append(f"{name}: adjacent marks")
    # node names in means
    names = [nd["name"] for nd in page["nodes"]]
    for i, x in enumerate(it["reading"]):
        used = [nm for nm in names if nm in strip(x["means"])]
        if not used: P.append(f"reading[{i}].means: no exact node name")
    # players vs page companies
    comp = {}
    for nd in page["nodes"]:
        for c in nd.get("companies", []):
            comp.setdefault(c["n"], set()).add((c.get("t", ""), c.get("m", "")))
    for i, p in enumerate(it["players"]):
        if p["n"] not in comp: P.append(f"players[{i}] name not on page: {p['n']}")
        elif (p["t"], p["m"]) not in comp[p["n"]]: P.append(f"players[{i}] ticker/market mismatch {p['n']} {p['t']} {p['m']} vs {comp[p['n']]}")
    print(f"== {ind}: overall emphasis {hl/max(1,tot):.0%}")
    for name, n, r in rows: print(f"   {name:9s} len {n:4d} ratio {r:.0%}")
    print(f"   watch {len(it['watch'])} players {len(it['players'])} reading {len(it['reading'])} terms {len(it['terms'])} missing {len(out['missing'])}")
    print(f"   PROBLEMS {len(P)}  WARN {len(W)}")
    for x in P: print("   !", x)
    for x in W: print("   ~", x)
for ind in sys.argv[1:]: check(ind)
