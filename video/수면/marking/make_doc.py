# 대본_사진표시.md 만들기: marked.txt, marks.json(mark.py 출력), photos.py(사진 설명)를 합친다.
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from photos import DESC

src = open(os.path.join(HERE, '..', '대본_원본.txt'), encoding='utf-8').read()
marked = open(os.path.join(HERE, 'marked.txt'), encoding='utf-8').read().rstrip('\n')
d = json.load(open(os.path.join(HERE, 'marks.json'), encoding='utf-8'))
num = d['num']; marks = d['marks']

# 번호마다 다시 쓰는 자리(두 번째부터): 그 구간의 앞부분을 짧게
paras = []; start = 0
for m in re.finditer(r'\n\s*\n|\Z', src):
    paras.append((start, m.start())); start = m.end()
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
