"""텔레그램 서브 에이전트 결과(out/T*.json)를 합쳐 '제목 + 한줄 요약' 뉴스 문서(newsdocs/)와 진행 기록(meta_out/)을 만든다.
사용(묶음 폴더에서): python3 -I mk_one_tg.py <DB 사본 폴더> <processed 날짜> <덤프 폴더> <기간 설명> [게시 시각 검사 정규식]
  예: python3 -I ../../tools/mk_one_tg.py ../../work/live2 2026-10-08 ../../work/dump2 '10월 6일 0시~10월 8일 08시 35분'
  DB에 쓰지는 않는다 — newsdocs/*.json과 meta_out/*.json을 ArtifactData batch에 넣는다.
  basis는 verified·partial·channel. channel이면 한줄 끝에 ' (채널 전언)'이 붙고 독립 출처가 없어도 된다."""
import json, glob, os, re, sys, collections
DB, TODAY, DUMP, SPAN = sys.argv[1:5]
DATE_RE = sys.argv[5] if len(sys.argv) > 5 else r'^2026-10-0[6-8]T'  # 기간 검사 정규식
prog = json.load(open(f'{DB}/meta/progressV4.json')); seen = json.load(open(f'{DB}/meta/newsSeen.json'))
NODES = {os.path.basename(p)[:-5]: [n['id'] for n in json.load(open(p))['nodes']] for p in glob.glob(f'{DB}/chains/*.json')}
TAIL = ' (채널 전언)'
items, skipped = [], []
for p in sorted(glob.glob('out/T*.json')):
    d = json.load(open(p)); a = os.path.basename(p)[:-5]
    for x in d['items']: x['_a'] = a; items.append(x)
    for s in d.get('skipped', []): s['_a'] = a; skipped.append(s)
P = []
by = {}
for x in items:
    if x['key'] in by: P.append(f"{x['key']}: 두 묶음에 중복({by[x['key']]['_a']}, {x['_a']})"); continue
    by[x['key']] = x
known_urls = {l.rsplit(' | ', 1)[-1] for l in seen['lines']}
known_ids = {l.split(' ')[1] for l in seen['lines'] if len(l.split(' ')) > 1}
os.makedirs('newsdocs', exist_ok=True); os.makedirs('meta_out', exist_ok=True)
for f in glob.glob('newsdocs/*.json'): os.remove(f)
lst = sorted(by.values(), key=lambda c: (c['published'], c['key']))
n0 = prog['newsSeq'].get('tg', 0); docs, new_lines = [], []
for i, c in enumerate(lst, 1):
    n = n0 + i; nid = f'n-tg-{n:04d}'; w = c['key']
    if nid in known_ids: P.append(f'{nid} 이미 있음')
    if c['url'] in known_urls: P.append(f'{w}: 이미 다룬 주소')
    if c['source'] != '텔레그램' or not c['url'].startswith('https://t.me/'): P.append(f'{w}: source·url')
    one = c['one'].strip().rstrip('.').strip(); title = c['title'].strip()
    core = one[:-len(TAIL)] if one.endswith(TAIL) else one
    if (c['basis'] == 'channel') != one.endswith(TAIL): P.append(f'{w}: basis {c["basis"]}와 (채널 전언) 꼬리가 맞지 않음')
    if not (60 <= len(core) <= 135): P.append(f'{w}: 한줄 {len(core)}자')
    if not core.endswith('다'): P.append(f'{w}: 한줄이 ~다로 끝나지 않음 …{core[-6:]}')
    if not (12 <= len(title) <= 50): P.append(f'{w}: 제목 {len(title)}자')
    for s in [one, title] + c['facts'] + [c['check']]:
        if '|' in s or '**' in s or '{{' in s: P.append(f'{w}: 금지 문자')
    for s in c['facts']:
        if not re.search(r'\[(사실|채널|추론|미확인)\]$', s.strip()): P.append(f'{w}: 꼬리표 없는 사실 줄 …{s[-12:]}')
    if not re.match(DATE_RE, c['published']): P.append(f'{w}: 날짜 {c["published"]}')
    for nd in c['nodes']:
        a, b = nd.split('/')
        if b not in NODES.get(a, []): P.append(f'{w}: 없는 노드 {nd}')
        if a not in c['inds']: P.append(f'{w}: inds에 {a} 없음')
    if not c['src'] or not all(s.get('u', '').startswith('http') for s in c['src']): P.append(f'{w}: src')
    if c['basis'] in ('verified', 'partial') and len(c['src']) < 2: P.append(f'{w}: 독립 출처 없음')
    if c['basis'] not in ('verified', 'partial', 'channel'): P.append(f'{w}: basis {c["basis"]}')
    d = {'id': nid, 'feed': 'v5', 'format': 'one1', 'num': n, 'processed': TODAY, 'source': '텔레그램', 'key': w, 'published': c['published'], 'url': c['url'],
         'inds': c['inds'], 'nodes': c['nodes'], 'title': title, 'one': one, 'headline': title, 'facts': c['facts'], 'basis': c['basis'], 'check': c['check'],
         'src': c['src'], 'tags': [], 'cycles': [], 'incentive': '', 'insight': {}, 'channel': c.get('channel', '')}
    if 'macro/semis' in c['nodes']: d['ind'] = 'semis'
    if c.get('dupOf'): d['dupOf'] = c['dupOf']
    json.dump(d, open(f'newsdocs/{nid}.json', 'w'), ensure_ascii=False, indent=1); docs.append(d)
    new_lines.append(f"{c['published'][:16]} {nid} {title} | {c['url']}")
