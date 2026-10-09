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
NEWIND = {'tech', 'auto', 'aero', 'pharma', 'fin', 'consumer', 'shipping', 'realestate', 'industrial', 'metals', 'agri'}
CHAN = json.load(open('chan.json'))['chan']
TAILS = {'title': ' (제목 기준)', 'channel': ' (채널 전언)'}
SRCN = {'bbg': '블룸버그', 'rtr': '로이터', 'tg': '텔레그램'}

when, kind = {}, {}
for l in open('all.tsv'):
    x = l.rstrip('\n').split('\t')
    when[x[4]] = f'2026-{x[2][:5]}T{x[2][6:11]}:00+09:00'
    kind[x[4]] = x[1]
known_urls = {l.rsplit(' | ', 1)[-1] for l in seen['lines']}
if os.path.exists(f'{DB}/meta/newsSeenOld.json'):
    known_urls |= {l.rsplit(' | ', 1)[-1] for l in json.load(open(f'{DB}/meta/newsSeenOld.json'))['lines']}

items, skipped, P = [], [], []
for p in sorted(glob.glob('out2/W*.json')):
    d = json.load(open(p)); items += d['items']; skipped += d.get('skipped', [])

def label(u):
    k = kind.get(u, '')
    return '텔레그램 ' + CHAN.get(k[3:], k[3:]) if k.startswith('tg:') else SRCN.get(k, '')

def check(x, its):
    w = x['cid']; one = x['one']
    tail = TAILS.get(x['basis'], '')
    if tail and not one.endswith(tail): P.append(f'{w} basis {x["basis"]} 꼬리 없음')
    core = one[:-len(tail)] if tail and one.endswith(tail) else one
    for t in TAILS.values():
        if core.endswith(t): P.append(f'{w} 꼬리가 basis와 다름')
    lo, hi = (80, 130) if len(its) <= 1 and not x.get('attachTo') else (85, 165)
    if not lo <= len(core) <= hi: P.append(f'{w} one {len(core)}자')
    if not core.endswith('다'): P.append(f'{w} one 끝맺음')
    if not 12 <= len(x['title']) <= 60: P.append(f'{w} title {len(x["title"])}자')
    for nd in x.get('nodes', []):
        i, _, k = nd.partition('/')
        if k not in NODES.get(i, []): P.append(f'{w} node {nd}')
        if i not in x.get('inds', []): P.append(f'{w} inds에 {i} 없음')
    for i in x.get('inds', []):
        if i not in NODES and i not in NEWIND: P.append(f'{w} ind {i}')
    for s in [x['title'], one, x['check']] + x.get('facts', []):
        if '|' in s or '**' in s or '{{' in s: P.append(f'{w} 금지 문자')
    for f in x.get('facts', []):
        if not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f.strip()): P.append(f'{w} 꼬리표 없는 사실 줄 …{f[-12:]}')
    if x['basis'] not in ('verified', 'partial', 'title', 'channel'): P.append(f'{w} basis {x["basis"]}')
    if x['basis'] in ('verified', 'partial') and not x.get('src'): P.append(f'{w} 독립 출처 없음')
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
        u0 = its[0]['u']; k = kind[u0]; sk = 'tg' if k.startswith('tg:') else k
        seq[sk] += 1; did = f'n-{sk}-{seq[sk]:04d}'
        d = {'id': did, 'num': seq[sk], 'key': f'mix-{x["cid"]}-{TODAY}', 'feed': 'v5', 'format': 'one1',
             'source': SRCN[sk], 'processed': TODAY, 'published': lt, 'url': u0, 'origTitle': '', 'headline': x['title'],
             'src': ([{'o': its[0]['o'], 'd': its[0]['d'], 'u': u0}] if sk == 'tg' else []) + x.get('src', []),
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
summary = (f'{TODAY}: {SPAN} 텔레그램·블룸버그·로이터 글을 함께 거르고 묶어(data/mix-2026-10-09) 새 문서 {nnew}건, 기존 문서에 더함 {len(attached)}건. '
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
