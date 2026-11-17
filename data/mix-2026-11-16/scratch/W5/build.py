"""W5 출력 조립: python3 -I build.py  (p1.py, p2.py ... 를 차례로 읽어 out2/W5.json 저장)"""
import json, os
D = '/home/user/news-desk/data/mix-2026-11-16/scratch/W5'
OUT = '/home/user/news-desk/data/mix-2026-11-16/out2/W5.json'
items, skipped = [], []
for n in range(1, 10):
    f = f'{D}/p{n}.py'
    if not os.path.exists(f): continue
    g = {}
    exec(open(f, encoding='utf-8').read(), g)
    items += g.get('ITEMS', []); skipped += g.get('SKIPPED', [])
O = {"agent": "W5", "searches_used": 16, "fetches_used": 0, "items": items, "skipped": skipped}
json.dump(O, open(OUT, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('saved', len(items), 'items', len(skipped), 'skipped')
