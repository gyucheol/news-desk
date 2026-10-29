# 03편 「퇴근 후 의지력」 v1 영상 기록 (2026-10-29)

사용자가 보낸 표시 대본(user_script_marked.txt)과 AI 사진 75장, 10월 28일 녹음으로 만든 첫 영상의 기록입니다.
영상, 녹음, 사진, 스톡 원본, 음악 원본은 올리지 않았습니다.

- credits_v1.md: 제작 기록(정한 것과 이유, 사진 메모, 장면 목록, 스톡 라이선스, 배경음악, 점검, 확인할 것)
- run_v1.sh: 처음부터 다시 만드는 순서와 커밋하지 않은 준비물
- user_script_marked.txt: 사용자가 보낸 표시 대본 원문('<문장>번호'는 사진, '/'는 스톡 바꿈)
- parse_marks.py → pieces_marked.json, parse_out.txt: 표시를 2판 자막 조각(../plan/plan_data.py)에 맞춤
- build_lines_v3.py → lines_v3.json, units_v3.json: 자막 450줄(사진 4장에 맞춰 [69]만 다시 나눔)
- onsets_v3.json: 줄마다 목소리 시작과 끝 시각(onsets_v2.py, add_line_ends.py)
- seg_plan.py, build_segments.py → segments.json: 장면 181개(사진, 스톡, 검은 화면)
- wm_remove_v3.py, wm_post.py, wm_choose.py, wm_bh.py, wm_dir.py, wm_patchfill.py: 사진 오른쪽 아래 별 표시 지우기
  (wm_choose_*.txt: 사진마다 고른 방법과 점수)
- make_photos_v3.py: 받은 순서와 번호 맞추기, 상표 흐림 → photos_final/PNN.png(올리지 않음)
- stock/picks/group_A~D.json: 고른 Mixkit 영상(쓸 구간, 메모), stock_overrides.json: 바꾼 영상과 흐림, 잘라내기, 밝기
- stock/items/lic_*.json: 영상 86개의 라이선스 확인 기록, stock/tools/mk.py: Mixkit 검색, 라이선스 확인, 내려받기
- audio/bgm_segments.json: 배경음악 8곡과 구간
- build_spec_v3.py → spec.json: 장면 명세(F의 연애 render.py 형식)
- checkframes.py: 스톡 장면 점검 프레임 시트, checks/ocr_hits.json: 글자 검사(tesseract)에서 글자로 잡힌 프레임
- make_result_v1.py → result.json, make_credits_v1.py → credits_v1.md
- ../align/lines.json, ../align/align_ctc.json: 2판 자막 줄과 녹음 음절 맞춤 결과(build_lines_v3.py, add_line_ends.py가 읽음)
