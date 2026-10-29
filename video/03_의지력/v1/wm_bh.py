# 어두운 배경에서 별 자리에 아주 옅은 잔상이 남은 사진: 원본에서 별 자리(조금 넓게)를 비우고 주변 색으로 매끄럽게 메운 뒤
# (biharmonic inpaint), 바로 바깥 고리와 같은 크기의 잔무늬(입자)를 더함. 별 모양 경계가 생기지 않게 가장자리는 부드럽게 섞음.
# usage: wm_bh.py <orig> <clean png to overwrite> <cx> <cy> <width> <alpha npy> [seed]
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
from skimage.restoration import inpaint_biharmonic
orig, outp, CX, CY, W, ap = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
seed = int(sys.argv[7]) if len(sys.argv) > 7 else 0
DIL = int(sys.argv[8]) if len(sys.argv) > 8 else 2
s = W / 2000.0
A = np.load(ap); h, w = A.shape
x0, y0 = int(round(CX - 68 * s)), int(round(CY - 68 * s))
img = np.asarray(Image.open(orig).convert("RGB"), np.float64) / 255.0
pad = 8
ya, yb, xa, xb = y0 - pad, y0 + h + pad, x0 - pad, x0 + w + pad
reg = img[ya:yb, xa:xb].copy()
m = np.zeros(reg.shape[:2], bool)
m[pad:pad + h, pad:pad + w] = ndi.binary_dilation(A > 0.01, iterations=DIL)
F = inpaint_biharmonic(reg, m, channel_axis=-1)
ring = ndi.binary_dilation(m, iterations=6) & ~ndi.binary_dilation(m, iterations=1)
rng = np.random.default_rng(seed)
for c in range(3):
    hf = reg[..., c] - ndi.gaussian_filter(reg[..., c], 1.0)
    sd = hf[ring].std()
    n = ndi.gaussian_filter(rng.normal(0, 1, m.shape), 0.6)
    n = n / (n.std() + 1e-9) * sd
    F[..., c] = np.where(m, F[..., c] + n, F[..., c])
# soft blend at the mask edge
wgt = ndi.gaussian_filter(m.astype(float), 1.2)
out = reg * (1 - wgt[..., None]) + F * wgt[..., None]
clean = np.asarray(Image.open(outp).convert("RGB"), np.float64) / 255.0
clean[ya:yb, xa:xb] = out
Image.fromarray(np.clip(clean * 255 + 0.5, 0, 255).astype(np.uint8)).save(outp)
print("ok", outp)
