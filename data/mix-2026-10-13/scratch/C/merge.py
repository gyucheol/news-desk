import json, os, collections
D = os.path.dirname(os.path.abspath(__file__))
B = os.path.abspath(os.path.join(D, "..", ".."))
p1 = json.load(open(os.path.join(D, "part1.json")))
p2 = json.load(open(os.path.join(D, "part2.json")))
groups = [tuple(c) for c in p1] + [tuple(c) for c in p2["C"]]
groups += [(t, f, a, [ln]) for ln, f, a, t in p2["S"]]
keep = [int(l.split("\t", 1)[0]) for l in open(os.path.join(B, "keep.tsv"), encoding="utf-8") if l.strip()]
groups.sort(key=lambda g: (-len(g[3]), min(g[3])))
clusters = [{"cid": "C%03d" % (i + 1), "theme": t, "field": f, "attachTo": a, "lines": sorted(ls)}
            for i, (t, f, a, ls) in enumerate(groups)]
drop = [{"line": l, "reason": r} for l, r in sorted(p2["DROP"])]
used = [l for c in clusters for l in c["lines"]] + [d["line"] for d in drop]
cnt = collections.Counter(used)
dup = sorted(l for l, n in cnt.items() if n > 1)
miss = sorted(set(keep) - set(cnt))
extra = sorted(set(cnt) - set(keep))
big = [c["cid"] for c in clusters if len(c["lines"]) >= 9]
print("keep", len(keep), "dup", dup, "missing", miss, "extra", extra, "big", big)
if not (dup or miss or extra):
    json.dump({"clusters": clusters, "drop": drop}, open(os.path.join(B, "clusters.json"), "w"), ensure_ascii=False, indent=1)
    print("clusters", len(clusters), "singles", sum(len(c["lines"]) == 1 for c in clusters),
          "attachTo", sum(bool(c["attachTo"]) for c in clusters), "drop", len(drop))
