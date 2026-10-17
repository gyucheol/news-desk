"""산업 한 페이지 업데이트(UPDATE.md) 변경분을 검사하고 기존 페이지에 합친다. DB에 쓰지 않는다.
사용: python3 -I tools/industry/upd_apply.py <작업 폴더> <DB 사본 폴더> <오늘 YYYY-MM-DD> [--check <산업 id>]
입력: <작업 폴더>/out/<id>.json(변경분), <작업 폴더>/news/<id>.jsonl(입력 뉴스), <DB>/chains/<id>.json, <DB>/meta/chainsLog.json
결과(--check가 아니면): <작업 폴더>/save/<id>.json(합친 전체 페이지), <작업 폴더>/save_meta/chainsLog.json, PROBLEMS n
합치는 규칙: 새 줄에 rev=오늘(데스크 NEW 표시). node.state는 노드마다 최근 4줄, industryState는 최근 6줄, cycle.flags는 최근 12줄만 남김.
cycle은 변경분이 있으면 통째로 바꿈(flags는 이어 붙임). insight는 변경분의 칸만 바꿈. 문서 크기 250,000바이트 이하."""
import json, glob, os, re, sys
W, DB, TODAY = sys.argv[1:4]
ONLY = sys.argv[5] if len(sys.argv) > 5 and sys.argv[4] == '--check' else None
TAG = re.compile(r'\[(사실|채널|제목|귀납|연역|유추|추측)[^\]]*\]\s*$')
KEYS = ('a', 'a1', 'a2', 'b', 'b1', 'b2', 'c', 'c1', 'd')
KINDS = ('price', 'supply', 'demand', 'capex', 'policy')
P = []

def txt(i, where, s, need_tag=True, lo=10, hi=400):
    s = s or ''
    if '{{' in s or '}}' in s or '**' in s: P.append(f'{i} {where} 강조 표시')
    if need_tag and not TAG.search(s): P.append(f'{i} {where} 꼬리표 없음')
    core = TAG.sub('', s).strip()
    if not lo <= len(core) <= hi: P.append(f'{i} {where} {len(core)}자')

def srcs(i, where, src):
    if not src: P.append(f'{i} {where} 출처 없음')
    for s in src or []:
        if not s.get('o') or not s.get('u'): P.append(f'{i} {where} 출처 o·u 빈 칸')

