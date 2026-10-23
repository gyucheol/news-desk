# 번아웃 편 본편 기록

작성 2026-10-22, 2차~5차 수정본 2026-10-23. 결과 파일: burnout_v5.mp4 (1920×1080, 30fps, 8분 15초). 운영자 목소리가 들어 있어 영상과 녹음은 저장소에 커밋하지 않았습니다(SendUserFile로 전달). 첫 완성본(burnout_full.mp4, 8분 18초)의 기록은 커밋 7220ef9, 2차 수정본(8분 9초)은 커밋 73ac990, 3차 수정본(8분 11초)은 커밋 df49335, 4차 수정본(8분 13초)은 커밋 df30733에 있습니다.

아래 시각은 모두 5차 수정본 기준입니다.

---

## 0. 수정 기록

### 0-1. 5차 수정 (2026-10-23, 재녹음 2곳·장면·자막 나눔)

사용자 요청(3차 수정본을 보고 보낸 목록): 6:07 문장을 "작년 십이월, 한 언론 기사에 31살 직장인 박 모 씨의 이야기가 실렸습니다"로 바꿔 1번 파일로 바꾸고 배경은 스톡 뉴스 사진에 아주 천천히 확대, 6:15 문장을 "출근하면 일할 의욕이 없고, 퇴근해서 취미를 하나 만들어보려고 해도 너무 피곤해서 잠만 자는 날이 계속 이어졌다고 합니다"로 바꿔 2번 파일로 바꾸고 관련 스톡 영상, 두 녹음 모두 "뒤에 갑자기 소리가 줄어들거나 짤리는 일 없게", 인용 뒷배경이 점점 확대, "저는 / '열심히 살고 있는데도' / 라는 부분이 / 유독 마음에 오래 남더라고요"로 자막 나눔, 그리고 소리가 이상한 곳 여섯 군데. 기록에서는 1번 파일을 re6, 2번 파일을 re7로 부릅니다.
1. 녹음: 두 파일(5.2초, 7.4초)을 받아 적어 보니 대본과 글자가 같았습니다. 4차의 5번 파일처럼 숨소리·입소리 처리와 쉼 자르기 없이 다듬고(polish_voice.py --keep-levels), 목소리 30ms 앞부터 넣었습니다(edit_narration_v5.py, edit_log_v5.json).
2. 끝: 두 파일 모두 녹음 앱이 맨 끝 0.06~0.09초를 배경 소리보다 작게 줄여 놓았습니다. 목소리는 그 전에 배경 수준까지 잦아들어 있어서(1번 5.34초, 2번 7.555초), 앱이 줄이기 시작하는 곳(5.35초, 7.58초)까지 쓰고 원래 녹음의 실내 소리로 20ms 동안 넘겼습니다. 처음에는 앱이 줄인 부분을 실내 소리와 겹쳐 넘겼는데, 배경 소리가 0.05초 동안 -69dB까지 빠져서 바꿨습니다. 목소리의 끝 울림은 자르지 않았습니다.
3. 크기: 바꾸는 원래 부분과 같은 크기(BS.1770 적분 음량)로 일정하게 맞췄습니다(1번 -0.9dB, 2번 -1.4dB). 맞춘 뒤 1번 -14.8 LUFS(원래 -14.8), 2번 -15.4 LUFS(원래 -15.5)입니다. loudnorm으로 재면 5~7초짜리 짧은 구간에서 0.8dB까지 낮게 나와 이 두 곳은 ebur128로 쟀습니다. 1~5번 파일은 4차 값 그대로입니다(ebur128로 다시 재도 차이 0.55dB 이하).
4. 쉼: 새 문장 앞뒤 쉼은 원래 녹음의 길이로 맞췄습니다(1번 앞 0.175초, 뒤 0.195초, 2번 앞 0.17초). 2번 뒤 "그리고 기사에서" 앞은 원래 0.11초로 짧아서, 다른 문장 사이와 비슷한 0.19초로 두었습니다.
5. 바꾼 두 곳 밖의 소리는 4차 수정본과 샘플 단위로 같습니다. 새 문장이 원래보다 길어 1번 뒤는 0.57초, 2번 뒤는 1.74초 늦게 나옵니다. 영상은 8분 15초입니다.
6. 자막: 6:07 "작년 12월, 한 언론 기사에 / 31살 직장인 / 박 모 씨의 이야기가 실렸습니다."(서른한 살 → 31살). 6:15 "출근하면 일할 의욕이 없고, / 퇴근해서 취미를 하나 / 만들어보려고 해도 / 너무 피곤해서 잠만 자는 날이 / 계속 이어졌다고 합니다."(U238~U241b, 녹음에서 쉬거나 숨을 고르는 자리에서 나눔). 6:31 "저는 이 말 중에서 / '열심히 살고 있는데도' / 라는 부분이 / 유독 마음에 오래 남더라고요."(U248~U250b). 녹음에 있는 "이 말 중에서"는 사용자 지시("녹음된 걸 기준으로")대로 남겼고, "라는" 앞에는 녹음에도 짧은 쉼이 있습니다. 새 녹음 부분은 다시 받아 적고(align_v5.py) 쉼 뒤 목소리 시작과 음절 정렬로 맞췄습니다. 나머지 305줄은 4차와 같은 시각(늦춰진 만큼만 다름)이고, U271은 4차처럼 직접 고쳤습니다(7:07).
7. 장면
   1. 6:07 뉴스: 신문 기사 그림 대신 Mixkit 41192(펼친 신문을 위에서 본 장면)의 7.4초 장면 한 장을 깔고 5.3초 동안 1.0배에서 1.04배로 천천히 다가갑니다. 실제 멕시코 신문이라 기사 제목과 신문 이름이 읽히지 않게 흐리게(12) 하고 어둡게 했습니다. 그 위에 "작년 12월 / 31살 직장인 / 박 모 씨"를 각각 말하는 순간에 나타나게 했습니다(4차까지는 "26살 직장인"과 "박 모 씨"가 말보다 먼저 나왔음).
   2. 6:15 출근하면 일할 의욕이 없고: 사무실 책상에서 노트북 대신 휴대폰을 보는 젊은 남성을 위에서 찍은 장면(4801, 얼굴이 보이지 않음).
   3. 6:17 퇴근해서 취미를 하나 만들어보려고 해도: 기타 코드를 잡는 손(42834).
   4. 6:19 너무 피곤해서 잠만 자는 날이: 눈가리개를 내리며 눕는 남성(31416). 6:21 계속 이어졌다고 합니다: 잠든 모습(31411). 앞 장면 "그는 처음엔…"(31415)과 같은 인물입니다.
   5. 사무실에서 의욕 없는 모습을 직접 보여 주는 Mixkit 영상 7개(48609, 6328, 49482, 8904, 11599, 47988, 14798)는 제한 라이선스였고, 무료인 4607은 이 영상에서 이미 두 번 써서 고르지 않았습니다.
   6. 6:25 인용 뒷배경(A16): 5.9초 동안 1.0배에서 1.05배로 천천히 다가갑니다(4차는 1.05배로 멈춰 있었음).
   7. 빠진 영상: 26089(폭식), 26090의 두 번째 쓰임(입맛), 31411의 앞 시작점(화장실 갈 기운). 26090은 3:45에 그대로 있습니다.
