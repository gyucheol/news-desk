# -*- coding: utf-8 -*-
"""pharma.json 형식·강조 검사 (scratch)."""
import json, re, sys

P_OUT = "/home/user/news-desk/data/industry-2026-10-14/out/pharma.json"
d = json.load(open(P_OUT, encoding="utf-8"))
P, W = [], []
JOSA = set('은는이가을를에의와과도로만')
LBL = re.compile(r'\s*\[(사실|귀납|연역|유추|추측)[^\]]*\]\s*\.?\s*$')
strip = lambda s: s.replace('{{', '').replace('}}', '')

def sentences(s):
    p = LBL.sub('', strip(s)).strip()
    return [x for x in re.split(r'(?<=[.!?])\s+', p) if x]

def emph(name, s, lo=0.50, hi=0.65, strict=True):
    raw = s
    s = LBL.sub('', s)
    if raw.count('{{') != raw.count('}}') or re.search(r'\{\{[^}]*\{\{', raw) or re.search(r'\}\}[^{]*\}\}', raw) or '{{}}' in raw \
            or re.search(r'(?<!\{)\{(?!\{)|(?<!\})\}(?!\})', raw):
        P.append(f"{name}: 괄호 짝")
    marks = re.findall(r'\{\{(.+?)\}\}', s)
    plain = strip(s); n = len(plain); h = sum(len(m) for m in marks)
    r = h / max(1, n)
    for m in marks:
        if m != m.strip(): P.append(f"{name}: 공백 시작/끝 '{m}'")
        if re.search(r'\[(사실|귀납|연역|유추|추측)', m): P.append(f"{name}: 꼬리표 강조 '{m}'")
        if m.count('(') != m.count(')'): W.append(f"{name}: 괄호 안 닫힘 '{m}'")
        if len(m) > 30: W.append(f"{name}: 덩어리 김({len(m)}) '{m}'")
        if re.match(r'^[,.)·]|[,(·]$', m): W.append(f"{name}: 문장부호 시작/끝 '{m}'")
        if len(m) == 1 and m in JOSA: W.append(f"{name}: 조사 한 글자 '{m}'")
    if re.search(r'\}\}\{\{', raw): W.append(f"{name}: 강조가 붙어 있음")
    # 덩어리 바로 뒤 조사 안쪽 포함 검사: '{{...은}}' 같은 경우
    for m in marks:
        if len(m) >= 2 and m[-1] in '은는을를' and not re.search(r'[가-힣]{1}[은는을를]$', m[-2:]) is None:
            pass
    if strict and not (lo <= r <= hi): W.append(f"{name}: 강조 비율 {r:.0%} (목표 {lo:.0%}~{hi:.0%})")
    return n, h

def no_emph(name, obj):
    if '{{' in json.dumps(obj, ensure_ascii=False): P.append(f"{name}: 강조 금지 칸에 강조")

# ── 최상위 ──
need = ["id", "name", "short", "icon", "order", "asOf", "rev", "summary", "intro", "nodes", "cycle", "industryState", "insight", "flows", "gaps", "history"]
for k in need:
    if k not in d: P.append(f"최상위 칸 없음: {k}")
if d["id"] != "pharma": P.append("id")
if d["order"] != 21: P.append("order")
if len(d["short"]) > 6: P.append(f"short 길이 {len(d['short'])}")
if d["insight"] != {} or d["flows"] != []: P.append("insight/flows")
ns = len(sentences(d["summary"]))
if not 3 <= ns <= 5: P.append(f"summary 문장 {ns}")
tot = hl = 0
n, h = emph("summary", d["summary"]); tot += n; hl += h

# ── intro ──
it = d["intro"]
for k, (a, b) in {"what": (2, 3), "money": (2, 3), "drivers": (3, 4)}.items():
    c = len(sentences(it[k]))
    if not a <= c <= b: P.append(f"intro.{k} 문장 {c} (목표 {a}-{b})")
    n, h = emph(f"intro.{k}", it[k]); tot += n; hl += h
for k, (a, b) in {"watch": (3, 5), "players": (5, 8), "reading": (3, 5), "terms": (3, 6)}.items():
    if not a <= len(it[k]) <= b: P.append(f"intro.{k} 개수 {len(it[k])}")
for k in ["watch", "players", "terms"]:
    no_emph(f"intro.{k}", it[k])
for i, x in enumerate(it["watch"]):
    if set(x) != {"n", "why", "where"}: P.append(f"watch[{i}] keys")
for i, x in enumerate(it["players"]):
    if set(x) != {"n", "t", "m", "role"}: P.append(f"players[{i}] keys")
node_names = [nd["name"].split("(")[0] for nd in d["nodes"]]
for i, x in enumerate(it["reading"]):
    if set(x) != {"news", "means"}: P.append(f"reading[{i}] keys")
    no_emph(f"reading[{i}].news", x["news"])
    n, h = emph(f"reading[{i}].means", x["means"]); tot += n; hl += h
    if not re.search(r'노드', x["means"]): P.append(f"reading[{i}] 노드 이름 없음")
for i, x in enumerate(it["terms"]):
    if set(x) != {"k", "v"}: P.append(f"terms[{i}] keys")

