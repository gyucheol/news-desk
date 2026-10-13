"""보강 결과(out/*.json)를 DB 사본에 반영한다. 사용(저장소 루트): python3 -I data/backfill-2026-10-13/apply_bf.py <원본 사본 폴더> <새 사본 폴더>
title·one(강조), added, items[].s만 바꾸고 updatedAt·processed는 건드리지 않는다. 바꾼 문서 id는 <새 사본>/backfilled.txt."""
import json, glob, os, shutil, sys
SRC, DST = sys.argv[1:3]
if os.path.exists(DST): shutil.rmtree(DST)
shutil.copytree(SRC, DST)
plain = lambda s: s.replace('{{', '').replace('}}', '')
done = []
for p in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'out', '*.json'))):
    for x in json.load(open(p, encoding='utf-8'))['docs']:
        f = f"{DST}/news/{x['id']}.json"; d = json.load(open(f, encoding='utf-8'))
        assert plain(x['title']) == d['title'] and plain(x['one']) == d['one'], x['id']
        d['title'] = x['title']; d['one'] = x['one']
        if d.get('headline') is not None: d['headline'] = x['title']
        if x.get('added'):
            d['added'] = x['added']
            s = {it['u']: it['s'] for it in x['items']}
            for it in d['items']:
                if it['u'] in s: it['s'] = s[it['u']]
        json.dump(d, open(f, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        done.append(x['id'])
open(f'{DST}/backfilled.txt', 'w').write('\n'.join(done) + '\n')
print('backfilled', len(done))
