# 01편 「불안형 답장」 본편 기록

작성 2026-10-24. 결과 파일: 01_불안형_답장.mp4 (1920×1080, 30fps, H.264 + AAC 48kHz 스테레오, 12분 3.6초). 운영자 목소리가 들어 있어 영상과 녹음은 저장소에 커밋하지 않았습니다(SendUserFile로 전달). 스톡 원본, AI 사진, 모델도 커밋하지 않았습니다(다시 만드는 법은 3장).

사용자 요청: "이제 첫번째 영상을 만들어보자. INFJ입니다 채널에서 영상 만들 때 피드백했던 내용까지 다 적용시켜서 롱폼 가로 영상으로 만들어줘." 작업 중에 최종 대본과 '바뀜' 녹음을 받았습니다: "기존 대본에 있는 해당 부분을 "음성2_1.1배속_10월24일_2차" 녹음 파일에서 지워주고, 해당 부분에 "바뀜" 녹음 파일을 넣어주면 돼." 대본은 F의연애/대본/01_불안형_답장_v3_최종.md에 그대로 옮겼습니다.

---

## 1. 구성

1. 녹음 (edit_narration.py, edit_log.json). 속도, 쉼, 숨소리는 녹음 그대로 두었습니다(HANDOFF_FEEDBACK.md 2장).
   - 음성1_1.1배속_10월24일_2차 (428.92초) 전체 → 0:00~7:08.9
   - 0.15초 쉼 (문단 사이. 녹음 속 문단 사이 쉼 0.4~0.55초와 비슷해지도록)
   - 음성2_1.1배속_10월24일_2차의 앞 247.22초 → 7:09.1~11:16.3. 그 뒤의 옛 마지막 부분("마지막으로, 영상의 주제와 관련된 짧은 이야기를…", 메아리 이야기)은 지시대로 지웠습니다. 자른 자리는 "…꺼내 보시길 바랍니다." 뒤의 거의 조용한 쉼(-64~-83dB)입니다.
   - 바뀜 (44.49초) 전체 → 11:16.3~12:00.8. 크기만 지운 부분과 같게 한 번 맞췄습니다(+0.3dB, ebur128 기준).
   - 마지막 말("…공유해 주세요.")이 끝난 720.61초 뒤 3초에 영상이 끝납니다.
   - 전체를 한 번의 고정 이득(+0.1dB)으로 -14 LUFS에 맞췄고, 크기를 출렁이게 하는 처리(loudnorm 등)는 쓰지 않았습니다. 마지막 섞기에서 순간 최고점만 -1.5dBFS 리미터로 눌렀습니다(최종 최고점 -1.4dBFS).
2. 자막 460줄 (subtitles.txt → make_lines.py → lines.json; 시각은 run_align.sh → lines_align.json)
   - 아래 자막 419줄(한 줄 25자 이하의 짧은 뜻 덩어리), 가운데 자막 20줄(한 문장을 통째로), 기울인 혼잣말 13줄, 말풍선으로만 보이는 줄 8줄(카톡 화면 안의 글이라 아래 자막은 비움)
   - 자막, 장면 전환, 가운데 글씨는 다음 목소리가 나오기 시작할 때 바뀝니다(앞당김 0초).
   - 숫자는 아라비아 숫자로 썼습니다(예: 세 가지 → 3가지, 60센티미터 → 60cm). 노란 강조는 작업 규칙 9번 기준.
   - 손으로 고친 시각 1곳(timing_overrides.json): "그룹이었습니다."의 시작 549.22초(자동 정렬이 앞의 쉼을 시작으로 잡음).
3. 장면 184개: 스톡 영상 85, 흰 선 아이콘 화면 61(35종류), 검은 화면 카드 29, AI 사진 9 (build_spec.py → spec.json)
   - 아이콘: 카톡 화면(kakao, 말풍선과 읽음 표시 '1'), 경보등(siren), 세 그룹(groups3), 바위와 뱀, 전극, 노키아 휴대폰, 거미 실험 등. scripts/icons_chat.py, icons_exp.py, icons_misc.py
   - 사진은 좌우로 움직이지 않고 아주 천천히 확대만 합니다(초당 0.8%, 최대 1.05배).
4. 소리: 내레이션 -14 LUFS, 배경음악 -36 LUFS(분위기가 바뀌는 곳에서 곡을 3초 겹쳐 바꿈, 9곡), 효과음 10곳(5장). Claude는 소리를 들을 수 없어 배경음악과 효과음을 태그와 분석값으로 골랐습니다. 사용자가 귀로 확인해 주셔야 합니다.

