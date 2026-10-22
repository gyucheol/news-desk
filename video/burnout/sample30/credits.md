# 30초 예시 (스톡 영상 혼합) 기록

작성 2026-10-22. 파일: burnout_30s_stock_example.mp4 (1920×1080, 30fps, 31.6초)

---

## 1. 구성

- 대본: 핸드오프 7-4 검토 반영본의 ① 훅 전체 + ② 첫 문장("출근길에 업무 메일 알림이 하나 뜹니다.")
- 장면 12개(스톡 영상 9, 아이콘 화면 2, 검은 화면 카드 1). 컷당 평균 약 2.6초입니다.
- 템포: 말 속도를 분당 약 527자로 가정했습니다(첫 샘플 447자보다 약 18% 빠름). 자막과 장면 전환 시각은 이 속도로 읽은 임시 음성에서 계산했고, 영상에 그 음성은 넣지 않았습니다.
- 목소리: 비워 두었습니다. 운영자가 녹음하면 그 녹음에 맞춰 다시 맞춥니다.
- 배경음악: 임시. 목소리가 없어서 -22 LUFS로 넣었습니다. 내레이션과 섞을 때는 더 낮춥니다.
- 아이콘 화면(장면 006 전구, 007 배터리): 지침 6-3 방식으로 직접 그렸습니다(검은 배경, 흰 선 아이콘, 강조색 #F2C94C).
- 색 보정: 모든 장면에 공통 보정을 넣고, 밝은 장면(004a 소파, 005, 008a 창가)은 더 어둡게 맞췄습니다(spec.json의 grade).

---

## 2. 스톡 영상 (Mixkit, 2026-10-22 영상 페이지에서 라이선스 확인)

모두 "Mixkit Stock Video Free License"입니다. 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다(라이선스 원문 확인).

1. 31411 Sleeping boy moves in bed — https://mixkit.co/free-stock-video/sleeping-boy-moves-in-bed-31411/ — 0.2초부터
2. 28899 Woman turning off her alarm clock in the morning — https://mixkit.co/free-stock-video/woman-turning-off-her-alarm-clock-in-the-morning-28899/ — 6.4초부터, 1.6배속
3. 4548 Woman lying on a sofa — https://mixkit.co/free-stock-video/woman-lying-on-a-sofa-4548/ — 2.0초부터
4. 51394 Woman with insomnia lying in her bed trying to sleep — https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/ — 8.0초부터
5. 4701 Worried and sad man with his head down — https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/ — 0.4초부터
6. 4511 Sad girl looking out the window — https://mixkit.co/free-stock-video/sad-girl-looking-out-the-window-4511/ — 0초부터
7. 99909 Close up of a hand writing to do list on a yellow paper notebook — https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/ — 0.5초부터
8. 4333 View inside a wagon in motion — https://mixkit.co/free-stock-video/view-inside-a-wagon-in-motion-4333/ — 5.0초부터
9. 144 Hands shown texting on a smartphone — https://mixkit.co/free-stock-video/hands-shown-texting-on-a-smartphone-144/ — 4.0초부터

영상 페이지 주소는 검색 결과에 있던 링크를 그대로 옮겼습니다.

### 2-1. 라이선스 때문에 뺀 영상

처음 고른 10개 중 7개가 "Mixkit Stock Video Restricted License"였습니다. 이 라이선스는 수익화 유튜브 영상에 쓸 수 없어서 모두 뺐습니다.
- 48732 Woman sleeping on her back at night
- 46395 Man reads a book lying on the sofa in the lounge
- 48733 Man staring up at the ceiling struggling to get to sleep
- 48297 Light bulb illuminating in the dark
- 24063 Exhausted worker having a break late at night
- 46768 Close up of a man writing in a notebook
- 14669 Hands texting on a mobile phone at night

교훈: Mixkit은 검색 결과에 라이선스가 표시되지 않습니다. 영상 페이지에서 꼭 확인해야 합니다(scripts/mixkit_license_check.py).

추가로 뺀 것: 99888(손 메모)은 무료 라이선스지만 수첩 표지에 로고처럼 보이는 문양이 있어 지침의 로고 금지에 맞춰 99909로 바꿨습니다.

---

## 3. 배경음악

- Mixkit 614 "Silent Descent" (태그: Film Score, Reflective, Piano, Strings, Cinematic, Melodic)
- 라이선스: Mixkit Stock Music Free License. 유튜브 영상 사용은 허용됩니다. 다만 원문에 "저작권 신고(claim)를 받으면 team@mixkit.co로 알려 달라"는 단서가 있어, Content ID 신고가 없다고 보장되지는 않습니다.
- 곡 페이지에는 라이선스 표시가 따로 없었습니다. Mixkit의 음악 라이선스는 이 한 종류뿐이어서(사이트 코드의 라이선스 목록 기준) 이 곡도 같은 조건이라고 판단했습니다(연역 추론).
- 고른 방법: 저는 소리를 들을 수 없어서 태그와 앞 40초의 분석값으로 골랐습니다. 소리 크기는 -34에서 -28dB로 완만하게 커지고, 음은 초당 1.35개로 성기며, 음색 중심은 642Hz로 어둡고 따뜻한 편입니다.
- 지침 10-6은 유튜브 오디오 보관함 음원을 권장합니다. 본편에서는 운영자가 고른 곡으로 바꾸는 것을 권합니다.

---

## 4. 확인하지 못한 것

- Envato(Mixkit 운영사)의 허용 사용 정책 원문은 이 환경에서 접속이 막혀(403) 읽지 못했습니다. 검색 요약상으로는 민감한 주제를 착취하거나 선정적으로 다루는 사용을 금지하고, 교육·정보 목적 사용은 허용합니다. 인물이 나오는 영상은 이 기준과 지침(얼굴이 드러나지 않는 구도 우선)을 함께 고려해 골랐습니다.
- Pexels, Pixabay, Unsplash는 API 키가 없어 이번에는 쓰지 못했습니다(사진은 이 사이트들에 많습니다).

---

## 5. 다시 만드는 순서 (video/burnout 폴더에서)

1. `sample30/fetch_stock.sh` (스톡 영상 9개와 음악 1곡)
2. 시각 계산용 임시 음성: `venv/bin/python scripts/tts.py sample30/sentences.json work/guide_raw.wav` → `scripts/prep_audio.py work/guide_raw.wav work/guide.wav`
3. `scripts/align.py work/guide.wav sample30/units.json work/align.json` → `scripts/refine.py work/guide.wav work/align.json work/align_refined.json` (결과는 sample30/align_refined.json과 같아야 합니다)
4. 배경음악: 614.mp3를 영상 길이(31.62초)로 자르고 앞 0.8초·끝 2초 페이드, -22 LUFS로 맞춰 work/bgm.wav
5. `scripts/build_timeline.py sample30/spec.json work/align_refined.json work/bgm.wav work/timeline30.json` → `scripts/render.py work/timeline30.json out.mp4`

운영자 녹음이 생기면 2~3번의 임시 음성 대신 녹음 파일을 넣고, 4번 배경음악은 내레이션 아래로 낮춰 섞습니다.
