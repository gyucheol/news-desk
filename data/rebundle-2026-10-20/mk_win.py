"""1단계 묶음(clusters/G*.json)을 검사하고 2단계 작성 입력(win/W*.json)을 만든다.
사용: python3 -I mk_win.py <DB 사본> [묶음 수 상한=60]
결과: plan.json(묶음별 처리: keep(그대로)·write), win/W01.json …"""
import json, glob, re, sys, os, collections
DB = sys.argv[1]; CAP = int(sys.argv[2]) if len(sys.argv) > 2 else 60
lines = json.load(open('lines.json'))
cl = []
for p in sorted(glob.glob('clusters/G*.json')): cl += json.load(open(p))
m = [k for c in cl for k in c['m']]
miss, dup = set(lines) - set(m), len(m) - len(set(m))
assert not miss and not dup and not set(m) - set(lines), (len(miss), dup)
assert len({c['c'] for c in cl}) == len(cl)
clean = lambda s: re.sub(r'\s+', ' ', (s or '').replace('{{', '').replace('}}', '')).strip()
docitems = collections.Counter(x['doc'] for x in lines.values())
plan = []
for c in cl:
    c['m'] = sorted(c['m'], key=lambda k: (lines[k]['d'], k))
    docs = collections.Counter(lines[k]['doc'] for k in c['m'])
    same = len(docs) == 1 and docitems[next(iter(docs))] == len(c['m']) == 1
    plan.append({'c': c['c'], 'theme': c['theme'], 'core': c['core'], 'm': c['m'], 'docs': [d for d, _ in docs.most_common()], 'mode': 'keep' if same else 'write'})
json.dump(plan, open('plan.json', 'w'), ensure_ascii=False, indent=0)
W = [p for p in plan if p['mode'] == 'write']
print('묶음', len(plan), '그대로', len(plan) - len(W), '작성', len(W), '1건짜리', sum(len(p['m']) == 1 for p in plan), '작성 기사', sum(len(p['m']) for p in W))
def docctx(i):
    d = json.load(open(f'{DB}/news/{i}.json'))
    src = [{'k': f'{i}#S{j+1}', 'o': s.get('o', ''), 'd': s.get('d', ''), 'u': s.get('u', '')} for j, s in enumerate(d.get('src') or [])]
    x = {'title': clean(d.get('title') or d.get('headline')), 'one': clean(d.get('one')), 'facts': [clean(f) for f in d.get('facts') or []],
         'check': clean(d.get('check')), 'basis': d.get('basis', ''), 'src': src, 'inds': d.get('inds', []), 'nodes': d.get('nodes', []), 'vc': d.get('vc', [])}
    if d.get('fed'): x['fed'] = d['fed']
    return x
# 같은 원 문서의 묶음끼리 모아 작성 파일을 나눈다
W.sort(key=lambda p: (p['docs'][0], p['c']))
chunks, cur, curi = [], [], 0
for p in W:
    if cur and (len(cur) >= CAP or curi + len(p['m']) > 130):
        chunks.append(cur); cur, curi = [], 0
    cur.append(p); curi += len(p['m'])
if cur: chunks.append(cur)
os.makedirs('win', exist_ok=True)
for f in glob.glob('win/*.json'): os.remove(f)
for n, ch in enumerate(chunks, 1):
    ds = sorted({d for p in ch for d in p['docs']})
    out = {'docs': {i: docctx(i) for i in ds}, 'clusters': []}
    for p in ch:
        its = [{'t': lines[k]['t'], 'o': lines[k]['o'], 'd': lines[k]['d'], 's': lines[k]['s'], 'u': lines[k]['u']} for k in p['m']]
        out['clusters'].append({'c': p['c'], 'theme': p['theme'], 'core': p['core'], 'docs': p['docs'], 'items': its})
    json.dump(out, open(f'win/W{n:02d}.json', 'w'), ensure_ascii=False, indent=1)
    print(f'W{n:02d}', len(ch), '묶음', sum(len(p['m']) for p in ch), '기사', len(ds), '문서', os.path.getsize(f'win/W{n:02d}.json') // 1024, 'KB')
