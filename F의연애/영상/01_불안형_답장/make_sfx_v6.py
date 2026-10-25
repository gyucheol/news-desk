# Sound effects v6 (2026-10-25): v4's six effects at the same lines, on the v6 times (lines_align_v6.json: the owner's
# new recordings). Below are the v4 notes, unchanged in method.
# Sound effects for 01편 v4 (2026-10-25): v3's effects (make_sfx_v3.py, notes below) on the v4 lines and times
# (lines_align_v4.json: after the cut sigh everything is 0.527 s earlier), without the reply pop at '뭐 할껀 없어 같이
# 저녁 먹을까?' (the owner: "\"뭐 할껀 없어 같이 저녁 먹을까?\"에 효과음 빼기"). The other reply pop and the four
# 'sent' pops stay: the owner asked for this one only. Four of the sent messages are now centre text over the photo
# (owner 1, 7, 9, 11) instead of a chat screen; the pop still marks the message being sent.
# --- v3 notes ---
# Sound effects for 01편 v3 (2026-10-25): the same effects at the same lines as v2 (make_sfx_v2.py, below), read from the
# v3 lines (only one centre line was split; the other lines keep their v2 times). The shock pop at '손등에 따끔한 전기가
# 흐릅니다.' now plays over the owner's photo 15 (the snake under the rock) instead of the snake icon.
# --- v2 notes ---
# Sound effects for 01편 v2 (2026-10-24). As v1 (make_sfx.py: a soft pop when my message bubble appears, another
# pop when a reply arrives, a small electric pop on the shock; Mixkit Sound Effects Free License, peaks about -20 dBFS
# under the voice), with the owner's v2 list:
#  - no clock ticks ("시계 초침이 막 넘어갈 때 이상한 효과음이 나오는데, 그거 없애줘": both running-clock screens);
#  - no typing under the memo line: the memo screen it went with is gone (the line is now centre text, owner 52).
# The message pops stay: the "카톡 등장 효과" the owner asked to remove is taken as the picture's entrance (owner 20
# asks for it at "메시지 옆 숫자 '1'은 그대로입니다.", where v1 had no sound but did animate the chat screen).
# Each effect sits on the voice onset of its line (lines_align_v4.json). The AI cannot listen: the owner checks them.
# usage: make_sfx_v6.py <episode folder> <VIDEO_ROOT> total_seconds out.wav log.json
import json, re, subprocess, sys
import numpy as np
F, VR, total, out, logp = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4], sys.argv[5]
SR = 48000
lines = json.load(open(f"{F}/lines_v6.json"))
al = {u["id"]: u["start"] for u in json.load(open(f"{F}/lines_align_v6.json"))}
plain = lambda s: re.sub(r"[\[\]]", "", s).replace("\n", " ")


def t(prefix):
    hits = [o["id"] for o in lines if plain(o["text"]).startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return al[hits[0]]


def load(name, dur=None):
    cmd = ["ffmpeg", "-v", "error", "-i", f"{VR}/work/stock/sfx/{name}.mp3"] + (["-t", str(dur)] if dur else []) + \
          ["-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).copy()


def at_level(x, peak_db):
    return x * (10 ** (peak_db / 20) / (np.abs(x).max() + 1e-9))


bed = np.zeros((int(total * SR) + SR, 2), np.float32)
log = []


def put(x, t0, what):
    a = int(t0 * SR); bed[a:a + len(x)] += x[:len(bed) - a]
    log.append({"t": round(t0, 2), "sfx": what, "seconds": round(len(x) / SR, 2)})


sent = at_level(load("2354"), -20)              # Message pop alert
recv = at_level(load("2357"), -19)              # Bubble pop up alert notification
for p in ("오늘 퇴근하고 뭐할꺼야?", "오늘 하루 어땠어요?", "바쁘세요??", "자요..?"):
    put(sent.copy(), t(p), f"보냄: {p}")
for p in ("헉 미안해..ㅜ회식 와서 연락을 이제 봤네",):          # v4: not at '뭐 할껀 없어'
    put(recv.copy(), t(p), f"받음: {p}")
put(at_level(load("2365"), -22), t("손등에 따끔한 전기가 흐릅니다.") + 0.15, "전기: 손등에 따끔한 전기가")
bed = bed[:int(total * SR)]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_f32le", out],
               input=bed.astype(np.float32).tobytes(), check=True)
json.dump(log, open(logp, "w"), ensure_ascii=False, indent=1)
print(out, len(log), "effects")
