"""서브 에이전트 결과(out/A*.json)를 합쳐 '제목 + 한줄 요약' 뉴스 문서(newsdocs/)와 진행 기록(meta_out/)을 만든다.
사용: python3 -I mk_one.py <DB 사본 폴더> <processed 날짜>   (DB에 쓰지는 않음 — WRITES 줄을 ArtifactData batch에 넣는다)"""
import json, glob, os, re, sys
DB, TODAY = sys.argv[1], sys.argv[2]
prog = json.load(open(f'{DB}/meta/progressV4.json')); seen = json.load(open(f'{DB}/meta/newsSeen.json'))
NODES = {os.path.basename(p)[:-5]: [n['id'] for n in json.load(open(p))['nodes']] for p in glob.glob(f'{DB}/chains/*.json')}
items = []; skipped = []
for p in sorted(glob.glob('out/A*.json')):
    d = json.load(open(p))
    for x in d['items']: x['_a'] = os.path.basename(p)[:-5]; items.append(x)
    for s in d.get('skipped', []): s['_a'] = os.path.basename(p)[:-5]; skipped.append(s)
by = {x['key']: x for x in items}
def merge(keep, drop, add_inds=()):
    k, d = by[keep], by.pop(drop)
    have = {s['u'] for s in k['src']}
    k['src'] += [s for s in d['src'] if s['u'] not in have]
    for i in add_inds:
        if i not in k['inds']: k['inds'].append(i)
    for n in d['nodes']:
        if n not in k['nodes']: k['nodes'].append(n)
    k['check'] = k['check'].rstrip() + ' 같은 사건을 다룬 다른 분야 정리와 한 건으로 합쳤습니다.'
merge('bbg-1006-vietnam-lng-power-behind-schedule', 'bbg-1006-vietnam-lng-power-delay')
merge('bbg-1006-jgb-10y-auction-solid', 'bbg-1006-japan-10y-auction-solid')
# 도시바 HDD: 블룸버그·로이터 주소가 없어, 이 소식이 실제로 들어온 텔레그램 글(하나증권 중국전략 69767)을 원문으로 둔다.
t = by.pop('nik-1002-toshiba-hdd-capacity-double')
t.update(key='tg-HANAchina-69767', source='텔레그램', channel='하나증권 중국전략', url='https://t.me/HANAchina/69767', published='2026-10-02T21:33:00+09:00',
         check='텔레그램 글(닛케이 보도 전재)로 들어온 소식이며, 닛케이 보도를 인용한 TrendForce(10월 2일) 자체 기사로 확인했습니다. 블룸버그·로이터 기사 주소는 찾지 못했습니다.')
t['src'] = [{'o': '텔레그램 하나증권 중국전략', 'd': '2026-10-02', 'u': 'https://t.me/HANAchina/69767'}] + t['src']
deep = json.load(open('toshiba_deep.json')); t['detail'] = deep['detail']; t['insight2'] = deep['insight2']
by[t['key']] = t
P = []
known_urls = {l.rsplit(' | ', 1)[-1] for l in seen['lines']}
known_ids = {l.split(' ')[1] for l in seen['lines'] if len(l.split(' ')) > 1}
PRE = {'텔레그램': 'tg', '블룸버그': 'bbg', '로이터': 'rtr'}
os.makedirs('newsdocs', exist_ok=True); os.makedirs('meta_out', exist_ok=True)
for f in glob.glob('newsdocs/*.json'): os.remove(f)
docs = []; new_lines = []
for src, pre in PRE.items():
    lst = sorted([x for x in by.values() if x['source'] == src], key=lambda c: (c['published'], c['key']))
    n0 = prog['newsSeq'].get(pre, 0)
    for i, c in enumerate(lst, 1):
        n = n0 + i; nid = f'n-{pre}-{n:04d}'; w = c['key']
        if nid in known_ids: P.append(f'{nid} 이미 있음')
        if c['url'] in known_urls: P.append(f'{w}: 이미 다룬 주소')
        one = c['one'].strip().rstrip('.').strip(); title = c['title'].strip()
        if not (60 <= len(one) <= 135): P.append(f'{w}: 한줄 {len(one)}자')
        if not one.endswith('다'): P.append(f'{w}: 한줄이 ~다로 끝나지 않음 …{one[-6:]}')
        if not (12 <= len(title) <= 50): P.append(f'{w}: 제목 {len(title)}자')
        for s in [one, title] + c['facts'] + [c['check']]:
            if '|' in s or '**' in s or '{{' in s: P.append(f'{w}: 금지 문자')
        if not re.match(r'^2026-10-0[1-8]', c['published']): P.append(f'{w}: 날짜 {c["published"]}')
        for nd in c['nodes']:
            a, b = nd.split('/')
            if b not in NODES.get(a, []): P.append(f'{w}: 없는 노드 {nd}')
            if a not in c['inds']: P.append(f'{w}: inds에 {a} 없음')
        if not c['src'] or not all(s.get('u', '').startswith('http') for s in c['src']): P.append(f'{w}: src')
        if len(c['src']) < 2: P.append(f'{w}: 독립 출처 없음')
        if c['basis'] not in ('verified', 'partial'): P.append(f'{w}: basis {c["basis"]}')
        d = {'id': nid, 'feed': 'v5', 'format': 'one1', 'num': n, 'processed': TODAY, 'source': src, 'key': w, 'published': c['published'], 'url': c['url'],
             'inds': c['inds'], 'nodes': c['nodes'], 'title': title, 'one': one, 'headline': title, 'facts': c['facts'], 'basis': c['basis'], 'check': c['check'],
             'src': c['src'], 'tags': [], 'cycles': [], 'incentive': '', 'insight': {}}
        if src == '텔레그램': d['channel'] = c.get('channel', '')
        if 'macro/semis' in c['nodes']: d['ind'] = 'semis'
        if c.get('origTitle'): d['origTitle'] = c['origTitle']
        if c.get('dupOf'): d['dupOf'] = c['dupOf']
        for k in ('detail', 'insight2'):
            if c.get(k): d[k] = c[k]
        json.dump(d, open(f'newsdocs/{nid}.json', 'w'), ensure_ascii=False, indent=1); docs.append(d)
        new_lines.append(f"{c['published'][:16]} {nid} {title} | {c['url']}")
    prog['newsSeq'][pre] = n0 + len(lst)
