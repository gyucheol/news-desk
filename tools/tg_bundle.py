"""후보 목록(T*.json)과 텔레그램 덤프(JSONL)로 서브 에이전트용 원문 묶음(bundle/<묶음>.md)을 만든다.
사용: python3 -I tg_bundle.py <후보 폴더> <덤프 폴더>
  후보 폴더의 T*.json(post, key, channel, url, published, gist, inds, nodes, also)을 읽어 같은 폴더 bundle/에 쓴다.
  also의 'HANAchina/69982(...)', 'Trillion_labs/10033·10036' 꼴에서 글 번호를 뽑아 원문을 함께 붙인다."""
import json, glob, os, re, sys
CAND, DUMP = sys.argv[1], sys.argv[2]
NAME = {'HANAchina': '하나증권 중국전략', 'Trillion_labs': '트릴리온', 'The_MariTimes': 'Polaristimes', 'insidertracking': '미국 주식 인사이더',
        'Badonions': '나쁜양파', 'PipeBeom': '상상인 김진범', 'w_compass': '부의 나침반', 'TNBfolio': 'TNBfolio', 'Onionfarmer': '양파농장',
        'cahier_de_market': '카이에 de market', 'kkkontemp': 'KK Kontemporaries'}
posts = {}
for p in glob.glob(f'{DUMP}/**/*.jsonl', recursive=True):
    ch = os.path.basename(p)[:-6]
    for l in open(p):
        d = json.loads(l); posts[(ch, d['id'])] = d

def refs(also):
    out, cur = [], None
    for tok in re.findall(r'([A-Za-z_]+)/(\d+)|·(\d+)', also or ''):
        if tok[0]: cur = tok[0]; out.append((cur, int(tok[1])))
        elif cur: out.append((cur, int(tok[2])))
    return out

def body(ch, pid, cap=1800):
    d = posts.get((ch, pid))
    if not d: return None, None
    x = d['x'] if len(d['x']) <= cap else d['x'][:cap] + ' …(이하 생략)'
    return d['t'][:16], x

os.makedirs(f'{CAND}/bundle', exist_ok=True)
missing = []
for f in sorted(glob.glob(f'{CAND}/T*.json')):
    g = os.path.basename(f)[:-5]; lines = [f'# 묶음 {g}\n']
    for i, c in enumerate(json.load(open(f)), 1):
        ch, pid = c['post'].split('/'); pid = int(pid)
        t, x = body(ch, pid)
        if x is None: missing.append(c['post'])
        lines.append(f"## {i}. key={c['key']}  채널={NAME.get(ch, ch)}  게시={(t or c['published'][:16])}:00+09:00  url=https://t.me/{ch}/{pid}")
        lines.append(f"제안 산업·노드: {','.join(c['inds'])} / {','.join(c['nodes'])}")
        lines.append(f"요지(미확인): {c['gist']}")
        if c.get('also'): lines.append(f"함께 볼 글 메모: {c['also']}")
        lines.append(f"[원문] {x if x is not None else '(덤프에 없음 — 요지만 있음)'}")
        for rch, rid in refs(c.get('also')):
            if (rch, rid) == (ch, pid): continue
            rt, rx = body(rch, rid, 1200)
            if rx is None: missing.append(f'{rch}/{rid}'); continue
            lines.append(f"[함께 볼 글 {NAME.get(rch, rch)} {rch}/{rid} {rt}] {rx}")
        lines.append('')
    open(f'{CAND}/bundle/{g}.md', 'w').write('\n'.join(lines))
    print(g, os.path.getsize(f'{CAND}/bundle/{g}.md'), 'bytes')
print('덤프에 없는 글', len(missing), missing)
