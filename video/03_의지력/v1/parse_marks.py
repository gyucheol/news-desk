# 사용자 표시 대본(<자막>번호, <<...>>, /, *)을 2판 자막 조각(plan_data.py)에 맞춰 붙인다.
import re, sys, json, difflib
sys.path.insert(0, '../plan')
import plan_data as d

raw = open('user_script_raw.txt', encoding='utf-8').read()
body = raw.split('* 대본', 1)[1]

# 1) 토큰화: <<...>>, <...>N, 나머지 글자
toks = []  # (kind, text, num)
i = 0
pat = re.compile(r'<<(.*?)>>|<(.*?)>\s*(\d+)?', re.S)
pos = 0
for m in pat.finditer(body):
    if m.start() > pos:
        toks.append(('plain', body[pos:m.start()], None))
    if m.group(1) is not None:
        toks.append(('special', m.group(1), None))
    else:
        n = m.group(3)
        toks.append(('photo', m.group(2), int(n) if n else None))
    pos = m.end()
toks.append(('plain', body[pos:], None))

# 번호 없는 사진 표시: 앞뒤 번호로 채움(2와 4 사이 → 3)
for k, t in enumerate(toks):
    if t[0] == 'photo' and t[2] is None:
        prev = [x[2] for x in toks[:k] if x[0] == 'photo' and x[2]][-1]
        toks[k] = ('photo', t[1], prev + 1)
        print('번호 없는 사진 표시 →', prev + 1, ':', t[1].strip())

NUMW = [('이천십팔년', '2018년'), ('이백사십팔 명', '248명'), ('삼십 분', '30분'), ('여덟 시', '8시'),
        ('아홉 시', '9시'), ('두 시간', '2시간'), ('세 가지', '3가지'), ('한 시간', '1시간'), ('오 분', '5분')]
def numw(s):
    for a, b in NUMW:
        s = s.replace(a, b)
    return s
def norm(s):
    return re.sub(r'[\s\.,\?\!"“”\'‘’·:;\-]', '', numw(s))
toks = [(k, numw(t), n) for k, t, n in toks]

# 2) 사용자 글자열과 칸 표시 만들기. 칸: ('P', n) 사진, ('S',) 특별, ('U', run_id) 표시 없음
#    '/'는 스톡 바꿈, '*'는 단락 표시
chars, labels, slash_before, para_before = [], [], set(), set()
run = 0
pending_slash = False
pending_para = False
last_kind = None
for kind, text, num in toks:
    if kind == 'plain':
        for ch in text:
            if ch == '/':
                pending_slash = True; continue
            if ch == '*':
                pending_para = True; continue
            n = norm(ch)
            if not n: continue
            if last_kind != 'U':
                run += 1
            if pending_slash: slash_before.add(len(chars)); pending_slash = False
            if pending_para: para_before.add(len(chars)); pending_para = False
            chars.append(n); labels.append(('U', run)); last_kind = 'U'
    else:
        lab = ('P', num) if kind == 'photo' else ('S', 0)
        first = True
        for ch in text:
            n = norm(ch)
            if not n: continue
            if pending_para: para_before.add(len(chars)); pending_para = False
            if pending_slash: slash_before.add(len(chars)); pending_slash = False
            chars.append(n); labels.append(lab)
        last_kind = kind
ustr = ''.join(chars)

# 3) 2판 자막 조각 글자열
pieces = []  # (sent_no, piece_idx, text, pos)
sn = 0
for sec in d.SECTIONS:
    for s in sec['sents']:
        sn += 1
        for pi, (t, p) in enumerate(s):
            pieces.append((sn, pi, t, p))
pchars, powner = [], []
for k, (sn, pi, t, p) in enumerate(pieces):
    for ch in norm(t):
        pchars.append(ch); powner.append(k)
pstr = ''.join(pchars)

sm = difflib.SequenceMatcher(None, ustr, pstr, autojunk=False)
umap = [None] * len(ustr)  # user idx -> piece char idx
for a, b, size in sm.get_matching_blocks():
    for j in range(size):
        umap[a + j] = b + j
print('맞은 글자', sum(1 for x in umap if x is not None), '/', len(ustr), '조각 글자', len(pstr))
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag != 'equal':
        print(' 차이', tag, repr(ustr[i1:i2]), '→', repr(pstr[j1:j2]))

# 4) 조각 글자마다 칸 붙이기(맞지 않은 글자는 앞 글자의 칸)
plab = [None] * len(pstr)
pslash = set(); ppara = set()
for ui, pj in enumerate(umap):
    if pj is None: continue
    plab[pj] = labels[ui]
    if ui in slash_before: pslash.add(pj)
    if ui in para_before: ppara.add(pj)
for j in range(len(plab)):
    if plab[j] is None:
        plab[j] = plab[j - 1] if j else labels[0]

# 5) 조각별 칸, 조각 안에서 칸이 바뀌는 곳
res = []
for k, (sn, pi, t, p) in enumerate(pieces):
    idx = [j for j, o in enumerate(powner) if o == k]
    labs = [plab[j] for j in idx]
    segs = []
    for j, l in zip(idx, labs):
        key = l if l[0] != 'U' else ('U', l[1])
        brk = (j in pslash)
        if not segs or segs[-1]['lab'] != key or brk:
            segs.append({'lab': key, 'from': j - idx[0], 'slash': brk, 'para': j in ppara})
        else:
            pass
    res.append({'k': k, 'sent': sn, 'pi': pi, 'text': t, 'pos': p, 'segs': segs})
json.dump(res, open('pieces_marked.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=0)

def lab_s(l):
    return f"사진{l[1]}" if l[0] == 'P' else ('특별' if l[0] == 'S' else f"스톡run{l[1]}")
for r in res:
    segs = r['segs']
    if len(segs) == 1:
        s = segs[0]
        flag = (' /' if s['slash'] else '') + (' *' if s['para'] else '')
        print(f"[{r['sent']}.{r['pi']}] {r['pos']} {lab_s(s['lab'])}{flag} | {r['text']}")
    else:
        parts = []
        for a, s in enumerate(segs):
            end = segs[a + 1]['from'] if a + 1 < len(segs) else None
            nt = norm(r['text'])
            parts.append(f"{lab_s(s['lab'])}{' /' if s['slash'] else ''}:{nt[s['from']:end]}")
        print(f"[{r['sent']}.{r['pi']}] {r['pos']} 조각 안에서 바뀜 → " + ' | '.join(parts))
