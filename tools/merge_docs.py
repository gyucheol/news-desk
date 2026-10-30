"""이미 따로 저장된 비슷한 뉴스를 소급해 한 문서로 묶는다(흡수한 문서는 지울 대상).
사용(작업 폴더 안에서): python3 -I ../../tools/merge_docs.py <DB 사본 폴더> <processed 날짜>
입력: merged.json — [{gid, keep, absorb: [id...], title, one, facts, basis, check}] (title·one·facts는 묶음 전체로 새로 쓴 값)
결과: newsdocs/<id>.json(고친 keep 문서, dupOf를 고친 다른 문서), deletes.txt(지울 id), meta_out/newsSeen·newsSeenOld(흡수된 id를 keep id로 바꿈)
DB에 쓰지는 않는다."""
import json, glob, os, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from bundle_attach import absorb, now_kst

DB, TODAY = sys.argv[1], sys.argv[2]
NOW = now_kst()
news = {os.path.basename(p)[:-5]: json.load(open(p)) for p in glob.glob(f'{DB}/news/*.json')}
P, out, dels, moved = [], {}, [], {}
for g in json.load(open('merged.json')):
    keep, ab = g['keep'], g['absorb']
    if keep not in news or any(a not in news for a in ab): P.append(f"{g['gid']}: 없는 문서"); continue
    if set(ab) & (set(dels) | set(out)) or keep in dels: P.append(f"{g['gid']}: 다른 묶음과 겹침"); continue
    for a in ab:
        if news[a].get('detail') or news[a].get('insight2'): P.append(f"{g['gid']}: {a}에 자세한 정리·인사이트가 있음")
    one = re.sub(r' \((제목 기준|채널 전언)\)$', '', g['one'])
    if not 85 <= len(one) <= 165: P.append(f"{g['gid']}: 한줄 {len(one)}자")
    if not one.endswith('다'): P.append(f"{g['gid']}: 한줄 끝맺음")
    if not 12 <= len(g['title']) <= 60: P.append(f"{g['gid']}: 제목 {len(g['title'])}자")
    for f in g['facts']:
        if '|' in f or '**' in f: P.append(f"{g['gid']}: facts 기호")
    fields = {k: g[k] for k in ('title', 'one', 'facts', 'basis', 'check')}
    out[keep] = absorb(news[keep], [news[a] for a in ab], fields, TODAY, NOW)
    dels += ab
    for a in ab: moved[a] = keep
# 흡수된 문서를 dupOf로 가리키던 다른 문서는 keep을 가리키게 한다
for i, d in news.items():
    if i in dels: continue
    tgt = moved.get(d.get('dupOf'))
    if tgt:
        d = out.get(i) or dict(d)
        if tgt == i: d.pop('dupOf', None)
        else: d['dupOf'] = tgt
        out[i] = d
# newsSeen 줄의 id도 keep으로 바꾼다(주소 중복 검사는 그대로, 에이전트가 grep으로 찾을 때 지운 id가 나오지 않게)
os.makedirs('newsdocs', exist_ok=True); os.makedirs('meta_out', exist_ok=True)
for f in glob.glob('newsdocs/*.json'): os.remove(f)
for name in ('newsSeen', 'newsSeenOld'):
    s = json.load(open(f'{DB}/meta/{name}.json')); n = 0
    for k, l in enumerate(s['lines']):
        p = l.split(' ')
        if len(p) > 2 and p[1] in moved: p[1] = moved[p[1]]; s['lines'][k] = ' '.join(p); n += 1
    if n: s['updated'] = TODAY; json.dump(s, open(f'meta_out/{name}.json', 'w'), ensure_ascii=False)
    print(name, '바꾼 줄', n, 'bytes', len(json.dumps(s, ensure_ascii=False).encode()))
for i, d in out.items(): json.dump(d, open(f'newsdocs/{i}.json', 'w'), ensure_ascii=False, indent=1)
open('deletes.txt', 'w').write(''.join(f'{i}\n' for i in dels))
print('PROBLEMS', len(P)); [print(' ', p) for p in P]
print('고친 문서', len(out), '지울 문서', len(dels), 'bytes', max((len(json.dumps(d, ensure_ascii=False).encode()) for d in out.values()), default=0))
