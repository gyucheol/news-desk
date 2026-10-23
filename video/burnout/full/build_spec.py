# Build the full burnout episode spec (scenes + subtitles) from units.json and a material plan.
# Scene design follows the channel scene table (10장 3-2); materials: Mixkit Free stock, icon screens, black cards,
# AI photo-style images (work/img, gen_batch.py) and graphics (icons.py).
# v2 (2026-10-23 owner feedback): only the scene changes the owner listed (phone in bed, psychology, 1970s New York,
# a passionate person, bedridden, burnout title, 2019/WHO, research papers, news, interview background); turning the
# other abstract scenes into AI images comes later (owner, same day). U163-U164 cut; U105-U107, U229-U232 split as the
# owner marked; U188 shows no 그러니까; subtitles start on the voice onset (sub_lead 0, onsets.py + ctc_align.py).
# usage: build_spec.py <folder with units.json> [stock search index.json, adds clip titles as notes] -> <folder>/spec.json
import json, re, sys
F = sys.argv[1]
units = json.load(open(f"{F}/units.json"))
TXT = {u["id"]: u["text"] for u in units}

# subtitles show numbers as digits (user request 2026-10-22); ordinals and 한 번/한 발/하나 stay in words
DIGITS = [("여섯 시쯤", "6시쯤"), ("천구백칠십 년대", "1970년대"), ("열두 시간", "12시간"), ("새벽 두 시", "새벽 2시"),
          ("한두 시간씩", "1~2시간씩"), ("천구백칠십사 년", "1974년"), ("이천십구 년", "2019년"), ("세 가지", "3가지"),
          ("열 시간", "10시간"), ("한 시간째", "1시간째"), ("이천구 년", "2009년"), ("일곱 편", "7편"),
          ("여섯 가지", "6가지"), ("십이월", "12월"), ("스물여섯 살", "26살"), ("두 가지", "2가지"),
          ("십 점", "10점"), ("삼 점", "3점")]
EMPH = {"U047": "번아웃", "U094": "번아웃", "U106": "직장 스트레스", "U113": "질병", "U116": "직장", "U121": "배터리",
        "U127": "무언가", "U129": "3가지", "U131": "에너지", "U149": "꺼내 쓸 힘", "U152": "연료", "U154": "거리",
        "U166": "심리적 거리감", "U167": "냉소", "U176": "거리", "U178": "느낌", "U187": "직업적 효능감", "U195": "힘",
        "U202": "7편", "U206": "사라졌습니다", "U210": "첫 주", "U217": "일터", "U222": "어긋날 때", "U230": "의지",
        "U249": "열심히 살고 있는데도", "U259": "2가지", "U262": "10점 만점", "U267": "숫자 하나", "U281": "하나만",
        "U296": "배터리", "U305": "애써 온"}
DISPLAY = {"U188": "내가 해낼 수 있다는 믿음이"}                  # centre text without the spoken 그러니까 (owner)
ITALIC = {"U004", "U005", "U006", "U027", "U028", "U042", "U184"}            # inner thoughts on black cards

PAST = {"sat": 0.35, "black": 0.06, "gamma": 1.3, "vignette": 0.6}         # 1970s story: colour drained
BRIGHT = {"sat": 0.8, "black": 0.06, "gamma": 1.45, "vignette": 0.55}       # tame bright stock to the dark tone
DARK = {"sat": 0.85, "black": 0.05, "gamma": 1.3, "vignette": 0.5}

# (from unit, kind, arg, extra) — kind: v = stock video id, card, icon, photo = AI image id (AI_FILES)
# v1 full-res check (2026-10-22): heavy blur on 4766's staff photo (an older doctor who could pass for Freudenberger);
# light blur hides readable text/logos (42666 room name + TV logo, 914 monitor logos); crops cut a book title (50753)
# and a typewriter maker's logo; 99910 and 50112 start after a logo notebook / branded highlighter leaves the frame.
# v2 AI images: no faces that could pass for Freudenberger (backs, hands, covered faces) in his story.
# AI images: images/ next to spec.json (full/images/ in the repo, the 6 PNGs rendered in v2; gen_batch.py with
# full/ai_images.json makes them again into work/img/, slightly different on other library versions)
AI_FILES = {}                                      # filled in below from the chosen seeds
AI_SEED = {"A01": 1, "A02": 1, "A07": 21, "A11": 1, "A12": 1, "A16": 1}
for k, sd in AI_SEED.items():
    AI_FILES[k] = f"{k}_s{sd}.png"
