# Time the one-line subtitles of a Short. Each subtitle line of the episode is cut into the chunks the owner listed,
# and every chunk appears when its first word is spoken, by the rule of full/align_v8.py:
#   - a chunk that starts a line keeps the line's owner-checked start (lines_align.json);
#   - a chunk inside a line starts on the first voice after a pause of 120 ms or more (60 ms after a comma or quote),
#     otherwise on the CTC frame of its first syllable (CTC fires at the vowel, so never before the word);
#   - at least 0.15 s after the chunk before.
# CTC: the Korean wav2vec2 model of scripts/ctc_align.py, forced alignment of the line's spoken text on the line's audio.
# usage: split_subs.py narration.wav model_dir <folder with lines.json, lines_align.json, build_spec.py> spec.json out.json
#   spec "one_line": {line id: [chunks as spoken]}; "display": {chunk: text on screen} for chunks that differ
#   (numbers come from build_spec.py DIGITS, the yellow word from the line's [ ] mark).
import ast, json, re, subprocess, sys
import numpy as np

audio, mdir, F, spec_path, outp = sys.argv[1:6]
sp = json.load(open(spec_path))
lines = json.load(open(f"{F}/lines.json"))
times = {a["id"]: a for a in json.load(open(f"{F}/lines_align.json"))}
src = open(f"{F}/build_spec.py", encoding="utf-8").read()
DIGITS = ast.literal_eval(re.search(r"^DIGITS = (\[.*?\])\n", src, re.S | re.M).group(1))
SR, FR, HOP = 16000, 0.02, 0.01
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                 capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768

# voice frames as in onsets.py / align_v8.py (threshold from the whole narration)
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


import torch
from transformers import Wav2Vec2ForCTC
vocab = json.load(open(f"{mdir}/vocab.json"))
BLANK, UNK, SEP = vocab["[PAD]"], vocab["[UNK]"], vocab["|"]
torch.set_num_threads(4)
model = Wav2Vec2ForCTC.from_pretrained(mdir).eval()


def viterbi(lp, y):                      # same as full/align_v8.py
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
    first = np.full(L, -1)
    for t in range(T - 1, -1, -1):
        if s % 2 == 1:
            first[s // 2] = t
        s -= int(back[t, s])
    return first


order = [l["id"] for l in lines]
by_id = {l["id"]: l for l in lines}
out = []
for lid, chunks in sorted(sp["one_line"].items(), key=lambda kv: order.index(kv[0])):
    line = by_id[lid]
    spoken = line.get("spoken", line["text"])
    assert re.sub(r"[\s\[\]]", "", "".join(chunks)) == re.sub(r"[\s\[\]]", "", spoken), (lid, chunks, spoken)
    t_line = times[lid]["start"]
    nxt = order[order.index(lid) + 1] if order.index(lid) + 1 < len(order) else None
    t0 = max(t_line - 0.25, 0.0)
    t1 = (times[nxt]["start"] - 0.03) if nxt else times[lid]["end"] + 0.3
    words = re.findall(r"[가-힣]+", spoken)
    toks, owner = [], []
    for wi, wd in enumerate(words):
        if wi:
            toks.append(SEP); owner.append(None)
        for ci, c in enumerate(wd):
            toks.append(vocab.get(c, UNK)); owner.append((wi, ci))
    seg = x[int(t0 * SR):int(t1 * SR)]
    seg = (seg - seg.mean()) / (seg.std() + 1e-7)
    with torch.inference_mode():
        lp = torch.log_softmax(model(torch.from_numpy(seg)[None]).logits[0], -1).numpy()
    first = viterbi(lp, np.array(toks))
    syl = {o: round(t0 + first[i] * FR, 3) for i, o in enumerate(owner) if o is not None}
    emph = re.findall(r"\[(.+?)\]", line["text"])
    wi, prev = 0, None
    for ci, ch in enumerate(chunks):
        shown = sp.get("display", {}).get(ch, ch)
        for a, b in DIGITS:
            shown = shown.replace(a, b)
        for e in emph:
            if e in shown and f"[{e}]" not in shown:
                shown = shown.replace(e, f"[{e}]")
        n = len(re.findall(r"[가-힣]+", ch))
        v = {"line": lid, "chunk": ci, "spoken": ch, "text": shown}
        if ci == 0:
            v.update(start=t_line, how="line start")
        else:
            tc = syl[(wi, 0)]
            tp = syl[(wi - 1, len(words[wi - 1]) - 1)]
            q, qend = longest_quiet(tp, tc + 0.04)
            punct = bool(re.search(r"[,.?!'\"…”’]\s*$", chunks[ci - 1]))
            if q >= 0.12 or (q >= 0.06 and punct):
                v.update(start=round(qend, 3), how=f"after pause ({q:.2f} s)")
            else:
                v.update(start=tc, how="ctc")
            v["start_ctc"] = tc
            v["start"] = round(max(v["start"], prev + 0.15), 3)
        out.append(v); prev = v["start"]; wi += n
json.dump(out, open(outp, "w"), ensure_ascii=False, indent=1)
for v in out:
    print(f'{v["line"]}.{v["chunk"]} {v["start"]:8.3f} {v["how"]:<22} {v["text"]}')
print(len(out), "chunks")
