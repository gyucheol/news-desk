# 핸드오프 — 「F의 연애」 썸네일

작성: 2026-10-22 (Claude Code에서 한 썸네일 작업을 정리)
갱신: 2026-10-26 (운영자 지시로 01편 주제 단어를 "불안"에서 "불안형"으로, 글자 크기를 262px에서 259px로, 카톡 메시지를 두 번 바꿈(마지막은 오후 7:11~7:26에 보낸 4개). 1장 6번, 2장 13~16번, 3-1, 3-2, 3-3, 6장, 7장, 부록 A·B)
이전 작업 도구: Claude Code. 문서 안의 'Claude'는 이전에 작업한 AI를 가리킵니다.

이 문서 사용법
- 새 대화창(Claude, Gemini 등)에 이 파일을 첨부하고, 예를 들어 이렇게 요청합니다.
  - "첨부한 썸네일 핸드오프대로 02편 썸네일을 만들어 줘. 주제 단어는 ○○, 핵심 장면은 ○○이야."
- 이 파일 하나에 확정된 틀, 수치, 결정 이력, 만드는 법, 스크립트 전문(부록)이 모두 들어 있습니다.
- 그림을 실제로 만들려면 파이썬(pillow, numpy)과 글꼴 파일이 있는 환경이 필요합니다(예: Claude Code 클라우드 세션). 실행 환경이 없는 채팅창에서는 문구와 장면 설계까지만 할 수 있습니다.
- 원본 파일: GitHub 저장소 gyucheol/news-desk의 ccr-af593d67-8pqav6 브랜치, F의연애/썸네일/ 폴더(thumb.py, thumb_chat.py, README.md, 편별 폴더). 기본(main) 브랜치에는 아직 합쳐지지 않았습니다.
- 채널 설정, 대본, 영상 제작은 별도 문서 HANDOFF_F의연애.md에 있습니다.

---

## 0. 이 문서를 받은 AI에게

1. 우선순위: 운영자의 최신 지시 > 이 문서 > 채널 핸드오프(HANDOFF_F의연애.md)
2. 답변 규칙: 정중한 존댓말 한국어, 결론부터, 마크다운 표 없이, 문서에는 굵은 글씨 없이 씁니다. 근거가 없으면 지어내지 않고 "모릅니다", "확인 필요"라고 씁니다. 추론은 추론이라고 밝힙니다.
3. 운영자는 휴대폰으로 봅니다. 답은 짧게 쓰고, 썸네일은 파일로 보내 바로 볼 수 있게 합니다.
4. 아래 2장의 결정은 다시 묻지 않습니다.
5. 시안을 확인할 때는 원래 크기와 함께 휴대폰 피드 크기(가로 약 360px)로 줄인 모습도 봅니다.
6. 시안은 2~3장을 보여 주고 추천안과 이유를 한 줄로 붙입니다. 운영자는 지금까지 시안을 보고 고르는 방식으로 결정했습니다.

---

## 1. 한눈에 보기 (확정된 틀)

1. 크기: 1280×720, JPG(롱폼 가로 썸네일)
2. 배경: 검은색
3. 위쪽 두 칸(화면 높이를 셋으로 나눈 위 두 칸): 영상 내용의 핵심이 되는 물체 하나. 작게 봐도 알아보도록 크게, 기울이지 않고 똑바로 둡니다.
4. 아래쪽 한 칸: 주제 단어 한 단어(2~3글자). 흰색, Noto Sans KR 굵기 800, 글자 높이는 화면 높이의 1/3(240px) 이상
5. 참고 채널(검은 배경 위 사물 사진 + 흰 굵은 제목, 예: "호감의 역설", "북극곰 효과")처럼 하되 너무 따라 하지 않습니다. 우리 채널은 비유적인 사물 대신 내용을 직접 보여 주는 물체를 씁니다(01편은 카톡 대화).
6. 01편 결과: 썸네일/01_불안형_답장/썸네일.jpg
   - 다크 테마 카톡 화면에 나만 보낸 말풍선 4개("머해?", "바빠??", "카톡 보기 어려워??", "뭐하는데..", 2026-10-26 바꿈), 모두 읽지 않은 '1', 메시지마다 보낸 시각
   - 아래에 흰 글씨 "불안형"(2026-10-26 "불안"에서 바꿈, 글자 크기 259px)

---

## 2. 운영자 결정과 피드백 이력 (2026-10-22~26, 다시 묻지 않음)

1. 첫 지시: 뒷배경은 검은색. VOX 느낌으로 내용의 핵심이 되는 물체를 가운데 두고, 밑에 영상 주제 단어를 크게(빨간색 또는 흰색) 씁니다.
   - 01편 예시로 든 물체: 불안해하는 사람의 스톡 사진, 불안을 상징하는 사진, 나만 카톡을 보내고 있는 스마트폰. 단어는 "불안"
