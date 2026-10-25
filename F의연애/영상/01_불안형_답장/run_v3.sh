#!/usr/bin/env bash
# 01편 v3 (2026-10-25, the owner's v3 request): v2 with the owner's own AI photos where the script marks them, the brain
# explainer, the split screen, one centre line split in two, and calmer, tenser music. Run from anywhere with
# VIDEO_ROOT set, after run_v2.sh (v3 reuses work/v2/narration.wav and work/v2/words.json: the narration is v2's).
# The owner's 29 photos (webp, sent in the chat) go in work/owner_v3/raw/ (not in the repository).
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; PY="$VR/venv/bin/python"
W="$VR/work"; V2="$W/v2"; V="$W/v3"
mkdir -p "$V" "$VR/out"

# 1. the owner's photos: the white star mark off (owner_wm_remove.py), black bars off, numbered (make_photos_v3.py)
"$PY" -I "$SC/owner_wm_remove.py" "$W/owner_v3/raw" "$V/wm_alpha.npy" "$W/owner_v3/clean" "$V/wm_sheet.png"
"$PY" -I "$E/make_photos_v3.py" "$W/owner_v3/clean" "$W/owner_v3"

# 2. subtitles v3 (subtitles_v3.txt -> lines_v3.json, units_say_v3.json)
"$PY" -I "$SC/make_lines.py" "$E" subtitles_v3.txt lines_v3.json
"$PY" -I -c "
import json; L=json.load(open('$E/lines_v3.json'))
json.dump([{'id':o['id'],'text':o['spoken']} for o in L], open('$V/units_disp.json','w'), ensure_ascii=False, indent=1)"

# 3. line times as in run_v2.sh (same narration and recognised words; only the split line gets new times)
cp "$V2/words.json" "$V/words.json"
"$PY" -I "$SC/align_words.py" "$V/units_disp.json" "$V/align.json" "$V/words.json:0"
"$PY" -I "$SC/onsets.py" "$V2/narration.wav" "$V/align.json" "$V/onsets.json"
"$PY" -I -c "
import json; say={o['id']:o['say'] for o in json.load(open('$E/lines_v3.json'))}
U=json.load(open('$V/onsets.json'))
for u in U: u['shown']=u['text']; u['text']=say[u['id']]
json.dump(U, open('$V/onsets_say.json','w'), ensure_ascii=False, indent=1)"
(cd "$VR" && "$PY" -I "$SC/ctc_align.py" "$V2/narration.wav" "$V/onsets_say.json" models/w2v_ko "$V/align_ctc.json")
"$PY" -I "$SC/onsets_v2.py" "$V2/narration.wav" "$V/align_ctc.json" "$E/lines_v3.json" "$V/onsets_v2.json"
"$PY" -I -c "
import json
U=json.load(open('$V/onsets_v2.json')); L={o['id']:o for o in json.load(open('$E/lines_v3.json'))}
out=[]
for u in U:
    o={k:u[k] for k in ('id','text','start','end','anchor','onset_v2','first_consonant','start_ctc') if k in u}
    o['shown']=L[u['id']]['text']; o['kind']=L[u['id']]['kind']; out.append(o)
assert all(b['start']>a['start'] for a,b in zip(out,out[1:]))
json.dump(out, open('$E/lines_align_v3.json','w'), ensure_ascii=False, indent=1)"

# 4. the scene plan and the v3 music
"$PY" -I "$E/build_spec_v3.py" "$E" "$VR"
"$E/fetch_stock.sh" v3

# 5. sound: v3 music, the v2 effects, mix (-14 LUFS)
"$E/make_audio_v3.sh"

# 6. timeline and render (render.py loads the icon modules next to it: no -I)
"$PY" -I "$SC/build_timeline.py" "$V/spec_abs.json" "$E/lines_align_v3.json" "$V/final_audio.wav" "$V/timeline.json" \
  "$E/lines_align_v3.json" > "$V/timeline.log"
"$PY" -I "$SC/fit_clips.py" "$V/timeline.json"
(cd "$VR" && "$PY" "$SC/render_parallel.py" "$V/timeline.json" "$VR/out/01_불안형_답장_v3.mp4" 3)
