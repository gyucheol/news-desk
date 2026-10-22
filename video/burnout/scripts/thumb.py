# 「INFJ입니다.」 썸네일 (2026-10-22): 「F의 연애」 썸네일 틀을 그대로 따름(사용자 지시)
# 검은 배경 + 위 두 칸(y 0~480)에 그림 하나(크게, 기울이지 않음)
# + 아래 한 칸에 주제 단어 한 단어(흰색, Noto Sans KR 800, 262px, 바닥선 y=679, 글자 높이 240px 이상). 1280x720 JPG.
# 가운데 그림: 좌절하거나 지친 사람(2026-10-22 사용자 지시). 얼굴은 보이지 않게(손으로 가림, 엎드림, 뒷모습, 실루엣).
# 공통 함수(bottom_fade, put_word, finish, noto)는 「F의 연애」 thumb.py·thumb_chat.py와 같은 값입니다.
#
# usage (저장소 맨 위 폴더에서):
#   thumb.py photo   OUT.jpg IMAGE --box x0,y0,x1,y1 [--word 번아웃] [--height 520] [--gamma 1.45] [--bg-dark 0~1]
#       사진(무료 라이선스 스톡 영상의 한 장면, 검토 받은 AI 이미지)의 box 부분을 위 두 칸 가운데에 두고
#       가장자리를 검게 녹임. --height: 그림 높이(사람과 글자 사이가 50px 이상 남게 조절)
#       --bg-dark: 밝고 색이 옅은 배경(창문, 흰 벽)만 눌러 어두운 방처럼 만듦(피부색은 유지)
#   thumb.py preview SHEET.png A.jpg B.jpg ...
#       시안마다 원래 크기 축소(640)와 휴대폰 피드 크기(가로 360)를 나란히 놓은 검토용 한 장
# fonts/NotoSansKR-VF.ttf (OFL) 필요: setup.sh가 받습니다.
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONT = f"{ROOT}/fonts/NotoSansKR-VF.ttf"
W, H, S = 1280, 720, 2                                   # draw at 2x, then downsample
COLORS = {"white": (255, 255, 255), "red": (230, 40, 48)}
WORD_SIZE, WORD_BASE, WORD_WEIGHT = 262, 679, 800        # 「F의 연애」와 같음. "번아웃" 높이 246px, 너비 723px


def noto(weight, size):
    """Noto Sans KR variable font at `weight`."""
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_axes([weight])
    return f


def bottom_fade(img, y0, y1):
    """Fade the picture to black from y0 to y1 so the word sits on black."""
    a = np.asarray(img, np.float32)
    g = np.clip((np.arange(img.height, dtype=np.float32) - y0) / (y1 - y0), 0, 1)
    g = g * g * (3 - 2 * g)
    a *= (1 - g)[:, None, None]
    return Image.fromarray(a.round().astype(np.uint8), "RGB")


def put_word(img, word, color="white"):
    """Topic word: Noto Sans KR 800, centered, soft dark shadow underneath."""
    f = noto(WORD_WEIGHT, WORD_SIZE)
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).text((W / 2, WORD_BASE + 6), word, font=f, fill=235, anchor="ms")
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    img = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, sh)
    ImageDraw.Draw(img).text((W / 2, WORD_BASE), word, font=f, fill=COLORS.get(color, color), anchor="ms")
    return img


def finish(img):
    """Edges fall off to black (dark room), faint noise, downsample to 1280x720."""
    CW, CH = img.size
    a = np.asarray(img, np.float32)
    yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
    r = np.sqrt(((xx - 0.50 * CW) / (0.64 * CW)) ** 2 + ((yy - 0.38 * CH) / (0.64 * CH)) ** 2)
    v = np.clip(1 - (r - 0.62) / 0.45, 0, 1)
    a *= (v * v * (3 - 2 * v))[..., None]
    a += np.random.default_rng(3).normal(0, 1.2, a.shape)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)


def make_photo(src, box, height=520, gamma=1.45, top=0, bg_dark=0.0):
    """Part of a photo (box) centred in the top area; edges melt into black, colours muted, mids darker.
    bg_dark (0~1): also press down bright, colourless areas (window, white wall) so a bright stock scene
    reads as a dark room; skin keeps its colour."""
    im = Image.open(src).convert("RGB").crop(box)
    sc = height / im.height
    im = im.resize((round(im.width * sc), height), Image.LANCZOS)
    a = np.asarray(im, np.float32) / 255
    lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    if bg_dark:
        sat = (a.max(2) - a.min(2)) / (a.max(2) + 1e-6)
        sm = lambda x: (lambda c: c * c * (3 - 2 * c))(np.clip(x, 0, 1))
        m = sm((lum - 0.45) / 0.30) * (1 - sm((sat - 0.08) / 0.17))
        m = np.asarray(Image.fromarray((m * 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(6)), np.float32) / 255
        a *= (1 - bg_dark * m)[..., None]
        lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    a = lum[..., None] + (a - lum[..., None]) * 0.85
    a = np.clip(a, 0, 1) ** gamma
    h, w = lum.shape
    yy, xx = np.mgrid[0:h, 0:w].astype(np.float32)
    r = np.sqrt(((xx - w / 2) / (w * 0.50)) ** 2 + ((yy - h * 0.45) / (h * 0.56)) ** 2)
    v = np.clip(1 - (r - 0.55) / 0.50, 0, 1)                         # wide soft oval, melts into black
    a *= (v * v * (3 - 2 * v))[..., None]
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    canvas.paste(Image.fromarray((np.clip(a, 0, 1) * 255).round().astype(np.uint8)), ((W - w) // 2, top))
    big = canvas.resize((W * S, H * S), Image.LANCZOS)
    return finish(big)


def preview(sheet, files):
    """Each draft at 640 px next to the phone-feed size (360 px), with its letter."""
    lab = noto(800, 40)
    out = Image.new("RGB", (640 + 360 + 60, len(files) * 380 + 20), (40, 40, 44))
    d = ImageDraw.Draw(out)
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB")
        y = 20 + i * 380
        out.paste(im.resize((640, 360), Image.LANCZOS), (50, y))
        out.paste(im.resize((360, 203), Image.LANCZOS), (50 + 640 + 10, y + 157))
        d.text((10, y), chr(ord("A") + i), font=lab, fill=(255, 215, 80))
    out.save(sheet)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    mode, out = a[0], a[1]
    if mode == "preview":
        preview(out, a[2:]); print(out); sys.exit()
    if mode != "photo":
        sys.exit(f"unknown mode {mode}: use photo or preview")
    box = tuple(int(v) for v in opt("--box", "0,0,1920,1080").split(","))
    img = make_photo(a[2], box, int(opt("--height", "520")), float(opt("--gamma", "1.45")),
                     bg_dark=float(opt("--bg-dark", "0")))
    img = bottom_fade(img, 430, 560)
    put_word(img, opt("--word", "번아웃"), opt("--color", "white")).save(out, quality=93)
    print(out)
