# 최종 대본 만들기: 사용자 대본(문단·문장부호 그대로) + 최종 영상 자막 줄(녹음대로)의 문장을 맞대어,
# 같은 문장은 대본 글자를 그대로 두고, 녹음에서 바뀐 문장은 자막 글자로 바꾸고, 녹음에만 있는 문장은 넣고, 녹음에 없는 문장은 뺌.
# usage: final_script.py script.txt lines.json out.txt report.txt
import json, re, sys, difflib
src, lines_p, outp, repp = sys.argv[1:5]
raw = open(src, encoding='utf-8').read()
paras = [p.strip() for p in re.split(r'\n\s*\n|\n', raw) if p.strip()]
SPLIT = re.compile(r'(?<=[.?!])["”’」』]?\s+|(?<=[.?!]["”’」』])')
def sents_of(p):
    out, buf = [], ''
    for tok in re.findall(r'[^.?!]*[.?!]+["”’」』]?|[^.?!]+$', p):
        t = tok.strip()
        if t:
            out.append(t)
    return out or [p]
orig = []          # (para index, sentence text)
for pi, p in enumerate(paras):
    for s in sents_of(p):
        orig.append((pi, s))
def norm(s):
    s = s.replace('•', '')
    return re.sub(r'[^0-9A-Za-z가-힣]', '', s)
L = json.load(open(lines_p, encoding='utf-8'))
fin = {}
for l in L:
    fin.setdefault(l['sent'], []).append(l)
fin_s = []
for k in sorted(fin):
    ps = sorted(fin[k], key=lambda l: l['pi'])
    text = ' '.join(p['text'] for p in ps)
    say = ' '.join(p.get('say', p['text']) for p in ps)
    fin_s.append((text, say))
A = [norm(s) for _, s in orig]
B = [norm(t) for t, _ in fin_s]
Bs = [norm(s) for _, s in fin_s]
# equal if either display or spoken form matches
B_key = [b if b in set(A) else (bs if bs in set(A) else b) for b, bs in zip(B, Bs)]
sm = difflib.SequenceMatcher(a=A, b=B_key, autojunk=False)
out = []   # (para index or None, text, tag)
rep = []
for tag, i1, i2, j1, j2 in sm.get_opcodes():
    if tag == 'equal':
        for i in range(i1, i2):
            out.append((orig[i][0], orig[i][1], 'same'))
    else:
        olds = [orig[i][1] for i in range(i1, i2)]
        news = [fin_s[j][0] for j in range(j1, j2)]
        if olds and ''.join(A[i1:i2]) in (''.join(B[j1:j2]), ''.join(Bs[j1:j2])):
            # 글자는 같고 문장 나눔·문장부호만 다름 -> 대본 그대로
            for i in range(i1, i2):
                out.append((orig[i][0], orig[i][1], 'same'))
            continue
        rep.append(f'[{tag}] 대본: ' + (' / '.join(olds) if olds else '(없음)') + '\n        녹음: ' + (' / '.join(news) if news else '(없음)'))
        used = set()
        for j in range(j1, j2):
            best, bi = 0.0, None
            for i in range(i1, i2):
                if i in used:
                    continue
                r = difflib.SequenceMatcher(a=A[i], b=B[j], autojunk=False).ratio()
                if r > best:
                    best, bi = r, i
            if bi is not None and best >= 0.6:
                used.add(bi)
                out.append((orig[bi][0], fin_s[j][0], 'changed'))
            else:
                out.append((None, fin_s[j][0], 'added'))
# rebuild paragraphs: consecutive sentences with the same para index join with a space; None (inserted) -> own paragraph
res, cur, cur_pi = [], [], object()
for pi, t, tag in out:
    if pi is None or pi != cur_pi:
        if cur:
            res.append(' '.join(cur))
        cur, cur_pi = [t], (object() if pi is None else pi)
    else:
        cur.append(t)
if cur:
    res.append(' '.join(cur))
open(outp, 'w', encoding='utf-8').write('\n\n'.join(res) + '\n')
open(repp, 'w', encoding='utf-8').write('\n'.join(rep) + '\n')
print('script sentences', len(orig), '| final sentences', len(fin_s), '| changed blocks', len(rep), '| paragraphs', len(res))
