# Final soundtrack = owner's narration + background music, then the mix is normalized to -14 LUFS / -1.5 dBTP.
# Inputs: narration from prep_audio.py (-14 LUFS, mono), music from make_bgm.py --lufs -32 (same length or longer).
# usage: mix_audio.py narration.wav bgm.wav out.wav
import json, re, subprocess, sys

nar, bgm, out = sys.argv[1:4]
tmp = out.replace(".wav", "_raw.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", nar, "-i", bgm, "-filter_complex",
                "[0:a]aformat=channel_layouts=stereo,aresample=48000[n];[1:a]aresample=48000[b];"
                "[n][b]amix=inputs=2:duration=first:normalize=0[m]", "-map", "[m]", "-ar", "48000", "-ac", "2", tmp],
               check=True)
base = "loudnorm=I=-14:TP=-1.5:LRA=11"
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", tmp, "-af", base + ":print_format=json", "-f", "null", "-"],
                   capture_output=True, text=True)
m = json.loads(re.search(r"\{[^{}]*\"input_i\"[^{}]*\}", r.stderr).group(0))
af = (f"{base}:measured_I={m['input_i']}:measured_TP={m['input_tp']}:measured_LRA={m['input_lra']}"
      f":measured_thresh={m['input_thresh']}:offset={m['target_offset']}:linear=true")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af, "-ar", "48000", "-ac", "2", out], check=True)
r = subprocess.run(["ffmpeg", "-hide_banner", "-i", out, "-af", "ebur128=peak=true", "-f", "null", "-"],
                   capture_output=True, text=True)
i_val = re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)
print(out, "integrated", i_val[-1] if i_val else "?", "LUFS")