## 2. 대본과 녹음이 다른 곳 (자막은 녹음을 따름)

1. 0:19 말풍선: 대본 "헉 미안해, 회식 와서 연락을 이제 봤네." → 녹음 "…연락을 이제 받네." 자막과 말풍선 모두 "받네"로 썼습니다.
2. 그 밖에 낱말이 다른 곳은 찾지 못했습니다(대본과 자막을 낱말 단위로 맞대 봄, 숫자 표기만 다름).

## 3. 다시 만드는 순서 (F의연애/영상 폴더에서, VIDEO_ROOT에 venv/·models/·work/)

1. setup.sh: 가상환경, 글꼴, 음성 인식·음절 정렬·그림 모델
2. 녹음 세 파일을 48kHz 모노 wav로 바꿔 work/rec/에 둡니다(part1 = 음성1, part2 = 음성2, part3 = 바뀜). 음성 인식은 녹음마다 한 번씩 scripts/transcribe.py(faster-whisper large-v3)로 돌려 part{1,2,3}_words.json을 만듭니다.
3. edit_narration.py work/rec work/narration.wav 01_불안형_답장/edit_log.json
4. run_align.sh → lines.json, lines_align.json
5. fetch_stock.sh(스톡·음악·효과음, 끝에 prep_patches.sh로 39789p를 만듦), gen_batch.py ai_images.json(AI 사진)
6. build_spec.py 01_불안형_답장 $VIDEO_ROOT → spec.json, work/spec_abs.json
7. build_timeline.py work/spec_abs.json 01_불안형_답장/lines_align.json work/final_audio.wav work/timeline.json, 그다음 fit_clips.py work/timeline.json
8. make_audio.sh: make_bgm_segments.py → bgm_segments.json, bgm_sequence.py(--lufs -36 --fade-out 3.0) → work/bgm.wav, make_sfx.py → work/sfx.wav, 둘을 섞은 work/bed.wav, mix_audio.py → work/final_audio.wav (실제로는 7번보다 먼저 돌려 final_audio.wav를 만들어 둠)
9. render_parallel.py work/timeline.json 01_불안형_답장.mp4 3 (render.py는 같은 폴더의 아이콘 모듈을 불러오므로 -I 없이 실행)
10. 점검: ocr_scan.py(스톡·AI 사진의 글자), 장면별 원래 크기 화면, ffprobe, ebur128
11. 기록: make_credits.py → 이 문서 7~10장(스톡·AI 사진·배경음악·효과음 목록)

## 4. 점검에서 고친 것

1. 읽히는 글자·로고(HANDOFF_VIDEO.md 4장 5번: 로고·브랜드 표시, 읽히는 글자는 쓰지 않음)
   - 7:10 시부야 교차로(4401): 1.0초부터 쓰면 일본 아이돌 광고 트럭("Sexy Zone")이 지나감 → 2.65초부터(트럭이 지나간 뒤, 6.75초에 나오는 글자 버스 전)
   - 2:02 침대에서 휴대폰(39789): 휴대폰 뒷면에 애플 로고가 또렷함 → 로고 자리만 둘레 색으로 메운 판(39789p, scripts/logo_patch.py: 첫 화면에서 로고 위치를 눈으로 잡고 템플릿 맞춤으로 따라감, 135프레임 모두 일치도 0.95 이상, 확인판 39789p.mp4.png). 원래 쓰던 7초 뒤 구간은 크게 웃는 얼굴이라 불안하게 다시 읽는 장면과 맞지 않아 0초부터(무표정)로 바꿈
   - 0:51 "5분마다 습관처럼"(원래 39789) → 51397(침대에 누워 휴대폰을 드는 장면, 무료). 같은 클립이 70초 뒤에 또 나오지 않도록
   - 9:33 잠든 사람 옆 휴대폰(39780): 잠금 화면 알림 글자("Are you awake ?" 등)가 원래 크기에서 읽힘 → 휴대폰 자리만 흐림(render.py의 새 옵션 blur_box, sigma 8)
   - 대신 고른 후보 중 39773(침대에서 채팅)은 스페인어 대화와 이름이 또렷이 읽혀서, 16140·47972·36425는 제한 라이선스라 쓰지 않았습니다.
