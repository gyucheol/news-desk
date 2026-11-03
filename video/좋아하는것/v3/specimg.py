# 구간 스펙트로그램 그림(0~12kHz). usage: specimg.py in.wav out.png t0 t1 [t0 t1 ...]
import sys, subprocess
import numpy as np
from PIL import Image, ImageDraw
src, out = sys.argv[1], sys.argv[2]
spans = [(float(a), float(b)) for a, b in zip(sys.argv[3::2], sys.argv[4::2])]
SR = 48000
tiles = []
for a, b in spans:
    raw = subprocess.run(['ffmpeg', '-v', 'error', '-ss', str(a), '-t', str(b - a), '-i', src, '-ac', '1', '-ar', str(SR), '-f', 'f32le', '-'], capture_output=True, check=True).stdout
    x = np.frombuffer(raw, np.float32).astype(np.float64)
    N, H = 1024, 240
    w = np.hanning(N)
    nfr = (len(x) - N) // H
    S = np.array([np.abs(np.fft.rfft(x[i * H:i * H + N] * w)) for i in range(nfr)]).T
    F = np.fft.rfftfreq(N, 1 / SR)
    S = S[F <= 12000]
    D = 20 * np.log10(S + 1e-9)
    top = np.percentile(D, 99.5)
    D = np.clip((D - (top - 80)) / 80, 0, 1)
    img = Image.fromarray((255 * (1 - D[::-1])).astype(np.uint8)).resize((1700, 256))
    img = img.convert('RGB')
    dr = ImageDraw.Draw(img)
    for k in range(0, 12001, 2000):
        y = 256 - k / 12000 * 256
        dr.line((0, y, 12, y), fill=(255, 0, 0)); dr.text((14, y - 10 if k else y - 12), f'{k // 1000}k', fill=(255, 0, 0))
    dur = b - a
    for s in np.arange(np.ceil(a), b, 1.0):
        X = (s - a) / dur * 1700
        dr.line((X, 250, X, 256), fill=(0, 0, 255)); dr.text((X + 2, 240), f'{int(s // 60)}:{s % 60:04.1f}', fill=(0, 0, 255))
    tiles.append(img)
canvas = Image.new('RGB', (1700, len(tiles) * 262), 'white')
for i, t in enumerate(tiles):
    canvas.paste(t, (0, i * 262))
canvas.save(out)
