"""Split-band de-esser: the 4.5-11 kHz band is turned down only while it is loud (sibilants).
y = rest + band * gain(t); rest = x - band (linear-phase FIR, so the split is exact).
Usage: deess.py IN.wav OUT.wav [threshold_dB_rel_speech] [ratio] [max_reduction_dB]"""
import sys, numpy as np, soundfile as sf
from scipy.signal import firwin, oaconvolve
from scipy.ndimage import uniform_filter1d
src, dst = sys.argv[1], sys.argv[2]
thr = float(sys.argv[3]) if len(sys.argv) > 3 else -18.0
ratio = float(sys.argv[4]) if len(sys.argv) > 4 else 3.0
maxred = float(sys.argv[5]) if len(sys.argv) > 5 else 8.0
x, sr = sf.read(src, dtype='float64'); mono = x.ndim == 1; x = x if mono else x.mean(1)
h = firwin(401, [4500, 11000], pass_zero=False, fs=sr, window=('kaiser', 8.0))
band = oaconvolve(x, h, mode='same'); rest = x - band
w = int(.02*sr); n = len(x)//w; fr = 20*np.log10(np.sqrt((x[:n*w].reshape(n, w)**2).mean(1)) + 1e-12)
speech_db = 10*np.log10(np.mean(10**(fr[fr > np.percentile(fr, 90) - 25]/10)))      # level of speech frames
env_db = 10*np.log10(uniform_filter1d(band**2, int(.005*sr)) + 1e-20) - speech_db
gr = np.clip((env_db - thr) * (1 - 1/ratio), 0, maxred)
la = int(.002*sr); gr = np.concatenate([gr[la:], np.zeros(la)])                       # 2 ms look-ahead
aa, ar = 1 - np.exp(-1/(.001*sr)), 1 - np.exp(-1/(.060*sr)); s = 0.0; sm = np.empty_like(gr)
for i, g in enumerate(gr):
    s += (g - s) * (aa if g > s else ar); sm[i] = s
y = rest + band * 10**(-sm/20)
sf.write(dst, y.astype(np.float32), sr, subtype='FLOAT')
act = sm > 0.5
print(f"{dst.split('/')[-1]}: thr {thr} dB, ratio {ratio}, max {maxred} dB | reduced >0.5 dB in {act.mean()*100:.1f}% of time, "
      f"max {sm.max():.1f} dB")
