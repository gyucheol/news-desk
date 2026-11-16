# 살걸·팔걸 편 사진: 별 표시 지운 것(photos_clean_all/inNN.png) -> photos_final/PNN.png (NN = 대본 번호 = 받은 순서)
# BLUR: 상표·로고·전화번호처럼 보이는 자리만 흐림. 좌표는 1024x572 기준.
import glob, os
from PIL import Image, ImageDraw, ImageFilter
src, dst = 'photos_clean_all', 'photos_final'
os.makedirs(dst, exist_ok=True)
BLUR = {
    '37': [('r', 150, 268, 232, 348, 5)],    # 상자 옆면의 쇼핑몰 로고(웃는 화살표)와 글자
    '29': [('r', 952, 34, 1022, 66, 3),     # 오른쪽 위 간판의 전화번호처럼 보이는 숫자
           ('r', 824, 78, 892, 100, 3)],    # 식당 간판 아래 작은 숫자
}
for p in sorted(glob.glob(f'{src}/in*.png')):
    key = os.path.basename(p)[2:-4]
    im = Image.open(p).convert('RGB')
    for kind, a_, b_, c_, d_, sig in BLUR.get(key, []):
        mask = Image.new('L', im.size, 0)
        ImageDraw.Draw(mask).rectangle((a_, b_, c_, d_), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(3))
        im = Image.composite(im.filter(ImageFilter.GaussianBlur(sig)), im, mask)
    im.save(f'{dst}/P{key}.png')
print(len(glob.glob(f'{dst}/P*.png')), 'photos ->', dst, '| blurred:', sorted(BLUR))
