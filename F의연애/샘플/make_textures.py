# 샘플용 종이 질감·필름 그레인 이미지를 tex/ 폴더에 다시 만듭니다. (python3 make_textures.py)
import os
import numpy as np
from PIL import Image, ImageFilter
os.makedirs('tex', exist_ok=True)
rng = np.random.default_rng(7)
W, H = 1920, 1080
low = Image.fromarray((rng.random((H // 16, W // 16)) * 255).astype(np.uint8)).resize((W, H), Image.BICUBIC).filter(ImageFilter.GaussianBlur(30))
low = (np.asarray(low, np.float32) / 255 - 0.5) * 14
fine = (rng.random((H, W)) - 0.5) * 7
fib = Image.fromarray((rng.random((H, W)) > 0.9985).astype(np.uint8) * 255).filter(ImageFilter.GaussianBlur(0.8))
fib = np.asarray(fib, np.float32) / 255 * -18
paper = np.zeros((H, W, 3), np.float32); paper[:] = (236, 232, 223); paper += (low + fine + fib)[..., None]
Image.fromarray(np.clip(paper, 0, 255).astype(np.uint8)).save('tex/paper.png')
dark = np.zeros((H, W, 3), np.float32); dark[:] = (28, 28, 28); dark += (low * 0.8 + fine * 0.8)[..., None]
Image.fromarray(np.clip(dark, 0, 255).astype(np.uint8)).save('tex/dark.png')
for k in range(4):
    n = rng.normal(128, 40, (H // 2, W // 2)).clip(0, 255).astype(np.uint8)
    a = Image.fromarray(n).resize((W, H), Image.NEAREST)
    Image.merge('RGBA', (a, a, a, Image.new('L', (W, H), 255))).save(f'tex/grain{k}.png')