2. AI 사진
   - B08(간호사): 지시문은 뒷모습인데 옆얼굴이 또렷이 나와, 기록 영화 속 실제 간호사로 오해될 수 있어 B08b(뒷모습)로 다시 만듦
   - B09(실험실): 오른쪽 모니터에 해골 같은 이상한 그림이 나옴 → B09b(화면에 바위 사진을 요청)는 사람이 빠지고 의자가 일그러짐 → B09c 두 장 중 씨앗 2(뒷모습 두 사람이 큰 화면의 바위를 봄)를 씀. 씨앗 1은 사람이 화면 속에 들어가 쓰지 않음
4. 렌더링: 프로세스 3개가 자막 그림 460장(장당 약 8MB)을 각각 모두 미리 만들어 메모리가 거의 찼음(각 3.9GB, 남은 2.5GB) → render.py가 맡은 구간의 자막만 만들도록 고침(각 약 1.5GB). 고치기 전과 같은 화면이 나오는지 두 시각에서 확인함(픽셀 차이 0)
3. 앞선 점검(같은 날, 첫 장면표 이후): 같은 클립 구간이 여러 번 겹치던 곳(4915 5번, 51399 5번)을 다른 클립으로 바꿈, 아이가 나오던 장면(8743으로), 내용과 반대인 통화 장면(4951 → 4938), 대학 이름이 보이는 건물(4560 8초부터), 가장자리 글자 잘라 내기(42982, 4401)

## 5. 아직 임시이거나 결정이 필요한 것

1. 배경음악 9곡과 효과음 10곳: 귀로 들어 보고 바꿀 곳을 알려 주세요.
2. AI 사진 7장(B01 영사기, B02 빈 병동, B05 침대 난간, B06 곰인형, B07 뒷모습 간호사, B08b 뒷모습 간호사, B09c_s2 실험실의 뒷모습 두 사람과 바위 화면): 맞는 무료 스톡이 없어 넣었습니다(영사기·병원 침대·간호사 스톡은 모두 제한 라이선스였음). 사용자 검토 전입니다.
3. 연구자 사진과 기관 마크는 쓰지 않았습니다(기본값, CLAUDE.md 영상 제작 5번). 로라(실존 인물)는 그리지 않고 물건과 빈 병동으로 보여 줍니다.
4. 1인칭 아바타, 사례 구간 캐릭터, 썸네일은 이번 영상에 넣지 않았습니다(결정 대기).

## 6. 최종 대본에서 원문과 맞춰 볼 곳 (Claude 메모, 고칠지는 사용자 결정)

녹음이 끝난 대본이라 영상은 대본대로 만들었습니다. 아래는 v2의 근거 메모(대본/01_불안형_답장_v2.md 끝, 원문 확인 기록)와 다른 곳입니다. 고치려면 그 부분을 다시 녹음해야 합니다.

1. 바위와 뱀(de Berker 외 2016): 대본은 "바위 두 개 … 밑에 뱀이 없는 바위를 골라야" 합니다. 근거 메모는 "바위 두 개 중 하나가 뜨면 그 밑에 뱀이 있을지 맞힘"입니다(고르기가 아니라 맞히기). "100% 확실할 때는 오히려 낮아졌다"는 결과를 줄여 말한 것으로 큰 차이는 없습니다.
2. 문자 8분(Smith & Williams 2004): 자기 탓이 가장 많았다는 것은 맞습니다(자기 탓 7명, 기술 문제 5명, 실험자 탓 3명; 답한 사람만, 통계 검정 없음). 다만 "'내가 말을 재미없게 했나?' 하며"는 참가자의 실제 말처럼 들리는데 원문에서 확인한 말이 아닙니다(작업 규칙 12번: 참가자의 말은 원문에 있는 것만).
3. 로라(Robertson 1952): "감염을 막는다는 이유로 … 면회를 엄격하게 금지"는 근거 메모의 "부모 면회가 엄격히 제한됨"보다 나아간 표현이고(이유와 '금지'는 확인하지 않음), "침대 난간을 붙잡고 엄마를 부르며"도 확인한 장면이 아닙니다.
4. 스트레스 호르몬(Diamond 외 2008로 보임): "급격히 치솟고, 밤잠까지 설치는"은 확인한 내용보다 셉니다. 원문은 출장처럼 4~7일 떨어진 커플 42쌍에서 집에 남은 사람 중 애착 불안이 높은 사람만 코르티솔이 올랐다는 것이고, 잠은 확인하지 않았습니다.
5. 만약-그러면(Gollwitzer & Sheeran 2006): "성공 확률이 비약적으로 높아집니다"는 메타분석의 효과 크기(중간에서 큰 정도)보다 센 표현입니다.
6. 어머니 사진(Selcuk 외 2012): "훨씬 더 빠르고 크게 회복"의 '빠르고'는 확인하지 않았습니다. "사진을 먼저 본 그룹에서는 효과가 나타나지 않았다"는 2012년 연구로는 맞지만, 같은 공저자의 2025년 연구(Zayas, Strycharz & Ni 2025)는 먼저 봐도 나쁜 기분이 덜했다고 보고해, 일반 규칙처럼 들리면 최신 결과와 어긋날 수 있습니다(진단 문서 9장에 적어 둔 결정 대기 항목).

