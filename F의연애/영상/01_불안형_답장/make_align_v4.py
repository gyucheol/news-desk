# Subtitle times for 01편 v4 (2026-10-25): the v3 times (lines_align_v3.json, checked line by line against the voice in
# v2/v3) carried over to the v4 lines, with every time after the cut sigh moved earlier by the cut length
# (edit_narration_v4.py -> cut_v4.json). No new alignment is run: the narration is the same apart from the cut, so the
# voice onsets are the same sounds. Lines are paired in order by their spoken Hangul; the two changes in the line list:
#   - '(아) 내가 연락을 너무 재촉하는 것처럼' -> '내가 연락을 너무 재촉하는 것처럼' (the 아 is cut from the recording;
#     the line already started at 내가, the first shown word),
#   - '이 마음속 경보 장치가' + '사라지지 않는다는 데 있습니다.' -> one centre line in two rows (owner 26): the start of
#     the first, the end of the second.
# usage: make_align_v4.py <episode folder> cut_v4.json -> <folder>/lines_align_v4.json
import json, re, sys

F, cutp = sys.argv[1], sys.argv[2]
cut = json.load(open(cutp))
v3 = json.load(open(f"{F}/lines_v3.json"))
a3 = {u["id"]: u for u in json.load(open(f"{F}/lines_align_v3.json"))}
v4 = json.load(open(f"{F}/lines_v4.json"))
norm = lambda o: re.sub(r"[^가-힣]", "", o["say"])


def shift(t):
    if t <= cut["keep_until"]:
        return t
    assert t >= cut["moved_from"], ("a time inside the cut", t)
    return round(t - cut["removed"], 3)


out, i = [], 0
for o in v4:
    n = norm(o)
    if norm(v3[i]) == n:
        src = [v3[i]]
    elif i + 1 < len(v3) and norm(v3[i]) + norm(v3[i + 1]) == n:
        src = [v3[i], v3[i + 1]]
    elif norm(v3[i]) == "아" + n:
        src = [v3[i]]
    else:
        raise SystemExit(f"no v3 line for {o['id']} {o['text']!r} (v3 {v3[i]['id']} {v3[i]['text']!r})")
    i += len(src)
    out.append({"id": o["id"], "text": o["say"], "shown": o["text"], "kind": o["kind"],
                "start": shift(a3[src[0]["id"]]["start"]), "end": shift(a3[src[-1]["id"]]["end"]),
                "v3": [s["id"] for s in src]})
assert i == len(v3), ("v3 lines left over", i, len(v3))
assert all(b["start"] > a["start"] for a, b in zip(out, out[1:]))
json.dump(out, open(f"{F}/lines_align_v4.json", "w"), ensure_ascii=False, indent=1)
moved = sum(1 for u in out if u["start"] != a3[u["v3"][0]]["start"])
print(len(out), "lines;", moved, "moved earlier by", cut["removed"], "s;",
      [(u["id"], u["v3"]) for u in out if len(u["v3"]) > 1 or norm(v3[0]) is None])