print('PROBLEMS', len(P)); [print(' -', x) for x in P]
# 진행 기록
left = [s for s in skipped if re.search(r'예산|독립 출처 없음', s.get('reason', ''))]
note = ('10월 8일: 10월 1~8일분을 웹 검색으로 찾아 제목+한줄 요약으로 저장(블룸버그 %d·로이터 %d). 남은 후보(확인 못 해 뺀 제목): ' % (sum(1 for d in docs if d['source'] == '블룸버그'), sum(1 for d in docs if d['source'] == '로이터'))
        + ' / '.join('%s(%s, %s)' % (s['title'][:70], (s.get('date') or '')[5:], '예산' if '예산' in s['reason'] else '독립 출처 없음') for s in left))
prog.setdefault('bloomberg', {})['notePrev'] = prog.get('bloomberg', {}).get('note', '')
prog['bloomberg']['note'] = note
prog['reuters']['newNote'] = '10월 8일: reuters.com은 본문·검색이 모두 막혀, tradingview.com 검색에 나온 로이터 제목만으로 후보를 찾고 독립 출처로 확인해 저장. 사이트맵 전체 목록은 받지 못해 빠진 기사가 있을 수 있음 / ' + prog['reuters'].get('newNote', '')[:400]
prog['mode'] = '2026-10-08 개편: 뉴스는 제목+한줄 요약(format one1)으로 저장하고 10월 8일부터 날짜를 거슬러 올라가며 정리. 자세한 정리는 사용자가 페이지에서 자세히에 체크한 뉴스만(data/users/<id>/detailReq), 투자 인사이트(산업 구조·뒤집어 보기·후보 기업)는 자세한 정리 안에서 체크한 뉴스만(insightReq) 작성. 예전 요약 카드(format sum1)는 산업 한 페이지에 반영을 마쳐 목록에서 숨김. 산업 한 페이지는 매일 20:47(KST) 예약 작업. 모든 하위 작업은 Opus'
prog['log'] = (prog['log'] + [{'d': TODAY, 't': '%s 데스크 개편(제목+한줄 목록·자세히 체크·읽음·자세한 정리·투자 인사이트 영역, 예전 요약 카드 161건은 이전 기록으로 숨김). 블룸버그·로이터 10월 1~8일분 %d건을 분야별 서브 에이전트 8개(Opus)가 웹 검색과 독립 출처 확인으로 작성: %s~%s. 도시바 HDD 증설(텔레그램 하나증권 중국전략 69767)은 시안의 자세한 정리·투자 인사이트를 함께 저장' % (TODAY, len(docs), docs[0]['id'], docs[-1]['id'])}])[-60:]
json.dump(prog, open('meta_out/progressV4.json', 'w'), ensure_ascii=False, indent=1)
seen['lines'] = (seen['lines'] + new_lines)[-1500:]; seen['count'] = len(seen['lines']); seen['updated'] = TODAY
json.dump(seen, open('meta_out/newsSeen.json', 'w'), ensure_ascii=False)
import collections
print(len(docs), collections.Counter(d['source'] for d in docs), collections.Counter(d['published'][:10] for d in docs), prog['newsSeq'])
print(collections.Counter(d.get('ind') or d['inds'][0] for d in docs), 'bytes', sum(os.path.getsize(f) for f in glob.glob('newsdocs/*.json')))
print('note len', len(note))
