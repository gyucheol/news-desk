import json, sys
D = '/home/user/news-desk/work/live52/news/'
for i in sys.argv[1:]:
    d = json.load(open(D + i + '.json'))
    its = d.get('items') or []
    ds = [it.get('d', '') for it in its]
    print('=====', i, '| pub', (d.get('published') or '')[:16], '| proc', d.get('processed'), '| upd', (d.get('updatedAt') or '')[:16], '| n', len(its), '| dates', min(ds) if ds else '', '~', max(ds) if ds else '')
    print('TITLE:', d.get('title'))
    print('ONE:', (d.get('one') or '').replace('\n', ' / ')[:700])
    if d.get('added'): print('ADDED:', d.get('added')[:300])
    full = '-v' in sys.argv[0:1]
    for it in its:
        print('   ', it.get('d', ''), (it.get('o') or '')[:14], '|', (it.get('t') or '')[:90])