prog['newsSeq']['tg'] = n0 + len(lst)
print('PROBLEMS', len(P)); [print(' -', x) for x in P]
# 진행 기록: 채널별 마지막으로 읽은 글 번호와 메모
last = {}
for p in glob.glob(f'{DUMP}/*.jsonl'):
    ids = [json.loads(l)['id'] for l in open(p)]
    if ids: last[os.path.basename(p)[:-6]] = max(ids)
tg = prog['telegram']; tg['new'].update(last)
bas = collections.Counter(d['basis'] for d in docs)
note = (f'{TODAY}: {SPAN} 글을 curl 덤프로 모두 받아(work/{os.path.basename(DUMP.rstrip("/"))}) 관심 산업 후보 {len(items) + len(skipped)}건 중 {len(docs)}건을 제목+한줄 요약으로 저장'
        f'({docs[0]["id"]}~{docs[-1]["id"]}, 독립 출처 확인 {bas["verified"]}·일부 확인 {bas["partial"]}·채널 전언 {bas["channel"]}). 뺀 후보: '
        + ' / '.join(f"{s.get('key', '')}({s.get('reason', '')[:30]})" for s in skipped))
tg['newNote'] = note + ' // ' + tg.get('newNote', '')[:600]
prog['log'] = (prog['log'] + [{'d': TODAY, 't': f'{TODAY} 텔레그램 {SPAN}분 {len(docs)}건({docs[0]["id"]}~{docs[-1]["id"]})을 덤프 원문 + 분야별 서브 에이전트 5개(Opus)로 제목+한줄 작성. 독립 출처 확인 {bas["verified"]}, 일부 확인 {bas["partial"]}, 채널 전언 {bas["channel"]}'}])[-60:]
json.dump(prog, open('meta_out/progressV4.json', 'w'), ensure_ascii=False, indent=1)
seen['lines'] = (seen['lines'] + new_lines)[-1500:]; seen['count'] = len(seen['lines']); seen['updated'] = TODAY
json.dump(seen, open('meta_out/newsSeen.json', 'w'), ensure_ascii=False)
print(len(docs), collections.Counter(d['published'][:10] for d in docs), bas, prog['newsSeq'])
print(collections.Counter(d.get('ind') or d['inds'][0] for d in docs), 'bytes', sum(os.path.getsize(f) for f in glob.glob('newsdocs/*.json')))
print('skipped', len(skipped), 'note len', len(note))
