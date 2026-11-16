# 스톡 장면 안내서: segments.json(시각·자막) + stock_ideas.py(찾을 그림) + 앞뒤 화면 -> stock/brief.json
import json, sys
sys.path.insert(0, '.')
from stock_ideas import IDEAS
sys.path.insert(0, '/home/user/news-desk/video/주식심리/살걸팔걸/marking')
from photos import DESC
num = json.load(open('/home/user/news-desk/video/주식심리/살걸팔걸/marking/marks.json', encoding='utf-8'))['num']
inv = {v: k for k, v in num.items()}
SEG = json.load(open('segments.json', encoding='utf-8'))['segs']
def desc(s):
    if s is None: return '영상 끝'
    if s['kind'] == 'P':
        n = int(s['value'][1:]); return f"사진 {n}번: {DESC[inv[n]]}"
    return f"스톡 {s['value']}"
out = []
for k, s in enumerate(SEG):
    if s['kind'] != 'S': continue
    out.append({'seg': s['value'], 'start': s['t0'], 'est_sec': s['dur'], 'text': s['text'],
                'centre_lines': f"{sum(1 for c in s['pos'] if c in 'ci')}/{len(s['pos'])}", 'idea': IDEAS[s['value']],
                'before': desc(SEG[k - 1] if k else None), 'after': desc(SEG[k + 1] if k + 1 < len(SEG) else None)})
json.dump(out, open('stock/brief.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
missing = [s['value'] for s in SEG if s['kind'] == 'S' and s['value'] not in IDEAS]
print(len(out), 'stock scenes ->', 'stock/brief.json', '| missing ideas:', missing, '| total', round(sum(o['est_sec'] for o in out), 1), 's')
