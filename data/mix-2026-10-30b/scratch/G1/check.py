"""clusters_G1.json 검사: 줄 누락·중복, core 1~5개·15~45자, attachTo 존재, 큰 묶음부터, core 숫자 근거."""
import json, re, collections, os
B = '/home/user/news-desk/data/mix-2026-10-30b/'
NEWS = '/home/user/news-desk/work/live47/news/'
d = json.load(open(B + 'clusters_G1.json'))
keep = {int(l.split('\t')[0]): l.rstrip('\n').split('\t') for l in open(B + 'keep_G1.tsv')}
rows = {int(l.split('\t')[0]): l.rstrip('\n').split('\t') for l in open(B + 'all.tsv')}
ex = {l.split('\t')[1] for l in open(B + 'existing.tsv')}
FIELDS = set('fed macro rates geo trade energy power metals semis ai jpins tech auto aero agri consumer shipping realestate industrial other'.split())
P = []
seen = collections.Counter()
for c in d['clusters']:
    for n in c['lines']: seen[n] += 1
for x in d['drop']: seen[x['line']] += 1
miss = sorted(set(keep) - set(seen)); extra = sorted(set(seen) - set(keep)); dup = sorted(n for n, k in seen.items() if k > 1)
if miss: P.append(f'누락 {miss}')
if extra: P.append(f'keep에 없는 줄 {extra}')
if dup: P.append(f'중복 {dup}')
prev = 10**9
for i, c in enumerate(d['clusters'], 1):
    if c['cid'] != f'G1-{i:03d}': P.append(f"cid 순서 {c['cid']}")
    if len(c['lines']) > prev: P.append(f"{c['cid']} 큰 묶음부터 아님")
    prev = len(c['lines'])
    if not 1 <= len(c['core']) <= 5: P.append(f"{c['cid']} core {len(c['core'])}개")
    for x in c['core']:
        if not 15 <= len(x) <= 45: P.append(f"{c['cid']} core 길이 {len(x)}: {x}")
    if c['field'] not in FIELDS: P.append(f"{c['cid']} field {c['field']}")
    if c['attachTo'] and (c['attachTo'] not in ex or not os.path.exists(NEWS + c['attachTo'] + '.json')):
        P.append(f"{c['cid']} attachTo 없음 {c['attachTo']}")
    # core 숫자가 글이나 붙일 문서에 있는지
    src = ' '.join(rows[n][3] for n in c['lines'])
    if c['attachTo']:
        doc = json.load(open(NEWS + c['attachTo'] + '.json'))
        src += ' ' + (doc.get('title') or '') + ' ' + (doc.get('one') or '') + ' ' + ' '.join(doc.get('facts') or [])
    nums = lambda t: set(x.replace(',', '') for x in re.findall(r'\d+(?:[.,]\d+)*', t))
    lost = nums(' '.join(c['core'])) - nums(src)
    if lost: P.append(f"{c['cid']} core 숫자 근거 없음 {sorted(lost)}")
for x in d['drop']:
    m = re.match(r'이미 다룸\((n-[a-z]+-\d+)\)', x['reason'])
    if m and m.group(1) not in ex: P.append(f"drop {x['line']} 문서 없음 {m.group(1)}")
cl = d['clusters']
print('keep 줄', len(keep), '| 묶음', len(cl), '| 1건짜리', sum(len(c['lines']) == 1 for c in cl),
      '| attachTo', sum(bool(c['attachTo']) for c in cl), '| 새 문서', sum(not c['attachTo'] for c in cl),
      '| 묶인 줄', sum(len(c['lines']) for c in cl), '| drop', len(d['drop']))
print('문제', len(P))
for p in P: print(' -', p)
