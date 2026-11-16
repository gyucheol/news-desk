# 녹음의 여러 구간을 음절 모델(w2v_ko)로 다시 듣기(04편 ctc_check.py를 한 번에 여러 구간으로).
#  greedy: 모델이 그대로 받아 적은 음절 / 후보 점수: 프레임당 평균 log 확률(클수록 그 문장에 가까움)
# usage: ctc_check_batch.py checks.json   ([{"audio", "t0", "t1", "cands": [...]}, ...])
import json, re, subprocess, sys
import numpy as np
import torch
from transformers import Wav2Vec2ForCTC
MD = "/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/models/w2v_ko"
SR = 16000
vocab = json.load(open(f"{MD}/vocab.json")); inv = {v: k for k, v in vocab.items()}
BLANK, SEP = vocab["[PAD]"], vocab["|"]
torch.set_num_threads(4)
model = Wav2Vec2ForCTC.from_pretrained(MD).eval()
for ck in json.load(open(sys.argv[1], encoding="utf-8")):
    x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-ss", str(ck["t0"]), "-to", str(ck["t1"]), "-i", ck["audio"], "-ac", "1",
                                      "-ar", str(SR), "-f", "s16le", "-"], capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
    seg = (x - x.mean()) / (x.std() + 1e-7)
    with torch.inference_mode():
        lp = torch.log_softmax(model(torch.from_numpy(seg)[None]).logits[0], -1).numpy()
    ids = lp.argmax(1); out, prev = [], None
    for i in ids:
        if i != prev and i != BLANK:
            out.append(" " if i == SEP else inv.get(int(i), "?"))
        prev = i
    print(f"== {ck['audio'].split('/')[-1]} {ck['t0']}-{ck['t1']}")
    print("greedy:", re.sub(r"\s+", " ", "".join(out)).strip())
    def score(text):
        y = []
        for w in re.findall(r"[가-힣]+", text):
            if y: y.append(SEP)
            y += [vocab.get(c, vocab["[UNK]"]) for c in w]
        T, L = lp.shape[0], len(y)
        lab = np.full(2 * L + 1, BLANK); lab[1::2] = y
        S = len(lab); NEG = -1e30
        a = np.full(S, NEG); a[0] = lp[0, lab[0]]; a[1] = lp[0, lab[1]]
        skip = np.zeros(S, bool); skip[3::2] = lab[3::2] != lab[1:-2:2]
        for t in range(1, T):
            s1 = np.concatenate([[NEG], a[:-1]]); s2 = np.concatenate([[NEG, NEG], a[:-2]]); s2[~skip] = NEG
            a = np.maximum(np.maximum(a, s1), s2) + lp[t, lab]
        return max(a[S - 1], a[S - 2]) / T
    for c in ck.get("cands", []):
        print(f"{score(c):8.4f}  {c}")
