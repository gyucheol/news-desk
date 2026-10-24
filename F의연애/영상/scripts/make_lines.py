# F의 연애 subtitles (2026-10-24): subtitles.txt -> lines.json (one subtitle per line, also the timing units).
# Text file: "◎ " = centre subtitle, "◇ " = centre subtitle in italics (inner thoughts, other people's words),
# "◆ " = words shown only inside a picture (chat bubble, memo), no subtitle box;
# " / " = row break on screen, [ ] = yellow word, ( ) = spoken but not shown (at the start or the end of a line),
# { } = what the recording actually says when it differs from the shown words (v2: the bubble "…봤네" is read "…받네").
# Each line gets "say": the words as spoken in Hangul (digits read out), used by the syllable aligner (ctc_align.py
# only knows Hangul syllables) and by the matching against the recognised words, and "lead": the Hangul syllables of
# hidden words at the start (v2, 2026-10-24: "(하며) 대수롭지 않게 넘깁니다." shows from the voice of 대수롭지; the
# previous subtitle stays while 하며 is spoken).
# usage: make_lines.py <episode folder> [subtitles file = subtitles.txt] [out = lines.json]
#        -> <folder>/<out>, <folder>/units_say.json (or units_say_<suffix>.json for another out name)
import json, re, sys

F = sys.argv[1]
SRC = sys.argv[2] if len(sys.argv) > 2 else "subtitles.txt"
OUT = sys.argv[3] if len(sys.argv) > 3 else "lines.json"
SAY = [  # display -> spoken (longest first); readings checked against the recording (Whisper words, CTC: 삼삼일공)
    ("1~2시간", "한두 시간"), ("6시 30분", "여섯 시 삼십 분"), ("11시 50분", "열한 시 오십 분"), ("9시 반", "아홉 시 반"),
    ("5명 중 1명", "다섯 명 중 한 명"), ("2년 5개월", "이 년 오 개월"), ("2004년", "이천사 년"), ("1952년", "천구백오십이 년"),
    ("2012년", "이천십이 년"), ("3310", "삼삼일공"), ("320번", "삼백이십 번"), ("100%", "백 퍼센트"), ("138명", "백삼십팔 명"),
    ("88명", "팔십팔 명"), ("60cm", "육십 센티미터"), ("90초", "구십 초"), ("30분", "삼십 분"), ("3가지", "세 가지"),
    ("3시간", "세 시간"), ("4시간", "네 시간"), ("5분", "오 분"), ("8분", "팔 분"), ("2주", "이 주"), ("7시", "일곱 시"),
    ("8시", "여덟 시"), ("9시", "아홉 시"), ("3시", "세 시"), ("3줄", "세 줄"), ("3개", "세 개"), ("2개", "두 개"),
    ("3번", "세 번"), ("8일", "팔 일"), ("'1'", "'일'"), ("숫자 1", "숫자 일"),
]


def say(t):
    for a, b in SAY:
        t = t.replace(a, b)
    assert not re.search(r"\d", t), t
    return t


rows = [l.rstrip("\n") for l in open(f"{F}/{SRC}", encoding="utf-8")]
rows = [l for l in rows if l.strip() and not l.startswith("#")]
out = []
for i, l in enumerate(rows):
    kind = {"◎ ": "center", "◇ ": "italic", "◆ ": "bubble"}.get(l[:2], "bottom")
    t = l[2:] if kind != "bottom" else l
    override = re.search(r"\{([^}]*)\}", t)
    t = re.sub(r"\s*\{[^}]*\}\s*", " ", t).strip()
    lead = re.match(r"\(([^)]*)\)\s*", t)
    shown = re.sub(r"\s*\([^)]*\)\s*", " ", t).strip()
    spoken = override.group(1) if override else t.replace(" / ", " ").replace("(", "").replace(")", "")
    plain = spoken.replace("[", "").replace("]", "")
    if kind == "bottom":
        assert " / " not in t and len(shown.replace("[", "").replace("]", "")) <= 25, (i + 1, l)
    o = {"id": f"L{i + 1:03d}", "kind": kind, "text": shown.replace(" / ", "\n"), "spoken": plain, "say": say(plain)}
    if lead:
        o["lead"] = say(lead.group(1))
    out.append(o)
json.dump(out, open(f"{F}/{OUT}", "w"), ensure_ascii=False, indent=1)
us = "units_say.json" if OUT == "lines.json" else f"units_say_{OUT[6:-5] or 'x'}.json"
json.dump([{"id": o["id"], "text": o["say"]} for o in out], open(f"{F}/{us}", "w"), ensure_ascii=False, indent=1)
emph = sum("[" in o["text"] for o in out)
print(len(out), "lines |", sum(o["kind"] == "bottom" for o in out), "bottom |",
      sum(o["kind"] in ("center", "italic") for o in out), "centre |", sum(o["kind"] == "bubble" for o in out),
      "in pictures |", emph, "with a yellow word |", sum("lead" in o for o in out), "with hidden leading words |",
      sum(len(re.sub(r"[^가-힣0-9A-Za-z]", "", o["spoken"])) for o in out), "syllables")