## 7. 스톡 영상 (64개, Mixkit)

모두 영상 페이지의 copyrightNotice가 "Free"(Mixkit Stock Video Free License)인 것을 확인했습니다(2026-10-24, 받아 둔 페이지 기준). 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다. 시각은 영상 안에서 장면이 시작하는 때입니다.

1. 4822 Woman texting on the street — https://mixkit.co/free-stock-video/woman-texting-on-the-street-4822/
   - 장면 001 0:00 (1초부터)
2. 4915 Hands of a person typing on a cell phone — https://mixkit.co/free-stock-video/hands-of-a-person-typing-on-a-cell-phone-4915/
   - 장면 002 0:01 (2초부터); 장면 027 1:36 (6초부터); 장면 144 9:20 (11.19초부터)
3. 4548 Woman lying on a sofa — https://mixkit.co/free-stock-video/woman-lying-on-a-sofa-4548/
   - 장면 010 0:42 (2초부터)
4. 26092 Young man eating while watching television — https://mixkit.co/free-stock-video/young-man-eating-while-watching-television-26092/
   - 장면 012 0:45 (1초부터)
5. 51397 Young woman using her cell phone lying in her bed — https://mixkit.co/free-stock-video/young-woman-using-her-cell-phone-lying-in-her-bed-51397/
   - 장면 014 0:51 (1초부터)
6. 51394 Woman with insomnia lying in her bed trying to sleep — https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/
   - 장면 016 0:57 (12초부터); 장면 040 2:10 (3초부터); 장면 107 6:57 (20초부터); 장면 113 7:16 (32.5초부터); 장면 118 7:38 (28초부터)
7. 51399 Restless woman with insomnia trying to sleep — https://mixkit.co/free-stock-video/restless-woman-with-insomnia-trying-to-sleep-51399/
   - 장면 017 0:59 (2초부터); 장면 042 2:18 (8초부터); 장면 057 3:35 (11.7초부터)
8. 4513 Worried and sad woman hugging a cushion — https://mixkit.co/free-stock-video/worried-and-sad-woman-hugging-a-cushion-4513/
   - 장면 019 1:07 (1초부터); 장면 084 5:18 (6초부터)
9. 4733 Scientist observing through a microscope — https://mixkit.co/free-stock-video/scientist-observing-through-a-microscope-4733/
   - 장면 022 1:20 (1초부터)
10. 4897 Girl reading a book in nature — https://mixkit.co/free-stock-video/girl-reading-a-book-in-nature-4897/
   - 장면 023 1:26 (1초부터); 장면 127 8:06 (8초부터)
11. 100050 Woman smiling at her phone on a cozy couch — https://mixkit.co/free-stock-video/woman-smiling-at-her-phone-on-a-cozy-couch-100050/
   - 장면 025 1:31 (1초부터); 장면 184 11:59 (6초부터)
12. 4333 View inside a wagon in motion — https://mixkit.co/free-stock-video/view-inside-a-wagon-in-motion-4333/
   - 장면 026 1:34 (1초부터)
13. 42982 Couple having dinner together at home — https://mixkit.co/free-stock-video/couple-having-dinner-together-at-home-42982/
   - 장면 029 1:40 (1초부터, 가장자리 잘라 냄)
14. 100053 A young smiling woman sitting on a comfy couch using her phone — https://mixkit.co/free-stock-video/a-young-smiling-woman-sitting-on-a-comfy-couch-using-100053/
   - 장면 031 1:45 (1초부터); 장면 155 10:03 (6초부터)
