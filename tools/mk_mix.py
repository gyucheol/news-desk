"""텔레그램·블룸버그·로이터를 함께 묶은 작성 결과(out2/W*.json)를 뉴스 문서로 합친다.
새 묶음은 새 문서(id는 묶음에서 가장 이른 글의 출처: n-tg / n-bbg / n-rtr), attachTo가 있으면 기존 문서에 기사를 더한다(bundle_attach.attach).
사용(작업 폴더 안에서): python3 -I ../../tools/mk_mix.py <DB 사본 폴더> <processed 날짜> <텔레그램 덤프 폴더> <기간 설명>
입력: all.tsv(줄번호·출처·KST 'MM-DD HH:MM'·제목·주소), chan.json(채널 표기 이름), out2/W*.json
결과: newsdocs/<id>.json, meta_out/progressV4.json·newsSeen.json(·newsSeenOld.json), attached.txt(고친 기존 문서 id)
DB에 쓰지는 않는다."""
import json, glob, os, re, sys, collections
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bundle_attach import attach, now_kst, rotate_seen
DB, TODAY, DUMP, SPAN = sys.argv[1:5]
NOW = now_kst()
prog = json.load(open(f'{DB}/meta/progressV4.json')); seen = json.load(open(f'{DB}/meta/newsSeen.json'))
NODES = {os.path.basename(p)[:-5]: [n['id'] for n in json.load(open(p))['nodes']] for p in glob.glob(f'{DB}/chains/*.json')}
NEWIND = {'pharma', 'fin', 'tech', 'auto', 'aero', 'agri', 'consumer', 'shipping', 'realestate', 'industrial', 'metals', 'oil'}
# 밸류체인 한 줄(vc, 2026-10-14 사용자 요청): 산업·노드는 tools/industry/nodes.json(산업 한 페이지 목록)과 DB 사본 chains 기준.
# 이번 회차 작성 결과에 vc를 쓰지 않았으면 NO_VC=1 로 실행합니다(나중에 vc를 따로 붙일 때).
VCN = dict(NODES)
if os.path.exists(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'industry', 'nodes.json')):
    VCN.update(json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'industry', 'nodes.json'))))
NEED_VC = os.environ.get('NO_VC') != '1'
CHAN = json.load(open('chan.json'))['chan']
TAILS = {'title': ' (제목 기준)', 'channel': ' (채널 전언)'}
SRCN = {'bbg': '블룸버그', 'rtr': '로이터', 'tg': '텔레그램', 'fed': '연준 공식'}
# 연준 인사 발언(fed, 2026-10-15 사용자 지시: 매크로에 연준 인사 발언·관련 뉴스를 꼭 담음). 출처 fed:<기관>은 tools/fedspeech.py.
FEDR = json.load(open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'industry', 'fed_roster.json')))
BANKS = FEDR['banks']
FED_KIND = ('발언', '연설', '인터뷰', '증언', '성명·의사록', '조사·보고서', '인사·독립성', '감독·규제', '관련 뉴스')
FED_STANCE = ('매파', '비둘기파', '중립', '')

when, kind = {}, {}
for l in open('all.tsv'):
    x = l.rstrip('\n').split('\t')
    when[x[4]] = f'2026-{x[2][:5]}T{x[2][6:11]}:00+09:00'
    kind[x[4]] = x[1]
known_urls = {l.rsplit(' | ', 1)[-1] for l in seen['lines']}
for p in glob.glob(f'{DB}/meta/newsSeenOld*.json'):  # newsSeenOld가 256KB에 닿아 옛 줄은 newsSeenOld2로 옮김(2026-10-13)
    known_urls |= {l.rsplit(' | ', 1)[-1] for l in json.load(open(p))['lines']}

items, skipped, P = [], [], []
for p in sorted(glob.glob('out2/W*.json')):
    d = json.load(open(p)); items += d['items']; skipped += d.get('skipped', [])

def label(u):
    k = kind.get(u, '')
    if k.startswith('fed:'): return '연준 공식 ' + BANKS.get(k[4:], k[4:])
    return '텔레그램 ' + CHAN.get(k[3:], k[3:]) if k.startswith('tg:') else SRCN.get(k, '')

