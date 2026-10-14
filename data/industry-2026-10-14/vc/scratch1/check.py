# VC.md 3절 확인: json.load, 모든 id, ind·node가 nodes.md에 있는지, f·dir·k 값, t 길이(12~45)와 금지 문자.
import json
import re
import sys
from collections import Counter

inp, out, nodes_md = sys.argv[1], sys.argv[2], sys.argv[3]

ids = []
with open(inp, encoding="utf-8") as fh:
    for line in fh:
        if line.strip():
            ids.append(json.loads(line)["id"])

with open(out, encoding="utf-8") as fh:
    vc = json.load(fh)

nodes = {}
cur = None
with open(nodes_md, encoding="utf-8") as fh:
    for line in fh:
        m = re.match(r"^## (\w+) — ", line)
        if m:
            cur = m.group(1)
            nodes[cur] = set()
            continue
        m = re.match(r"^- (\w+) — ", line)
        if m and cur:
            nodes[cur].add(m.group(1))

P = []
missing = [i for i in ids if i not in vc]
extra = [i for i in vc if i not in ids]
if missing:
    P.append(f"missing ids {missing}")
if extra:
    P.append(f"extra ids {extra}")
if len(ids) != len(set(ids)):
    P.append("duplicate input ids")

fc, dc, kc = Counter(), Counter(), Counter()
lens = []
for i, items in vc.items():
    if not isinstance(items, list) or not 1 <= len(items) <= 3:
        P.append(f"{i} item count {len(items) if isinstance(items, list) else type(items)}")
        continue
    seen = set()
    for x in items:
        if set(x) != {"ind", "node", "f", "dir", "k", "t"}:
            P.append(f"{i} keys {sorted(x)}")
        ind, node = x.get("ind"), x.get("node")
        if ind not in nodes:
            P.append(f"{i} ind {ind}")
        elif node not in nodes[ind]:
            P.append(f"{i} node {ind}/{node}")
        if x.get("f") not in ("공급", "수요", "가격", "-"):
            P.append(f"{i} f {x.get('f')}")
        if x.get("dir") not in ("up", "down", "flat", "mixed"):
            P.append(f"{i} dir {x.get('dir')}")
        if x.get("k") not in ("실제", "예상"):
            P.append(f"{i} k {x.get('k')}")
        if x.get("f") == "-" and x.get("dir") != "flat":
            P.append(f"{i} f '-' needs dir flat")
        key = (ind, node, x.get("f"))
        if key in seen:
            P.append(f"{i} same node+f twice {key}")
        seen.add(key)
        t = x.get("t", "")
        lens.append(len(t))
        if not 12 <= len(t) <= 45:
            P.append(f"{i} t length {len(t)}: {t}")
        if "{{" in t or "}}" in t:
            P.append(f"{i} t emphasis: {t}")
        if re.search(r"[\"'‘’“”「」『』]", t):
            P.append(f"{i} t quote: {t}")
        if t.endswith(".") or re.search(r"\.(\s|$)", t):
            P.append(f"{i} t period: {t}")
        if re.search(r"\[(사실|채널|제목|미확인)\]|\((제목 기준|채널 전언)\)", t):
            P.append(f"{i} t tag: {t}")
        if not re.search(r"[가-힣]", t):
            P.append(f"{i} t not Korean: {t}")
        fc[x.get("f")] += 1
        dc[x.get("dir")] += 1
        kc[x.get("k")] += 1

print("docs", len(ids), "out ids", len(vc), "items", sum(len(x) for x in vc.values()))
print("f", dict(fc))
print("dir", dict(dc))
print("k", dict(kc))
print("t len min/max", min(lens), max(lens))
print("PROBLEMS", len(P))
for p in P:
    print(" ", p)
