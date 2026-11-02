# 사용자 AI 사진(별 표시 지운 것, photos_clean) -> 대본 번호 이름(photos_final/PNN.png), 상표·로고 자리만 흐림.
# 번호는 photo_map.py. 흐림 좌표는 그 사진의 원래 크기(2000x1116 또는 1024x572) 기준.
import glob, os, sys
from PIL import Image, ImageDraw, ImageFilter
sys.path.insert(0, '.')
from photo_map import IN2NUM
src, dst = 'photos_clean', 'photos_final'
os.makedirs(dst, exist_ok=True)
BLUR = {
    5: [('e', 1324, 348, 26, 15, 6)],                                   # 휴대폰 화면 왼쪽 위 빨간 앱 로고
    6: [('r', 364, 158, 394, 247, 4)],                                  # TV 화면 왼쪽 메뉴 아이콘(빨간 아이콘 하나)
    18: [('r', 538, 80, 602, 102, 4), ('r', 352, 238, 448, 288, 5)],    # 'Gmail Images' 글자, 바로가기 아이콘(빨간 영상 앱 아이콘)과 이름
    19: [('r', 503, 368, 567, 394, 4)],                                 # 노트북 아래 테두리의 옅은 상표 글자
    20: [('r', 463, 393, 527, 417, 4)],                                 # 노트북 아래 테두리의 옅은 상표 글자
    21: [('e', 513, 472, 34, 18, 6)],                                   # 운동 가방의 흰 스우시 로고
    22: [('r', 196, 122, 1004, 236, 4), ('r', 262, 226, 372, 282, 6)],  # 브라우저 탭·주소창(google.com, 아이콘), 'Google' 로고
    25: [('r', 793, 393, 902, 430, 5)],                                 # 태블릿 영상 재생기 오른쪽 아래 아이콘(빨간 로고 모양)
    28: [('e', 175, 437, 15, 15, 5)],                                   # 모니터 아래 사과 로고
    30: [('r', 538, 342, 588, 368, 4)],                                 # 모니터 영상 재생기 오른쪽 아래 빨간 아이콘
}
files = {int(os.path.basename(p)[2:4]): p for p in glob.glob(f'{src}/in*.png')}
for k, num in sorted(IN2NUM.items(), key=lambda t: t[1]):
    im = Image.open(files[k]).convert('RGB')
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
print(len(IN2NUM), 'photos ->', dst, '| blurred:', sorted(BLUR))
