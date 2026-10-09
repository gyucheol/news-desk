"""news-insight 결과 파일(data/insight/<id>.json) 형식 검사. 사용: python3 -I tools/insight/check.py <파일> [뉴스 문서 파일 — 주면 원문이 모두 반영됐는지도 본다]
페이지(desk/parts/js2.js blocksHtml)가 그리는 블록 종류와 필드만 허용한다. 문제가 없으면 'OK'만 찍는다."""
import json, re, sys

TEXT = {'h3', 'h4', 'lead', 'p', 'dim', 'callout'}
LIST = {'pts', 'num', 'src', 'chain'}
P = []

def s_ok(where, t):
    if not isinstance(t, str) or not t.strip(): P.append(f'{where}: 빈 글'); return
    if '**' in t: P.append(f'{where}: ** 금지')

def blocks(where, bs):
    if not isinstance(bs, list) or not bs: P.append(f'{where}: blocks 없음'); return
    for i, b in enumerate(bs):
        w = f'{where}[{i}]'; k = b.get('k') if isinstance(b, dict) else None
        if k in TEXT: s_ok(w, b.get('t'))
        elif k in LIST:
            if not b.get('items'): P.append(f'{w} {k}: items 없음')
            for x in b.get('items', []): s_ok(w, x)
        elif k == 'vc':
            for c in b.get('cols', []):
                s_ok(w, c.get('h'))
                for x in c.get('items', []): s_ok(w, x if isinstance(x, str) else x.get('t'))
        elif k == 'seg':
            for x in b.get('items', []): [s_ok(w, x.get(f)) for f in ('nm', 'stage', 'why')]
        elif k == 'hyps':
            for x in b.get('items', []):
                s_ok(w, x.get('h'))
                if not x.get('kv'): P.append(f'{w} hyps: kv 없음')
        elif k == 'verdict':
            for x in b.get('items', []): s_ok(w, x.get('h')); s_ok(w, x.get('t'))
        elif k in ('cmp', 'series'):
            for x in b.get('items', []):
                if not (isinstance(x, list) and len(x) == 2): P.append(f'{w} {k}: [왼쪽, 오른쪽] 꼴 아님')
        elif k == 'picks':
            for x in b.get('items', []): [s_ok(w, x.get(f)) for f in ('k', 'n', 't')]
        elif k == 'co':
            s_ok(w, b.get('name'))
            for j, p in enumerate(b.get('parts', [])): s_ok(w, p.get('h')); blocks(f'{w}.parts[{j}]', p.get('blocks'))
        else: P.append(f'{w}: 모르는 블록 {k!r}')

d = json.load(open(sys.argv[1], encoding='utf-8'))
if not re.match(r'^n-[a-z]+-\d{4}$', d.get('id', '')): P.append('id')
det, ins = d.get('detail') or {}, d.get('insight2') or {}
for nm, x in (('detail', det), ('insight2', ins)):
    if not re.match(r'^\d{4}-\d{2}-\d{2}$', x.get('updated', '')): P.append(f'{nm}.updated')
blocks('detail', det.get('blocks'))
ids = [p.get('id') for p in ins.get('parts', [])]
if ids != ['structure', 'flip', 'picks']: P.append(f'insight2.parts id 순서 {ids}')
for p in ins.get('parts', []):
    for f in ('tag', 'title'): s_ok(f'insight2.{p.get("id")}.{f}', p.get(f))
    blocks(f'insight2.{p.get("id")}', p.get('blocks'))
# 원문 목록(items)이 여러 건인 뉴스는 자세한 정리에 원문 주소가 모두 들어가야 한다(사용자 지시: 원문을 모두 반영)
if len(sys.argv) > 2:
    nd = json.load(open(sys.argv[2], encoding='utf-8')); nd = nd.get('data', nd) if isinstance(nd.get('data'), dict) else nd
    its = nd.get('items') or []
    if len(its) > 1:
        txt = json.dumps(det, ensure_ascii=False)
        miss = [it.get('u', '') for it in its if it.get('u') and it['u'] not in txt]
        if miss: P.append(f'원문 {len(its)}건 중 {len(miss)}건이 자세한 정리에 없음: ' + ', '.join(miss[:5]))
        if not any(b.get('k') == 'h3' and '원문' in b.get('t', '') for b in det.get('blocks', [])): P.append("'원문 N건 핵심' 절 없음")
print('OK' if not P else '\n'.join(['PROBLEMS ' + str(len(P))] + P[:60]))
sys.exit(1 if P else 0)