2. 시안 A(휴대폰 + 흰 글씨), B(휴대폰 + 빨간 글씨), C(손 사진 + 빨간 글씨) 중 B를 골랐습니다.
3. 피드백: 글씨가 촌스럽다(첫 글꼴 Pretendard Black). 운영자가 보낸 참고 채널 썸네일 글씨처럼 깔끔하게 → 본고딕 계열 Noto Sans KR 800으로 바꿨습니다.
4. 지시: 참고 채널처럼 만들되 너무 따라 한 것처럼 보이지 않게
5. 지시: 롱폼 가로 썸네일 크기로, 뒤의 그림은 최대한 현실적인 사진풍으로
6. 지시: 휴대폰 몸체까지 나올 필요는 없다. 안의 대화 내용만 확대해서, 작게 봐도 눈에 확 들어오게
7. 피드백: 카톡 그림이 삐뚤다 → 원근 기울기를 빼고 똑바로 세웠습니다. 이후 '글씨가 든 그림은 기울이지 않는다'가 채널 규칙이 됐습니다.
8. 결정: 글씨는 흰색
9. 피드백: 카톡 글씨체가 AI 같다. 진짜 갤럭시 글씨체, 애플 글씨체로 만들어 고르게 해 달라.
   - 두 기본 글꼴은 기기 전용이라 쓸 수 없다고 알리고 실제 화면 캡처를 부탁했습니다.
   - 운영자가 갤럭시 카톡 캡처(기본 테마)를 보냈습니다. 그 화면에서 색과 비율을 재고, 가장 가까운 무료 글꼴(Noto Sans KR 450)로 다시 그렸습니다(5장).
   - 아이폰 캡처는 받지 않아 아이폰판은 만들지 않았습니다.
10. 결정: 라이트(카톡 기본 하늘색 화면 조각)와 다크 중 다크
11. 지시: "불안" 글씨를 더 크게 → 다음 지시로 '가로로 3등분했을 때 한 칸만큼' 이상
    - 화면을 가로줄로 세 칸으로 나눈 한 칸(240px)으로 해석했습니다. 01편 "불안"은 높이 242px, 너비 465px로, 너비도 화면 너비의 1/3(427px)보다 큽니다.
12. 지시: 메시지마다 보낸 시각을 다르게. "오늘 하루 어땠어요?" 오후 6:12, "바빠요? ㅎㅎ" 오후 8:43, "자요..?" 오후 11:50
13. (2026-10-26) 지시: "불안" 말고 "불안형"으로 → 글꼴·크기(262px)·위치는 그대로 두고 단어만 바꿨습니다. 세 글자도 높이 247px, 너비 688px로 화면 안에 들어갑니다(좌우 여백 약 290px).
14. (2026-10-26) 지시: 카톡을 "오늘 저녁에 뭐해 ?", "바빠?", "자?.."로 → 띄어쓰기와 문장부호까지 보낸 그대로 넣었습니다. 보낸 시각(오후 6:12, 8:43, 11:50)은 말이 없어 그대로 두었습니다. 그 전 메시지("오늘 하루 어땠어요?", "바빠요? ㅎㅎ", "자요..?")는 대본 v2에 맞춘 것이라, 운영자가 고쳐 쓴 최종 대본과 영상의 메시지와 달랐습니다.
15. (2026-10-26) 지시: "불안형 글씨가 너무 크다.. 3p만 줄이자" → '3p'를 글자 크기 3포인트로 보고 262px에서 259px로 줄였습니다(72ppi 기준으로 1포인트 = 1px). 약 1% 작아져 눈으로는 차이가 거의 없어서, 262·259·236(10% 줄임)·210(20% 줄임)을 나란히 놓은 비교 그림도 보냈습니다. 높이 240px 이상 기준은 256px까지 지켜집니다.
16. (2026-10-26) 지시: 카톡을 4개로. "7시 11분 : 머해?", "7시 16분 : 바빠??", "7시 22분 : 카톡 보기 어려워??", "7시 26분 : 뭐하는데.." → 문구는 보낸 그대로 넣고, 시각은 저녁으로 보고 '오후'를 붙였습니다(추론: 오전·오후가 적혀 있지 않음). 말풍선이 4개라 높이를 100px에서 80px로 줄였습니다(묶음 y=34~406, 글자와 53px).

---

## 3. 규격 수치

### 3-1. 화면 배치
1. 위 두 칸(y 0~480)에 물체, 아래 한 칸에 주제 단어를 둡니다.
2. 01편 실측: 말풍선 4개(높이 80px) 묶음 y=34~406, 주제 단어 "불안형"(259px) y=459~702(높이 244px, 너비 681px), 둘 사이 53px. 말풍선 3개(높이 100px)일 때 묶음은 y=34~377, 둘 사이 82px(262px 글자는 y=456~702, 높이 247px, 너비 688px). 이전 "불안"은 y=459~700(높이 242px, 너비 465px), 둘 사이 82px
3. 물체 아래쪽은 y=405~520에서 검게 사라지게 해 글자 뒤를 비웁니다.
4. 가장자리는 어두운 방처럼 검게 감쌉니다(가운데 밝고 가장자리 어두움). 아주 약한 노이즈만 넣습니다.

### 3-2. 주제 단어
1. 글꼴: Noto Sans KR 가변 글꼴, 굵기 800, 262px(틀의 기본값. 편마다 thumb_chat.py --size로 바꿀 수 있고, 01편 "불안형"은 259px), 가운데 정렬, 글자 바닥선 y=679
2. 글자 아래에 은은한 검은 그림자(아래로 6px, 흐림 14px)를 깝니다.
3. 색: 흰색(255, 255, 255)이 기본입니다. 빨간색(230, 40, 48)도 고를 수 있습니다.
4. 한 단어(2~3글자)를 권합니다. 단어가 길어 크기를 줄여야 하면, 높이 1/3 규칙과 부딪히므로 운영자에게 먼저 묻습니다.

