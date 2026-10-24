# Narration -> 48 kHz mono WAV at about -14 LUFS (guide 10-6) with ONE constant gain. Written as 32-bit float, so peaks
# over full scale are kept, not clipped; mix_audio.py limits peaks once at the very end.
# 2026-10-23: the earlier two-pass loudnorm asked for linear=true, but ffmpeg silently switches loudnorm to its dynamic
# mode when the peak after the gain would pass the -1.5 dBTP target, and that happened for every recording here. The
# dynamic mode rides the gain over a few seconds, so the end of a phrase could come out quieter than the rest (owner:
# "녹음한 파일이 ... 후반에 소리가 줄어들거나 그렇게 만들지마"). A constant gain keeps every part in proportion and
# keeps timing sample-exact.
# usage: prep_audio.py input(wav/m4a/mp3) out.wav [target_lufs=-14]
import re, subprocess, sys

src, out = sys.argv[1], sys.argv[2]
target = float(sys.argv[3]) if len(sys.argv) > 3 else -14.0


def measure(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    i_val = float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)[-1])
    tp = re.findall(r"Peak:\s+(-?[\d.]+|-inf) dBFS", r.stderr)
    return i_val, (float(tp[-1]) if tp and tp[-1] != "-inf" else -99.0)


i_in, tp_in = measure(src)
gain = target - i_in
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-af", f"volume={gain:.3f}dB", "-ar", "48000", "-ac", "1",
                "-c:a", "pcm_f32le", out], check=True)
i_out, tp_out = measure(out)
print(out, "integrated", i_out, "LUFS | constant gain", round(gain, 2), "dB, true peak", tp_out, "dBTP")
