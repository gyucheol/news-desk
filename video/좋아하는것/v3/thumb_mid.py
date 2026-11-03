# 04편 썸네일 후보(2026-11-03). 사용자: "썸네일 후보 4가지 주라. 중간에 글씨는 '취미가 있는 사람' 이렇게"
# 채널 틀(video/burnout/scripts/thumb.py, 「F의 연애」 틀)을 따름: 1280x720 JPG, 사진은 원본 그대로(효과 없음, 기울이지 않음,
# 넘치는 부분만 자름), 흰 글씨 Noto Sans KR 800, 글자 아래 그림자(아래로 6px, 흐림 14px), 빨강 (230,40,48)은 고를 수 있는 색.
# 다른 점(사용자 요청): 글씨를 아래 칸이 아니라 화면 가운데(세로 가운데 y=360)에 둠. 7글자라 한 단어 규격 262px로는 화면에
# 들어가지 않아, 한 줄(가로 1150px 안에 드는 가장 큰 크기) 또는 두 줄("취미가 있는" / "사람")로 만듦.
# 2026-11-03 추가: --text로 다른 문구(짧으면 채널 틀 크기 262px, 길면 가로 1150px 안에 맞춤).
# usage: thumb_mid.py OUT.jpg IMAGE --lines 1|2 [--text 문구] [--box x0,y0,x1,y1] [--red 취미] [--cy 360] [--size px]
import sys
from PIL import Image, ImageDraw, ImageFilter, ImageFont
FONT = '/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/fonts/NotoSansKR-VF.ttf'
W, H = 1280, 720
WHITE, RED = (255, 255, 255), (230, 40, 48)
TEXT = '취미가 있는 사람'


def noto(size, weight=800):
    f = ImageFont.truetype(FONT, size)
    f.set_variation_by_axes([weight])
    return f


def fill_photo(src, box=None):
    im = Image.open(src).convert('RGB')
    if box:
        im = im.crop(box)
    sc = max(W / im.width, H / im.height)
    im = im.resize((round(im.width * sc), round(im.height * sc)), Image.LANCZOS)
    x0, y0 = (im.width - W) // 2, (im.height - H) // 2
    return im.crop((x0, y0, x0 + W, y0 + H))


def fit_size(lines, maxw=1150, start=300):
    s = start
    while s > 60:
        f = noto(s)
        if max(f.getlength(l) for l in lines) <= maxw:
            return s
        s -= 2
    return s


def put_text(img, lines, cy=360, red=None, gap=0.10, size=None):
    size = size or fit_size(lines)
    f = noto(size)
    asc, desc = f.getmetrics()
    # 글자 높이: 한글 글자 상자 기준(실제 잉크 높이로 줄 간격을 잡음)
    ink = [f.getbbox(l) for l in lines]
    line_h = max(b[3] - b[1] for b in ink)
    step = line_h * (1 + gap)
    total = line_h + step * (len(lines) - 1)
    top = cy - total / 2
    # 그림자
    sh = Image.new('L', (W, H), 0)
    d = ImageDraw.Draw(sh)
    pos = []
    for i, l in enumerate(lines):
        b = ink[i]
        y = top + i * step - b[1]            # 잉크 윗선이 top + i*step
        x = (W - f.getlength(l)) / 2
        pos.append((x, y))
        d.text((x, y + 6), l, font=f, fill=235)
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    img = Image.composite(Image.new('RGB', (W, H), (0, 0, 0)), img, sh)
    d = ImageDraw.Draw(img)
    for (x, y), l in zip(pos, lines):
        if red and red in l:
            k = l.index(red)
            pre, mid, post = l[:k], red, l[k + len(red):]
            d.text((x, y), pre, font=f, fill=WHITE)
            x2 = x + f.getlength(pre)
            d.text((x2, y), mid, font=f, fill=RED)
            d.text((x2 + f.getlength(mid), y), post, font=f, fill=WHITE)
        else:
            d.text((x, y), l, font=f, fill=WHITE)
    return img, size, line_h, (top, top + total)


if __name__ == '__main__':
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    out, src = a[0], a[1]
    n = int(opt('--lines', '1'))
    lines = [TEXT] if n == 1 else ['취미가 있는', '사람']
    if '--text' in a:
        lines = [opt('--text', TEXT)]
    box = tuple(int(v) for v in opt('--box', '').split(',')) if '--box' in a else None
    img = fill_photo(src, box)
    size = int(opt('--size', '0')) or None
    if size is None and '--text' in a:
        size = min(262, fit_size(lines))          # 짧은 문구는 채널 틀의 한 단어 크기(262px)까지
    img, size, lh, span = put_text(img, lines, float(opt('--cy', '360')), opt('--red', None), size=size)
    img.save(out, quality=93)
    print(out, f'font {size}px, ink height {lh}px, text y {span[0]:.0f}-{span[1]:.0f}')
