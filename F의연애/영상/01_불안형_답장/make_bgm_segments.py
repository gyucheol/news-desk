# Background music plan for 01편 (2026-10-24): a track per part of the story, changed 0.4 s before the first subtitle of
# the part, 3 s cross-fades (bgm_sequence.py). Tracks were chosen from Mixkit Free music by tags and by measured values
# (steady loudness, few sharp onsets, little energy above 2 kHz so they stay under the voice); the AI cannot listen.
# usage: make_bgm_segments.py <episode folder> <VIDEO_ROOT> total_seconds -> <folder>/bgm_segments.json
# (track paths are relative to VIDEO_ROOT: run bgm_sequence.py from there)
import json, re, sys
F, VR, total = sys.argv[1], sys.argv[2], float(sys.argv[3])
lines = json.load(open(f"{F}/lines.json"))
al = {u["id"]: u["start"] for u in json.load(open(f"{F}/lines_align.json"))}
plain = lambda s: re.sub(r"[\[\]]", "", s).replace("\n", " ")


def t(prefix, after=0):
    for k, o in enumerate(lines):
        if k >= after and plain(o["text"]).startswith(prefix):
            return round(al[o["id"]] - 0.4, 2), k
    raise SystemExit(prefix)


PARTS = [  # (first line of the part, Mixkit id, title / author, why)
    ("금요일 저녁 7시 퇴근길에,", "493", "Beautiful Dream / Diego Nava", "도입: 연인과의 카톡, 기다림 (Jazz, Melancholic, Love)"),
    ("지우는 2주째,", "41", "Love in the Air / Ahjay Stelino", "공감 사례 지우: 설렘에서 불안으로 (Reflective, Piano, Strings, Love)"),
    ("그 이유를 찾기 위해,", "615", "Tapis / Eugenio Mininni", "실험 1 뱀과 바위: 긴장 (Mysterious, Atmospheric)"),
    ("게다가 이렇게", "168", "Staring at the Night Sky / Alejandro Magaña", "실험 2 노키아 문자: 침묵 (Mysterious, Cello, Piano)"),
    ("도대체 왜 우리의 뇌는,", "681", "Classical vibes 1 / Grigoriy Nuzhny", "로라와 애착: 슬픔 (Reflective, Piano, Drama)"),
    ("그런데 참 신기하죠.", "310", "Alignment / Arulo", "개인차: 생각 (Hopeful, Reflective, Piano)"),
    ("하지만, 괜찮습니다.", "713", "Classical 6 / Jonny S.", "희망과 해결책 1 (Hopeful, Reflective, Piano)"),
    ("둘째, 휴대폰을 언제 확인할지,", "682", "Classical vibes 2 / Grigoriy Nuzhny", "해결책 2, 3 (Uplifting, Hopeful, Piano)"),
    ("생각해 보면,", "1081", "We'll Be Okay / Michael Ramir C.", "마무리 (Reflective, Emotional, Piano)"),
]
segs, k = [], 0
for i, (first, mid, name, why) in enumerate(PARTS):
    st, k = t(first, k)
    segs.append({"track": f"work/stock/music/{mid}.mp3", "start": 0.0 if i == 0 else st, "offset": 0,
                 "name": name, "why": why, "mixkit": mid})
for i in range(len(segs)):
    segs[i]["end"] = segs[i + 1]["start"] if i + 1 < len(segs) else total
json.dump(segs, open(f"{F}/bgm_segments.json", "w"), ensure_ascii=False, indent=1)
for s in segs:
    print(f'{s["start"]:7.2f}-{s["end"]:7.2f}  {s["mixkit"]:>5} {s["name"]}')