15. 4911 Young woman lying down watching images on her cell phone — https://mixkit.co/free-stock-video/young-woman-lying-down-watching-images-on-her-cell-phone-4911/
   - 장면 032 1:48 (1초부터); 장면 170 11:06 (6.92초부터)
16. 43381 Woman at night lying down using her cell phone — https://mixkit.co/free-stock-video/woman-at-night-lying-down-using-her-cell-phone-43381/
   - 장면 034 1:54 (8초부터); 장면 108 7:01 (1초부터)
17. 4708 Girl regretting regret and sad — https://mixkit.co/free-stock-video/girl-regretting-regret-and-sad-4708/
   - 장면 036 1:56 (1초부터); 장면 164 10:35 (6초부터)
18. 39789 Girl lying down chatting on her cell phone before sleeping — https://mixkit.co/free-stock-video/girl-lying-down-chatting-on-her-cell-phone-before-sleeping-39789/
   - 장면 038 2:02 (0초부터, 휴대폰 뒷면 로고를 지운 판(logo_patch.py))
19. 4457 Tower Bridge in London during sunset — https://mixkit.co/free-stock-video/tower-bridge-in-london-during-sunset-4457/
   - 장면 044 2:27 (1초부터)
20. 4809 Business people at work meeting — https://mixkit.co/free-stock-video/business-people-at-work-meeting-4809/
   - 장면 060 3:47 (1초부터)
21. 101412 Emotionally Disconnected Couple — https://mixkit.co/free-stock-video/emotionally-disconnected-couple-101412/
   - 장면 061 3:49 (1초부터)
22. 51429 A visible looking worried woman walking through her tiny apartment at night — https://mixkit.co/free-stock-video/a-visible-looking-worried-woman-walking-through-her-tiny-apartment-51429/
   - 장면 062 3:53 (2초부터); 장면 101 6:35 (8초부터)
23. 31413 Young man lying on his bed checking his smartphone — https://mixkit.co/free-stock-video/young-man-lying-on-his-bed-checking-his-smartphone-31413/
   - 장면 063 3:56 (1초부터)
24. 42088 Close up of the flag of Australia waving — https://mixkit.co/free-stock-video/close-up-of-the-flag-of-australia-waving-42088/
   - 장면 065 4:05 (1초부터)
25. 4519 Students walking in a university — https://mixkit.co/free-stock-video/students-walking-in-a-university-4519/
   - 장면 066 4:09 (1초부터); 장면 068 4:20 (6초부터)
26. 28321 Frustrated student at his school studying his notes — https://mixkit.co/free-stock-video/frustrated-student-at-his-school-studying-his-notes-28321/
   - 장면 069 4:23 (1초부터)
27. 39958 Boy whispering something funny to a girl — https://mixkit.co/free-stock-video/boy-whispering-something-funny-to-a-girl-39958/
   - 장면 071 4:31 (1초부터)
28. 4560 Students walking through a college — https://mixkit.co/free-stock-video/students-walking-through-a-college-4560/
   - 장면 073 4:41 (1초부터); 장면 163 10:32 (8초부터)
29. 99890 Close up a hand writing notes on a notebook with a pen — https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/
   - 장면 076 4:56 (1초부터)
30. 4701 Worried and sad man with his head down — https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/
   - 장면 079 5:04 (1초부터)
31. 8743 Heartbroken crying woman slowly sits on the floor — https://mixkit.co/free-stock-video/heartbroken-crying-woman-slowly-sits-on-the-floor-8743/
   - 장면 080 5:07 (1초부터)
32. 8739 Worried and sad woman, outdoors — https://mixkit.co/free-stock-video/worried-and-sad-woman-outdoors-8739/
   - 장면 081 5:11 (1초부터); 장면 116 7:30 (6초부터)
33. 51395 Girl using her cell phone in her bed waiting to sleep — https://mixkit.co/free-stock-video/girl-using-her-cell-phone-in-her-bed-waiting-to-51395/
   - 장면 082 5:14 (15초부터); 장면 103 6:43 (1.5초부터); 장면 181 11:40 (8초부터)
34. 40421 Mother hugs her crying daughter — https://mixkit.co/free-stock-video/mother-hugs-her-crying-daughter-40421/
   - 장면 097 6:20 (1초부터)
35. 939 Couple silhouette walking through a neighborhood — https://mixkit.co/free-stock-video/couple-silhouette-walking-through-a-neighborhood-939/
   - 장면 099 6:29 (1초부터)