### 3-3. 카톡 대화 물체 (thumb_chat.py)
1. 기준 화면: 운영자가 보낸 갤럭시 카톡 캡처. 친구 이름과 프로필 사진이 있어 원본은 저장하지 않았습니다.
2. 캡처에서 잰 색
   - 말풍선 (253, 229, 0)
   - 말풍선 글자 (24, 24, 24)
   - 기본 테마 배경 (171, 192, 209)
3. 다크 테마 색(01편 확정판): 화면 배경 (22, 22, 24), 시간 글자 (150, 152, 156). 다크 참고 화면이 없어 어림잡은 값입니다.
4. 말풍선 높이 h를 기준으로 한 비율(캡처 실측)
   - 모서리 둥글기 0.40h, 글자 높이 0.37h
   - 왼쪽 여백 0.32h, 오른쪽 여백 0.36h, 말풍선 사이 0.22h
5. 읽지 않은 '1': 노랑 (246, 222, 18), 굵기 700, 높이 0.28h, 말풍선 왼쪽 0.10h 떨어진 곳. 실제(0.22h)보다 조금 크게 그려 작은 썸네일에서도 보이게 했습니다.
6. 시간: 굵기 400, 높이 0.24h, 그 메시지의 '1' 바로 아래
7. 카톡 묶음 규칙(캡처에서 확인)
   - 같은 분에 보낸 메시지는 한 묶음입니다. 시간은 마지막 말풍선에만 붙습니다.
   - 분이 다르면 새 묶음입니다. 말풍선마다 꼬리가 새로 생기고 '1'과 시간이 위아래로 붙습니다.
   - 꼬리는 묶음의 첫 말풍선 오른쪽 위에 붙습니다.
8. 01편 배치: 말풍선 높이 80px(메시지 4개, 2026-10-26. 3개일 때는 100px), 위 끝 y=34. 시간까지 포함한 묶음 전체를 가로 가운데에 둡니다. 메시지가 늘면 묶음이 글자와 50px 이상 떨어지도록 thumb_chat.py --bubble로 줄입니다.
9. 글꼴: Noto Sans KR 굵기 450
10. 노란 말풍선 주변에만 약한 빛 번짐을 넣습니다(어두운 방의 화면 느낌).

---

## 4. 다음 편 물체 고르는 법

1. 영상의 핵심 장면을 직접 보여 주는 물체를 고릅니다. 작게 봐도 무엇인지 알아볼 수 있어야 합니다.
2. 글씨가 든 물체(채팅, 메모 등)는 기울이지 않습니다. 화면 끝에서 잘리는 글씨도 두지 않습니다(01편은 그래서 상대 이름 줄을 뺐습니다).
3. 재료별 원칙
   - 직접 그린 화면(카톡 등): 앱 로고와 상표는 넣지 않습니다. 실제 앱처럼 보이게 하려면 실제 캡처에서 비율을 잽니다.
   - 스톡 영상의 한 장면: Mixkit에서 영상 페이지의 라이선스가 Free인 것만 씁니다. 사람 얼굴에 '불안' 같은 감정 단어를 붙이지 않고 손, 뒷모습, 실루엣을 씁니다. Envato(Mixkit 운영사) 허용 사용 정책 원문은 접속이 막혀 읽지 못했습니다(확인 필요).
   - AI 이미지: 사물이나 공간 위주로 씁니다. 사진풍 AI 이미지를 쓰면 업로드할 때 '변경되거나 합성된 콘텐츠'를 '예'로 체크합니다.
   - 운영자가 준 캡처: 실명과 프로필 사진은 쓰지 않고, 원본은 저장소에 올리지 않습니다.
4. 참고 채널과 겹치지 않게 합니다. 비유적인 사물 사진에 흰 제목을 붙이는 조합을 그대로 따라 하지 않고, 우리 채널은 내용을 직접 보여 주는 물체(대화, 알림 등)를 씁니다.

---

## 5. 글꼴과 라이선스

1. Noto Sans KR(SIL Open Font License 1.1): 주제 단어와 카톡 글씨에 씁니다. 상업적 이용이 가능합니다.
   - 받는 곳: https://raw.githubusercontent.com/google/fonts/main/ofl/notosanskr/NotoSansKR%5Bwght%5D.ttf
   - NotoSansKR-VF.ttf라는 이름으로 글꼴 폴더에 저장합니다.
