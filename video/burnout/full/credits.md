# 번아웃 편 본편 기록

작성 2026-10-22. 결과 파일: burnout_full.mp4 (1920×1080, 30fps, 8분 18초). 운영자 목소리가 들어 있어 영상과 녹음은 저장소에 커밋하지 않았습니다(SendUserFile로 전달).

---

## 1. 구성

1. 대본: 사용자가 준 "[번아웃 온 사람 특징 대본]". 자막에서 오타 3곳을 고쳤습니다(회서에서 → 회사에서, 번이웃을 → 번아웃을, 들려드릴께요 → 들려드릴게요).
2. 목소리: 운영자 녹음 490.2초 → polish_voice.py로 다듬어 486.4초. 긴 쉼 21곳을 줄이고, 큰 숨소리 63곳과 쉼 안의 입소리 42곳을 줄였습니다. 속도는 녹음 그대로(1.0배)입니다.
3. 자막: 311개 단위(units.json). 숫자는 아라비아 숫자로 씁니다(2026-10-22 사용자 지시, 예: 천구백칠십 년대 → 1970년대). 바꾼 표현은 build_spec.py의 DIGITS에 있습니다. 서수(첫 번째)와 '한 번', '한 발', '숫자 하나'는 글자로 둡니다.
4. 장면 137개: 스톡 영상 86, 아이콘 화면 26, 검은 화면 카드 25. 컷 길이 중앙값 3.4초입니다.
5. 아이콘 화면: scripts/icons.py로 직접 그렸습니다(시계, 계기판, 연료, 배터리 둘, 앱, 꺼지는 휴대폰, 연구 문서, 휴가 그래프, 복귀 첫 주, 휴가 길이 막대, 일터의 6가지 조건, 요일별 점수, 10점 메모).
6. 세 가지 신호 카드 위에 "1 / 3", "2 / 3", "3 / 3"을 작은 회색 글씨로 넣었습니다.
7. 색 보정: 프로이덴버거 이야기(1970년대)는 채도를 크게 낮춘 PAST 보정, 나머지는 DARK·BRIGHT 보정입니다(build_spec.py 맨 위).
8. 끝 12초: 말이 끝난 뒤 바다 일출 장면만 이어지는 최종 화면 구간입니다(유튜브 최종 화면 요소를 넣는 자리). 마지막 자막은 말이 끝나고 1초 뒤 사라집니다(spec.json의 last_sub_hold).

---

## 2. 배경음악 (흐름이 바뀌는 곳마다 바꿈)

2026-10-22 사용자 지시: 배경음악은 한 곡일 필요가 없고, 상황이 반전되거나 바뀌면 자연스럽게 바꿔도 좋음. 곡이 바뀌는 곳에서 3초 동안 겹쳐 넘깁니다. 모두 Mixkit Stock Music Free License(음악 목록 페이지 표기, 2026-10-22 확인)입니다. AI는 소리를 들을 수 없어 태그와 분위기 목록으로 골랐습니다(핸드오프 5장 5-2).

1. 0:00–1:07 훅과 일주일 묘사 — 614 Silent Descent (Eugenio Mininni)
2. 1:07–1:31 번아웃이라는 이름, 프로이덴버거 소개 — 168 Staring at the Night Sky (Alejandro Magaña)
3. 1:31–2:24 크리스마스 아침에 무너짐, 녹음기 — 520 Ode to Loneliness (Diego Nava)
4. 2:24–5:05 핵심 메시지, 세계보건기구 정의, 세 가지 신호 — 184 Vastness (Andrew Ev)
5. 5:05–6:03 휴가 연구, 일터의 원인 — 22 Piano Reflections (Ahjay Stelino)
6. 6:03–6:42 26살 직장인 사례 — 601 Skyline (Eugenio Mininni)
7. 6:42–7:35 작은 방법 2가지 — 148 Forest Mist Whispers (Alejandro Magaña)
8. 7:35–끝 마무리 — 684 Classical vibes 4 (Grigoriy Nuzhny)

