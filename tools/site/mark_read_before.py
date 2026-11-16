"""이번 회차 전까지의 뉴스를 모두 읽음으로 만든 읽음 기록(data/users/me/reads) 문서를 만든다(2026-11-16 사용자 요청: "그 전까지 내용은 읽음처리").
사용: python3 -I tools/site/mark_read_before.py <받은 reads.json> <DB 사본 폴더> <이번 회차에 쓴 문서 id 파일> <출력 json>
- DB 사본의 뉴스 가운데 이번 회차에 새로 만들거나 기사를 더한 문서(id 파일)는 건드리지 않는다(안 읽음으로 남음).
- 나머지는 reads[id]를 max(기존 값, 지금 시각 ms, 그 문서 updatedAt ms)로 둔다. 다른 필드는 그대로 둔다.
- 출력은 문서 전체(version 제외). ArtifactData set(collection data/users/me, doc_id reads, if_version=받은 버전)으로 저장한다."""
import json, glob, os, sys, time
from datetime import datetime
src, db, excl, out = sys.argv[1:5]
doc = json.load(open(src)); doc.pop('version', None)
ids = dict(doc.get('ids', {}))
skip = set(open(excl).read().split())
now = int(time.time() * 1000)
def upd(d):
    u = d.get('updatedAt')
    return int(datetime.fromisoformat(u.replace('Z', '+00:00')).timestamp() * 1000) if u else 0
n_new = n_all = 0
for p in glob.glob(f'{db}/news/*.json'):
    d = json.load(open(p)); i = d.get('id') or os.path.basename(p)[:-5]
    if i in skip: continue
    n_all += 1
    u = upd(d)
    if not (ids.get(i) and ids[i] >= u): n_new += 1
    ids[i] = max(ids.get(i, 0), now, u)
doc['ids'] = ids
json.dump(doc, open(out, 'w'), ensure_ascii=False)
print('대상', n_all, '새로 읽음', n_new, '건너뜀(이번 회차)', len(skip), '전체 키', len(ids), 'bytes', os.path.getsize(out))
