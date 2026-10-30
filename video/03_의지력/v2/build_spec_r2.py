# 03편 v1 영상 장면 명세 (2026-10-29, 사용자가 대본에 표시해 보낸 AI 사진 75장 + 스톡).
# segments.json(seg_plan.py -> build_segments.py)의 장면 181개 -> spec.json (F의 연애 render.py 형식).
# - 사용자 사진: 아주 천천히 확대만(초당 0.8%, 최대 1.05배), 색은 거의 그대로(OWN).
# - 스톡: Mixkit 무료 라이선스 영상(stock/picks/group_*.json), 밝은 영상은 어둡게.
# - 검은 화면: 2판에서 검은 화면이던 질문·전환 문장(K).
# - 가운데 자막이 나오는 동안 그 장면의 그림을 흐리고 약간 어둡게(2판 2장 2번). 장면이 가운데 자막으로 시작하면 처음부터
#   흐리게, 같은 장면에서 아래 자막이 2초 넘게 이어지면 다시 선명하게. 사용자 사진은 덜 흐리게(F의 연애 v3~v5와 같음).
# - 큰 글씨: 2018년, 회복의 역설, 2002년, 실행 의도(2판 그대로), 그 말을 할 때 나타남.
# 03편 v2: 입력과 출력을 인자로 받음. usage: build_spec_r2.py lines.json onsets.json segments.json out_spec.json
import glob, json, os, re, sys

L = json.load(open(sys.argv[1], encoding='utf-8'))
O = {o['id']: o for o in json.load(open(sys.argv[2], encoding='utf-8'))}
SEG = json.load(open(sys.argv[3], encoding='utf-8'))
PICKS = {}
for p in sorted(glob.glob('stock/picks/group_*.json')):
    for x in json.load(open(p, encoding='utf-8')):
        PICKS[x['seg']] = x
OVR = json.load(open('stock_overrides.json', encoding='utf-8')) if os.path.exists('stock_overrides.json') else {}

DEFAULT_GRADE = {"sat": 0.88, "black": 0.02, "gamma": 1.12, "vignette": 0.35}
DARK = {"sat": 0.85, "black": 0.05, "gamma": 1.3, "vignette": 0.5}
BRIGHT = {"sat": 0.8, "black": 0.06, "gamma": 1.45, "vignette": 0.55}
VBRIGHT = {"sat": 0.78, "black": 0.08, "gamma": 1.6, "vignette": 0.6}
OWN = {"sat": 0.95, "black": 0.01, "gamma": 1.05, "vignette": 0.3}
OWN_DIM = {"sat": 0.85, "black": 0.05, "gamma": 1.45, "vignette": 0.55}
OWN_BLUR = 6
KEEP_BLUR = 2.0
# 03편 v2 (2026-10-30): 가운데로 옮긴 "다큐멘터리를 본 뒤에는 ~ 멈췄습니다." 밑의 흰 배경 실내 자전거 영상(st25, st26)은
# 흐림만으로는 흰 바탕에 흰 글씨라 읽기 어려워 밝기를 낮춤(render.py grade "gain", scripts_r2).
MIX_GAIN_R2 = {'st25': 0.45, 'st26': 0.45}
TITLES = {(59, 2): '2018년', (59, 4): '회복의 역설', (91, 0): '2002년', (96, 2): '실행 의도'}


def soft_v(g):
    g = g or DEFAULT_GRADE
    return {"sat": round(g["sat"] * 0.95, 3), "black": round(g["black"] + 0.02, 3),
            "gamma": round(g["gamma"] * 1.15, 3), "vignette": max(g["vignette"], 0.5)}


def stock_grade(pk):
    n = (pk.get('notes') or '').lower() + ' ' + (pk.get('grade_hint') or '').lower()
    if 'very bright' in n or 'daylight' in n and 'bright' in n:
        return VBRIGHT
    if 'bright' in n:
        return BRIGHT
    return DEFAULT_GRADE


def lid(i):
    return L[i]['id']


