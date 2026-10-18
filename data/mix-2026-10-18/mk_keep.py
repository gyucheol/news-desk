"""거르기 결과(out/F*.tsv) → keep.tsv(묶기 입력), DB 사본 → existing.tsv(10월 6일 이후 문서). 사용: python3 -I mk_keep.py <DB 사본>"""
import json, glob, sys, collections, re
DB = sys.argv[1]
rows = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open('all.tsv')}
K, D, n = [], collections.Counter(), 0
for f in sorted(glob.glob('out/F*.tsv')):
    for l in open(f):
        p = l.rstrip('\n').split('\t')
        if len(p) < 3: continue
        n += 1
        if p[1] == 'K': K.append((int(p[0]), p[2]))
        else: D[p[2]] += 1
miss = set(rows) - {str(k) for k, _ in K} - {l.split('\t')[0] for f in glob.glob('out/F*.tsv') for l in open(f) if l.split('\t')[1:2] == ['D']}
with open('keep.tsv', 'w') as o:
    for k, fld in sorted(K):
        r = rows[str(k)]; o.write('\t'.join([str(k), fld, r[1], r[2], re.sub(r'\s+', ' ', r[3])[:400], r[4]]) + '\n')
ex = []
for p in glob.glob(f'{DB}/news/*.json'):
    d = json.load(open(p))
    if not d.get('one'): continue
    day = (d.get('published') or d.get('processed') or '')[:10]
    if day < '2026-10-06': continue
    ex.append((day, d['id'], d.get('source', ''), re.sub(r'\{\{|\}\}', '', d.get('title', '')), str(len(d.get('items') or []) or 1)))
open('existing.tsv', 'w').write(''.join('\t'.join(x) + '\n' for x in sorted(ex)))
print('judged', n, 'of', len(rows), 'K', len(K), 'D', sum(D.values()), dict(D.most_common()), '| missing', len(miss), '| existing', len(ex))