8. 소리가 이상한 여섯 곳: 4차 수정본이 나오기 전에 3차를 들으며 보낸 목록이라, 4차 수정본의 같은 자리를 원래 녹음과 10ms 단위로 비교했습니다. 여섯 곳 모두 원래 녹음과 크기 흐름이 같고(차이 1dB 안), 마지막 리미터도 그 자리에서 0.5dB 넘게 누르지 않습니다. 3차의 원인은 다음과 같았고 모두 4차에서 고쳤습니다(0-2). 5차는 그 상태를 그대로 씁니다.
   - "배터리는 또 닳기 시작할 거예요"(5:59): 숨소리 줄이기가 마지막 '요'를 약 10dB 줄였고, loudnorm이 앞 구절을 4~5dB 눌렀습니다.
   - "이렇게 며칠만 적어 봐도 ~ 시작합니다"(7:06): 뒤에 넣은 쉼 소리에 끝 울림 조각(-33dB)이 섞여 '다'가 한 번 더 들렸습니다.
   - "…짚어 보는 거죠"(7:26): 쉼 자르기가 '죠'의 끝 0.15초를 잘랐습니다.
   - "딱 하나만 짚어 봐도"(7:29): 숨소리 줄이기가 구절 안을 5~12dB 줄였습니다.
   - "…보여 주는 건지도 모릅니다"(7:47), "…작은 도움이 되었으면 좋겠습니다"(8:10): 끝 '다'가 잘렸고, 뒤의 쉼 소리 조각이 '다'처럼 다시 들렸습니다.

### 0-2. 4차 수정 (2026-10-23, 끝소리·재녹음·사진·WHO 마크)

사용자 요청: 3차의 새 문장 끝이 잘렸으니 고칠 것, 프로이덴버거 사진(저작권 허락 받음)과 WHO 마크(보낸 그림에서 추출)를 넣을 것, U156~U162를 새 녹음(5번 파일)으로 바꾸되 "녹음한 파일이 짤리거나 후반에 소리가 줄어들거나 그렇게 만들지마".
1. 잘린 끝소리: 3차의 새 문장(4번 파일) "…모르겠습니다"의 마지막 '다' 울림이 잘려 있었습니다. polish_voice.py가 파일 끝을 '마지막 목소리 + 0.35초'에서 잘랐고, 이어 붙이는 단계가 한 번 더 잘랐습니다. 같은 이유로 1번(…주세요, 0.12초)과 2번(…모릅니다, 0.09초)도 끝 울림이 잘려 있었습니다(3번은 없음). 이제 잦아드는 소리가 배경 수준으로 내려간 뒤 0.1초까지 남기고, 이어 붙일 때는 다듬은 파일 끝까지 씁니다. 말이 끝난 뒤 조용한 시간은 3차와 같게 맞췄습니다(이어지는 쉼을 0.1초 줄임).
2. U156~U162 재녹음: 3:59 "회의에서 새로운 의견이 나오면 ~ 점심은 그냥 혼자 먹고 싶어지죠."를 5번 파일로 바꿨습니다. 받아 적은 글자가 기존 자막과 같아 자막 글자는 그대로입니다. 사용자가 "문장 끝부분들이 이상하다"고 한 원인은 녹음이 아니라 처음 다듬을 때의 숨소리 줄이기였습니다. 문장 끝의 약한 울림("듭니다"의 '다', "싶어지죠"의 '죠')을 숨소리로 보고 12dB 줄였습니다. 5번 파일은 숨소리·입소리 처리와 쉼 자르기 없이, 저음 잡음 제거(75Hz)와 일정한 음량만 적용했습니다.
3. 같은 일이 전체 녹음의 다른 문장 끝에도 있었습니다. 처음 '숨소리'로 줄인 63곳 중 스펙트로그램으로 확인한 표본(16곳)은 거의 모두 말소리(문장 끝 울림이나 다음 단어의 시작)였습니다. 그래서 전체 녹음과 1~4번 파일도 숨소리·입소리 처리 없이 다시 다듬었습니다(polish_voice.py --keep-levels). 쉼은 처음과 같은 자리를 잘라(--cuts-from) 시각이 그대로입니다. 다만 7:28 앞 "…거죠." 끝을 0.15초 잘라 먹던 한 곳은 자르지 않아 그 뒤가 0.21초 늦어졌습니다. 처음 자른 자리 중 끝 울림과 겹치는 곳이 10곳 더 있지만, 겹치는 양이 0.04초 이하이거나 영상에 쓰지 않는 구간입니다.
4. 음량: 예전에는 녹음 다듬기와 낭독본 음량 맞추기에서 ffmpeg loudnorm이 dynamic 모드로 돌았습니다(피크가 한도를 넘으면 알리지 않고 바뀜). 그래서 구간마다 소리 크기가 -1~+3.5dB 오르내렸고, 특히 첫 30초가 2~3.5dB 작게 눌려 있었습니다. 이제 모든 단계가 일정한 비율 하나로만 맞추고, 마지막 섞기에서만 리미터(-1.5dBFS)로 피크를 누릅니다(prep_audio.py, mix_audio.py). 최종 -14.1 LUFS, 피크 -1.4dBTP, 음량 폭(LRA) 4.4LU입니다.
5. 쉼 소리(방 소리): 0.4초 창의 평균으로 고르던 것을 0.2초 창의 가장 큰 값으로 고르게 바꿨습니다. 예전 방식은 -33dB의 끝 울림 조각을 쉼 소리에 섞었습니다. 이제 -52dB입니다.
6. 프로이덴버거 사진: 사용자가 저작권자 허락을 받았다고 알려 준 사진을 1:14 "미국의 심리학자 / 허버트 프로이덴버거인데요"의 이름 카드 자리에 넣었습니다. 1970년대 장면과 같은 색 보정이고 천천히 다가갑니다. 허락은 영상에 쓰는 것이라 사진 파일은 커밋하지 않았습니다(work/photos/freudenberger.png).
7. WHO 마크: 사용자가 보낸 WHO 깃발 그림에서 파란 배경을 빼고 마크만 뽑아, 2:39 "2019년 / 세계보건기구 (WHO)" 화면의 지구 그림 자리에 넣었습니다(사용자 결정). WHO는 엠블럼 사용을 제한하고 있습니다(특히 WHO가 보증하는 것처럼 보이는 사용). 파일은 커밋하지 않았고(work/photos/who_emblem.png), 파일이 없으면 지구 그림이 나옵니다(icons.py).
8. 자막 시각은 새 낭독본에서 다시 쟀습니다(align_v4.py → onsets.py → ctc_align.py). 바뀌지 않은 307줄 중 300줄은 3차와 0.05초 안에서 같습니다. 0.1초 넘게 달라진 6줄을 확인했습니다. U183·U030은 3차가 한 음절 늦었고, U175·U242는 3차가 쉼 안에서 0.2초 일렀습니다(4차가 맞음). U285는 늘어난 쉼만큼 늦어졌습니다. U271("'아, 월요일…")은 작게 말한 '아'를 잡음으로 보고 늦게 잡혀서, 7:07(425.64초)로 직접 고쳤습니다.

