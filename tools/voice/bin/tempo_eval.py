"""Compare a time-stretched file with its original: duration ratio, pitch (median f0), timbre (1/3-octave LTAS),
and optionally a round-trip file (stretched then un-stretched) via PESQ-WB / ESTOI after alignment."""
import sys, json, numpy as np, soundfile as sf
from math import gcd
from scipy.signal import resample_poly, welch, fftconvolve

def load16(p, max_s=None):
    x, sr = sf.read(p, dtype='float64', always_2d=True)
    x = x.mean(axis=1)
    if max_s: x = x[:int(max_s * sr)]
    g = gcd(sr, 16000)
    return resample_poly(x, 16000 // g, sr // g) if sr != 16000 else x

def f0_median(x, sr=16000):
    fl, hop, lmin, lmax = int(.04 * sr), int(.01 * sr), int(sr / 400), int(sr / 60)
    starts = np.arange(0, len(x) - fl - lmax, hop)
    en = np.array([np.dot(x[i:i + fl], x[i:i + fl]) for i in starts])
    thr = en.max() * 10 ** (-35 / 10)
    c2 = np.concatenate([[0], np.cumsum(x ** 2)])
    f0 = []
    for i, e in zip(starts, en):
        if e < thr: continue
        a, seg = x[i:i + fl], x[i:i + fl + lmax]
        r = fftconvolve(seg, a[::-1], mode='valid')          # r[L] = sum a[n] seg[n+L]
        ew = c2[i + np.arange(lmax + 1) + fl] - c2[i + np.arange(lmax + 1)]
        nccf = r / np.sqrt(e * ew + 1e-20)
        L = lmin + int(np.argmax(nccf[lmin:lmax + 1]))
        if nccf[L] > 0.7: f0.append(sr / L)
    return float(np.median(f0)), len(f0)

def ltas(x, sr=16000):
    f, p = welch(x, sr, nperseg=2048)
    centers = 1000 * 2 ** (np.arange(-10, 9) / 3)              # ~100 Hz .. ~6.3 kHz
    out = []
    for fc in centers:
        m = (f >= fc / 2 ** (1 / 6)) & (f < fc * 2 ** (1 / 6))
        out.append(p[m].sum())
    out = np.array(out); return 10 * np.log10(out / out.sum())

def align(ref, deg, max_lag=1600):
    n = min(len(ref), len(deg)); c = fftconvolve(deg[:n], ref[:n][::-1], mode='full')
    mid = n - 1; lag = int(np.argmax(c[mid - max_lag: mid + max_lag + 1])) - max_lag
    if lag > 0: deg = deg[lag:]
    elif lag < 0: ref = ref[-lag:]
    n = min(len(ref), len(deg)); return ref[:n], deg[:n], lag

orig, stretched = sys.argv[1], sys.argv[2]
rt = sys.argv[3] if len(sys.argv) > 3 else None
x, y = load16(orig, 60), load16(stretched, 50)
fx, nx = f0_median(x); fy, ny = f0_median(y)
dl = ltas(y) - ltas(x)
res = {"dur_ratio": sf.info(stretched).duration / sf.info(orig).duration,
       "f0_orig_Hz": round(fx, 1), "f0_stretched_Hz": round(fy, 1), "f0_change_pct": round(100 * (fy / fx - 1), 2),
       "ltas_mean_abs_dB": round(float(np.mean(np.abs(dl))), 2), "ltas_max_abs_dB": round(float(np.max(np.abs(dl))), 2)}
if rt:
    from pesq import pesq
    from pystoi import stoi
    r, d, lag = align(load16(orig), load16(rt))
    res.update({"roundtrip_lag_ms": round(lag / 16, 1), "roundtrip_PESQ_WB": round(float(pesq(16000, r, d, 'wb')), 2),
                "roundtrip_ESTOI": round(float(stoi(r, d, 16000, extended=True)), 3)})
print(json.dumps(res))
