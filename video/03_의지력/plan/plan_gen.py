# 장면 표시 대본 만들기: plan_data(문장·조각) + plan_registry(재료) -> 번호 매기기, 점검, 마크다운 조각 출력
import json, sys, importlib.util, os
D = os.path.dirname(os.path.abspath(__file__))
def load(name):
    spec = importlib.util.spec_from_file_location(name, os.path.join(D, name + '.py'))
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
data, reg = load('plan_data'), load('plan_registry')
EXTRA = json.load(open(os.path.join(D, 'extra.json'), encoding='utf-8')) if os.path.exists(os.path.join(D, 'extra.json')) else {}
STOCKPICK = {x['shot']: x for x in json.load(open(EXTRA['stock_plan'], encoding='utf-8'))} if EXTRA.get('stock_plan') and os.path.exists(EXTRA['stock_plan']) else {}

POS = {'b': '아래', 'c': '가운데', 'i': '가운데 기울임'}
BG = {'prev': '앞 장면 이어서 흐리게', 'new': '새 그림 흐리게', 'black': '검은 화면'}

num = {'A': {}, 'S': {}, 'G': {}, 'P': {}}
uses = {'A': {}, 'S': {}, 'G': {}, 'P': {}}
problems = []

def split_vis(v):
    over = None
    if '+T:' in v:
        v, over = v.split('+T:')
    return v, over

def register(kind, key, sent_no):
    if key not in num[kind]:
        num[kind][key] = f"{kind}{len(num[kind]) + 1:02d}" if kind != 'P' else '실존 인물'
    uses[kind].setdefault(key, [])
    if sent_no not in uses[kind][key]:
        uses[kind][key].append(sent_no)
    return num[kind][key]

def label(kind, key):
    if kind == 'A': return reg.AI[key][1]
    if kind == 'S': return reg.STOCK[key]
    if kind == 'G': return reg.GRAPHICS[key]
    if kind == 'P': return reg.PEOPLE[key]

def describe(v, sent_no, first_time):
    """return text for a visual and the 'identity' used to detect scene changes"""
    v, over = split_vis(v)
    if v == 'K':
        return '검은 화면', 'K'
    if v.startswith('SPLIT:'):
        left, right = v[6:].split('|')
        parts = []
        ident = []
        for side, x in (('왼쪽', left), ('오른쪽', right)):
            if x == '-':
                parts.append(f'{side}은 아직 비움'); ident.append('-'); continue
            kind, key = x.split(':', 1)
            n = register(kind, key, sent_no)
            parts.append(f'{side} {n} {label(kind, key)}'); ident.append(n)
        return '화면 반 나누기: ' + ', '.join(parts), 'SPLIT:' + '|'.join(ident)
    kind, key = v.split(':', 1)
    n = register(kind, key, sent_no)
    txt = f'{n} {label(kind, key)}' if kind != 'P' else label(kind, key)
    if over:
        txt += f" + 그 말을 할 때 큰 글씨 '{over}'"
    return txt, n + (f'+{over}' if over else '')

out = []
stats = {'아래': 0, '가운데': 0, '가운데 기울임': 0}
scene_count = {'A': 0, 'S': 0, 'G': 0, 'K': 0, 'SPLIT': 0, 'P': 0}
sent_no = 0
prev_ident, prev_desc_base, prev_short = None, None, None
for sec in data.SECTIONS:
    out.append(f"### {sec['title']}" + (f" ({EXTRA['sec_time'][sec['title']]})" if EXTRA.get('sec_time', {}).get(sec['title']) else ''))
    for pieces in sec['sents']:
        sent_no += 1
        text = ' / '.join(p[0] for p in pieces)
        tt = EXTRA.get("sent_time", [])
        out.append(f"- [{sent_no}] " + (f"({tt[sent_no-1]}) " if len(tt) >= sent_no else "") + text)
        for (t, v, pos, bg) in pieces:
            if len(t) > 25:
                problems.append(f'[{sent_no}] 25자 넘음({len(t)}): {t}')
            if ',' in t:
                problems.append(f'[{sent_no}] 쉼표: {t}')
            if pos in ('c', 'i') and any(q in t for q in '"\'“”‘’'):
                problems.append(f'[{sent_no}] 가운데 따옴표: {t}')
            stats[POS[pos]] += 1
            if v == '=':
                if prev_ident is None:
                    problems.append(f'[{sent_no}] 첫 조각이 = 입니다')
                desc = f'{prev_short} 그대로'
                ident = prev_ident
            else:
                desc, ident = describe(v, sent_no, True)
                prev_desc_base = desc.split(' + ')[0]
                prev_short = ('검은 화면' if ident == 'K' else ('화면 반 나누기' if ident.startswith('SPLIT') else ('실존 인물 사진' if v.startswith('P:') else ident.split('+')[0])))
                if ident != prev_ident:
                    k = 'K' if ident == 'K' else ('SPLIT' if ident.startswith('SPLIT') else ('P' if v.startswith('P:') else ident[0]))
                    scene_count[k] += 1
            pos_txt = POS[pos]
            tail = f" · {pos_txt}" + (f" · {BG[bg]}" if bg else '')
            if pos in ('c', 'i') and not bg:
                problems.append(f'[{sent_no}] 가운데인데 배경 표시 없음: {t}')
            if v == 'K' and pos == 'b':
                problems.append(f'[{sent_no}] 검은 화면 아래 자막: {t}')
            if len(pieces) == 1:
                out.append(f"  - → {desc}{tail}")
            else:
                out.append(f"  - {t} → {desc}{tail}")
            prev_ident = ident
    out.append('')

