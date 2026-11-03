# 자막 줄마다(말소리 프레임) 대역 비율: t1 = 2-4k, t2 = 4-7k, t3 = 150-500 (모두 0.5-2k 대비 dB). usage: line_tilt.py in.wav
import sys, json, subprocess
import numpy as np
SR, N, H = 48000, 4096, 1200
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', sys.argv[1], '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).astype(np.float64)
nfr = (len(x) - N) // H
w = np.hanning(N)
F = np.fft.rfftfreq(N, 1 / SR)
P = np.empty((nfr, len(F)))
for i in range(nfr):
    P[i] = np.abs(np.fft.rfft(x[i * H:i * H + N] * w)) ** 2
t = (np.arange(nfr) * H + N / 2) / SR
tot = 10 * np.log10(P[:, (F >= 100) & (F < 4000)].sum(1) + 1e-12)
sp = tot > np.percentile(tot, 10) + 25
O = json.load(open('../v1/onsets_v2_full.json'))
res = []
for i, o in enumerate(O):
    a = o['start']; b = min(O[i + 1]['start'] if i + 1 < len(O) else o['end'] + 0.3, o['end'] + 0.3)
    m = sp & (t >= a) & (t < b)
    if m.sum() < 8:
        continue
    S_ = P[m].mean(0)
    L = lambda lo, hi: 10 * np.log10(S_[(F >= lo) & (F < hi)].sum() + 1e-12)
    ref = L(500, 2000)
    res.append((a, L(2000, 4000) - ref, L(4000, 7000) - ref, L(150, 500) - ref))
r = np.array(res)
def runstd(v, k=6):
    d = [v[i] - np.median(v[max(0, i - k):i + k + 1]) for i in range(len(v))]
    return np.std(d)
print('lines', len(r), '| std t1 %.2f t2 %.2f t3 %.2f' % tuple(r[:, 1:].std(0)), '| smoothed (13-line median) std t1 %.2f t2 %.2f t3 %.2f' % tuple(
    np.std([np.median(r[max(0, i - 6):i + 7, c]) for i in range(len(r))]) for c in (1, 2, 3)))
for name, a, b in [('part1', 0, 210.6), ('part2', 210.7, 434.2), ('part3', 434.3, 700)]:
    m = (r[:, 0] >= a) & (r[:, 0] < b)
    print(' ', name, 'median t1 %.1f t2 %.1f t3 %.1f' % tuple(np.median(r[m, 1:], 0)))
