# 장면 표시 대본 만들기 (2판): plan_data(문장·자막 조각) + plan_scenes(장면마다 화면 하나) + plan_registry(재료)
# -> 번호 매기기(대본 순서), 점검, 장면 목록·AI 사진·스톡·그래픽 목록, summary.json, 스톡 고르기용 shots.md
import json, os, re, importlib.util
D = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(D, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
data, scn, reg = load('plan_data'), load('plan_scenes'), load('plan_registry')
EXTRA = json.load(open(os.path.join(D, 'extra.json'), encoding='utf-8'))
STOCKPICK = {}
SP = os.path.join(D, EXTRA['stock_plan']) if EXTRA.get('stock_plan') else None
if SP and os.path.exists(SP):
    STOCKPICK = {x['shot']: x for x in json.load(open(SP, encoding='utf-8'))}
START, END = EXTRA['piece_start'], EXTRA['video_end']
KEEP_BLUR = 2.0   # 가운데 자막 사이(또는 장면 끝)의 아래 자막이 이보다 짧으면 흐림을 풀지 않음
MARK = {'b': '(아래) ', 'c': '(가운데) ', 'i': '(기울임) '}
problems = []

# 1. 문장과 조각 펼치기
sents, pieces, sec_of = [], [], {}
for si, sec in enumerate(data.SECTIONS):
    for s in sec['sents']:
        n = len(sents) + 1
        idx = []
        for (t, pos) in s:
            pieces.append({'sent': n, 'k': len(idx), 'text': t, 'pos': pos, 'start': START[len(pieces)]})
            idx.append(len(pieces) - 1)
        sents.append(idx); sec_of[n] = si
assert len(pieces) == len(START), (len(pieces), len(START))
for a, b in zip(pieces, EXTRA['piece_text']):
    if a['text'].replace(' ', '') != b.replace(' ', ''):
        problems.append(f"시각 표와 자막이 다름: {a['text']} / {b}")
for i, p in enumerate(pieces):
    p['end'] = pieces[i + 1]['start'] if i + 1 < len(pieces) else END
    t = p['text']
    if len(t) > 25: problems.append(f"[{p['sent']}] 25자 넘음({len(t)}): {t}")
    if ',' in t: problems.append(f"[{p['sent']}] 쉼표: {t}")
    if p['pos'] in 'ci' and any(q in t for q in '"\'“”‘’'): problems.append(f"[{p['sent']}] 가운데 따옴표: {t}")

# 2. 장면 만들기
firsts = [x[0] for x in scn.SCENES]
if firsts[0] != 1 or firsts != sorted(set(firsts)) or firsts[-1] > len(sents):
    problems.append('장면 첫 문장 번호 순서가 이상함')
scenes = []
for k, (first, vis, opt) in enumerate(scn.SCENES):
    last = (firsts[k + 1] - 1) if k + 1 < len(firsts) else len(sents)
    pidx = [i for n in range(first, last + 1) for i in sents[n - 1]]
    sc = {'no': k + 1, 'first': first, 'last': last, 'vis': vis, 'opt': opt, 'pieces': pidx,
          'start': pieces[pidx[0]]['start'], 'end': (pieces[sents[last][0]]['start'] if last < len(sents) else END)}
    sc['dur'] = sc['end'] - sc['start']
    scenes.append(sc)
for a, b in zip(scenes, scenes[1:]):
    if a['vis'] == b['vis']:
        problems.append(f"장면 {a['no']}·{b['no']} 화면이 같음(합쳐야 함): {a['vis']}")

# 3. 번호(처음 나오는 순서)와 쓰는 곳
num = {'A': {}, 'S': {}, 'G': {}}
uses = {'A': {}, 'S': {}, 'G': {}}
def reg_use(kind, key, sc, side, t0, t1):
    if kind == 'A' and key not in reg.AI: problems.append(f'AI 키 없음: {key}')
    if kind == 'S' and key not in reg.STOCK: problems.append(f'스톡 키 없음: {key}')
    if kind == 'G' and key not in reg.GRAPHICS: problems.append(f'그래픽 키 없음: {key}')
    if key not in num[kind]:
        num[kind][key] = f'{kind}{len(num[kind]) + 1:02d}'
    uses[kind].setdefault(key, []).append({'scene': sc['no'], 'first': sc['first'], 'last': sc['last'], 'side': side, 'dur': t1 - t0})
def parse(v):
    kind, key = v.split(':', 1); return kind, key
for sc in scenes:
    v = sc['vis']
    if v == 'K':
        continue
    if v.startswith('SPLIT:'):
        L, R = v[6:].split('|')
        rs, rk = sc['opt']['right_at']
        t_right = pieces[sents[rs - 1][rk]]['start']
        sc['right_start'] = t_right
        sc['right_text'] = pieces[sents[rs - 1][rk]]['text']
        reg_use(*parse(L), sc, '왼쪽', sc['start'], sc['end'])
        reg_use(*parse(R), sc, '오른쪽', t_right, sc['end'])
    else:
        reg_use(*parse(v), sc, None, sc['start'], sc['end'])

def label(kind, key):
    return {'A': lambda k: reg.AI[k][1], 'S': lambda k: reg.STOCK[k], 'G': lambda k: reg.GRAPHICS[k]}[kind](key)
def short(kind, key):
    if kind == 'G':   # 그래픽은 설명이 길어 이름만
        return reg.GSHORT[key]
    if kind == 'S':   # 스톡 고를 때의 조건(괄호)은 목록에만
        return re.sub(r'\([^()]*\)$', '', reg.STOCK[key]).strip()
    return label(kind, key)
def vis_text(sc):
    v = sc['vis']
    if v == 'K': return '검은 화면'
    if v.startswith('SPLIT:'):
        L, R = v[6:].split('|')
        (lk, lkey), (rk_, rkey) = parse(L), parse(R)
        return (f"화면 반 나누기: 왼쪽 {num[lk][lkey]} {short(lk, lkey)}, 오른쪽 {num[rk_][rkey]} {short(rk_, rkey)}"
                f"('{sc['right_text']}'부터)")
    kind, key = parse(v)
    return f"{num[kind][key]} {short(kind, key)}"

# 4. 흐림: 가운데 자막에서 흐리게, 그 사이·장면 끝의 짧은 아래 자막은 흐린 채, 아래 자막이 2초 넘게 이어지면 다시 선명하게
for sc in scenes:
    ps = [pieces[i] for i in sc['pieces']]
    blur, on = [], False
    j = 0
    while j < len(ps):
        if ps[j]['pos'] in 'ci':
            on = True; blur.append(True); j += 1; continue
        r = j
        while r < len(ps) and ps[r]['pos'] == 'b': r += 1
        run = ps[r - 1]['end'] - ps[j]['start']
        keep = on and run < KEEP_BLUR
        blur += [keep] * (r - j)
        on = keep
        j = r
    sc['blur'] = blur
    if sc['vis'] == 'K':
        for p in ps:
            if p['pos'] == 'b': problems.append(f"[{p['sent']}] 검은 화면 아래 자막: {p['text']}")
    # 흐림 구간(영상 만들 때 씀)
    iv, cur = [], None
    for p, b in zip(ps, blur):
        if b and cur is None: cur = p['start']
        if not b and cur is not None: iv.append([round(cur, 3), round(p['start'], 3)]); cur = None
    if cur is not None: iv.append([round(cur, 3), round(sc['end'], 3)])
    sc['blur_iv'] = iv if sc['vis'] != 'K' else []

# 5. 장면 목록
fmt = lambda t: f'{int(t) // 60}:{int(t) % 60:02d}'
secs = lambda t: f'{max(1, round(t))}초'
def sent_line(n):
    out, prev = [], None
    for i in sents[n - 1]:
        p = pieces[i]
        m = '' if (prev is None and p['pos'] == 'b') or p['pos'] == prev else MARK[p['pos']]
        out.append(m + p['text']); prev = p['pos']
    return f"[{n}] " + ' / '.join(out)
sec_first = []
for si in range(len(data.SECTIONS)):
    sec_first.append(min(n for n in sec_of if sec_of[n] == si))
sec_time = {}
for si, sec in enumerate(data.SECTIONS):
    a = pieces[sents[sec_first[si] - 1][0]]['start']
    b = pieces[sents[sec_first[si + 1] - 1][0]]['start'] if si + 1 < len(sec_first) else END
    sec_time[sec['title']] = f'{fmt(a)}~{fmt(b)}'
out, cur_sec = [], None
for sc in scenes:
    for n in range(sc['first'], sc['last'] + 1):
        si = sec_of[n]
        if si != cur_sec:
            if cur_sec is not None: out.append('')
            title = data.SECTIONS[si]['title']
            out.append(f"### {title} ({sec_time[title]})")
            if n != sc['first']:
                out.append(f"- 장면 {sc['no']} 이어서 ({vis_text(sc)} 그대로)")
            cur_sec = si
        if n == sc['first']:
            head = f"- 장면 {sc['no']} ({fmt(sc['start'])}, {secs(sc['dur'])}) {vis_text(sc)}"
            big = sc['opt'].get('big')
            if big:
                head += ' + 큰 글씨 ' + ', '.join(f"'{w}'" + ('' if pieces[sents[bs - 1][bk]]['text'] == w else f"('{pieces[sents[bs - 1][bk]]['text']}'에서)") for bs, bk, w in big)
            if sc['opt'].get('note'):
                head += f" ({sc['opt']['note']})"
            out.append(head)
        out.append('  - ' + sent_line(n))
out.append('')
open(os.path.join(D, 'scene_list.md'), 'w', encoding='utf-8').write('\n'.join(out))

def where(kind, key, with_dur=False):
    parts = []
    for u in uses[kind][key]:
        rng = f"[{u['first']}]" if u['first'] == u['last'] else f"[{u['first']}]~[{u['last']}]"
        side = f" {u['side']}" if u['side'] else ''
        d = f", {secs(u['dur'])}" if with_dur else ''
        parts.append(f"장면 {u['scene']}{side}({rng}{d})")
    return ', '.join(parts)

# 6. AI 사진 목록 (묶음별, 묶음 안에서는 번호 순, 맨 앞이 기준 사진)
ai_out, person_in = [], []
for gid, gname, gset, person, same_people, standalone in reg.GROUPS:
    keys = sorted([k for k in num['A'] if reg.AI[k][0] == gid], key=lambda k: num['A'][k])
    if not keys: continue
    ref = keys[0]
    ai_out.append(f"### 묶음 {gid[1:]}. {gname} ({', '.join(num['A'][k] for k in keys)})")
    if standalone:   # 장소가 서로 다른 한 장씩: 요청문마다 장소를 다 적음
        ai_out.append(f"- 한 장씩 따로 만드는 묶음입니다. 주인공이 나오는 사진은 묶음 1의 주인공 사진({num['A']['sit_by_guitar']})을 함께 올리고 \"이 사진과 같은 사람으로\"를 앞에 붙여 주세요.")
        for k in keys:
            has_person = '사람 없음' not in reg.AI[k][2]
            prompt = f"{reg.LOOK} " + (f"{reg.PERSON} " if (person and has_person) else '') + reg.AI[k][2]
            if reg.PERSON in prompt: person_in.append(f"묶음 {gid[1:]}의 {num['A'][k]}")
            ai_out.append(f"- {num['A'][k]} {reg.AI[k][1]} (쓰는 곳: {where('A', k)})")
            ai_out.append(f"  - 요청문: {prompt}")
        ai_out.append('')
        continue
    ai_out.append(f"- 공통 설정: {gset}")
    ai_out.append(f"- 기준 사진: {num['A'][ref]} (이 묶음에서 가장 먼저 만들어 주세요)")
    seen = False   # 이 묶음에서 사람이 나온 사진이 이미 있는지
    for k in keys:
        has_person = '사람 없음' not in reg.AI[k][2]
        if k == ref:
            prompt = f"{reg.LOOK} {gset}" + (f" {reg.PERSON}" if (person and has_person) else '') + f" 장면: {reg.AI[k][2]}"
        elif has_person and person and not seen:   # 기준 사진에 사람이 없으면 처음 사람이 나오는 사진에 인물 카드
            prompt = f"앞의 기준 사진과 같은 장소, 같은 사진 느낌으로. {reg.PERSON} 장면: {reg.AI[k][2]}"
        else:
            prompt = "앞의 기준 사진과 같은 장소, 같은 사진 느낌" + (", 같은 인물로" if (same_people and has_person and seen) else '으로') + f". 장면: {reg.AI[k][2]}"
        seen = seen or has_person
        if reg.PERSON in prompt: person_in.append(f"묶음 {gid[1:]}의 {num['A'][k]}")
        ai_out.append(f"- {num['A'][k]} {reg.AI[k][1]} (쓰는 곳: {where('A', k)})")
        ai_out.append(f"  - 요청문: {prompt}")
    ai_out.append('')
open(os.path.join(D, 'ai_list.md'), 'w', encoding='utf-8').write('\n'.join(ai_out))

# 7. 스톡 목록 (필요한 길이 = 화면에 나오는 가장 긴 시간)
st_out, shots = [], []
for k in sorted(num['S'], key=lambda k: num['S'][k]):
    n = num['S'][k]
    need = max(u['dur'] for u in uses['S'][k])
    base = f"- {n} {reg.STOCK[k]} (쓰는 곳: {where('S', k, True)})"
    pick = STOCKPICK.get(k)
    if pick and pick.get('id'):
        seg = pick.get('segment') or []
        segtxt = f", {seg[0]}~{seg[1]}초 사용" if len(seg) == 2 else ''
        day = re.search(r'\d{4}-\d\d-\d\d', pick.get('license') or '')
        lic = f"무료 라이선스 확인 {day.group(0)}" if (day and 'Free' in pick['license']) else pick.get('license', '')
        alt = f", 대안 {pick['alt_id']}" if pick.get('alt_id') else ''
        note = f" {reg.STOCK_NOTE[k]}." if k in reg.STOCK_NOTE else ''
        st_out.append(f"{base}: Mixkit {pick['id']}{segtxt}.{note} {pick.get('url', '')} ({lic}{alt})")
    else:
        st_out.append(f"{base}: 고르는 중")
    shots.append({'shot': k, 'num': n, 'desc': reg.STOCK[k], 'need_s': round(need, 1),
                  'uses': [{'scene': u['scene'], 'sents': [u['first'], u['last']], 'side': u['side'], 'dur_s': round(u['dur'], 1)} for u in uses['S'][k]]})
open(os.path.join(D, 'stock_list.md'), 'w', encoding='utf-8').write('\n'.join(st_out))
json.dump(shots, open(os.path.join(D, 'shots_v2.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

g_out = []
for k in sorted(num['G'], key=lambda k: num['G'][k]):
    g_out.append(f"- {num['G'][k]} {reg.GSHORT[k]}: {reg.GRAPHICS[k]} (쓰는 곳: {where('G', k, True)})")
open(os.path.join(D, 'graphics_list.md'), 'w', encoding='utf-8').write('\n'.join(g_out))

# 8. 요약
counts = {'아래': 0, '가운데': 0, '가운데 기울임': 0}
for p in pieces: counts[{'b': '아래', 'c': '가운데', 'i': '가운데 기울임'}[p['pos']]] += 1
kinds = {'A': 0, 'S': 0, 'G': 0, 'K': 0, 'SPLIT': 0}
for sc in scenes:
    v = sc['vis']; kinds['K' if v == 'K' else ('SPLIT' if v.startswith('SPLIT') else v[0])] += 1
black_sents = [n for sc in scenes if sc['vis'] == 'K' for n in range(sc['first'], sc['last'] + 1)]
summary = {'sentences': len(sents), 'scenes': len(scenes), 'avg_s': round(END / len(scenes), 1),
           'scene_kinds': kinds, 'subtitle_counts': counts, 'ai': len(num['A']), 'stock': len(num['S']),
           'graphics': len(num['G']), 'black_sents': black_sents, 'problems': problems, 'sec_time': sec_time,
           'groups': {g[0]: [num['A'][k] for k in sorted(num['A'], key=lambda k: num['A'][k]) if reg.AI[k][0] == g[0]] for g in reg.GROUPS},
           'person_in': person_in, 'ai_map': num['A'], 'stock_map': num['S'], 'graphics_map': num['G'],
           'ai_uses': {k: [u['scene'] for u in v] for k, v in uses['A'].items()},
           'scene_rows': [{'no': sc['no'], 'sents': [sc['first'], sc['last']], 'vis': sc['vis'], 'start': round(sc['start'], 3),
                           'end': round(sc['end'], 3), 'blur': sc['blur_iv'], 'right_start': sc.get('right_start'),
                           'big': [[round(pieces[sents[bs - 1][bk]]['start'], 3), w] for bs, bk, w in sc['opt'].get('big', [])]} for sc in scenes]}
json.dump(summary, open(os.path.join(D, 'summary.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: summary[k] for k in ('sentences', 'scenes', 'avg_s', 'scene_kinds', 'subtitle_counts', 'ai', 'stock', 'graphics', 'problems')}, ensure_ascii=False))
