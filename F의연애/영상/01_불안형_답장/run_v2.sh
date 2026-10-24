#!/usr/bin/env bash
# 01편 v2 (2026-10-24, the owner's v2 list): the whole v2 from the v1 narration to the video. Run from anywhere with
# VIDEO_ROOT set (venv/, models/, work/ as for v1: work/narration.wav from edit_narration.py, work/rec/part*_words.json,
# AI photos in work/img from gen_batch.py ai_images.json; stock, music and sound effects come from fetch_stock.sh v2).
# The owner's two photos go in work/owner/bowlby.png and work/owner/ariely.png (not in the repository).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
W="$VR/work"; V="$W/v2"
mkdir -p "$V" "$VR/out"

# 1. narration v2: fades on the owner's edit cuts, two clicks repaired, shorter pauses, -14 LUFS
"$PY" -I "$E/edit_narration_v2.py" "$W/narration.wav" "$E/lines.json" "$E/lines_align.json" \
  "$V/narration.wav" "$V/timemap.json" "$E/edit_log_v2.json"

# 2. subtitles v2 (subtitles_v2.txt -> lines_v2.json, units_say_v2.json)
"$PY" -I "$SC/make_lines.py" "$E" subtitles_v2.txt lines_v2.json
"$PY" -I -c "
import json; L=json.load(open('$E/lines_v2.json'))
json.dump([{'id':o['id'],'text':o['spoken']} for o in L], open('$V/units_disp.json','w'), ensure_ascii=False, indent=1)"

# 3. line times: the recognised words moved to the v2 clock, then as run_align.sh, then onsets_v2.py
"$PY" -I "$SC/map_words.py" "$V/timemap.json" "$V/words.json" "$W/rec/part1_words.json:0" \
  "$W/rec/part2_words.json:429.078:0:247.22" "$W/rec/part3_words.json:676.298"
"$PY" -I "$SC/align_words.py" "$V/units_disp.json" "$V/align.json" "$V/words.json:0"
"$PY" -I "$SC/onsets.py" "$V/narration.wav" "$V/align.json" "$V/onsets.json"
"$PY" -I -c "
import json; say={o['id']:o['say'] for o in json.load(open('$E/lines_v2.json'))}
U=json.load(open('$V/onsets.json'))
for u in U: u['shown']=u['text']; u['text']=say[u['id']]
json.dump(U, open('$V/onsets_say.json','w'), ensure_ascii=False, indent=1)"
(cd "$VR" && "$PY" -I "$SC/ctc_align.py" "$V/narration.wav" "$V/onsets_say.json" models/w2v_ko "$V/align_ctc.json")
"$PY" -I "$SC/onsets_v2.py" "$V/narration.wav" "$V/align_ctc.json" "$E/lines_v2.json" "$V/onsets_v2.json"
"$PY" -I -c "
import json, re
U=json.load(open('$V/onsets_v2.json')); L={o['id']:o for o in json.load(open('$E/lines_v2.json'))}
out=[]
for u in U:
    o={k:u[k] for k in ('id','text','start','end','anchor','onset_v2','first_consonant','start_ctc') if k in u}
    o['shown']=L[u['id']]['text']; o['kind']=L[u['id']]['kind']; out.append(o)
assert all(b['start']>a['start'] for a,b in zip(out,out[1:]))
json.dump(out, open('$E/lines_align_v2.json','w'), ensure_ascii=False, indent=1)"

# 4. pictures: the owner's photos on 16:9, the scene plan, the v2 clips and music (skips files already there)
"$PY" -I "$E/make_photos_v2.py" "$W/owner/bowlby.png" "$W/owner/ariely.png" "$W/img"
"$PY" -I "$E/build_spec_v2.py" "$E" "$VR"
"$E/fetch_stock.sh" v2

# 5. sound: music, effects, mix (-14 LUFS)
"$E/make_audio_v2.sh"

# 6. timeline and render (render.py loads the icon modules next to it: no -I)
"$PY" -I "$SC/build_timeline.py" "$V/spec_abs.json" "$E/lines_align_v2.json" "$V/final_audio.wav" "$V/timeline.json" \
  "$E/lines_align_v2.json" > "$V/timeline.log"
"$PY" -I "$SC/fit_clips.py" "$V/timeline.json"
(cd "$VR" && "$PY" "$SC/render_parallel.py" "$V/timeline.json" "$VR/out/01_불안형_답장_v2.mp4" 3)
