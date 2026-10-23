# Stock text check: OCR every stock scene (and AI photo) of a timeline (2 frames/s, with render.py's crop/scale/blur; no colour grade or subtitles)
# to catch readable text or logos before the full render. Needs tesseract (setup.sh). Prints words found per scene and writes
# outdir/hits.json. It misses blurred text a person can still read and low-contrast text (glass, screens), so look too.
# usage: ocr_scan.py timeline.json outdir
import json, os, re, subprocess, sys
from concurrent.futures import ThreadPoolExecutor
tl, out = json.load(open(sys.argv[1])), sys.argv[2]
os.makedirs(out, exist_ok=True)
jobs = []
photos = []
for sc in tl["scenes"]:
    if sc["type"] == "photo":                 # AI images can carry fake lettering or logo-like marks
        photos.append((sc["id"], sc["image"]))
        continue
    if sc["type"] != "video":
        continue
    sp = sc.get("speed", 1.0); dur = (sc["end"] - sc["start"]) * sp
    c = sc.get("crop")
    pre = f"crop=iw*{c[2]-c[0]:.4f}:ih*{c[3]-c[1]:.4f}:iw*{c[0]:.4f}:ih*{c[1]:.4f}," if c else ""
    post = f",gblur=sigma={sc['blur']}" if sc.get("blur") else ""
    vf = f"{pre}fps=2,scale=1920:1080:force_original_aspect_ratio=increase,crop=1920:1080{post}"
    jobs.append((sc["id"], sc["src"], sc.get("in", 0), dur, vf))
def extract(j):
    sid, src, t0, dur, vf = j
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", str(t0), "-t", f"{dur:.2f}", "-i", src, "-vf", vf, "-q:v", "3",
                    f"{out}/{sid}_%03d.jpg"], check=True)
with ThreadPoolExecutor(4) as ex:
    list(ex.map(extract, jobs))
for sid, img in photos:
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", img, "-vf", "scale=1920:1080:force_original_aspect_ratio=increase,"
                    "crop=1920:1080", "-q:v", "3", f"{out}/{sid}_001.jpg"], check=True)
frames = sorted(f for f in os.listdir(out) if f.endswith(".jpg"))
def ocr(f):
    # one OpenMP thread per tesseract: 4 processes x default threads made each frame take 20-85 s instead of 0.3 s
    r = subprocess.run(["tesseract", f"{out}/{f}", "-", "--psm", "11", "tsv"], capture_output=True, text=True,
                       env=dict(os.environ, OMP_THREAD_LIMIT="1"), timeout=120)
    words = []
    for line in r.stdout.splitlines()[1:]:
        p = line.split("\t")
        if len(p) == 12 and p[11].strip():
            conf, w = float(p[10]), p[11].strip()
            if conf >= 70 and re.fullmatch(r"[A-Za-z][A-Za-z'’.-]{2,}", w) and re.search(r"[aeiouyAEIOUY]", w):
                words.append((w, int(conf)))
    return f, words
with ThreadPoolExecutor(4) as ex:
    res = list(ex.map(ocr, frames))
hits = {}
for f, ws in res:
    if ws:
        hits.setdefault(f.split("_")[0], []).append((f, ws))
json.dump(hits, open(f"{out}/hits.json", "w"), ensure_ascii=False, indent=1)
print(len(frames), "frames,", len(hits), "scenes with words")
for sid, lst in sorted(hits.items()):
    allw = sorted({w for _, ws in lst for w, _ in ws})
    print(sid, len(lst), "frames:", " ".join(allw)[:160])