HL = re.compile(r'\{\{([^{}]+)\}\}')
# 강조 {{ }}는 쓰지 않습니다(2026-10-15 사용자 지시: "회색 강조하는 거 다 지워줘 앞으로도"). 남아 있으면 문제로 봅니다.
def hl_check(w, name, s, lo=None, hi=None):
    if '{{' in s or '}}' in s: P.append(f'{w} {name} 강조 표시 남음')
    return s.replace('{{', '').replace('}}', '')

def sub_line(w, name, s, lo, hi, nlo, nhi):
    core = re.sub(r' \((제목 기준|채널 전언)\)$', '', hl_check(w, name, s, nlo, nhi))
    if not lo <= len(core) <= hi: P.append(f'{w} {name} {len(core)}자')
    if not core.endswith('다'): P.append(f'{w} {name} 끝맺음')

def added_line(w, s):
    core = re.sub(r' \((제목 기준|채널 전언)\)$', '', hl_check(w, 'added', s, 1, 3))
    if not 40 <= len(core) <= 140: P.append(f'{w} added {len(core)}자')
    if not core.endswith('내용이 추가됨'): P.append(f"{w} added 끝맺음('~ 내용이 추가됨')")
    if ' — ' not in core: P.append(f"{w} added 꼴('[출처·건수] — [내용] 내용이 추가됨')")

def check_vc(w, vc):
    if not isinstance(vc, list) or not 1 <= len(vc) <= 3: P.append(f'{w} vc 개수'); return
    for v in vc:
        i, n = v.get('ind'), v.get('node')
        if i not in VCN: P.append(f'{w} vc 산업 {i}')
        elif n not in VCN[i]: P.append(f'{w} vc 노드 {i}/{n}')
        if v.get('f') not in ('공급', '수요', '가격', '-'): P.append(f"{w} vc f {v.get('f')}")
        if v.get('dir') not in ('up', 'down', 'flat', 'mixed'): P.append(f"{w} vc dir {v.get('dir')}")
        if v.get('k') not in ('실제', '예상'): P.append(f"{w} vc k {v.get('k')}")
        t = v.get('t', '')
        if not 8 <= len(t) <= 60 or '{{' in t: P.append(f'{w} vc t {len(t)}자')

def check_fed(w, x, its):
    fed = x.get('fed')
    if fed is None:
        if any(kind.get(it['u'], '').startswith('fed:') for it in its): P.append(f'{w} 연준 공식 글인데 fed 없음')
        return
    if not isinstance(fed, list) or not fed: P.append(f'{w} fed 형식'); return
    if 'macro' not in x.get('inds', []): P.append(f'{w} fed인데 inds에 macro 없음')
    if 'macro/cb' not in x.get('nodes', []): P.append(f'{w} fed인데 nodes에 macro/cb 없음')
    if (x.get('vc') or NEED_VC) and not any(v.get('ind') == 'macro' and v.get('node') == 'cb' for v in x.get('vc') or []): P.append(f'{w} fed인데 vc에 macro/cb 없음')
    us = {it['u'] for it in its}
    for f in fed:
        if f.get('kind') not in FED_KIND: P.append(f"{w} fed kind {f.get('kind')}")
        if f.get('stance', '') not in FED_STANCE: P.append(f"{w} fed stance {f.get('stance')}")
        if not f.get('who') or not f.get('role'): P.append(f'{w} fed who·role 없음')
        t = f.get('t', '')
        if not 15 <= len(t) <= 80 or '{{' in t or not t.endswith('다'): P.append(f'{w} fed t {len(t)}자')
        if f.get('u') not in us: P.append(f"{w} fed 주소가 items에 없음 {str(f.get('u'))[:60]}")
        if not re.match(r'^\d{4}-\d{2}-\d{2}$', f.get('d', '')): P.append(f"{w} fed d {f.get('d')}")

