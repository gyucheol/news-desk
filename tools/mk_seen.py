"""이미 처리한 주소 목록(work/seen.txt, work/seen_urls.txt)을 DB 사본의 meta/newsSeenOld*·newsSeen에서 만든다.
사용: python3 -I tools/mk_seen.py <DB 사본 폴더>   (newsSeenOld, newsSeenOld2, 3, 4 … 다음 newsSeen 순서로 합침. 같은 주소는 처음 것만)"""
import json, glob, os, re, sys
DB = sys.argv[1]
R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'work')
olds = sorted(glob.glob(f'{DB}/meta/newsSeenOld*.json'), key=lambda p: int(re.sub(r'\D', '', os.path.basename(p)) or 1))
L = []
for p in olds + [f'{DB}/meta/newsSeen.json']:
    L += json.load(open(p))['lines']; print(os.path.basename(p), len(json.load(open(p))['lines']))
seen, S = [], set()
for l in L:
    u = l.rsplit(' | ', 1)[-1].strip()
    if u in S: continue
    S.add(u); seen.append(l)
open(f'{R}/seen.txt', 'w').write('\n'.join(seen) + '\n')
open(f'{R}/seen_urls.txt', 'w').write('\n'.join(l.rsplit(' | ', 1)[-1].strip() for l in seen) + '\n')
print(len(seen))