36. 4500 Upset woman sitting on the floor — https://mixkit.co/free-stock-video/upset-woman-sitting-on-the-floor-4500/
   - 장면 102 6:39 (1초부터)
37. 4549 Mother with her happy daughters — https://mixkit.co/free-stock-video/mother-with-her-happy-daughters-4549/
   - 장면 105 6:50 (1초부터)
38. 4624 Couple holding hands in a walk — https://mixkit.co/free-stock-video/couple-holding-hands-in-a-walk-4624/
   - 장면 106 6:54 (1초부터)
39. 4401 Crowds of people cross a street junction — https://mixkit.co/free-stock-video/crowds-of-people-cross-a-street-junction-4401/
   - 장면 111 7:10 (2.65초부터, 가장자리 잘라 냄)
40. 26091 Man eats watching television on a rainy night — https://mixkit.co/free-stock-video/man-eats-watching-television-on-a-rainy-night-26091/
   - 장면 112 7:14 (1초부터)
41. 4700 Woman stressed and wailing, profile view — https://mixkit.co/free-stock-video/woman-stressed-and-wailing-profile-view-4700/
   - 장면 122 7:48 (1초부터)
42. 4764 Cute old couple in a park — https://mixkit.co/free-stock-video/cute-old-couple-in-a-park-4764/
   - 장면 125 7:59 (1초부터)
43. 4800 Woman meditating with her dog in the sunset — https://mixkit.co/free-stock-video/woman-meditating-with-her-dog-in-the-sunset-4800/
   - 장면 126 8:03 (1초부터)
44. 42270 Face of a very worried girl — https://mixkit.co/free-stock-video/face-of-a-very-worried-girl-42270/
   - 장면 143 9:16 (1초부터)
45. 39780 Girl is awakened by messages that arrive on her cell phone — https://mixkit.co/free-stock-video/girl-is-awakened-by-messages-that-arrive-on-her-cell-39780/
   - 장면 148 9:33 (1초부터, 휴대폰 화면 글자 흐림)
46. 8744 Young man upset and frustrated receiving a message — https://mixkit.co/free-stock-video/young-man-upset-and-frustrated-receiving-a-message-8744/
   - 장면 150 9:41 (1초부터)
47. 4938 Hands of a girl working on a computer — https://mixkit.co/free-stock-video/hands-of-a-girl-working-on-a-computer-4938/
   - 장면 152 9:52 (1초부터)
48. 4761 Concentrated boy studying at home — https://mixkit.co/free-stock-video/concentrated-boy-studying-at-home-4761/
   - 장면 153 9:55 (0.76초부터)
49. 41638 Programmer using his cell phone while working at his desk — https://mixkit.co/free-stock-video/programmer-using-his-cell-phone-while-working-at-his-desk-41638/
   - 장면 154 10:00 (1초부터)
50. 4517 Annoyed woman working in a room — https://mixkit.co/free-stock-video/annoyed-woman-working-in-a-room-4517/
   - 장면 157 10:09 (1초부터)
51. 42655 A woman writing in her spiral notebook — https://mixkit.co/free-stock-video/a-woman-writing-in-her-spiral-notebook-42655/
   - 장면 160 10:18 (1초부터)
52. 41180 Eye of a woman looking at a tablet — https://mixkit.co/free-stock-video/eye-of-a-woman-looking-at-a-tablet-41180/
   - 장면 165 10:37 (1초부터)
53. 4511 Sad girl looking out the window — https://mixkit.co/free-stock-video/sad-girl-looking-out-the-window-4511/
   - 장면 169 11:03 (1초부터)
54. 4656 Couple sitting watching a photo album — https://mixkit.co/free-stock-video/couple-sitting-watching-a-photo-album-4656/
   - 장면 171 11:09 (1초부터)
55. 101233 Girl Hugging Dog — https://mixkit.co/free-stock-video/girl-hugging-dog-101233/
   - 장면 172 11:10 (1초부터)
56. 4644 Photo album opened by a man — https://mixkit.co/free-stock-video/photo-album-opened-by-a-man-4644/
   - 장면 173 11:12 (0.93초부터)
57. 4840 Woman during a sunset on a rooftop — https://mixkit.co/free-stock-video/woman-during-a-sunset-on-a-rooftop-4840/
   - 장면 174 11:16 (1초부터)