### 0-3. 3차 수정 (2026-10-23, 앞부분 대본 한 문장)

사용자가 앞부분의 한 문장을 바꾸고 그 문장만 다시 녹음했습니다("대본 및 녹음본 교체").
1. 대본: "그렇다면 오늘 이야기가 작은 힌트가 될지도 모르겠습니다." → "그렇다면 오늘 이야기가 그 질문의 답을 찾는 데 작은 힌트가 될지도 모르겠습니다." 사용자가 적은 "찾는데"는 '데'가 의존 명사(~하는 일)라서 맞춤법대로 "찾는 데"로 띄었습니다.
2. 자막: 0:15부터 세 줄입니다. "그렇다면 오늘 이야기가 / 그 질문의 답을 찾는 데 / 작은 힌트가 될지도 모르겠습니다." (U012, U012b, U013). 세 줄 모두 쉼 뒤 목소리가 시작하는 때에 나옵니다. 전구 그림 화면이 세 줄을 모두 덮습니다.
3. 녹음: 새 녹음(4번 파일, 5.1초)을 polish_voice.py로 다듬어 원래 문장 자리에 넣었습니다(edit_narration_v3.py, edit_log_v3.json). 앞뒤 쉼은 원래 길이(앞 0.34초, 뒤 0.38초)로 맞추고, 소리 크기는 원래 문장에 맞췄습니다(3차 당시 +0.65dB). 이때 끝 울림이 잘렸고 4차에서 되살렸습니다(0-2). 말 빠르기는 앞뒤 문장과 비슷해서(초당 약 7.6음절, 앞뒤 7.5~8.1음절) 바꾸지 않았습니다.
4. 새 문장이 원래보다 1.56초 길어, 그 뒤의 자막, 장면, 배경음악 구간이 모두 1.56초씩 늦춰졌습니다. 바꾼 문장 밖의 소리는 2차 수정본과 한 샘플도 다르지 않았습니다. 영상은 8분 11초였습니다.

### 0-4. 2차 수정 (2026-10-23 사용자 요청)

사용자가 첫 완성본을 보고 고칠 곳을 적어 주었습니다. 같은 날 "사진·영상을 전부 AI 사진으로 만드는 건 나중에 하고, 수정 요청한 것만 먼저 반영"하라고 해서 목록에 있는 것만 바꿨습니다.

1. 시각: 자막, 장면 전환, 가운데 글씨가 다음 목소리가 나오기 시작할 때 바뀝니다. 첫 완성본은 refine.py가 숨소리 시작이나 쉼 중간을 시작으로 잡아 평균 약 0.2초, 길게는 0.7초 일찍 바뀌었습니다. 이번에는 onsets.py(쉼 뒤 실제 목소리 시작)와 ctc_align.py(음절 단위 강제 정렬)로 정하고 앞당기지 않았습니다(spec.json의 sub_lead 0). 4차 기준 316개 단위 중 214개는 쉼 뒤 목소리 시작(그중 210개는 음절 정렬과 0.15초 안에서 일치), 101개는 이어 말하는 구간이라 음절 정렬 시각입니다.
2. 가운데 글씨: 64px → 70px. 64px에서 1px 키우면 눈에 보이지 않아, 문서에서 10pt를 11pt로 키우는 비율(약 9%)로 한 단계 키웠습니다. 아래 자막은 64px 그대로입니다.
3. 배경음악: -32 → -36 LUFS(약 4dB 작게). 내레이션보다 약 22dB 낮습니다.
4. 장면 바꿈(사용자 목록 순서)
   1. 0:41 "집에 와서는 ~ 휴대폰 화면만 멍하니": 침대에 누워 휴대폰을 보는 사람(31413, 0초부터). 장면 017.
   2. 1:12 "심리학에서 이 말을 처음 쓴 사람은": 1970년대 상담실 AI 사진(A01). 1:14 "미국의 심리학자 허버트 프로이덴버거인데요": 이름 카드(이름, 영문 이름, 1926–1999 · 미국의 심리학자). 4차에서 사용자가 허락받은 실제 사진으로 바꿨습니다.
   3. 1:17 "1970년대 뉴욕에서 일하던 그는": 1970년대 뉴욕 거리 AI 사진(A02) 위에 큰 글자 "1970년대"와 작은 글자 "뉴욕".
   4. 1:19 "누구보다 열정과 사명감이 넘치는 사람이었습니다": 촛불 옆에서 밤늦게 타자기를 치는 손(10395, 얼굴이 나오지 않음). AI 사진을 두 번 만들었으나 둘 다 얼굴이 나와 프로이덴버거 본인으로 오해될 수 있어 쓰지 않았습니다.
   5. 1:42 "그는 그날 아침 침대에서 ~ 며칠 내내 앓아누웠습니다": 침대에 누운 사람의 뒷모습 AI 사진(A07).
   6. 2:21 "이렇게 열정을 다 태우고 ~ '번아웃'이라고 불렀습니다": 연기 장면 대신 벽에 기대 무릎에 고개를 묻은 사람 AI 사진(A11), 1.2초 뒤 가운데에 큰 글자 "번아웃".
   7. 2:34 "오히려 누구보다 책임감이 강하고 ~ 제일 먼저 번아웃에 빠졌다는 거죠": 앞 영상(50133)을 문장 끝까지 이어서 씁니다(첫 완성본은 마지막 문장에서 연기 장면으로 바뀜).
   8. 2:39 "그로부터 한참 뒤인 2019년, 세계보건기구는": "2019년"과 "세계보건기구 (WHO)" 글자 화면. 4차에서 WHO 마크를 넣었습니다(0-2의 7번).
   9. 5:10 "휴가에 관한 연구들은": 연구 논문과 그래프 AI 사진(A12).
   10. 6:07 "작년 12월, 한 언론 기사에": 신문 기사 그림 화면(뉴스, 작년 12월, 26살 직장인, 박 모 씨가 차례로 나타남). 5차에서 신문 사진으로 바꿨습니다(0-1의 7번).
   11. 6:25 "열심히 살고 있는데도 ~ 오는 것 같다": 거리 인터뷰 AI 사진(A16)을 흐리고 어둡게 깔고(흐림 9) 그 위 가운데에 인용 글자. 5차에서 천천히 다가가게 했습니다.
5. 가운데 글씨 나눔(사용자가 / 로 나눈 대로)
   - 2:43 '제대로 관리되지 않은 / 만성적인 직장 스트레스에서 생기는 증후군' / 이라고 정의했습니다.
   - 6:00 바로 이 때문에 / 번아웃을 / 개인의 의지만의 문제로 보기는 / 어렵습니다.
   - 6:04 이쯤에서 / 한 사람의 / 실제 이야기를 / 들려드릴게요.
