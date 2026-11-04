# 새 녹음에서 '열나흘'과 '십사 일' 중 어느 쪽으로 읽었는지: 같은 구간을 두 글로 강제 맞춤해 점수(로그 확률)를 견줌.
import json, re, subprocess, sys
import numpy as np, torch
from transformers import Wav2Vec2ForCTC
mdir = sys.argv[1]; audio = sys.argv[2]
SR = 16000
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                 capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
vocab = json.load(open(f"{mdir}/vocab.json")); BLANK, UNK, SEP = vocab["[PAD]"], vocab["[UNK]"], vocab["|"]
model = Wav2Vec2ForCTC.from_pretrained(mdir).eval()
def toks(text):
    out = []
    for w in re.findall(r"[가-힣]+", text):
        if out: out.append(SEP)
        out += [vocab.get(c, UNK) for c in w]
    return np.array(out)
def score(lp, y):
    T, L = lp.shape[0], len(y)
    lab = np.full(2 * L + 1, BLANK); lab[1::2] = y; S_ = len(lab); NEG = -1e30
    a = np.full(S_, NEG); a[0] = lp[0, lab[0]]; a[1] = lp[0, lab[1]]
    skip = np.zeros(S_, bool); skip[3::2] = lab[3::2] != lab[1:-2:2]
    for t in range(1, T):
        s1 = np.concatenate([[NEG], a[:-1]]); s2 = np.concatenate([[NEG, NEG], a[:-2]]); s2[~skip] = NEG
        a = np.maximum(np.maximum(a, s1), s2) + lp[t, lab]
    return float(max(a[-1], a[-2]))
for t0, t1, cands in [(0.0, 2.6, ["참가자들은 열나흘 동안", "참가자들은 십사 일 동안"]),
                      (float(sys.argv[3]), float(sys.argv[4]), ["열나흘 뒤에는", "십사 일 뒤에는"])]:
    seg = x[int(t0 * SR):int(t1 * SR)]; seg = (seg - seg.mean()) / (seg.std() + 1e-7)
    with torch.inference_mode():
        lp = torch.log_softmax(model(torch.from_numpy(seg)[None]).logits[0], -1).numpy()
    print(f"{t0:.2f}-{t1:.2f}", [(c, round(score(lp, toks(c)), 1)) for c in cands])
    # 탐욕 해독(참고)
    ids = lp.argmax(-1); inv = {v: k for k, v in vocab.items()}; out = []; prev = -1
    for i in ids:
        if i != prev and i != BLANK: out.append(inv.get(int(i), '?'))
        prev = i
    print('   greedy:', ''.join(out).replace('|', ' '))
