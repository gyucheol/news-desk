#!/usr/bin/env bash
# 03편 v1 영상을 처음부터 다시 만드는 순서 (2026-10-29). 저장소의 video/03_의지력/v1/ 파일을 작업 폴더(W)에 두고 돌립니다.
# 커밋하지 않는 준비물: 운영자 녹음(rec.wav, 2026-10-28에 받은 것), 사용자 AI 사진 75장(대화 첨부, photos_in/),
# Mixkit 영상 원본(stock/full/, mk.py get으로 받음), 음악 원본(stock/music/), 모델(models/w2v_ko), 글꼴(fonts/).
# 저장소에 있는 입력: ../plan/plan_data.py(2판 자막 조각), ../align/lines.json, ../align/align_ctc.json(2판 음절 맞춤).
# 도구: F의 연애 영상 도구(scripts/: onsets_v2.py, build_timeline.py, fit_clips.py, render.py, render_parallel.py,
#       prep_audio.py, bgm_sequence.py, mix_audio.py). render.py는 같은 폴더의 아이콘 모듈을 불러오므로 -I 없이 실행합니다.
set -euo pipefail
VR="${VIDEO_ROOT:?set VIDEO_ROOT (venv/, fonts/, models/, stock/music/)}"; W="$(cd "$(dirname "$0")" && pwd)"
SC="${SCRIPTS:?set SCRIPTS (F의 연애 scripts folder)}"; PY="$VR/venv/bin/python"; REC="${REC:?set REC (rec.wav)}"
cd "$W"
# 1. 대본 표시 읽기와 자막 줄([69]만 사진 4장에 맞춰 나눔), 목소리 시작 시각
python3 -I parse_marks.py > /dev/null
python3 -I build_lines_v3.py
"$PY" -I "$SC/onsets_v2.py" "$REC" units_v3.json lines_v3.json onsets_v3.json
python3 -I add_line_ends.py
# 2. 장면 계획(사진·스톡·검은 화면)과 시각
python3 -I build_segments.py
# 3. 사용자 사진: 별 표시 지우기(크기별), 테두리 메움, 주변과 더 맞는 방법 고르기, 일부는 다시 채움, 번호 붙이기와 상표 흐림
for g in "1918.5 1034.5 2000" "1255.5 648 1376" "934 482.5 1024"; do set -- $g
  if [ "$3" = 2000 ]; then "$PY" -I wm_remove_v3.py photos_in photos_clean wm_sheet $1 $2 $3
  else "$PY" -I wm_remove_v3.py photos_in photos_clean wm_sheet $1 $2 $3 "in*" wm_sheet_2000_alpha.npy; fi
  "$PY" -I wm_post.py photos_clean $1 $2 $3 wm_sheet_$3_alpha.npy
  "$PY" -I wm_choose.py photos_in photos_clean $1 $2 $3 wm_sheet_$3_alpha.npy
done
"$PY" -I wm_patchfill.py photos_in/in62_*.webp photos_clean/in62_m12_1.png 1255.5 648 1376 wm_sheet_1376_alpha.npy
for n in in14_m02_3 in22_m04_1 in28_m05_2 in34_m06_3 in35_m06_4 in37_m07_1 in39_m07_3; do
  "$PY" -I wm_bh.py photos_in/$n.jpg photos_clean/$n.png 934 482.5 1024 wm_sheet_1024_alpha.npy 0 6; done
"$PY" -I wm_dir.py photos_in/in54_m10_3.webp photos_clean/in54_m10_3.png 1918.5 1034.5 2000 wm_sheet_2000_alpha.npy
"$PY" -I make_photos_v3.py
# 4. 소리: 녹음 그대로(일정한 크기 -14 LUFS), 560초까지 무음, 배경음악 8곡(-36 LUFS, 곡마다 고정 크기), 섞기
mkdir -p audio
"$PY" -I "$SC/prep_audio.py" "$REC" audio/narration.wav
ffmpeg -v error -y -i audio/narration.wav -af "apad=whole_dur=560.0,atrim=0:560.0" -ar 48000 -ac 1 -c:a pcm_f32le audio/narration_end.wav
(cd "$VR" && "$PY" -I "$SC/bgm_sequence.py" "$W/audio/bgm_segments.json" 560.0 "$W/audio/bgm.wav" --lufs -36 --constant --fade-out 4)   # track 경로는 VIDEO_ROOT 기준
"$PY" -I "$SC/mix_audio.py" audio/narration_end.wav audio/bgm.wav audio/final_audio.wav
# 5. 장면 명세 -> 타임라인 -> 화면(3 프로세스) -> 소리 붙이기
python3 -I build_spec_v3.py
"$PY" -I "$SC/build_timeline.py" spec.json onsets_v3.json audio/final_audio.wav timeline.json onsets_v3.json > timeline.log
"$PY" -I "$SC/fit_clips.py" timeline.json
(cd "$VR" && VIDEO_ROOT="$VR" "$PY" "$SC/render_parallel.py" "$W/timeline.json" "$W/03_v1_video.mp4" 3 --video-only)
# 점검: 스톡 장면 프레임 시트(흐림 상자 장면은 3장씩), 글자 검사(tesseract)
SCRIPTS="$SC" "$PY" -I checkframes.py "$W/timeline.json" "$W/chk"
"$PY" -I "$SC/ocr_scan.py" "$W/timeline.json" "$W/ocr"
ffmpeg -v error -y -i 03_v1_video.mp4 -i audio/final_audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -ar 48000 \
  -ac 2 -movflags +faststart 03_의지력_v1.mp4
