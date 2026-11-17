"""W1 원고 합치기 + 자체 점검: python3 -I build.py"""
import json, re, runpy, os, sys
H = "/home/user/news-desk/data/mix-2026-11-16"
S = f"{H}/scratch/W1"
docs, skipped = [], []
for p in ("part1.py", "part2.py", "part3.py"):
    g = runpy.run_path(f"{S}/{p}")
    docs += g["L"]
    skipped += g.get("SKIP", [])
order = list(json.load(open(f"{H}/bundle/W1.meta.json")))
docs.sort(key=lambda x: order.index(x["cid"]))
out = {"agent": "W1", "searches_used": 16, "fetches_used": 6, "items": docs, "skipped": skipped}
json.dump(out, open(f"{H}/out2/W1.json", "w"), ensure_ascii=False, indent=1)

# ---- 자체 점검 ----
P = []
md = open(f"{H}/bundle/W1.md").read()
urls, cur = {}, None
for line in md.splitlines():
    m = re.match(r"^## (\S+) ", line)
    if m: cur = m.group(1); urls[cur] = []
    m = re.match(r"^### (.+?) · (\d\d)-(\d\d) (\d\d:\d\d) KST · (\S+)", line)
    if m and cur: urls[cur].append((m.group(5), f"2026-{m.group(2)}-{m.group(3)}"))
valid = {}
ind = None
for line in open("/home/user/news-desk/tools/industry/nodes.md"):
    m = re.match(r"^## (\w+) — ", line)
    if m: ind = m.group(1); valid[ind] = set(); continue
    m = re.match(r"^- (\w+) — ", line)
    if m and ind: valid[ind].add(m.group(1))
OLD9 = {"uranium", "drilling", "gas", "coal", "power", "petchem", "jpins", "beauty", "macro"}
meta = json.load(open(f"{H}/bundle/W1.meta.json"))
TAILS = (" (제목 기준)", " (채널 전언)")
def strip(s):
    for t in TAILS:
        if s.endswith(t): return s[:-len(t)]
    return s
for x in docs:
    c = x["cid"]; m = meta[c]
    if not 20 <= len(x["title"]) <= 70: P.append(f"{c} title {len(x['title'])}")
    lines = strip(x["one"]).split("\n")
    if not 40 <= len(lines[0]) <= 90: P.append(f"{c} one1 {len(lines[0])}")
    for i, l in enumerate(lines[1:], 2):
        if not 25 <= len(l) <= 90: P.append(f"{c} one{i} {len(l)}: {l[:30]}")
    if not 2 <= len(x["facts"]) <= 5: P.append(f"{c} facts {len(x['facts'])}")
    if not x["facts"][0].startswith("무엇이:"): P.append(f"{c} facts0")
    blob = json.dumps(x, ensure_ascii=False)
    for bad in ("|", "**", "{{"):
        if bad in blob: P.append(f"{c} 금지문자 {bad}")
    if m["attachTo"] != x["attachTo"]: P.append(f"{c} attachTo")
    if m["attachTo"]:
        a = x.get("added", "")
        if not 40 <= len(strip(a)) <= 140 or "내용이 추가됨" not in a: P.append(f"{c} added {len(a)}")
    elif "added" in x: P.append(f"{c} added 있으면 안 됨")
    bu = urls[c]
    if len(x["items"]) != len(bu): P.append(f"{c} items {len(x['items'])} vs {len(bu)}")
    for it, (u, d) in zip(x["items"], bu):
        if it["u"] != u: P.append(f"{c} url {it['u'][-40:]} != {u[-40:]}")
        if it["d"] != d: P.append(f"{c} date {it['d']} != {d}")
        if not 25 <= len(it["t"]) <= 60: P.append(f"{c} t {len(it['t'])}: {it['t']}")
        need_s = not (m["n"] <= 1 and not m["attachTo"])
        if need_s:
            s = strip(it.get("s", ""))
            if not 45 <= len(s) <= 110: P.append(f"{c} s {len(s)}: {s[:30]}")
            if not s.endswith("다"): P.append(f"{c} s 끝맺음: {s[-10:]}")
        elif "s" in it: P.append(f"{c} s 있으면 안 됨")
    for v in x["vc"]:
        if v["f"] not in ("공급", "수요", "가격", "-") or v["dir"] not in ("up", "down", "flat", "mixed") or v["k"] not in ("실제", "예상"): P.append(f"{c} vc 값")
        if not 12 <= len(v["t"]) <= 45: P.append(f"{c} vc t {len(v['t'])}: {v['t']}")
        if "newInd" in v:
            if v["ind"] in valid or v["node"] != "": P.append(f"{c} newInd")
        elif v["ind"] not in valid or v["node"] not in valid[v["ind"]]: P.append(f"{c} vc 노드 {v['ind']}/{v['node']}")
    for nd in x["nodes"]:
        i, n = nd.split("/")
        if i not in OLD9 or n not in valid[i]: P.append(f"{c} node {nd}")
        if i not in x["inds"]: P.append(f"{c} inds에 {i} 없음")
    for i in x["inds"]:
        if i not in valid: P.append(f"{c} ind {i}")
    tail = {"title": TAILS[0], "channel": TAILS[1]}.get(x["basis"])
    if tail and not x["one"].endswith(tail): P.append(f"{c} 꼬리")
    if x["basis"] == "verified" and x["one"].endswith(TAILS): P.append(f"{c} 꼬리 불필요")
print("docs", len(docs), "skipped", len(skipped), "self-problems", len(P))
for p in P: print(" -", p)
