# Lists for credits.md (F의 연애 01, 2026-10-24): stock clips with the scenes that use them, AI photos, music, sound effects.
# Reads the render timeline and the licence checks saved under work/stock (each Mixkit item page, copyrightNotice).
# v2 (2026-10-24): --v2 reads work/v2/timeline.json, bgm_segments_v2.json and sfx_log_v2.json, adds the licence checks
# of the v2 stock search (work/stock/items3*) and lists the owner's photos. A clip counts as Free only if every saved
# check of its page says Free.
# v3 (2026-10-25): --v3 reads work/v3/timeline.json, bgm_segments_v3.json and sfx_log_v3.json and also lists the
# owner's v3 photos (work/owner_v3/NN.png) with the scenes that show them, split-screen panels included.
# v4 (2026-10-25): --v4 reads work/v4/timeline.json, bgm_segments_v4.json and sfx_log_v4.json; the owner's photos are
# v3's 29 (the photos the owner attached to the v4 list were files they had already sent).
# v5 (2026-10-25): --v5 reads work/v5/timeline.json and lines_v5.json; the sound is v4's (bgm_segments_v4.json,
# sfx_log_v4.json). It also lists the owner's second set of AI photos (work/owner_v5/NN.png, make_photos_v5.py).
# v6 (2026-10-25): --v6 reads work/v6/timeline.json, lines_v6.json, bgm_segments_v6.json and sfx_log_v6.json (the
# owner's new recordings; the pictures are v5's).
# usage: make_credits.py <episode folder> <VIDEO_ROOT> [--v2 | --v3 | --v4 | --v5 | --v6] > lists.md
import json, os, sys

F, VR = sys.argv[1], sys.argv[2]
V6 = "--v6" in sys.argv
V5 = "--v5" in sys.argv or V6
V4 = "--v4" in sys.argv or V5
V3 = "--v3" in sys.argv or V4
V2 = "--v2" in sys.argv or V3
VER = "v6" if V6 else ("v5" if V5 else ("v4" if V4 else ("v3" if V3 else "v2")))
SND = "v6" if V6 else ("v4" if V5 else VER)    # v5 kept the v4 sound; v6 has its own
W = f"{VR}/work"
tl = json.load(open(f"{W}/{VER}/timeline.json" if V2 else f"{W}/timeline.json"))
lic, notices = {}, {}
for p in ("stock/license_check_batch1.json", "stock/items/license_check.json", "stock/items2/license_check.json") + \
        (("stock/items3/license_check.json", "stock/items3b/license_check.json", "stock/items3c/license_check.json",
          "stock/items3_s1/license_check.json", "stock/items3_final/license_check.json") if V2 else ()):
    if os.path.exists(f"{W}/{p}"):
        for x in json.load(open(f"{W}/{p}")):
            lic.setdefault(x["id"], x)
            notices.setdefault(x["id"], set()).add(x.get("copyrightNotice"))


def mmss(t):
    return f"{int(t // 60)}:{int(t % 60):02d}"


uses, order = {}, []
for sc in tl["scenes"]:
    if sc["type"] != "video":
        continue
    cid = os.path.basename(sc["src"])[:-4]
    base = cid.rstrip("p")
    if base not in uses:
        uses[base] = []; order.append(base)
    how = f"{sc.get('in', 0):g}초부터"
    if sc.get("speed", 1.0) != 1.0:
        how += f", {sc['speed']:g}배속"
    if sc.get("crop"):
        how += ", 가장자리 잘라 냄"
    if sc.get("blur_box"):
        how += ", 휴대폰 화면 글자 흐림"
    if cid.endswith("p"):
        how += ", 휴대폰 뒷면 로고를 지운 판(logo_patch.py)"
    uses[base].append(f"장면 {sc['id']} {mmss(sc['start'])} ({how})")
print(f"## 스톡 영상 ({len(order)}개, Mixkit)\n")
print("모두 영상 페이지의 copyrightNotice가 \"Free\"(Mixkit Stock Video Free License)인 것을 확인했습니다(2026-10-24, 받아 둔 "
      "페이지 기준). 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다. 시각은 영상 안에서 장면이 시작하는 때입니다.\n")
bad = []
for k, cid in enumerate(order, 1):
    x = lic.get(cid, {})
    if notices.get(cid) != {"Free"}:
        bad.append(cid)
    print(f"{k}. {cid} {x.get('title', '(제목 기록 없음)')} — {x.get('url', '')}")
    print("   - " + "; ".join(uses[cid]))
if bad:
    print("\n확인 필요: 라이선스 기록이 Free가 아님 " + ", ".join(bad))

print("\n## AI 사진\n")
print("RealVisXL V5.0 Lightning(SG161222, openrail++ 라이선스, 상업 이용 가능), scripts/gen_batch.py, 지시문은 ai_images.json. "
      "실존 인물(로라, 연구자)은 그리지 않았고, 사람은 뒷모습만 넣었습니다(B07 뒤쪽의 작은 두 사람은 얼굴을 알아볼 수 없을 만큼 작고 흐림).\n")
ai = {j["id"]: j for j in json.load(open(f"{F}/ai_images.json"))}
ph, own, own5 = {}, {}, {}
line_text = {o["id"]: o["text"].replace("\n", " ").replace("[", "").replace("]", "")
             for o in json.load(open(f"{F}/lines_{VER}.json"))} if V2 else {}
