# Many scene images in one run with RealVisXL V5.0 Lightning on a CPU without AMX (2026-10-23).
#   gen.py needs AMX for bf16; without it bf16 is emulated (10+ min per image) and loading the whole pipeline in fp32
#   does not fit (this sandbox kills a process near 11 GB). Here the text encoders run first (fp32) for every prompt
#   and are freed; then the UNet is loaded, stored in bf16 and computed in fp32 layer by layer (diffusers layerwise
#   casting), and the VAE is loaded last. Loading happens once for the whole job list.
# usage: gen_batch.py jobs.json
#   jobs.json: [{"id": "A01", "seeds": [11, 12], "prompt": "...", "neg": "extra negative terms",
#                "size": "1344x768", "steps": 5, "cfg": 1.5}, ...]
# Output: work/img/<id>_s<seed>.png (existing files are skipped, so a stopped run can be restarted).
import gc, json, os, sys, time, torch
from diffusers import (AutoencoderKL, DDIMScheduler, DPMSolverSDEScheduler, StableDiffusionXLPipeline,
                       UNet2DConditionModel)

ROOT = os.environ.get("VIDEO_ROOT", os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
M = f"{ROOT}/models/realvisxl5l"
OUT = f"{ROOT}/work/img"
STYLE = ("photorealistic photo, natural light, realistic skin texture, muted colors, "
         "shallow depth of field, 35mm film look")
NEG = ("text, letters, words, caption, logo, watermark, signature, brand, celebrity, cartoon, anime, drawing, "
       "illustration, render, worst quality, low quality, blurry, deformed hands, bad hands, fused fingers, "
       "extra fingers, missing fingers, bad anatomy, deformed face")
torch.set_num_threads(os.cpu_count() or 4)
os.makedirs(OUT, exist_ok=True)
jobs = json.load(open(sys.argv[1]))
todo = [j for j in jobs if any(not os.path.exists(f"{OUT}/{j['id']}_s{s}.png") for s in j["seeds"])]
if not todo:
    sys.exit("nothing to do")
t0 = time.time()
# 1) prompts -> embeddings with the text encoders only
te = StableDiffusionXLPipeline.from_pretrained(M, unet=None, vae=None, torch_dtype=torch.float32, variant="fp16",
                                               use_safetensors=True)
emb = {}
with torch.inference_mode():
    for j in todo:
        cfg = j.get("cfg", 1.5)
        full = f"{j['prompt']}, {j.get('style', STYLE)}"
        n = len(te.tokenizer(full)["input_ids"])
        if n > 77:
            print(f"{j['id']}: prompt has {n} tokens, the part after 77 is cut off", flush=True)
        neg = NEG + (", " + j["neg"] if j.get("neg") else "")
        emb[j["id"]] = te.encode_prompt(prompt=full, negative_prompt=neg, device="cpu",
                                        do_classifier_free_guidance=cfg > 1.0)
del te; gc.collect()
print(f"prompts encoded {time.time() - t0:.0f}s", flush=True)
# 2) UNet + VAE in fp32
unet = UNet2DConditionModel.from_pretrained(M, subfolder="unet", torch_dtype=torch.float32, variant="fp16")
# weights stored in bf16 (half the memory), each layer upcast to fp32 just for its own computation: the whole UNet in
# fp32 (10.3 GB) plus sampling went over this sandbox's ~11 GB process limit and was killed (2026-10-23)
unet.enable_layerwise_casting(storage_dtype=torch.bfloat16, compute_dtype=torch.float32)
gc.collect()
vae = AutoencoderKL.from_pretrained(M, subfolder="vae", torch_dtype=torch.float32, variant="fp16")
pipe = StableDiffusionXLPipeline.from_pretrained(M, unet=unet, vae=vae, text_encoder=None, text_encoder_2=None,
                                                 tokenizer=None, tokenizer_2=None, torch_dtype=torch.float32,
                                                 variant="fp16", use_safetensors=True)
pipe.scheduler = DPMSolverSDEScheduler.from_config(DDIMScheduler.load_config(M, subfolder="scheduler"),
                                                   use_karras_sigmas=True)   # model card: DPM++ SDE Karras
pipe.set_progress_bar_config(disable=True)
pipe.vae.enable_tiling()                          # decode in tiles: the full-size fp32 decode peaked near the memory limit
print(f"models loaded {time.time() - t0:.0f}s", flush=True)
for j in todo:
    pe, npe, ppe, nppe = emb[j["id"]]
    W, H = (int(x) for x in j.get("size", "1344x768").split("x"))
    for seed in j["seeds"]:
        out = f"{OUT}/{j['id']}_s{seed}.png"
        if os.path.exists(out):
            continue
        t1 = time.time()
        with torch.inference_mode():
            img = pipe(prompt_embeds=pe, negative_prompt_embeds=npe, pooled_prompt_embeds=ppe,
                       negative_pooled_prompt_embeds=nppe, num_inference_steps=j.get("steps", 5),
                       guidance_scale=j.get("cfg", 1.5), width=W, height=H,
                       generator=torch.Generator("cpu").manual_seed(seed)).images[0]
        img.save(out)
        print(f"{out} {time.time() - t1:.0f}s", flush=True)
