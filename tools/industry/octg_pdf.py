import json, re, html, sys
C = '/home/user/news-desk/work/live28/chains/drilling.json'
CY = '/home/user/news-desk/work/live27/meta/cycle.json'
OUT = sys.argv[1]
d = json.load(open(C)); cy = json.load(open(CY))
stg = {s['n']: s for s in cy['stages']}
CIRC = ['', '①', '②', '③', '④', '⑤', '⑥', '⑦', '⑧']
node = [x for x in d['nodes'] if x['id'] == 'octg'][0]
cl = lambda s: re.sub(r'\{\{|\}\}', '', s or '')
def tx(s):
    s = html.escape(cl(s))
    return re.sub(r'\s*\[(사실|귀납|연역|유추|추측|채널|제목|추론|미확인)([^\]]*)\]', r' <span class="lb">\1\2</span>', s)
def srcname(o):
    o = o or ''
    if re.match(r'텔레그램 (새|TG) #', o): return '텔레그램'
    if re.match(r'로이터 RTR #', o): return '로이터'
    return o
def src(lst):
    out = []
    for x in lst or []:
        u = x.get('u', '')
        out.append(f'<div class="src">출처: {html.escape(srcname(x.get("o")))}{" · " + x["d"] if x.get("d") else ""}<br><a href="{html.escape(u)}">{html.escape(u)}</a></div>')
    return ''.join(out)
def li(t, s=None): return f'<li><p>{tx(t)}</p>{src(s)}</li>'

intro = d['intro']
term = [t for t in intro['terms'] if 'OCTG' in t['k']][0]
money = [x for x in re.split(r'(?<=다\.)\s+', cl(intro['money'])) if '강관' in x]
reading = [r for r in intro['reading'] if r['news'].startswith('미국 리그 수 증가')][0]
watch = [w for w in intro['watch'] if 'OCTG' in w['n']]
ts = [p for p in intro['players'] if p['t'] == 'TS'][0]
summ = [x for x in re.split(r'(?<=다\.)\s+', cl(d['summary'])) if x.startswith('OCTG')]
ins = d['insight']
INS = [('산업·밸류체인의 구조적 변화', [ins['a'][3]]),
       ('정반대로 흐른다면, 그 이유', ins['b2'][:3]),
       ('이 흐름과 정반대되는 정보', [ins['c'][2]])]
for _, xs in INS:
    for x in xs: assert re.search('OCTG|강관|세아', cl(x['t'])), x
flows = sorted([f for f in d['flows'] if f.get('node') == 'octg'], key=lambda f: f['d'], reverse=True)
gaps = cl(d['gaps'])
g3 = re.search(r'\(3\)[^()]*?(\([^)]*\)[^()]*?)*?(?=\(4\))', gaps).group(0).strip()
g4 = re.search(r'\(4\)[^(]*?(?=, 삼성중공업)', gaps).group(0).strip()
cyc = d['cycle']

H = []
H.append(f'''<!doctype html><html lang="ko"><head><meta charset="utf-8"><title>강관(OCTG) 한 페이지</title><style>
@font-face{{font-family:P;src:url("file:///home/user/news-desk/design/fonts/PretendardVariable.woff2") format("woff2");font-weight:100 900}}
@page{{size:A4;margin:16mm 15mm 16mm 15mm}}
body{{font-family:P,sans-serif;font-size:10.2pt;line-height:1.62;color:#222;word-break:keep-all;overflow-wrap:anywhere}}
h1{{font-size:19pt;font-weight:650;margin:0 0 4px;color:#111}}
.sub{{color:#666;font-size:9pt;margin:0 0 14px}}
h2{{font-size:12.5pt;font-weight:620;margin:20px 0 8px;padding-bottom:4px;border-bottom:1px solid #ccc;color:#111;break-after:avoid}}
p{{margin:0 0 6px}} ul{{margin:0;padding-left:16px}} li{{margin:0 0 9px;break-inside:avoid}} li p{{margin:0}}
.lb{{font-size:8pt;color:#555;border:1px solid #bbb;border-radius:3px;padding:0 4px;white-space:nowrap}}
.src{{font-size:8pt;color:#777;margin-top:2px}} .src a{{color:#2a5db0;text-decoration:none;word-break:break-all}}
.box{{background:#f4f6f8;border-radius:6px;padding:10px 12px;margin:0 0 8px}}
.k{{color:#555}} .co{{margin:0 0 7px;break-inside:avoid}} .co .nm{{color:#111}} .tk{{color:#666;font-size:9pt}}
.foot{{margin-top:22px;font-size:8.3pt;color:#777;border-top:1px solid #ddd;padding-top:8px}}
</style></head><body>''')
H.append('<h1>강관(OCTG) — 산업 한 페이지 발췌</h1>')
H.append(f'<p class="sub">다운턴 뉴스 선별 데스크 · 「{html.escape(d["name"])}」 페이지의 OCTG·강관 부분 · 페이지 기준일 {d.get("asOf")} · PDF 작성 2026-10-19</p>')

