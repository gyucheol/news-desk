# 채널 프로필 사진 시안 (2026-10-24, 「INFJ입니다.」)
#   1_text.png: 검은 배경에 흰 "INFJ" + 노란 마침표(채널 이름 "INFJ입니다."의 마침표, 자막 강조색 #F2C94C).
#               글꼴은 썸네일 주제 단어와 같은 Noto Sans KR 굵기 800(OFL).
#   2_bulb.png: 영상의 '작은 힌트' 아이콘 화면(render.py icon_frame "bulb", 켜진 상태)에서 전구 둘레를 정사각형으로 자름.
#   review_sheet.png: 두 시안을 원형으로 잘라 큰 크기, 98px(유튜브 도움말의 표시 크기), 40px로 밝은·어두운 배경 위에 나란히.
# 유튜브 도움말(2026-10-24 확인): 98 x 98 px로 보임, JPG·GIF·BMP·PNG(움직이는 GIF 제외), 15MB 이하, 정사각형이나 원형 권장.
# 그림은 원형으로 잘려 보이므로 글자·그림을 가운데 원 안에 둡니다. 800 x 800으로 저장합니다.
# usage: VIDEO_ROOT=<fonts/가 있는 폴더> python scripts/profile_pic.py <out folder>
import os, sys
from PIL import Image, ImageDraw, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import render                                                  # icon_frame, ROOT, YELLOW

OUT = sys.argv[1]
os.makedirs(OUT, exist_ok=True)
N = 800
YEL = render.YELLOW[:3]                                        # (242, 201, 76) = #F2C94C


def noto(weight, size):
    f = ImageFont.truetype(f"{render.ROOT}/fonts/NotoSansKR-VF.ttf", size)
    f.set_variation_by_axes([weight])
    return f


def text_logo(width_frac=0.70):
    """White "INFJ" + yellow ".", ink centred, ink width = width_frac of the canvas (drawn at 2x)."""
    SS = 2
    M = N * SS
    img = Image.new("RGB", (M, M), (0, 0, 0))
    d = ImageDraw.Draw(img)
    size = 400
    for _ in range(4):                                         # scale the font until the ink width fits
        f = noto(800, size)
        x0, y0, x1, y1 = d.textbbox((0, 0), "INFJ.", font=f, anchor="ls")
        size = round(size * width_frac * M / (x1 - x0))
    f = noto(800, size)
    x0, y0, x1, y1 = d.textbbox((0, 0), "INFJ.", font=f, anchor="ls")
    ox, oy = (M - (x1 - x0)) / 2 - x0, (M - (y1 - y0)) / 2 - y0
    d.text((ox, oy), "INFJ", font=f, fill=(255, 255, 255), anchor="ls")
    d.text((ox + d.textlength("INFJ", font=f), oy), ".", font=f, fill=YEL, anchor="ls")
    return img.resize((N, N), Image.LANCZOS), size // SS


def bulb():
    """The lit bulb from the icon screen, cropped to a square around the bulb (it fits inside the round crop)."""
    fr = render.icon_frame("bulb", 2.0, 3.0)                   # 1920 x 1080, lit
    cx, cy, side = render.W / 2, render.H * 0.42 + 23, 640     # bulb spans about cy-191 .. cy+237 (render.py)
    box = (round(cx - side / 2), round(cy - side / 2), round(cx + side / 2), round(cy + side / 2))
    return fr.crop(box).resize((N, N), Image.LANCZOS)


def circle(img, d):
    im = img.resize((d, d), Image.LANCZOS)
    m = Image.new("L", (d * 4, d * 4), 0)
    ImageDraw.Draw(m).ellipse([0, 0, d * 4 - 1, d * 4 - 1], fill=255)
    return im, m.resize((d, d), Image.LANCZOS)


def sheet(drafts, path):
    sizes = [300, 98, 40]
    pw, row_h, top = 640, 420, 70                              # circles sit above a 50px label strip
    W2 = pw * 2 + 60
    out = Image.new("RGB", (W2, top + row_h * len(drafts)), (40, 40, 40))
    d = ImageDraw.Draw(out)
    fl = noto(500, 26)
    d.text((30 + pw / 2, 36), "밝은 화면", font=fl, fill=(230, 230, 230), anchor="mm")
    d.text((90 + pw * 1.5, 36), "어두운 화면", font=fl, fill=(230, 230, 230), anchor="mm")
    for i, (label, img) in enumerate(drafts):
        y = top + i * row_h
        for j, bg in enumerate([(255, 255, 255), (15, 15, 15)]):
            x0 = 30 + j * (pw + 30)
            d.rectangle([x0, y, x0 + pw, y + row_h - 20], fill=bg)
            fg = (20, 20, 20) if j == 0 else (235, 235, 235)
            d.text((x0 + 16, y + 12), label, font=noto(700, 28), fill=fg)
            x = x0 + 30
            for s in sizes:
                im, m = circle(img, s)
                yy = y + 50 + (row_h - 20 - 50 - 50 - s) / 2
                out.paste(im, (round(x), round(yy)), m)
                d.text((x + s / 2, y + row_h - 45), f"{s}px", font=noto(400, 20), fill=fg, anchor="mm")
                x += s + 50
    out.save(path)


t, size = text_logo()
t.save(f"{OUT}/1_text.png")
b = bulb()
b.save(f"{OUT}/2_bulb.png")
sheet([("1  INFJ.", t), ("2  전구", b)], f"{OUT}/review_sheet.png")
print("text font size", size, "| saved 1_text.png, 2_bulb.png, review_sheet.png in", OUT)
