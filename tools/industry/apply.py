"""산업 페이지 결과를 검사하고 DB에 쓸 파일을 만든다.
사용: python3 -I tools/industry/apply.py <작업 폴더(out/·intro/ 포함)> <DB 사본 폴더> <오늘 YYYY-MM-DD>
- out/<id>.json: 새 산업 페이지(그대로 set). intro/<id>.json: 기존 페이지에 더할 입문(update: intro + history 한 줄).
결과: <작업 폴더>/save/<id>.json, 문제 목록 출력(PROBLEMS n). DB에 쓰지 않는다."""
import json, glob, os, re, sys
W, DB, TODAY = sys.argv[1:4]
P = []
def has_src(x): return all(s.get('o') and s.get('u') for s in x.get('src', []))
def check_intro(i, it):
    if not isinstance(it, dict): P.append(f'{i} intro 없음'); return
    for k in ('what', 'money', 'drivers'):
        if not (it.get(k) or '').strip(): P.append(f'{i} intro.{k} 없음')
    for k, lo, hi in (('watch', 3, 6), ('players', 4, 9), ('reading', 3, 6), ('terms', 2, 8)):
        n = len(it.get(k) or [])
        if not lo <= n <= hi: P.append(f'{i} intro.{k} {n}개')
    for r in it.get('reading') or []:
        if not r.get('news') or not r.get('means'): P.append(f'{i} intro.reading 빈 칸')
    for s in [it.get('what', ''), it.get('money', ''), it.get('drivers', '')] + [r.get('means', '') for r in it.get('reading') or []]:
        if '{{' in s or '}}' in s: P.append(f'{i} intro 강조 표시 남음(10월 15일부터 강조 안 씀)')
os.makedirs(f'{W}/save', exist_ok=True)
orders = {}
for f in sorted(glob.glob(f'{W}/out/*.json')):
    i = os.path.basename(f)[:-5]
    try: c = json.load(open(f))
    except Exception as e: P.append(f'{i} json {e}'); continue
    if c.get('id') != i: P.append(f'{i} id 다름 {c.get("id")}')
    for k in ('name', 'short', 'icon', 'summary'):
        if not c.get(k): P.append(f'{i} {k} 없음')
    if len(c.get('short', '')) > 6: P.append(f'{i} short {len(c["short"])}자')
    if c.get('order') in orders.values(): P.append(f'{i} order 겹침 {c.get("order")}')
    orders[i] = c.get('order')
    ids = [n.get('id') for n in c.get('nodes', [])]
    if not 4 <= len(ids) <= 10: P.append(f'{i} 노드 {len(ids)}개')
    if len(set(ids)) != len(ids): P.append(f'{i} 노드 id 중복')
    for n in c.get('nodes', []):
        if not re.fullmatch(r'[a-z][a-z0-9]{1,11}', n.get('id') or ''): P.append(f'{i} 노드 id {n.get("id")}')
        if not n.get('name') or not n.get('role'): P.append(f'{i} 노드 {n.get("id")} 이름·역할 없음')
        for l in n.get('links', []):
            if l.get('to') and '/' not in l['to']: P.append(f'{i} links {l["to"]}')
        for s in n.get('state', []):
            if not s.get('u'): P.append(f'{i} 노드 {n.get("id")} state 주소 없음')
    cy = c.get('cycle') or {}
    if cy.get('stage') not in range(1, 9): P.append(f'{i} cycle.stage {cy.get("stage")}')
    if cy.get('conf') not in ('높음', '중간', '낮음'): P.append(f'{i} cycle.conf {cy.get("conf")}')
    if not 2 <= len(cy.get('why') or []) <= 5: P.append(f'{i} cycle.why {len(cy.get("why") or [])}줄')
    for w in cy.get('why') or []:
        if not w.get('src') or not has_src(w): P.append(f'{i} cycle.why 출처')
    for sp in cy.get('split') or []:
        for nd in sp.get('nodes', []):
            if nd not in ids: P.append(f'{i} split 노드 {nd}')
    for s in c.get('industryState') or []:
        if not s.get('u'): P.append(f'{i} industryState 주소 없음')
    check_intro(i, c.get('intro'))
    c['insight'] = c.get('insight') or {}; c['flows'] = c.get('flows') or []
    c['asOf'] = c.get('asOf') or TODAY; c['rev'] = TODAY
    json.dump(c, open(f'{W}/save/{i}.json', 'w'), ensure_ascii=False)
for f in sorted(glob.glob(f'{W}/intro/*.json')):
    i = os.path.basename(f)[:-5]
    try: x = json.load(open(f))
    except Exception as e: P.append(f'{i} intro json {e}'); continue
    base = f'{DB}/chains/{i}.json'
    if not os.path.exists(base): P.append(f'{i} 기존 페이지 없음'); continue
    check_intro(i, x.get('intro'))
    old = json.load(open(base))
    hist = (old.get('history') or []) + [{'rev': TODAY, 'note': '입문 칸 추가(무엇을 팔고, 돈을 어디서 벌고, 무엇이 업황을 움직이고, 무엇을 보고, 뉴스를 어떻게 읽는지)'}]
    json.dump({'intro': x['intro'], 'history': hist}, open(f'{W}/save/{i}.json', 'w'), ensure_ascii=False)
    for m in x.get('missing') or []: print(f'  참고 {i} 노드 없음: {m.get("news", "")[:50]} → {m.get("suggest", "")}')
print('PROBLEMS', len(P))
for p in P: print(' -', p)
for f in sorted(glob.glob(f'{W}/save/*.json')): print(os.path.basename(f), os.path.getsize(f))