def check(x, its):
    w = x['cid']
    if 'vc' in x or NEED_VC: check_vc(w, x.get('vc'))
    check_fed(w, x, its)
    hl_check(w, 'title', x['title'], 1, 2)
    one = hl_check(w, 'one', x['one'], 2, 4)
    tail = TAILS.get(x['basis'], '')
    if tail and not one.endswith(tail): P.append(f'{w} basis {x["basis"]} 꼬리 없음')
    core = one[:-len(tail)] if tail and one.endswith(tail) else one
    for t in TAILS.values():
        if core.endswith(t): P.append(f'{w} 꼬리가 basis와 다름')
    lo, hi = (80, 130) if len(its) <= 1 and not x.get('attachTo') else (85, 165)
    if not lo <= len(core) <= hi: P.append(f'{w} one {len(core)}자')
    if not core.endswith('다'): P.append(f'{w} one 끝맺음')
    if not 12 <= len(x['title'].replace('{{', '').replace('}}', '')) <= 60: P.append(f'{w} title {len(x["title"])}자')
    for nd in x.get('nodes', []):
        i, _, k = nd.partition('/')
        if k not in NODES.get(i, []): P.append(f'{w} node {nd}')
        if i not in x.get('inds', []): P.append(f'{w} inds에 {i} 없음')
    for i in x.get('inds', []):
        if i not in NODES and i not in NEWIND: P.append(f'{w} ind {i}')
    for s in [x['title'], one, x['check']] + x.get('facts', []):
        if '|' in s or '**' in s: P.append(f'{w} 금지 문자')
    for s in [x['check']] + x.get('facts', []) + [it.get('t', '') for it in its] + [f.get('t', '') for f in x.get('fed') or []]:
        if '{{' in s: P.append(f'{w} 강조 표시 남음')
    for f in x.get('facts', []):
        if not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f.strip()): P.append(f'{w} 꼬리표 없는 사실 줄 …{f[-12:]}')
    if x['basis'] not in ('verified', 'partial', 'title', 'channel'): P.append(f'{w} basis {x["basis"]}')
    if x['basis'] in ('verified', 'partial') and not x.get('src'): P.append(f'{w} 독립 출처 없음')
    multi = len(its) > 1 or bool(x.get('attachTo'))
    # 추가된 내용(added): 이전 회차에 저장한 문서에 기사를 더할 때만 씀(2026-10-17 사용자 지시).
    # 같은 회차에 한꺼번에 묶은 새 문서에는 쓰지 않음. 꼴: '[출처·건수] — [새 핵심] 내용이 추가됨'
    prior = bool(x.get('attachTo')) and os.path.exists(f"{DB}/news/{x['attachTo']}.json")
    if prior: added_line(w, x.get('added', ''))
    elif x.get('added'): P.append(f'{w} 새 문서(이전 회차 문서에 더한 것이 아님)에 added')
    if multi:
        for k, it in enumerate(its): sub_line(w, f'items[{k}].s', it.get('s', ''), 45, 110, 1, 2)
    elif any(it.get('s') for it in its): P.append(f'{w} 한 건짜리에 s')
    for it in its:
        if it['u'] not in when: P.append(f'{w} 주소가 후보에 없음 {it["u"][:80]}')
        if it['u'] in known_urls: P.append(f'{w} 이미 다룬 주소 {it["u"][:80]}')

def norm_items(lst):
    out, have = [], set()
    for it in lst:
        if it['u'] in have: continue
        have.add(it['u']); it = dict(it)
        if it['u'] in when: it['d'] = when[it['u']][:10]
        it['o'] = label(it['u']) or it.get('o', '')
        out.append(it)
    return sorted(out, key=lambda it: when.get(it['u'], it.get('d', '')))

