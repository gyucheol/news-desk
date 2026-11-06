#!/usr/bin/env bash
# 살걸·팔걸 편 v1 영상을 처음부터 다시 만드는 순서 (2026-11-06). 저장소의 video/주식심리/살걸팔걸/v1/ 파일을 작업 폴더(W)에 두고 돌립니다.
# 커밋하지 않는 준비물: 사용자 녹음 3개(rec_in/1_1.mp3, 2_1.mp3, 3_1.mp3), 사용자 AI 사진 47장(photos_in/P01~P47.png, 받은 순서),
#   Mixkit 영상 원본(stock/full/, tools/mk.py get), 음악 원본(scratchpad/stock/music/), 모델(models/fw-large-v3, models/w2v_ko), 글꼴(fonts/).
# 도구: 04편 도구 폴더(ep4/tools/scripts: transcribe.py, align_words.py, onsets.py, ctc_align.py, onsets_v2.py, prep_audio.py,
#   bgm_sequence.py, mix_audio.py, build_timeline.py, fit_clips.py, render.py, render_parallel.py).
set -euo pipefail
S=/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad
W="$S/salgeol/v1"; SC="$S/ep4/tools/scripts"; PY="$S/venv/bin/python"
cd "$W"
# 1. 녹음: 48 kHz 모노로만 바꿈 -> 받아쓰기 -> 세 파일 잇기(무음으로 쉼만 맞춤)
for n in 1 2 3; do ffmpeg -v error -y -i rec_in/${n}_1.mp3 -ac 1 -ar 48000 -c:a pcm_s16le rec/part$n.wav; done
bash rec/run_tr.sh
"$PY" -I join_narration.py
# 2. 사진: 별 표시 지우기(1024x572, 별 중심 934.5, 482.5, 03편 2000 크기 별 모양을 줄여 씀) -> 번호 붙이기와 흐림
"$PY" -I wm_remove_v3.py wm_in photos_clean wm_sheet 934.5 482.5 1024 "in*" "$S/ep3/v3/wm_sheet_2000_alpha.npy"
"$PY" -I wm_post.py photos_clean 934.5 482.5 1024 wm_sheet_1024_alpha.npy
"$PY" -I wm_choose.py wm_in photos_clean 934.5 482.5 1024 wm_sheet_1024_alpha.npy
"$PY" -I wm_remove_v3.py wm_in2 photos_clean2 wm_sheetB 934.5 482.5 1024 "in*" "$S/ep3/v3/wm_sheet_2000_alpha.npy"
"$PY" -I wm_post.py photos_clean2 934.5 482.5 1024 wm_sheetB_1024_alpha.npy
"$PY" -I wm_choose.py wm_in2 photos_clean2 934.5 482.5 1024 wm_sheetB_1024_alpha.npy
mkdir -p photos_clean_all && cp photos_clean/in*.png photos_clean2/in*.png photos_clean_all/
"$PY" -I make_photos.py
# 3. 자막 줄과 목소리 시작 시각
python3 -I make_lines.py
for n in 1 2 3; do python3 -I ko_words.py rec/part${n}_words_seg.json rec/part${n}_words_ko.json; done
bash run_align.sh
"$PY" -I ctc_recheck.py lines.json onsets_v2.json rec/rec.wav recheck_all.json
python3 -I fix_onsets.py
# 4. 장면 계획과 스톡 안내서
python3 -I build_segments.py onsets_v3.json segments.json
python3 -I make_brief.py
# 5. 소리: 목소리 -14 LUFS, 배경음악 6곡(-36 LUFS, 곡마다 고정 크기, 3초 겹쳐 바꿈, 끝 4초 줄임), 섞기
END=$(python3 -c "import json; print(json.load(open('segments.json'))['end'])")
"$PY" -I "$SC/prep_audio.py" rec/rec.wav audio/narration.wav
ffmpeg -v error -y -i audio/narration.wav -af "apad=whole_dur=$END,atrim=0:$END" -ar 48000 -ac 1 -c:a pcm_f32le audio/narration_end.wav
(cd "$S" && "$PY" -I "$SC/bgm_sequence.py" "$W/audio/bgm_segments.json" "$END" "$W/audio/bgm.wav" --lufs -36 --constant --fade-out 4)
"$PY" -I "$SC/mix_audio.py" audio/narration_end.wav audio/bgm.wav audio/final_audio.wav
# 6. 장면 명세 -> 타임라인 -> 화면(3 프로세스) -> 소리 붙이기 (6~7단계는 render_all.sh로도 한 번에 돌림)
#    스톡: 세 묶음(stock/picks/group_A·B·C.json) + 바꾼 것(stock_overrides.json). 렌더링 전에 점검 시트를 봄:
#    "$PY" -I pick_sheet.py chk/picks/all   (장면마다 쓰는 구간의 처음, 가운데, 끝 프레임)
python3 -I build_spec.py
"$PY" -I "$SC/build_timeline.py" spec.json onsets_v3.json audio/final_audio.wav timeline.json onsets_v3.json > timeline.log
"$PY" -I "$SC/fit_clips.py" timeline.json
(cd "$S" && VIDEO_ROOT="$S" "$PY" "$SC/render_parallel.py" "$W/timeline.json" "$W/salgeol_video.mp4" 3 --video-only)
ffmpeg -v error -y -i salgeol_video.mp4 -i audio/final_audio.wav -map 0:v -map 1:a -c:v copy -c:a aac -b:a 320k -ar 48000 -ac 2 \
  -movflags +faststart 살걸팔걸_v1.mp4
# 7. 점검: 장면마다 가운데 시각의 프레임 시트
"$PY" -I scene_sheet.py 살걸팔걸_v1.mp4 chk/scenes
