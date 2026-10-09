"""재확인 결과(out/R*.json)를 문서에 반영해 newsdocs/에 쓴다. 사용: python3 -I apply.py <DB 사본 폴더> (이 폴더 안에서)"""
import json, glob, os, re, sys
DB = sys.argv[1]; P = []; n = 0
os.makedirs('newsdocs', exist_ok=True)
for f in glob.glob('newsdocs/*.json'): os.remove(f)
ids = [l.split('\t')[0] for l in open('../sm-2026-10-07-09/recheck_title.tsv') if l.strip()]
got = {}
for p in sorted(glob.glob('out/R*.json')):
    for x in json.load(open(p))['docs']: got[x['id']] = x
for i in ids:
    if i not in got: P.append(f'{i} 결과 없음'); continue
for i, x in got.items():
    d = json.load(open(f'{DB}/news/{i}.json'))
    if x.get('changed'):
        for k in ('title', 'one', 'facts', 'basis', 'check'):
            if x.get(k): d[k] = x[k]
        d['headline'] = d['title']
        hs = {s.get('u') for s in d.get('src', [])}
        d['src'] = d.get('src', []) + [s for s in x.get('src_add', []) if s.get('u') not in hs and 'bloomberg.com' not in s.get('u', '') and 'reuters.com' not in s.get('u', '')]
    one = re.sub(r' \(제목 기준\)$', '', d['one'])
    if d['basis'] == 'title' and one == d['one']: P.append(f'{i} title인데 꼬리 없음')
    if d['basis'] != 'title' and one != d['one']: P.append(f'{i} 꼬리 남음')
    lo, hi = (80, 135) if len(d.get('items') or []) <= 1 else (85, 165)
    if not lo <= len(one) <= hi: P.append(f'{i} 한줄 {len(one)}자')
    if not one.endswith('다'): P.append(f'{i} 끝맺음')
    if any('|' in s or '**' in s for s in d['facts']): P.append(f'{i} 기호')
    json.dump(d, open(f'newsdocs/{i}.json', 'w'), ensure_ascii=False, indent=1); n += 1
import collections
print('PROBLEMS', len(P)); [print(' ', p) for p in P]
print('docs', n, collections.Counter(json.load(open(f))['basis'] for f in glob.glob('newsdocs/*.json')))
