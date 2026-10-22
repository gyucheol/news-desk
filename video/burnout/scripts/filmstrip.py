# One row per clip: N frames evenly spaced, labeled with id and time (to choose in/out points).
# usage: filmstrip.py out.png N clip1.mp4 clip2.mp4 ...
import io, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont
out, n, clips = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
f = ImageFont.truetype(f"{ROOT}/fonts/Pretendard-Bold.otf", 18)
tw, th, lab = 256, 144, 26
sheet = Image.new("RGB", (n * tw, len(clips) * (th + lab)), (30, 30, 30))
d = ImageDraw.Draw(sheet)
for r, c in enumerate(clips):
    dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", c],
                               capture_output=True, text=True).stdout or 0)
    for k in range(n):
        t = dur * (k + 0.5) / n
        png = subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", c, "-frames:v", "1", "-f", "image2pipe",
                              "-vcodec", "png", "-"], capture_output=True).stdout
        try:
            im = Image.open(io.BytesIO(png)).convert("RGB").resize((tw, th))
        except Exception:
            im = Image.new("RGB", (tw, th), (80, 0, 0))
        sheet.paste(im, (k * tw, r * (th + lab) + lab))
        d.text((k * tw + 4, r * (th + lab) + 3), f"{os.path.basename(c)[:-4]}  {t:.1f}s / {dur:.1f}", font=f, fill=(255, 215, 80))
sheet.save(out); print(out)
