"""upd_apply.py가 만든 save/·save_meta/를 ArtifactData batch 입력 파일로 나눈다(묶음당 1 MiB·50건 이하, chainsLog는 맨 마지막 묶음에 따로).
사용: python3 -I tools/industry/upd_batch.py <작업 폴더> <버전 파일>
버전 파일: {"chains/<id>": 버전, "meta/chainsLog": 버전} — DB를 받을 때 결과에 나온 version을 적은 것. 없는 문서가 있으면 멈춤.
결과: <작업 폴더>/batch/c1.json … (각 파일은 batch의 writes 배열 그대로)"""
import json, glob, os, sys
W, VF = os.path.abspath(sys.argv[1]), sys.argv[2]
ver = json.load(open(VF))
writes, miss = [], []
for f in sorted(glob.glob(f'{W}/save/*.json')):
    i = os.path.basename(f)[:-5]
    if f'chains/{i}' not in ver: miss.append(f'chains/{i}'); continue
    writes.append(({'op': 'set', 'collection': 'chains', 'doc_id': i, 'file_path': f, 'if_version': ver[f'chains/{i}']}, os.path.getsize(f)))
meta = f'{W}/save_meta/chainsLog.json'
if os.path.exists(meta) and 'meta/chainsLog' not in ver: miss.append('meta/chainsLog')
if miss: sys.exit('버전 없음: ' + ', '.join(miss))
LIM = 900_000
groups, cur, size = [], [], 0
for w, sz in writes:
    if cur and (size + sz > LIM or len(cur) >= 50): groups.append(cur); cur, size = [], 0
    cur.append(w); size += sz
if cur: groups.append(cur)
if os.path.exists(meta):
    groups.append([{'op': 'set', 'collection': 'meta', 'doc_id': 'chainsLog', 'file_path': meta, 'if_version': ver['meta/chainsLog']}])
os.makedirs(f'{W}/batch', exist_ok=True)
for k, g in enumerate(groups, 1):
    json.dump(g, open(f'{W}/batch/c{k}.json', 'w'), ensure_ascii=False)
    print(f'{W}/batch/c{k}.json', len(g), '건')
