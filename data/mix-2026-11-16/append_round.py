"""11월 17일 추가분: work/sm25·dump25의 새 글을 all.tsv 뒤에 이어 붙이고 거르기 입력 in/F4~F6.tsv를 만든다(번호는 289부터).
사용: python3 -I append_round.py <거르기 에이전트 수>"""
import json, glob, os, re, sys
R = '/home/user/news-desk'; W = f'{R}/data/mix-2026-11-16'
seen = set(open(f'{R}/work/seen_urls.txt').read().split())
old = [l.rstrip('\n').split('\t') for l in open(f'{W}/all.tsv')]
have = {r[-1] for r in old}
prev = set()
for pp in ['mix-2026-11-02', 'mix-2026-11-02b']:
    prev |= {l.rstrip('\n').split('\t')[-1] for l in open(f'{R}/data/{pp}/all.tsv')}
clean = lambda s: re.sub(r'\s+', ' ', s).strip()
rows = []
for l in open(f'{R}/work/sm25/bbg.txt'):
    if l.startswith('#'): continue
    p = l.rstrip('\n').split('\t'); u = p[-1]
    if u in seen or u in have or u in prev: continue
    title = p[3] if p[3].strip() else re.sub(r'-', ' ', u.rstrip('/').rsplit('/', 1)[-1])
    rows.append(['bbg', p[1], clean(title), u])
if os.path.exists(f'{R}/work/sm25/fed.txt'):
    for l in open(f'{R}/work/sm25/fed.txt'):
        p = l.rstrip('\n').split('\t')
        if len(p) < 5 or p[4] in seen or p[4] in have or p[4] in prev: continue
        rows.append(['fed:' + p[1], p[0][5:16], clean((p[2] + ': ' if p[2] else '') + p[3]), p[4]])
for f in glob.glob(f'{R}/work/dump25/*.jsonl'):
    ch = os.path.basename(f)[:-6]
    o = f'{R}/work/dump24/{ch}.jsonl'
    mx = max((json.loads(l)['id'] for l in open(o)), default=0) if os.path.exists(o) else 0
    for l in open(f):
        d = json.loads(l); u = f'https://t.me/{ch}/{d["id"]}'
        if d['id'] <= mx or not d['x'].strip() or u in seen or u in have: continue
        rows.append(['tg:' + ch, d['t'][5:10] + ' ' + d['t'][11:16], clean(d['x']), u])
rows.sort(key=lambda r: (r[1], r[3]))
start = len(old) + 1
with open(f'{W}/all.tsv', 'a') as o:
    for i, r in enumerate(rows, start): o.write('\t'.join([str(i)] + r) + '\n')
k = int(sys.argv[1]); sz = -(-len(rows) // k)
for j in range(k):
    with open(f'{W}/in/F{j + 4}.tsv', 'w') as o:
        for i, r in enumerate(rows[j * sz:(j + 1) * sz], start + j * sz):
            o.write('\t'.join([str(i), r[0], r[1], r[2][:260], r[3]]) + '\n')
import collections
print('appended', len(rows), 'from', start, collections.Counter(r[0] for r in rows))
