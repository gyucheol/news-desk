# Subtitle times for 01편 v6 (2026-10-25): the line starts found on the edited v6 narration (onsets_v2.py, as v2),
# except the lines listed in FROM_JOINED, which take the start found on the joined narration before the pauses were
# shortened (onsets_v2.py on joined.wav), moved to the edited clock through timemap.json.
# Why: the two runs agree within 0.01 s on 483 of the 504 lines. Of the 8 lines that differ by more than 0.03 s, seven
# were checked on the loudness curve and the syllable recogniser and the edited-narration start is the voice onset
# (kept). For '자요..?' the recogniser's word times fell inside a pause that was shortened, so on the edited narration
# the line matched nothing and its start landed on '요' (0.30 s late); on the joined narration it starts where the
# 'ㅈ' begins (credits_v6.md 4장).
# usage: make_align_v6.py <episode folder> onsets_v2.json onsets_v2_joined.json timemap.json -> lines_align_v6.json
import json, sys
import numpy as np

F, fin_p, joi_p, tm_p = sys.argv[1:5]
FROM_JOINED = {"L097": "자요..?"}
tm = json.load(open(tm_p)); pairs = np.array(tm["pairs"])


def to_new(t):
    k = max(int(np.searchsorted(pairs[:, 0], t, side="right")) - 1, 0)
    return float(pairs[k, 1] + (t - pairs[k, 0]))


U = json.load(open(fin_p)); J = {u["id"]: u for u in json.load(open(joi_p))}
L = {o["id"]: o for o in json.load(open(f"{F}/lines_v6.json"))}
out = []
for u in U:
    o = {k: u[k] for k in ("id", "text", "start", "end", "anchor", "onset_v2", "first_consonant", "start_ctc") if k in u}
    if u["id"] in FROM_JOINED:
        assert L[u["id"]]["spoken"] == FROM_JOINED[u["id"]], u["id"]
        o["start_edited_run"] = o["start"]
        o["start"] = round(to_new(J[u["id"]]["start"]), 3)
        o["from_joined"] = True
    o["shown"] = L[u["id"]]["text"]; o["kind"] = L[u["id"]]["kind"]
    out.append(o)
assert all(b["start"] > a["start"] for a, b in zip(out, out[1:]))
json.dump(out, open(f"{F}/lines_align_v6.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "lines;", ", ".join(f'{i} {o["start_edited_run"]} -> {o["start"]}' for o in out if o.get("from_joined") for i in [o["id"]]))
