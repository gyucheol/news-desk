# Background music v2 (2026-10-24): owner "브금이 너무 잔잔바리인데, 살짝 텐션감이 있는 브금으로 변경 요청".
# Nine Mixkit Free tracks with a steady drum and bass pulse, one per part of the story (bgm_plan_v2.json: track,
# license, offset and why, measured values in work/stock/music/analysis_v2.txt). A track changes 0.4 s before the
# first subtitle of its part, with 3 s cross-fades (bgm_sequence.py: a later track starts 3 s early, so its offset is
# heard 3 s before the anchor). A part must end before the track's usable end (no fade-out or ending inside it); if the
# v2 timing makes a part longer than planned, the offset moves earlier.
# usage: make_bgm_segments_v2.py <episode folder> total_seconds -> <folder>/bgm_segments_v2.json
import json, math, re, sys

F, total = sys.argv[1], float(sys.argv[2])
XF = 3.0
lines = json.load(open(f"{F}/lines_v2.json"))
al = {u["id"]: u["start"] for u in json.load(open(f"{F}/lines_align_v2.json"))}
plan = json.load(open(f"{F}/bgm_plan_v2.json"))
plain = lambda s: re.sub(r"[\[\]]", "", s).replace("\n", " ")
# the plan's anchors as they read in the v2 subtitles (the plan's notes: '하지만 괜찮습니다' is split into 하지만 / 괜찮습니다)
ANCHORS = ["금요일 저녁 7시 퇴근길에", "지우는 2주째", "도대체 왜", "2004년", "도대체 왜 우리의 뇌는", "그런데 참 신기하죠",
           "하지만", "둘째", "생각해 보면"]
assert len(ANCHORS) == len(plan)


def t(prefix, after):
    for k, o in enumerate(lines):
        if k >= after and plain(o["text"]).startswith(prefix):
            return round(al[o["id"]] - 0.4, 2), k
    raise SystemExit(prefix)


segs, k = [], 0
for i, (anc, p) in enumerate(zip(ANCHORS, plan)):
    st, k = t(anc, k + (1 if i else 0))
    segs.append({"track": p["track"], "start": 0.0 if i == 0 else st, "offset": p["offset"], "mixkit": p["mixkit"],
                 "name": f'{p["title"]} / {p["author"]}', "why": p["why"], "usable_until": p["usable_until"]})
for i, s in enumerate(segs):
    s["end"] = segs[i + 1]["start"] if i + 1 < len(segs) else total
    used = s["end"] - s["start"] + (XF if i else 0)
    if s["offset"] + used > s["usable_until"]:
        new = math.floor((s["usable_until"] - used) * 2) / 2
        s["note"] = f'offset {s["offset"]} -> {new} s: the part is {used:.1f} s with the v2 timing, the track is usable to {s["usable_until"]} s'
        s["offset"] = new
json.dump(segs, open(f"{F}/bgm_segments_v2.json", "w"), ensure_ascii=False, indent=1)
for s in segs:
    print(f'{s["start"]:7.2f}-{s["end"]:7.2f}  {s["mixkit"]:>5} from {s["offset"]:5.1f} s  {s["name"]}  {s.get("note", "")}')