- 번호는 Mixkit 곡 번호입니다. 파일 주소는 https://assets.mixkit.co/music/<번호>/<번호>.mp3 입니다(fetch_stock.sh).
- 곡이 바뀌는 시각은 그 단락 첫 자막 0.4초 전입니다(bgm_segments.json).
- 소리 크기: 곡마다 고르게 펴고(dynaudnorm) 같은 크기로 맞춘 뒤, 배경음악 전체 -32 LUFS, 내레이션과 섞은 최종 -14 LUFS입니다.
- 곡을 바꾸려면 bgm_segments.json에서 그 구간의 track만 바꾸고 3장의 6~7단계를 다시 실행합니다.

---

## 3. 다시 만드는 순서 (video/burnout 폴더에서)

1. `full/fetch_stock.sh` (스톡 영상 67개와 음악 8곡을 work/stock/에 받음)
2. 녹음 다듬기(녹음 원본은 운영자가 다시 줘야 함):
   `venv/bin/python scripts/polish_voice.py work/rec.m4a work/narration.wav --section 25.42,67.8,158.08,196.02,234.1,272.84,307.62,365.86,405.02,458.36 --report work/polish.json`
   - --section은 단락이 바뀌는 쉼의 녹음 원본 시각입니다.
3. 끝 12초 붙이기: `ffmpeg -i work/narration.wav -af apad=pad_dur=12 -ar 48000 -ac 1 work/narration_end.wav`
4. 자막 시각: 커밋된 full/align_refined.json을 씁니다(같은 다듬기 결과일 때). 새로 맞추려면 align.py → refine.py(7장 4번). 이때 음성 인식이 숫자로 적은 곳은 단위 글자도 숫자로 바꿔 넣어야 맞춤 점수가 정확합니다.
5. 장면 명세: `python3 full/build_spec.py full work/stock/search/index.json` (검색 목록이 없으면 마지막 인자를 빼도 됩니다. 장면 메모만 빠짐)
6. 배경음악: `venv/bin/python scripts/bgm_sequence.py full/bgm_segments.json 498.39 work/bgm.wav --lufs -32`
7. 섞기: `venv/bin/python scripts/mix_audio.py work/narration_end.wav work/bgm.wav work/final_audio.wav`
8. 타임라인: `venv/bin/python scripts/build_timeline.py full/spec.json full/align_refined.json work/final_audio.wav work/timeline.json` 다음 `venv/bin/python scripts/fit_clips.py work/timeline.json` (짧은 스톡의 시작점을 당김: 장면 051, 082, 113, 114)
9. 렌더링: `venv/bin/python scripts/render.py work/timeline.json work/burnout_full.mp4` (8분 18초에 약 40~50분)

---

## 4. 전체 해상도 점검에서 고친 것 (2026-10-22)

스톡 장면 86개의 가운데 화면을 모두 뽑아 보고, 의심되는 곳은 원래 크기로 확대해 확인했습니다(지침: 로고·읽히는 글자·실존 인물로 오해될 얼굴 금지).
1. 장면 044(4766): 가운데의 나이 든 의사가 프로이덴버거 본인으로 보일 수 있어 강하게 흐리게(blur 16) 했습니다. "동료들을 떠올렸어요"에 맞는 기억 속 장면처럼 보입니다.
2. 장면 038(4701): 프로이덴버거 이야기 구간이라 옆얼굴이 보이는 부분 대신 두 손으로 얼굴을 가린 0~2.4초를 씁니다.
3. 장면 073(42666): 회의실 유리벽의 공간 이름과 TV 화면의 채널 로고 → 흐림 5
4. 장면 109(41192): 신문 기사 제목이 읽힘 → 흐림 6
5. 장면 058, 101(914): 모니터 상표 → 흐림 3
6. 장면 065(50753): 시계 밑 책 제목 → 아래쪽을 잘라 냄(crop)
7. 장면 077: 99904(카페 간판 로고, 칠판 글씨) → 4872(동료 둘이 웃으며 이야기)
8. 장면 067: 39789(휴대폰 뒷면 로고) → 31413
9. 장면 101: 50726(책 제목) → 914(사무실, "일터")
10. 장면 121(99910): 수첩 표지의 회사 로고가 나오지 않는 6.5초부터 씁니다.
11. 장면 057: 4779가 장면 033과 같은 화면이라 검은 화면 카드("개인의 질병으로")로 바꿨습니다.
12. 마지막 장면들: 100831(3.9초)이 짧아 0.6배속으로 느려지던 것을 바꿨습니다. 100831은 7:44(0.9배속), 4397은 7:56, 1086은 8:03부터 끝까지입니다.

