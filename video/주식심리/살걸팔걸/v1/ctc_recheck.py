# 자막 줄 시작을 음절 모델로 다시 확인(살걸·팔걸 편, 2026-11-06).
# onsets.py는 '첫 낱말 끝까지의 가장 긴 쉼' 뒤를 시작으로 잡아서, 첫 낱말 뒤에 쉼이 있으면('2016년, 프리드먼과')
# 첫 낱말을 건너뛰고 늦게 잡음. 앞 줄과 이 줄을 이어 한 구간에서 음절 맞춤(Viterbi, 구간 제약 없음)을 하고,
# 이 줄 첫 음절의 시각과 지금 시작이 0.15초 넘게 다르면 보고함.
# usage: ctc_recheck.py lines.json onsets_v2.json rec.wav out.json [ID ...]
import json, re, subprocess, sys
import numpy as np
import torch
from transformers import Wav2Vec2ForCTC
MD = "/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/models/w2v_ko"
SR, FR = 16000, 0.02
L = json.load(open(sys.argv[1], encoding="utf-8")); O = {o['id']: o for o in json.load(open(sys.argv[2], encoding="utf-8"))}
audio, outp = sys.argv[3], sys.argv[4]
ids = sys.argv[5:] or [l['id'] for l in L]
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", audio, "-ac", "1", "-ar", str(SR), "-f", "s16le", "-"],
                                 capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
vocab = json.load(open(f"{MD}/vocab.json")); BLANK, UNK, SEP = vocab["[PAD]"], vocab["[UNK]"], vocab["|"]
torch.set_num_threads(4)
model = Wav2Vec2ForCTC.from_pretrained(MD).eval()
idx = {l['id']: i for i, l in enumerate(L)}
def toks(text):
    out = []
    for w in re.findall(r"[가-힣]+", text):
        if out: out.append(SEP)
        out += [vocab.get(c, UNK) for c in w]
    return out
def viterbi(lp, y):
    lab = np.full(2 * len(y) + 1, BLANK); lab[1::2] = y; S = len(lab); T = lp.shape[0]; NEG = -1e30
    a = np.full(S, NEG); a[0] = lp[0, lab[0]]; a[1] = lp[0, lab[1]]
    skip = np.zeros(S, bool); skip[3::2] = lab[3::2] != lab[1:-2:2]
    bp = np.zeros((T, S), np.int8)
    for t in range(1, T):
        c0 = a; c1 = np.concatenate([[NEG], a[:-1]]); c2 = np.concatenate([[NEG, NEG], a[:-2]]); c2[~skip] = NEG
        st = np.stack([c0, c1, c2]); b = st.argmax(0); a = st.max(0) + lp[t, lab]; bp[t] = b
    s = S - 1 if a[S - 1] >= a[S - 2] else S - 2
    path = [s]
    for t in range(T - 1, 0, -1):
        s = s - bp[t, s]; path.append(s)
    path = path[::-1]
    first = {}
    for t, s in enumerate(path):
        if s % 2 == 1 and (s // 2) not in first: first[s // 2] = t
    return first
res = []
for vid in ids:
    k = idx[vid]
    if k == 0: continue
    prev, cur = L[k - 1], L[k]
    t0 = max(O[prev['id']]['start'] - 0.25, 0); nxt = O[L[k + 1]['id']]['start'] if k + 1 < len(L) else O[cur['id']]['start'] + 3
    t1 = nxt + 0.1
    seg = x[int(t0 * SR):int(t1 * SR)]; seg = (seg - seg.mean()) / (seg.std() + 1e-7)
    with torch.inference_mode():
        lp = torch.log_softmax(model(torch.from_numpy(seg)[None]).logits[0], -1).numpy()
    yp, yc = toks(prev['say']), toks(cur['say'])
    y = yp + [SEP] + yc
    first = viterbi(lp, y)
    j = len(yp) + 1                      # first token of the current line
    tc = t0 + first.get(j, 0) * FR
    cur_s = O[cur['id']]['start']
    res.append({'id': cur['id'], 'start': cur_s, 'ctc_first': round(tc, 3), 'diff': round(cur_s - tc, 3), 'say': cur['say']})
    if abs(cur_s - tc) > 0.15:
        print(f"{cur['id']} now {cur_s:7.2f} ctc {tc:7.2f} diff {cur_s - tc:+.2f} | {cur['say']}", flush=True)
json.dump(res, open(outp, 'w'), ensure_ascii=False, indent=1)
print('checked', len(res))
