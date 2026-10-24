# Light up a phone screen in a generated image (no text on it), blend with SDXL img2img,
# and paste back only the area around the phone so everything else (e.g. a good hand) stays as is.
# Used for I02: the best composition had a dark phone, so the alarm did not read as an alarm.
# usage: screen_glow.py in.png out_prefix x0,y0,x1,y1 seed[,seed] [strength=0.45]
#   x0..y1: the screen inside the bezel, in source pixels
import os, sys, torch, numpy as np
from PIL import Image, ImageDraw, ImageFilter
from diffusers import StableDiffusionXLImg2ImgPipeline, DPMSolverSDEScheduler

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
src_path, out_prefix, box = sys.argv[1], sys.argv[2], [int(v) for v in sys.argv[3].split(",")]
seeds = [int(s) for s in sys.argv[4].split(",")]
strength = float(sys.argv[5]) if len(sys.argv) > 5 else 0.45
PROMPT = ("first-person view from bed in a dark bedroom at dawn, a hand in a navy knit sleeve reaching toward "
          "a smartphone alarm glowing brightly on the bedside table, cinematic photorealistic still, "
          "low-key lighting, muted navy, charcoal, beige and dark walnut, 35mm film look, soft film grain")
NEG = "text, letters, numbers, caption, logo, watermark, cartoon, drawing, render, blurry, deformed hands, extra fingers, bad anatomy"

src = Image.open(src_path).convert("RGB")
x0, y0, x1, y1 = box
sw, sh = x1 - x0, y1 - y0
# night lock-screen blue gradient + blurred "clock" pill + round stop button (no readable text)
g = np.linspace(0, 1, sh)[:, None, None]
arr = np.array([150, 172, 212]) * (1 - g) + np.array([78, 98, 146]) * g
screen = Image.fromarray(np.repeat(arr, sw, axis=1).astype(np.uint8))
d = ImageDraw.Draw(screen)
cx, cy, r = sw // 2, int(sh * 0.74), int(sw * 0.20)
d.ellipse([cx - r, cy - r, cx + r, cy + r], fill=(238, 242, 250))
d.rounded_rectangle([int(sw * 0.22), int(sh * 0.20), int(sw * 0.78), int(sh * 0.30)], radius=4, fill=(222, 230, 244))
screen = screen.filter(ImageFilter.GaussianBlur(1.2))
mask = Image.new("L", src.size, 0)
ImageDraw.Draw(mask).rounded_rectangle(box, radius=9, fill=255)
painted = src.copy()
layer = Image.new("RGB", src.size); layer.paste(screen, (x0, y0))
painted.paste(layer, (0, 0), mask.filter(ImageFilter.GaussianBlur(1.0)))
spill = np.asarray(mask.filter(ImageFilter.GaussianBlur(55)), np.float32)[..., None] / 255   # light on the table
painted = Image.fromarray(np.clip(np.asarray(painted, np.float32) + spill * np.array([120, 140, 180]) * 0.6, 0, 255).astype(np.uint8))

pipe = StableDiffusionXLImg2ImgPipeline.from_pretrained(f"{ROOT}/models/realvisxl5l", torch_dtype=torch.bfloat16,
                                                        variant="fp16", use_safetensors=True)
pipe.scheduler = DPMSolverSDEScheduler.from_config(pipe.scheduler.config, use_karras_sigmas=True)
pipe.set_progress_bar_config(disable=True)
torch.set_num_threads(os.cpu_count() or 4)
region = Image.new("L", src.size, 0)
ImageDraw.Draw(region).rounded_rectangle((x0 - 120, y0 - 110, x1 + 140, y1 + 90), radius=60, fill=255)
region = region.filter(ImageFilter.GaussianBlur(35))
for seed in seeds:
    with torch.inference_mode():
        res = pipe(prompt=PROMPT, negative_prompt=NEG, image=painted, strength=strength, num_inference_steps=10,
                   guidance_scale=1.5, generator=torch.Generator("cpu").manual_seed(seed)).images[0]
    out = src.copy(); out.paste(res.resize(src.size, Image.LANCZOS), (0, 0), region)
    p = f"{out_prefix}_s{seed}.png"; out.save(p); print(p, flush=True)
