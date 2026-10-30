"""Measure simple features of each candidate track (first 75 s): loudness envelope, build-up, pulse/tempo,
brightness, percussive share, minor/major guess. Usage: feat.py mp3dir ids..."""
import json, subprocess, sys
import numpy as np
from scipy import ndimage, signal
SR = 22050
def load(p, dur=75.0):
    r = subprocess.run(['ffmpeg', '-v', 'error', '-i', p, '-t', str(dur), '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True)
    return np.frombuffer(r.stdout, dtype=np.float32).astype(np.float64)
MAJ = np.array([6.35, 2.23, 3.48, 2.33, 4.38, 4.09, 2.52, 5.19, 2.39, 3.66, 2.29, 2.88])
MIN = np.array([6.33, 2.68, 3.52, 5.38, 2.60, 3.53, 2.54, 4.75, 3.98, 2.69, 3.34, 3.17])
NAMES = 'C C# D D# E F F# G G# A A# B'.split()
out = {}
for i in sys.argv[2:]:
    x = load(f'{sys.argv[1]}/{i}.mp3')
    n, h = 2048, 512
    f, t, Z = signal.stft(x, SR, nperseg=n, noverlap=n - h, boundary=None)
    M = np.abs(Z)
    # loudness envelope (dBFS RMS per 2 s)
    blk = SR * 2
    rms = [20 * np.log10(np.sqrt(np.mean(x[k:k + blk] ** 2)) + 1e-9) for k in range(0, len(x) - blk + 1, blk)]
    rms = np.array(rms)
    # HPSS-ish: median filter across time (harmonic) and frequency (percussive)
    Hm = ndimage.median_filter(M, size=(1, 17)); Pm = ndimage.median_filter(M, size=(17, 1))
    perc_share = float(np.sum(Pm ** 2 * (Pm > Hm)) / (np.sum(M ** 2) + 1e-12))
    # onset envelope and tempo via autocorrelation
    S_db = 20 * np.log10(M + 1e-9)
    flux = np.maximum(0, np.diff(S_db, axis=1)).mean(axis=0)
    flux = flux - ndimage.uniform_filter1d(flux, 40)
    flux = np.maximum(flux, 0)
    fps = SR / h
    ac = np.correlate(flux - flux.mean(), flux - flux.mean(), 'full')[len(flux) - 1:]
    ac /= ac[0] + 1e-12
    lo, hi = int(fps * 60 / 180), int(fps * 60 / 50)
    k = lo + int(np.argmax(ac[lo:hi]))
    tempo, pulse = 60 * fps / k, float(ac[k])
    onset_rate = float(np.sum(flux > flux.mean() + 2 * flux.std()) / (len(x) / SR))
    cent = float(np.sum(f[:, None] * M, axis=0).sum() / (M.sum() + 1e-12))
    low = float((M[f < 150] ** 2).sum() / ((M ** 2).sum() + 1e-12))
    # chroma -> key
    chroma = np.zeros(12)
    for b, fr in enumerate(f):
        if 55 <= fr <= 2000:
            chroma[int(round(12 * np.log2(fr / 440.0))) % 12 if fr > 0 else 0] += (M[b] ** 2).sum()
    chroma = np.roll(chroma, -3)  # index 0 = A -> shift so 0 = C
    chroma = np.roll(chroma, 0)
    best = max([(np.corrcoef(np.roll(MAJ, s), chroma)[0, 1], NAMES[s] + ' major') for s in range(12)] +
               [(np.corrcoef(np.roll(MIN, s), chroma)[0, 1], NAMES[s] + ' minor') for s in range(12)])
    first10 = float(np.mean(rms[:5])); mid = float(np.mean(rms[10:20])) if len(rms) > 20 else float(np.mean(rms[5:]))
    out[i] = {'rms_first10': round(first10, 1), 'rms_20_40': round(mid, 1), 'build_dB': round(mid - first10, 1),
              'rms_range': round(float(np.percentile(rms, 95) - np.percentile(rms, 5)), 1),
              'tempo': round(tempo, 1), 'pulse': round(pulse, 2), 'onsets_per_s': round(onset_rate, 2),
              'centroid_hz': round(cent), 'low_share': round(low, 2), 'perc_share': round(perc_share, 2),
              'key': best[1], 'key_r': round(float(best[0]), 2),
              'env': [round(v) for v in rms]}
    print(i, {k: v for k, v in out[i].items() if k != 'env'})
    print('   env(2s):', out[i]['env'])
json.dump(out, open('feat.json', 'w'), indent=1)
