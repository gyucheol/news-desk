# 사용자 AI 사진(별 표시 지운 것) -> 대본 번호 이름(photos_final/PNN.png), 상표 자리만 흐림.
# 번호는 사진 내용과 표시된 대사를 맞춰 정함(메시지 안의 순서는 번호 순서와 다른 곳이 있었음: 첫 메시지 5,1,2,3,4 / 둘째 7,8,9,10,6).
# 받은 순서 in55(54번과 거의 같은 두 번째 판)는 대본에 자리가 없어 쓰지 않고, 77번 사진은 아직 받지 못함.
import os, glob
import numpy as np
from PIL import Image, ImageFilter, ImageDraw
src, dst = 'photos_clean', 'photos_final'
os.makedirs(dst, exist_ok=True)
NUM = {1: 2, 2: 3, 3: 4, 4: 5, 5: 1, 6: 10, 7: 6, 8: 7, 9: 8, 10: 9}
for n in range(11, 55):
    NUM[n] = n                 # in11..in54 = 11..54
for n in range(55, 71):
    NUM[n] = n + 1             # in56..in71 = 55..70
NUM.update({72: 72, 74: 73, 75: 74, 76: 75})
# 상표: 65번 운동화 옆 로고(두 짝), 70번 배드민턴 라켓 줄의 로고, 75번 벽 포스터 글씨 (1376x768 기준)
BLUR = {65: [('e', 885, 457, 68, 36, 5), ('e', 478, 355, 42, 38, 5)],
        70: [('e', 722, 242, 62, 46, 6)],
        75: [('r', 288, 118, 408, 202, 5), ('r', 280, 276, 348, 302, 4), ('r', 325, 626, 412, 697, 5)]}
files = {int(os.path.basename(p)[2:4]): p for p in glob.glob(f'{src}/in*.png')}
for num, k in sorted(NUM.items()):
    im = Image.open(files[k]).convert('RGB')
    for spec in BLUR.get(num, []):
        kind, a, b, c, d, sig = spec
        mask = Image.new('L', im.size, 0)
        dr = ImageDraw.Draw(mask)
        if kind == 'e':
            dr.ellipse((a - c, b - d, a + c, b + d), fill=255)
        else:
            dr.rectangle((a, b, c, d), fill=255)
        mask = mask.filter(ImageFilter.GaussianBlur(4))
        im = Image.composite(im.filter(ImageFilter.GaussianBlur(sig)), im, mask)
    im.save(f'{dst}/P{num:02d}.png')
print(len(NUM), 'photos ->', dst)
