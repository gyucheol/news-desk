# 녹음 음색 추적: 말소리 프레임마다 대역 크기(dB)를 재고, 1초 창의 중앙값으로 '고음/중음' 비율이 어떻게 변하는지 봄.
# usage: spec_track.py in.wav out_prefix
import sys, json, subprocess
import numpy as np
from PIL import Image, ImageDraw
src, outp = sys.argv[1], sys.argv[2]
SR = 48000
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).astype(np.float64)
N, H = 2048, 480
win = np.hanning(N)
nfr = (len(x) - N) // H
idx = np.arange(N)[None, :] + H * np.arange(nfr)[:, None]
F = np.fft.rfftfreq(N, 1 / SR)
P = np.empty((nfr, len(F)), np.float32)
for a in range(0, nfr, 4000):
    b = min(nfr, a + 4000)
    P[a:b] = (np.abs(np.fft.rfft(x[idx[a:b]] * win, axis=1)) ** 2).astype(np.float32)
t = (np.arange(nfr) * H + N / 2) / SR
tot = 10 * np.log10(P[:, (F >= 100) & (F < 8000)].sum(1) + 1e-12)
floor = np.percentile(tot, 10)
speech = tot > floor + 25
bands = {'b1': (150, 500), 'b2': (500, 2000), 'b3': (2000, 4000), 'b4': (4000, 8000), 'b5': (8000, 12000), 'b6': (12000, 16000), 'b7': (16000, 20000)}
B = {k: 10 * np.log10(P[:, (F >= lo) & (F < hi)].sum(1) + 1e-12) for k, (lo, hi) in bands.items()}
rel = {k: B[k] - B['b2'] for k in bands if k != 'b2'}
# 99% rolloff
cs = np.cumsum(P[:, F >= 50], axis=1)
F50 = F[F >= 50]
roll = F50[np.argmax(cs >= 0.99 * cs[:, -1:], axis=1)]
step = 0.25
T = np.arange(0.5, t[-1] - 0.5, step)
ser = {k: np.full(len(T), np.nan) for k in list(rel) + ['roll', 'lev']}
for i, tc in enumerate(T):
    m = speech & (np.abs(t - tc) <= 0.5)
    if m.sum() < 30:
        continue
    for k in rel:
        ser[k][i] = np.median(rel[k][m])
    ser['roll'][i] = np.median(roll[m])
    ser['lev'][i] = np.median(tot[m])
glob = {k: float(np.nanmedian(v)) for k, v in ser.items()}
print('speech frames', int(speech.sum()), 'of', nfr, '| floor', round(floor, 1))
print('global medians', {k: round(v, 1) for k, v in glob.items()})
json.dump({'T': T.tolist(), **{k: [None if np.isnan(v) else round(float(v), 2) for v in s] for k, s in ser.items()}, 'glob': glob}, open(outp + '_series.json', 'w'))
# plot: 4 rows
rows, W, Hh = 4, 1800, 260
per = (T[-1] + 1) / rows
img = Image.new('RGB', (W + 60, rows * (Hh + 30)), 'white')
d = ImageDraw.Draw(img)
cols = {'b3': (0, 150, 0), 'b4': (220, 0, 0), 'b5': (0, 0, 220), 'b6': (150, 0, 150), 'roll': (255, 140, 0)}
for r in range(rows):
    y0 = r * (Hh + 30) + 20
    t0 = r * per
    d.rectangle((50, y0, 50 + W, y0 + Hh), outline=(180, 180, 180))
    for s in range(int(t0) // 10 * 10, int(t0 + per) + 1, 10):
        if s < t0: continue
        X = 50 + (s - t0) / per * W
        d.line((X, y0, X, y0 + Hh), fill=(235, 235, 235))
        d.text((X - 8, y0 + Hh + 2), f'{s // 60}:{s % 60:02d}', fill='black')
    for k, c in cols.items():
        v = ser[k]
        dev = (v - glob[k]) if k != 'roll' else (v - glob[k]) / 1000.0 * 2   # rolloff: 1 kHz = 2 dB scale
        pts = []
        for i, tc in enumerate(T):
            if tc < t0 or tc >= t0 + per:
                continue
            if np.isnan(dev[i]):
                if len(pts) > 1: d.line(pts, fill=c, width=1)
                pts = []
                continue
            X = 50 + (tc - t0) / per * W
            Y = y0 + Hh / 2 - np.clip(dev[i], -12, 12) / 12 * (Hh / 2)
            pts.append((X, Y))
        if len(pts) > 1: d.line(pts, fill=c, width=1)
    for db in (-6, 0, 6):
        Y = y0 + Hh / 2 - db / 12 * (Hh / 2)
        d.text((5, Y - 5), f'{db:+d}dB', fill='black')
        d.line((50, Y, 50 + W, Y), fill=(200, 200, 200) if db else (120, 120, 120))
d.text((60, 2), 'deviation from median: green 2-4k, red 4-8k, blue 8-12k, purple 12-16k (rel. to 0.5-2k), orange rolloff99 (1kHz=2dB)', fill='black')
img.save(outp + '_plot.png')