6. 뺀 문장: "예전엔 즐겁던 동료들의 수다조차 요즘은 시끄럽게만 들리고요."(목소리, 자막, 장면 모두). 앞뒤 쉼 안에서 잘라 이었습니다(4:12 바로 앞).
7. 4:51 가운데 글씨에서 "그러니까"를 뺐습니다("내가 해낼 수 있다는 믿음이"). 목소리는 그대로입니다.
8. 다시 녹음 3개로 바꿈(edit_narration_v2.py, edit_log_v2.json, 3차의 edit_narration_v3.py에도 그대로 들어 있음)
   - 1번 파일: 6:45 "혹시 지금 이 이야기가 ~ 번아웃을 극복하는 작은 방법 두 가지를 가볍게 기억해 주세요."(첫 녹음은 '번이웃'으로 발음)
   - 2번 파일: 7:39 "주말 내내 자고도 ~ 보여 주는 건지도 모릅니다."
   - 3번 파일: 8:01 "쉬어도 풀리지 않는 피로가 ~ 작은 도움이 되었으면 좋겠습니다." 사용자 메모에는 "음성파일 1"로 적혀 있었으나, 녹음 내용을 받아 적어 보니 이 문장은 3번 파일이었습니다.
   - 다시 녹음한 부분은 polish_voice.py로 다듬고, 바꾼 원래 구간과 소리 크기(LUFS)를 맞췄습니다(조정 -1.0~+0.2dB).
9. 7:06 "이렇게 며칠만 적어 봐도 ~ 눈에 들어오기 시작합니다." 뒤에 숨 쉴 틈을 0.45초 넣었습니다.
10. 끝: 마지막 말이 8:11에 끝나고 약 3초 뒤에 영상이 끝납니다(첫 완성본은 말이 끝난 뒤 12초). 마지막 자막은 말이 끝나고 1초 뒤 사라지고, 화면은 마지막 1.5초, 배경음악은 마지막 2.5초 동안 줄어듭니다.

---

## 1. 구성

1. 대본: 사용자가 준 "[번아웃 온 사람 특징 대본]"에 3차에서 한 문장(0-3), 5차에서 두 문장(0-1)을 바꾼 것. 자막에서 오타 3곳을 고쳤습니다(회서에서 → 회사에서, 번이웃을 → 번아웃을, 들려드릴께요 → 들려드릴게요).
2. 목소리: 운영자 녹음 490.2초를 polish_voice.py로 다듬고(4차부터 숨소리·입소리 처리 없음, 쉼은 처음과 같은 자리), 재녹음 7곳(re1~re7, 5차의 1·2번 파일이 re6·re7)과 한 문장 삭제, 숨 쉴 틈 1곳을 편집해 말이 491.6초에 끝나고, 끝 3초를 더해 494.7초입니다. 속도는 녹음 그대로(1.0배)입니다.
3. 자막: 316개 단위(units.json). 숫자는 아라비아 숫자로 씁니다(2026-10-22 사용자 지시, 예: 천구백칠십 년대 → 1970년대). 바꾼 표현은 build_spec.py의 DIGITS에 있습니다. 서수(첫 번째)와 '한 번', '한 발', '숫자 하나'는 글자로 둡니다.
4. 장면 137개: 스톡 영상 78, 사진 8(AI 6, 사용자 제공 1, 스톡 영상의 한 장면 1), 그림 화면 27, 검은 화면 카드 24. 컷 길이 중앙값 3.4초입니다.
5. 그림 화면: scripts/icons.py로 직접 그렸습니다(시계, 계기판, 연료, 배터리 둘, 앱, 꺼지는 휴대폰, 연구 문서, 휴가 그래프, 복귀 첫 주, 휴가 길이 막대, 일터의 6가지 조건, 요일별 점수, 10점 메모, 2019년·세계보건기구(WHO 마크)). 5차의 신문 사진 위 글자(news_card)도 icons.py로 그립니다.
6. 세 가지 신호 카드 위에 "1 / 3", "2 / 3", "3 / 3"을 작은 회색 글씨로 넣었습니다.
7. 색 보정: 프로이덴버거 이야기(1970년대)는 채도를 크게 낮춘 PAST 보정, 나머지는 DARK·BRIGHT 보정입니다(build_spec.py 맨 위). 사진도 같은 보정을 거칩니다.
8. AI 사진 6장: RealVisXL V5.0 Lightning(openrail++ 라이선스)으로 scripts/gen_batch.py로 만들었습니다(목록은 아래 8. 사진). 그림 파일은 images/, 지시문과 씨앗은 ai_images.json에 있습니다. 사실적인 사람 모습이 들어가므로 업로드할 때 유튜브의 변경·합성 콘텐츠 질문에 "예"로 답합니다(핸드오프 5-3).

---

## 2. 배경음악 (흐름이 바뀌는 곳마다 바꿈)

2026-10-22 사용자 지시: 배경음악은 한 곡일 필요가 없고, 상황이 반전되거나 바뀌면 자연스럽게 바꿔도 좋음. 곡이 바뀌는 곳에서 3초 동안 겹쳐 넘깁니다. 모두 Mixkit Stock Music Free License(음악 목록 페이지 표기, 2026-10-22 확인)입니다. AI는 소리를 들을 수 없어 태그와 분위기 목록으로 골랐습니다(핸드오프 5장 5-2).

1. 0:00–1:09 훅과 일주일 묘사 — 614 Silent Descent (Eugenio Mininni)
2. 1:09–1:33 번아웃이라는 이름, 프로이덴버거 소개 — 168 Staring at the Night Sky (Alejandro Magaña)
3. 1:33–2:26 크리스마스 아침에 무너짐, 녹음기 — 520 Ode to Loneliness (Diego Nava)
4. 2:26–5:05 핵심 메시지, 세계보건기구 정의, 세 가지 신호 — 184 Vastness (Andrew Ev)
5. 5:05–6:04 휴가 연구, 일터의 원인 — 22 Piano Reflections (Ahjay Stelino)
6. 6:04–6:44 31살 직장인 사례 — 601 Skyline (Eugenio Mininni)
7. 6:44–7:38 작은 방법 2가지 — 148 Forest Mist Whispers (Alejandro Magaña)
8. 7:38–끝 마무리 — 684 Classical vibes 4 (Grigoriy Nuzhny)

- 번호는 Mixkit 곡 번호입니다. 파일 주소는 https://assets.mixkit.co/music/<번호>/<번호>.mp3 입니다(fetch_stock.sh).
- 곡이 바뀌는 시각은 그 단락 첫 자막 0.4초 전입니다(bgm_segments.json).
- 소리 크기: 곡마다 고르게 펴고(dynaudnorm) 같은 크기로 맞춘 뒤, 배경음악 전체 -36 LUFS(첫 완성본 -32), 내레이션과 섞은 최종 -14.1 LUFS입니다(4차부터 일정한 비율 하나와 마지막 리미터만 씀).
- 곡을 바꾸려면 bgm_segments.json에서 그 구간의 track만 바꾸고 3장의 7~8단계를 다시 실행합니다.

---

## 3. 다시 만드는 순서 (video/burnout 폴더에서)

