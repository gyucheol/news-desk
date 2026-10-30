# 03편 「퇴근 후 의지력」 v2 영상 기록 (2026-10-30, 만드는 중)

10월 30일 사용자 수정 요청으로 v1을 고치는 기록입니다. 영상, 녹음, 사진, 스톡 원본, 음악 원본은 올리지 않았습니다.

요청과 처리
- 초반 배경음악: 긴장감 있고 약간 미스터리한 곡으로 바꾸기. 사용자가 예시를 보고 고르기로 함.
  Mixkit 무료 음악 후보 4곡(music/opening_candidates.json, 모두 "Mixkit Stock Music Free License")을 v1과 같은 도구와 크기
  (bgm_sequence.py --lufs -36 --constant, mix_audio.py -14 LUFS)로 영상 첫 1분 10초에 넣어 들려 드림(music/make_previews.py).
  0:00~1:05(v1의 ① 구간)에 고른 곡을 넣을 예정.
- "다큐멘터리를 본 뒤에는 ~ 멈췄습니다"(V123~V126): 가운데 자막으로(pos_r2.py). 밑의 흰 배경 실내 자전거 영상(st25, st26)은
  흐림만으로는 흰 바탕에 흰 글씨라 밝기를 낮춤(build_spec_r2.py MIX_GAIN_R2, render.py에 grade "gain" 추가:
  scripts/render_gain.patch).
- "지금 막힌 곳은 ~ 단계입니다"(V183~V188): 아래 자막으로(pos_r2.py). 그 장면(st37)은 흐리지 않음.
- "좋아한다는 마음이 있어도 ~ 때문입니다"(65번 문장): 검은 화면에서 떼어 뒷배경(st94, Mixkit 193 자전거를 들고 계단을
  오르는 사람, 무료 라이선스 stock/items/lic_193.json)을 넣음(seg_plan_r2.py, stock/picks/group_E.json). 앞 질문은 검은 화면 그대로.
- 다시 녹음한 부분(rerec_script_user.txt, "헬스장에 가는 일도"~"활동을 배치한 시간도 바꿔 볼 수 있습니다", 자막 V203~V405):
  대본 글자는 v1 표시 대본과 같음(표시와 문장부호를 빼고 비교). 녹음 파일을 받으면 그 구간만 바꾸고 시각을 다시 맞출 예정.

파일
- pos_r2.py: lines_v3.json(v1) -> lines_r2.json, 자막 위치 바꾸기
- seg_plan_r2.py, build_segments_r2.py: 장면 계획(v1 + st94)
- build_spec_r2.py: 장면 명세(v1 build_spec_v3.py + 인자, 밝기 낮춤)
- music/: 후보 찾기(parse_music.py, lic_music.py), 소리 특성 측정(feat.py), 미리듣기 만들기(make_previews.py)
