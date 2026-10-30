"""문서 요약 보기: python3 -I show.py <id> ... (work/live14/news/<id>.json)"""
import json, re, sys
B = '/home/user/news-desk/work/live14/news/'
strip = lambda s: re.sub(r'\{\{|\}\}', '', s or '')
for i in sys.argv[1:]:
    try:
        d = json.load(open(B + i + '.json'))
    except Exception as e:
        print('##', i, 'ERR', e); continue
    print(f"## {i} [{(d.get('published') or '')[:10]}] {strip(d.get('title'))}")
    print('  one:', strip(d.get('one'))[:400])
    for f in d.get('facts', [])[:6]:
        print('  -', strip(f)[:220])
    for it in d.get('items', []):
        print(f"  * {it.get('d','')} {it.get('o','')}: {strip(it.get('t',''))[:150]}")
    print()
