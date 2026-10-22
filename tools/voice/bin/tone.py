"""Tonal balance of speech: octave bands vs the 500-2000 Hz average, plus sibilance (5-10 kHz level in the
most 's'-like 3% of speech frames, relative to the average speech-frame level)."""
import sys, numpy as np, soundfile as sf
from scipy.signal import welch, stft
def analyse(p):
    x, sr = sf.read(p); x = x if x.ndim == 1 else x.mean(1)
    w = int(0.02*sr); n = len(x)//w; fr = x[:n*w].reshape(n, w)
    rms = 20*np.log10(np.sqrt((fr**2).mean(1)) + 1e-12); act = rms > np.percentile(rms, 90) - 25
    f, P = welch(fr[act].ravel(), sr, nperseg=8192)
    cs = [63, 125, 250, 500, 1000, 2000, 4000, 8000, 12500]; b = {}
    for c in cs:
        m = (f >= c/2**0.5) & (f < min(c*2**0.5, sr/2)); b[c] = 10*np.log10(P[m].mean() + 1e-30)
    ref = np.mean([b[500], b[1000], b[2000]]); b = {c: b[c]-ref for c in cs}
    F, _, Z = stft(x[:n*w], sr, nperseg=w, noverlap=0, boundary=None, padded=False); E = np.abs(Z)**2
    E = E[:, :n]; hf = E[(F >= 5000) & (F < 10000)].sum(0); lf = E[(F >= 300) & (F < 3000)].sum(0); tot = E.sum(0)
    a = act[:E.shape[1]]; ratio = hf[a] / (lf[a] + 1e-20)
    top = ratio >= np.percentile(ratio, 97)
    sib = 10*np.log10(hf[a][top].mean() / tot[a].mean())
    return b, sib
names = sys.argv[1:]
rows = [(p.split('/')[-1].replace('.wav',''), *analyse(p)) for p in names]
cs = list(rows[0][1].keys())
print(f"{'file':<22}" + "".join(f"{c:>7}" for c in cs) + "   sibilance")
for name, b, sib in rows:
    print(f"{name:<22}" + "".join(f"{b[c]:>+7.1f}" for c in cs) + f"   {sib:+6.1f} dB")
