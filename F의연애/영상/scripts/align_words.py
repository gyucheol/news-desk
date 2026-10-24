# align.py without running the recogniser again: the narration was joined from several recordings that were each
# recognised once (faster-whisper large-v3, same settings as align.py). Words are shifted by each part's start in the
# joined narration and cut to the kept span, then matched to the units by characters exactly as align.py does.
# usage: align_words.py units.json out.json words.json:offset[:t_from:t_to] [...]
import json, re, sys, difflib

units = json.load(open(sys.argv[1]))
norm = lambda s: re.sub(r"[^0-9A-Za-z가-힣]", "", s)
words = []
for spec in sys.argv[3:]:
    p, off, *rng = spec.split(":")
    off = float(off)
    lo, hi = (float(rng[0]), float(rng[1])) if rng else (-1e9, 1e9)
    for s in json.load(open(p)):
        for a, b, w, pr in s["words"]:
            if lo <= a < hi and b - a > 0.0:          # zero-length words are Whisper's repeats (checked by ear-free CTC)
                words.append((a + off, b + off, w))
asr_chars, asr_t, asr_w = [], [], []
for wi, (a, b, w) in enumerate(words):
    cs = norm(w)
    for i, c in enumerate(cs):
        asr_chars.append(c); asr_t.append((a + (b - a) * i / len(cs), a + (b - a) * (i + 1) / len(cs))); asr_w.append(wi)
sc_chars, sc_unit = [], []
for k, u in enumerate(units):
    for c in norm(u["text"]):
        sc_chars.append(c); sc_unit.append(k)
sm = difflib.SequenceMatcher(None, sc_chars, asr_chars, autojunk=False)
m = {}
for blk in sm.get_matching_blocks():
    for j in range(blk.size):
        m[blk.a + j] = blk.b + j
res = []
for k, u in enumerate(units):
    hit = [m[i] for i, uu in enumerate(sc_unit) if uu == k and i in m]
    n = sum(1 for uu in sc_unit if uu == k)
    res.append({"id": u["id"], "text": u["text"],
                "start": float(asr_t[min(hit)][0]) if hit else None,
                "end": float(asr_t[max(hit)][1]) if hit else None,
                "first_word_end": float(words[asr_w[min(hit)]][1]) if hit else None,
                "match": round(len(hit) / max(n, 1), 2)})
for k, r in enumerate(res):
    if r["start"] is None:
        prev = next((res[j]["end"] for j in range(k - 1, -1, -1) if res[j]["end"] is not None), 0.0)
        r["start"] = r["end"] = r["first_word_end"] = prev
        r["warning"] = "not recognized - check"
json.dump(res, open(sys.argv[2], "w"), ensure_ascii=False, indent=1)
low = [r for r in res if r["match"] < 0.8 or "warning" in r]
print(len(res), "units |", len(low), "with match < 0.8:", " ".join(f'{r["id"]}({r["match"]})' for r in low))