---

## 5. 아직 임시인 것

1. 사례 구간(6:04~6:43, 26살 직장인 이야기)은 감자 캐릭터 대신 스톡 영상과 카드로 채웠습니다. 감자 캐릭터는 사용자와 함께 만든 뒤 바꿉니다(핸드오프 16장).
2. 배경음악은 Mixkit에서 골랐습니다. 사용자가 바꾸고 싶은 곡이 있으면 2장 방법으로 바꿉니다.

---

## 6. 유튜브 챕터 (설명란용)

chapters.txt에 있습니다. 시각은 각 단락 첫 자막 시각을 초 단위로 내림했습니다.

---

## 7. 스톡 영상 (67개, Mixkit)

모두 영상 페이지의 copyrightNotice가 "Free"(Mixkit Stock Video Free License)인 것을 확인했습니다(2026-10-22, 받아 둔 페이지 기준). 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다. 시각은 영상 안에서 장면이 시작하는 때입니다.

1. 31411 Sleeping boy moves in bed — https://mixkit.co/free-stock-video/sleeping-boy-moves-in-bed-31411/
   - 장면 001 0:00 (0.2초부터); 장면 113 6:17 (5.06초부터)
2. 28899 Woman turning off her alarm clock in the morning — https://mixkit.co/free-stock-video/woman-turning-off-her-alarm-clock-in-the-morning-28899/
   - 장면 002 0:01 (6.4초부터, 1.6배속); 장면 131 7:35 (1.0초부터)
3. 4548 Woman lying on a sofa — https://mixkit.co/free-stock-video/woman-lying-on-a-sofa-4548/
   - 장면 004 0:08 (2.0초부터); 장면 022 0:53 (9.0초부터); 장면 134 7:48 (14.0초부터)
4. 51394 Woman with insomnia lying in her bed trying to sleep — https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/
   - 장면 005 0:10 (8.0초부터)
5. 4701 Worried and sad man with his head down — https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/
   - 장면 006 0:11 (0.4초부터); 장면 038 1:37 (0.0초부터)
6. 4511 Sad girl looking out the window — https://mixkit.co/free-stock-video/sad-girl-looking-out-the-window-4511/
   - 장면 009 0:21 (0.0초부터); 장면 082 4:27 (1.94초부터)
7. 99909 Close up of a hand writing to do list on a yellow paper notebook — https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/
   - 장면 010 0:23 (0.5초부터); 장면 079 4:17 (6.0초부터)
8. 4333 View inside a wagon in motion — https://mixkit.co/free-stock-video/view-inside-a-wagon-in-motion-4333/
   - 장면 011 0:25 (5.0초부터)
9. 144 Hands shown texting on a smartphone — https://mixkit.co/free-stock-video/hands-shown-texting-on-a-smartphone-144/
   - 장면 012 0:26 (4.0초부터)
10. 1623 People getting into the subway train — https://mixkit.co/free-stock-video/people-getting-into-the-subway-train-1623/
   - 장면 013 0:27 (1.0초부터); 장면 106 5:56 (8.0초부터)
11. 4872 Two coworkers talking and laughing — https://mixkit.co/free-stock-video/two-coworkers-talking-and-laughing-4872/
   - 장면 014 0:30 (1.0초부터); 장면 077 4:09 (9.0초부터)
