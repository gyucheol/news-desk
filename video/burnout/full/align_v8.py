# v8 subtitle line times (2026-10-23): align_v7.py for the v8 narration, plus
#   - steps: the rows of a centre sentence that appear when they are spoken (lines.json "steps", make_lines_v8.py);
#     each step starts like a line does (v6 unit time on a unit start, else the CTC syllable / after-pause rule);
#   - points: other moments tied to a word (POINTS; the big title 번아웃 on the U092 photo starts when 번아웃 is said);
#   - U271: the v4 hand fix (427.38 s) put "'아, 월요일 …" on the soft ending ㅂ니다 of U270 that the misplaced breathing
#     pause had pushed after the silence (owner on v7: "시작합니다 부분에 오디오가 이상해", fixed in
#     edit_narration_v8.py). With the pause after the word, U271 starts on the first voice after the pause (아), and
#     <folder>/align_refined.json is written with that one value changed.
# The CTC syllable times may come from the cache made on the v5/v7 narration: the v8 narration is the same sample for
# sample except 426.94-427.62 s, and no line, step or point used here lies in that stretch (checked).
#
# v7 subtitle line times (2026-10-23). Lines that start where a v6 unit started keep the v6 time (align_refined.json,
# owner-checked onsets). Lines that start inside a v6 unit (44 of them) get the time of their first syllable from the
# same CTC pass as scripts/ctc_align.py (same chunks, same Viterbi path, so every v6 unit start comes out the same:
# checked), with the same rule as onsets.py + ctc_align.py: after a real pause (no voice for 120 ms or more, or 60 ms
# after a comma or quote) the subtitle starts on the first voice frame after it; inside continuous speech it starts on
# the CTC frame of the syllable (CTC fires at the vowel, so it is never before the word).
# usage: align_v8.py narration.wav onsets.json align_final.json model_dir <folder with units.json, align_refined.json,
#        lines.json> out.json [syllables.json]
#   onsets.json / align_final.json: the v5 inputs and output of ctc_align.py (they give its chunks and its starts).
#   syllables.json: cache of the CTC syllable times (written when missing, read when present).
import json, os, re, subprocess, sys
import numpy as np

audio, onp, finp, mdir, F, outp = sys.argv[1:7]
cache = sys.argv[7] if len(sys.argv) > 7 else None
SR, FR, HOP = 16000, 0.02, 0.01
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                 capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
ons = json.load(open(onp))
final = json.load(open(finp))
units = json.load(open(f"{F}/units.json"))
al = {u["id"]: u for u in json.load(open(f"{F}/align_refined.json"))}
lines = json.load(open(f"{F}/lines.json"))
assert [u["id"] for u in ons] == [u["id"] for u in units]


