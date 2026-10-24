# 「INFJ입니다.」 썸네일 (2026-10-22): 「F의 연애」 썸네일 틀을 따름(사용자 지시)
# 그림 하나(원본 그대로, 기울이지 않음) + 아래 한 칸에 주제 단어 한 단어(흰색, Noto Sans KR 800, 262px, 바닥선 y=679, 글자 높이 240px 이상). 1280x720 JPG.
# 가운데 그림: 좌절하거나 지친 사람(2026-10-22 사용자 지시). 얼굴은 보이지 않게(손으로 가림, 엎드림, 뒷모습, 실루엣).
# 배경이 있는 그림은 두 판을 만듦(같은 날 사용자 지시): 1 배경을 다 살린 판(full), 2 배경을 지우고 사람만 남긴 판(cutout.py + photo).
# 그림에는 그라데이션·효과를 넣지 않음(2026-10-22 사용자 지시): 가장자리 검게 녹이기, 아래쪽 사라지기,
# 어둡게 보정, 노이즈 없이 원본을 사각형 그대로 붙임. 주제 단어 함수(put_word)는 「F의 연애」와 같은 값입니다.
#
# usage (저장소 맨 위 폴더에서):
#   thumb.py full    OUT.jpg IMAGE [--box x0,y0,x1,y1] [--word 번아웃] [--word-cx 640]
#       배경을 다 살린 판: 그림이 썸네일 전체(1280x720)를 채우고 글자가 그림 위에 올라감.
#       --word-cx: 글자 가운데의 가로 위치(사람을 가리지 않는 쪽으로 옮김)
#   thumb.py photo   OUT.jpg IMAGE [--box x0,y0,x1,y1] [--word 번아웃] [--top 30] [--bottom 405]
#       그림을 원본 그대로 y=top~bottom 높이에 맞춰 검은 배경 가운데에 붙임. bottom은 글자 윗선(번아웃 459)보다
#       50px 이상 위. 배경을 지운 판: cutout.py로 오린 투명 배경 PNG를 넣으면 사람 윤곽대로 붙음(--box 생략 시 사람에 맞춰 자름)
#   thumb.py preview SHEET.png A.jpg B.jpg ... [--labels 1,2]
#       시안마다 원래 크기 축소(640)와 휴대폰 피드 크기(가로 360)를 나란히 놓은 검토용 한 장
# fonts/NotoSansKR-VF.ttf (OFL) 필요: setup.sh가 받습니다.
import os, sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
FONT = f"{ROOT}/fonts/NotoSansKR-VF.ttf"
W, H = 1280, 720
COLORS = {"white": (255, 255, 255), "red": (230, 40, 48)}
WORD_SIZE, WORD_BASE, WORD_WEIGHT = 262, 679, 800        # 「F의 연애」와 같음. "번아웃" 높이 246px, 너비 723px


def noto(weight, size):
    """Noto Sans KR variable font at `weight`."""
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_axes([weight])
    return f


def put_word(img, word, color="white", cx=W / 2):
    """Topic word: Noto Sans KR 800, centred on x=cx, soft dark shadow underneath (「F의 연애」 글자 규격)."""
    f = noto(WORD_WEIGHT, WORD_SIZE)
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).text((cx, WORD_BASE + 6), word, font=f, fill=235, anchor="ms")
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    img = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, sh)
    ImageDraw.Draw(img).text((cx, WORD_BASE), word, font=f, fill=COLORS.get(color, color), anchor="ms")
    return img


def place_photo(src, box=None, top=30, bottom=405):
    """The picture as is (no gradient, no effects): crop `box`, scale to the height top~bottom, centre on black.
    A cut-out with a transparent background (cutout.py) is pasted by its own outline; without --box it is
    cropped to the person."""
    im = Image.open(src)
    cut = im.mode in ("RGBA", "LA") or "transparency" in im.info
    im = im.convert("RGBA" if cut else "RGB")
    if box is None:
        box = im.getchannel("A").point(lambda v: 255 if v > 8 else 0).getbbox() if cut else (0, 0, im.width, im.height)
    im = im.crop(box)
    h = bottom - top
    im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    if im.width > W:
        sys.exit(f"picture is {im.width}px wide (> {W}): use a narrower --box")
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    canvas.paste(im, ((W - im.width) // 2, top), im if cut else None)
    return canvas


def fill_photo(src, box=None):
    """The picture as is, filling the whole thumbnail (background kept). Crops only what does not fit 16:9."""
    im = Image.open(src).convert("RGB")
    if box:
        im = im.crop(box)
    sc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x0, y0 = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x0, y0, x0 + W, y0 + H))


def preview(sheet, files, labels=None):
    """Each draft at 640 px next to the phone-feed size (360 px), with its label (A, B, C... by default)."""
    lab = noto(800, 40)
    out = Image.new("RGB", (640 + 360 + 60, len(files) * 380 + 20), (40, 40, 44))
    d = ImageDraw.Draw(out)
    for i, f in enumerate(files):
        im = Image.open(f).convert("RGB")
        y = 20 + i * 380
        out.paste(im.resize((640, 360), Image.LANCZOS), (50, y))
        out.paste(im.resize((360, 203), Image.LANCZOS), (50 + 640 + 10, y + 157))
        d.text((10, y), labels[i] if labels else chr(ord("A") + i), font=lab, fill=(255, 215, 80))
    out.save(sheet)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    mode, out = a[0], a[1]
    if mode == "preview":
        files = [x for x in a[2:] if x != "--labels" and x != opt("--labels", None)]
        labels = opt("--labels", None)
        preview(out, files, labels.split(",") if labels else None); print(out); sys.exit()
    box = tuple(int(v) for v in opt("--box", "").split(",")) if "--box" in a else None
    if mode == "photo":
        img = place_photo(a[2], box, int(opt("--top", "30")), int(opt("--bottom", "405")))
    elif mode == "full":
        img = fill_photo(a[2], box)
    else:
        sys.exit(f"unknown mode {mode}: use photo, full or preview")
    cx = float(opt("--word-cx", W / 2))
    put_word(img, opt("--word", "번아웃"), opt("--color", "white"), cx).save(out, quality=93)
    print(out)
