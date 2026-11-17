# 04편 전체 영상 v2 장면 명세 (2026-11-02). 부분 영상 v1(build_spec.py)과 같은 방식, 입력만 전체(lines_full, onsets_v2_full, segments_full).
# - 사용자 사진: 아주 천천히 확대만(초당 0.8%), 색은 거의 그대로(OWN).
# - 스톡: Mixkit 무료 라이선스 영상(stock/picks/group_*.json), 밝은 영상은 어둡게.
# - 가운데 자막(c, i)이 나오는 동안 그 장면의 그림을 흐리고 약간 어둡게. 장면이 가운데 자막으로 시작하면 처음부터 흐리게,
#   같은 장면에서 아래 자막이 2초 넘게 이어지면 다시 선명하게. 사용자 사진은 덜 흐리게.
# usage: build_spec_full.py  (ep4/v1에서) -> spec_full.json
import glob, json, os
L = json.load(open('lines_full.json', encoding='utf-8'))
O = {o['id']: o for o in json.load(open('onsets_v2_full.json', encoding='utf-8'))}
SEG = json.load(open('segments_full.json', encoding='utf-8'))
PICKS = {}
for p in sorted(glob.glob('stock/picks/group_*.json')):
    for x in json.load(open(p, encoding='utf-8')):
        PICKS[x['seg']] = x
OVR = json.load(open('stock_overrides.json', encoding='utf-8')) if os.path.exists('stock_overrides.json') else {}
DEFAULT_GRADE = {"sat": 0.88, "black": 0.02, "gamma": 1.12, "vignette": 0.35}
BRIGHT = {"sat": 0.8, "black": 0.06, "gamma": 1.45, "vignette": 0.55}
VBRIGHT = {"sat": 0.78, "black": 0.08, "gamma": 1.6, "vignette": 0.6}
OWN = {"sat": 0.95, "black": 0.01, "gamma": 1.05, "vignette": 0.3}
OWN_DIM = {"sat": 0.85, "black": 0.05, "gamma": 1.45, "vignette": 0.55}
OWN_BLUR = 6
KEEP_BLUR = 2.0


def soft_v(g):
    g = g or DEFAULT_GRADE
    out = {"sat": round(g["sat"] * 0.95, 3), "black": round(g["black"] + 0.02, 3),
           "gamma": round(g["gamma"] * 1.15, 3), "vignette": max(g["vignette"], 0.5)}
    if g.get("gain"):
        out["gain"] = g["gain"]
    return out


def stock_grade(pk):
    n = (pk.get('notes') or '').lower() + ' ' + (pk.get('grade_hint') or '').lower()
    if 'very bright' in n or ('daylight' in n and 'bright' in n):
        return VBRIGHT
    if 'bright' in n:
        return BRIGHT
    return DEFAULT_GRADE


def lid(i):
    return L[i]['id']


def soft_plan(i0, i1, t_end):
    cen = [L[i]['pos'] in 'ci' for i in range(i0, i1)]
    if not any(cen):
        return None
    starts = [O[lid(i)]['start'] for i in range(i0, i1)] + [t_end]
    first_c = cen.index(True)
    at = lid(i0 + first_c)
    starts_soft = first_c == 0
    until, k, second = None, first_c, False
    while k < len(cen):
        if not cen[k]:
            j = k
            while j < len(cen) and not cen[j]:
                j += 1
            if starts[j] - starts[k] >= KEEP_BLUR:
                if until is None:
                    until = lid(i0 + k)
                if j < len(cen):
                    second = True
            k = j
        else:
            k += 1
    return at, starts_soft, until, second


scenes, subs, notes = [], [], []
for d in SEG['segs']:
    i0, i1, t_end = d['i0'], d['i1'], d['t1']
    sid = f"s{d['n']:03d}"
    if d['kind'] == 'P':
        num = d['value']
        sc = {"id": sid, "type": "photo", "image": f"photos_final/P{num:02d}.png", "from": lid(i0),
              "z0": 1.0, "zoom_rate": 0.008, "grade": OWN, "note": f"사용자 사진 {num}"}
    else:
        st = d['value']
        pk = dict(PICKS.get(st, {}))
        pk.update(OVR.get(st, {}))
        pk = {k: v for k, v in pk.items() if v is not None}
        if not pk.get('id'):
            notes.append(f"{st}: no pick yet")
            sc = {"id": sid, "type": "card", "from": lid(i0), "note": f"{st} 스톡 없음(임시 검은 화면)"}
        else:
            g = dict(pk.get('grade') or stock_grade(pk))
            sc = {"id": sid, "type": "video", "src": f"stock/full/{pk['id']}.mp4", "in": float(pk.get('in', 0.0)),
                  "speed": float(pk.get('speed', 1.0) or 1.0), "from": lid(i0), "grade": g,
                  "note": f"{st} Mixkit {pk['id']} {pk.get('title', '')}"}
            for k in ('crop', 'blur', 'blur_box', 'cont'):
                if pk.get(k):
                    sc[k] = pk[k]
            bb = sc.get('blur_box')
            if bb and not isinstance(bb[0], (list, tuple)):
                # 고른 사람이 적은 1920x1080 픽셀 상자 [x0, y0, x1, y1] -> render.py 형식 [[x0, y0, x1, y1, sigma]] (화면 비율)
                sc['blur_box'] = [[round(bb[0] / 1920, 4), round(bb[1] / 1080, 4), round(bb[2] / 1920, 4), round(bb[3] / 1080, 4), 12]]
    if sc['type'] in ('photo', 'video'):
        sp = soft_plan(i0, i1, t_end)
        if sp:
            at, starts_soft, until, second = sp
            if sc['type'] == 'photo':
                mx = {"at": at, "dur": 0.5, "shift": -0.6 if starts_soft else -0.25, "grade": OWN_DIM, "blur": OWN_BLUR}
            else:
                mx = {"at": at, "dur": 0.5, "shift": -0.6 if starts_soft else -0.25, "grade": soft_v(sc['grade']), "blur": 10}
            if until:
                mx.update({"until": until, "until_shift": -0.25})
            sc['mix'] = mx
            if second:
                notes.append(f"{sid}: centre text again after a long bottom run (kept sharp there)")
    scenes.append(sc)
    for i in range(i0, i1):
        l = L[i]
        s = {"line": l['id'], "text": l['text']}
        if l['pos'] in 'ci':
            s['pos'] = 'center'
            if l['pos'] == 'i':
                s['italic'] = True
            if sc['type'] != 'card':
                s['shadow'] = True
        elif sc['type'] == 'card':
            s['box'] = False
        subs.append(s)
spec = {"sub_lead": 0, "fade_in": 0.3, "fade_out": 0.8, "last_sub_hold": 1.0, "scenes": scenes, "subs": subs}
json.dump(spec, open('spec_full.json', 'w'), ensure_ascii=False, indent=1)
print(len(scenes), 'scenes,', len(subs), 'subs;', sum(1 for s in scenes if s['type'] == 'video'), 'video,',
      sum(1 for s in scenes if s['type'] == 'photo'), 'photo,', sum(1 for s in scenes if s['type'] == 'card'), 'card')
for n in notes:
    print('NOTE', n)
