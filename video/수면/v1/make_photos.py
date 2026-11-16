# 수면 편 사진: 별 표시 지운 것(photos_clean_t/inNN.png) -> photos_final/PNN.png (NN = 대본 번호, 03b·08b는 같은 번호로 하나 더 받은 사진)
# BLUR: 상표·로고 자리만 흐림. FILL: AI가 잘못 그린 곳을 주변으로 메움(biharmonic). 좌표는 1376x768 기준.
import glob, os
import numpy as np
from PIL import Image, ImageDraw, ImageFilter
from skimage.restoration import inpaint_biharmonic
src, dst = 'photos_clean_t', 'photos_final'
os.makedirs(dst, exist_ok=True)
BLUR = {
    '12': [('r', 485, 518, 527, 540, 4),    # 모니터 아래 테두리의 상표 글자
           ('r', 246, 236, 342, 262, 3)],   # 메일 화면 왼쪽 위 로고
    '14': [('r', 298, 250, 342, 272, 4),    # 왼쪽 모니터 아래 상표 글자
           ('r', 893, 183, 952, 207, 4)],   # 오른쪽 모니터 아래 상표 글자
}
FILL = {
    # 29번 혈당 측정기의 작은 글자는 지어낸 글자이고 영상 크기에서 읽히지 않아 그대로 둠(흐림·메움 모두 얼룩이 더 눈에 띔)
    '16': [(1250, 236, 1338, 306)],         # 문이 없는 오른쪽 끝에 하나 더 그려진 팻말('8 HOURS')
    '19': [(444, 505, 488, 556)],           # 졸림 눈금 맨 앞에 하나 더 그려진 '1'
    '35': [(246, 456, 364, 509)],           # TV 테두리의 상표 글자(흐림보다 깨끗해서 메움)
}
for p in sorted(glob.glob(f'{src}/in*.png')):
    key = os.path.basename(p)[2:-4]
    im = Image.open(p).convert('RGB')
    for (x0, y0, x1, y1) in FILL.get(key, []):
        pad = 12
        a = np.asarray(im, np.float64) / 255.0
        X0, Y0, X1, Y1 = max(x0 - pad, 0), max(y0 - pad, 0), min(x1 + pad, im.width), min(y1 + pad, im.height)
        sub = a[Y0:Y1, X0:X1].copy()
        m = np.zeros(sub.shape[:2], bool); m[y0 - Y0:y1 - Y0, x0 - X0:x1 - X0] = True
        sub = inpaint_biharmonic(sub, m, channel_axis=-1)
        rng = np.random.default_rng(int(key[:2]))
        noise = rng.normal(0, 0.006, sub.shape) * m[..., None]       # 둘레와 같은 잔결
        a[Y0:Y1, X0:X1] = np.clip(sub + noise, 0, 1)
        im = Image.fromarray((a * 255 + 0.5).astype(np.uint8))
    for kind, a_, b_, c_, d_, sig in BLUR.get(key, []):
        mask = Image.new('L', im.size, 0)
        ImageDraw.Draw(mask).rectangle((a_, b_, c_, d_), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(3))
        im = Image.composite(im.filter(ImageFilter.GaussianBlur(sig)), im, mask)
    im.save(f'{dst}/P{key}.png')
print(len(glob.glob(f'{dst}/P*.png')), 'photos ->', dst, '| blurred:', sorted(BLUR), '| filled:', sorted(FILL))
