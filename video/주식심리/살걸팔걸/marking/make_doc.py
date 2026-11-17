# 대본_사진표시.md 만들기: marked.txt, marks.json(mark.py 출력), photos.py(사진 설명)를 합친다.
# 이 대본은 한 줄이 한 문단이다(수면 편 make_doc.py를 줄 단위로 바꿈).
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from photos import DESC

src = open(os.path.join(HERE, '..', '대본_최종_사용자.txt'), encoding='utf-8').read()
marked = open(os.path.join(HERE, 'marked.txt'), encoding='utf-8').read().rstrip('\n')
d = json.load(open(os.path.join(HERE, 'marks.json'), encoding='utf-8'))
num = d['num']; marks = d['marks']

paras = []; start = 0
for m in re.finditer(r'\n|\Z', src):
    if src[start:m.start()].strip():
        paras.append((start, m.start()))
    start = m.end()
def seg_start(e):
    a = next(a for a, b in paras if a < e <= b)
    prev = [x for _, _, x in marks if a < x < e]
    return max(prev) if prev else a
seen = {}; reuse = {}
for n, k, e in marks:
    if k in seen:
        t = src[seg_start(e):e].strip()
        t = t if len(t) <= 22 else t[:20].rstrip() + '…'
        reuse.setdefault(n, []).append(f"'{t}'")
    seen[k] = 1
inv = {v: k for k, v in num.items()}
photo_lines = []
for n in range(1, len(num) + 1):
    line = f'{n}. {DESC[inv[n]]}'
    if n in reuse:
        line += ' 다시 씀: ' + ', '.join(reuse[n]) + '.'
    photo_lines.append(line)

doc = open(os.path.join(HERE, 'doc_template.md'), encoding='utf-8').read()
doc = doc.replace('{{MARKED}}', marked).replace('{{PHOTOS}}', '\n'.join(photo_lines))
assert '{{' not in doc
open(os.path.join(HERE, '..', '대본_사진표시.md'), 'w', encoding='utf-8').write(doc)
print('photos', len(num), 'marks', len(marks), 'reuse spots', sum(len(v) for v in reuse.values()))
