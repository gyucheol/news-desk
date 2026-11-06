# 고른 스톡 영상 점검 시트 (살걸·팔걸 편, 2026-11-06). 장면마다 쓰는 구간의 처음, 가운데, 끝 프레임을 한 줄에 놓음.
# 렌더링 전에 얼굴, 글자, 상표, 컷 전환, 앞뒤 장면과 비슷한 그림이 없는지 눈으로 보기 위함.
# usage: pick_sheet.py OUT_PREFIX [SEG ...]   (salgeol/v1에서, scratchpad venv python -I) -> OUT_PREFIX_1.jpg, _2.jpg ...
import glob, json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

out_prefix, only = sys.argv[1], set(sys.argv[2:])
picks = {}
for p in sorted(glob.glob('stock/picks/group_*.json')):
    for x in json.load(open(p, encoding='utf-8')):
        picks[x['seg']] = x
ovr = json.load(open('stock_overrides.json', encoding='utf-8')) if os.path.exists('stock_overrides.json') else {}
brief = json.load(open('stock/brief.json', encoding='utf-8'))
font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 22)
TW, TH, LW = 384, 216, 150
rows = []
for b in brief:
    s = b['seg']
    if only and s not in only:
        continue
    pk = dict(picks.get(s, {}))
    pk.update(ovr.get(s, {}))
    if not pk.get('id'):
        rows.append((s, None, 'no pick', []))
        continue
    src = f"stock/full/{pk['id']}.mp4"
    use = min(float(pk.get('use', b['est_sec'] + 0.5)), float(pk.get('clip_len', 99)) - float(pk.get('in', 0)))
    t0 = float(pk.get('in', 0))
    ims = []
    for t in (t0 + 0.15, t0 + use / 2, t0 + use - 0.15):
        tmp = f'/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/_ps_{s}_{len(ims)}.jpg'
        subprocess.run(['ffmpeg', '-v', 'error', '-y', '-ss', f'{t:.2f}', '-i', src, '-frames:v', '1', '-vf', f'scale={TW}:{TH}', tmp], check=True)
        ims.append(Image.open(tmp).convert('RGB'))
        os.remove(tmp)
    rows.append((s, pk['id'], f"in {t0:g} use {use:.2f}", ims))
PER = 10
for n in range(0, len(rows), PER):
    part = rows[n:n + PER]
    sheet = Image.new('RGB', (LW + 3 * TW, TH * len(part)), (20, 20, 20))
    d = ImageDraw.Draw(sheet)
    for r, (s, i, info, ims) in enumerate(part):
        y = r * TH
        d.text((8, y + 10), s, font=font, fill=(255, 230, 120))
        d.text((8, y + 44), str(i), font=font, fill=(230, 230, 230))
        d.text((8, y + 78), info, font=ImageFont.truetype(font.path, 15), fill=(180, 180, 180))
        for k, im in enumerate(ims):
            sheet.paste(im, (LW + k * TW, y))
    sheet.save(f'{out_prefix}_{n // PER + 1}.jpg', quality=82)
    print(f'{out_prefix}_{n // PER + 1}.jpg', [p[0] for p in part])
