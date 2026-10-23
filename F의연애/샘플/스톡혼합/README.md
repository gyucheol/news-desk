# 01편 훅 30초 예시: 스톡 혼합 방식

결과 영상: ../F의연애_스톡혼합샘플_30초.mp4
출처와 라이선스: credits.md

「INFJ입니다.」 영상 제작 핸드오프(HANDOFF_VIDEO.md, 2026-10-22 갱신)의 방식을 「F의 연애」 01편 훅에 적용한 예시입니다. 스톡 영상 + 흰 선 아이콘 화면 + 검은 화면 카드 + 일부 AI 이미지로 만들고, 목소리 없이 배경음악만 넣었습니다.

## 파일
- units.json: 자막 단위 20개(화면 자막과 글자 하나까지 같음)
- timing_estimate.json: 글자 수로 추정한 자막 시각(estimate_timing.py 출력, 녹음 전 예시용)
- spec.json: 장면 14개와 자막 명세. 스톡 경로는 ../work/stock/full/<번호>.mp4 기준이고, 스톡 원본은 커밋하지 않습니다.
- images/R01.png: 장면 010에 쓴 AI 이미지
- render_icons.patch: render.py에 새 아이콘 두 개(chat, siren)를 더한 변경분
- credits.md: 스톡 영상별 라이선스 확인 결과, 뺀 영상과 이유, AI 이미지 기록

## 다시 만드는 순서
1. 도구: gyucheol/video-studio 저장소(옮기기 전이면 news-desk 저장소 ccr-1818b982-ozofkq 브랜치의 video/burnout/)를 준비하고 `git apply render_icons.patch`로 아이콘을 더합니다.
2. 이 폴더를 도구 폴더 아래(예: fy/)에 두고, credits.md의 영상 번호로 Mixkit 1080p 원본을 work/stock/full/에, 음악 614를 work/stock/music/에 받습니다.
3. 아래 명령을 도구 폴더 맨 위에서 실행합니다.
   - `venv/bin/python scripts/estimate_timing.py fy/units.json fy/timing_estimate.json`
   - `venv/bin/python scripts/make_bgm.py work/stock/music/614.mp3 31.06 work/bgm_fy.wav --lufs -22`
   - `venv/bin/python scripts/build_timeline.py fy/spec.json fy/timing_estimate.json work/bgm_fy.wav work/timeline_fy.json`
   - `venv/bin/python scripts/render.py work/timeline_fy.json out.mp4`
4. 녹음이 생기면 핸드오프 7장 순서(prep_audio → align → refine)로 시각을 다시 잡고, 배경음악은 -32 LUFS로 낮춥니다.