1. `full/fetch_stock.sh` (스톡 영상 63개와 음악 8곡을 work/stock/에 받고, 신문 장면 한 장을 work/stock/stills/에 뽑음). 사용자가 준 사진 두 장(work/photos/freudenberger.png, who_emblem.png)은 저장소에 없어 운영자에게 다시 받아야 합니다.
2. 녹음 다듬기(녹음 원본은 운영자가 다시 줘야 함). 쉼은 기록된 자리만 자르고(--cuts-from), 소리 크기는 건드리지 않습니다(--keep-levels):
   `venv/bin/python scripts/polish_voice.py work/rec.m4a work/narration_take.wav --section 25.42,67.8,158.08,196.02,234.1,272.84,307.62,365.86,405.02,458.36 --cuts-from full/polish_v4/take.json --keep-levels --report work/polish_take.json`
   - 재녹음 7개도 같게: `venv/bin/python scripts/polish_voice.py work/re1.m4a work/re1_pol.wav --cuts-from full/polish_v4/re1.json --keep-levels --report work/re1_polish.json` (re2~re5도 같게, re6·re7은 full/polish_v5/의 기록으로. re5~re7은 자르는 곳 없음). --words(faster-whisper 단어 시각)를 주지 않으면 도구가 받아 적습니다.
3. 편집: `python3 full/edit_narration_v5.py work/narration_take.wav work work` 다음 `venv/bin/python scripts/prep_audio.py work/narration_v5_raw.wav work/narration_v5.wav` (re6·re7의 다듬기 기록 re6_polish.json, re7_polish.json도 work/에 있어야 함)
4. 자막 시각: 커밋된 full/align_refined.json을 씁니다(같은 녹음과 편집일 때). 새로 맞추려면 full/align_v2.py → full/align_v3.py → full/align_v4.py → full/align_v5.py → scripts/onsets.py → scripts/ctc_align.py(각 파일 맨 위의 사용법) 다음, U271의 시작을 427.38초로 고칩니다(0-2의 8번, 0-1의 6번).
5. 장면 명세: `python3 full/build_spec.py full work/stock/search/index.json` (검색 목록이 없으면 마지막 인자를 빼도 됩니다. 장면 메모만 빠짐). AI 사진은 full/images/, 프로이덴버거 사진은 work/photos/에서 읽습니다.
6. 배경음악: `venv/bin/python scripts/bgm_sequence.py full/bgm_segments.json 494.723 work/bgm.wav --lufs -36 --fade-out 2.5`
7. 섞기: `venv/bin/python scripts/mix_audio.py work/narration_v5.wav work/bgm.wav work/final_audio.wav`
8. 타임라인: `venv/bin/python scripts/build_timeline.py full/spec.json full/align_refined.json work/final_audio.wav work/timeline.json` 다음 `venv/bin/python scripts/fit_clips.py work/timeline.json` (짧은 스톡의 시작점을 당김: 장면 051, 080, 113, 114)
9. 렌더링 전 글자 검사: `venv/bin/python scripts/ocr_scan.py work/timeline.json work/ocr` (tesseract, 약 2분)
10. 렌더링: `venv/bin/python scripts/render.py work/timeline.json work/burnout_v5.mp4` (8분 15초에 약 30~50분, 2026-10-23)

---

## 4. 점검에서 고친 것

### 4-1. 첫 완성본 (2026-10-22, 장면 번호는 첫 완성본 기준)

스톡 장면 86개의 가운데 화면을 모두 뽑아 보고, 의심되는 곳은 원래 크기로 확대해 확인했습니다(지침: 로고·읽히는 글자·실존 인물로 오해될 얼굴 금지). 그 뒤 모든 스톡 장면을 초당 2장씩(610장) 글자 인식기(scripts/ocr_scan.py)로 검사했고, 걸린 것은 창문·불빛 무늬 같은 잡음뿐이었습니다. 글자 인식기는 흐린 글자를 사람보다 못 읽으므로(4번 신문 예), 흐림을 쓴 장면과 글자가 있을 만한 장면의 처음·끝 화면은 눈으로 다시 봤습니다.
1. 장면 044(4766): 가운데의 나이 든 의사가 프로이덴버거 본인으로 보일 수 있어 강하게 흐리게(blur 16) 했습니다. "동료들을 떠올렸어요"에 맞는 기억 속 장면처럼 보입니다.
2. 장면 038(4701): 프로이덴버거 이야기 구간이라 옆얼굴이 보이는 부분 대신 두 손으로 얼굴을 가린 0~2.4초를 씁니다.
3. 장면 073(42666): 회의실 유리벽의 공간 이름과 TV 화면의 채널 로고 → 흐림 5
4. 장면 109: 41192(신문)는 흐림 6으로도 실제 정치 기사 제목이 읽혔습니다(첫 완성본의 전체 점검에서 발견). 144(휴대폰을 든 손 실루엣)로 바꿔 다시 렌더링했습니다.
5. 장면 058, 101(914): 모니터 상표 → 흐림 3
6. 장면 065(50753): 시계 밑 책 제목 → 아래쪽을 잘라 냄(crop)
7. 장면 077: 99904(카페 간판 로고, 칠판 글씨) → 4872(동료 둘이 웃으며 이야기)
8. 장면 067: 39789(휴대폰 뒷면 로고) → 31413
9. 장면 101: 50726(책 제목) → 914(사무실, "일터")
10. 장면 121(99910): 수첩 표지의 회사 로고가 나오지 않는 6.5초부터 씁니다.
11. 장면 057: 4779가 장면 033과 같은 화면이라 검은 화면 카드("개인의 질병으로")로 바꿨습니다.
12. 장면 029(10395): 타자기 오른쪽 끝의 제조사 로고 → 가장자리를 잘라 냄(crop)
13. 장면 129(50112): 앞부분에 상표가 찍힌 형광펜이 보여 4.3초부터 씁니다.
14. 마지막 장면들: 100831(3.9초)이 짧아 0.6배속으로 느려지던 것을 바꿨습니다. 100831은 7:44(0.9배속), 4397은 7:56, 1086은 8:03부터 끝까지입니다.

### 4-2. 2차 수정본 (2026-10-23, 장면 번호는 2차·3차 기준)

1. 새로 넣었거나 첫 완성본보다 길게 보이는 장면 26개(AI 사진 6장 포함)를 초당 2장씩(148장) 글자 인식기로 검사했고, 걸린 글자는 없었습니다.
2. 새로 보이는 부분(길어진 끝부분, 새 시작점)은 눈으로 다시 봤습니다. 장면 052(50133): 후드티 가슴의 영문 글자(Artisan)가 읽혀 아래쪽을 잘라 냈습니다(위 74%만 씀). 첫 완성본에도 있었는데 그때 점검에서 놓쳤습니다.
3. AI 사진: 프로이덴버거 이야기 안에서는 얼굴이 나오지 않게 했습니다(A07 뒷모습, A11 고개 숙임). A03(열정적인 사람)은 두 번 만들었으나 둘 다 얼굴이 나와 쓰지 않고 스톡 10395로 바꿨습니다. A12 종이 위의 글자 모양은 읽히지 않는 무늬입니다.
4. A16(인터뷰)은 실제 인물이 아닌 AI로 만든 얼굴이고, 흐리고 어둡게 깔았습니다. 기사 속 박 모 씨 본인의 모습이 아닙니다.