2. Pretendard(OFL): 초안 방식(thumb.py의 휴대폰 그림)에만 씁니다.
3. 쓰지 않는 글꼴: 아이폰 한글 기본 글꼴(Apple SD 산돌고딕 Neo)과 갤럭시 기본 글꼴(삼성 전용 서체)은 각 기기 안에서만 쓰도록 허락된 글꼴입니다. 인터넷에 도는 파일은 비공식 배포본이라 받지 않습니다.
4. 참고 채널 글꼴: 이미지만으로는 확정할 수 없었습니다. 글자 모양을 나란히 비교해 보니 본고딕(Source Han Sans, Noto Sans KR) 계열과 가장 비슷했습니다(유추 추론).
5. 카톡 글씨 글꼴 비교(갤럭시 캡처 글씨와 같은 높이로 맞췄을 때 너비 / 획 굵기 비율)
   - Noto Sans KR 450: 98.9% / 102.8% (선택)
   - SUIT 500: 98.2% / 97.0%
   - Gothic A1 500: 106.4% / 99.1%
   - Pretendard 400: 99.5% / 91.4%
   - 그 밖에 Noto 400·500, SUIT 400, Wanted Sans 400, Gothic A1 400, IBM Plex Sans KR 400, Nanum Gothic 400도 비교했습니다.

---

## 6. 만드는 법

1. 준비: python3, pillow, numpy. 글꼴 폴더에 NotoSansKR-VF.ttf를 둡니다. 위치는 FONT_DIR 환경 변수로 정하거나, 스크립트 옆 fonts/ 폴더를 씁니다.
2. 다크 카톡판(01편 방식)
   - `python3 thumb_chat.py out.jpg --word 불안형 --msgs "머해?|바빠??|카톡 보기 어려워??|뭐하는데.." --times "오후 7:11|오후 7:16|오후 7:22|오후 7:26" --size 259 --bubble 80`
   - `--theme light`: 카톡 기본 하늘색 화면 조각판
   - `--color red`: 빨간 글씨
   - `--time "오후 11:52"`: 마지막 메시지에만 시간
3. 점검
   - 1280×720인지
   - 주제 단어 높이가 240px 이상인지, 물체와 겹치지 않는지(간격 50px 이상 권장)
   - 가로 360px로 줄였을 때 물체와 단어가 보이는지
   - 잘린 글씨, 기울어진 글씨, 로고가 없는지
4. 저장: 썸네일/<편 번호_소재>/썸네일.jpg. 고르지 않은 시안은 같은 폴더의 초안/에 둡니다.

---

## 7. 01편 결과와 초안

1. 최종: 썸네일/01_불안형_답장/썸네일.jpg
   - 말풍선 4개(높이 80px): "머해?"(오후 7:11), "바빠??"(오후 7:16), "카톡 보기 어려워??"(오후 7:22), "뭐하는데.."(오후 7:26). 모두 읽지 않은 '1'(2026-10-26 바꿈)
   - 주제 단어: 흰색 "불안형"(2026-10-26 "불안"에서 바꿈), 글자 크기 259px(2026-10-26 262px에서 줄임)
2. 초안/에 남긴 것
   - A·B·C: 첫 시안(휴대폰 + 흰 글씨, 휴대폰 + 빨간 글씨, 손 사진 + 빨간 글씨), 글꼴 Pretendard Black
   - B2: 휴대폰 + 본고딕 글씨(빨간·흰)
   - 채팅 확대판: 빨간 글씨, 흰 글씨(이전 글꼴 Pretendard SemiBold)
   - 갤럭시 라이트: 카톡 기본 하늘색 화면 조각판
   - 썸네일_불안: 2026-10-22 확정본(주제 단어 "불안")
   - 썸네일_불안형_이전메시지: 2026-10-26 주제 단어만 "불안형"으로 바꾼 판(메시지는 이전 것)
   - 썸네일_불안형_글씨262: 2026-10-26 메시지 3개("오늘 저녁에 뭐해 ?", "바빠?", "자?..")에 글자 크기 262px인 판
   - 썸네일_불안형_메시지3개: 2026-10-26 같은 메시지 3개에 글자 크기 259px인 판

---

## 8. 하지 말 것 (운영자가 싫어한 것)

1. 너무 굵고 뭉툭한 제목 글씨(Pretendard Black): 촌스럽다고 했습니다.
2. 원근으로 기울인 물체: 삐뚤어 보인다고 했습니다.
3. 실제 앱보다 굵은 글씨와 과장된 비율: AI 같다고 했습니다.
4. 휴대폰 몸체를 크게 넣기: 굳이 필요 없고 내용이 작아집니다.
5. 화면 끝에서 잘린 글씨, 작은 장식 글씨(채널 작업 규칙)

---

## 9. 다음 편 썸네일 진행 순서

1. 운영자에게 주제 단어와 핵심 장면을 묻거나, 대본에서 후보를 2~3개 뽑아 제안합니다.
2. 시안 2~3장을 만들어, 작게 줄인 미리보기와 함께 보여 주고 추천안을 붙입니다.
3. 운영자가 고르면 썸네일.jpg로 확정하고, 썸네일/README.md와 진행 기록에 남깁니다.

---

## 10. 출처

1. Noto Sans KR 라이선스(SIL OFL 1.1): https://raw.githubusercontent.com/google/fonts/main/ofl/notosanskr/OFL.txt
2. Pretendard(SIL OFL 1.1): https://github.com/orioncactus/pretendard
3. Mixkit 라이선스: https://mixkit.co/license/ (영상 Free 라이선스 원문: https://mixkit.co/license/modal/videoFree/)
4. YouTube 고객센터, 변경되거나 합성된 콘텐츠 표시: https://support.google.com/youtube/answer/14328491
5. 참고 채널 썸네일과 갤럭시 카톡 화면: 운영자가 대화창에 보낸 캡처. 참고 채널 이름은 확인하지 않았고, 캡처 원본은 저장하지 않았습니다.