58. 52419 The tree branches gently moving with the wind over a clear blue sky and the moon at daytime — https://mixkit.co/free-stock-video/the-tree-branches-gently-moving-with-the-wind-over-a-52419/
   - 장면 175 11:22 (1초부터)
59. 4547 People having a work meeting around a table — https://mixkit.co/free-stock-video/people-having-a-work-meeting-around-a-table-4547/
   - 장면 176 11:27 (1초부터)
60. 1623 People getting into the subway train — https://mixkit.co/free-stock-video/people-getting-into-the-subway-train-1623/
   - 장면 177 11:29 (1초부터)
61. 4231 Pedestrian walk in Tokyo — https://mixkit.co/free-stock-video/pedestrian-walk-in-tokyo-4231/
   - 장면 179 11:33 (1초부터)
62. 25592 Young stressed woman with headache — https://mixkit.co/free-stock-video/young-stressed-woman-with-headache-25592/
   - 장면 180 11:35 (1초부터)
63. 4664 Lovers holding each other on a romantic sunset — https://mixkit.co/free-stock-video/lovers-holding-each-other-on-a-romantic-sunset-4664/
   - 장면 182 11:45 (0초부터, 0.795배속)
64. 100067 A young smiling woman enjoys social media scrolling on her red phone laying on the comfy bed at midnight — https://mixkit.co/free-stock-video/a-young-smiling-woman-enjoys-social-media-scrolling-on-her-100067/
   - 장면 183 11:57 (1초부터)

## 8. AI 사진

RealVisXL V5.0 Lightning(SG161222, openrail++ 라이선스, 상업 이용 가능), scripts/gen_batch.py, 지시문은 ai_images.json. 실존 인물(로라, 연구자)은 그리지 않았고, 사람은 뒷모습만 넣었습니다(B07 뒤쪽의 작은 두 사람은 얼굴을 알아볼 수 없을 만큼 작고 흐림).

1. B01 — 장면 086 5:26 (B01_s1.png): 1952년 영국에서 공개된, 한 흑백 기록 영화 (영사기 스톡 4개가 모두 제한 라이선스)
   - 지시문: vintage 16mm film projector casting a bright beam of light across a dark room, dust in the beam / black and white documentary photo, 1950s, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
2. B05 — 장면 092 5:52 (B05_s1.png): 침대 난간을 붙잡고 엄마를 부르며 (아이는 그리지 않음: 실존 인물)
   - 지시문: close-up of the white iron bars of an old hospital crib, crumpled small blanket inside, dramatic window light / black and white documentary photo, 1950s Britain, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
3. B02 — 장면 088 5:36 (B02_s1.png), 장면 095 6:06 (B02_s1.png): 로라는 작은 수술을 받기 위해, 8일 동안 병원에 입원 (병동, 사람 없음)
   - 지시문: 1950s hospital children's ward, rows of empty white iron cribs with folded blankets, tall windows, polished floor, no people / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
4. B06 — 장면 093 5:57 (B06_s1.png): 로라는 더 이상 울지도 않고, 멍하니 앉아 있습니다 (아이 대신 인형)
   - 지시문: a small worn teddy bear sitting alone in a white iron hospital crib, empty ward, quiet afternoon light / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
5. B07 — 장면 094 6:02 (B07_s1.png): 간호사들 눈에는, 병원 생활에 잘 적응한 아이처럼
   - 지시문: a 1950s nurse in a white uniform and cap walking away down a long hospital ward, seen from behind, iron beds / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
6. B08 — 쓰지 않음: 간호사가 다정하게 다가와 말을 걸자 — 쓰지 않음: 지시문은 뒷모습인데 옆얼굴이 또렷이 나옴(기록 영화 속 실제 간호사로 오해될 수 있음), B08b로 바꿈
   - 지시문: a 1950s nurse in uniform and cap gently leaning over a white iron crib, seen from behind, warm window light / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
7. B09 — 쓰지 않음: 지금 여러분은, 실험실 의자에 앉아 있습니다 (스톡 48503 제한 라이선스) — 쓰지 않음: 오른쪽 모니터에 해골 같은 이상한 그림이 나옴, B09b로 바꿈
   - 지시문: a person seen from behind sitting on a chair facing a large computer screen in a dim psychology lab, cables on the desk
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
8. B08b — 장면 096 6:12 (B08b_s1.png): 간호사가 다정하게 다가와 말을 걸자 (B08을 다시 만듦: 뒷모습)
   - 지시문: back view of a 1950s nurse in a white uniform and cap, her back to the camera, bending over a white iron crib in a hospital ward, warm window light / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
