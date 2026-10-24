# Make every stock clip long enough for its scene (run after build_timeline.py).
# If in + scene length runs past the clip's end, the in-point moves earlier; if the whole clip is still too short,
# it plays slower (down to 0.6x); anything still short is reported (render.py would freeze its last frame).
# usage: fit_clips.py timeline.json [min_speed=0.6]
import json, subprocess, sys

tl_path = sys.argv[1]
min_speed = float(sys.argv[2]) if len(sys.argv) > 2 else 0.6
tl = json.load(open(tl_path))
dur_cache = {}


def clip_len(p):
    if p not in dur_cache:
        dur_cache[p] = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", p],
                                            capture_output=True, text=True, check=True).stdout)
    return dur_cache[p]


prev = None
for sc in tl["scenes"]:
    if sc["type"] != "video":
        prev = None
        continue
    if sc.get("cont"):
        # F의 연애 01 v2 (2026-10-24): "cont" = the previous scene's shot runs on (e.g. the same clip blurred under centre
        # text, owner: "스톡 영상이 그대로 뒷 배경화면으로 이어지게"). The in-point follows on from the previous scene; if
        # the clip runs out, only this part plays slower (moving the in-point would break the continuity).
        assert prev is not None and prev["src"] == sc["src"], ("cont needs the same clip just before", sc["id"])
        sp = prev.get("speed", 1.0)
        sc["in"] = round(prev.get("in", 0.0) + (sc["start"] - prev["start"]) * sp, 3)
        sc["speed"] = sp
        L, dur = clip_len(sc["src"]), sc["end"] - sc["start"]
        if sc["in"] + dur * sp + 0.1 > L:
            sc["speed"] = round(max(min_speed, (L - 0.15 - sc["in"]) / dur), 3)
        print(f'{sc["id"]} {sc["src"].split("/")[-1]}: continues at {sc["in"]} s, speed {sc["speed"]}')
        prev = sc
        continue
    prev = sc
    L, need = clip_len(sc["src"]), (sc["end"] - sc["start"]) * sc.get("speed", 1.0) + 0.1
    before = (sc.get("in", 0.0), sc.get("speed", 1.0))
    if sc.get("in", 0.0) + need > L:
        sc["in"] = round(max(0.0, L - need - 0.05), 2)
    if need > L:
        sc["in"] = 0.0
        sc["speed"] = round(max(min_speed, (L - 0.15) / (sc["end"] - sc["start"])), 3)
    if (sc.get("in", 0.0), sc.get("speed", 1.0)) != before:
        left = L - sc["in"] - (sc["end"] - sc["start"]) * sc.get("speed", 1.0)
        print(f'{sc["id"]} {sc["src"].split("/")[-1]}: in {before[0]}->{sc["in"]}, speed {before[1]}->{sc.get("speed", 1.0)}'
              + (f"  WARNING freezes {-left:.1f}s" if left < 0 else ""))
json.dump(tl, open(tl_path, "w"), ensure_ascii=False, indent=1)
