"""산업 한 페이지 업데이트(UPDATE.md) 입력을 만든다: 산업마다 반영 안 된 뉴스 목록.
사용: python3 -I tools/industry/upd_prep.py <DB 사본 폴더> <작업 폴더> <처리일 하한 YYYY-MM-DD>
대상: meta/chainsLog.applied에 없는 문서, 또는 applied 날짜보다 processed가 뒤인 문서(기사를 더한 문서, upd=true). processed가 하한 이상인 것만.
산업: 문서의 inds와 vc[].ind. 결과: <작업 폴더>/news/<산업 id>.jsonl, 산업별 건수 출력."""
import json, glob, os, re, sys, collections
DB, W, SINCE = sys.argv[1:4]
app = json.load(open(f'{DB}/meta/chainsLog.json'))['applied']
# 2026-10-30 사용자 지시: 없앤 산업(fin·pharma)과, 읽음 처리한 다른 나라 매크로·긍정 AI 뉴스는 해당 산업 입력에서 뺌(tools/industry/skip_news.json)
_sk = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'skip_news.json')
SK = json.load(open(_sk)) if os.path.exists(_sk) else {}
REMOVED, SKIP = set(SK.get('removed_industries', [])), SK.get('skip', {})
pages = {os.path.basename(p)[:-5] for p in glob.glob(f'{DB}/chains/*.json')}
P = lambda s: re.sub(r'\{\{|\}\}', '', s or '')
out = collections.defaultdict(list)
for p in glob.glob(f'{DB}/news/*.json'):
    d = json.load(open(p))
    pr = (d.get('processed') or '')[:10]
    if pr < SINCE: continue
    if d['id'] in app and pr <= app[d['id']]: continue
    vc = d.get('vc') or []
    inds = set(d.get('inds') or []) | {v.get('ind') for v in vc if v.get('ind')}
    src = [{'o': it.get('o', ''), 'u': it.get('u', ''), 'd': it.get('d', '')} for it in (d.get('items') or [])][-3:] or [{'o': d.get('source', ''), 'u': d.get('url', ''), 'd': pr}]
    for i in inds:
        if i not in pages or i in REMOVED or i in SKIP.get(d['id'], []): continue
        out[i].append({'id': d['id'], 'd': pr, 'title': P(d.get('title')), 'one': P(d.get('one')), 'added': P(d.get('added')),
                       'facts': [P(f) for f in (d.get('facts') or [])[:4]], 'vc': [v for v in vc if v.get('ind') == i], 'src': src,
                       'upd': d['id'] in app})
os.makedirs(f'{W}/news', exist_ok=True)
for i in sorted(pages):
    rows = sorted(out.get(i, []), key=lambda r: (r['d'], r['id']))
    with open(f'{W}/news/{i}.jsonl', 'w') as f:
        for r in rows: f.write(json.dumps(r, ensure_ascii=False) + '\n')
    print(i, len(rows), sum(r['upd'] for r in rows))
