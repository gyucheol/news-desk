# 목소리 음색 평준화(04편 v3, 2026-11-03). 사용자: "중간중간 소리가 먹어들어가는 소리가 한번씩 있네. 음질이 깔끔해졌다가
# 약간 먹먹하다가 그런 부분이 있어. 찾아내서 평준화 시켜줘."
# 원인: 녹음 앱의 잡음 제거 처리로 구간마다 고음(2~7kHz)과 저음 쪽 비율이 달라짐(말 사이는 완전 무음, 7kHz 위는 거의 없음).
# 방법: 유성음(모음) 프레임만 골라 1/3옥타브 대역의 '모양'(전체 크기를 뺀 대역별 dB)을 재고, 앞뒤 1.5초(창 3초)의 평균 모양이
# 녹음 전체의 중앙값 모양과 다른 만큼 반대로 보정(α배, 대역마다 ±MAX dB까지). 보정 값은 시간과 주파수 방향으로 부드럽게.
# 7.5kHz 위는 올리지 않음(잡음만 커지므로). 8.5kHz 위 잡음 성분은 많은 곳만 줄여 고르게. 기준 모양은 녹음 전체의 중앙값(전체 밝기는 그대로).
# 크기 전체는 바꾸지 않음(뒤에서 prep_audio.py가 -14 LUFS로 맞춤).
# 보정 한계: 500Hz 아래는 -4~+3 dB, 그 위는 -4~+max_db dB.
# usage: eq_level.py in.wav out.wav report.json [alpha=0.8] [max_db=6] [half_window_s=1.5]
import sys, json, subprocess
import numpy as np
from scipy.ndimage import uniform_filter1d, gaussian_filter1d
src, out, rep = sys.argv[1:4]
ALPHA = float(sys.argv[4]) if len(sys.argv) > 4 else 0.8
MAXDB = float(sys.argv[5]) if len(sys.argv) > 5 else 6.0
HW = float(sys.argv[6]) if len(sys.argv) > 6 else 1.5
SR, N, H = 48000, 2048, 512
raw = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
x = np.frombuffer(raw, np.float32).astype(np.float64)
L = len(x)
pad = N
xp = np.concatenate([np.zeros(pad), x, np.zeros(pad + N)])
nfr = (len(xp) - N) // H + 1
win = np.sqrt(np.hanning(N + 1)[:N])          # sqrt-Hann analysis and synthesis (overlap 75% -> constant sum after normalisation)
F = np.fft.rfftfreq(N, 1 / SR)
X = np.empty((nfr, len(F)), np.complex64)
for a in range(0, nfr, 2000):
    b = min(nfr, a + 2000)
    idx = np.arange(N)[None, :] + H * np.arange(a, b)[:, None]
    X[a:b] = np.fft.rfft(xp[idx] * win, axis=1)