### 4-3. 3차 수정본 (2026-10-23)

1. 새로 보이는 스톡 화면이 없습니다(길어진 것은 전구 그림 화면뿐이고, 나머지 장면은 길이가 같고 시각만 늦춰짐).
2. 바꾼 문장 밖의 소리가 2차 수정본과 같은지 샘플 단위로 비교했습니다(차이 0).
3. 자막 시각: 바꾼 세 줄 말고는 2차 수정본 시각에 1.56초를 더한 것과 같습니다(307줄은 같고 6줄은 0.01초 차이, 음절 정렬의 20ms 틀 때문).

### 4-4. 4차 수정본 (2026-10-23)

1. 끝소리: 재녹음 다섯 개의 끝이 모두 배경 수준까지 잦아든 뒤 쉼으로 이어지는 것을 소리 크기로 확인했습니다.
2. 숨소리 판정: 처음 줄인 63곳 중 16곳을 스펙트로그램으로 봤고, 거의 모두 말소리였습니다(0-2의 3번). 남은 7곳과 2번 파일 1곳도 다음 단어의 시작이 걸려 있어 모두 끄기로 했습니다.
3. 시각: 다시 다듬은 전체 녹음은 445초 앞에서 예전과 1~2샘플(0.04ms) 차이입니다. 이어 붙이는 경계마다 옛 문장의 끝 울림 조각이 들어오지 않는지 확인했습니다.
4. 새로 보이는 스톡 화면(길이가 바뀐 장면 8개, 53장)을 글자 인식기로 검사했고 걸린 글자는 없었습니다. 끝부분과 새 시작점은 눈으로도 봤습니다.

### 4-5. 5차 수정본 (2026-10-23)

1. 새로 보이는 화면(장면 7개)을 글자 인식기로 검사했습니다. 새 영상 4개(4801, 42834, 31416, 31411)에서는 걸린 글자가 없었습니다. 신문 장면은 흐리기 전 그림에서 'Se suman…'의 일부가 읽혔고, 영상과 같은 흐림(12)을 준 그림에서는 확대 1.0~1.04배 모두 읽힌 글자가 없었습니다. 눈으로도 기사 제목, 신문 이름, 'EMPRESAS' 띠가 읽히지 않는 것을 확인했습니다.
2. 4801의 휴대폰 화면은 게임 화면처럼 보이지만, 화면에서 작고(약 60×100픽셀) 알아볼 수 있는 글자나 로고가 없습니다. 42834는 기타 머리(상표 자리)가 화면에 나오지 않습니다.
3. 소리: 이어 붙인 네 곳의 소리 크기를 10ms 단위로 봤습니다. 새 문장 끝은 배경 수준(-51dB, -44dB)까지 잦아든 뒤 실내 소리(-52dB)로 넘어가고, 중간에 소리가 빠지는 곳이 없습니다.
4. 바꾼 두 곳 밖의 소리는 4차와 샘플 단위로 같고, 자막 305줄은 4차와 같은 시각입니다(늦춰진 만큼만 다름).

---

## 5. 아직 임시이거나 결정이 필요한 것

1. 프로이덴버거 사진: 사용자가 저작권 허락을 받았다고 알려 준 사진을 4차에서 넣었습니다. 허락 범위가 영상이라 파일은 저장소에 두지 않습니다.
2. WHO 마크: 사용자 결정으로 4차에서 넣었습니다. WHO는 이름과 엠블럼 사용을 제한하고 있다는 점을 기록해 둡니다.
3. 추상적인 장면을 AI 사진으로 바꾸는 일: 사용자 지시로 미뤘습니다(2026-10-23).
4. 사례 구간(6:04~6:45, 31살 직장인 이야기)은 감자 캐릭터 대신 스톡 영상, 그림 화면, AI 사진으로 채웠습니다. 감자 캐릭터는 사용자와 함께 만든 뒤 바꿉니다(핸드오프 16장).
5. 배경음악은 Mixkit에서 골랐습니다. 사용자가 바꾸고 싶은 곡이 있으면 2장 방법으로 바꿉니다.
6. 끝 3초: 유튜브 최종 화면 요소는 영상의 마지막 5~20초에 넣을 수 있어, 넣으면 마지막 문장 위에 겹칩니다.

---

## 6. 유튜브 챕터 (설명란용)

chapters.txt에 있습니다. 시각은 각 단락 첫 자막 시각을 초 단위로 내림했습니다. 5차에서 사례 장 제목을 '31살 직장인의 이야기'로 바꿨고, 새 녹음이 원래보다 길어 마지막 두 챕터가 4차보다 1~2초 늦춰졌습니다.

---

## 7. 스톡 영상 (63개, Mixkit)

모두 영상 페이지의 copyrightNotice가 "Free"(Mixkit Stock Video Free License)인 것을 확인했습니다(2026-10-22, 5차에 더한 4801, 42834, 31416, 41192는 2026-10-23, 받아 둔 페이지 기준). 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다. 시각은 영상 안에서 장면이 시작하는 때입니다.

1. 31411 Sleeping boy moves in bed — https://mixkit.co/free-stock-video/sleeping-boy-moves-in-bed-31411/
   - 장면 001 0:00 (0.2초부터); 장면 113 6:21 (6.71초부터)
2. 28899 Woman turning off her alarm clock in the morning — https://mixkit.co/free-stock-video/woman-turning-off-her-alarm-clock-in-the-morning-28899/
   - 장면 002 0:02 (6.4초부터, 1.6배속); 장면 131 7:39 (1.0초부터)
3. 4548 Woman lying on a sofa — https://mixkit.co/free-stock-video/woman-lying-on-a-sofa-4548/
   - 장면 004 0:08 (2.0초부터); 장면 021 0:55 (9.0초부터); 장면 134 7:53 (14.0초부터)
4. 51394 Woman with insomnia lying in her bed trying to sleep — https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/
   - 장면 005 0:10 (8.0초부터)
5. 4701 Worried and sad man with his head down — https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/
   - 장면 006 0:12 (0.4초부터); 장면 038 1:39 (0.0초부터)
6. 4511 Sad girl looking out the window — https://mixkit.co/free-stock-video/sad-girl-looking-out-the-window-4511/
   - 장면 009 0:22 (0.0초부터); 장면 080 4:27 (1.95초부터)
7. 99909 Close up of a hand writing to do list on a yellow paper notebook — https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/
   - 장면 010 0:26 (0.5초부터); 장면 077 4:18 (6.0초부터)
8. 4333 View inside a wagon in motion — https://mixkit.co/free-stock-video/view-inside-a-wagon-in-motion-4333/
   - 장면 011 0:27 (5.0초부터)
9. 144 Hands shown texting on a smartphone — https://mixkit.co/free-stock-video/hands-shown-texting-on-a-smartphone-144/
   - 장면 012 0:28 (4.0초부터)
10. 1623 People getting into the subway train — https://mixkit.co/free-stock-video/people-getting-into-the-subway-train-1623/
   - 장면 013 0:29 (1.0초부터); 장면 105 5:57 (8.0초부터)
