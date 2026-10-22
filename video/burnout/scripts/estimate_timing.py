# Estimate when each subtitle unit would be spoken, from character counts only.
# For previews before the owner's recording. No voice is generated (owner's rule, 2026-10-22).
# Rule fitted to the 30-second example (mean error 0.13 s, max 0.39 s):
#   585 chars/min while speaking (spaces and punctuation counted), +0.28 s after a comma,
#   +0.30 s after . ? !  -> about 527 chars/min overall.
# usage: estimate_timing.py units.json out.json [--cpm 585] [--silence out.wav]
#   out.json has the same shape as refine.py output, so build_timeline.py can use it.
#   --silence writes a silent WAV of the total length (or make the BGM that long with make_bgm.py).
import json, sys, wave

args = sys.argv[1:]
units_path, out_path = args[0], args[1]
cpm = float(args[args.index("--cpm") + 1]) if "--cpm" in args else 585.0
silence = args[args.index("--silence") + 1] if "--silence" in args else None
LEAD, TAIL, COMMA, STOP = 0.24, 1.0, 0.28, 0.30

units = json.load(open(units_path))
t, res = LEAD, []
for u in units:
    txt = u["text"]
    dur = len(txt) / cpm * 60
    res.append({"id": u["id"], "text": txt, "start": round(t, 3), "end": round(t + dur, 3), "estimated": True})
    t += dur
    core = txt.rstrip().rstrip("'\"’”")
    last = core[-1:] if core else ""
    t += COMMA if last == "," else (STOP if last in ".?!" else 0.0)
total = round(t + TAIL, 3)
json.dump(res, open(out_path, "w"), ensure_ascii=False, indent=1)
if silence:
    w = wave.open(silence, "wb"); w.setnchannels(2); w.setsampwidth(2); w.setframerate(48000)
    w.writeframes(b"\x00\x00\x00\x00" * int(total * 48000)); w.close()
chars = sum(len(u["text"]) for u in units)
print(f"{len(units)} units, {chars} chars, total {total:.2f} s ({chars / (total - LEAD - TAIL) * 60:.0f} chars/min overall)")
for r in res:
    print(f'{r["id"]:>5} {r["start"]:6.2f}  {r["text"]}')