KB = lambda d: {"z0": 1.0, "z1": 1.05, "cx0": 0.5 - 0.02 * d, "cx1": 0.5 + 0.02 * d}   # slow push-in with a small pan
PLAN = [
 # ① hook: the 30-second example the owner approved (sample30)
 ("U001", "v", "31411", {"in": 0.2}), ("U002", "v", "28899", {"in": 6.4, "speed": 1.6}), ("U004", "card", None, {}),
 ("U007", "v", "4548", {"in": 2.0, "grade": {"sat": 0.78, "black": 0.08, "gamma": 1.6, "vignette": 0.6}}),
 ("U009", "v", "51394", {"in": 8.0}),
 ("U010", "v", "4701", {"in": 0.4, "grade": {"sat": 0.88, "black": 0.03, "gamma": 1.22, "vignette": 0.45}}),
 ("U012", "icon", "bulb", {}), ("U014", "icon", "battery", {}),
 ("U016", "v", "4511", {"in": 0.0, "grade": {"sat": 0.85, "black": 0.05, "gamma": 1.35, "vignette": 0.5}}),
 ("U018", "v", "99909", {"in": 0.5}),
 # ② empathy: a week of a tired worker
 ("U019", "v", "4333", {"in": 5.0}), ("U019", "v", "144", {"in": 4.0, "offset": 1.2}),
 ("U020", "v", "1623", {"in": 1.0, "grade": DARK}),
 ("U022", "v", "4872", {"in": 1.0, "grade": BRIGHT}),
 ("U024", "v", "3428", {"in": 1.0, "grade": DARK}),
 ("U027", "card", None, {}),
 ("U029", "v", "31413", {"in": 0.0, "grade": DARK}),          # v2: lying down, staring at the phone (owner)
 ("U033", "v", "42653", {"in": 0.5, "grade": DARK}), ("U034", "v", "100050", {"in": 1.0, "grade": DARK}),
 ("U036", "v", "50931", {"in": 1.0, "grade": BRIGHT}), ("U037", "v", "4548", {"in": 9.0, "grade": {"sat": 0.78, "black": 0.08, "gamma": 1.6, "vignette": 0.6}}),
 ("U038", "v", "42896", {"in": 2.0, "grade": BRIGHT}), ("U039", "card", None, {}),
 ("U040", "v", "4513", {"in": 1.0, "grade": DARK}), ("U042", "card", None, {}), ("U043", "icon", "clock6", {}),
 # ③ the name and Freudenberger's story
 ("U046", "card", None, {}),
 ("U048", "photo", "A01", {"grade": PAST, **KB(1)}),          # psychology: a therapy room (owner)
 ("U049", "icon", "freud_card", {}),                          # no freely licensed photo of him: profile card
 ("U051", "photo", "A02", {"grade": PAST, **KB(-1), "title": "1970년대", "title_sub": "뉴욕"}),
 # passionate, dedicated (owner): hands typing late by candlelight, no face; the AI try showed two faces that could pass
 # for him (2026-10-23). The crop cuts the typewriter maker's logo, as in v1.
 ("U052", "v", "10395", {"in": 1.0, "grade": PAST, "crop": [0.0, 0.0, 0.94, 0.94]}),
 ("U054", "v", "28886", {"in": 1.0, "grade": PAST}),
 ("U056", "v", "4779", {"in": 1.0, "grade": PAST}),
 ("U058", "icon", "clock2", {}),
 ("U059", "v", "39841", {"in": 1.0, "grade": PAST}),
 ("U061", "v", "44579", {"in": 1.0, "grade": PAST}), ("U064", "v", "3461", {"in": 1.0}),
 ("U065", "v", "4701", {"in": 0.0, "grade": PAST}),
 ("U067", "photo", "A07", {"grade": PAST, **KB(1)}),          # bedridden, cannot move (owner)
 ("U071", "v", "425", {"in": 1.0, "grade": PAST}),
 ("U074", "v", "28893", {"in": 1.0, "grade": PAST}),
 ("U076", "v", "425", {"in": 8.0, "grade": PAST}), ("U078", "v", "1967", {"in": 1.0}),
 ("U081", "v", "4766", {"in": 6.5, "grade": PAST, "blur": 16}), ("U083", "v", "4607", {"in": 1.0, "grade": PAST}),
 ("U087", "v", "8744", {"in": 1.0, "grade": PAST}),
 ("U089", "v", "2707", {"in": 1.0}),
 ("U091", "v", "21587", {"in": 1.0, "grade": PAST}),
 ("U092", "photo", "A11", {"grade": PAST, **KB(1), "title": "번아웃", "title_size": 230, "title_delay": 1.2}),
 ("U095", "card", None, {}), ("U097", "v", "39841", {"in": 8.0, "grade": PAST}),
 # v2: runs on through U102 (owner). The crop cuts the word on the hoodie (Artisan), readable in v1 too.
 ("U100", "v", "50133", {"in": 1.0, "grade": DARK, "crop": [0.0, 0.0, 1.0, 0.74]}),
 # ③ WHO definition and the battery metaphor
 ("U103", "icon", "who2019", {}),                             # year + name; the WHO emblem needs WHO's permission
 ("U105", "card", None, {}), ("U108", "icon", "gauge", {}),
 ("U111", "card", None, {}), ("U115", "v", "914", {"in": 1.0, "grade": BRIGHT, "blur": 3}),
 ("U118", "v", "4915", {"in": 1.0, "grade": DARK}), ("U120", "icon", "battery", {}), ("U123", "icon", "phone_off", {}),
 ("U126", "icon", "apps", {}),
 # ④ three signs
 ("U128", "card", None, {}), ("U130", "card", None, {"label": "1 / 3"}),
 ("U132", "v", "50753", {"in": 1.0, "grade": DARK, "crop": [0.06, 0.0, 0.94, 0.88]}), ("U135", "v", "50754", {"in": 2.0, "grade": DARK}),
 ("U138", "v", "31413", {"in": 8.0, "grade": DARK}), ("U141", "icon", "battery2", {}), ("U146", "card", None, {}),
 ("U147", "v", "26090", {"in": 1.0, "grade": DARK}), ("U148", "icon", "fuel", {}),
 ("U153", "card", None, {"label": "2 / 3"}),
 ("U156", "v", "42666", {"in": 1.0, "grade": BRIGHT, "blur": 5}), ("U158", "v", "4607", {"in": 8.0, "grade": BRIGHT}),
 ("U160", "v", "4908", {"in": 1.0, "grade": DARK}), ("U162", "v", "4720", {"in": 1.0, "grade": DARK}),
 ("U165", "card", None, {}),
 ("U168", "v", "99909", {"in": 6.0}),
 ("U171", "v", "31412", {"in": 1.0, "grade": DARK}),
 ("U173", "v", "4893", {"in": 1.0, "grade": DARK}), ("U175", "v", "4511", {"in": 8.0, "grade": {"sat": 0.85, "black": 0.05, "gamma": 1.35, "vignette": 0.5}}),
 ("U177", "card", None, {"label": "3 / 3"}),
 ("U180", "v", "313", {"in": 1.0, "grade": BRIGHT}),
 ("U182", "v", "39841", {"in": 4.0, "grade": DARK}),
 ("U184", "card", None, {}), ("U185", "v", "4500", {"in": 1.0, "grade": DARK}), ("U187", "card", None, {}),
 ("U190", "v", "99890", {"in": 1.0, "grade": DARK}), ("U192", "v", "42655", {"in": 1.0, "grade": DARK}),
 ("U194", "icon", "bulb_dim", {}),
 # ⑤ does rest fix it
 ("U197", "card", None, {}), ("U198", "v", "1958", {"in": 1.0, "grade": BRIGHT}),
 ("U199", "photo", "A12", {"grade": DARK, **KB(1)}),          # research papers (owner)
 ("U201", "icon", "docs7", {}),
 ("U204", "v", "1013", {"in": 1.0, "grade": BRIGHT}), ("U205", "icon", "graph", {}), ("U207", "icon", "docs_many", {}),
 ("U210", "icon", "calendar", {}), ("U212", "icon", "bars", {}), ("U214", "card", None, {}),
 ("U215", "v", "914", {"in": 10.0, "grade": DARK, "blur": 3}), ("U218", "icon", "six", {}), ("U222", "icon", "six_off", {}),
 ("U224", "v", "100252", {"in": 1.0, "grade": DARK}), ("U225", "icon", "battery", {}),
 ("U227", "v", "1623", {"in": 8.0, "grade": DARK}), ("U229", "card", None, {}),
 # ⑥ a real story (potato character comes later)
 ("U231", "card", None, {}),
 ("U233", "icon", "news", {}),                                # news graphic (owner: 뉴스, 기사)
 ("U236", "v", "31415", {"in": 1.0, "grade": DARK}), ("U238", "v", "26089", {"in": 1.0, "grade": DARK}),
 ("U239", "v", "26090", {"in": 8.0, "grade": DARK}),
 ("U240", "v", "31411", {"in": 8.0}),
 ("U242", "v", "4720", {"in": 8.0, "grade": DARK}),
 ("U244", "photo", "A16", {"grade": {"sat": 0.7, "black": 0.08, "gamma": 1.9, "vignette": 0.6}, "blur": 9,
                           "z0": 1.05, "z1": 1.05, "center_subs": True}),   # the quote over the blurred, darkened interview (owner)
 ("U248", "card", None, {}),
 ("U251", "v", "3461", {"in": 6.0}), ("U254", "v", "50956", {"in": 8.0}),
 # ⑦ two small things to try
 ("U256", "card", None, {}), ("U261", "icon", "memo10", {}), ("U264", "v", "99910", {"in": 6.5, "grade": DARK}),
 ("U267", "card", None, {}), ("U268", "icon", "week", {}), ("U271", "icon", "week3", {}),
 ("U273", "v", "3977", {"in": 1.0}),
 ("U277", "icon", "six", {}), ("U280", "icon", "six_pick", {}),
 ("U282", "icon", "six_seq", {}), ("U285", "v", "50112", {"in": 4.3, "grade": DARK}),
 ("U289", "v", "52452", {"in": 1.0, "grade": DARK}),
 # ⑧ closing
 ("U292", "v", "28899", {"in": 1.0, "grade": DARK}), ("U294", "icon", "battery", {}),
 ("U298", "v", "100831", {"in": 0.0, "speed": 0.9}),
 ("U301", "v", "4548", {"in": 14.0, "grade": {"sat": 0.78, "black": 0.08, "gamma": 1.6, "vignette": 0.6}}),
 ("U304", "card", None, {}), ("U306", "v", "4397", {"in": 0.5, "grade": DARK}), ("U310", "v", "1086", {"in": 0.5, "grade": DARK}),
]

