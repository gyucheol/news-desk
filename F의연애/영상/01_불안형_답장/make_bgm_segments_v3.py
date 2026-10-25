# Background music v3 (2026-10-25): the owner on v2's music: "브금이 좀 긴장감 있었음 좋겠음. 너무 밝아. 정적인 교육
# 영상에 쓸법한 브금으로 변경 요청." The tracks, their licences, offsets and the reasons are in bgm_plan_v3.json (measured
# values in work/stock/music/analysis_v3.txt). As v2 (make_bgm_segments_v2.py): a track changes 0.4 s before the first
# subtitle of its part (the plan's "anchor", searched in order in the v3 subtitles), with 3 s cross-fades
# (bgm_sequence.py: a later track starts 3 s early, so its offset is heard 3 s before the anchor). A part must end
# before the track's usable end; if it is longer than planned, the offset moves earlier.
# usage: make_bgm_segments_v3.py <episode folder> total_seconds -> <folder>/bgm_segments_v3.json
import json, math, re, sys

F, total = sys.argv[1], float(sys.argv[2])
XF = 3.0
lines = json.load(open(f"{F}/lines_v3.json"))
al = {u["id"]: u["start"] for u in json.load(open(f"{F}/lines_align_v3.json"))}
plan = json.load(open(f"{F}/bgm_plan_v3.json"))
plain = lambda s: re.sub(r"[\[\]]", "", s).replace("\n", " ")


def t(prefix, after):
    for k, o in enumerate(lines):
        if k >= after and plain(o["text"]).startswith(prefix):
            return round(al[o["id"]] - 0.4, 2), k
    raise SystemExit(f"anchor not found: {prefix}")


segs, k = [], 0
for i, p in enumerate(plan):
    st, k = (0.0, 0) if i == 0 else t(p["anchor"], k + 1)
    segs.append({"track": p["track"], "start": st, "offset": p["offset"], "source": p.get("source", "Mixkit"),
                 "id": p.get("id", p.get("mixkit")), "name": f'{p["title"]} / {p["author"]}', "url": p.get("url", ""),
                 "license": p.get("license", ""), "why": p["why"], "usable_until": p["usable_until"]})
for i, s in enumerate(segs):
    s["end"] = segs[i + 1]["start"] if i + 1 < len(segs) else total
    used = s["end"] - s["start"] + (XF if i else 0)
    if s["offset"] + used > s["usable_until"]:
        new = math.floor((s["usable_until"] - used) * 2) / 2
        assert new >= 0, (s["name"], "track too short for its part", used, s["usable_until"])
        s["note"] = f'offset {s["offset"]} -> {new} s: the part is {used:.1f} s, the track is usable to {s["usable_until"]} s'
        s["offset"] = new
json.dump(segs, open(f"{F}/bgm_segments_v3.json", "w"), ensure_ascii=False, indent=1)
for s in segs:
    print(f'{s["start"]:7.2f}-{s["end"]:7.2f}  {s["id"]} from {s["offset"]:5.1f} s  {s["name"]}  {s.get("note", "")}')
