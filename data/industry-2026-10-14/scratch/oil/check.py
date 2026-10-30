"""Format + emphasis checker for an industry page JSON (BUILD.md step 4).
usage: python3 check.py <out.json> [news.tsv nodemap.tsv]
"""
import json, re, sys

path = sys.argv[1]
d = json.load(open(path))
errs, warns = [], []

# --- required top-level keys
for k in ["id", "name", "short", "icon", "order", "asOf", "rev", "summary", "intro", "nodes", "cycle",
          "industryState", "insight", "flows", "gaps", "history"]:
    if k not in d:
        errs.append(f"missing top key {k}")
if len(d.get("short", "")) > 6:
    errs.append(f"top short >6: {d['short']}")
if d.get("insight") != {} or d.get("flows") != []:
    errs.append("insight must be {} and flows []")

# --- intro
it = d["intro"]
for k, lo, hi in [("watch", 3, 5), ("players", 5, 8), ("reading", 3, 5), ("terms", 3, 6)]:
    n = len(it.get(k, []))
    if not lo <= n <= hi:
        errs.append(f"intro.{k} count {n} not in {lo}-{hi}")
for k in ["watch", "players", "terms"]:
    if "{{" in json.dumps(it[k], ensure_ascii=False):
        errs.append(f"intro.{k} must not contain emphasis")
for p in it["players"]:
    for f in ["n", "t", "m", "role"]:
        if f not in p:
            errs.append(f"player missing {f}: {p}")

# --- nodes
nodes = d["nodes"]
ids = [n["id"] for n in nodes]
if len(ids) != len(set(ids)):
    errs.append(f"duplicate node ids {ids}")
if not 5 <= len(nodes) <= 9:
    errs.append(f"node count {len(nodes)}")
for n in nodes:
    if not re.fullmatch(r"[a-z]{2,12}", n["id"]):
        errs.append(f"bad node id {n['id']}")
    if len(n["short"]) > 6:
        errs.append(f"node short >6: {n['short']}")
    if not 2 <= len(n["indicators"]) <= 3:
        errs.append(f"{n['id']} indicators {len(n['indicators'])}")
    if not 2 <= len(n["companies"]) <= 5:
        errs.append(f"{n['id']} companies {len(n['companies'])}")
    if len(n.get("state", [])) > 3:
        errs.append(f"{n['id']} state >3")
    if "stage" in n and n["stage"] is not None and not 1 <= n["stage"] <= 8:
        errs.append(f"{n['id']} stage {n['stage']}")
    for s in n.get("state", []):
        for f in ["d", "o", "t", "u"]:
            if not s.get(f):
                errs.append(f"{n['id']} state missing {f}")
    for l in n.get("links", []):
        if not re.fullmatch(r"[a-z]+/[a-z]+", l.get("to", "")):
            errs.append(f"{n['id']} bad link {l}")

# --- cycle
c = d["cycle"]
if not isinstance(c.get("stage"), int) or not 1 <= c["stage"] <= 8:
    errs.append(f"cycle.stage {c.get('stage')}")
if c.get("conf") not in ("높음", "중간", "낮음"):
    errs.append("cycle.conf")
if not 2 <= len(c["why"]) <= 4:
    errs.append(f"cycle.why count {len(c['why'])}")
for w in c["why"]:
    if not w.get("src"):
        errs.append("why without src")
    for s in w["src"]:
        if not s.get("o") or not s.get("u"):
            errs.append(f"why src missing o/u: {s}")
    if not re.search(r"\[(사실|귀납|유추|추측|연역)\]$", w["t"]):
        errs.append(f"why tag missing: {w['t'][-20:]}")
if not 3 <= len(c["watch"]) <= 5:
    errs.append("cycle.watch count")
for sp in c.get("split", []):
    for nid in sp["nodes"]:
        if nid not in ids:
            errs.append(f"split node {nid} unknown")