12. 3428 Street with people walking at dusk — https://mixkit.co/free-stock-video/street-with-people-walking-at-dusk-3428/
   - 장면 015 0:34 (1.0초부터)
13. 26091 Man eats watching television on a rainy night — https://mixkit.co/free-stock-video/man-eats-watching-television-on-a-rainy-night-26091/
   - 장면 017 0:39 (1.0초부터)
14. 31413 Young man lying on his bed checking his smartphone — https://mixkit.co/free-stock-video/young-man-lying-on-his-bed-checking-his-smartphone-31413/
   - 장면 018 0:43 (2.0초부터); 장면 067 3:31 (8.0초부터)
15. 42653 Woman finishes working on her computer — https://mixkit.co/free-stock-video/woman-finishes-working-on-her-computer-42653/
   - 장면 019 0:47 (0.5초부터)
16. 100050 Woman smiling at her phone on a cozy couch — https://mixkit.co/free-stock-video/woman-smiling-at-her-phone-on-a-cozy-couch-100050/
   - 장면 020 0:48 (1.0초부터)
17. 50931 A young man slowly wakes up on a clean white bed — https://mixkit.co/free-stock-video/a-young-man-slowly-wakes-up-on-a-clean-white-50931/
   - 장면 021 0:52 (1.0초부터)
18. 42896 Young woman laying on a white soft bed slowly wakes up in the morning — https://mixkit.co/free-stock-video/young-woman-laying-on-a-white-soft-bed-slowly-wakes-42896/
   - 장면 023 0:55 (2.0초부터)
19. 4513 Worried and sad woman hugging a cushion — https://mixkit.co/free-stock-video/worried-and-sad-woman-hugging-a-cushion-4513/
   - 장면 025 0:58 (1.0초부터)
20. 10395 Close-up view of a typewriter while a man works on it — https://mixkit.co/free-stock-video/close-up-view-of-a-typewriter-while-a-man-works-on-10395/
   - 장면 029 1:10 (1.0초부터)
21. 42343 Movement in a city at night in an aerial shot — https://mixkit.co/free-stock-video/movement-in-a-city-at-night-in-an-aerial-shot-42343/
   - 장면 030 1:12 (1.0초부터)
22. 3429 City street with trolleybus at night — https://mixkit.co/free-stock-video/city-street-with-trolleybus-at-night-3429/
   - 장면 031 1:15 (1.0초부터)
23. 28886 Analog wall clock on a black background in a closed socket — https://mixkit.co/free-stock-video/analog-wall-clock-on-a-black-background-in-a-closed-28886/
   - 장면 032 1:20 (1.0초부터)
24. 4779 Doctor walking down a hospital hallway — https://mixkit.co/free-stock-video/doctor-walking-down-a-hospital-hallway-4779/
   - 장면 033 1:22 (1.0초부터)
25. 39841 Young man working in an office overtime — https://mixkit.co/free-stock-video/young-man-working-in-an-office-overtime-39841/
   - 장면 035 1:28 (1.0초부터); 장면 051 2:26 (4.89초부터); 장면 085 4:40 (4.0초부터)
26. 44579 Close view of a Christmas tree — https://mixkit.co/free-stock-video/close-view-of-a-christmas-tree-44579/
   - 장면 036 1:31 (1.0초부터)
27. 3461 Lighting candles in the dark — https://mixkit.co/free-stock-video/lighting-candles-in-the-dark-3461/
   - 장면 037 1:35 (1.0초부터); 장면 117 6:34 (6.0초부터)
28. 31414 Man lying down moving a lot because of not being able to sleep — https://mixkit.co/free-stock-video/man-lying-down-moving-a-lot-because-of-not-being-31414/
   - 장면 039 1:40 (2.0초부터)
29. 425 Moving needle on retro audio tape recorder — https://mixkit.co/free-stock-video/moving-needle-on-retro-audio-tape-recorder-425/
   - 장면 040 1:47 (1.0초부터); 장면 042 1:54 (8.0초부터)