# ── nodes ──
ids = [nd["id"] for nd in d["nodes"]]
if len(ids) != len(set(ids)): P.append("노드 id 중복")
if not 5 <= len(ids) <= 9: P.append(f"노드 수 {len(ids)}")
for nd in d["nodes"]:
    nid = nd["id"]
    if not re.fullmatch(r'[a-z]{2,12}', nid): P.append(f"노드 id 형식 {nid}")
    if len(nd["short"]) > 6: P.append(f"{nid}.short 길이 {len(nd['short'])}")
    for k in ["name", "short", "role", "bottleneck", "indicators", "companies"]:
        if k not in nd: P.append(f"{nid}: {k} 없음")
    rs = len(sentences(nd["role"]))
    if not 1 <= rs <= 2: P.append(f"{nid}.role 문장 {rs}")
    emph(f"{nid}.role", nd["role"], 0.45, 0.70)
    emph(f"{nid}.bottleneck", nd["bottleneck"], 0.45, 0.75)
    if not re.search(r'\[(사실|귀납|연역|유추|추측)[^\]]*\]\s*$', nd["bottleneck"]): W.append(f"{nid}.bottleneck 꼬리표 없음")
    if not 2 <= len(nd["indicators"]) <= 3: P.append(f"{nid}.indicators {len(nd['indicators'])}")
    if not 2 <= len(nd["companies"]) <= 5: P.append(f"{nid}.companies {len(nd['companies'])}")
    no_emph(f"{nid}.indicators", nd["indicators"])
    no_emph(f"{nid}.stageNote", nd.get("stageNote", ""))
    no_emph(f"{nid}.links", nd.get("links", []))
    for c in nd["companies"]:
        if set(c) != {"n", "t", "m", "note"}: P.append(f"{nid}.company keys {c.get('n')}")
        emph(f"{nid}.co.{c['t'] or c['n']}", c["note"], 0.40, 0.75)
    for l in nd.get("links", []):
        if "to" in l and l["to"] not in ("macro/fiscal", "macro/geo", "jpins/demand"): P.append(f"{nid}.links 허용 밖 {l['to']}")
    if "stage" in nd and nd["stage"] is not None and not 1 <= nd["stage"] <= 8: P.append(f"{nid}.stage")
    st = nd.get("state", [])
    if len(st) > 3: P.append(f"{nid}.state {len(st)}")
    for j, s in enumerate(st):
        if not s.get("o") or not s.get("u"): P.append(f"{nid}.state[{j}] o/u 없음")
        if not re.fullmatch(r'\d{4}-\d{2}(-\d{2})?', s.get("d", "")): P.append(f"{nid}.state[{j}] d 형식")
        if not LBL.search(s["t"]): W.append(f"{nid}.state[{j}] 꼬리표 없음")
        emph(f"{nid}.state[{j}]", s["t"], 0.40, 0.75)

# ── cycle ──
cy = d["cycle"]
if not (isinstance(cy["stage"], int) and 1 <= cy["stage"] <= 8): P.append("cycle.stage")
if cy["conf"] not in ("높음", "중간", "낮음"): P.append("cycle.conf")
if not 2 <= len(cy["why"]) <= 4: P.append(f"cycle.why {len(cy['why'])}")
for j, w in enumerate(cy["why"]):
    if not w.get("src"): P.append(f"why[{j}] src 없음")
    for s in w.get("src", []):
        if not s.get("o") or not s.get("u"): P.append(f"why[{j}] src o/u 없음")
    if not LBL.search(w["t"]): P.append(f"why[{j}] 꼬리표 없음")
    emph(f"why[{j}]", w["t"], 0.45, 0.75)
emph("cycle.next", cy["next"], 0.45, 0.75)
if not LBL.search(cy["next"]): P.append("next 꼬리표 없음")
if not 3 <= len(cy["watch"]) <= 5: P.append("cycle.watch 개수")
no_emph("cycle.watch", cy["watch"])
for sp in cy.get("split", []):
    for x in sp["nodes"]:
        if x not in ids: P.append(f"split 노드 {x}")

# ── industryState ──
if not 2 <= len(d["industryState"]) <= 5: P.append("industryState 개수")
for j, s in enumerate(d["industryState"]):
    if s.get("kind") not in ("price", "supply", "demand", "capex", "policy"): P.append(f"industryState[{j}].kind")
    if not s.get("o") or not s.get("u"): P.append(f"industryState[{j}] o/u")
no_emph("industryState", d["industryState"])
no_emph("gaps", d["gaps"]); no_emph("history", d["history"])

# ── 금지 도메인 ──
blob = json.dumps(d, ensure_ascii=False)
for bad in ["bloomberg.com", "reuters.com"]:
    if bad in blob: P.append(f"금지 도메인 주소 {bad}")

print(f"intro+summary 강조 비율 {hl / max(1, tot):.0%}")
print(f"PROBLEMS {len(P)}  WARN {len(W)}")
for x in P: print(" !", x)
for x in W: print(" ~", x)
if '-v' in sys.argv:
    for k in ["what", "money", "drivers"]:
        s = it[k]; marks = re.findall(r'\{\{(.+?)\}\}', s); print(k, f"{sum(map(len, marks)) / len(strip(s)):.0%}", ' / '.join(marks))
