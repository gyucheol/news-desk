"""VC.md 3절 검사: json.load, 입력 id 전부, ind·node가 nodes.md에 있는지, f·dir·k 값, t 길이(12~45자).
덧붙여: 문서당 1~3개, 같은 node·f 중복 없음, '-'이면 dir flat, t에 {{ }}·따옴표·꼬리표·끝 마침표 없음.
사용: python3 -I check.py <in.jsonl> <out.json> <nodes.md>"""
import json, re, sys
from collections import Counter

inp, outp, nodes_md = sys.argv[1:4]
P = []
ids = [json.loads(l)["id"] for l in open(inp, encoding="utf-8") if l.strip()]
try:
    out = json.load(open(outp, encoding="utf-8"))
except Exception as e:
    print("PROBLEMS 1\n - json.load 실패:", e); sys.exit(1)

valid, ind = set(), None
for line in open(nodes_md, encoding="utf-8"):
    m = re.match(r"^## (\w+) — ", line)
    if m: ind = m.group(1); continue
    m = re.match(r"^- (\w+) — ", line)
    if m and ind: valid.add((ind, m.group(1)))

for i in ids:
    if i not in out: P.append(f"{i} 출력에 없음")
for i in out:
    if i not in ids: P.append(f"{i} 입력에 없는 id")
if len(ids) != len(set(ids)): P.append("입력 id 중복")

F, D, K = {"공급", "수요", "가격", "-"}, {"up", "down", "flat", "mixed"}, {"실제", "예상"}
cf, cd, ck, lens = Counter(), Counter(), Counter(), []
for i, items in out.items():
    if not isinstance(items, list) or not 1 <= len(items) <= 3: P.append(f"{i} 항목 수 {len(items) if isinstance(items, list) else items!r}")
    seen = set()
    for x in items:
        if set(x) != {"ind", "node", "f", "dir", "k", "t"}: P.append(f"{i} 키 {sorted(x)}")
        if (x.get("ind"), x.get("node")) not in valid: P.append(f"{i} ind·node 없음 {x.get('ind')}/{x.get('node')}")
        if x.get("f") not in F: P.append(f"{i} f {x.get('f')}")
        if x.get("dir") not in D: P.append(f"{i} dir {x.get('dir')}")
        if x.get("k") not in K: P.append(f"{i} k {x.get('k')}")
        if x.get("f") == "-" and x.get("dir") != "flat": P.append(f"{i} f '-'인데 dir {x.get('dir')}")
        key = (x.get("ind"), x.get("node"), x.get("f"))
        if key in seen: P.append(f"{i} 같은 node·f 중복 {key}")
        seen.add(key)
        t = x.get("t") or ""
        lens.append(len(t))
        if not 12 <= len(t) <= 45: P.append(f"{i} t 길이 {len(t)}: {t}")
        if re.search(r"\{\{|\}\}|[\"'‘’“”「」『』]|\[[^\]]*\]|\((사실|채널|제목|추론|미확인|예상|실제)", t): P.append(f"{i} t 금지 문자·꼬리표: {t}")
        if t.rstrip().endswith((".", "。", "…")): P.append(f"{i} t 끝 마침표: {t}")
        if not re.search(r"[가-힣]", t): P.append(f"{i} t 한국어 아님: {t}")
        cf[x.get("f")] += 1; cd[x.get("dir")] += 1; ck[x.get("k")] += 1

print("docs", len(out), "/ input", len(ids), "| items", sum(len(v) for v in out.values()))
print("f", dict(cf), "| dir", dict(cd), "| k", dict(ck))
print("t len min", min(lens), "max", max(lens))
print("PROBLEMS", len(P))
for p in P: print(" -", p)