P = np.abs(X).astype(np.float64) ** 2
tfr = (np.arange(nfr) * H + N / 2 - pad) / SR
# bands (1/3 octave, 100 Hz .. 8 kHz)
cents = 1000 * 2 ** (np.arange(-10, 10) / 3)
cents = cents[(cents >= 100) & (cents <= 8000)]
edges = np.sqrt(cents[:-1] * cents[1:])
edges = np.concatenate([[cents[0] / 2 ** (1 / 6)], edges, [cents[-1] * 2 ** (1 / 6)]])
BL = np.stack([10 * np.log10(P[:, (F >= lo) & (F < hi)].sum(1) + 1e-12) for lo, hi in zip(edges[:-1], edges[1:])], 1)
# voiced frames: speech level + harmonicity from normalised autocorrelation at 8 kHz
lev = 10 * np.log10(P[:, (F >= 100) & (F < 4000)].sum(1) + 1e-12)
speech = lev > np.percentile(lev, 15) + 25
dec = 6
y8 = subprocess.run(['ffmpeg', '-v', 'error', '-i', src, '-ac', '1', '-ar', '8000', '-f', 'f32le', '-'], capture_output=True, check=True).stdout
y8 = np.frombuffer(y8, np.float32).astype(np.float64)
y8p = np.concatenate([np.zeros(pad // dec), y8, np.zeros(pad // dec + N)])
M = N // dec
harm = np.zeros(nfr)
for i in np.nonzero(speech)[0]:
    s = y8p[i * H // dec: i * H // dec + M]
    s = s - s.mean()
    e = np.dot(s, s)
    if e <= 0:
        continue
    r = np.correlate(s, s, 'full')[M - 1:]
    seg = r[20:115] / e
    harm[i] = seg.max()
voiced = speech & (harm > 0.5)
ref_lo, ref_hi = (cents >= 300) & (cents <= 3000), None
shape = BL - BL[:, ref_lo].mean(1, keepdims=True)
R = np.median(shape[voiced], 0)
# local mean shape over +-HW s of voiced frames
hw = int(round(HW * SR / H))
vs = np.where(voiced[:, None], shape, 0.0)
cnt = uniform_filter1d(voiced.astype(float), 2 * hw + 1, mode='nearest') * (2 * hw + 1)
sm = uniform_filter1d(vs, 2 * hw + 1, axis=0, mode='nearest') * (2 * hw + 1)
ok = cnt >= 25
loc = np.where(ok[:, None], sm / np.maximum(cnt, 1)[:, None], np.nan)
# hold last valid value through pauses
last = np.zeros(len(cents))
for i in range(nfr):
    if ok[i]:
        last = loc[i]
    else:
        loc[i] = last
D = loc - R
G = -ALPHA * D
lowB = cents < 500
G[:, lowB] = np.clip(G[:, lowB], -4.0, 3.0)                      # 저음은 덜 올림(웅웅거림 방지)
G[:, ~lowB] = np.clip(G[:, ~lowB], -4.0, MAXDB)
G = uniform_filter1d(G, 3, axis=1, mode='nearest')            # neighbouring bands
G = gaussian_filter1d(G, sigma=0.15 * SR / H, axis=0)          # about 0.15 s in time
G = G - G[:, ref_lo].mean(1, keepdims=True)                     # keep the 300-3000 Hz level as it is
# 8.5kHz 위('바람' 같은 잡음 성분): 구간마다 양이 달라 맑았다 먹먹했다 들리는 원인 중 하나. 많은 곳만 30번째 백분위까지 줄임.
Aair = 10 * np.log10(P[:, (F >= 8500) & (F < 15000)].sum(1) + 1e-12) - 10 * np.log10(P[:, (F >= 2000) & (F < 7000)].sum(1) + 1e-12)
va = np.where(voiced, Aair, 0.0)
aloc = uniform_filter1d(va, 2 * hw + 1, mode='nearest') * (2 * hw + 1) / np.maximum(cnt, 1)
aloc = np.where(ok, aloc, np.nan)
lasta = np.nanmedian(aloc)
for i in range(nfr):
    if np.isnan(aloc[i]):
        aloc[i] = lasta
    else:
        lasta = aloc[i]
AIR_T = float(np.percentile(aloc[ok], 30))
gair = np.clip(AIR_T - aloc, -8.0, 0.0)
gair = gaussian_filter1d(gair, sigma=0.15 * SR / H)
# gain per FFT bin: interpolate in log-frequency between band centres; below 100 Hz follow the lowest band towards 0;
# above 7.5 kHz never boost
lf = np.log2(np.maximum(F, 1.0))
lc = np.log2(cents)
Gbin = np.empty((nfr, len(F)))
for i in range(nfr):
    g = np.interp(lf, lc, G[i])
    Gbin[i] = g
Gbin[:, F < 60] = 0.0
hi = F > 7500
Gbin[:, hi] = np.minimum(Gbin[:, hi], 0.0)
ramp = np.clip((F - 7500) / 1000, 0, 1)
Gbin += gair[:, None] * ramp[None, :]
Y = X * (10 ** (Gbin / 20)).astype(np.float32)
# overlap-add
y = np.zeros(len(xp))
wsum = np.zeros(len(xp))
for a in range(0, nfr, 2000):
    b = min(nfr, a + 2000)
    fr = np.fft.irfft(Y[a:b], n=N, axis=1) * win
    for k, i in enumerate(range(a, b)):
        y[i * H:i * H + N] += fr[k]
        wsum[i * H:i * H + N] += win ** 2
y = y / np.maximum(wsum, 1e-8)
y = y[pad:pad + L]
subprocess.run(['ffmpeg', '-v', 'error', '-y', '-f', 'f32le', '-ar', str(SR), '-ac', '1', '-i', '-', '-c:a', 'pcm_f32le', out],
               input=y.astype(np.float32).tobytes(), check=True)
# report: per 0.5 s, mean deviation (before correction) in 2-7 kHz and 150-500 Hz, and the applied gain there
hiB = (cents >= 2000) & (cents <= 7000)
loB = (cents >= 150) & (cents <= 500)
step = int(0.5 * SR / H)
reprows = []
for i in range(0, nfr, step):
    if tfr[i] < 0 or tfr[i] > L / SR:
        continue
    reprows.append([round(float(tfr[i]), 2), round(float(np.nanmean(D[i, hiB])), 2), round(float(np.nanmean(D[i, loB])), 2),
                    round(float(G[i, hiB].mean()), 2), round(float(G[i, loB].mean()), 2), bool(ok[i])])
json.dump({'alpha': ALPHA, 'max_db': MAXDB, 'half_window_s': HW, 'bands_hz': [round(float(c)) for c in cents],
           'ref_shape_db': [round(float(v), 2) for v in R], 'voiced_frames': int(voiced.sum()), 'frames': int(nfr),
           'rows_t_devHF_devLF_gainHF_gainLF_ok': reprows}, open(rep, 'w'))
print('air target %.1f dB, air cut up to %.1f dB |' % (AIR_T, gair.min()), 'voiced frames', int(voiced.sum()), 'of', nfr, '| gain range HF %.1f..%.1f dB, LF %.1f..%.1f dB' % (
    G[:, hiB].mean(1).min(), G[:, hiB].mean(1).max(), G[:, loB].mean(1).min(), G[:, loB].mean(1).max()))
