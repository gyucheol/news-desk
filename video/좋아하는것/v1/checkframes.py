# 03편 v1 점검용 프레임: 스톡 장면마다 가운데 한 장, 흐림 상자나 잘라내기가 있는 장면은 처음·가운데·끝 세 장을
# render.py --frames-only로 만들고(자막, 색, 흐림이 모두 들어간 실제 화면), 12장씩 묶어 시트로 만듭니다.
# usage: checkframes.py timeline.json outdir [scene_id,...]   (VIDEO_ROOT, SCRIPTS 환경변수 필요)
import json, os, subprocess, sys
from PIL import Image, ImageDraw, ImageFont

tl = json.load(open(sys.argv[1], encoding='utf-8'))
out = sys.argv[2]
only = set(sys.argv[3].split(',')) if len(sys.argv) > 3 else None
VR, SC = os.environ['VIDEO_ROOT'], os.environ['SCRIPTS']
os.makedirs(out, exist_ok=True)
items = []          # (time, label)
for s in tl['scenes']:
    if s['type'] != 'video' or (only and s['id'] not in only):
        continue
    a, b = s['start'], s['end']
    lab = s['id'] + ' ' + s.get('note', '')[:34]
    if s.get('blur_box') or s.get('crop') or (only and s['id'] in only):
        ts = [a + 0.35, (a + b) / 2, b - 0.35] if b - a > 1.2 else [(a + b) / 2]
    else:
        ts = [(a + b) / 2]
    for t in ts:
        items.append((round(t, 2), f"{lab} @{t:.2f}"))
items.sort()
B = 40                 # frames per render.py call (each keeps its decoders open until the end)
pngs = {}
for k in range(0, len(items), B):
    part = items[k:k + B]
    base = os.path.join(out, 'f.mp4')
    r = subprocess.run([os.path.join(VR, 'venv/bin/python'), os.path.join(SC, 'render.py'), sys.argv[1], base,
                        '--frames-only', ','.join(f"{t:.2f}" for t, _ in part)], capture_output=True, text=True,
                       cwd=VR, env=dict(os.environ, VIDEO_ROOT=VR))
    if r.returncode:
        print(r.stderr[-2000:]); sys.exit(1)
    for t, lab in part:
        pngs[(t, lab)] = base.replace('.mp4', f"_t{t:05.2f}.png")
font = ImageFont.truetype(os.path.join(VR, 'fonts/Pretendard-Bold.otf'), 22)
tw, th, cols, per = 640, 360, 3, 12
sheets = []
for n in range(0, len(items), per):
    grp = items[n:n + per]
    rows = (len(grp) + cols - 1) // cols
    sh = Image.new('RGB', (cols * tw, rows * (th + 34)), (40, 40, 40))
    d = ImageDraw.Draw(sh)
    for i, it in enumerate(grp):
        im = Image.open(pngs[it]).convert('RGB').resize((tw, th), Image.LANCZOS)
        x, y = (i % cols) * tw, (i // cols) * (th + 34)
        sh.paste(im, (x, y + 34))
        d.text((x + 6, y + 4), it[1], font=font, fill=(255, 220, 90))
    p = os.path.join(out, f"sheet_{n // per:02d}.jpg")
    sh.save(p, quality=82)
    sheets.append(p)
print(len(items), 'frames;', ' '.join(sheets))
