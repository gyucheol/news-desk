import json, sys, os, glob, re
H = '/home/user/news-desk/data/multiline-2026-10-20'
I = json.load(open(f'{H}/in/M01.json'))
D = {}
for f in sorted(glob.glob(f'{H}/scratch/M01/b*.txt')):
    for blk in open(f, encoding='utf-8').read().strip().split('\n\n'):
        lines = blk.strip().split('\n')
        D[lines[0].strip()] = '\n'.join(l.strip().rstrip('.') for l in lines[1:])
TAIL = {'title': ' (제목 기준)', 'channel': ' (채널 전언)'}
out = []
for x in I:
    if x['id'] in D:
        one = D[x['id']] + TAIL.get(x['basis'], '')
        out.append({'id': x['id'], 'one': one})
json.dump(out, open(f'{H}/out/M01.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
# report lengths
for o in out:
    L = o['one'].split('\n')
    bad = [(k, len(l)) for k, l in enumerate(L) if (k == 0 and not 40 <= len(l) <= 90) or (k > 0 and not 25 <= len(l) <= 90)]
    if bad: print(o['id'], bad)
print('saved', len(out))
