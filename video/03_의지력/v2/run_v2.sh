#!/usr/bin/env bash
# 03편 v2 영상을 만드는 순서 (2026-10-30). 저장소의 video/03_의지력/v2/ 파일과 v1/ 파일을 작업 폴더(W)에 두고 돌립니다.
# 커밋하지 않는 준비물: 옛 녹음 REC(10월 28일 rec.wav), 새 녹음 NEW(10월 30일 다시 녹음한 m4a를 wav로), v1의 사진(photos_final/)과
# Mixkit 영상 원본(stock/full/, 193.mp4 추가), 음악 원본(VIDEO_ROOT/stock/music/, 565.mp3 추가), 모델(models/), 글꼴(fonts/).
# 도구: v1과 같은 F의 연애 영상 도구 + render.py의 grade "gain"(scripts/render_gain.patch를 적용한 사본 = SCRIPTS).
set -euo pipefail
VR="${VIDEO_ROOT:?}"; W="$(cd "$(dirname "$0")" && pwd)"; SC="${SCRIPTS:?}"; PY="$VR/venv/bin/python"
REC="${REC:?old rec.wav}"; NEW="${NEW:?new recording wav}"; NEWW="${NEW_WORDS:?Whisper words of NEW: transcribe.py NEW new_words.json}"
A="$W/../align"; OLDW="$A/words.json"    # 2판 units_disp.json, lines.json, words.json(옛 녹음 받아쓰기), v1 onsets는 ../v1/onsets_v3.json
cd "$W"
# 1. 녹음 잇기: 옛 녹음 0~248.08 s + 무음 0.06 s + 새 녹음 전부 + 무음 0.03 s + 옛 녹음 494.03 s~ (splice_r2.json에 시각)
"$PY" -I splice_r2.py "$REC" "$NEW" audio/rec_r2.wav audio/splice_r2.json
D=$(python3 -c "import json;print(json.load(open('audio/splice_r2.json'))['delta_after'])")
N0=$(python3 -c "import json;print(json.load(open('audio/splice_r2.json'))['new_start'])")
# 2. 자막 시각: 받아쓴 낱말(옛 녹음 앞뒤 + 새 녹음) -> 단위 시작 -> 음절 맞춤(CTC) -> 줄 시작(onsets_v2)과 끝
"$PY" -I "$SC/align_words.py" "$A/units_disp.json" align_r2.json "$OLDW:0:0:248.08" "$NEWW:$N0" "$OLDW:$D:494.03:9999"
"$PY" -I "$SC/onsets.py" audio/rec_r2.wav align_r2.json onsets_units_r2.json
python3 -I -c "
import json; L={o['id']:o for o in json.load(open('$A/lines.json'))}
U=json.load(open('onsets_units_r2.json'))
for u in U: u['shown']=L[u['id']]['text']; u['text']=L[u['id']]['say']
json.dump(U, open('onsets_say_r2.json','w'), ensure_ascii=False, indent=1)"
(cd "$VR" && "$PY" -I "$SC/ctc_align.py" "$W/audio/rec_r2.wav" "$W/onsets_say_r2.json" models/w2v_ko "$W/align_ctc_r2.json")
python3 -I build_lines_r2.py align_ctc_r2.json lines_base_r2.json units_r2.json
python3 -I pos_r2.py lines_base_r2.json lines_r2.json
"$PY" -I "$SC/onsets_v2.py" audio/rec_r2.wav units_r2.json lines_r2.json onsets_r2_raw.json
python3 -I add_line_ends_r2.py align_ctc_r2.json lines_r2.json onsets_r2_raw.json
# 녹음이 그대로인 앞뒤는 v1 시각(뒤는 delta만큼), 새 녹음 구간만 새 시각, V213만 손으로 고침(merge_onsets_r2.py 머리말)
python3 -I merge_onsets_r2.py ../v1/onsets_v3.json onsets_r2_raw.json audio/splice_r2.json onsets_r2.json
python3 -I check_align_r2.py ../v1/onsets_v3.json onsets_r2.json audio/splice_r2.json "$NEWW" lines_r2.json
"$PY" -I find_late_r2.py audio/rec_r2.wav onsets_r2.json units_r2.json lines_r2.json V203 V405
END=$(python3 -c "print(round(560.0 + $D, 2))")          # v1과 같이 마지막 말 뒤 약 2초
# 3. 장면 계획과 명세
python3 -I build_segments_r2.py lines_r2.json onsets_r2.json "$END" segments_r2.json
python3 -I build_spec_r2.py lines_r2.json onsets_r2.json segments_r2.json spec_r2.json
# 4. 소리: 녹음 그대로 -14 LUFS, END까지 무음, 배경음악 8곡(① 도입만 565로), 섞기
"$PY" -I "$SC/prep_audio.py" audio/rec_r2.wav audio/narration.wav
ffmpeg -v error -y -i audio/narration.wav -af "apad=whole_dur=$END,atrim=0:$END" -ar 48000 -ac 1 -c:a pcm_f32le audio/narration_end.wav
python3 -I bgm_r2.py ../v1/audio/bgm_segments.json onsets_r2.json "$END" audio/bgm_segments_r2.json
(cd "$VR" && "$PY" -I "$SC/bgm_sequence.py" "$W/audio/bgm_segments_r2.json" "$END" "$W/audio/bgm.wav" --lufs -36 --constant --fade-out 4)
"$PY" -I "$SC/mix_audio.py" audio/narration_end.wav audio/bgm.wav audio/final_audio.wav
# 5. 타임라인 -> 화면(3 프로세스) -> 점검 -> 소리 붙이기
"$PY" -I "$SC/build_timeline.py" spec_r2.json onsets_r2.json audio/final_audio.wav timeline_r2.json onsets_r2.json > timeline_r2.log
"$PY" -I "$SC/fit_clips.py" timeline_r2.json
(cd "$VR" && VIDEO_ROOT="$VR" "$PY" "$SC/render_parallel.py" "$W/timeline_r2.json" "$W/03_v2_video.mp4" 3 --video-only)
SCRIPTS="$SC" "$PY" -I checkframes.py "$W/timeline_r2.json" "$W/chk"
"$PY" -I "$SC/ocr_scan.py" "$W/timeline_r2.json" "$W/ocr"
ffmpeg -v error -y -i 03_v2_video.mp4 -i audio/final_audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -ar 48000 \
  -ac 2 -movflags +faststart 03_의지력_v2.mp4
