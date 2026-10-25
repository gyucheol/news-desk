# 「F의 연애」 영상 제작 폴더

작성 2026-10-24. 스톡 혼합 방식(스톡 영상 + 흰 선 아이콘 화면 + 검은 화면 카드 + 필요할 때 AI 사진, 하단 자막)으로 롱폼을 만드는 도구와 편별 기록입니다. 영상, 녹음, 스톡 원본, AI 사진, 모델은 커밋하지 않습니다(운영자 목소리·용량). 작업 폴더(VIDEO_ROOT)에 venv/, models/, work/를 두고 돌립니다.

- setup.sh: 가상환경, 글꼴, 음성 인식·음절 정렬·그림 모델 설치
- scripts/: 「INFJ입니다.」 번아웃 편 도구(news-desk 저장소 ccr-1818b982-ozofkq 브랜치 video/burnout/scripts/, 그 브랜치의 2026-10-24 최신 커밋 f6ebebf)를 복사하고 「F의 연애」용을 더했습니다.
  - 더한 것(2026-10-24): fy_common.py·icons_chat.py·icons_exp.py·icons_misc.py(이 채널 아이콘 화면: 카톡 화면, 경보등, 실험 그림 등), make_lines.py(subtitles.txt → 자막 줄), align_words.py(녹음별로 미리 받아 적은 낱말로 맞춤), apply_overrides.py(손으로 고친 자막 시각), transcribe.py(녹음 받아 적기), render_parallel.py(긴 영상을 여러 프로세스로 렌더링), logo_patch.py(스톡 속 움직이는 작은 로고를 따라가며 지움), icon_preview.py
  - 고친 것: render.py(아이콘 모듈 불러오기, --range, blur_box: 화면의 한 부분만 흐림, --range·--frames-only일 때 그 구간의 자막만 미리 만들어 메모리 절약), ocr_scan.py(blur_box 반영), mixkit_search.py(검색 간격 3초, 둘째 쪽 검색)
  - tts.py(합성 음성)는 원본 도구에 들어 있던 것이고 쓰지 않습니다(CLAUDE.md 작업 규칙 13번: 운영자 녹음만).
  - render.py는 같은 폴더의 아이콘 모듈을 불러오므로 python -I 없이 실행합니다. 나머지는 -I로 실행합니다.
- 01_불안형_답장/: 01편 본편(2026-10-24, 12분 3.6초). 기록과 다시 만드는 순서는 credits.md
  - v2(2026-10-24, 사용자 수정 목록 반영, 11분 50.6초): credits_v2.md, 한 번에 다시 만드는 run_v2.sh. v2에서 더한 도구: onsets_v2.py(음절 위치 + 실제 소리로 자막 시작), map_words.py(쉼을 줄인 녹음의 시각으로 낱말 옮기기), fit_clips.py의 cont(앞 장면 영상이 이어짐), bgm_sequence.py --constant(곡마다 고정 크기), render_parallel.py AAC 320kbps, 아이콘 화면 글꼴 G마켓 산스(fy_common.py, setup.sh가 받음)
  - v3(2026-10-25, 사용자 v3 요청: 사용자가 만든 AI 사진 29장, 뇌 사진 설명 화면, 화면 반 나누기, 긴장감 있고 차분한 배경음악): credits_v3.md, run_v3.sh. v3에서 더한 도구: owner_wm_remove.py(사용자 사진 오른쪽 아래 별 표시 지우기), icons_photo.py(사진 위에 그리는 그림: 뇌 위 물음표), render.py의 split(화면 반 나누기)·mix(사진이 다른 판으로 서서히 바뀜)·사진 위 그림이 확대를 따라감, render_parallel.py --video-only(소리 없이 화면만 먼저)
  - v4(2026-10-25, 사용자 v4 수정 목록 1~52번: 노란 강조 삭제, 자막 위치, 앞 장면 이어받기, 첨부 사진, '하..' 숨소리 자르기, 11분 50.1초): credits_v4.md, run_v4.sh. v4에서 더한 도구: render.py의 영상 장면 mix(같은 영상이 가운데 자막 동안만 흐려졌다 돌아옴, until)·icon_overlay(검은 바탕 그래픽을 영상 위에 투명하게 겹침), icons_chat.py의 slots(카톡 화면 배치 맞추기)·panels3 titles/labels, icons_exp.py의 people5 caption·drops3 lift/drop/arrow/note, edit_narration_v4.py(녹음의 한 구간 잘라 내기), make_align_v4.py(검증한 자막 시각을 잘라 낸 만큼 옮기기)
  - v5(2026-10-25, 사용자 v5 요청: 사용자가 새로 만든 AI 사진 29장을 대본에 표시한 30곳에, 27번 사진은 흐리게 + 가운데 자막, 11분 50.1초): credits_v5.md, run_v5.sh(run_v4.sh 다음에 돌림). v5에서 더한 것: make_photos_v5.py(새 사진의 번호와 검은 띠), build_spec_v5.py의 kind own5(두 번째 사진 묶음), make_align_v5.py(v4 자막 시각을 그대로 씀), make_credits.py --v5, fetch_stock.sh v5. scripts/의 도구는 바꾸지 않았습니다.