H.append('<h2>한눈에 보기</h2><div class="box">')
H.append(f'<p><span class="k">강관 노드 위치:</span> {CIRC[node["stage"]]} {html.escape(stg[node["stage"]]["name"])} — {html.escape(node.get("stageNote",""))} (노드 위치는 참고용)</p>')
H.append(f'<p><span class="k">산업 전체 판정:</span> {CIRC[cyc["stage"]]} {html.escape(stg[cyc["stage"]]["name"])} (신뢰도 {html.escape(cyc.get("conf",""))}, 드릴십 일당이 이끈 판정)</p>')
for s in summ: H.append(f'<p>{tx(s)}</p>')
H.append('</div>')

H.append('<h2>강관이란</h2>')
H.append(f'<p>{tx(node["role"])}</p><p><span class="k">용어:</span> {tx(term["v"])}</p>')
for s in money: H.append(f'<p><span class="k">돈 버는 방식:</span> {tx(s)}</p>')

H.append('<h2>병목</h2>'); H.append(f'<p>{tx(node["bottleneck"])}</p>')

H.append('<h2>현재 상태</h2><ul>')
for s in sorted(node['state'], key=lambda x: x['d'], reverse=True):
    H.append(li(f'{s["d"]} — {s["t"]}', [{'o': s.get('o'), 'd': '', 'u': s.get('u')}]))
H.append('</ul>')

H.append('<h2>투자 인사이트 중 강관 관련</h2>')
for lab, xs in INS:
    H.append(f'<p class="k">{html.escape(lab)}</p><ul>')
    for x in xs: H.append(li(x['t'], x.get('src')))
    H.append('</ul>')

H.append(f'<h2>최근 흐름 ({len(flows)}줄, 최신순)</h2><ul>')
for f in flows: H.append(li(f'{f["d"]} — {f["t"]}', f.get('src')))
H.append('</ul>')

H.append('<h2>관련 기업</h2>')
H.append(f'<div class="co"><span class="nm">{html.escape(ts["n"])}</span> <span class="tk">{ts["t"]} · {ts["m"]}</span><br>{tx(ts["role"])}</div>')
for c in node['companies']:
    H.append(f'<div class="co"><span class="nm">{html.escape(c["n"])}</span> <span class="tk">{html.escape(c["t"])} · {html.escape(c["m"])}</span><br>{tx(c.get("note",""))}</div>')

H.append('<h2>이런 뉴스가 나오면</h2>')
H.append(f'<p><span class="k">뉴스:</span> {tx(reading["news"])}</p><p><span class="k">뜻:</span> {tx(reading["means"])}</p>')

H.append('<h2>볼 지표</h2><ul>')
for i in node['indicators']: H.append(f'<li><p>{tx(i["n"])} <span class="tk">— {html.escape(i["src"])}</span></p></li>')
for w in watch: H.append(f'<li><p>{tx(w["n"])} <span class="tk">— {html.escape(w["where"])}</span><br>{tx(w["why"])}</p></li>')
H.append('</ul>')

H.append('<h2>다른 노드와의 연결</h2><ul>')
for l in node['links']: H.append(f'<li><p><span class="k">{html.escape(l.get("to") or l.get("ext",""))}:</span> {tx(l["why"])}</p></li>')
H.append('</ul>')

H.append('<h2>확인하지 못한 것 (페이지 작성 기록에서)</h2><ul>')
H.append(f'<li><p>{tx(g3)}</p></li><li><p>{tx(g4)}…</p></li></ul>')

H.append('<p class="foot">이 PDF는 데스크 DB의 산업 한 페이지(해양시추·OCTG, chains/drilling)에서 강관 관련 부분만 옮긴 것이며 내용은 바꾸지 않았습니다(강조 표시만 지움). 근거 꼬리표: 사실=독립 출처로 확인, 채널=텔레그램 글에만 있음, 귀납·유추=추론. 한줄 요약과 산업 위치는 Claude가 조사 근거로 정리·판정한 것입니다. 블룸버그·로이터 원문은 직접 읽지 못해 독립 매체와 1차 출처로 확인했습니다. 투자 권유가 아닌 관찰 기록입니다.</p></body></html>')
open(OUT, 'w').write(''.join(H))
print('ok', len(flows), 'flows', len(node['state']), 'state')