def ctc_syllables():
    """(unit index, word index, syllable index) -> (first, last) seconds; chunks and Viterbi as in ctc_align.py"""
    import torch
    from transformers import Wav2Vec2ForCTC
    vocab = json.load(open(f"{mdir}/vocab.json"))
    BLANK, UNK, SEP = vocab["[PAD]"], vocab["[UNK]"], vocab["|"]
    torch.set_num_threads(4)
    model = Wav2Vec2ForCTC.from_pretrained(mdir).eval()

    def viterbi(lp, y):
        T, L = lp.shape[0], len(y)
        lab = np.full(2 * L + 1, BLANK); lab[1::2] = y
        S = len(lab)
        NEG = -1e30
        a = np.full(S, NEG); a[0] = lp[0, lab[0]]; a[1] = lp[0, lab[1]]
        skip = np.zeros(S, bool); skip[3::2] = lab[3::2] != lab[1:-2:2]
        back = np.zeros((T, S), np.int8)
        for t in range(1, T):
            s1 = np.concatenate([[NEG], a[:-1]]); s2 = np.concatenate([[NEG, NEG], a[:-2]]); s2[~skip] = NEG
            m = np.stack([a, s1, s2]); k = m.argmax(0)
            a = m[k, np.arange(S)] + lp[t, lab]; back[t] = k
        s = S - 1 if a[S - 1] >= a[S - 2] else S - 2
        first = np.full(L, -1); last = np.full(L, -1)
        for t in range(T - 1, -1, -1):
            if s % 2 == 1:
                first[s // 2] = t
                if last[s // 2] < 0:
                    last[s // 2] = t
            s -= int(back[t, s])
        return first, last

    starts = [0] + [k for k, u in enumerate(ons) if k and u["onset"] == "after pause"]
    chunks, cur = [], 0
    for k in starts[1:]:
        if ons[k]["start"] - ons[cur]["start"] >= 6.0:
            chunks.append((cur, k)); cur = k
    chunks.append((cur, len(ons)))
    syl = {}
    for a, b in chunks:
        t0 = max(ons[a]["start"] - 0.25, 0.0)
        t1 = ons[b]["start"] - 0.03 if b < len(ons) else len(x) / SR
        seg = x[int(t0 * SR):int(t1 * SR)]
        seg = (seg - seg.mean()) / (seg.std() + 1e-7)
        with torch.inference_mode():
            lp = torch.log_softmax(model(torch.from_numpy(seg)[None]).logits[0], -1).numpy()
        toks, owner = [], []
        for k in range(a, b):
            ws = re.findall(r"[가-힣]+", ons[k]["text"])
            if toks and ws:
                toks.append(SEP); owner.append(None)
            for wi, w in enumerate(ws):
                if wi:
                    toks.append(SEP); owner.append(None)
                for ci, c in enumerate(w):
                    toks.append(vocab.get(c, UNK)); owner.append((k, wi, ci))
        first, last = viterbi(lp, np.array(toks))
        for i, o in enumerate(owner):
            if o is not None:
                syl[o] = (round(t0 + first[i] * FR, 3), round(t0 + last[i] * FR + FR, 3))
    return syl


if cache and os.path.exists(cache):
    raw = json.load(open(cache))
    syl = {}
    for k, u in enumerate(raw):
        for wi, w in enumerate(u["words"]):
            for ci, t in enumerate(w["t"]):
                syl[(k, wi, ci)] = tuple(t)
else:
    syl = ctc_syllables()
    if cache:
        json.dump([{"id": u["id"], "words": [{"w": w, "t": [syl[(k, wi, ci)] for ci in range(len(w))]}
                                             for wi, w in enumerate(re.findall(r"[가-힣]+", u["text"]))]}
                   for k, u in enumerate(ons)], open(cache, "w"), ensure_ascii=False)
# the same CTC path as ctc_align.py: the first syllable of every unit lands where ctc_align.py put it (outside the
# stretch v8 changed, where a fresh CTC pass on the v8 narration may differ)
CHANGED = (426.94, 427.62)
bad = [u["id"] for k, u in enumerate(final) if u.get("start_ctc") is not None and syl[(k, 0, 0)][0] != u["start_ctc"]
       and not CHANGED[0] - 0.5 < u["start_ctc"] < CHANGED[1] + 0.5]
assert not bad, bad

# voice frames as in onsets.py
w = int(0.02 * SR)
db = 20 * np.log10(np.sqrt(np.convolve(x ** 2, np.ones(w) / w, mode="same")[::int(HOP * SR)] + 1e-12))
voice = db > np.percentile(db, 95) - 22
i = 0
while i < len(voice):
    if voice[i]:
        j = i
        while j < len(voice) and voice[j]:
            j += 1
        if j - i < 4 and i > 0 and j < len(voice):
            voice[i:j] = False
        i = j
    else:
        i += 1


def longest_quiet(ta, tb):
    a, b = int(round(ta / HOP)), int(round(tb / HOP))
    best, r0 = (0.0, None), None
    for i in range(a, b + 1):
        q = not voice[min(i, len(voice) - 1)]
        if q and r0 is None:
            r0 = i
        if (not q or i == b) and r0 is not None:
            r1 = i if not q else i + 1
            if (r1 - r0) * HOP > best[0]:
                best = ((r1 - r0) * HOP, r1 * HOP)
            r0 = None
    return best


uidx = {u["id"]: k for k, u in enumerate(units)}
words = {k: re.findall(r"[가-힣0-9]+", u["text"]) for k, u in enumerate(units)}     # = the CTC words
# the text between a word and the one before it (a comma or a quote there counts as a reading pause)
gaps = {k: [u["text"][a.end():b.start()] for a, b in zip(list(re.finditer(r"[가-힣0-9]+", u["text"]))[:-1],
                                                          list(re.finditer(r"[가-힣0-9]+", u["text"]))[1:])]
        for k, u in enumerate(units)}


def locate(k, at):
    """syllable number `at` of unit k -> (word index, syllable index in the word)"""
    for wi, wd in enumerate(words[k]):
        if at < len(wd):
            return wi, at
        at -= len(wd)
    raise ValueError


POINTS = {"title_U092": ("U094", 4)}      # 처음으로 '[번아웃]'이라고: the title fades in from the voice onset of 번아웃


def point_time(pid, uid, at, prev):
    """start of the word at syllable `at` of unit uid: the v6 unit time on a unit start, else CTC / after a pause"""
    k = uidx[uid]
    v = {"id": pid, "from": uid, "at": at}
    if at == 0:
        v.update(start=al[uid]["start"], how="v6 unit start")
    else:
        wi, ci = locate(k, at)
        assert ci == 0, (pid, "starts inside a word")
        tc = syl[(k, wi, 0)][0]
        tp = syl[(k, wi - 1, len(words[k][wi - 1]) - 1)][0]          # last syllable of the word before
        q, qend = longest_quiet(tp, tc + 0.04)
        punct = any(c in gaps[k][wi - 1] for c in ",.?!'\"…”’")
        if q >= 0.12 or (q >= 0.06 and punct):
            v.update(start=round(qend, 3), how=f"after pause ({q:.2f} s)")
        else:
            v.update(start=tc, how="ctc")
        v["start_ctc"] = tc
        v["after_word"] = words[k][wi - 1] + gaps[k][wi - 1].strip()
        assert not CHANGED[0] - 0.3 < v["start"] < CHANGED[1] + 0.3, (pid, "inside the stretch v8 changed")
    if prev is not None:
        v["start"] = round(max(v["start"], prev + 0.15), 3)
    return v


# U271 on the v8 narration: the first voice frame after the (moved) breathing pause
q, qend = longest_quiet(CHANGED[0] + 0.1, CHANGED[1] + 0.12)
assert q >= 0.3, q
u271_old = al["U271"]["start"]
al["U271"]["start"] = round(qend, 3)
al["U271"]["timing"] = "voice onset after the pause (v8; v4-v7 hand fix 427.38 was the misplaced ㅂ니다)"
refined = json.load(open(f"{F}/align_refined.json"))
for u in refined:
    if u["id"] == "U271":
        u.update(start=al["U271"]["start"], timing=al["U271"]["timing"])
json.dump(refined, open(f"{F}/align_refined.json", "w"), ensure_ascii=False, indent=1)
print(f"U271: {u271_old} -> {al['U271']['start']} (pause {q:.2f} s)")

out, extra = [], []
for n, l in enumerate(lines):
    v = point_time(l["id"], l["from"], l["at"], out[-1]["start"] if out else None)
    out.append(v)
    t = v["start"]
    for st in l.get("steps", []):
        w = point_time(st["id"], st["from"], st["at"], t)
        w.update(kind="step", line=l["id"], row=st["row"])
        extra.append(w); t = w["start"]
for pid, (uid, at) in POINTS.items():
    w = point_time(pid, uid, at, None)
    w["kind"] = "point"
    extra.append(w)
# ends: the end of the line's last unit when the next line starts on a unit start, else its last syllable
for n, v in enumerate(out):
    nxt = lines[n + 1] if n + 1 < len(lines) else None
    if nxt is None or nxt["at"] == 0:
        last_unit = units[(uidx[nxt["from"]] if nxt else len(units)) - 1]["id"]
        v["end"] = al[last_unit]["end"]
    else:
        k = uidx[nxt["from"]]
        wi, _ = locate(k, nxt["at"])
        v["end"] = syl[(k, wi - 1, len(words[k][wi - 1]) - 1)][1]
for w in extra:                              # a step must appear after its line starts and before the next line
    if w["kind"] == "step":
        n = next(i for i, v in enumerate(out) if v["id"] == w["line"])
        assert out[n]["start"] < w["start"] < (out[n + 1]["start"] if n + 1 < len(out) else 1e9), w
json.dump(out + extra, open(outp, "w"), ensure_ascii=False, indent=1)
new = [v for v in out if v["at"] > 0]
print(len(out), "lines;", len(new), "new starts:", sum(v["how"] == "ctc" for v in new), "ctc,",
      sum(v["how"].startswith("after") for v in new), "after a pause;", sum(w["kind"] == "step" for w in extra), "steps,",
      sum(w["kind"] == "point" for w in extra), "points")
for w in extra:
    print(f'  {w["id"]:12s} {w["start"]:8.3f} {w["how"]:22s} {w.get("after_word", "")}')
