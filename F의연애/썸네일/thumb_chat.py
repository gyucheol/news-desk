# 「F의 연애」 썸네일: 채팅 확대판 (2026-10-22 사용자 지시)
# 휴대폰 몸체 없이 대화 내용만 크게 확대해, 썸네일을 작게 봐도 노란 말풍선과 읽지 않은 '1'이 눈에 들어오게 한다.
# 실제 화면을 가까이서 찍은 사진처럼 보이게: 살짝 기운 원근, 가장자리 초점 흐림, 말풍선 빛 번짐, 은은한 화면 반사.
# 배경은 검은색으로 사라지고, 아래에 주제 단어(thumb.py와 같은 글꼴·위치).
#
# usage: thumb_chat.py OUT.jpg --word 불안 --color red [--msgs "a|b|c"] [--name "그 사람"]
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thumb import W, H, YEL, font, bottom_fade, put_word   # noqa: E402

S = 2                       # draw at 2x, then downsample
SCREEN = (22, 24, 30)       # dark-mode chat background


def chat_panel(msgs, name):
    """Flat dark-mode chat panel at 2x. Bubbles are big: about 88 px tall in the final 1280x720 thumbnail."""
    pw, ph = 1180 * S, 700 * S
    img = Image.new("RGB", (pw, ph), SCREEN)
    d = ImageDraw.Draw(img)
    hy = 62 * S                                                     # header (ends up soft and partly cropped)
    d.line([(70 * S, hy - 22 * S), (52 * S, hy), (70 * S, hy + 22 * S)], fill=(225, 225, 230), width=6 * S, joint="curve")
    d.ellipse([96 * S, hy - 32 * S, 160 * S, hy + 32 * S], fill=(92, 98, 112))
    d.text((182 * S, hy), name, font=font("SemiBold", 42 * S), fill=(235, 235, 240), anchor="lm")
    d.line([(0, 128 * S), (pw, 128 * S)], fill=(44, 47, 56), width=2 * S)
    fb, f1 = font("SemiBold", 46 * S), font("Bold", 54 * S)
    y = 168 * S
    right = pw - 320 * S
    for i, m in enumerate(msgs):
        tw = fb.getlength(m)
        bw, bh = tw + 72 * S, 92 * S
        x1, x0 = right, right - bw
        d.rounded_rectangle([x0, y, x1, y + bh], radius=32 * S, fill=YEL)
        if i == 0:
            d.polygon([(x1 - 40 * S, y), (x1 + 18 * S, y + 8 * S), (x1 - 4 * S, y + 38 * S)], fill=YEL)
        d.text(((x0 + x1) / 2, y + bh / 2 + 2 * S), m, font=fb, fill=(30, 26, 18), anchor="mm")
        d.text((x0 - 16 * S, y + bh - 6 * S), "1", font=f1, fill=YEL, anchor="rs")
        y += bh + 28 * S
    return img


def perspective_coeffs(dst, src):
    A, B = [], []
    for (x, y), (u, v) in zip(dst, src):
        A.append([x, y, 1, 0, 0, 0, -u * x, -u * y]); B.append(u)
        A.append([0, 0, 0, x, y, 1, -v * x, -v * y]); B.append(v)
    return np.linalg.solve(np.array(A, np.float64), np.array(B, np.float64)).tolist()


def photo_look(panel):
    """Place the panel with a mild 3D tilt (left side farther away), then add depth of field, glow and glare."""
    CW, CH = W * S, H * S
    pw, ph = panel.size
    # target quad (2x canvas): right edge nearer/taller than the left edge, slight downward tilt
    dst = [(40 * S, 40 * S), (1270 * S, -10 * S), (1290 * S, 650 * S), (60 * S, 560 * S)]
    src = [(0, 0), (pw, 0), (pw, ph), (0, ph)]
    img = panel.transform((CW, CH), Image.PERSPECTIVE, perspective_coeffs(dst, src), Image.BICUBIC, fillcolor=SCREEN)
    a = np.asarray(img, np.float32)
    # depth of field: sharp around the bubbles, softer toward the far (left) side and the top header
    yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
    cx, cy = 760 * S, 300 * S
    dist = np.sqrt(((xx - cx) / (560 * S)) ** 2 + ((yy - cy) / (300 * S)) ** 2)
    wgt = np.clip((dist - 0.75) / 0.6, 0, 1)
    soft = np.asarray(img.filter(ImageFilter.GaussianBlur(9 * S)), np.float32)
    a = a * (1 - wgt[..., None]) + soft * wgt[..., None]
    # glow: bright yellow bubbles bloom a little, like a lit screen in a dark room
    lum = a.mean(2)
    bright = Image.fromarray(np.clip((lum - 120) * 2, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(26 * S))
    a += (np.asarray(bright, np.float32) / 255)[..., None] * np.array([70, 55, 15], np.float32)
    # faint diagonal glare on the glass; smudges (fingerprints) only show where the glare is, as on real glass
    band = np.clip(1 - np.abs((xx - 0.62 * CW) * 0.8 + (yy - 0.3 * CH) * 1.0) / (260 * S), 0, 1)
    rng = np.random.default_rng(11)
    sm = Image.fromarray((rng.random((CH // 8, CW // 8)) * 255).astype(np.uint8)).resize((CW, CH), Image.BICUBIC)
    sm = np.asarray(sm.filter(ImageFilter.GaussianBlur(6 * S)), np.float32) / 255
    a += (band * (6 + 16 * np.clip((sm - 0.45) * 3, 0, 1)))[..., None]
    # light falls off toward the frame edges (dark room): fade to pure black
    r = np.sqrt(((xx - 0.55 * CW) / (0.62 * CW)) ** 2 + ((yy - 0.40 * CH) / (0.62 * CH)) ** 2)
    v = np.clip(1 - (r - 0.55) / 0.5, 0, 1)
    a *= (v * v * (3 - 2 * v))[..., None]
    a += np.random.default_rng(3).normal(0, 1.6, a.shape)          # faint sensor noise
    img = Image.fromarray(np.clip(a, 0, 255).astype(np.uint8))
    # lens: red and blue drift apart slightly toward the edges (chromatic aberration)
    rch, gch, bch = img.split()
    def zoom(ch, k):
        w2, h2 = round(CW * k), round(CH * k)
        z = ch.resize((w2, h2), Image.BICUBIC)
        return z.crop(((w2 - CW) // 2, (h2 - CH) // 2, (w2 - CW) // 2 + CW, (h2 - CH) // 2 + CH))
    img = Image.merge("RGB", (zoom(rch, 1.0016), gch, zoom(bch, 0.9984)))
    out = img.resize((W, H), Image.LANCZOS)
    return out


def make(out, msgs, name, word, color):
    img = photo_look(chat_panel(msgs, name))
    img = bottom_fade(img, 470, 600)
    put_word(img, word, color).save(out, quality=93)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    make(a[0], opt("--msgs", "오늘 하루 어땠어요?|바빠요? ㅎㅎ|자요..?").split("|"), opt("--name", "그 사람"),
         opt("--word", "불안"), opt("--color", "red"))
    print(a[0])
