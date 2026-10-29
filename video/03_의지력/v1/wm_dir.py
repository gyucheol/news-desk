# 별이 곧은 경계(책상 모서리 띠)를 가로지르는 사진(54번): 별 자리를 경계와 나란한 방향의 양쪽 바깥 픽셀로 채움.
# 경계 방향은 별 둘레 고리의 구조 텐서로 잼. usage: wm_dir.py <orig> <clean png> <cx> <cy> <width> <alpha npy>
import sys
import numpy as np
from PIL import Image
from scipy import ndimage as ndi
orig, outp, CX, CY, W, ap = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4]), int(sys.argv[5]), sys.argv[6]
s = W / 2000.0
A = np.load(ap); h, w = A.shape
x0, y0 = int(round(CX - 68 * s)), int(round(CY - 68 * s))
img = np.asarray(Image.open(orig).convert("RGB"), np.float64)
pad = 60
ya, yb, xa, xb = y0 - pad, y0 + h + pad, x0 - pad, min(x0 + w + pad, img.shape[1])
reg = img[ya:yb, xa:xb].copy()
m = np.zeros(reg.shape[:2], bool)
m[pad:pad + h, pad:pad + w] = ndi.binary_dilation(A > 0.01, iterations=4)
ring = ndi.binary_dilation(m, iterations=14) & ~ndi.binary_dilation(m, iterations=2)
g = ndi.gaussian_filter(reg.mean(2), 1.5)
gy, gx = np.gradient(g)
J = np.array([[np.sum((gx * gx)[ring]), np.sum((gx * gy)[ring])], [np.sum((gx * gy)[ring]), np.sum((gy * gy)[ring])]])
ev, evec = np.linalg.eigh(J)
n = evec[:, 1]                        # gradient direction (across the edge)
v = np.array([-n[1], n[0]])           # along the edge (x, y)
print("edge direction (x,y)", v.round(3), "angle", round(np.degrees(np.arctan2(v[1], v[0])), 1))
ys, xs = np.nonzero(m)
out = reg.copy()
Hh, Ww = m.shape
for y, x in zip(ys, xs):
    vals, wts = [], []
    for sgn in (1, -1):
        t = 1.0
        while t < 200:
            px, py = x + sgn * v[0] * t, y + sgn * v[1] * t
            ix, iy = int(round(px)), int(round(py))
            if not (0 <= ix < Ww and 0 <= iy < Hh):
                break
            if not m[iy, ix]:
                # bilinear sample just outside
                vals.append(ndi.map_coordinates(reg.transpose(2, 0, 1), [[[py]] * 3, [[px]] * 3], order=1).reshape(-1)[:3]
                            if False else np.array([ndi.map_coordinates(reg[..., c], [[py], [px]], order=1)[0] for c in range(3)]))
                wts.append(1.0 / t)
                break
            t += 0.5
    if vals:
        out[y, x] = np.average(np.array(vals), axis=0, weights=np.array(wts))
# light grain to match the ring
rng = np.random.default_rng(0)
for c in range(3):
    hf = reg[..., c] - ndi.gaussian_filter(reg[..., c], 1.0)
    sd = hf[ring].std()
    nz = ndi.gaussian_filter(rng.normal(0, 1, m.shape), 0.6)
    out[..., c] = np.where(m, out[..., c] + nz / (nz.std() + 1e-9) * sd, out[..., c])
wgt = ndi.gaussian_filter(m.astype(float), 1.0)[..., None]
res = reg * (1 - wgt) + out * wgt
clean = np.asarray(Image.open(outp).convert("RGB"), np.float64)
clean[ya:yb, xa:xb] = res
Image.fromarray(np.clip(clean + 0.5, 0, 255).astype(np.uint8)).save(outp)
print("ok")
