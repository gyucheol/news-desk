import json, glob, sys
d = sys.argv[1] if len(sys.argv) > 1 else 'db_after'; bad = 0; n = 0
for p in sorted(glob.glob('newsdocs/*.json')):
    i = p.split('/')[-1][:-5]; n += 1
    try: r = json.load(open(f'{d}/news/{i}.json'))
    except Exception: bad += 1; print('없음', i); continue
    if r != json.load(open(p)): bad += 1; print('다름', i)
print('checked', n, 'diff', bad)
