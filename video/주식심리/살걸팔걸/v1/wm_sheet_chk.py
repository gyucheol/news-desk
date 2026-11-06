# 별 자리 점검: 원본 / 지운 뒤 / 지운 뒤 대비 크게(남은 자국 보기). 사진 12장씩 한 장.
import sys, glob, os
import numpy as np
from PIL import Image, ImageDraw
CX, CY, R = 934.5, 482.5, 46
names = sys.argv[1:]
T = 200
def crop(p):
    im = Image.open(p).convert('RGB')
    return im.crop((int(CX - R), int(CY - R), int(CX + R), int(CY + R)))
def stretch(im):
    a = np.asarray(im, np.float64)
    m = a.mean((0, 1)); out = (a - m) * 4 + 128
    return Image.fromarray(np.clip(out, 0, 255).astype(np.uint8))
for k in range(0, len(names), 12):
    grp = names[k:k + 12]
    sheet = Image.new('RGB', (3 * (3 * T + 10), 4 * (T + 22)), (30, 30, 30))
    d = ImageDraw.Draw(sheet)
    for i, n in enumerate(grp):
        o = crop(f'wm_in_all/{n}.png'); c = crop(f'photos_clean_all/{n}.png')
        x = (i % 3) * (3 * T + 10); y = (i // 3) * (T + 22)
        for j, t in enumerate([o, c, stretch(c)]):
            sheet.paste(t.resize((T, T), Image.NEAREST), (x + j * T, y + 20))
        d.text((x + 4, y + 3), n, fill=(255, 255, 0))
    sheet.save(f'chk/wm_chk_{k // 12 + 1}.png')
    print(f'chk/wm_chk_{k // 12 + 1}.png', grp)
