# Photos the owner sent for v2 (2026-10-24): "심리학자 존 볼비 연구팀은" and "행동경제학자 댄 애리얼리는" show these
# instead of the profile icon ("뒷 배경 사진을 첨부한 사진으로 넣어줘", "첨부한 두번째 사진을 배경으로 써주셈").
# The files are small (646x475, 560x373): stretched over 1920x1080 they would be 3x enlarged and soft, so each is
# placed whole in the middle at about 1.7x, on a blurred, darkened copy of itself that fills the 16:9 frame.
# The owner's photos are not committed (rights stay with the owner); the output goes to work/img/.
# usage: make_photos_v2.py bowlby.png ariely.png out_dir
import sys
from PIL import Image, ImageEnhance, ImageFilter

W, H = 1920, 1080


def compose(src, out, height=820, y_mid=0.47):
    im = Image.open(src).convert("RGB")
    w, h = im.size
    k = max(W / w, H / h)                                   # background: cover the frame, blur, darken
    bg = im.resize((round(w * k), round(h * k)), Image.LANCZOS)
    x0, y0 = (bg.width - W) // 2, (bg.height - H) // 2
    bg = bg.crop((x0, y0, x0 + W, y0 + H)).filter(ImageFilter.GaussianBlur(28))
    bg = ImageEnhance.Brightness(bg).enhance(0.38)
    fg = im.resize((round(w * height / h), height), Image.LANCZOS)
    bg.paste(fg, ((W - fg.width) // 2, round(H * y_mid - height / 2)))
    bg.save(out)
    print(out, fg.size)


compose(sys.argv[1], f"{sys.argv[3]}/bowlby_v2.png")
compose(sys.argv[2], f"{sys.argv[3]}/ariely_v2.png")
