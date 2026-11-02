# 51~76번 사진: 별 표시 지운 것(photos_clean2/inNN_b2.png) -> 대본 번호 이름(photos_final/PNN.png), 상표·로고 자리만 흐림.
# 번호는 photo_map2.py. 흐림 좌표는 그 사진의 원래 크기(2752x1536 또는 1376x768) 기준.
import os, sys
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '.')
from photo_map2 import IN2NUM2
src, dst = 'photos_clean2', 'photos_final'
os.makedirs(dst, exist_ok=True)
BLUR = {
    60: [('r', 1045, 745, 1230, 772, 5)],    # 모니터 아래 작업 표시줄(시작 단추와 앱 아이콘)
    61: [('r', 180, 408, 330, 432, 4)],      # 모니터 아래 작업 표시줄(시작 단추와 앱 아이콘)
    67: [('r', 995, 295, 1100, 328, 5)],     # 기타 케이스 뚜껑의 옅은 필기체 상표 글자
    74: [('r', 1855, 212, 1905, 242, 5)],    # 헤드폰 머리띠 옆의 상표 글자
}
for k, num in sorted(IN2NUM2.items(), key=lambda t: t[1]):
    im = Image.open(f'{src}/in{k:02d}_b2.png').convert('RGB')
    for kind, a, b, c, d, sig in BLUR.get(num, []):
        mask = Image.new('L', im.size, 0)
        dr = ImageDraw.Draw(mask)
        if kind == 'e':
            dr.ellipse((a - c, b - d, a + c, b + d), fill=255)
        else:
            dr.rectangle((a, b, c, d), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(3))
        im = Image.composite(im.filter(ImageFilter.GaussianBlur(sig)), im, mask)
    im.save(f'{dst}/P{num:02d}.png')
print(len(IN2NUM2), 'photos ->', dst, '| blurred:', sorted(BLUR))
