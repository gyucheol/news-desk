# v9 subtitle lines (2026-10-23): subtitles_v9.txt -> lines.json, as make_lines_v7.py. In v9 the centre sentences the
# owner marked are separate centre lines, one per part: each part sits alone at the centre and the next part takes its
# place when its voice starts (owner: "첫 문장이 중앙에 위치한 다음, 녹음본이 그 내용을 읽고, 그 다음 읽을 대본이 그
# 자리에 올라가있게"; v8's build-up below the earlier rows was a misreading). Hidden words stay at the end of a line, so a
# line never starts on a word that is not shown.
# v7: subtitles_v7.txt (one subtitle per line, as the owner split the start of the script) -> lines.json. The owner asked: centre subtitles (black cards, the quote over the photo) never split, one whole
# sentence at a time; all other subtitles split like the owner's example (U014-U065) through the whole script.
# The words stay as recorded (units.json); this only says where each subtitle starts. Each line records the unit it
# starts in ("from") and the syllable it starts at ("at", 0 = the unit start, whose time is kept from v6).
# Text file: "◎ " starts a centre line, " / " breaks a row on screen, [ ] marks the yellow word, ( ) is spoken but not
# shown (그러니까 in U188, owner, v2).
# usage: make_lines_v9.py <folder with units.json and subtitles_v9.txt>  -> <folder>/lines.json
import json, re, sys

F = sys.argv[1]
units = json.load(open(f"{F}/units.json"))
norm = lambda s: re.findall(r"[가-힣0-9]", s)
stream = [(u["id"], k, c) for u in units for k, c in enumerate(norm(u["text"]))]
rows = [l.rstrip() for l in open(f"{F}/subtitles_v9.txt", encoding="utf-8")]
rows = [l for l in rows if l.strip() and not l.startswith("#")]
out, pos = [], 0
for i, l in enumerate(rows):
    center = l.startswith("◎ ")
    t = l[2:] if center else l
    assert " | " not in t and not t.lstrip().startswith("("), (i + 1, l)
    spoken = norm(t.replace("[", "").replace("]", "").replace("(", "").replace(")", ""))
    got = [c for _, _, c in stream[pos:pos + len(spoken)]]
    assert got == spoken, (i + 1, l, "".join(got))
    uid, at, _ = stream[pos]
    shown = re.sub(r"\s*\([^)]*\)\s*", " ", t).strip().replace(" / ", "\n")
    out.append({"id": f"L{i + 1:03d}", "from": uid, "at": at, "center": center, "text": shown,
                "spoken": t.replace(" / ", " ")})
    pos += len(spoken)
assert pos == len(stream), ("script left over", "".join(c for _, _, c in stream[pos:pos + 40]))
json.dump(out, open(f"{F}/lines.json", "w"), ensure_ascii=False, indent=1)
print(len(out), "lines |", sum(l["center"] for l in out), "centre |", sum(l["at"] > 0 for l in out),
      "start inside a v6 unit |", len(units) - len({l["from"] for l in out if l["at"] == 0}), "v6 unit starts not used")
