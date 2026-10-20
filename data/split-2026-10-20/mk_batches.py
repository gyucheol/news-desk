"""저장 batch 목록 만들기: batch/B01.json … (50건·900KB 이하). 뉴스 → chains → 삭제·meta(마지막)."""
import json, glob, os
H = os.path.abspath('.')
V = json.load(open('scratch/versions.json'))
W = []
def add(op, col, did, path=None, ver=None):
    e = {'op': op, 'collection': col, 'doc_id': did}
    if path: e['file_path'] = path
    if ver: e['if_version'] = ver
    W.append((e, os.path.getsize(path) if path else 100))
for p in sorted(glob.glob(f'{H}/newsdocs/*.json')):
    i = os.path.basename(p)[:-5]; add('set', 'news', i, p, V['news'].get(i))
for p in sorted(glob.glob(f'{H}/chains_out/*.json')):
    i = os.path.basename(p)[:-5]; add('set', 'chains', i, p, V['chains'][i])
last = [(dict(op='delete', collection='news', doc_id=i, if_version=V['news'][i]), 100) for i in open('deletes.txt').read().split()]
for p in sorted(glob.glob(f'{H}/meta_out/*.json')):
    i = os.path.basename(p)[:-5]; last.append(({'op': 'set', 'collection': 'meta', 'doc_id': i, 'file_path': p, 'if_version': V['meta'][i]}, os.path.getsize(p)))
B, cur, sz = [], [], 0
for e, s in W:
    if cur and (len(cur) >= 50 or sz + s > 880000): B.append(cur); cur, sz = [], 0
    cur.append(e); sz += s
if cur: B.append(cur)
# 마지막: 삭제 + meta (크기 때문에 둘로 나뉠 수 있음 — 삭제는 meta와 같은 마지막 batch에)
cur, sz = [], 0; tail = []
for e, s in last:
    if cur and sz + s > 880000: tail.append(cur); cur, sz = [], 0
    cur.append(e); sz += s
tail.append(cur); B += tail
os.makedirs('batch', exist_ok=True)
for f in glob.glob('batch/*.json'): os.remove(f)
for n, b in enumerate(B, 1): json.dump(b, open(f'batch/B{n:02d}.json', 'w'), ensure_ascii=False)
print(len(B), [len(b) for b in B])
