# Hand-checked line starts (2026-10-24). onsets.py can take the pause AFTER a one-word line for its start when the
# recognised first word runs into that pause ("그룹이었습니다." got the start of the next line); such lines are checked
# with ctc_greedy-style syllable times and the energy curve, then fixed here by their text. Also flags implausible
# durations (line shorter than 55% of its syllables at 7.5 per second) so new cases are seen.
# usage: apply_overrides.py align_ctc.json overrides.json out.json
import json, re, sys
A = json.load(open(sys.argv[1])); ov = json.load(open(sys.argv[2])); out = sys.argv[3]
by_text = {}
for u in A:
    by_text.setdefault(u["shown"], []).append(u)
for o in ov:
    hits = by_text.get(o["text"], [])
    assert len(hits) == 1, (o["text"], len(hits))
    u = hits[0]
    u["start_auto"], u["start"], u["timing"] = u["start"], o["start"], "checked: " + o["why"]
for k in range(1, len(A)):
    assert A[k]["start"] > A[k - 1]["start"], (A[k - 1]["id"], A[k]["id"])
syl = lambda t: len(re.findall(r"[가-힣]", t))
for k in range(len(A) - 1):
    d = A[k + 1]["start"] - A[k]["start"]
    if d < 0.55 * syl(A[k]["text"]) / 7.5:
        print("CHECK", A[k]["id"], f"{d:.2f}s", A[k]["shown"])
json.dump(A, open(out, "w"), ensure_ascii=False, indent=1)
print(len(A), "lines,", len(ov), "checked by hand ->", out)
