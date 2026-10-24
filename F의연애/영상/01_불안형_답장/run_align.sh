#!/usr/bin/env bash
# Subtitle line times for 01편 (2026-10-24). Run from anywhere; VIDEO_ROOT holds venv/, models/, work/.
# work/narration.wav from edit_narration.py; work/rec/part{1,2,3}_words.json from the recogniser (one run per recording).
set -euo pipefail
E="$(cd "$(dirname "$0")" && pwd)"; SC="$E/../scripts"; VR="${VIDEO_ROOT:?set VIDEO_ROOT}"; W="$VR/work"; PY="$VR/venv/bin/python"
"$PY" -I "$SC/make_lines.py" "$E"
"$PY" -I -c "
import json; L=json.load(open('$E/lines.json'))
json.dump([{'id':o['id'],'text':o['spoken']} for o in L], open('$W/units_disp.json','w'), ensure_ascii=False, indent=1)"
# recognised words, shifted to the joined narration (edit_log.json: part2 starts at 429.078 s and is cut at 247.22 s,
# part3 starts at 676.298 s)
"$PY" -I "$SC/align_words.py" "$W/units_disp.json" "$W/align.json" "$W/rec/part1_words.json:0" \
  "$W/rec/part2_words.json:429.078:0:247.22" "$W/rec/part3_words.json:676.298"
"$PY" -I "$SC/onsets.py" "$W/narration.wav" "$W/align.json" "$W/onsets.json"
"$PY" -I -c "
import json; say={o['id']:o['say'] for o in json.load(open('$E/lines.json'))}
U=json.load(open('$W/onsets.json'))
for u in U: u['shown']=u['text']; u['text']=say[u['id']]
json.dump(U, open('$W/onsets_say.json','w'), ensure_ascii=False, indent=1)"
(cd "$VR" && "$PY" -I "$SC/ctc_align.py" "$W/narration.wav" "$W/onsets_say.json" models/w2v_ko "$W/align_ctc.json")
"$PY" -I "$SC/apply_overrides.py" "$W/align_ctc.json" "$E/timing_overrides.json" "$E/lines_align.json"