---

# 부록 A. thumb.py 전문 (공통 함수: 주제 단어, 검게 사라지는 처리, 초안 방식)

파일 위치: F의연애/썸네일/thumb.py

```python
# 「F의 연애」 썸네일 틀 (초안, 2026-10-22)
# 검은 배경 + 가운데 핵심 물체 하나(VOX 느낌) + 아래에 주제 단어를 크게(흰색 또는 빨간색). 1280x720.
#
# usage:
#   thumb.py phone OUT.jpg --word 불안 --color white|red [--msgs "메시지1|메시지2|메시지3"] [--name "그 사람"]
#       나만 보내고 답이 없는 채팅 화면의 휴대폰을 직접 그린다(앱 로고·상표 없음).
#   thumb.py photo OUT.jpg IMAGE --word 불안 --color red [--crop x0,y0,x1,y1] [--gamma 1.3]
#       사진(스톡 영상의 한 장면 등)을 가운데에 두고 가장자리를 검게 감싼다.
# env FONT_DIR: Pretendard-Bold/SemiBold.otf(OFL)와 NotoSansKR-VF.ttf(Noto Sans KR 가변 글꼴, OFL)가 있는 폴더
# 주제 단어 글꼴(2026-10-22 갱신): Noto Sans KR 800(ExtraBold). Pretendard Black은 사용자가 촌스럽다고 해서 바꿈.
import math, os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

W, H = 1280, 720
FONT_DIR = os.environ.get("FONT_DIR", os.path.join(os.path.dirname(os.path.abspath(__file__)), "fonts"))
COLORS = {"white": (255, 255, 255), "red": (230, 40, 48)}   # 맑은 빨강(채도 높고 분홍기 없음)
YEL = (242, 201, 76)                                       # #F2C94C, 채널 강조색
WORD_SIZE, WORD_BASE, WORD_WEIGHT = 262, 679, 800          # 주제 단어 크기, 글자 바닥선(y), 굵기
# 2026-10-22 사용자 요청: 글자 높이가 화면을 세 칸으로 나눈 한 칸(240px) 이상 → 262px("불안" 기준 높이 약 241px)


def font(weight, size):
    return ImageFont.truetype(f"{FONT_DIR}/Pretendard-{weight}.otf", size)


def vgrad(w, h, c0, c1):
    g = np.linspace(0, 1, h)[:, None, None]
    a = np.array(c0, np.float32) * (1 - g) + np.array(c1, np.float32) * g
    return Image.fromarray(np.repeat(a, w, axis=1).astype(np.uint8), "RGB")


def phone(msgs, name="그 사람", width=425, S=3):
    """Drawn phone (dark mode chat): only my yellow bubbles, each with the unread '1'. Returns RGBA, `width` px wide."""
    pw, ph, r = 340 * S, 700 * S, 56 * S
    body = Image.new("RGBA", (pw, ph), (0, 0, 0, 0))
    outer = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(outer).rounded_rectangle([0, 0, pw - 1, ph - 1], radius=r, fill=255)
    body.paste(vgrad(pw, ph, (112, 112, 118), (34, 34, 38)), (0, 0), outer)          # metal rim
    d = ImageDraw.Draw(body)
    b = 5 * S
    d.rounded_rectangle([b, b, pw - 1 - b, ph - 1 - b], radius=r - b, fill=(6, 6, 7, 255))  # black glass bezel
    sb = 15 * S
    sw, sh, sr = pw - 2 * sb, ph - 2 * sb, r - sb + 5 * S
    scr = Image.new("RGBA", (sw, sh), (22, 24, 30, 255))
    sd = ImageDraw.Draw(scr)
    # header: back chevron, round avatar, name
    hy = 84 * S
    sd.line([(30 * S, hy - 12 * S), (20 * S, hy), (30 * S, hy + 12 * S)], fill=(225, 225, 230), width=3 * S, joint="curve")
    sd.ellipse([46 * S, hy - 18 * S, 82 * S, hy + 18 * S], fill=(92, 98, 112))
    sd.text((94 * S, hy), name, font=font("SemiBold", 22 * S), fill=(235, 235, 240), anchor="lm")
    sd.line([(0, 118 * S), (sw, 118 * S)], fill=(44, 47, 56), width=S)
    # my bubbles on the right, with the unread "1" on their left
    fb, f1 = font("SemiBold", 23 * S), font("Bold", 25 * S)
    y = 140 * S
    for i, m in enumerate(msgs):
        tw = fb.getlength(m)
        bw, bh = tw + 32 * S, 50 * S
        x1 = sw - 18 * S
        x0 = x1 - bw
        sd.rounded_rectangle([x0, y, x1, y + bh], radius=17 * S, fill=YEL)
        if i == 0:   # tail on the first bubble of the run
            sd.polygon([(x1 - 22 * S, y), (x1 + 9 * S, y + 4 * S), (x1 - 2 * S, y + 20 * S)], fill=YEL)
        sd.text(((x0 + x1) / 2, y + bh / 2 + S), m, font=fb, fill=(30, 26, 18), anchor="mm")
        sd.text((x0 - 8 * S, y + bh - 3 * S), "1", font=f1, fill=YEL, anchor="rs")
        y += bh + 14 * S
    smask = Image.new("L", (sw, sh), 0)
    ImageDraw.Draw(smask).rounded_rectangle([0, 0, sw - 1, sh - 1], radius=sr, fill=255)
    body.paste(scr, (sb, sb), smask)
    d.rounded_rectangle([pw / 2 - 52 * S, sb + 14 * S, pw / 2 + 52 * S, sb + 46 * S], radius=16 * S, fill=(0, 0, 0, 255))
    # faint diagonal glass reflection, screen only
    refl = Image.new("L", (pw, ph), 0)
    ImageDraw.Draw(refl).polygon([(pw * 0.62, 0), (pw * 1.0, 0), (pw * 0.30, ph), (-pw * 0.08, ph)], fill=13)
    sm = Image.new("L", (pw, ph), 0)
    sm.paste(smask, (sb, sb))
    refl = Image.fromarray((np.asarray(refl, np.float32) * np.asarray(sm, np.float32) / 255).astype(np.uint8))
    body.alpha_composite(Image.merge("RGBA", (*Image.new("RGB", (pw, ph), (255, 255, 255)).split(), refl)))
    return body.resize((width, round(width * ph / pw)), Image.LANCZOS)


def bottom_fade(img, y0, y1):
    """Fade the picture to black from y0 to y1 so the word sits on black."""
    a = np.asarray(img, np.float32)
    g = np.clip((np.arange(H, dtype=np.float32) - y0) / (y1 - y0), 0, 1)
    g = g * g * (3 - 2 * g)
    a *= (1 - g)[:, None, None]
    return Image.fromarray(a.round().astype(np.uint8), "RGB")


def word_font(size=WORD_SIZE, weight=WORD_WEIGHT):
    f = ImageFont.truetype(f"{FONT_DIR}/NotoSansKR-VF.ttf", size)
    f.set_variation_by_axes([weight])
    return f


def put_word(img, word, color, size=WORD_SIZE):
    """Topic word: clean heavy gothic, centered, with a soft dark shadow underneath for depth.
    size: 글자 크기(px). 기본 262, 01편 '불안형'은 259(2026-10-26 사용자: "3p만 줄이자")."""
    f = word_font(size)
    sh = Image.new("L", (W, H), 0)
    ImageDraw.Draw(sh).text((W / 2, WORD_BASE + 6), word, font=f, fill=235, anchor="ms")
    sh = sh.filter(ImageFilter.GaussianBlur(14))
    img = Image.composite(Image.new("RGB", (W, H), (0, 0, 0)), img, sh)
    ImageDraw.Draw(img).text((W / 2, WORD_BASE), word, font=f, fill=COLORS.get(color, color), anchor="ms")
    return img


def make_phone(out, word, color, msgs, name):
    canvas = Image.new("RGB", (W, H), (0, 0, 0))
    ph = phone(msgs, name)
    x, y = (W - ph.width) // 2, 24
    glow = Image.new("L", (W, H), 0)   # light spill from the screen so the phone separates from black
    ImageDraw.Draw(glow).rounded_rectangle([x - 20, y + 30, x + ph.width + 20, y + 500], radius=120, fill=80)
    glow = glow.filter(ImageFilter.GaussianBlur(70))
    canvas = Image.composite(Image.new("RGB", (W, H), (38, 44, 58)), canvas, glow)
    canvas.paste(ph, (x, y), ph)
    canvas = bottom_fade(canvas, 450, 590)
    put_word(canvas, word, color).save(out, quality=92)


def make_photo(out, src, word, color, crop=None, gamma=1.3):
    im = Image.open(src).convert("RGB")
    if crop:
        im = im.crop(crop)
    im = im.resize((W, H), Image.LANCZOS)
    a = np.asarray(im, np.float32) / 255
    lum = a @ np.array([0.2126, 0.7152, 0.0722], np.float32)
    a = lum[..., None] + (a - lum[..., None]) * 0.85            # mute colors a little
    a = np.clip(a, 0, 1) ** gamma                               # darker mids
    yy, xx = np.mgrid[0:H, 0:W].astype(np.float32)
    rr = np.sqrt(((xx - W / 2) / (W * 0.46)) ** 2 + ((yy - H * 0.40) / (H * 0.52)) ** 2)
    v = np.clip(1 - (rr - 0.55) / 0.55, 0, 1)                   # strong vignette into black
    a *= (v * v * (3 - 2 * v))[..., None]
    canvas = Image.fromarray((np.clip(a, 0, 1) * 255).round().astype(np.uint8), "RGB")
    canvas = bottom_fade(canvas, 430, 580)
    put_word(canvas, word, color).save(out, quality=92)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    mode, out = a[0], a[1]
    word, color = opt("--word", "불안"), opt("--color", "white")
    if mode == "phone":
        msgs = opt("--msgs", "오늘 하루 어땠어요?|바빠요? ㅎㅎ|자요..?").split("|")
        make_phone(out, word, color, msgs, opt("--name", "그 사람"))
    else:
        crop = tuple(int(v) for v in opt("--crop", "").split(",")) if "--crop" in a else None
        make_photo(out, a[2], word, color, crop, float(opt("--gamma", "1.3")))
    print(out)
```