if not 2 <= len(d["industryState"]) <= 5:
    errs.append(f"industryState count {len(d['industryState'])}")
for s in d["industryState"]:
    if s["kind"] not in ("price", "supply", "demand", "capex", "policy"):
        errs.append(f"industryState kind {s['kind']}")
    for f in ["d", "o", "t", "u"]:
        if not s.get(f):
            errs.append(f"industryState missing {f}")

# --- every src-like item (anything with 'u') has o and u
def walk(x, path=""):
    if isinstance(x, dict):
        if "u" in x and (not x.get("o") or not x.get("u")):
            errs.append(f"src item without o/u at {path}")
        for k, v in x.items():
            walk(v, path + "." + k)
    elif isinstance(x, list):
        for i, v in enumerate(x):
            walk(v, f"{path}[{i}]")
walk(d)

# --- emphasis checks
def emph_fields():
    yield "summary", d["summary"]
    for k in ["what", "money", "drivers"]:
        yield f"intro.{k}", it[k]
    for i, r in enumerate(it["reading"]):
        yield f"reading[{i}].means", r["means"]
    for n in nodes:
        yield f"{n['id']}.role", n["role"]
        if n.get("bottleneck"):
            yield f"{n['id']}.bottleneck", n["bottleneck"]
        for j, co in enumerate(n["companies"]):
            yield f"{n['id']}.co[{j}]", co["note"]
        for j, s in enumerate(n.get("state", [])):
            yield f"{n['id']}.state[{j}]", s["t"]
    for i, w in enumerate(c["why"]):
        yield f"why[{i}]", w["t"]
    yield "cycle.next", c["next"]

TAG = re.compile(r"\s*\[(사실|귀납|유추|추측|연역)\]")
report = []
for name, s in emph_fields():
    if s.count("{{") != s.count("}}"):
        errs.append(f"{name}: unbalanced braces")
        continue
    if re.search(r"\{\{[^}]*\{\{", s):
        errs.append(f"{name}: nested braces")
    chunks = re.findall(r"\{\{(.*?)\}\}", s)
    if not chunks:
        errs.append(f"{name}: no emphasis")
        continue
    for ch in chunks:
        if ch != ch.strip():
            errs.append(f"{name}: chunk has edge space '{ch}'")
        if len(ch) > 30:
            warns.append(f"{name}: long chunk ({len(ch)}) '{ch}'")
        if ch and ch[-1] in ",.":
            errs.append(f"{name}: punctuation inside chunk '{ch}'")
        if re.search(r"\[(사실|귀납|유추|추측)\]", ch):
            errs.append(f"{name}: tag inside chunk")
    plain = TAG.sub("", s.replace("{{", "").replace("}}", ""))
    em = "".join(chunks)
    tot = len(plain.replace(" ", ""))
    emn = len(em.replace(" ", ""))
    r = emn / tot if tot else 0
    report.append((name, round(r, 2)))
    if r < 0.45 or r > 0.70:
        warns.append(f"{name}: emphasis ratio {r:.2f}")

# --- news coverage
if len(sys.argv) > 3:
    news = [l.split("\t")[1] for l in open(sys.argv[2], encoding="utf-8") if l.strip()]
    mp = dict(l.rstrip("\n").split("\t")[:2] for l in open(sys.argv[3], encoding="utf-8") if l.strip())
    for nid in news:
        if nid not in mp:
            errs.append(f"news {nid} unmapped")
        elif mp[nid] not in ids:
            errs.append(f"news {nid} mapped to unknown node {mp[nid]}")

avg = sum(r for _, r in report) / len(report)
print(f"fields with emphasis: {len(report)}, mean ratio {avg:.2f}, min {min(r for _,r in report)}, max {max(r for _,r in report)}")
print("ERRORS:", len(errs))
for e in errs:
    print("  E", e)
print("WARNINGS:", len(warns))
for w in warns:
    print("  W", w)