NOTES = {}
idx = {v["id"]: v for v in json.load(open(sys.argv[2]))} if len(sys.argv) > 2 else {}
scenes, kind_of = [], {}
order = [u["id"] for u in units]
for i, (fu, kind, arg, ex) in enumerate(PLAN):
    sc = {"id": f"{i + 1:03d}", "from": fu}
    if kind == "v":
        sc.update({"type": "video", "src": f"../work/stock/full/{arg}.mp4", "in": ex.get("in", 0.0)})
        for k in ("speed", "grade", "offset", "crop", "blur"):
            if k in ex: sc[k] = ex[k]
        if arg in idx: sc["note"] = f"Mixkit {arg} {idx[arg]['title']}"
    elif kind == "icon":
        sc.update({"type": "icon", "icon": arg})
    elif kind == "photo":
        sc.update({"type": "photo", "image": f"images/{AI_FILES[arg]}", "note": f"AI image {arg}"})
        for k in ("grade", "blur", "z0", "z1", "cx0", "cx1", "cy0", "cy1", "title", "title_sub", "title_size",
                  "title_color", "title_delay", "center_subs"):
            if k in ex: sc[k] = ex[k]
    else:
        sc.update({"type": "card"})
        if "label" in ex: sc["label"] = ex["label"]
    scenes.append(sc)
