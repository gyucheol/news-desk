"""블룸버그·로이터 묶음 작성 결과(out2/W*.json)를 뉴스 문서로 합친다. 새 묶음은 새 문서, attachTo가 있으면 기존 문서에 기사를 더한다.
사용(작업 폴더 안에서): python3 -I ../../tools/mk_bundle.py <DB 사본 폴더> <processed 날짜>
결과: newsdocs/<id>.json(새 문서와 고친 기존 문서), meta_out/progressV4.json·newsSeen.json, attached.txt(고친 기존 문서 id와 version)
DB에 쓰지는 않는다."""
import json, glob, os, re, sys, collections
from datetime import datetime, timezone, timedelta
DB, TODAY = sys.argv[1], sys.argv[2]
KST = timezone(timedelta(hours=9))
NOW = datetime.now(KST).strftime('%Y-%m-%dT%H:%M:%S+09:00')

def load(p):
    d = json.load(open(p))
    return d.get('data', d) if 'data' in d and len(d) < 5 else d
def version(p):
    d = json.load(open(p)); return d.get('version')

prog = load(f'{DB}/meta/progressV4.json'); seen = load(f'{DB}/meta/newsSeen.json')
NODES = {os.path.basename(p)[:-5]: [n['id'] for n in load(p)['nodes']] for p in glob.glob(f'{DB}/chains/*.json')}
NEWIND = {'tech', 'auto', 'aero', 'pharma', 'fin', 'consumer', 'shipping', 'realestate', 'industrial', 'metals', 'agri'}
# keep.tsv: 줄번호, 분야, 출처, KST 'MM-DD HH:MM', 제목, 주소 → 주소별 시각
when = {}
for l in open('keep.tsv'):
    x = l.rstrip('\n').split('\t')
    when[x[5]] = f'2026-{x[3][:5]}T{x[3][6:11]}:00+09:00'
SRCN = {'bbg': '블룸버그', 'rtr': '로이터'}

items, skipped, probs = [], [], []
for p in sorted(glob.glob('out2/W*.json')):
    d = json.load(open(p))
    items += d['items']; skipped += d.get('skipped', [])

def check(x):
    one = re.sub(r' \(제목 기준\)$', '', x['one'])
    n = len(x.get('items') or [])
    lo, hi = (80, 130) if n <= 1 and not x.get('attachTo') else (85, 165)
    if not lo <= len(one) <= hi: probs.append(f"{x['cid']} one {len(one)}자")
    if not one.endswith('다'): probs.append(f"{x['cid']} one 끝맺음")
    if not 12 <= len(x['title']) <= 60: probs.append(f"{x['cid']} title {len(x['title'])}자")
    for nd in x.get('nodes', []):
        i, _, k = nd.partition('/')
        if k not in NODES.get(i, []): probs.append(f"{x['cid']} node {nd}")
    for i in x.get('inds', []):
        if i not in NODES and i not in NEWIND: probs.append(f"{x['cid']} ind {i}")
    for f in x.get('facts', []):
        if '|' in f or '**' in f: probs.append(f"{x['cid']} facts 기호")
    for it in x.get('items', []):
        if it['u'] not in when: probs.append(f"{x['cid']} 주소가 후보에 없음 {it['u'][:80]}")
    if x['basis'] not in ('verified', 'partial', 'title'): probs.append(f"{x['cid']} basis")
    if x['basis'] == 'title' and not x['one'].endswith(' (제목 기준)'): probs.append(f"{x['cid']} 제목 기준 꼬리")

def norm_items(lst):
    out, have = [], set()
    for it in lst:
        if it['u'] in have: continue
        have.add(it['u']); it = dict(it)
        if it['u'] in when: it['d'] = when[it['u']][:10]
        out.append(it)
    return sorted(out, key=lambda it: when.get(it['u'], it.get('d', '')))

def latest(lst):
    ts = [when[it['u']] for it in lst if it['u'] in when]
    return max(ts) if ts else ''

