"""작성 결과(out2)의 원문 주소가 후보(all.tsv)에 없으면, 그 묶음의 글 주소 중 가장 비슷한 것으로 바로잡는다(작성 에이전트가 주소를 옮겨 쓰다 바꾼 경우)."""
import json, glob, difflib
rows = {l.split('\t')[0]: l.rstrip('\n').split('\t') for l in open('all.tsv')}
U = {r[4] for r in rows.values()}
cl = {c['cid']: c for c in json.load(open('clusters.json'))['clusters']}
for p in sorted(glob.glob('out2/W*.json')):
    d = json.load(open(p)); ch = 0
    for x in d['items']:
        allowed = [rows[str(l)][4] for l in cl.get(x['cid'], {}).get('lines', [])]
        for it in x.get('items', []) + x.get('fed', []):
            if it.get('u') in U: continue
            m = difflib.get_close_matches(it.get('u', ''), allowed, 1, 0.6)
            print(p, x['cid'], it.get('u'), '->', m[0] if m else '없음')
            if m:
                old = it['u']; it['u'] = m[0]; ch += 1
                for f in x.get('fed', []):
                    if f.get('u') == old: f['u'] = m[0]
    if ch: json.dump(d, open(p, 'w'), ensure_ascii=False, indent=1)
