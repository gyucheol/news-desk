# Final soundtrack = owner's narration + background music, then the mix is brought to -14 LUFS with one constant gain.
# Inputs: narration from prep_audio.py (-14 LUFS, mono), music from make_bgm.py --lufs -32 (same length or longer).
# usage: mix_audio.py narration.wav bgm.wav out.wav
import json, re, subprocess, sys

nar, bgm, out = sys.argv[1:4]
tmp = out.replace(".wav", "_raw.wav")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", nar, "-i", bgm, "-filter_complex",
                "[0:a]aformat=channel_layouts=stereo,aresample=48000[n];[1:a]aresample=48000[b];"
                "[n][b]amix=inputs=2:duration=first:normalize=0[m]", "-map", "[m]", "-ar", "48000", "-ac", "2", tmp],
               check=True)
# one constant gain to -14 LUFS and a delay-compensated look-ahead limiter on peaks above -1.5 dBFS; no loudnorm
# (2026-10-23: loudnorm falls back to its gain-riding dynamic mode whenever the peak after the gain passes its target)
def measure(p):
    r = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", p, "-af", "ebur128=peak=true", "-f", "null", "-"],
                       capture_output=True, text=True)
    return float(re.findall(r"I:\s+(-?[\d.]+) LUFS", r.stderr)[-1])


gain = -14.0 - measure(tmp)
af = f"volume={gain:.3f}dB,alimiter=limit={10 ** (-1.5 / 20):.5f}:attack=5:release=80:level=false:latency=true"
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", tmp, "-af", af, "-ar", "48000", "-ac", "2", "-c:a", "pcm_s16le", out],
               check=True)
print(out, "integrated", measure(out), "LUFS | constant gain", round(gain, 2), "dB")
