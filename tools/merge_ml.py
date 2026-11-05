"""(2026-11-02판) 따로 저장된 같은 흐름 문서를 한 문서로 합친다. 여러 줄 요약 형식, vc·fed도 합침, 산업 페이지 nid·newsSeen* id를 keep으로 바꿈.
사용(작업 폴더 안에서): python3 -I ../../tools/merge_ml.py <DB 사본 폴더> <processed 날짜>
입력: merged.json — [{gid, keep, absorb, title, one, facts, basis, check, added}]
결과: newsdocs/<id>.json(고친 keep 문서), deletes.txt, meta_out/newsSeen*.json(바뀐 것만), chains_out/<id>.json(바뀐 것만). DB에 쓰지 않는다."""
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
    fields = {k: g[k] for k in ('title', 'one', 'facts', 'basis', 'check', 'added')}
    d = absorb(news[keep], [news[a] for a in ab], fields, TODAY, NOW)
    vc, seen = [], set()
    for x in [news[keep]] + [news[a] for a in ab]:
        for v in x.get('vc') or []:
            k = (v.get('ind'), v.get('node'), v.get('t'))
            if k not in seen: seen.add(k); vc.append(v)
    if vc: d['vc'] = vc
    fed, fs = [], set()
    for x in [news[keep]] + [news[a] for a in ab]:
        for f in x.get('fed') or []:
            k = (f.get('u'), f.get('t'))
            if k not in fs: fs.add(k); fed.append(f)
    if fed: d['fed'] = sorted(fed, key=lambda f: f.get('d', ''))
    out[keep] = d; dels += ab
    for a in ab: moved[a] = keep
for i, d in news.items():
    if i in dels: continue
    tgt = moved.get(d.get('dupOf'))
    if tgt:
        d = out.get(i) or dict(d)
        if tgt == i: d.pop('dupOf', None)
        else: d['dupOf'] = tgt
        out[i] = d
for k in ('newsdocs', 'meta_out', 'chains_out'):
    os.makedirs(k, exist_ok=True)
    for f in glob.glob(f'{k}/*.json'): os.remove(f)
pat = re.compile(r'"nid": "(n-(?:bbg|rtr|tg|fed)-\d{4})"')
for p in glob.glob(f'{DB}/chains/*.json'):
    s = open(p).read(); n = 0
    def sub(m):
        global n
        return f'"nid": "{moved[m.group(1)]}"' if m.group(1) in moved else m.group(0)
    s2 = pat.sub(sub, s)
    if s2 != s:
        c = json.loads(s2); c.pop('version', None); json.dump(c, open('chains_out/' + os.path.basename(p), 'w'), ensure_ascii=False)
        print('chains', os.path.basename(p)[:-5], sum(1 for m in pat.finditer(s) if m.group(1) in moved))
for p in glob.glob(f'{DB}/meta/newsSeen*.json'):
    s = json.load(open(p)); n = 0
    for k, l in enumerate(s['lines']):
        q = l.split(' ')
        if len(q) > 2 and q[1] in moved: q[1] = moved[q[1]]; s['lines'][k] = ' '.join(q); n += 1
    if n:
        s.pop('version', None); s['updated'] = TODAY
        json.dump(s, open('meta_out/' + os.path.basename(p), 'w'), ensure_ascii=False)
        print(os.path.basename(p), '바꾼 줄', n, 'bytes', len(json.dumps(s, ensure_ascii=False).encode()))
for i, d in out.items(): d.pop('version', None); json.dump(d, open(f'newsdocs/{i}.json', 'w'), ensure_ascii=False, indent=1)
open('deletes.txt', 'w').write(''.join(f'{i}\n' for i in dels))
print('PROBLEMS', len(P)); [print(' ', p) for p in P]
print('고친 문서', len(out), '지울 문서', len(dels), 'max bytes', max((len(json.dumps(d, ensure_ascii=False).encode()) for d in out.values()), default=0))
