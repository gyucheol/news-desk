"""Frame-by-frame pitch comparison: original time t vs stretched time t/speed (same speech moment)."""
import sys, numpy as np, soundfile as sf
from math import gcd
from scipy.signal import resample_poly, fftconvolve
def load16(p):
    x, sr = sf.read(p, dtype='float64', always_2d=True); x = x.mean(1); g = gcd(sr, 16000)
    return resample_poly(x, 16000 // g, sr // g) if sr != 16000 else x
def track(x, sr=16000, thr_db=-35):
    fl, hop, lmin, lmax = int(.04*sr), int(.005*sr), int(sr/400), int(sr/60)
    st = np.arange(0, len(x) - fl - lmax, hop); c2 = np.concatenate([[0], np.cumsum(x**2)])
    en = c2[st + fl] - c2[st]; thr = en.max() * 10**(thr_db/10); f0 = np.full(len(st), np.nan)
    for j, (i, e) in enumerate(zip(st, en)):
        if e < thr: continue
        r = fftconvolve(x[i:i+fl+lmax], x[i:i+fl][::-1], mode='valid')
        ew = c2[i + np.arange(lmax+1) + fl] - c2[i + np.arange(lmax+1)]
        nc = r / np.sqrt(e * ew + 1e-20); L = lmin + int(np.argmax(nc[lmin:lmax+1]))
        if nc[L] > 0.8 and 1 <= L - 1 and L + 1 <= lmax:            # parabolic refinement of the lag
            a, b, c = nc[L-1], nc[L], nc[L+1]; d = 0.5 * (a - c) / (a - 2*b + c + 1e-12)
            f0[j] = sr / (L + d)
    return (st + fl/2) / sr, f0
orig, out, speed = sys.argv[1], sys.argv[2], float(sys.argv[3])
to, fo = track(load16(orig)); tu, fu = track(load16(out))
idx = np.clip(np.round((tu * speed - to[0]) / (to[1] - to[0])).astype(int), 0, len(to) - 1)
ratio = fu / fo[idx]; ok = np.isfinite(ratio) & (ratio > 0.8) & (ratio < 1.25)       # drop octave errors
r = ratio[ok]; cents = 1200 * np.log2(r)
print(f"x{speed}: matched voiced frames {ok.sum()}, median pitch change {np.median(cents):+.1f} cents "
      f"({(2**(np.median(cents)/1200)-1)*100:+.2f}%), IQR {np.percentile(cents,25):+.1f}..{np.percentile(cents,75):+.1f} cents; "
      f"voiced-frame median f0: orig {np.nanmedian(fo):.1f} Hz, out {np.nanmedian(fu):.1f} Hz")
