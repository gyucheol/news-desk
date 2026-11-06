"""웹 보기판에서 복사해 온 '웹 읽음 N건: id id …' 글을 데스크 읽음 기록(data/users/me/reads)에 넣을 문서로 만든다.
사용: python3 -I tools/site/apply_reads.py <받아 둔 reads.json> <붙여 넣은 글 파일> <출력 json>
- 이미 읽음(reads[id]가 있고 그 값이 뉴스 updatedAt 이상)인 것은 그대로 두고, 나머지는 지금 시각(ms)으로 넣는다.
- 출력은 {"ids": {...}} 전체. ArtifactData update(collection data/users/me, doc_id reads, if_version=받은 버전)로 저장한다.
"""
import json, re, sys, time
src, txt, out = sys.argv[1:4]
doc = json.load(open(src)); ids = dict(doc.get('ids', {}))
want = sorted(set(re.findall(r'n-(?:bbg|rtr|tg|fed)-\d{4}', open(txt).read())))
now = int(time.time() * 1000); added = [k for k in want if not ids.get(k)]
for k in want: ids[k] = max(ids.get(k, 0), now)
json.dump({'ids': ids}, open(out, 'w'), ensure_ascii=False)
print('pasted', len(want), 'newly read', len(added), 'total', len(ids))
