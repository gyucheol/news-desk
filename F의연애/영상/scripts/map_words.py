# Recognised words of the original recordings -> the clock of an edited narration (F의 연애 01 v2, 2026-10-24).
# Each part's words are shifted by the part's start in the joined narration (and cut to its kept span) as in
# align_words.py, then moved through a time map written by an editing script (edit_narration_v2.py: pieces of the old
# clock kept in order; a word inside a removed pause stays at the cut). Output: one words file for align_words.py
# with offset 0.
# usage: map_words.py timemap.json out_words.json words.json:offset[:t_from:t_to] [...]
import json, sys
import numpy as np

tm = json.load(open(sys.argv[1]))
pairs = np.array(tm["pairs"])                    # (old, new) at every kept piece's start


def to_new(t):
    k = int(np.searchsorted(pairs[:, 0], t, side="right")) - 1
    k = max(k, 0)
    return float(pairs[k, 1] + (t - pairs[k, 0]))


segs = []
for spec in sys.argv[3:]:
    p, off, *rng = spec.split(":")
    off = float(off)
    lo, hi = (float(rng[0]), float(rng[1])) if rng else (-1e9, 1e9)
    for s in json.load(open(p)):
        ws = [[round(to_new(a + off), 3), round(to_new(b + off), 3), w, pr] for a, b, w, pr in s["words"] if lo <= a < hi]
        if ws:
            segs.append({"start": ws[0][0], "end": ws[-1][1], "text": s["text"], "words": ws})
json.dump(segs, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
print(len(segs), "segments,", sum(len(s["words"]) for s in segs), "words mapped")
