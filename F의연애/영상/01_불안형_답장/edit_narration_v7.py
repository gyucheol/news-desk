# 01편 narration v7 (2026-10-25, the owner's v7 list 4): the v6 narration (work/v6/narration.wav, edit_narration_v6.py)
# with seven lines taken out. The owner: "\"밤 11시 50분 지우는 마지막으로 카톡을 하나 더 보냅니다. \"자요..?\" 그렇게
# 보낸 세 줄의 메시지 옆에 숫자 '1' 세 개가 나란히 떠 있습니다.\" 해당 장면이랑 녹음파일을 아예 지워주라."
# The cut runs from the middle of the pause before '밤 11시 50분' to the middle of the pause before '아마 많은 분들이',
# so what stays between '좀 별로였나?' and '아마 많은 분들이' is the first half of one shortened sentence pause and the
# second half of the other: the voice of '별로였나?' fades out as before, the breath before '아마' stays, and the silence
# in between is as long as the other sentence pauses of v6 (0.20-0.21 s, the v2 rule). Pause = 10 ms frames under the
# speech level - 38 dB, as in edit_narration_v6.py. The two pieces are joined with a 15 ms equal-power crossfade inside
# the silence (both sides about 61 dB under the speech level there). Nothing else is changed; one constant gain brings
# the result back to -14.0 LUFS (it was -14.0 before the cut).
# Writes the new narration and edit_log_v7.json (the cut, also the time map: times before the cut stay, times after it
# move earlier by the cut length).
# usage: edit_narration_v7.py v6_narration.wav lines_v6.json lines_align_v6.json out.wav edit_log_v7.json
import json, re, subprocess, sys
import numpy as np

src, lines_p, align_p, outp, mapp = sys.argv[1:6]
SR, XF = 48000, 0.015
FIRST_CUT, FIRST_KEPT = "밤 11시 50분", "아마 많은 분들이"      # the first line taken out, the first line after them
x = np.frombuffer(subprocess.run(["ffmpeg", "-v", "error", "-i", src, "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                                 capture_output=True, check=True).stdout, np.float32).astype(np.float64)
lines = json.load(open(lines_p)); al = {a["id"]: a for a in json.load(open(align_p))}
ids = [o["id"] for o in lines]
k0 = next(k for k, o in enumerate(lines) if o["spoken"] == FIRST_CUT)
k1 = next(k for k, o in enumerate(lines) if o["spoken"] == FIRST_KEPT)
removed = lines[k0:k1]
assert [o["spoken"] for o in removed] == ["밤 11시 50분", "지우는 마지막으로", "카톡을 하나 더 보냅니다.", "자요..?",
                                          "그렇게 보낸 3줄의 메시지 옆에", "숫자 '1' 3개가", "나란히 떠 있습니다."], removed

hop = SR // 100
nf = len(x) // hop
db = 20 * np.log10(np.sqrt((x[:nf * hop].reshape(nf, hop) ** 2).mean(1)) + 1e-12)
level = np.percentile(db, 95)
quiet = db < level - 38


def pause_before(t):
    """The quiet run (start frame, end frame) that ends at the voice onset t (within 50 ms)."""
    j = int(round(t * 100))
    j = max(range(j - 5, j + 6), key=lambda i: (quiet[i - 1] and not quiet[i], -abs(i - j)))
    assert quiet[j - 1] and not quiet[j], ("no pause before", t)
    i = j - 1
    while quiet[i - 1]:
        i -= 1
    return i, j


a1, b1 = pause_before(al[ids[k0]]["start"])
a2, b2 = pause_before(al[ids[k1]]["start"])
assert b1 - a1 >= 15 and b2 - a2 >= 15, (b1 - a1, b2 - a2)        # both are shortened sentence pauses (about 0.21 s)
c1 = a1 + (b1 - a1 + 1) // 2            # keep the first half of the pause before '밤 …'
c2 = b2 - (b2 - a2) // 2                # and the second half of the pause before '아마 …'
s1, s2 = c1 / 100, c2 / 100
cut = s2 - s1
i1, i2, xf = c1 * hop, c2 * hop, int(XF * SR)
w = np.sin(np.linspace(0, np.pi / 2, xf)) ** 2
A, B = x[:i1 + xf // 2], x[i2 - xf // 2:]
out = np.concatenate([A[:-xf], A[-xf:] * (1 - w) + B[:xf] * w, B[xf:]])
assert len(out) == len(x) - (i2 - i1)
around = 20 * np.log10(np.sqrt((out[i1 - xf:i1 + xf] ** 2).mean()) + 1e-12) - level


def lufs(y):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-",
                        "-af", "ebur128=peak=true", "-f", "null", "-"], input=y.astype(np.float32).tobytes(),
                       capture_output=True)
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr.decode())[-1])


l0 = lufs(out)
g = 10 ** ((-14.0 - l0) / 20)
out *= g
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", "-", "-c:a", "pcm_f32le",
                outp], input=out.astype(np.float32).tobytes(), check=True)
kept = (c1 - a1 + b2 - c2) / 100
info = {"cut_v6_clock": [round(s1, 3), round(s2, 3)], "cut_seconds": round(cut, 3),
        "removed_lines": [o["id"] + " " + o["spoken"] for o in removed],
        "pause_before_first_cut": [a1 / 100, b1 / 100], "pause_before_first_kept": [a2 / 100, b2 / 100],
        "pause_kept_seconds": kept, "join_level_db_under_speech": round(-around, 1),
        "lufs_before_gain": l0, "gain_db": round(20 * np.log10(g), 3), "lufs": lufs(out),
        "old_duration": round(len(x) / SR, 4), "new_duration": round(len(out) / SR, 4),
        "map": "t < cut[0]: t; t >= cut[1]: t - cut_seconds (v6 clock -> v7 clock)"}
json.dump(info, open(mapp, "w"), ensure_ascii=False, indent=1)
print(json.dumps(info, ensure_ascii=False))
