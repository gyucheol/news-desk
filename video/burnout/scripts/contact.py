# Contact sheet: grab frames at given times from a video and tile them with time labels.
# usage: contact.py video.mp4 out.png t1,t2,... [cols]
import io, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
v, out, ts = sys.argv[1], sys.argv[2], [float(x) for x in sys.argv[3].split(",")]
cols = int(sys.argv[4]) if len(sys.argv) > 4 else 3
tw, th = 640, 360
ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
font = ImageFont.truetype(f"{ROOT}/fonts/Pretendard-Bold.otf", 28)
rows = (len(ts) + cols - 1) // cols
sheet = Image.new("RGB", (cols * tw, rows * (th + 40)), (40, 40, 40))
for i, t in enumerate(ts):
    png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t}", "-i", v, "-frames:v", "1", "-f", "image2pipe", "-vcodec", "png", "-"],
                         capture_output=True, check=True).stdout
    im = Image.open(io.BytesIO(png)).convert("RGB").resize((tw, th), Image.LANCZOS)
    x, y = (i % cols) * tw, (i // cols) * (th + 40)
    sheet.paste(im, (x, y + 40))
    ImageDraw.Draw(sheet).text((x + 10, y + 4), f"{t:.2f}s", font=font, fill=(255, 220, 90))
sheet.save(out); print(out)