9. B09b — 쓰지 않음: 지금 여러분은, 실험실 의자에 앉아 있습니다 (B09를 다시 만듦: 화면에 바위 사진) — 쓰지 않음: 사람이 빠지고 의자가 일그러짐
   - 지시문: a person seen from behind sitting on a chair in a dim psychology lab, facing one large monitor that shows a photograph of grey rocks on the ground, thin electrode wire on the desk
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
10. B09c — 장면 045 2:32 (B09c_s2.png), 장면 050 2:54 (B09c_s2.png): 지금 여러분은, 실험실 의자에 앉아 있습니다 (B09 지시문에 화면의 바위를 더함) — 씨앗 2(B09c_s2)를 씀: 뒷모습 두 사람이 큰 화면의 바위를 봄. 씨앗 1은 사람이 화면 속에 들어가 쓰지 않음
   - 지시문: a person seen from behind sitting on a chair facing a large computer screen in a dim psychology lab, the screen shows a photo of two grey rocks, cables on the desk
   - 씨앗 1, 2, 1152x648, 5단계, CFG 1.0

## 9. 배경음악 (Mixkit Stock Music Free License, -36 LUFS, 곡이 바뀔 때 3초 겹침)

1. 0:00~1:31 Beautiful Dream / Diego Nava (Mixkit 493, https://mixkit.co/free-stock-music/) — 도입: 연인과의 카톡, 기다림 (Jazz, Melancholic, Love)
2. 1:31~2:27 Love in the Air / Ahjay Stelino (Mixkit 41, https://mixkit.co/free-stock-music/) — 공감 사례 지우: 설렘에서 불안으로 (Reflective, Piano, Strings, Love)
3. 2:27~3:58 Tapis / Eugenio Mininni (Mixkit 615, https://mixkit.co/free-stock-music/) — 실험 1 뱀과 바위: 긴장 (Mysterious, Atmospheric)
4. 3:58~5:20 Staring at the Night Sky / Alejandro Magaña (Mixkit 168, https://mixkit.co/free-stock-music/) — 실험 2 노키아 문자: 침묵 (Mysterious, Cello, Piano)
5. 5:20~7:08 Classical vibes 1 / Grigoriy Nuzhny (Mixkit 681, https://mixkit.co/free-stock-music/) — 로라와 애착: 슬픔 (Reflective, Piano, Drama)
6. 7:08~7:50 Alignment / Arulo (Mixkit 310, https://mixkit.co/free-stock-music/) — 개인차: 생각 (Hopeful, Reflective, Piano)
7. 7:50~9:27 Classical 6 / Jonny S. (Mixkit 713, https://mixkit.co/free-stock-music/) — 희망과 해결책 1 (Hopeful, Reflective, Piano)
8. 9:27~11:15 Classical vibes 2 / Grigoriy Nuzhny (Mixkit 682, https://mixkit.co/free-stock-music/) — 해결책 2, 3 (Uplifting, Hopeful, Piano)
9. 11:15~12:03 We'll Be Okay / Michael Ramir C. (Mixkit 1081, https://mixkit.co/free-stock-music/) — 마무리 (Reflective, Emotional, Piano)

## 10. 효과음 (Mixkit Sound Effects Free License)

1. 2354 Message pop alert
2. 2357 Bubble pop up alert notification
3. 1395 Typing text on a smartphone
4. 1050 Slow tick-tock clock timer
5. 2365 Electric pop

넣은 자리(sfx_log.json):
1. 0:04 (4.13초) 보냄: 오늘 퇴근하고 뭐할꺼야?
2. 0:13 (13.80초) 받음: 뭐 할껀 없어, 같이 저녁 먹을까?
3. 0:19 (19.87초) 받음: 헉 미안해, 회식 와서 연락을 이제 받네.
4. 0:47 (47.02초) 시계 초침: 하지만 3시간, 4시간이 넘어가면,
5. 1:39 (99.24초) 보냄: 오늘 하루 어땠어요?
6. 1:51 (111.99초) 시계 초침: 그렇게 9시가 되고,
7. 1:55 (115.98초) 보냄: 바쁘세요??
8. 2:13 (133.77초) 보냄: 자요..?
9. 2:49 (169.67초) 전기: 손등에 따끔한 전기가
10. 9:24 (564.06초) 메모 입력
