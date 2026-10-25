# Subtitle times for 01편 v7 (2026-10-25, the owner's v7 list). The narration is v6's with seven lines cut out
# (edit_narration_v7.py), so every line that v7 keeps from v6 keeps its v6 start (the one found on the v6 narration,
# lines_align_v6.json), moved to the v7 clock: unchanged before the cut, cut_seconds earlier after it.
# Two v6 lines are split in two by the owner (list 9: "이 마음속 경보 장치가" (끊고) "사라지지 않는다는 데 있습니다",
# list 12: "지금 내 삶에서(끊고) 그 사람이 그만큼 소중하다는(끊고) 아주 솔직한 신호인지도 모르겠습니다."). The first part
# keeps the line's start; the second part starts where its first syllable is heard, found as for every other line
# (onsets_v2.py on the v7 narration, anchored on that syllable's frame from the v6 syllable alignment, ctc_align.py).
#   step "ctc":   v6 align_ctc.json -> v7 align_ctc.json (v7 line ids, v7 clock, the two split lines' syllables shared
#                 out by the syllables of each part), for onsets_v2.py
#   step "final": onsets_v2.py's result on the v7 narration + lines_align_v6.json -> lines_align_v7.json. It also
#                 prints how far the new run is from the moved v6 starts for the lines v7 keeps (a check).
# usage: make_align_v7.py ctc <episode folder> v6_align_ctc.json out_align_ctc.json
#        make_align_v7.py final <episode folder> v7_onsets_v2.json
import difflib, json, re, sys

step, F = sys.argv[1], sys.argv[2]
L6 = json.load(open(f"{F}/lines_v6.json")); L7 = json.load(open(f"{F}/lines_v7.json"))
cut = json.load(open(f"{F}/edit_log_v7.json"))
s1, s2 = cut["cut_v6_clock"]; D = cut["cut_seconds"]
norm = lambda s: re.sub(r"[^0-9A-Za-z가-힣]", "", s)
han = lambda s: re.findall(r"[가-힣]", s)


def to_v7(t):
    if t is None:
        return None
    assert not (s1 <= t < s2), ("time inside the cut", t)
    return round(t if t < s1 else t - D, 3)


# v7 line -> (v6 line, part index, number of parts)
src = {}
sm = difflib.SequenceMatcher(None, [norm(o["spoken"]) for o in L6], [norm(o["spoken"]) for o in L7], autojunk=False)
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == "equal":
        for a, b in zip(range(i1, i2), range(j1, j2)):
            src[L7[b]["id"]] = (L6[a]["id"], 0, 1)
    elif tag == "delete":                       # only the seven lines cut out of the narration
        removed = [x.split()[0] for x in cut["removed_lines"]]
        assert [o["id"] for o in L6[i1:i2]] == removed, (L6[i1:i2], removed)
    elif tag == "replace":
        assert i2 - i1 == 1 and j2 - j1 >= 2, (tag, L6[i1:i2], L7[j1:j2])
        assert "".join(norm(o["spoken"]) for o in L7[j1:j2]) == norm(L6[i1]["spoken"]), (L6[i1], L7[j1:j2])
        for p, b in enumerate(range(j1, j2)):
            src[L7[b]["id"]] = (L6[i1]["id"], p, j2 - j1)
    else:
        raise AssertionError((tag, L6[i1:i2], L7[j1:j2]))
assert len(src) == len(L7)
splits = {k: v for k, v in src.items() if v[2] > 1}

if step == "ctc":
    C6 = {u["id"]: u for u in json.load(open(sys.argv[3]))}
    out = []
    for o in L7:
        v6id, part, n = src[o["id"]]
        u = C6[v6id]
        syl = [[s, to_v7(t)] for s, t in u.get("syl") or []]
        if n == 1:
            v = dict(u, id=o["id"], text=o["say"], shown=o["text"].replace("\n", " "), syl=syl,
                     start=to_v7(u["start"]), end=to_v7(u["end"]), start_ctc=to_v7(u.get("start_ctc")),
                     start_asr=to_v7(u.get("start_asr")), first_word_end=to_v7(u.get("first_word_end")))
        else:                                   # share the syllables out: each part takes as many as it has
            sizes = [len(han(p["say"])) for p in L7 if src[p["id"]][0] == v6id]
            assert sum(sizes) == len(syl) and "".join(s for s, _ in syl) == "".join(han(u["text"])), (v6id, sizes)
            a = sum(sizes[:part]); mine = syl[a:a + sizes[part]]
            assert [s for s, _ in mine] == han(o["say"]), (o["id"], mine)
            v = {"id": o["id"], "text": o["say"], "shown": o["text"].replace("\n", " "), "syl": mine,
                 "start": to_v7(u["start"]) if part == 0 else mine[0][1],
                 "end": round(mine[-1][1] + 0.10, 3) if part < n - 1 else to_v7(u["end"]),
                 "start_ctc": to_v7(u.get("start_ctc")) if part == 0 else mine[0][1],
                 "split_from": v6id, "part": part + 1}
        out.append(v)
    json.dump(out, open(sys.argv[4], "w"), ensure_ascii=False, indent=1)
    print(len(out), "lines;", "split:", ", ".join(f"{k} <- {v[0]} part {v[1] + 1}/{v[2]}" for k, v in splits.items()))

elif step == "final":
    A6 = {a["id"]: a for a in json.load(open(f"{F}/lines_align_v6.json"))}
    R = {u["id"]: u for u in json.load(open(sys.argv[3]))}
    out, diffs = [], []
    for o in L7:
        v6id, part, n = src[o["id"]]
        if n == 1 or part == 0:                 # a v6 line (or the first part of one): its v6 start, moved
            a = A6[v6id]
            v = {k: a[k] for k in ("start", "end", "anchor", "onset_v2", "first_consonant", "start_ctc") if k in a}
            for k in ("start", "end", "anchor", "start_ctc"):
                if v.get(k) is not None:
                    v[k] = to_v7(v[k])
            v["from_v6"] = v6id
            if n > 1:
                v["end"] = R[o["id"]]["end"]; v["split_from"] = v6id; v["part"] = 1
            diffs.append((round(R[o["id"]]["start"] - v["start"], 3), o["id"], v6id))
        else:                                   # a new part: its own onset on the v7 narration
            r = R[o["id"]]
            v = {k: r[k] for k in ("start", "end", "anchor", "onset_v2", "first_consonant", "start_ctc")}
            v.update(split_from=v6id, part=part + 1)
        out.append(dict({"id": o["id"], "text": o["say"]}, **v, shown=o["text"], kind=o["kind"]))
    assert all(b["start"] > a["start"] for a, b in zip(out, out[1:]))
    json.dump(out, open(f"{F}/lines_align_v7.json", "w"), ensure_ascii=False, indent=1)
    big = [d for d in diffs if abs(d[0]) > 0.010]
    print(len(out), "lines | new run vs moved v6 start, lines kept from v6:", len(diffs), "| within 10 ms:",
          len(diffs) - len(big), "| more:", big)
    for k, v in splits.items():
        u = next(x for x in out if x["id"] == k)
        print(f"  {k} ({v[0]} part {v[1] + 1}/{v[2]}): {u['start']:.3f} {u['onset_v2']} {u['first_consonant']} {u['shown']}")
