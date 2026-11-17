import sys, json, subprocess
import numpy as np
SR, N, H = 48000, 4096, 1200
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', sys.argv[1], '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).astype(np.float64)
nfr = (len(x) - N) // H; w = np.hanning(N); F = np.fft.rfftfreq(N, 1 / SR)
P = np.empty((nfr, len(F)))
for i in range(nfr): P[i] = np.abs(np.fft.rfft(x[i * H:i * H + N] * w)) ** 2
t = (np.arange(nfr) * H + N / 2) / SR
B = lambda lo, hi: 10 * np.log10(P[:, (F >= lo) & (F < hi)].sum(1) + 1e-12)
tot = B(100, 4000); sp = tot > np.percentile(tot, 10) + 25
air = B(8500, 15000) - B(2000, 7000)
O = json.load(open('../v1/onsets_v2_full.json'))
r = []
for i, o in enumerate(O):
    a = o['start']; b = min(O[i + 1]['start'] if i + 1 < len(O) else o['end'] + 0.3, o['end'] + 0.3)
    m = sp & (t >= a) & (t < b)
    if m.sum() >= 8: r.append((a, np.median(air[m])))
r = np.array(r)
sm = np.array([np.median(r[max(0, i - 6):i + 7, 1]) for i in range(len(r))])
print('air per line std %.2f, smoothed std %.2f, p10/p50/p90 %s' % (r[:, 1].std(), sm.std(), np.percentile(r[:, 1], [10, 50, 90]).round(1)))
for name, a, b in [('part1', 0, 210.6), ('part2', 210.7, 434.2), ('part3', 434.3, 700)]:
    m = (r[:, 0] >= a) & (r[:, 0] < b); print(' ', name, 'air median %.1f' % np.median(r[m, 1]))
