"""안 읽은 뉴스 문서 → 분야별 PDF용 HTML. 사용: python3 -I mk_pdf.py <DB 사본> <출력 html>
안 읽음 = reads.ids[id] < updatedAt(ms), 또는 reads에 없음. 문서마다 제목·여러 줄 요약·추가된 내용·사실·원문 목록(출처·날짜·링크)."""
import json, glob, html, re, sys, collections
from datetime import datetime
DB, OUT = sys.argv[1:3]
ids = json.load(open(f'{DB}/data/users/me/reads.json'))['ids']
NAME = {json.load(open(f))['id']: json.load(open(f)).get('name', '') for f in glob.glob(f'{DB}/chains/*.json')}
ORDER = ['macro', 'fin', 'semis', 'tech', 'oil', 'gas', 'power', 'coal', 'uranium', 'drilling', 'petchem', 'metals', 'industrial',
         'aero', 'auto', 'shipping', 'agri', 'pharma', 'consumer', 'beauty', 'realestate', 'jpins', 'utilities']
def ms(u):
    if isinstance(u, (int, float)): return u
    return datetime.fromisoformat(u.replace('Z', '+00:00')).timestamp() * 1000 if u else 0
cl = lambda s: re.sub(r'\{\{|\}\}', '', s or '')
def tx(s):
    s = html.escape(cl(s))
    return re.sub(r'\s*\[(사실|채널|제목|추론|미확인)\]', r' <span class="lb">\1</span>', s)
BAS = {'verified': '독립 출처 확인', 'partial': '일부 확인', 'channel': '채널 전언', 'title': '제목 기준'}
G = collections.defaultdict(list)
for f in glob.glob(f'{DB}/news/*.json'):
    d = json.load(open(f))
    if d['id'] in ids and ids[d['id']] >= ms(d.get('updatedAt')): continue
    inds = d.get('inds') or ['other']
    oth = [i for i in ORDER if i in inds and i != 'macro']
    g = oth[0] if oth else ('semis' if 'macro/semis' in (d.get('nodes') or []) else (inds[0] if inds[0] != 'other' or len(inds) == 1 else inds[0]))
    G[g].append(d)
key = lambda d: d.get('published') or d.get('processed') or ''
secs = [g for g in ORDER if g in G] + sorted(g for g in G if g not in ORDER)
n = sum(len(v) for v in G.values())
toc = ''.join(f'<li><a href="#s-{g}">{html.escape(NAME.get(g, g))}</a> {len(G[g])}건</li>' for g in secs)
body = []
for g in secs:
    body.append(f'<h2 id="s-{g}">{html.escape(NAME.get(g, g))} <span class="cnt">{len(G[g])}건</span></h2>')
    for d in sorted(G[g], key=key, reverse=True):
        lines = cl(d.get('one')).split('\n')
        one = ''.join(f'<p class="{"o1" if i == 0 else "o2"}">{html.escape(l)}</p>' for i, l in enumerate(lines))
        facts = ''.join(f'<li>{tx(x)}</li>' for x in d.get('facts') or [])
        its = d.get('items') or ([{'o': d.get('source', ''), 'd': (d.get('published') or '')[:10], 't': d.get('origTitle') or '', 'u': d.get('url', '')}] if d.get('url') else [])
        src = ''.join(f'<li>{html.escape(x.get("d", ""))} · {html.escape(x.get("o", ""))} · {html.escape(cl(x.get("t", "")))}<br><a href="{html.escape(x.get("u", ""))}">{html.escape(x.get("u", ""))}</a></li>' for x in its)
        add = f'<p class="add">추가된 내용: {html.escape(cl(d["added"]))}</p>' if d.get('added') else ''
        body.append(f'''<div class="doc"><h3>{html.escape(cl(d.get("title")))}</h3>
<div class="meta">{html.escape(key(d)[:16].replace("T", " "))} · {html.escape(BAS.get(d.get("basis"), d.get("basis", "")))} · 원문 {len(its)}건 · {d["id"]}</div>
<div class="one">{one}</div>{add}<ul class="facts">{facts}</ul><div class="srch">원문</div><ul class="src">{src}</ul></div>''')
css = '''@font-face{font-family:P;src:url("file:///home/user/news-desk/design/fonts/PretendardVariable.woff2") format("woff2");font-weight:100 900}
@page{size:A4;margin:14mm 14mm 14mm 14mm}
body{font-family:P,sans-serif;font-size:9.6pt;line-height:1.55;color:#222;word-break:keep-all;overflow-wrap:anywhere}
h1{font-size:17pt;margin:0 0 4mm}h2{font-size:13pt;border-bottom:1.5px solid #333;padding-bottom:1mm;margin:8mm 0 3mm;page-break-before:always}
.cnt{font-size:9pt;color:#666;font-weight:400}h3{font-size:10.8pt;margin:0 0 1mm}
.doc{border-top:1px solid #ddd;padding:3mm 0 2mm}h3,.meta,.one{break-after:avoid}.src li,.facts li{break-inside:avoid}.meta{font-size:8pt;color:#777;margin-bottom:1.5mm}
.one p{margin:0}.o1{font-weight:600}.o2{padding-left:2mm}.add{background:#f4f4f4;padding:1mm 2mm;margin:1.5mm 0;font-size:9pt}
.facts{margin:1.5mm 0 1mm;padding-left:5mm}.facts li{margin:0.4mm 0}.lb{font-size:7.5pt;color:#666;border:1px solid #bbb;border-radius:2px;padding:0 1px}
.srch{font-size:8pt;color:#555;font-weight:600}.src{margin:0.5mm 0 0;padding-left:5mm;font-size:8pt;color:#444}.src a{color:#2a5db0;word-break:break-all}
.toc{columns:2;font-size:10pt}'''
open(OUT, 'w').write(f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><style>{css}</style></head><body>
<h1>안 읽은 뉴스 {n}건</h1><p>기준: 2026-10-21 데스크 사본(읽음 기록 기준 안 읽은 문서). 분야별, 분야 안에서는 최신순.</p><ul class="toc">{toc}</ul>
{''.join(body)}</body></html>''')
print(n, {g: len(G[g]) for g in secs})