30. 28893 Black analog clock in a very close shot — https://mixkit.co/free-stock-video/black-analog-clock-in-a-very-close-shot-28893/
   - 장면 041 1:51 (1.0초부터)
31. 1967 Smoke effect over black background — https://mixkit.co/free-stock-video/smoke-effect-over-black-background-1967/
   - 장면 043 1:57 (1.0초부터)
32. 4766 Clinic staff at a hospital reception — https://mixkit.co/free-stock-video/clinic-staff-at-a-hospital-reception-4766/
   - 장면 044 2:03 (6.5초부터, 흐림 16)
33. 4607 Bored young office workers in an office — https://mixkit.co/free-stock-video/bored-young-office-workers-in-an-office-4607/
   - 장면 045 2:06 (1.0초부터); 장면 074 4:01 (8.0초부터)
34. 8744 Young man upset and frustrated receiving a message — https://mixkit.co/free-stock-video/young-man-upset-and-frustrated-receiving-a-message-8744/
   - 장면 046 2:11 (1.0초부터)
35. 2707 A fireplace lit at Christmas time — https://mixkit.co/free-stock-video/a-fireplace-lit-at-christmas-time-2707/
   - 장면 047 2:14 (1.0초부터)
36. 21587 Stacked and piled books taken close up — https://mixkit.co/free-stock-video/stacked-and-piled-books-taken-close-up-21587/
   - 장면 048 2:18 (1.0초부터)
37. 50956 Soft and traslucent smoke flows up on a dark background — https://mixkit.co/free-stock-video/soft-and-traslucent-smoke-flows-up-on-a-dark-background-50956/
   - 장면 049 2:19 (1.0초부터); 장면 118 6:39 (8.0초부터)
38. 50133 A young man wearing a hoodie studying at night in the library with a calculator — https://mixkit.co/free-stock-video/a-young-man-wearing-a-hoodie-studying-at-night-in-50133/
   - 장면 052 2:32 (1.0초부터)
39. 1964 Smoke in motion — https://mixkit.co/free-stock-video/smoke-in-motion-1964/
   - 장면 053 2:35 (1.0초부터)
40. 4835 Office workers hands typing on their devices — https://mixkit.co/free-stock-video/office-workers-hands-typing-on-their-devices-4835/
   - 장면 054 2:37 (1.0초부터)
41. 914 Open office space — https://mixkit.co/free-stock-video/open-office-space-914/
   - 장면 058 2:55 (1.0초부터, 흐림 3); 장면 101 5:35 (10.0초부터, 흐림 3)
42. 4915 Hands of a person typing on a cell phone — https://mixkit.co/free-stock-video/hands-of-a-person-typing-on-a-cell-phone-4915/
   - 장면 059 3:01 (1.0초부터)
43. 50753 A young man turns off the alarm clock by the bedside — https://mixkit.co/free-stock-video/a-young-man-turns-off-the-alarm-clock-by-the-50753/
   - 장면 065 3:22 (1.0초부터, 아래 잘라 냄)
44. 50754 A young man slowly wakes up in bed — https://mixkit.co/free-stock-video/a-young-man-slowly-wakes-up-in-bed-50754/
   - 장면 066 3:27 (2.0초부터)
45. 26090 Table in a living room with fast food while a man watches television — https://mixkit.co/free-stock-video/table-in-a-living-room-with-fast-food-while-a-26090/
   - 장면 070 3:43 (1.0초부터); 장면 112 6:15 (8.0초부터)
46. 42666 Presentation during a work team meeting — https://mixkit.co/free-stock-video/presentation-during-a-work-team-meeting-42666/
   - 장면 073 3:57 (1.0초부터, 흐림 5)
47. 4908 Person working while scrolling on social networks — https://mixkit.co/free-stock-video/person-working-while-scrolling-on-social-networks-4908/
   - 장면 075 4:04 (1.0초부터)
48. 4720 Lonely boy on a park bench — https://mixkit.co/free-stock-video/lonely-boy-on-a-park-bench-4720/
   - 장면 076 4:07 (1.0초부터); 장면 114 6:20 (3.22초부터)
