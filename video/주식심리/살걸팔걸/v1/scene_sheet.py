# 완성 영상에서 장면마다 가운데 시각의 프레임을 뽑아 번호와 함께 시트로(점검용). usage: scene_sheet.py video.mp4 outprefix
import json, subprocess, sys, os
from PIL import Image, ImageDraw, ImageFont
vid, pre = sys.argv[1], sys.argv[2]
tl = json.load(open('timeline.json'))
font = ImageFont.truetype('/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/fonts/NotoSansKR-VF.ttf', 18)
os.makedirs(pre + '_f', exist_ok=True)
tiles = []
for sc in tl['scenes']:
    t = (sc['start'] + sc['end']) / 2
    out = f"{pre}_f/{sc['id']}.jpg"
    subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', vid, '-frames:v', '1', '-vf', 'scale=384:-1', out])
    lab = (sc.get('note') or '')[:28]
    tiles.append((out, f"{sc['id']} {t:.1f}s {lab}"))
cols, per = 4, 24
for k in range(0, len(tiles), per):
    part = tiles[k:k + per]
    rows = (len(part) + cols - 1) // cols
    s = Image.new('RGB', (cols * 388, rows * 242), (15, 15, 15)); d = ImageDraw.Draw(s)
    for i, (f, lab) in enumerate(part):
        x, y = (i % cols) * 388, (i // cols) * 242
        if os.path.exists(f): s.paste(Image.open(f), (x, y + 22))
        d.text((x + 3, y + 1), lab, fill=(255, 230, 0), font=font)
    s.save(f'{pre}_{k // per + 1}.jpg', quality=82)
print(len(tiles), 'scenes')
