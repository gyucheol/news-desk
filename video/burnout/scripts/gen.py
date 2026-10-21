# Scene images with RealVisXL V5.0 Lightning on CPU (bf16, about 2 min per image on 4 cores).
# usage: gen.py <image_id> <seed[,seed...]> "<scene prompt>" [steps=5] [cfg=1.5] [WxH=1344x768]
# env NEG_EXTRA: extra negative terms for this image (e.g. "alarm clock, two hands")
# Output: work/img/<image_id>_s<seed>.png. Keep scene prompt short: prompt + STYLE must fit 77 CLIP tokens.
import os, sys, time, torch
from diffusers import StableDiffusionXLPipeline, DPMSolverSDEScheduler

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# 장면 설계표 3-1의 기본 스타일 문구 (no text / no logo 는 부정 문구로 옮김)
STYLE = ("cinematic photorealistic still, low-key lighting, deep black background, "
         "muted color palette of navy, charcoal, beige and dark walnut wood, shallow depth of field, "
         "35mm film look, soft film grain")
# 3-1의 금지 문구 + 품질 문구
NEG = ("text, letters, caption, logo, watermark, signature, celebrity, cartoon, anime, drawing, render, "
       "worst quality, low quality, blurry, deformed hands, bad hands, fused fingers, extra fingers, "
       "missing fingers, bad anatomy, deformed face, gore, blood, medical")
if os.environ.get("NEG_EXTRA"):
    NEG += ", " + os.environ["NEG_EXTRA"]

torch.set_num_threads(os.cpu_count() or 4)
iid, seeds, prompt = sys.argv[1], [int(s) for s in sys.argv[2].split(",")], sys.argv[3]
steps = int(sys.argv[4]) if len(sys.argv) > 4 else 5
cfg = float(sys.argv[5]) if len(sys.argv) > 5 else 1.5
W, H = (int(x) for x in (sys.argv[6] if len(sys.argv) > 6 else "1344x768").split("x"))
os.makedirs(f"{ROOT}/work/img", exist_ok=True)

t0 = time.time()
pipe = StableDiffusionXLPipeline.from_pretrained(f"{ROOT}/models/realvisxl5l", torch_dtype=torch.bfloat16,
                                                 variant="fp16", use_safetensors=True)
# model card: 5 steps, DPM++ SDE Karras, CFG 1.0-2.0
pipe.scheduler = DPMSolverSDEScheduler.from_config(pipe.scheduler.config, use_karras_sigmas=True)
pipe.set_progress_bar_config(disable=True)
full = f"{prompt}, {STYLE}"
print(f"load {time.time()-t0:.1f}s | prompt tokens {len(pipe.tokenizer(full)['input_ids'])}/77"
      f" | negative tokens {len(pipe.tokenizer(NEG)['input_ids'])}/77", flush=True)
for seed in seeds:
    t1 = time.time()
    g = torch.Generator("cpu").manual_seed(seed)
    with torch.inference_mode():
        img = pipe(prompt=full, negative_prompt=NEG, num_inference_steps=steps, guidance_scale=cfg,
                   width=W, height=H, generator=g).images[0]
    out = f"{ROOT}/work/img/{iid}_s{seed}.png"
    img.save(out)
    print(f"{out} {time.time()-t1:.1f}s", flush=True)
