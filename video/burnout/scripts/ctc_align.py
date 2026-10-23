# Character-level forced alignment of subtitle units (2026-10-23). Recognised word times from Whisper drift by up to
# 0.5 s inside continuous speech (바로 이 때문에 | 번아웃을), and energy rules cannot tell a word boundary from a
# consonant closure. A Korean CTC model with Hangul-syllable tokens (kresnik/wav2vec2-large-xlsr-korean, Apache-2.0,
# the default Korean alignment model of WhisperX) gives each syllable its frame (20 ms) by Viterbi alignment.
# Each unit inside continuous speech starts at its first syllable. After a real pause the energy onset from onsets.py
# is kept (it marks the first audible voice; CTC tends to fire at the vowel, a little late).
# usage: ctc_align.py audio onsets.json model_dir out.json      (onsets.json: output of onsets.py)
import json, re, subprocess, sys
import numpy as np
import torch
from transformers import Wav2Vec2ForCTC

audio, alp, mdir, outp = sys.argv[1:5]
SR, FR = 16000, 0.02
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                 capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
units = json.load(open(alp))
vocab = json.load(open(f"{mdir}/vocab.json"))
BLANK, UNK, SEP = vocab["[PAD]"], vocab["[UNK]"], vocab["|"]
torch.set_num_threads(4)
model = Wav2Vec2ForCTC.from_pretrained(mdir).eval()


def tokens(text):
    out = []
    for w in re.findall(r"[가-힣]+", text):
        if out:
            out.append((SEP, None))
        out += [(vocab.get(c, UNK), c) for c in w]
    return out


def viterbi(lp, y):
    """CTC forced alignment: lp (T, V) log-probs, y target ids -> first frame of each target."""
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


# chunks start at units that follow a real pause, about 6-25 s long
starts = [0] + [k for k, u in enumerate(units) if k and u["onset"] == "after pause"]
chunks, cur = [], 0
for k in starts[1:]:
    if units[k]["start"] - units[cur]["start"] >= 6.0:
        chunks.append((cur, k)); cur = k
chunks.append((cur, len(units)))
res = {}
for a, b in chunks:
    t0 = max(units[a]["start"] - 0.25, 0.0)
    t1 = units[b]["start"] - 0.03 if b < len(units) else len(x) / SR
    seg = x[int(t0 * SR):int(t1 * SR)]
    seg = (seg - seg.mean()) / (seg.std() + 1e-7)
    with torch.inference_mode():
        lp = torch.log_softmax(model(torch.from_numpy(seg)[None]).logits[0], -1).numpy()
    toks, owner = [], []
    for k in range(a, b):
        tk = tokens(units[k]["text"])
        if toks and tk:
            toks.append((SEP, None)); owner.append(None)
        toks += tk; owner += [k] * len(tk)
    first = viterbi(lp, np.array([t for t, _ in toks]))
    for i, (tk, k) in enumerate(zip(toks, owner)):
        if k is not None and k not in res:
            res[k] = t0 + first[i] * FR
out = []
for k, u in enumerate(units):
    c = res.get(k)
    v = dict(u, start_ctc=None if c is None else round(c, 3))
    if u["onset"] == "after pause":
        # after a real pause the measured voice onset wins: CTC fires at the vowel, 0.2-0.25 s late after a pause in
        # 4 of 183 units (자책하고: ㅈ starts before the spike)
        v["timing"] = "voice onset" + (" (ctc agrees)" if c is not None and abs(u["start"] - c) <= 0.15 else "")
    elif c is not None:
        v["start"], v["timing"] = round(c, 3), "ctc"   # inside continuous speech (개인의 질병으로: heuristics 0.6 s early)
    out.append(v)
for k in range(1, len(out)):                                   # keep order, at least 0.15 s apart
    out[k]["start"] = round(max(out[k]["start"], out[k - 1]["start"] + 0.15), 3)
json.dump(out, open(outp, "w"), ensure_ascii=False, indent=1)
d = np.array([v["start"] - u["start"] for v, u in zip(out, units)])
print(f"{len(chunks)} chunks | moved vs onsets.py: median {np.median(np.abs(d)):.3f}s, over 0.15 s: {int((np.abs(d) > 0.15).sum())}"
      f" | timing: {sum(v.get('timing') == 'ctc' for v in out)} ctc, "
      f"{sum(v.get('timing', '').startswith('voice') for v in out)} voice onset")