def merge(i, x, c, news_ids):
    nodes = {n['id']: n for n in c.get('nodes', [])}
    for nid, arr in (x.get('state') or {}).items():
        if nid not in nodes: P.append(f'{i} state 노드 {nid} 없음'); continue
        for s in arr:
            txt(i, f'state.{nid}', s.get('t'), lo=25, hi=180)
            if not s.get('u') or not s.get('o') or not s.get('d'): P.append(f'{i} state.{nid} d·o·u 빈 칸')
            if s.get('nid') and s['nid'] not in news_ids: P.append(f'{i} state.{nid} nid {s["nid"]} 입력에 없음')
            s['rev'] = TODAY
        n = nodes[nid]; n['state'] = sorted((n.get('state') or []) + arr, key=lambda s: s.get('d', ''))[-4:]
    if sum(len(v) for v in (x.get('state') or {}).values()) > 14: P.append(f'{i} state 14줄 넘음')
    for s in x.get('industryState') or []:
        txt(i, 'industryState', s.get('t'), lo=25, hi=220)
        if s.get('kind') not in KINDS: P.append(f'{i} industryState kind {s.get("kind")}')
        if not s.get('u') or not s.get('o'): P.append(f'{i} industryState o·u 빈 칸')
        s['rev'] = TODAY
    if len(x.get('industryState') or []) > 4: P.append(f'{i} industryState 4줄 넘음')
    c['industryState'] = sorted((c.get('industryState') or []) + (x.get('industryState') or []), key=lambda s: s.get('d', ''))[-6:]
    cy = x.get('cycle')
    old_cy = c.get('cycle') or {}
    if cy:
        if cy.get('stage') not in range(1, 9): P.append(f'{i} cycle.stage {cy.get("stage")}')
        if cy.get('conf') not in ('높음', '중간', '낮음'): P.append(f'{i} cycle.conf {cy.get("conf")}')
        if not 2 <= len(cy.get('why') or []) <= 5: P.append(f'{i} cycle.why {len(cy.get("why") or [])}줄')
        for w in cy.get('why') or []: txt(i, 'cycle.why', w.get('t'), lo=20, hi=320); srcs(i, 'cycle.why', w.get('src'))
        txt(i, 'cycle.next', cy.get('next'), lo=20, hi=320)
        if not 3 <= len(cy.get('watch') or []) <= 6: P.append(f'{i} cycle.watch {len(cy.get("watch") or [])}개')
        for sp in cy.get('split') or []:
            if sp.get('stage') not in range(1, 9): P.append(f'{i} split stage')
            for nd in sp.get('nodes', []):
                if nd not in nodes: P.append(f'{i} split 노드 {nd}')
        new_cy = {k: cy[k] for k in ('stage', 'conf', 'why', 'next', 'watch', 'split') if k in cy}
        new_cy['rev'] = TODAY; new_cy['flags'] = old_cy.get('flags') or []
        for k in old_cy:
            if k not in new_cy: new_cy[k] = old_cy[k]
        c['cycle'] = new_cy
    fl = []
    for f in x.get('flags') or []:
        txt(i, 'flags', f.get('t'), lo=20, hi=260)
        if f.get('nid') not in news_ids: P.append(f'{i} flags nid {f.get("nid")} 입력에 없음')
        fl.append({'nid': f.get('nid'), 't': f.get('t'), 'rev': TODAY})
    if len(fl) > 3: P.append(f'{i} flags 3개 넘음')
    c.setdefault('cycle', {})['flags'] = ((c['cycle'].get('flags') or []) + fl)[-12:]
    for nid, ns in (x.get('nodeStage') or {}).items():
        if nid not in nodes: P.append(f'{i} nodeStage 노드 {nid} 없음'); continue
        if ns.get('stage') not in range(1, 9): P.append(f'{i} nodeStage {nid} stage')
        nodes[nid]['stage'] = ns.get('stage'); nodes[nid]['stageNote'] = ns.get('stageNote', nodes[nid].get('stageNote', ''))
    ins = x.get('insight') or {}
    if ins:
        c['insight'] = dict(c.get('insight') or {})
        for k, arr in ins.items():
            if k not in KEYS: P.append(f'{i} insight 칸 {k}'); continue
            if not 1 <= len(arr) <= 3: P.append(f'{i} insight.{k} {len(arr)}줄')
            for a in arr: txt(i, f'insight.{k}', a.get('t'), lo=20, hi=360); srcs(i, f'insight.{k}', a.get('src')); a['rev'] = TODAY
            c['insight'][k] = arr
    if x.get('summary'):
        txt(i, 'summary', x['summary'], need_tag=False, lo=120, hi=900); c['summary'] = x['summary']
    if x.get('gaps'): c['gaps'] = x['gaps']
    txt(i, 'note', x.get('note'), need_tag=False, lo=15, hi=400)
    c['history'] = (c.get('history') or []) + [{'rev': TODAY, 'note': x.get('note', '')}]
    c['rev'] = TODAY; c['asOf'] = TODAY
    return c

os.makedirs(f'{W}/save', exist_ok=True); os.makedirs(f'{W}/save_meta', exist_ok=True)
log = json.load(open(f'{DB}/meta/chainsLog.json'))
done = {}
for f in sorted(glob.glob(f'{W}/out/*.json')):
    i = os.path.basename(f)[:-5]
    if ONLY and i != ONLY: continue
    try: x = json.load(open(f))
    except Exception as e: P.append(f'{i} json {e}'); continue
    if x.get('id') != i: P.append(f'{i} id 다름')
    ids = [json.loads(l)['id'] for l in open(f'{W}/news/{i}.jsonl')] if os.path.exists(f'{W}/news/{i}.jsonl') else []
    miss = set(ids) - set(x.get('applied') or [])
    if miss: P.append(f'{i} applied에 빠진 뉴스 {len(miss)}건')
    extra = set(x.get('applied') or []) - set(ids)
    if extra: P.append(f'{i} applied에 입력에 없는 id {sorted(extra)[:3]}')
    c = merge(i, x, json.load(open(f'{DB}/chains/{i}.json')), set(ids))
    sz = len(json.dumps(c, ensure_ascii=False).encode())
    if sz > 250000: P.append(f'{i} 크기 {sz}바이트')
    done[i] = (len(ids), sz, x.get('searches', 0), (c.get('cycle') or {}).get('stage'))
    if not ONLY:
        json.dump(c, open(f'{W}/save/{i}.json', 'w'), ensure_ascii=False)
        for n in ids: log['applied'][n] = TODAY
if not ONLY and done:
    log['runs'] = (log.get('runs') or []) + [{'d': TODAY, 'mode': '수동(사용자 요청: 산업 한 페이지 전부 업데이트)', 'n': sum(v[0] for v in done.values()),
                                              'problems': len(P), 'inds': {k: {'news': v[0], 'bytes': v[1], 'searches': v[2], 'stage': v[3]} for k, v in done.items()}}]
    log['runs'] = log['runs'][-60:]
    json.dump(log, open(f'{W}/save_meta/chainsLog.json', 'w'), ensure_ascii=False)
print('PROBLEMS', len(P))
for p in P: print(' -', p)
for k, v in done.items(): print(k, '뉴스', v[0], '바이트', v[1], '검색', v[2], '국면', v[3])