49. 31412 Boy puts his cell phone aside so he can go to sleep — https://mixkit.co/free-stock-video/boy-puts-his-cell-phone-aside-so-he-can-go-31412/
   - 장면 080 4:21 (1.0초부터)
50. 4893 Footsteps of a young man walking down the street — https://mixkit.co/free-stock-video/footsteps-of-a-young-man-walking-down-the-street-4893/
   - 장면 081 4:24 (1.0초부터)
51. 313 Colleagues reading a report together — https://mixkit.co/free-stock-video/colleagues-reading-a-report-together-313/
   - 장면 084 4:35 (1.0초부터)
52. 4500 Upset woman sitting on the floor — https://mixkit.co/free-stock-video/upset-woman-sitting-on-the-floor-4500/
   - 장면 087 4:45 (1.0초부터)
53. 99890 Close up a hand writing notes on a notebook with a pen — https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/
   - 장면 089 4:55 (1.0초부터)
54. 42655 A woman writing in her spiral notebook — https://mixkit.co/free-stock-video/a-woman-writing-in-her-spiral-notebook-42655/
   - 장면 090 4:57 (1.0초부터)
55. 1958 Virgin lonely beach with a palapa — https://mixkit.co/free-stock-video/virgin-lonely-beach-with-a-palapa-1958/
   - 장면 093 5:08 (1.0초부터)
56. 1013 Feet walking on the beach — https://mixkit.co/free-stock-video/feet-walking-on-the-beach-1013/
   - 장면 095 5:17 (1.0초부터)
57. 100252 Pouring Tea into a Cup on a Rustic Table Setting — https://mixkit.co/free-stock-video/pouring-tea-into-a-cup-on-a-rustic-table-setting-100252/
   - 장면 104 5:51 (1.0초부터)
58. 41192 POV flipping through a newspaper — https://mixkit.co/free-stock-video/pov-flipping-through-a-newspaper-41192/
   - 장면 109 6:06 (1.0초부터, 흐림 6)
59. 31415 Frustrated boy in his bed for not being able to sleep — https://mixkit.co/free-stock-video/frustrated-boy-in-his-bed-for-not-being-able-to-31415/
   - 장면 110 6:11 (1.0초부터)
60. 26089 Man watching TV and eating fast food — https://mixkit.co/free-stock-video/man-watching-tv-and-eating-fast-food-26089/
   - 장면 111 6:14 (1.0초부터)
61. 99910 Beside a modern laptop the hands write a note on a yellow page notebook with a pen — https://mixkit.co/free-stock-video/beside-a-modern-laptop-the-hands-write-a-note-on-99910/
   - 장면 121 6:54 (6.5초부터)
62. 3977 View of a window with a curtain — https://mixkit.co/free-stock-video/view-of-a-window-with-a-curtain-3977/
   - 장면 125 7:07 (1.0초부터)
63. 50112 Student hand takes a stiky note to paste it on the notebook — https://mixkit.co/free-stock-video/student-hand-takes-a-stiky-note-to-paste-it-on-50112/
   - 장면 129 7:25 (1.0초부터)
64. 52452 Gliding along a quiet asphalt road at dawn, the soft, golden light of the rising sun iluminates the highway. — https://mixkit.co/free-stock-video/gliding-along-a-quiet-asphalt-road-at-dawn-the-soft-52452/
   - 장면 130 7:30 (1.0초부터)
65. 100831 Sky Transitioning from Night to Sunrise — https://mixkit.co/free-stock-video/sky-transitioning-from-night-to-sunrise-100831/
   - 장면 133 7:44 (0.0초부터, 0.9배속)
66. 4397 The silhouette of a woman at sunrise — https://mixkit.co/free-stock-video/the-silhouette-of-a-woman-at-sunrise-4397/
   - 장면 136 7:56 (0.5초부터)
67. 1086 Sunrise on the ocean — https://mixkit.co/free-stock-video/sunrise-on-the-ocean-1086/
   - 장면 137 8:03 (0.5초부터)
