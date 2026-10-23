# 01편 훅 30초 예시 (스톡 혼합 방식) 기록

작성 2026-10-22. 결과 영상: ../F의연애_스톡혼합샘플_30초.mp4 (1920×1080, 30fps, 31.1초, 배경음악만)

---

## 1. 구성

- 방식: 「INFJ입니다.」 영상 제작 핸드오프(2026-10-22 갱신)의 '녹음 전 예시 만들기' 절차(8장)를 그대로 따랐습니다.
- 대본: 01편 ① 훅 전체 + ② 첫 문장. 30초에 맞추려고 ②의 "장면 하나를 떠올려 볼게요."는 뺐습니다.
- 자막 20개, 장면 14개(스톡 영상 10, 아이콘 화면 2, 검은 화면 카드 1, AI 이미지 1). 컷당 평균 약 2.2초입니다.
- 자막 시각: 글자 수로 추정했습니다(estimate_timing.py, 말하는 동안 분당 585자, 쉼표 뒤 0.28초, 문장 끝 뒤 0.30초). 실제 녹음이 들어오면 녹음에 맞춰 다시 맞춥니다.
- 목소리: 넣지 않았습니다(합성 음성 금지 규칙).
- 노란 강조: 30분째, 한 시간, 두 시간, 머릿속, 연구, 경보 장치, 작은 방법(자막 하나에 한 단어).
- 새 아이콘 2개(render_icons.patch)
  - chat: 내가 보낸 말풍선 옆에 노란 '1'이 뜨고 그대로 남습니다. "30분째 1이 안 사라져요" 장면입니다. 카카오톡 화면을 그대로 쓰면 로고·상표 문제가 있어 아이콘으로 그렸습니다.
  - siren: 경보등이 천천히 계속 울립니다(초당 1.25번 밝아졌다 어두워짐). "마음속 경보 장치" 장면입니다.
- 색 보정: 모든 장면에 공통 보정을 넣고, 밝은 장면(003 독서, 004 시계, 009 창가, 014 노을)은 더 어둡게 맞췄습니다(spec.json의 grade).

---

## 2. 스톡 영상 (Mixkit, 2026-10-22 영상 페이지에서 라이선스 확인)

모두 "Free"(Mixkit Stock Video Free License)입니다. 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다.

1. 4915 Hands of a person typing on a cell phone — https://mixkit.co/free-stock-video/hands-of-a-person-typing-on-a-cell-phone-4915/ — 장면 001, 2.0초부터
2. 42741 Girl reading a book sitting near a window — https://mixkit.co/free-stock-video/girl-reading-a-book-sitting-near-a-window-42741/ — 장면 003, 3.0초부터
3. 28893 Black analog clock in a very close shot — https://mixkit.co/free-stock-video/black-analog-clock-in-a-very-close-shot-28893/ — 장면 004, 2.0초부터, 2배속
4. 51395 Girl using her cell phone in her bed waiting to sleep — https://mixkit.co/free-stock-video/girl-using-her-cell-phone-in-her-bed-waiting-to-51395/ — 장면 005, 1.5초부터
5. 51394 Woman with insomnia lying in her bed trying to sleep — https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/ — 장면 007, 12.0초부터
6. 42973 Upset man and sad woman — https://mixkit.co/free-stock-video/upset-man-and-sad-woman-42973/ — 장면 008, 2.5초부터
7. 4511 Sad girl looking out the window — https://mixkit.co/free-stock-video/sad-girl-looking-out-the-window-4511/ — 장면 009, 0.5초부터
8. 99909 Close up of a hand writing to do list on a yellow paper notebook — https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/ — 장면 012, 0.5초부터
9. 41375 Tour high above a city at dusk — https://mixkit.co/free-stock-video/tour-high-above-a-city-at-dusk-41375/ — 장면 013, 3.0초부터
10. 4808 Silhouette of a man texting during the sunset — https://mixkit.co/free-stock-video/silhouette-of-a-man-texting-during-the-sunset-4808/ — 장면 014, 3.0초부터

51394, 4511, 99909는 「INFJ입니다.」 30초 예시에도 쓴 영상입니다. 이번에 영상 페이지에서 다시 확인했습니다.

### 2-1. 라이선스 때문에 뺀 영상

아래 6개는 "Mixkit Restricted License"라 수익화 유튜브 영상에 쓸 수 없어 뺐습니다. 이번에도 처음 고른 9개 중 4개가 제한 라이선스였습니다.
- 32056 An upset young woman by the window
- 13299 Lonely girl sitting on floor with headphones backlit by window
- 48574 Thousands of books in a dark library archive
- 21840 Texting in the city at night
- 24632 Inside an old library
- 6754 City street traffic by night

### 2-2. 무료지만 바꾼 영상

- 21591 Lonely library seen carefully and in detail(Free): 밝은 빨간 벽과 알록달록한 책장이라 보정해도 앞뒤 장면의 어두운 톤과 맞지 않았습니다. '연구를 보면' 장면을 AI 이미지로 바꿨습니다(3장).

### 2-3. 접속 제한 메모

연속 요청 약 13번 만에 Mixkit이 보안 확인 화면(Cloudflare, HTTP 429)을 띄웠습니다. 약 10분 뒤 풀렸고, 이후 영상 페이지는 6초 간격으로 열었습니다(핸드오프 기준 1.5초보다 느리게).

---

## 3. AI 이미지

- 장면 010(images/R01.png): "알려 드릴게요. / 연구를 보면, 이건 예민해서 / 그런 게 아니에요."
- 모델: RealVisXL V5.0 Lightning(openrail++), CPU bf16, 5단계, 가이던스 1.5, 1344×768, 씨앗 301
- 지시문: "a stack of closed old hardcover books with blank spines and reading glasses on a dark wooden desk, warm desk lamp glow at night" + gen.py 기본 스타일 문구(71/77토큰)
- 추가 부정 문구: open book pages, handwriting, people, hands, face, bright room. 기본 부정 문구가 길어 77토큰 한도에서 뒷부분이 잘렸을 수 있습니다.
- 후보 3장(씨앗 301~303) 중 1번을 골랐습니다. 2번과 3번은 안경이 두 개씩 그려졌습니다.
- 움직임: 4초 동안 1.0배에서 1.04배로 천천히 확대합니다.
- 검토: 2026-10-22 사용자 지시("스톡으로 표현이 안 되거나 어색하면 AI로 만들어서 넣어 주면 된다")에 따라 먼저 넣었습니다. 마음에 들지 않으면 다시 만들거나 스톡으로 되돌립니다.
- 업로드 때: 사진풍 AI 장면이 있으므로 '변경되거나 합성된 콘텐츠'를 '예'로 체크합니다(핸드오프 5-3).
- AI 영상(움직이는 장면 생성)은 이 환경(CPU만 있음)에서 만들 수 없어 정지 이미지에 천천히 확대를 넣는 방식으로 했습니다.

---

## 4. 배경음악

- Mixkit 614 "Silent Descent"(「INFJ입니다.」 30초 예시와 같은 곡), -22 LUFS(목소리 없는 예시 기준)
- 라이선스: Mixkit Stock Music Free License. 유튜브 영상 사용은 허용되지만, 원문에 "저작권 신고(claim)를 받으면 team@mixkit.co로 알려 달라"는 단서가 있어 Content ID 신고가 없다고 보장되지는 않습니다.
- 본편 곡은 운영자가 유튜브 오디오 보관함에서 고른 곡으로 바꿉니다.
