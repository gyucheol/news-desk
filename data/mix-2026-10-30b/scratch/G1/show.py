"""문서 요약 보기: python3 -I show.py <id> [<id> ...]  (items는 날짜·출처·제목만)"""
import json, sys
BASE = '/home/user/news-desk/work/live47/news/'
for i in sys.argv[1:]:
    try:
        d = json.load(open(BASE + i + '.json'))
    except FileNotFoundError:
        print('###', i, 'MISSING'); continue
    print('###', i, '|', d.get('key'), '| pub', (d.get('published') or '')[:16], '| proc', d.get('processed'), '| items', len(d.get('items') or []))
    print('T:', d.get('title'))
    print('ONE:', (d.get('one') or '').replace('\n', ' / '))
    for it in d.get('items') or []:
        print('  -', it.get('d'), '|', it.get('o'), '|', it.get('t'))
    print()
