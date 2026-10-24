# Paint out a small moving logo (e.g. the mark on the back of a phone) in a section of a stock clip (F의 연애 01, 2026-10-24).
# The logo is tracked by template matching from a starting point you give, and a disc around it is filled from the pixels
# around it (normalized convolution), so the surface looks plain instead of blurred. Writes the patched section as a new clip
# (starting at t0, so use "in": 0 for it) and a check sheet (original | patched, every 4th frame) next to it.
# usage: logo_patch.py src.mp4 t0 t1 x y out.mp4 [radius=30] [search=20]
#   (x, y): logo centre at t0 in source pixels. Look at the sheet before using the clip: the track can slip off on fast moves.
import json, subprocess, sys
import numpy as np
from numpy.lib.stride_tricks import sliding_window_view
from scipy.ndimage import gaussian_filter
from PIL import Image, ImageDraw

src, t0, t1, x, y, out = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
rad = int(sys.argv[7]) if len(sys.argv) > 7 else 30
S = int(sys.argv[8]) if len(sys.argv) > 8 else 20
R = 36                                   # template half size: the logo plus a margin of the surface around it
info = json.loads(subprocess.run(["ffprobe", "-v", "error", "-select_streams", "v:0", "-show_entries",
                                  "stream=width,height,r_frame_rate", "-of", "json", src],
                                 capture_output=True, text=True, check=True).stdout)["streams"][0]
W, H, fps = info["width"], info["height"], info["r_frame_rate"]
dec = subprocess.Popen(["ffmpeg", "-v", "error", "-ss", str(t0), "-t", f"{t1 - t0:.3f}", "-i", src,
                        "-f", "rawvideo", "-pix_fmt", "rgb24", "-"], stdout=subprocess.PIPE)
enc = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgb24", "-s", f"{W}x{H}", "-r", fps,
                        "-i", "-", "-c:v", "libx264", "-crf", "12", "-preset", "medium", "-pix_fmt", "yuv420p", out],
                       stdin=subprocess.PIPE)

P = 3 * rad                              # local window for the fill
yy, xx = np.mgrid[-P:P + 1, -P:P + 1]
dist = np.hypot(xx, yy)
known = (dist > rad).astype(np.float32)
alpha = np.clip((rad - dist) / 6.0, 0, 1)[..., None]   # 6 px feather at the disc edge


def fill(img, cx, cy):
    y0, x0 = cy - P, cx - P
    if y0 < 0 or x0 < 0 or cy + P + 1 > H or cx + P + 1 > W:
        return img                       # too close to the edge (not needed so far)
    patch = img[y0:cy + P + 1, x0:cx + P + 1].astype(np.float32)
    den = gaussian_filter(known, rad / 1.5)
    num = np.stack([gaussian_filter(patch[..., c] * known, rad / 1.5) for c in range(3)], -1)
    filled = num / np.maximum(den, 1e-4)[..., None]
    img[y0:cy + P + 1, x0:cx + P + 1] = np.clip(patch * (1 - alpha) + filled * alpha, 0, 255).astype(np.uint8)
    return img


def ncc_best(gray, T, cx, cy):
    reg = gray[cy - R - S:cy + R + S + 1, cx - R - S:cx + R + S + 1]
    win = sliding_window_view(reg, T.shape)                     # (2S+1, 2S+1, 2R+1, 2R+1)
    wm = win - win.mean(axis=(2, 3), keepdims=True)
    tm = T - T.mean()
    score = (wm * tm).sum(axis=(2, 3)) / (np.sqrt((wm ** 2).sum(axis=(2, 3)) * (tm ** 2).sum()) + 1e-6)
    dy, dx = np.unravel_index(np.argmax(score), score.shape)
    return cx + dx - S, cy + dy - S, float(score.max())


n, T, track, sheet = W * H * 3, None, [], []
k = 0
while True:
    buf = dec.stdout.read(n)
    if len(buf) < n:
        break
    img = np.frombuffer(buf, np.uint8).reshape(H, W, 3).copy()
    gray = img.astype(np.float32).mean(-1)
    if T is None:
        T, sc = gray[y - R:y + R + 1, x - R:x + R + 1].copy(), 1.0
    else:
        x, y, sc = ncc_best(gray, T, x, y)
        T = 0.8 * T + 0.2 * gray[y - R:y + R + 1, x - R:x + R + 1]   # follow slow changes of light and angle
    track.append((k, x, y, round(sc, 3)))
    before = img[y - 100:y + 100, x - 100:x + 100].copy()
    img = fill(img, x, y)
    if k % 4 == 0:
        sheet.append((k, before, img[y - 100:y + 100, x - 100:x + 100].copy(), sc))
    enc.stdin.write(img.tobytes())
    k += 1
enc.stdin.close(); enc.wait(); dec.wait()
print(k, "frames; lowest match", min(t[3] for t in track), "; track every 12th:", [t[:3] for t in track[::12]])
cols = 4
im = Image.new("RGB", (cols * 410, ((len(sheet) + cols - 1) // cols) * 216), (30, 30, 30)); d = ImageDraw.Draw(im)
for i, (kk, a, b, sc) in enumerate(sheet):
    X, Y = (i % cols) * 410, (i // cols) * 216
    im.paste(Image.fromarray(a), (X, Y + 16)); im.paste(Image.fromarray(b), (X + 205, Y + 16))
    d.text((X + 3, Y + 2), f"frame {kk}  match {sc:.2f}", fill=(255, 215, 80))
im.save(out + ".png")
print("sheet", out + ".png")