def soft_plan(i0, i1, t_end):
    """Centre-text softening for lines i0..i1-1: (at_line, starts_soft, until_line or None) or None."""
    cen = [L[i]['pos'] in 'ci' for i in range(i0, i1)]
    if not any(cen):
        return None
    starts = [O[lid(i)]['start'] for i in range(i0, i1)] + [t_end]
    first_c = cen.index(True)
    at = lid(i0 + first_c)
    starts_soft = first_c == 0
    # after the first centre line: find a bottom run of >= KEEP_BLUR s; centre after that would need a second softening
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
for d in SEG:
    i0, i1 = d['i0'], d['i1']
    t_end = d['t1']
    sid = f"s{d['n']:03d}"
    if d['kind'] == 'K':
        scenes.append({"id": sid, "type": "card", "from": lid(i0), "note": "검은 화면"})
    elif d['kind'] == 'P':
        num = d['value']
        sc = {"id": sid, "type": "photo", "image": f"photos_final/P{num:02d}.png", "from": lid(i0),
              "z0": 1.0, "zoom_rate": 0.008, "grade": OWN, "note": f"사용자 사진 {num}"}
        scenes.append(sc)
    else:
        st = d['value']
        pk = dict(PICKS.get(st, {}))
        pk.update(OVR.get(st, {}))
        if not pk.get('id'):
            notes.append(f"{st}: no pick yet")
            scenes.append({"id": sid, "type": "card", "from": lid(i0), "note": f"{st} 스톡 없음(임시 검은 화면)"})
        else:
            g = pk.get('grade') or stock_grade(pk)
            sc = {"id": sid, "type": "video", "src": f"stock/full/{pk['id']}.mp4", "in": float(pk.get('in', 0.0)),
                  "speed": float(pk.get('speed', 1.0) or 1.0), "from": lid(i0), "grade": g,
                  "note": f"{st} Mixkit {pk['id']} {pk.get('title', '')}"}
            for k in ('crop', 'blur', 'blur_box', 'cont'):
                if pk.get(k):
                    sc[k] = pk[k]
            scenes.append(sc)
    sc = scenes[-1]
    # big words (2판): split a scene where the second title starts (st35: same clip continues)
    # centre text softening
    if sc['type'] in ('photo', 'video'):
        sp = soft_plan(i0, i1, t_end)
        if sp:
            at, starts_soft, until, second = sp
            if sc['type'] == 'photo':
                mx = {"at": at, "dur": 0.5, "shift": -0.6 if starts_soft else -0.25, "grade": OWN_DIM, "blur": OWN_BLUR}
            else:
                mx = {"at": at, "dur": 0.5, "shift": -0.6 if starts_soft else -0.25, "grade": soft_v(sc['grade']), "blur": 10}
                if d['value'] in MIX_GAIN_R2:       # 03편 v2: 흰 배경 영상 위 가운데 자막이 읽히게 더 어둡게
                    mx['grade'] = dict(mx['grade'], gain=MIX_GAIN_R2[d['value']])
            if until:
                mx.update({"until": until, "until_shift": -0.25})
            sc['mix'] = mx
            if second:
                notes.append(f"{sid}: centre text again after a long bottom run (kept sharp there)")
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

# titles: attach to the scene that contains the line; st35 is split at (59,4) so each title has its own scene
key2line = {(l['sent'], l['pi']): l['id'] for l in L}
line2idx = {l['id']: i for i, l in enumerate(L)}
out_scenes = []
for sc in scenes:
    out_scenes.append(sc)
for (sn, pi), word in TITLES.items():
    lineid = key2line[(sn, pi)]
    li = line2idx[lineid]
    # the scene holding this line
    owner = max((s for s in out_scenes if line2idx[s['from']] <= li), key=lambda s: line2idx[s['from']])
    if owner.get('title'):
        # second title in the same scene: split the scene here, same clip/photo continues
        new = {k: v for k, v in owner.items() if k not in ('title', 'title_at', 'mix', 'id', 'from', 'note')}
        new.update({"id": owner['id'] + 'b', "from": lineid, "note": owner.get('note', '') + ' (이어짐)'})
        if new['type'] == 'video':
            new['cont'] = True
        else:
            notes.append(f"title split on a photo scene {owner['id']}")
        if owner.get('mix'):
            new['mix'] = owner['mix']
        new.update({"title": word, "title_at": lineid})
        out_scenes.insert(out_scenes.index(owner) + 1, new)
    else:
        owner.update({"title": word, "title_at": lineid})
spec = {"sub_lead": 0, "fade_in": 0.3, "fade_out": 0.5, "last_sub_hold": 1.0, "scenes": out_scenes, "subs": subs}
json.dump(spec, open(sys.argv[4], 'w'), ensure_ascii=False, indent=1)
# absolute paths for build_timeline.py (paths are relative to the spec there, so keep relative and run from here)
print(len(out_scenes), 'scenes,', len(subs), 'subs;', sum(1 for s in out_scenes if s['type'] == 'video'), 'video,',
      sum(1 for s in out_scenes if s['type'] == 'photo'), 'photo,', sum(1 for s in out_scenes if s['type'] == 'card'), 'card')
for n in notes:
    print('NOTE', n)
