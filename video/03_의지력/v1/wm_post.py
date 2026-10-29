# 별을 지운 사진에서 별 테두리를 따라 남은 아주 옅은 선을 주변 그림으로 메움(biharmonic inpaint, 테두리 띠만).
# usage: wm_post.py <clean dir> <cx> <cy> <width> <alpha npy of that size>
import glob, sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage.restoration import inpaint_biharmonic
d, CX, CY, W, ap = sys.argv[1], float(sys.argv[2]), float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
s = W / 2000.0
A = np.load(ap)
h, w = A.shape
x0, y0 = int(round(CX - 68 * s)), int(round(CY - 68 * s))
gy, gx = np.gradient(ndi.gaussian_filter(A, 0.7))
gm = np.hypot(gx, gy)
band = ndi.binary_dilation(gm > 0.2 * gm.max(), iterations=1)
for p in sorted(glob.glob(f"{d}/in*.png")):
    im = Image.open(p).convert("RGB")
    if im.size[0] != W:
        continue
    a = np.asarray(im, np.float64) / 255.0
    pad = 6
    ya, yb, xa, xb = y0 - pad, y0 + h + pad, x0 - pad, x0 + w + pad
    reg = a[ya:yb, xa:xb].copy()
    m = np.zeros(reg.shape[:2], bool)
    m[pad:pad + h, pad:pad + w] = band
    out = inpaint_biharmonic(reg, m, channel_axis=-1)
    a[ya:yb, xa:xb] = out
    Image.fromarray(np.clip(a * 255 + 0.5, 0, 255).astype(np.uint8)).save(p)
print("done", W)
