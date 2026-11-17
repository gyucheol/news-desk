"""길이 보고: python3 -I lens.py  (out2/W5.json 의 각 필드 글자 수)"""
import json, os
H = '/home/user/news-desk/data/mix-2026-11-16'
O = json.load(open(f'{H}/out2/W5.json'))
TAIL = (' (제목 기준)', ' (채널 전언)')
def strip(s):
    for t in TAIL:
        if s.endswith(t): return s[:-len(t)]
    return s
for x in O['items']:
    print('==', x['cid'], 'title', len(x['title']), 'basis', x['basis'])
    for i, l in enumerate(strip(x['one']).split('\n')):
        print(f'  one{i+1} {len(l)}', '' if (i == 0 and 40 <= len(l) <= 90) or (i > 0 and 25 <= len(l) <= 90) else '<<')
    if x.get('added'): print('  added', len(strip(x['added'])), '' if 40 <= len(strip(x['added'])) <= 140 else '<<')
    for v in x.get('vc', []): print('  vc', len(v['t']), '' if 12 <= len(v['t']) <= 45 else '<<', v['t'])
    for it in x['items']:
        s = it.get('s')
        print('  item t', len(it['t']), '' if 25 <= len(it['t']) <= 60 else '<<', ('s %d' % len(strip(s)) + ('' if 45 <= len(strip(s)) <= 110 else ' <<')) if s else '')
    print('  facts', len(x['facts']))