---

# 부록 B. thumb_chat.py 전문 (01편 확정 방식: 카톡 대화 확대판)

파일 위치: F의연애/썸네일/thumb_chat.py. thumb.py와 같은 폴더에 두고 실행합니다.

```python
# 「F의 연애」 썸네일: 채팅 확대판 (2026-10-22)
# 휴대폰 몸체 없이 카톡 대화 내용만 크게 보여 준다. 썸네일을 작게 봐도 노란 말풍선과 읽지 않은 '1'이 눈에 들어오게.
# 말풍선 모양·색·비율과 '1'·시간 위치는 사용자가 보내 준 갤럭시 카톡 화면에서 잰 값이다(2026-10-22).
# 갤럭시 기본 글꼴은 기기 전용이라 쓸 수 없어서, 같은 높이로 맞춰 비교했을 때 너비·굵기가 가장 가까운
# Noto Sans KR(OFL) 굵기 450을 쓴다(너비 98.9%, 획 굵기 102.8%).
# 말풍선은 기울이지 않고 똑바로 둔다. 아래에 주제 단어(thumb.py와 같은 글꼴·위치, 기본 흰색).
#
# usage: thumb_chat.py OUT.jpg [--theme dark|light] [--word 불안] [--color white|red]   (기본: dark, white)
#                              [--msgs "a|b|c"] [--times "오후 6:12|오후 8:43|오후 11:50"] [--size 262] [--bubble 100]
#   --size : 주제 단어 글자 크기(px, 기본 262). 01편 '불안형'은 259(2026-10-26 사용자: "3p만 줄이자").
#   --bubble: 말풍선 높이(px, 기본 100). 메시지가 4개면 묶음이 글자와 50px 이상 떨어지도록 80(2026-10-26 01편).
#   --times: 메시지마다 보낸 시각. 분이 다르면 카톡은 말풍선마다 꼬리를 새로 달고, 왼쪽에 '1'과 시간을 위아래로 둔다.
#   light: 카톡 기본 테마(하늘색 배경) 화면 조각을 검은 배경 위에 둔다
#   dark : 카톡 다크 테마처럼 검은 화면에 노란 말풍선만
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter, ImageFont

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from thumb import W, H, FONT_DIR, WORD_SIZE, bottom_fade, put_word   # noqa: E402

S = 2                                   # draw at 2x, then downsample
BUBBLE = (253, 229, 0)                  # measured on the Galaxy screenshot
TEXT = (24, 24, 24)
ONE = (246, 222, 18)
THEMES = {"light": dict(bg=(171, 192, 209), time=(84, 96, 106)),   # bg measured; time from the darkest time pixels
          "dark": dict(bg=(22, 22, 24), time=(150, 152, 156))}     # dark-mode values are approximate (no reference)
# proportions relative to the bubble height h (Galaxy screenshot: h = 105 px)
R_RADIUS, R_TEXT, R_PADL, R_PADR, R_GAP = 0.40, 0.37, 0.32, 0.36, 0.22
R_ONE = 0.28        # real '1' is about 0.22 h tall; a little larger so it still shows on a small thumbnail
R_TIME = 0.24


def noto(weight, px_height, sample="원하는거 올릴수있게변함"):
    """Noto Sans KR at the size whose glyph box for `sample` is px_height tall."""
    path = f"{FONT_DIR}/NotoSansKR-VF.ttf"
    size = max(8, round(px_height * 1.08))
    for _ in range(6):
        f = ImageFont.truetype(path, size)
        f.set_variation_by_axes([weight])
        bb = f.getbbox(sample)
        size = max(8, round(size * px_height / max(1, bb[3] - bb[1])))
    f = ImageFont.truetype(path, size)
    f.set_variation_by_axes([weight])
    return f


def draw_chat(d, msgs, right, top, h, theme, times):
    """My messages, Galaxy KakaoTalk style: yellow pill bubbles right-aligned at x=right, '1' on the left of each.
    times: one entry per message (None = no time shown). A message with a time closes its minute group, so the next
    bubble starts a new group and gets the tail again, as on the real screen. Returns the bounding box drawn."""
    ft, f1, fm = noto(450, R_TEXT * h), noto(700, R_ONE * h, "1"), noto(400, R_TIME * h, "오후 11:52")
    y, box = top, [right, top, right, top]
    new_group = True
    for i, m in enumerate(msgs):
        time = times[i] if i < len(times) else None
        bb = ft.getbbox(m)
        bw = (bb[2] - bb[0]) + (R_PADL + R_PADR) * h
        x1, x0 = right, right - bw
        d.rounded_rectangle([x0, y, x1, y + h], radius=R_RADIUS * h, fill=BUBBLE)
        if new_group:   # tail on the first bubble of each group (top right)
            d.polygon([(x1 - 0.30 * h, y), (x1 + 0.13 * h, y + 0.02 * h), (x1 - 0.02 * h, y + 0.26 * h)], fill=BUBBLE)
        d.text((x0 + R_PADL * h - bb[0], y + h / 2), m, font=ft, fill=TEXT, anchor="lm")
        one_bottom = y + h - (0.46 if time else 0.12) * h
        d.text((x0 - 0.10 * h, one_bottom), "1", font=f1, fill=ONE, anchor="rs")
        if time:
            d.text((x0 - 0.10 * h, y + h - 0.10 * h), time, font=fm, fill=THEMES[theme]["time"], anchor="rs")
            box[0] = min(box[0], x0 - 0.10 * h - fm.getlength(time))
        box[0] = min(box[0], x0 - 0.10 * h - f1.getlength("1"))
        new_group = bool(time)
        y += h + R_GAP * h
    box[3] = y - R_GAP * h
    return box


def make_light(msgs, times, h=100):
    """A crop of the default-theme chat screen (light blue) floating on black, softly lit."""
    CW, CH = W * S, H * S
    hh = h * S
    # measure the chat block first, then size the screen crop around it
    probe = Image.new("RGB", (CW, CH)); bx = draw_chat(ImageDraw.Draw(probe), msgs, CW, 0, hh, "light", times)
    bw, bh = CW - bx[0], bx[3] - bx[1]
    pad_l, pad_r, pad_v = 70 * S, 34 * S, 40 * S
    cw, ch = round(bw + pad_l + pad_r), round(bh + 2 * pad_v)
    cx0, cy0 = (CW - cw) // 2, 24 * S                 # crop ends well above the title
    card = Image.new("RGB", (cw, ch), THEMES["light"]["bg"])
    draw_chat(ImageDraw.Draw(card), msgs, cw - pad_r, pad_v, hh, "light", times)
    img = Image.new("RGB", (CW, CH), (0, 0, 0))
    glow = Image.new("L", (CW, CH), 0)          # screen light spilling into the dark around the crop
    ImageDraw.Draw(glow).rounded_rectangle([cx0 - 20 * S, cy0 - 10 * S, cx0 + cw + 20 * S, cy0 + ch + 30 * S], radius=60 * S, fill=110)
    glow = glow.filter(ImageFilter.GaussianBlur(60 * S))
    img = Image.composite(Image.new("RGB", (CW, CH), (60, 72, 84)), img, glow)
    m = Image.new("L", (cw, ch), 0)
    ImageDraw.Draw(m).rounded_rectangle([0, 0, cw - 1, ch - 1], radius=26 * S, fill=255)
    img.paste(card, (cx0, cy0), m)
    return finish(img)


def make_dark(msgs, times, h=100):
    """Dark-theme chat: black screen, only my yellow bubbles, a soft glow like a lit screen in a dark room."""
    CW, CH = W * S, H * S
    hh = h * S
    probe = Image.new("RGB", (CW, CH)); bx = draw_chat(ImageDraw.Draw(probe), msgs, CW, 0, hh, "dark", times)
    bw = CW - bx[0]
    right = (CW + bw) / 2
    img = Image.new("RGB", (CW, CH), THEMES["dark"]["bg"])
    draw_chat(ImageDraw.Draw(img), msgs, right, 34 * S, hh, "dark", times)
    a = np.asarray(img, np.float32)
    lum = a.mean(2)
    bright = Image.fromarray(np.clip((lum - 120) * 2, 0, 255).astype(np.uint8)).filter(ImageFilter.GaussianBlur(26 * S))
    a += (np.asarray(bright, np.float32) / 255)[..., None] * np.array([60, 50, 12], np.float32)
    return finish(Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)))


def finish(img):
    """Edges fall off to black (dark room), faint noise, downsample to 1280x720."""
    CW, CH = img.size
    a = np.asarray(img, np.float32)
    yy, xx = np.mgrid[0:CH, 0:CW].astype(np.float32)
    r = np.sqrt(((xx - 0.50 * CW) / (0.64 * CW)) ** 2 + ((yy - 0.38 * CH) / (0.64 * CH)) ** 2)
    v = np.clip(1 - (r - 0.62) / 0.45, 0, 1)
    a *= (v * v * (3 - 2 * v))[..., None]
    a += np.random.default_rng(3).normal(0, 1.2, a.shape)
    return Image.fromarray(np.clip(a, 0, 255).astype(np.uint8)).resize((W, H), Image.LANCZOS)


if __name__ == "__main__":
    a = sys.argv[1:]
    opt = lambda k, dflt: a[a.index(k) + 1] if k in a else dflt
    msgs = opt("--msgs", "오늘 하루 어땠어요?|바빠요? ㅎㅎ|자요..?").split("|")
    if "--times" in a:
        times = [t.strip() or None for t in opt("--times", "").split("|")]
    elif "--time" in a:                      # one time under the last message only
        times = [None] * (len(msgs) - 1) + [opt("--time", "")]
    else:                                    # 01편: 저녁 6:12, 8:43, 밤 11:50에 하나씩 보냄(2026-10-22 사용자 지정)
        times = ["오후 6:12", "오후 8:43", "오후 11:50"]
    img = (make_light if opt("--theme", "dark") == "light" else make_dark)(msgs, times, int(opt("--bubble", 100)))   # 기본 다크(2026-10-22 사용자 결정)
    img = bottom_fade(img, 405, 520)
    put_word(img, opt("--word", "불안"), opt("--color", "white"), int(opt("--size", WORD_SIZE))).save(a[0], quality=93)
    print(a[0])
```