seq = dict(prog['newsSeq']); docs, attached, new_lines = {}, {}, []
for x in sorted(items, key=lambda x: x['cid']):
    check(x)
    its = norm_items(x.get('items') or [])
    if not its: probs.append(f"{x['cid']} 기사 없음"); continue
    base = {k: x[k] for k in ('title', 'one', 'facts', 'basis', 'check', 'inds', 'nodes')}
    if x.get('attachTo'):
        aid = x['attachTo']
        path = f'{DB}/news/{aid}.json'
        if aid in docs: d = docs[aid]
        elif os.path.exists(path):
            d = load(path); attached[aid] = version(path)
            if not d.get('items'):
                d['items'] = [{'t': d.get('title', ''), 'o': (d['source'] + (' ' + d['channel'] if d.get('source') == '텔레그램' and d.get('channel') else '')),
                               'd': (d.get('published') or d.get('processed') or '')[:10], 'u': d.get('url') or (d.get('src') or [{}])[0].get('u', '')}]
        else: probs.append(f"{x['cid']} attachTo 없음 {aid}"); continue
        d = dict(d)
        d['items'] = d['items'] + [it for it in its if it['u'] not in {i['u'] for i in d['items']}]
        d.update(base); d['headline'] = d['title']
        d['inds'] = sorted(set(d.get('inds', [])) | set(x['inds']), key=lambda i: (i != 'macro', i))
        d['nodes'] = sorted(set(d.get('nodes', [])) | set(x['nodes']))
        have = {s.get('u') for s in d.get('src', [])}
        d['src'] = d.get('src', []) + [s for s in x.get('src', []) if s.get('u') not in have]
        lt = latest(its)
        if lt > (d.get('published') or ''): d['published'] = lt
        d['updatedAt'] = NOW; d['processed'] = TODAY
        docs[aid] = d
    else:
        sk = 'bbg' if 'bloomberg.com' in its[0]['u'] else 'rtr'
        seq[sk] += 1; did = f'n-{sk}-{seq[sk]:04d}'
        d = {'id': did, 'num': seq[sk], 'key': f'bnd-{x["cid"]}-{TODAY}', 'feed': 'v5', 'format': 'one1',
             'source': SRCN[sk], 'processed': TODAY, 'published': latest(its), 'url': its[0]['u'], 'origTitle': '',
             'headline': x['title'], 'src': x.get('src', []), 'items': its, 'cycles': [], 'tags': [], 'insight': {}, 'incentive': ''}
        d.update(base)
        if len(its) > 1: d['updatedAt'] = NOW
        docs[did] = d
    for it in its:
        new_lines.append(f"{when.get(it['u'], it['d'])[:16]} {d['id']} {it['t']} | {it['u']}")

os.makedirs('newsdocs', exist_ok=True); os.makedirs('meta_out', exist_ok=True)
for f in glob.glob('newsdocs/*.json'): os.remove(f)
for i, d in docs.items(): json.dump(d, open(f'newsdocs/{i}.json', 'w'), ensure_ascii=False, indent=1)
open('attached.txt', 'w').write(''.join(f'{i} {v}\n' for i, v in attached.items()))
bas = collections.Counter(x['basis'] for x in items)
nnew = len(docs) - len(attached)
prog['newsSeq'] = seq
prog['log'] = (prog['log'] + [{'d': TODAY, 't': f'{TODAY} 블룸버그·로이터 10월 7~9일 사이트맵 1,517건 → 1차 거르기(Haiku) 720건 → 같은 흐름 묶기 → 새 문서 {nnew}건, 기존 문서에 더함 {len(attached)}건. 독립 출처 확인 {bas["verified"]}, 일부 확인 {bas["partial"]}, 제목 기준 {bas["title"]}'}])[-60:]
json.dump(prog, open('meta_out/progressV4.json', 'w'), ensure_ascii=False)
seen['lines'] = (seen['lines'] + new_lines)[-3000:]; seen['count'] = len(seen['lines']); seen['updated'] = TODAY
json.dump(seen, open('meta_out/newsSeen.json', 'w'), ensure_ascii=False)
print('PROBLEMS', len(probs)); [print(' ', p) for p in probs[:60]]
print('docs', len(docs), 'new', nnew, 'attached', len(attached), 'articles', len(new_lines), dict(bas), 'skipped', len(skipped), seq)
print('bytes', sum(len(json.dumps(d, ensure_ascii=False)) for d in docs.values()))
