# Background music: cut to the video length, fade in/out, loudness-normalize (two-pass loudnorm), stereo 48 kHz.
# usage: make_bgm.py music.(mp3|wav) duration_s out.wav [--lufs -22] [--in 0] [--fade-in 0.8] [--fade-out 2.0]
#   --lufs -22 : preview without narration (sample30)
#   --lufs -32 : under the owner's narration (narration is -14 LUFS, so music sits about 18 dB lower)
#   --in       : start point inside the music (s)
import json, re, subprocess, sys

a = sys.argv[1:]
src, dur, out = a[0], float(a[1]), a[2]
opt = lambda k, d: float(a[a.index(k) + 1]) if k in a else d
lufs, t_in, fi, fo = opt("--lufs", -22.0), opt("--in", 0.0), opt("--fade-in", 0.8), opt("--fade-out", 2.0)
tmp = out.replace(".wav", "_raw.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t_in), "-i", src, "-t", str(dur),
                "-af", f"afade=t=in:st=0:d={fi},afade=t=out:st={max(dur - fo, 0):.3f}:d={fo}",
                "-ar", "48000", "-ac", "2", tmp], check=True)
base = f"loudnorm=I={lufs}:TP=-2:LRA=11"
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", tmp, "-af", base + ":print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))
af = (f"{base}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
      f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af, "-ar", "48000", "-ac", "2", out], check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "ebur128", "-f", "null", "-"], capture_output=True, text=True)
i_val = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
print(out, f"{dur:.2f} s", "integrated", i_val[-1] if i_val else "?", "LUFS")
