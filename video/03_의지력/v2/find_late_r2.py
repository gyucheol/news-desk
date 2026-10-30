# 새 녹음 구간에서 자막 시작이 늦게 잡혔을 수 있는 줄 찾기: 줄 시작보다 0.12 s 넘게 앞에서 쉼(말소리 -30 dB 아래 120 ms 이상)이
# 끝나고, 그 뒤 줄 시작까지 목소리가 끊기지 않으며, 그 쉼이 앞 줄의 둘째 음절보다 뒤에 있으면 표시합니다.
# usage: find_late_r2.py audio.wav onsets.json units.json lines.json V_first V_last
import json, subprocess, sys
import numpy as np
SR, HOP = 16000, 0.01
x = np.frombuffer(subprocess.run(['ffmpeg', '-v', 'error', '-i', sys.argv[1], '-ac', '1', '-ar', str(SR), '-f', 's16le', '-'],
                                 capture_output=True, check=True).stdout, np.int16).astype(np.float32) / 32768
w = int(0.02 * SR)
db = 20 * np.log10(np.sqrt(np.convolve(x ** 2, np.ones(w) / w, mode='same')[::int(HOP * SR)] + 1e-12))
lvl = np.percentile(db, 95); quiet = db < lvl - 30
O = json.load(open(sys.argv[2])); U = json.load(open(sys.argv[3])); L = json.load(open(sys.argv[4]))
idx = {o['id']: i for i, o in enumerate(O)}
# pause ends: frame where a quiet run of >= 12 frames ends
ends = []
run = 0
for k, q in enumerate(quiet):
    if q:
        run += 1
    else:
        if run >= 12:
            ends.append(k * HOP)
        run = 0
ends = np.array(ends)
out = []
for i in range(idx[sys.argv[5]], idx[sys.argv[6]] + 1):
    s = O[i]['start']
    prev_syl = [t for _, t in U[i - 1]['syl']]
    lo = prev_syl[1] if len(prev_syl) > 1 else O[i - 1]['start']
    cand = ends[(ends > lo) & (ends < s - 0.12)]
    if not len(cand):
        continue
    p = cand.max()
    a, b = int(p / HOP), int(s / HOP)
    if quiet[a:b].sum() > 3:          # another quiet stretch between the pause and the start: not one voiced run
        continue
    out.append((O[i]['id'], round(p, 3), round(s, 3), round(s - p, 3), O[i].get('onset_v2'), L[i]['text'], [(c, round(t, 2)) for c, t in U[i - 1]['syl'][-3:]]))
for r in out:
    print(r)
print(len(out), 'flagged')