11. 4872 Two coworkers talking and laughing — https://mixkit.co/free-stock-video/two-coworkers-talking-and-laughing-4872/
   - 장면 014 0:32 (1.0초부터)
12. 3428 Street with people walking at dusk — https://mixkit.co/free-stock-video/street-with-people-walking-at-dusk-3428/
   - 장면 015 0:36 (1.0초부터)
13. 31413 Young man lying on his bed checking his smartphone — https://mixkit.co/free-stock-video/young-man-lying-on-his-bed-checking-his-smartphone-31413/
   - 장면 017 0:41 (0.0초부터); 장면 066 3:33 (8.0초부터)
14. 42653 Woman finishes working on her computer — https://mixkit.co/free-stock-video/woman-finishes-working-on-her-computer-42653/
   - 장면 018 0:49 (0.5초부터)
15. 100050 Woman smiling at her phone on a cozy couch — https://mixkit.co/free-stock-video/woman-smiling-at-her-phone-on-a-cozy-couch-100050/
   - 장면 019 0:50 (1.0초부터)
16. 50931 A young man slowly wakes up on a clean white bed — https://mixkit.co/free-stock-video/a-young-man-slowly-wakes-up-on-a-clean-white-50931/
   - 장면 020 0:53 (1.0초부터)
17. 42896 Young woman laying on a white soft bed slowly wakes up in the morning — https://mixkit.co/free-stock-video/young-woman-laying-on-a-white-soft-bed-slowly-wakes-42896/
   - 장면 022 0:57 (2.0초부터)
18. 4513 Worried and sad woman hugging a cushion — https://mixkit.co/free-stock-video/worried-and-sad-woman-hugging-a-cushion-4513/
   - 장면 024 1:00 (1.0초부터)
19. 10395 Close-up view of a typewriter while a man works on it — https://mixkit.co/free-stock-video/close-up-view-of-a-typewriter-while-a-man-works-on-10395/
   - 장면 031 1:19 (1.0초부터, 가장자리 잘라 냄)
20. 28886 Analog wall clock on a black background in a closed socket — https://mixkit.co/free-stock-video/analog-wall-clock-on-a-black-background-in-a-closed-28886/
   - 장면 032 1:22 (1.0초부터)
21. 4779 Doctor walking down a hospital hallway — https://mixkit.co/free-stock-video/doctor-walking-down-a-hospital-hallway-4779/
   - 장면 033 1:25 (1.0초부터)
22. 39841 Young man working in an office overtime — https://mixkit.co/free-stock-video/young-man-working-in-an-office-overtime-39841/
   - 장면 035 1:30 (1.0초부터); 장면 051 2:28 (4.89초부터); 장면 083 4:40 (4.0초부터)
23. 44579 Close view of a Christmas tree — https://mixkit.co/free-stock-video/close-view-of-a-christmas-tree-44579/
   - 장면 036 1:33 (1.0초부터)
24. 3461 Lighting candles in the dark — https://mixkit.co/free-stock-video/lighting-candles-in-the-dark-3461/
   - 장면 037 1:37 (1.0초부터); 장면 117 6:36 (6.0초부터)
25. 425 Moving needle on retro audio tape recorder — https://mixkit.co/free-stock-video/moving-needle-on-retro-audio-tape-recorder-425/
   - 장면 040 1:49 (1.0초부터); 장면 042 1:56 (8.0초부터)
26. 28893 Black analog clock in a very close shot — https://mixkit.co/free-stock-video/black-analog-clock-in-a-very-close-shot-28893/
   - 장면 041 1:53 (1.0초부터)
27. 1967 Smoke effect over black background — https://mixkit.co/free-stock-video/smoke-effect-over-black-background-1967/
   - 장면 043 1:59 (1.0초부터)
28. 4766 Clinic staff at a hospital reception — https://mixkit.co/free-stock-video/clinic-staff-at-a-hospital-reception-4766/
   - 장면 044 2:05 (6.5초부터, 흐림 16)
29. 4607 Bored young office workers in an office — https://mixkit.co/free-stock-video/bored-young-office-workers-in-an-office-4607/
   - 장면 045 2:08 (1.0초부터); 장면 073 4:03 (8.0초부터)
30. 8744 Young man upset and frustrated receiving a message — https://mixkit.co/free-stock-video/young-man-upset-and-frustrated-receiving-a-message-8744/
   - 장면 046 2:13 (1.0초부터)
31. 2707 A fireplace lit at Christmas time — https://mixkit.co/free-stock-video/a-fireplace-lit-at-christmas-time-2707/
   - 장면 047 2:16 (1.0초부터)
32. 21587 Stacked and piled books taken close up — https://mixkit.co/free-stock-video/stacked-and-piled-books-taken-close-up-21587/
   - 장면 048 2:19 (1.0초부터)
33. 50133 A young man wearing a hoodie studying at night in the library with a calculator — https://mixkit.co/free-stock-video/a-young-man-wearing-a-hoodie-studying-at-night-in-50133/
   - 장면 052 2:34 (1.0초부터, 가장자리 잘라 냄)
34. 914 Open office space — https://mixkit.co/free-stock-video/open-office-space-914/
   - 장면 057 2:57 (1.0초부터, 흐림 3); 장면 100 5:36 (10.0초부터, 흐림 3)
35. 4915 Hands of a person typing on a cell phone — https://mixkit.co/free-stock-video/hands-of-a-person-typing-on-a-cell-phone-4915/
   - 장면 058 3:03 (1.0초부터)
36. 50753 A young man turns off the alarm clock by the bedside — https://mixkit.co/free-stock-video/a-young-man-turns-off-the-alarm-clock-by-the-50753/
   - 장면 064 3:24 (1.0초부터, 가장자리 잘라 냄)
37. 50754 A young man slowly wakes up in bed — https://mixkit.co/free-stock-video/a-young-man-slowly-wakes-up-in-bed-50754/
   - 장면 065 3:29 (2.0초부터)
38. 26090 Table in a living room with fast food while a man watches television — https://mixkit.co/free-stock-video/table-in-a-living-room-with-fast-food-while-a-26090/
   - 장면 069 3:45 (1.0초부터)
39. 42666 Presentation during a work team meeting — https://mixkit.co/free-stock-video/presentation-during-a-work-team-meeting-42666/
   - 장면 072 3:59 (1.0초부터, 흐림 5)
40. 4908 Person working while scrolling on social networks — https://mixkit.co/free-stock-video/person-working-while-scrolling-on-social-networks-4908/
   - 장면 074 4:07 (1.0초부터)
41. 4720 Lonely boy on a park bench — https://mixkit.co/free-stock-video/lonely-boy-on-a-park-bench-4720/
   - 장면 075 4:10 (1.0초부터); 장면 114 6:23 (3.24초부터)
42. 31412 Boy puts his cell phone aside so he can go to sleep — https://mixkit.co/free-stock-video/boy-puts-his-cell-phone-aside-so-he-can-go-31412/
   - 장면 078 4:22 (1.0초부터)
43. 4893 Footsteps of a young man walking down the street — https://mixkit.co/free-stock-video/footsteps-of-a-young-man-walking-down-the-street-4893/
   - 장면 079 4:25 (1.0초부터)
