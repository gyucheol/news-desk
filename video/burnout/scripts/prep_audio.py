# Narration -> 48 kHz mono WAV at about -14 LUFS (guide 10-6), two-pass ffmpeg loudnorm.
# usage: prep_audio.py input(wav/m4a/mp3) out.wav [target_lufs=-14]
import json, re, subprocess, sys

src, out = sys.argv[1], sys.argv[2]
target = sys.argv[3] if len(sys.argv) > 3 else "-14"
base = f"loudnorm=I={target}:TP=-1.5:LRA=11"
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", src, "-af", base + ":print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))
af = (f"{base}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
      f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", src, "-af", af, "-ar", "48000", "-ac", "1", out], check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True)
i_val = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
print(out, "integrated", i_val[-1] if i_val else "?", "LUFS")
