# Scene spec (장면 설계표 as JSON) + aligned unit times -> render timeline.
# Each subtitle shows from (unit onset - LEAD) until the next subtitle starts (VREW-style, no gaps);
# a scene cuts at the start of its first subtitle (+ optional offset). Image/video paths are relative to the spec.
# usage: build_timeline.py spec.json align_refined.json narration.wav out.json
import json, os, subprocess, sys

spec_path, al_path, audio, outp = sys.argv[1:5]
spec = json.load(open(spec_path))
# subtitles (and the scene cuts tied to them) lead the voice by this much; v2 (2026-10-23) uses 0 so nothing changes
# before the next voice starts (owner feedback), with starts on real voice onsets from onsets.py
LEAD = spec.get("sub_lead", 0.10)
al = {u["id"]: u for u in json.load(open(al_path))}
base = os.path.dirname(os.path.abspath(spec_path))
dur = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", audio],
                           capture_output=True, text=True, check=True).stdout)
subs = [dict(s, start=round(max(al[s["unit"]]["start"] - LEAD, 0.0), 3)) for s in spec["subs"]]
for i, s in enumerate(subs):
    s["end"] = subs[i + 1]["start"] if i + 1 < len(subs) else round(dur, 3)
if "last_sub_hold" in spec:     # audio runs on past the narration (end screen): last subtitle leaves this long after speech
    subs[-1]["end"] = round(min(al[subs[-1]["unit"]]["end"] + spec["last_sub_hold"], dur), 3)
start_of = {s["unit"]: s["start"] for s in subs}
scenes = []
for i, sc in enumerate(spec["scenes"]):
    # a scene starts with its first subtitle, or `offset` seconds after it (cuts inside one subtitle)
    sc = dict(sc, start=0.0 if i == 0 else round(start_of[sc["from"]] + sc.get("offset", 0.0), 3))
    for k in ("image", "src"):
        if sc.get(k):
            sc[k] = os.path.join(base, sc[k])
    scenes.append(sc)
for i, sc in enumerate(scenes):
    sc["end"] = scenes[i + 1]["start"] if i + 1 < len(scenes) else round(dur, 3)
tl = {"duration": round(dur, 3), "audio": os.path.abspath(audio), "fade_in": spec.get("fade_in", 0.3),
      "fade_out": spec.get("fade_out", 0.5), "scenes": scenes, "subs": subs}
json.dump(tl, open(outp, "w"), ensure_ascii=False, indent=1)
for sc in scenes:
    print("scene", sc["id"], sc["type"], f'{sc["start"]:.2f}-{sc["end"]:.2f}')
for s in subs:
    print("  sub", s["unit"], f'{s["start"]:.2f}-{s["end"]:.2f}', s.get("pos", "bottom"),
          "italic" if s.get("italic") else "", s["text"])
