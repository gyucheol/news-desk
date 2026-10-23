# v8 subtitle lines (2026-10-23): subtitles_v8.txt -> lines.json. As make_lines_v7.py, plus steps: in a centre line,
# " | " starts a new row that appears only when its words are spoken (owner: "자막을 먼저 띄우고, 뒷 내용은 그 뒤에
# 띄우기"); the whole sentence keeps its final layout from the start, so the rows already shown do not move.
# A step starts at its first shown syllable: "(그러니까) 내가 …" appears when 내가 is spoken.
# Each line records the unit it starts in ("from") and the syllable it starts at ("at", 0 = the unit start, whose time
# is kept from v6); each step records the same for its first shown word and the row it starts at.
# Text file: "◎ " starts a centre line, " / " breaks a row, " | " breaks a row and starts a step, [ ] marks the yellow
# word, ( ) is spoken but not shown (그러니까 in U188, owner, v2).
# usage: make_lines_v8.py <folder with units.json and subtitles_v8.txt>  -> <folder>/lines.json
import json, re, sys

F = sys.argv[1]
units = json.load(open(f"{F}/units.json"))
norm = lambda s: re.findall(r"[가-힣0-9]", s)
stream = [(u["id"], k, c) for u in units for k, c in enumerate(norm(u["text"]))]
rows = [l.rstrip() for l in open(f"{F}/subtitles_v8.txt", encoding="utf-8")]
rows = [l for l in rows if l.strip() and not l.startswith("#")]
spoken_of = lambda t: norm(t.replace("[", "").replace("]", "").replace("(", "").replace(")", ""))
hidden_len = lambda t: len(norm("".join(re.findall(r"^\s*\(([^)]*)\)", t))))   # hidden words at the start of a part
out, pos = [], 0
for i, l in enumerate(rows):
    center = l.startswith("◎ ")
    t = l[2:] if center else l
    lid = f"L{i + 1:03d}"
    steps, row, p = [], 0, pos
    for j, part in enumerate(t.split(" | ")):
        if j:
            q = p + hidden_len(part)
            uid, at, _ = stream[q]
            steps.append({"id": f"{lid}.{j + 1}", "row": row, "from": uid, "at": at})
        row += len(part.split(" / "))
        p += len(spoken_of(part))
    spoken = spoken_of(t)
    got = [c for _, _, c in stream[pos:pos + len(spoken)]]
    assert got == spoken, (i + 1, l, "".join(got))
    assert hidden_len(t) == 0, (lid, "a line starts with hidden words")
    uid, at, _ = stream[pos]
    shown = re.sub(r"\s*\([^)]*\)\s*", " ", t).strip().replace(" | ", "\n").replace(" / ", "\n")
    v = {"id": lid, "from": uid, "at": at, "center": center, "text": shown, "spoken": t.replace(" | ", " ").replace(" / ", " ")}
    if steps:
        assert center, (lid, "steps are for centre lines")
        v["steps"] = steps
    out.append(v)
    pos += len(spoken)
assert pos == len(stream), ("script left over", "".join(c for _, _, c in stream[pos:pos + 40]))
json.dump(out, open(f"{F}/lines.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "lines |", sum(l["center"] for l in out), "centre |", sum(len(l.get("steps", [])) for l in out),
      "steps in", sum(1 for l in out if l.get("steps")), "lines |", sum(l["at"] > 0 for l in out), "start inside a v6 unit")
