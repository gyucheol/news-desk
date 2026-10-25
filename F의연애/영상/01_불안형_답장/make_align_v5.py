# Subtitle times for 01편 v5 (2026-10-25): the narration and the lines are v4's (only four lines moved to the centre,
# subtitles_v5.txt), so every line keeps its v4 time (lines_align_v4.json); the kind and the shown text come from
# lines_v5.json. The spoken words of each line must be the same as in v4.
# usage: make_align_v5.py <episode folder> -> <folder>/lines_align_v5.json
import json, sys

F = sys.argv[1]
v4 = json.load(open(f"{F}/lines_align_v4.json"))
v5 = json.load(open(f"{F}/lines_v5.json"))
assert len(v4) == len(v5)
out = []
for a, o in zip(v4, v5):
    assert a["id"] == o["id"] and a["text"] == o["say"], (a["id"], a["text"], o["say"])
    out.append(dict(a, shown=o["text"], kind=o["kind"]))
json.dump(out, open(f"{F}/lines_align_v5.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "lines;", sum(a["kind"] != b["kind"] for a, b in zip(v4, out)), "changed kind")