for sc in tl["scenes"]:
    if sc["type"] == "photo" and ("/owner_v3/" in sc["image"] or "/owner_v5/" in sc["image"]):
        (own5 if "/owner_v5/" in sc["image"] else own).setdefault(os.path.basename(sc["image"])[:2], []).append(
            f"장면 {sc['id']} {mmss(sc['start'])} \"{line_text.get(sc['from'], '')}\"부터")
    elif sc["type"] == "photo":
        fn = os.path.basename(sc["image"])
        ph.setdefault(fn.split("_")[0], []).append(f"장면 {sc['id']} {mmss(sc['start'])} ({fn})")
    elif sc["type"] == "split":
        for p in sc["panels"]:
            first = p.get("at", sc["from"])
            own.setdefault(os.path.basename(p["image"])[:2], []).append(
                f"장면 {sc['id']} {mmss(sc['start'])} 화면 {'오른쪽' if p['side'] == 'right' else '왼쪽'}, "
                f"\"{line_text.get(first, '')}\"부터")
k = 0
for aid, j in ai.items():
    if V2 and aid not in ph:
        continue
    k += 1
    print(f"{k}. {aid} — {', '.join(ph.get(aid, ['쓰지 않음']))}: {j['use']}")
    print(f"   - 지시문: {j['prompt']}" + (f" / {j['style']}" if j.get('style') else ""))
    print(f"   - 씨앗 {', '.join(map(str, j['seeds']))}, {j['size']}, {j['steps']}단계, CFG {j['cfg']}")

if V2:
    print("\n## 운영자 사진\n")
    for k, who in enumerate(("bowlby", "ariely"), 1):
        print(f"{k}. {who}_v2.png — {', '.join(ph.get(who, ['쓰지 않음']))}: 운영자가 보낸 사진(make_photos_v2.py로 16:9 화면에 맞춤, 커밋하지 않음)")
if V3:
    print("\n## 운영자 AI 사진 1 (v3 요청과 함께 보내 주신 29장)\n" if V5 else f"\n## 운영자 AI 사진 ({VER})\n")
    print("운영자가 직접 만들어 보낸 사진 29장(번호는 대본의 <대사>(번호)). 오른쪽 아래 별 모양 표시를 지우고"
          "(scripts/owner_wm_remove.py), 위아래 검은 띠를 잘라 냄(make_photos_v3.py). 커밋하지 않음.\n")
    for n in range(1, 31):
        key = f"{n:02d}"
        if n == 26:
            print(f"{n}. (사진 없음: 대본의 두 번째 (23) 자리에 23번을 다시 씀)")
            continue
        print(f"{n}. {key}.png — {', '.join(own.get(key, ['대본에 번호가 없어 쓰지 않음' if not V5 else 'v5에서는 쓰지 않음']))}")
if V5:
    print("\n## 운영자 AI 사진 2 (v5)\n")
    print("운영자가 v5 요청과 함께 새로 만들어 보낸 사진 29장(번호는 v5 대본의 <대사>(번호), 14번은 없음, 27번은 두 곳). "
          "오른쪽 아래 별 모양 표시를 지우고(scripts/owner_wm_remove.py), 4번과 21번의 검은 띠를 잘라 냄"
          "(make_photos_v5.py). 커밋하지 않음.\n")
    for n in range(1, 31):
        key = f"{n:02d}"
        if n == 14:
            print(f"{n}. (대본에 14번이 없고 사진도 없음)")
            continue
        print(f"{n}. {key}.png — {', '.join(own5.get(key, ['쓰지 않음']))}")
print("\n## 배경음악 (Mixkit Stock Music Free License, -36 LUFS, 곡이 바뀔 때 3초 겹침)\n")
for k, s in enumerate(json.load(open(f"{F}/bgm_segments_{SND}.json" if V2 else f"{F}/bgm_segments.json")), 1):
    end = s.get("end", tl["duration"])
    off = f", 곡 {s['offset']:g}초부터" if s.get("offset") else ""
    print(f"{k}. {mmss(s['start'])}~{mmss(end)} {s['name']} (Mixkit {s.get('mixkit', s.get('id'))}{off}, https://mixkit.co/free-stock-music/) — {s['why']}"
          + (f" [{SND} 시각에 맞춘 조정: {s['note']}]" if s.get("note") else ""))

print("\n## 효과음 (Mixkit Sound Effects Free License)\n")
names = {"2354": "Message pop alert", "2357": "Bubble pop up alert notification", "1395": "Typing text on a smartphone",
         "1050": "Slow tick-tock clock timer", "2365": "Electric pop"}
if V2:                                   # v2: no clock ticks, no typing (make_sfx_v2.py)
    names = {i: n for i, n in names.items() if i in ("2354", "2357", "2365")}
for k, (i, n) in enumerate(names.items(), 1):
    print(f"{k}. {i} {n}")
sl = f"sfx_log_{SND}.json" if V2 else "sfx_log.json"
print(f"\n넣은 자리({sl}):")
for k, s in enumerate(sorted(json.load(open(f"{F}/{sl}")), key=lambda s: s["t"]), 1):
    print(f"{k}. {mmss(s['t'])} ({s['t']:.2f}초) {s['sfx']}")