open(os.path.join(D, 'scene_list.md'), 'w', encoding='utf-8').write('\n'.join(out))

# AI 사진 목록 (묶음별, 묶음 안에서는 기준 사진 먼저, 그다음 번호 순)
ai_out = []
for gid, gname, gset, person, same_people in reg.GROUPS:
    keys = [k for k in num['A'] if reg.AI[k][0] == gid]
    if not keys:
        continue
    keys.sort(key=lambda k: num['A'][k])
    ref = keys[0]
    ai_out.append(f"### 묶음 {gid[1:]}. {gname} ({', '.join(num['A'][k] for k in keys)})")
    ai_out.append(f"- 공통 설정: {gset}")
    ai_out.append(f"- 기준 사진: {num['A'][ref]} (이 묶음에서 가장 먼저 만들어 주세요)")
    for k in keys:
        n = num['A'][k]
        where = ', '.join(f'[{s}]' for s in uses['A'][k])
        if k == ref:
            prompt = f"{reg.LOOK} {gset}" + (f" {reg.PERSON}" if person else '') + f" 장면: {reg.AI[k][2]}"
        else:
            prompt = f"앞의 기준 사진과 같은 장소, 같은 사진 느낌" + (", 같은 인물로" if (same_people and '사람 없음' not in reg.AI[k][2]) else '으로') + f". 장면: {reg.AI[k][2]}"
        ai_out.append(f"- {n} {reg.AI[k][1]} (문장 {where})")
        ai_out.append(f"  - 요청문: {prompt}")
    ai_out.append('')
open(os.path.join(D, 'ai_list.md'), 'w', encoding='utf-8').write('\n'.join(ai_out))

st_out = []
for k in sorted(num['S'], key=lambda k: num['S'][k]):
    n = num['S'][k]
    where = ', '.join(f'[{s}]' for s in uses['S'][k])
    pick = STOCKPICK.get(k)
    if pick and pick.get('id'):
        seg = pick.get('segment') or []
        segtxt = f", 쓸 구간 {seg[0]}~{seg[1]}초" if len(seg) == 2 else ''
        alt = f", 대안 {pick['alt_id']}" if pick.get('alt_id') else ''
        note = f" ({pick['notes']})" if pick.get('notes') else ''
        st_out.append(f"- {n} {reg.STOCK[k]} (문장 {where}): Mixkit {pick['id']} {pick.get('title','')} {pick.get('url','')}{segtxt}, {pick.get('license','')}{alt}{note}")
    else:
        st_out.append(f"- {n} {reg.STOCK[k]} (문장 {where}): 고르는 중")
open(os.path.join(D, 'stock_list.md'), 'w', encoding='utf-8').write('\n'.join(st_out))

g_out = []
for k in sorted(num['G'], key=lambda k: num['G'][k]):
    g_out.append(f"- {num['G'][k]} {reg.GRAPHICS[k]} (문장 {', '.join(f'[{s}]' for s in uses['G'][k])})")
open(os.path.join(D, 'graphics_list.md'), 'w', encoding='utf-8').write('\n'.join(g_out))

summary = {'sentences': sent_no, 'subtitle_counts': stats, 'scene_counts': scene_count,
           'ai': len(num['A']), 'stock': len(num['S']), 'graphics': len(num['G']), 'people': len(num['P']),
           'problems': problems,
           'groups': {g[0]: [num['A'][k] for k in num['A'] if reg.AI[k][0] == g[0]] for g in reg.GROUPS},
           'stock_map': num['S'], 'ai_map': num['A']}
json.dump(summary, open(os.path.join(D, 'summary.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps({k: v for k, v in summary.items() if k not in ('stock_map', 'ai_map')}, ensure_ascii=False, indent=1))