# which scene kind covers each unit (a scene runs until the next scene's first unit)
starts = [(order.index(s["from"]), s) for s in scenes]
for k, (pos, s) in enumerate(starts):
    end = starts[k + 1][0] if k + 1 < len(starts) else len(order)
    if k + 1 < len(starts) and starts[k + 1][0] == pos:   # two scenes inside one unit: keep the first one's kind
        continue
    for j in range(pos, max(end, pos + 1)):
        kind_of.setdefault(order[j], "photo_center" if s.get("center_subs") else s["type"])
subs = []
for u in units:
    t = u["text"]
    for a, b in DIGITS:
        t = t.replace(a, b)
    if u["id"] in EMPH and EMPH[u["id"]] in t:
        t = t.replace(EMPH[u["id"]], f"[{EMPH[u['id']]}]", 1)
    t = DISPLAY.get(u["id"], t)
    s = {"unit": u["id"], "text": t}
    k = kind_of.get(u["id"])
    if k == "photo_center":                  # quote over a dimmed photo: centred like a card, no box, soft shadow
        s.update({"pos": "center", "box": False, "shadow": True})
    elif k == "card":
        s["pos"] = "center"
        if u["id"] in ITALIC: s["italic"] = True
    elif k == "icon":
        s["box"] = False
    subs.append(s)
# v2: the video ends about 3 s after the last word (owner); the last subtitle leaves 1 s after speech ends
spec = {"fade_in": 0.3, "fade_out": 1.5, "last_sub_hold": 1.0, "sub_lead": 0.0, "scenes": scenes, "subs": subs}
json.dump(spec, open(f"{F}/spec.json", "w"), ensure_ascii=False, indent=1)
print(len(scenes), "scenes |", sum(1 for s in scenes if s["type"] == "video"), "video,",
      sum(1 for s in scenes if s["type"] == "photo"), "AI photo,",
      sum(1 for s in scenes if s["type"] == "icon"), "icon,", sum(1 for s in scenes if s["type"] == "card"), "card")
print("clips:", ",".join(sorted({x[2] for x in PLAN if x[1] == "v"}, key=int)))
print("emphasis not found:", [k for k, w in EMPH.items() if f"[{w}]" not in next(s["text"] for s in subs if s["unit"] == k)])