44. 313 Colleagues reading a report together — https://mixkit.co/free-stock-video/colleagues-reading-a-report-together-313/
   - 장면 082 4:36 (1.0초부터)
45. 4500 Upset woman sitting on the floor — https://mixkit.co/free-stock-video/upset-woman-sitting-on-the-floor-4500/
   - 장면 085 4:45 (1.0초부터)
46. 99890 Close up a hand writing notes on a notebook with a pen — https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/
   - 장면 087 4:55 (1.0초부터)
47. 42655 A woman writing in her spiral notebook — https://mixkit.co/free-stock-video/a-woman-writing-in-her-spiral-notebook-42655/
   - 장면 088 4:58 (1.0초부터)
48. 1958 Virgin lonely beach with a palapa — https://mixkit.co/free-stock-video/virgin-lonely-beach-with-a-palapa-1958/
   - 장면 091 5:08 (1.0초부터)
49. 1013 Feet walking on the beach — https://mixkit.co/free-stock-video/feet-walking-on-the-beach-1013/
   - 장면 094 5:17 (1.0초부터)
50. 100252 Pouring Tea into a Cup on a Rustic Table Setting — https://mixkit.co/free-stock-video/pouring-tea-into-a-cup-on-a-rustic-table-setting-100252/
   - 장면 103 5:52 (1.0초부터)
51. 41192 POV flipping through a newspaper — https://mixkit.co/free-stock-video/pov-flipping-through-a-newspaper-41192/
   - 장면 108 6:07 (7.4초의 한 장면을 사진처럼 씀, 흐림 12, 1.0배에서 1.04배로 천천히 다가감)
52. 31415 Frustrated boy in his bed for not being able to sleep — https://mixkit.co/free-stock-video/frustrated-boy-in-his-bed-for-not-being-able-to-31415/
   - 장면 109 6:12 (1.0초부터)
53. 4801 Young man sitting scrolling on his cell phone — https://mixkit.co/free-stock-video/young-man-sitting-scrolling-on-his-cell-phone-4801/
   - 장면 110 6:15 (0.2초부터)
54. 42834 Hands of a guitarist changing chords — https://mixkit.co/free-stock-video/hands-of-a-guitarist-changing-chords-42834/
   - 장면 111 6:17 (4.8초부터)
55. 31416 Young man turns off the light to lie down to sleep — https://mixkit.co/free-stock-video/young-man-turns-off-the-light-to-lie-down-to-31416/
   - 장면 112 6:19 (4.4초부터)
56. 50956 Soft and traslucent smoke flows up on a dark background — https://mixkit.co/free-stock-video/soft-and-traslucent-smoke-flows-up-on-a-dark-background-50956/
   - 장면 118 6:41 (8.0초부터)
57. 99910 Beside a modern laptop the hands write a note on a yellow page notebook with a pen — https://mixkit.co/free-stock-video/beside-a-modern-laptop-the-hands-write-a-note-on-99910/
   - 장면 121 6:57 (6.5초부터)
58. 3977 View of a window with a curtain — https://mixkit.co/free-stock-video/view-of-a-window-with-a-curtain-3977/
   - 장면 125 7:10 (1.0초부터)
59. 50112 Student hand takes a stiky note to paste it on the notebook — https://mixkit.co/free-stock-video/student-hand-takes-a-stiky-note-to-paste-it-on-50112/
   - 장면 129 7:28 (4.3초부터)
60. 52452 Gliding along a quiet asphalt road at dawn, the soft, golden light of the rising sun iluminates the highway. — https://mixkit.co/free-stock-video/gliding-along-a-quiet-asphalt-road-at-dawn-the-soft-52452/
   - 장면 130 7:33 (1.0초부터)
61. 100831 Sky Transitioning from Night to Sunrise — https://mixkit.co/free-stock-video/sky-transitioning-from-night-to-sunrise-100831/
   - 장면 133 7:49 (0.0초부터, 0.9배속)
62. 4397 The silhouette of a woman at sunrise — https://mixkit.co/free-stock-video/the-silhouette-of-a-woman-at-sunrise-4397/
   - 장면 136 8:01 (0.5초부터)
63. 1086 Sunrise on the ocean — https://mixkit.co/free-stock-video/sunrise-on-the-ocean-1086/
   - 장면 137 8:08 (0.5초부터)

---

## 8. 사진 (AI 6장, 사용자 제공 1장; 스톡 영상의 한 장면은 7장 목록의 41192)

RealVisXL V5.0 Lightning(SG161222, openrail++ 라이선스, 상업 이용 가능), scripts/gen_batch.py. 공통 문구(STYLE, NEG)는 gen_batch.py에 있습니다.

1. A01 (images/A01_s1.png) — 장면 028 1:12, 심리학에서 이 말을 처음 쓴 사람은: 1970년대 상담실
   - 지시문: vintage 1970s psychotherapy office, empty leather therapy couch and armchair, notepad on a small side table, bookshelves, warm lamp light, vintage film photo
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
2. A02 (images/A02_s1.png) — 장면 030 1:17, 1970년대 뉴욕에서 일하던 그는: 1970년대 뉴욕 거리 (글자 '1970년대 / 뉴욕'은 render.py가 얹음)
   - 지시문: 1970s New York City street, yellow taxi cabs and old cars, brick buildings with fire escapes, pedestrians seen from behind, overcast daylight, vintage film photo
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
3. A07 (images/A07_s21.png) — 장면 039 1:42, 그는 그날 아침 침대에서 ... 앓아누웠습니다: 침대에 누운 사람, 뒷모습
   - 지시문: back view of a man lying motionless in bed facing away from the camera under a thick blanket, only the back of his head on the pillow, pale morning light through curtains, 1970s bedroom, vintage film photo
   - 씨앗 21, 1152x648, 5단계, CFG 1.0
4. A11 (images/A11_s1.png) — 장면 049 2:21, 열정을 다 태우고 ... '번아웃'이라고 불렀습니다: 벽에 기대 고개를 묻은 사람 (큰 글자 '번아웃'은 render.py)
   - 지시문: exhausted office worker sitting on the floor against a wall with his head down on his knees, dim empty office at night, scattered papers on the floor
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
5. A12 (images/A12_s1.png) — 장면 092 5:10, 휴가에 관한 연구들은: 연구 논문과 그래프
   - 지시문: stacks of research papers and scientific journals on a wooden desk, printed charts and bar graphs, reading glasses, soft daylight
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
6. A16 (images/A16_s1.png) — 장면 115 6:25, "열심히 살고 있는데도 ..." 인용 뒤 배경: 거리 인터뷰 (흐림 9, 어둡게)
   - 지시문: young korean man in office clothes being interviewed on a city street at dusk, a reporter holding a microphone toward him, side view
   - 씨앗 1, 1152x648, 5단계, CFG 1.0

사용자 제공: 프로이덴버거 사진(work/photos/freudenberger.png, 1240×620) — 장면 029 1:14, 사용자가 저작권자 허락을 받았다고 알려 줌(2026-10-23). 커밋하지 않음.
