# Sound effects for 01편 (2026-10-24, F의연애/CLAUDE.md 영상 제작 4: the channel adds sound effects). Few and literal,
# each on the voice onset of its line: a soft pop when my message bubble appears, a different pop when a reply arrives,
# a slow clock tick under the running-clock screens, a small electric pop on the shock, phone typing under the memo.
# Mixkit Sound Effects Free License. Levels are set low (peaks about -20 dBFS before the final constant gain) so they
# sit under the voice. The AI cannot listen: the owner checks them by ear.
# usage: make_sfx.py <episode folder> <VIDEO_ROOT> total_seconds out.wav
import json, re, subprocess, sys
import numpy as np
F, VR, total, out = sys.argv[1], sys.argv[2], float(sys.argv[3]), sys.argv[4]
SR = 48000
lines = json.load(open(f"{F}/lines.json"))
al = {u["id"]: u["start"] for u in json.load(open(f"{F}/lines_align.json"))}
plain = lambda s: re.sub(r"[\[\]]", "", s).replace("\n", " ")


def t(prefix):
    hits = [o["id"] for o in lines if plain(o["text"]).startswith(prefix)]
    assert len(hits) == 1, (prefix, hits)
    return al[hits[0]]


def load(name, dur=None):
    cmd = ["ffmpeg", "-v", "error", "-i", f"{VR}/work/stock/sfx/{name}.mp3"] + (["-t", str(dur)] if dur else []) + \
          ["-ac", "2", "-ar", str(SR), "-f", "f32le", "-"]
    return np.frombuffer(subprocess.run(cmd, capture_output=True, check=True).stdout, np.float32).reshape(-1, 2).copy()


def at_level(x, peak_db=None, rms_db=None):
    if peak_db is not None:
        return x * (10 ** (peak_db / 20) / (np.abs(x).max() + 1e-9))
    return x * (10 ** (rms_db / 20) / (np.sqrt(np.mean(x ** 2)) + 1e-9))


bed = np.zeros((int(total * SR) + SR, 2), np.float32)
log = []


def put(x, t0, what, fade=0.0):
    if fade:
        n = int(fade * SR); x[-n:] *= np.linspace(1, 0, n)[:, None]
    a = int(t0 * SR); bed[a:a + len(x)] += x[:len(bed) - a]
    log.append({"t": round(t0, 2), "sfx": what, "seconds": round(len(x) / SR, 2)})


sent = at_level(load("2354"), peak_db=-20)              # Message pop alert
recv = at_level(load("2357"), peak_db=-19)              # Bubble pop up alert notification
for p in ("오늘 퇴근하고 뭐할꺼야?", "오늘 하루 어땠어요?", "바쁘세요??", "자요..?"):
    put(sent.copy(), t(p), f"보냄: {p}")
for p in ("뭐 할껀 없어, 같이 저녁 먹을까?", "헉 미안해, 회식 와서 연락을 이제 받네."):
    put(recv.copy(), t(p), f"받음: {p}")
tick_starts = [("하지만 3시간, 4시간이 넘어가면,", "슬슬 애가 타기 시작하죠."), ("그렇게 9시가 되고,", "결국 참지 못한 채,")]
for a, b in tick_starts:                                 # Slow tick-tock clock timer, under the clock screens
    d = t(b) - t(a) + 1.2
    put(at_level(load("1050", d), rms_db=-34), t(a), f"시계 초침: {a}", fade=0.4)
put(at_level(load("2365"), peak_db=-22), t("손등에 따끔한 전기가 흐릅니다.") + 0.15, "전기: 손등에 따끔한 전기가")
memo = [o for o in lines if o["kind"] == "bubble" and o["spoken"].startswith("\"6시 30분")][0]
put(at_level(load("1395", 4.0), rms_db=-33), al[memo["id"]] + 0.25, "메모 입력", fade=0.5)
bed = bed[:int(total * SR)]
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", "-", "-c:a", "pcm_f32le", out],
               input=bed.astype(np.float32).tobytes(), check=True)
json.dump(log, open(f"{F}/sfx_log.json", "w"), ensure_ascii=False, indent=1)
print(out, len(log), "effects")
