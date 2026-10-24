# Remove the background and keep only the person (for thumbnails: "배경을 지우고 사람만 남긴 버전", 2026-10-22).
# Uses rembg (MIT) with the BiRefNet portrait model (MIT, about 970 MB, downloaded once to models/rembg/).
# usage: cutout.py IN.png OUT.png [--model birefnet-portrait]
# Output: RGBA PNG (transparent background), same size as the input. thumb.py photo accepts it directly.
import os, sys, time

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ.setdefault("U2NET_HOME", f"{ROOT}/models/rembg")
from PIL import Image
from rembg import new_session, remove

a = sys.argv[1:]
src, dst = a[0], a[1]
model = a[a.index("--model") + 1] if "--model" in a else "birefnet-portrait"
t0 = time.time()
session = new_session(model)
out = remove(Image.open(src).convert("RGB"), session=session)
out.save(dst)
alpha = out.getchannel("A")
print(f"{dst} model={model} person bbox={alpha.point(lambda v: 255 if v > 128 else 0).getbbox()} {time.time() - t0:.1f}s")
