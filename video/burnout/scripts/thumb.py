# 「INFJ입니다.」 썸네일 (2026-10-22): 「F의 연애」 썸네일 틀을 따름(사용자 지시)
# 검은 배경 + 위 두 칸에 그림 하나(원본 그대로, 기울이지 않음)
# + 아래 한 칸에 주제 단어 한 단어(흰색, Noto Sans KR 800, 262px, 바닥선 y=679, 글자 높이 240px 이상). 1280x720 JPG.
# 가운데 그림: 좌절하거나 지친 사람(2026-10-22 사용자 지시). 얼굴은 보이지 않게(손으로 가림, 엎드림, 뒷모습, 실루엣).
# 그림에는 그라데이션·효과를 넣지 않음(2026-10-22 사용자 지시): 가장자리 검게 녹이기, 아래쪽 사라지기,
# 어둡게 보정, 노이즈 없이 원본을 사각형 그대로 붙임. 주제 단어 함수(put_word)는 「F의 연애」와 같은 값입니다.
#
# usage (저장소 맨 위 폴더에서):
#   thumb.py photo   OUT.jpg IMAGE --box x0,y0,x1,y1 [--word 번아웃] [--top 30] [--bottom 405]
#       사진(무료 라이선스 스톡 영상의 한 장면, 검토 받은 AI 이미지)의 box 부분을 원본 그대로
#       y=top~bottom 높이에 맞춰 가로 가운데에 붙임. bottom은 글자 윗선(번아웃 459)보다 50px 이상 위
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


def put_word(img, word, color="white"):
    """Topic word: Noto Sans KR 800, centered, soft dark shadow underneath."""
    f = noto(WORD_WEIGHT, WORD_SIZE)
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).text((W / 2, WORD_BASE + 6), word, font=f, fill=235, anchor="ms")
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    img = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, sh)
    ImageDraw.Draw(img).text((W / 2, WORD_BASE), word, font=f, fill=COLORS.get(color, color), anchor="ms")
    return img


def place_photo(src, box, top=30, bottom=405):
    """The picture as is (no gradient, no effects): crop `box`, scale to the height top~bottom, centre on black."""
    im = Image.open(src).convert("RGB").crop(box)
    h = bottom - top
    im = im.resize((round(im.width * h / im.height), h), Image.LANCZOS)
    if im.width > W:
        sys.exit(f"picture is {im.width}px wide (> {W}): use a narrower --box")
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    canvas.paste(im, ((W - im.width) // 2, top))
    return canvas


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
    if mode != "photo":
        sys.exit(f"unknown mode {mode}: use photo or preview")
    box = tuple(int(v) for v in opt("--box", "0,0,1920,1080").split(","))
    img = place_photo(a[2], box, int(opt("--top", "30")), int(opt("--bottom", "405")))
    put_word(img, opt("--word", "번아웃"), opt("--color", "white")).save(out, quality=93)
    print(out)