seq = dict(prog['newsSeq']); docs, attached, new_lines, used = {}, set(), [], set()
for x in sorted(items, key=lambda x: x['cid']):
    its = norm_items(x.get('items') or [])
    check(x, its)
    dup = [it['u'] for it in its if it['u'] in used]
    if dup: P.append(f"{x['cid']} 다른 묶음과 겹치는 주소 {len(dup)}")
    used |= {it['u'] for it in its}
    if not its: P.append(f"{x['cid']} 기사 없음"); continue
    fields = {k: x[k] for k in ('title', 'one', 'facts', 'basis', 'check')}
    if x.get('added'): fields['added'] = x['added']
    if x.get('vc'): fields['vc'] = x['vc']
    if x.get('fed'):  # 원문별 발언 목록. 기존 문서에 붙일 때는 기존 목록에 더함(같은 주소는 새 것으로)
        old = (docs.get(x.get('attachTo')) or (json.load(open(f"{DB}/news/{x['attachTo']}.json")) if x.get('attachTo') and os.path.exists(f"{DB}/news/{x['attachTo']}.json") else {})).get('fed', [])
        nu = {f['u'] for f in x['fed']}
        fields['fed'] = sorted([f for f in old if f.get('u') not in nu] + x['fed'], key=lambda f: f.get('d', ''))
    lt = max(when.get(it['u'], '') for it in its)
    if x.get('attachTo'):
        aid = x['attachTo']; path = f'{DB}/news/{aid}.json'
        if aid in docs: base = docs[aid]
        elif os.path.exists(path): base = json.load(open(path))
        else: P.append(f"{x['cid']} attachTo 없음 {aid}"); continue
        d = attach(base, its, fields, TODAY, NOW, x.get('src', []), x.get('inds', []), x.get('nodes', []), lt)
        if 'macro/semis' in d['nodes'] and not d.get('ind'): d['ind'] = 'semis'
        docs[aid] = d; attached.add(aid)
    else:
        u0 = its[0]['u']; k = kind[u0]; sk = 'tg' if k.startswith('tg:') else 'fed' if k.startswith('fed:') else k
        seq[sk] = seq.get(sk, 0) + 1; did = f'n-{sk}-{seq[sk]:04d}'
        d = {'id': did, 'num': seq[sk], 'key': f'mix-{x["cid"]}-{TODAY}', 'feed': 'v5', 'format': 'one1',
             'source': SRCN[sk], 'processed': TODAY, 'published': lt, 'url': u0, 'origTitle': '', 'headline': x['title'],
             'src': ([{'o': its[0]['o'], 'd': its[0]['d'], 'u': u0}] if sk in ('tg', 'fed') else []) + x.get('src', []),
             'items': its, 'cycles': [], 'tags': [], 'insight': {}, 'incentive': '',
             'inds': x.get('inds', []), 'nodes': x.get('nodes', [])}
        if sk == 'tg': d['channel'] = CHAN.get(k[3:], k[3:])
        if 'macro/semis' in d['nodes']: d['ind'] = 'semis'
        d.update(fields)
        if len(its) > 1: d['updatedAt'] = NOW
        docs[did] = d
    for it in its:
        new_lines.append(f"{when.get(it['u'], it['d'])[:16]} {d['id']} {it['t']} | {it['u']}")

os.makedirs('newsdocs', exist_ok=True); os.makedirs('meta_out', exist_ok=True)
for f in glob.glob('newsdocs/*.json') + glob.glob('meta_out/*.json'): os.remove(f)
for i, d in docs.items(): json.dump(d, open(f'newsdocs/{i}.json', 'w'), ensure_ascii=False, indent=1)
open('attached.txt', 'w').write(''.join(f'{i}\n' for i in sorted(attached)))
bas = collections.Counter(x['basis'] for x in items)
nnew = len(docs) - len(attached)
prog['newsSeq'] = seq
# 텔레그램 채널별 마지막으로 읽은 글 번호
last = {}
for p in glob.glob(f'{DUMP}/*.jsonl'):
    ids = [json.loads(l)['id'] for l in open(p)]
    if ids: last[os.path.basename(p)[:-6]] = max(ids)
tg = prog['telegram']; tg['new'].update({k: max(v, tg['new'].get(k, 0)) for k, v in last.items()})
summary = (f'{TODAY}: {SPAN} 텔레그램·블룸버그·로이터 글을 함께 거르고 묶어(data/{os.path.basename(os.getcwd())}) 새 문서 {nnew}건, 기존 문서에 더함 {len(attached)}건. '
           f'독립 출처 확인 {bas["verified"]}, 일부 확인 {bas["partial"]}, 채널 전언 {bas["channel"]}, 제목 기준 {bas["title"]}, 건너뜀 {len(skipped)}')
tg['newNote'] = summary + ' // ' + tg.get('newNote', '')[:600]
prog['log'] = (prog['log'] + [{'d': TODAY, 't': summary}])[-60:]
json.dump(prog, open('meta_out/progressV4.json', 'w'), ensure_ascii=False, indent=1)
seen['lines'] = seen['lines'] + new_lines; seen['count'] = len(seen['lines']); seen['updated'] = TODAY
old = json.load(open(f'{DB}/meta/newsSeenOld.json'))
if rotate_seen(seen, old, TODAY): json.dump(old, open('meta_out/newsSeenOld.json', 'w'), ensure_ascii=False)
json.dump(seen, open('meta_out/newsSeen.json', 'w'), ensure_ascii=False)
print('PROBLEMS', len(P)); [print(' -', p) for p in P[:80]]
print('docs', len(docs), 'new', nnew, 'attached', len(attached), 'articles', len(new_lines), dict(bas), 'skipped', len(skipped), seq)
print('bytes', sum(os.path.getsize(f) for f in glob.glob('newsdocs/*.json')))
