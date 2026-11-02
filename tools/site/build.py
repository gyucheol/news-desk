"""데스크를 Claude 밖에서 볼 수 있는 정적 웹사이트로 만든다(GitHub Pages용).

사용: python3 -I tools/site/build.py <DB 사본 폴더> <출력 폴더>
  예) python3 -I tools/site/build.py work/live49 work/site
- DB 사본: ArtifactData list로 받은 폴더(news/, chains/, meta/cycle.json).
- 화면은 desk/index.html(데스크 게시본 원본)을 그대로 쓰고, tools/site/shim.js로 데이터 읽기를 data/*.json으로 바꾼다.
- 데스크와 같게 뉴스는 processed 최신순 1,000건만 넣는다.
- 요청 버튼(뉴스 내용 및 인사이트 요청)은 Claude 안에서만 동작하므로 숨긴다. 읽음 표시는 보는 브라우저에만 남는다.
"""
import json, glob, os, sys, shutil, re
from datetime import datetime, timezone, timedelta

R = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
DB, OUT = sys.argv[1], sys.argv[2]
KST = timezone(timedelta(hours=9))
stamp = datetime.now(KST).strftime('%Y-%m-%d %H:%M')

def docs(coll):
    out = []
    for p in sorted(glob.glob(f'{DB}/{coll}/*.json')):
        d = json.load(open(p))
        d.pop('version', None)
        d['id'] = d.get('id') or os.path.basename(p)[:-5]
        out.append(d)
    return out

news = docs('news')
news.sort(key=lambda d: str(d.get('processed') or ''), reverse=True)
news = news[:1000]
chains = docs('chains')
cyc = json.load(open(f'{DB}/meta/cycle.json')) if os.path.exists(f'{DB}/meta/cycle.json') else None
if cyc: cyc.pop('version', None)
assert news and chains, 'DB 사본에 news·chains가 없습니다'

os.makedirs(f'{OUT}/data', exist_ok=True); os.makedirs(f'{OUT}/fonts', exist_ok=True)
dump = lambda o, f: json.dump(o, open(f'{OUT}/data/{f}', 'w'), ensure_ascii=False, separators=(',', ':'))
dump(news, 'news.json'); dump(chains, 'chains.json'); dump(cyc, 'cycle.json')
shutil.copy(f'{R}/tools/site/shim.js', f'{OUT}/shim.js')
shutil.copy(f'{R}/design/fonts/PretendardVariable.woff2', f'{OUT}/fonts/PretendardVariable.woff2')
open(f'{OUT}/.nojekyll', 'w').close()

page = open(f'{R}/desk/index.html', encoding='utf-8').read()
head = ('<!doctype html>\n<html lang="ko">\n<head>\n<meta charset="utf-8">\n'
        '<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
        '<meta name="robots" content="noindex,nofollow">\n'
        '<meta name="apple-mobile-web-app-capable" content="yes">\n<meta name="mobile-web-app-capable" content="yes">\n'
        '<meta name="apple-mobile-web-app-title" content="뉴스 데스크">\n'
        '<meta name="theme-color" content="#101318">\n'
        '<style>.reqbar,[data-act="dreq"],[data-act="req"]{display:none!important}'
        '.sitenote{margin:0;color:var(--muted);font-size:13px}</style>\n'
        f'<script>window.SITE_BUILD={json.dumps(stamp)};</script>\n'
        '<script src="shim.js"></script>\n</head>\n<body>\n')
main = '<script>\n(() => {\n  const $ = id => document.getElementById(id);'
assert page.count(main) == 1, '데스크 원본의 본 스크립트 시작을 찾지 못했습니다'
note = (f'<p class="sitenote">웹 보기판 · 마지막 갱신 {stamp} (KST) · 읽음 표시는 이 기기에만 저장되고, '
        '요청 버튼은 Claude 데스크에서만 쓸 수 있습니다.</p>\n')
anchor = '<p class="status" id="status">'
assert page.count(anchor) == 1
page = page.replace(anchor, note + anchor)
open(f'{OUT}/index.html', 'w', encoding='utf-8').write(head + page + '\n</body>\n</html>\n')
print('news', len(news), 'chains', len(chains), 'cycle', bool(cyc), 'stamp', stamp,
      'size', {f: os.path.getsize(f'{OUT}/data/{f}') for f in os.listdir(f'{OUT}/data')})
