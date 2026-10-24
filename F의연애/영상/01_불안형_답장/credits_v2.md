# 01편 「불안형 답장」 v2 기록

작성 2026-10-24. 결과 파일: 01_불안형_답장_v2.mp4 (점검 결과는 11장). 운영자 목소리와 운영자가 보낸 사진이 들어 있어 영상, 녹음, 사진은 저장소에 커밋하지 않았습니다(SendUserFile로 전달). v1 기록은 credits.md입니다.

사용자 요청: v1 영상을 보고 보낸 [변경 필요 내용] 목록(녹음 음질, 쉼 줄이기, 자막 시각, 배경음악, 그리고 1~57번 항목)과 존 볼비·댄 애리얼리 사진 두 장, 작업 중에 더한 한 가지("이건 실험 전에 미리 작동 테스트를 끝낸, 꽤나 따끔한 전기가 흐르는 장치죠."도 가운데 자막으로). 아래 괄호 안 번호는 그 목록의 번호입니다.

---

## 1. 한눈에

1. 녹음: 원인을 분석해 우리 쪽에서 생긴 문제 4가지를 없앴고(2장), 녹음 파일 자체에 들어 있는 것 3가지는 원본이 있어야 없앨 수 있어 다음 녹음 방법을 제안합니다.
2. 문장 사이 쉼 109곳을 줄였습니다(합계 11.6초, 12분 3.6초 → 11분 50.6초, 3장).
3. 자막 시각을 음절 단위로 다시 맞췄습니다(4장).
4. 자막 504줄: 쉼표를 모두 빼고, 가운데 글씨의 따옴표를 빼고, 가운데 자막은 모두 끊어서 같은 자리에서 차례로 바꿉니다(5장).
5. 장면 188개: 스톡 교체 12곳(클립 16개), 흐린 배경 위 가운데 글씨 8곳, 운영자 사진 2장, AI 그림 1장, 카톡 등장 효과와 노란 빛 제거(6장).
6. 배경음악 9곡을 박자가 있는 곡으로 바꾸고, 시계 효과음을 뺐습니다(7장).
7. 아이콘 화면의 글꼴을 바꿨습니다(8장).

## 2. 녹음 음질 (요청 1)

결론: v1에서 음질이 한 번씩 나빠지는 원인은 우리 쪽 처리와 녹음 파일 자체, 두 군데에 있었습니다. 우리 쪽 원인은 모두 고쳤습니다. 녹음 파일에 이미 들어 있는 것은 그 파일로는 되돌릴 수 없어, 다음 녹음부터 원본을 받는 방법을 제안합니다. Claude는 소리를 들을 수 없어 아래는 모두 측정값으로 찾은 것입니다. 들으실 때 여전히 나빠지는 곳이 있으면 영상의 분:초를 알려 주세요.

1. 우리 쪽에서 생긴 것 (고침)
   - 영상 소리 압축: v1은 AAC 192kbps로 넣었습니다. 목소리의 4~15kHz 대역에서 압축 오차가 신호보다 중앙값 21.2dB 낮았고, 오차가 신호의 1/4(-6dB)을 넘는 0.02초 구간이 48곳 있었습니다. 320kbps로 올리면 오차가 31.8dB 낮아지고 그런 구간은 2곳만 남습니다. v2는 320kbps입니다(render_parallel.py).
   - 배경음악 크기: v1은 곡마다 dynaudnorm(0.5초마다 크기를 자동으로 맞추는 처리)을 썼습니다. 이 처리는 말이 쉬는 사이마다 음악을 키우고 말할 때 줄여서, 소리 전체가 출렁이는 것처럼 들릴 수 있습니다. v2는 곡마다 고정된 크기 하나만 줍니다(bgm_sequence.py --constant). 3초 단위 음악 크기는 구간마다 ±2dB 안에서 고릅니다.
   - 7:09의 딸깍 소리: 음성2 파일이 편집으로 자른 자리(18.6밀리초)에서 바로 시작해, 붙인 곳에서 딸깍 소리가 났습니다. 잘린 조각을 지우고 15밀리초 동안 서서히 키웠습니다. 음성1의 시작(12.1밀리초)도 같게 처리했습니다.
   - 녹음 안의 딸깍 소리 2곳: v1 3:47(227.22초)과 5:55(355.00초)에 한 표본짜리 튐이 있었습니다. 그 앞뒤 1.6밀리초를 양쪽 30밀리초 소리로 예측해 메웠습니다(edit_narration_v2.py).
   - 확인한 것: 마지막 리미터(최고점 -1.5dBFS)가 줄인 크기는 최대 0.33dB이고 0.5dB 넘게 줄인 순간은 없습니다. 섞기 전후 어디에서도 소리가 잘리지(클리핑) 않았습니다.
2. 녹음 파일 자체에 들어 있는 것 (이 파일로는 되돌릴 수 없음)
   - 손실 압축을 여러 번 거침: 받은 파일은 AAC 256kbps m4a(ffmpeg Lavf60으로 저장)이고, 15.5kHz 위가 이미 잘려 있습니다. 그 전에 한 번 더 손실 압축을 거친 흔적입니다(추론: 256kbps AAC만으로는 보통 이 위치에서 잘리지 않음). 압축으로 잃은 소리는 되살릴 수 없습니다.
   - 1.1배속: 녹음 단계에서 빠르게 한 파일입니다. 속도를 바꾸는 처리는 음절에 따라 금속성 울림을 만들 수 있고, 그 정도가 문장마다 다릅니다(일반적인 성질에서 유추, 이 파일의 원본이 없어 직접 비교하지는 못함).
   - 잡음 게이트: 말이 없는 곳은 -70dB 가까이 잘려 있고, 그 사이에 100Hz 웅 소리가 10~15% 깊이로 오르내립니다. 게이트는 말끝을 함께 깎을 수 있습니다.
   - 문장별 말소리 품질 점수(DNSMOS P.835, Microsoft, CC BY 4.0, 1~5점)는 영상 전체에서 고르게 중앙값 3.44였습니다. 특정 시간대에 몰려 나빠지는 곳은 없었고, 가장 낮은 문장은 두 번 나오는 "알려드리겠습니다."(2.15, 2.46)였습니다. 소리 압축(AAC)은 이 점수를 바꾸지 않았습니다.
3. 다음 녹음 제안: 녹음 앱에서 나온 원본(가능하면 WAV, 아니면 가장 높은 음질의 m4a)을 1.0배속 그대로, 잡음 제거·게이트 없이 보내 주세요. 속도 조절과 필요한 처리는 영상 만들 때 한 번에 하겠습니다. 이번처럼 이미 편집한 파일이 편하시면 그대로 쓰겠습니다.

## 3. 문장 사이 쉼 (요청 0)

"녹음 문장과 문장 사이의 빈 시간이 있다면 줄이되, 최대한 자연스럽게 줄여줘"

1. 소리 없는 구간(0.01초 단위로 말소리보다 38dB 이상 작은 곳, 녹음의 게이트 수준)의 가운데만 잘라 냈습니다. 말 뒤 0.06초와 다음 말 앞 0.05초, 숨소리는 그대로 두고, 자른 자리는 소리 없는 곳 안에서 0.015초 동안 겹쳐 이었습니다.
2. 남기는 쉼: 문장과 문장 사이 0.22초(83곳, 중앙값 0.31 → 0.22초), 새 구간이 시작하는 곳 0.38초(3곳), 쉼표 자리나 한 줄 안 0.16초(23곳). 이보다 짧은 쉼은 건드리지 않았습니다.
3. 합계 11.6초가 줄어 723.6초 → 710.6초가 되었습니다. 마지막 말 뒤 3초에 끝나는 것은 같습니다. 바뀐 곳 전부는 edit_log_v2.json에 있습니다.

## 4. 자막 시각 (요청 4)

"녹음본의 목소리가 해당 자막을 읽을 때 자막이 같이 딱 나올 수 있게"

1. v1에서 어긋난 이유(스펙트로그램으로 확인): 쉼 뒤에 소리가 커지는 곳을 시작으로 잡았는데, 그 쉼이 앞 줄 안에 있으면 0.3초 일찍("불안해라고"의 '라고' 중에 다음 자막), 줄 안의 쉼이면 0.5초 늦게 나왔습니다.
2. v2: 자막 첫 음절의 위치를 음절 정렬 모델(kresnik/wav2vec2-large-xlsr-korean, Apache-2.0)로 먼저 찾고, 실제 소리로 미세 조정합니다(scripts/onsets_v2.py).
   - 그 음절 바로 앞(0.06~0.15초 안, 첫 자음에 따라 다름)에 쉼이 끝나면 소리가 다시 시작하는 곳(358줄)
   - ㅅ·ㅈ·ㅊ처럼 바람 소리로 시작하는 음절은 그 소리가 시작하는 곳(12줄. 모델은 모음에 표시해 0.05~0.12초 늦었음: 슬슬, 심리학, 스스로, 생각해, 사람들)
   - 이어서 말하는 곳은 첫 자음의 작은 골짜기가 끝나는 곳(131줄)
   - 그 밖에는 모델 위치에서 이 녹음에서 잰 차이(0.012초)만큼 앞(3줄)
   - 쉼 끝에서 0.15초 넘게 떨어진 소리(숨소리)는 시작으로 보지 않습니다. 첫 판에서 "이미", "이런", "알림"이 숨소리 시작에 걸려 0.12~0.15초 일찍 나와 고쳤습니다.
3. 화면은 1초에 30장이라, 자막이 첫 소리에 가장 가까운 장에서 나오도록 0.017초(반 장) 당겼습니다. 장면 전환과 가운데 글씨도 같은 시각에 바뀝니다.
4. 확인: 30줄 넘게 스펙트로그램과 소리 크기 곡선 위에 표시해 눈으로 봤습니다. 자막 시작은 모델이 찾은 첫 음절 위치보다 중앙값 0.020초 앞이고, 90%가 0.068초 앞~0.010초 뒤입니다(첫 자음 소리가 모음보다 먼저 나므로 앞이 맞음).

## 5. 자막 문구 (subtitles_v2.txt, 504줄)

1. 모든 자막에서 쉼표를 뺐습니다(17).
2. 가운데 자막(108줄)
   - 한 문장을 통째로 쓰지 않고 아래 자막처럼 끊어서, 말하는 때에 맞춰 같은 자리에서 차례로 바꿉니다(33, 15, 24, 25, 31, 40, 52 등 표시한 곳 포함).
   - 가운데 글씨의 따옴표(' ")를 모두 뺐습니다(8, 12. 큰따옴표도 같은 이유로 뺌).
   - 가운데로 바꾼 곳: 35, 36, 38, 39, 42, 44, 51, 57, 추가 1곳(이건 실험 전에…)
   - '어제 내 농담이 별로였나?'는 아래 자막으로(32)
3. 문구
   - "헉 미안해..ㅜ회식 와서 연락을 이제 봤네"(1, 말풍선. 소리는 녹음 그대로 "받네")
   - "여러분은 어떤 상황에 / 가장 마음이 쓰이셨나요?"('자'는 뺌, 3)
   - "대수롭지 않게 넘깁니다.", "온갖 부정적인 상상을 펼칩니다.", "자신을 탓합니다."(9, 13, 14)
   - "심리학은 아니라고 대답합니다."(16), "내가 연락을 너무 재촉하는 것처럼 / 보이면 어떡하지."('아'는 뺌, 21)
   - 같은 이유로 Claude가 더 뺀 곳 2곳: "자기 자신을 탓한 학생이"('하며'), "최악의 시나리오를"('하는'). 둘 다 가운데 혼잣말 바로 뒤에 오는 연결말입니다(9장).
4. 자막에서 뺀 말('자', '하며' 등)은 녹음에는 그대로 있어, 자막은 그 말이 끝난 뒤 다음 낱말에서 나옵니다.

## 6. 장면 (build_spec_v2.py, 188개: 스톡 101, 아이콘 42, 검은 카드 32, 사진 13)

1. 카톡 화면(1, 2, 20, 22): 말풍선이 튀어나오는 효과와 숫자 1 뒤의 노란 빛을 모두 뺐습니다. 말풍선은 그 줄을 말하는 순간 그냥 나타납니다.
2. 첫 번째·두 번째·세 번째 글씨: 흰색, 더 크게(2). 같은 이유로 "1 / 3" 같은 항목 표시도 흰색으로 키웠습니다.
3. 세 상황 비교 화면(6, 7): 세 칸에 실제 카톡 내용(내 메시지와 답장)을 넣고, 세 번째 칸 밑 "3시간째 1"을 지웠습니다.
4. 스톡 교체
   - 5분마다 습관처럼(11): 휴대폰을 쥐고 보며 기다리는 여자(25583)
   - 7시가 훌쩍 넘었는데도(19): 바늘이 7시 55분을 지나 돌아가는 시계(39826, 빠르게 찍은 영상). 7시를 막 넘어가는 무료 영상은 찾지 못했습니다.
   - 불확실성(26): v1의 51399는 파일 자체에 뒤척이는 장면이 빠르게 감긴 구간(3.5~6.0초, 11.5~15.5초)이 있었습니다. 같은 배우가 어둠 속에 누워 천장을 보는 보통 속도 영상(51390)으로 바꿨습니다. 51399를 쓰는 다른 두 장면도 빠른 구간을 피했습니다(0초부터, 7.8초부터).
   - 비록 카톡을 주고받는 실험은 아니었지만(27): 밤에 소파에 누워 휴대폰만 보는 여자(43381, 그림 대신)
   - 게다가 이렇게 … 빈칸을 채우기 시작합니다(28): 생각에 잠긴 여자 → 누워서 걱정하는 얼굴(51389, 51390)
   - 곧 편하게 이야기를 나누는(30): 웃으며 문자를 보내는 여자(51121)
   - 결국 불 꺼진 방에서(37): 어두운 방 바닥에 무릎을 안고 앉은 여자(25586)
   - 자 그렇다면 … 다독여야 할까요?(41): 밤에 침대에서 휴대폰을 보는 남자 → 눈을 감고 숨을 고르는 여자(31413, 42904)
   - 키르칸스키 연구팀(43): 겁에 질려 입을 막은 얼굴, 벽에 손 그림자가 기어감(43846). AI 거미 그림과 옆 글씨는 뺐습니다.
   - 소리 내어 읽게 했습니다(45): 종이를 들고 대사를 읽는 배우(43396)
   - 일주일 뒤 … 어디였을까요?(49): 저녁에서 밤으로 바뀌는 도시(3132) → 창밖을 보는 여자(8736). 달력 무료 영상은 글자가 보이거나 제한 라이선스라 쓰지 않았습니다.
   - 스스로를 달랜 그룹도, 딴생각을 한 그룹도 아닌(50): 숨을 고르는 여자 → 소파에서 멍하니 간식을 먹는 남자(42904, 26090)
5. 흐리고 조금 어둡게 깐 배경 위 가운데 글씨
   - 운동은 얼마나 자주 해요?(29): 러닝머신을 달리는 사람들(100530)
   - 그 정적 같은 8분이 흐른 뒤(31): 휴대폰을 보다 이마를 짚는 남자(8757)
   - 첫 번째·두 번째·세 번째 그룹(46~48): 감정을 담아 말하는 여자(43404), 눈을 감고 명상하는 여자(42903), 거실 소파와 TV(3110). 가운데에 "자기 감정에 솔직하게 이름 붙이기", "스스로 달래기", "아예 딴생각하기"와 각 그룹이 읽은 말
   - 만약 30분이 지나도 …(55): 바로 앞 "예를 들어, 이렇게 정해 두는 겁니다."의 영상(42655, 공책에 적는 손)이 끊기지 않고 이어집니다(fit_clips.py의 cont. 클립이 짧아 이어지는 부분만 0.94배속).
   - 아무리 불러도 엄마가 오지 않자 …(35): 바로 앞의 빈 병동 사진이 흐려지며 이어집니다.
   - 여러분들만의 … 댓글로 공유해 주세요.(57): v1의 영상 두 개를 흐리게
6. 검은 화면 가운데 글씨: 경보기 그림을 뺀 곳(36, 38), AI 그림을 뺀 곳(42), 아이콘을 뺀 곳(39, 44, 51), 전극 문장(추가), 배경을 지운 곳(56)
7. 운영자 사진(34, 53): 화면 가운데에 크게 두고, 같은 사진을 흐리고 어둡게 깔아 빈 곳을 채웠습니다. 보내 주신 사진이 작아서(646×475, 560×373) 화면 전체로 늘리면 3배 확대되어 흐려지기 때문입니다(make_photos_v2.py).
8. AI 그림(18): "원래 인간의 뇌는 '알 수 없는 상태'를 … 위협적으로 받아들이도록 설계되어 있거든요"에 짙은 안개 앞에 홀로 선 뒷모습(C02, 얼굴 없음). 후보 3장 중 골랐습니다(C01 휴대폰의 큰 그림자, C03 침대에 앉은 뒷모습은 쓰지 않음).
9. 세 가지 현실적인 방법을 알려드리겠습니다(23): 앞의 책 읽는 영상이 그대로 이어지고, AI 그림(숫자 3)은 뺐습니다.

## 7. 소리: 배경음악과 효과음

1. 배경음악(5): "살짝 텐션감이 있는 브금"으로 9곡을 모두 바꿨습니다. 드럼·베이스 박자가 있는 Mixkit 무료 곡이고, 이야기 구간마다 곡을 바꿉니다(3초 겹침, -36 LUFS). 곡과 고른 근거는 15장, 측정값은 bgm_plan_v2.json. v1 곡들은 드럼이 거의 없었습니다(타악 비율 0.02~0.04 → v2 중앙값 0.23).
2. 효과음
   - 시계 초침 소리 2곳을 모두 뺐습니다(10).
   - 메모 입력 소리를 뺐습니다. 함께 쓰던 메모 화면이 가운데 자막으로 바뀌었기 때문입니다(52).
   - 남긴 것: 메시지 보냄 4곳, 받음 2곳, 전기 1곳(16장).

## 8. 아이콘 화면 글꼴 (54)

"자료도 그렇게 글씨체가 너무 ai같은데, 좀 보완할 방법 없나?"

1. 원인(추론): 아이콘 화면 글씨를 자막과 같은 Pretendard로 써서, 그림과 자막이 모두 같은 매끈한 글꼴이라 기계가 만든 느낌이 강했습니다.
2. 바꾼 것: 아이콘 화면의 글씨를 G마켓 산스(굵은 기하학 글꼴, 지마켓 배포)로 바꿨습니다. 무료 글꼴 세 개를 같은 화면에 놓고 비교해 골랐습니다. 글꼴 파일에 들어 있는 라이선스는 SIL Open Font License 1.1이고, 요약에 "상업적 목적의 사용(인쇄물, 광고물, 온라인, 영상 포함)" 가능으로 적혀 있습니다(2026-10-24 확인). 카톡 말풍선 안 글씨는 실제 카톡처럼 Noto Sans KR, 자막은 Pretendard 그대로입니다.
3. 되돌리려면 FY_FONT=pretendard로 렌더링합니다(scripts/fy_common.py).

## 9. Claude가 해석해서 정한 곳 (확인 부탁드립니다)

1. "카톡 등장 효과"(1)는 화면 효과(말풍선이 튀어나오는 움직임)로 보고 뺐습니다. 메시지 보냄·받음 소리는 남겼습니다. 20번에서 같은 말을 쓰신 자리("메시지 옆 숫자 1은 그대로입니다")에는 v1에 소리가 없고 화면 효과만 있었기 때문입니다. 소리도 빼길 원하시면 알려 주세요.
2. 가운데 글씨의 따옴표(12)는 작은따옴표와 함께 큰따옴표도 뺐습니다. 아래 자막의 따옴표는 그대로 두었습니다.
3. '하며', '하고'를 빼신 것과 같은 자리 2곳에서 연결말을 더 뺐습니다(5장 3번).
4. 가운데 글씨의 배경: 따로 말씀하신 곳(29, 31, 46~48, 55)은 흐린 영상 위에, 경보기·AI 그림·아이콘을 빼신 곳은 검은 화면에 두었습니다. 따로 말씀이 없던 35번(병동 사진)과 57번(마지막 영상)은 v1의 사진·영상을 흐리게 깔았습니다.
5. 52번(6시 30분에 보낸 카톡이…)은 v1의 메모 화면 대신 검은 화면 가운데 글씨로 끊어서 보여 줍니다.
6. 19번 시계는 7시 55분 무렵입니다. 7시를 막 넘기는 장면을 원하시면 그림(아이콘)으로 그릴 수 있습니다.
7. 시계 효과음(10)은 말씀하신 "3시간, 4시간이 넘어가면" 외에 "그렇게 9시가 되고"의 같은 소리도 뺐습니다.

## 10. 다시 만드는 순서

run_v2.sh 하나로 v1 녹음에서 v2 영상까지 만듭니다(VIDEO_ROOT 설정, v1 준비물은 credits.md 3장, 운영자 사진은 work/owner/에).

1. edit_narration_v2.py: v1 녹음 → 쉼 줄이기, 딸깍 소리 처리 → work/v2/narration.wav, timemap.json, edit_log_v2.json
2. make_lines.py 01_불안형_답장 subtitles_v2.txt lines_v2.json
3. map_words.py(음성 인식 낱말을 v2 시각으로) → align_words.py → onsets.py → ctc_align.py → onsets_v2.py → lines_align_v2.json
4. make_photos_v2.py, build_spec_v2.py → spec_v2.json
5. make_audio_v2.sh: make_bgm_segments_v2.py → bgm_sequence.py --constant → make_sfx_v2.py → mix_audio.py → work/v2/final_audio.wav
6. build_timeline.py → fit_clips.py → render_parallel.py(3개 프로세스, AAC 320kbps)
7. 기록: make_credits.py 01_불안형_답장 $VIDEO_ROOT --v2 → 이 문서 12~16장

## 11. 점검

(렌더링 뒤에 채움)

## 12. 스톡 영상 (79개, Mixkit)

모두 영상 페이지의 copyrightNotice가 "Free"(Mixkit Stock Video Free License)인 것을 확인했습니다(2026-10-24, 받아 둔 페이지 기준). 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다. 시각은 영상 안에서 장면이 시작하는 때입니다.

1. 4822 Woman texting on the street — https://mixkit.co/free-stock-video/woman-texting-on-the-street-4822/
   - 장면 001 0:00 (1초부터)
2. 4915 Hands of a person typing on a cell phone — https://mixkit.co/free-stock-video/hands-of-a-person-typing-on-a-cell-phone-4915/
   - 장면 002 0:02 (2초부터); 장면 026 1:34 (6초부터); 장면 148 9:12 (11.29초부터)
3. 4548 Woman lying on a sofa — https://mixkit.co/free-stock-video/woman-lying-on-a-sofa-4548/
   - 장면 010 0:40 (2초부터)
4. 26092 Young man eating while watching television — https://mixkit.co/free-stock-video/young-man-eating-while-watching-television-26092/
   - 장면 012 0:43 (1초부터)
5. 25583 Upset woman checking a cell phone while drinking tea — https://mixkit.co/free-stock-video/upset-woman-checking-a-cell-phone-while-drinking-tea-25583/
   - 장면 014 0:49 (0초부터)
6. 51394 Woman with insomnia lying in her bed trying to sleep — https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/
   - 장면 016 0:56 (12초부터); 장면 040 2:07 (3초부터); 장면 109 6:53 (20초부터); 장면 115 7:12 (32.5초부터); 장면 120 7:33 (28초부터)
7. 51399 Restless woman with insomnia trying to sleep — https://mixkit.co/free-stock-video/restless-woman-with-insomnia-trying-to-sleep-51399/
   - 장면 017 0:58 (0초부터); 장면 042 2:16 (7.8초부터)
8. 4513 Worried and sad woman hugging a cushion — https://mixkit.co/free-stock-video/worried-and-sad-woman-hugging-a-cushion-4513/
   - 장면 019 1:05 (1초부터); 장면 086 5:15 (6초부터)
9. 4733 Scientist observing through a microscope — https://mixkit.co/free-stock-video/scientist-observing-through-a-microscope-4733/
   - 장면 022 1:19 (1초부터)
10. 4897 Girl reading a book in nature — https://mixkit.co/free-stock-video/girl-reading-a-book-in-nature-4897/
   - 장면 023 1:24 (1초부터); 장면 129 8:01 (8초부터)
11. 100050 Woman smiling at her phone on a cozy couch — https://mixkit.co/free-stock-video/woman-smiling-at-her-phone-on-a-cozy-couch-100050/
   - 장면 024 1:29 (1초부터); 장면 188 11:46 (6초부터)
12. 4333 View inside a wagon in motion — https://mixkit.co/free-stock-video/view-inside-a-wagon-in-motion-4333/
   - 장면 025 1:32 (1초부터)
13. 42982 Couple having dinner together at home — https://mixkit.co/free-stock-video/couple-having-dinner-together-at-home-42982/
   - 장면 028 1:38 (1초부터, 가장자리 잘라 냄)
14. 39826 Alarm clock outside, time lapse — https://mixkit.co/free-stock-video/alarm-clock-outside-time-lapse-39826/
   - 장면 029 1:40 (0초부터, 가장자리 잘라 냄)
15. 100053 A young smiling woman sitting on a comfy couch using her phone — https://mixkit.co/free-stock-video/a-young-smiling-woman-sitting-on-a-comfy-couch-using-100053/
   - 장면 031 1:43 (1초부터); 장면 159 9:54 (6초부터)
16. 4911 Young woman lying down watching images on her cell phone — https://mixkit.co/free-stock-video/young-woman-lying-down-watching-images-on-her-cell-phone-4911/
   - 장면 032 1:46 (1초부터); 장면 174 10:56 (6.94초부터)
17. 43381 Woman at night lying down using her cell phone — https://mixkit.co/free-stock-video/woman-at-night-lying-down-using-her-cell-phone-43381/
   - 장면 034 1:52 (8초부터); 장면 059 3:37 (10초부터)
18. 4708 Girl regretting regret and sad — https://mixkit.co/free-stock-video/girl-regretting-regret-and-sad-4708/
   - 장면 036 1:54 (2.5초부터); 장면 168 10:25 (6초부터)
19. 39789 Girl lying down chatting on her cell phone before sleeping — https://mixkit.co/free-stock-video/girl-lying-down-chatting-on-her-cell-phone-before-sleeping-39789/
   - 장면 038 2:00 (0초부터, 휴대폰 뒷면 로고를 지운 판(logo_patch.py))
20. 4457 Tower Bridge in London during sunset — https://mixkit.co/free-stock-video/tower-bridge-in-london-during-sunset-4457/
   - 장면 044 2:25 (1초부터)
21. 51390 Face of a woman lying down trying to sleep — https://mixkit.co/free-stock-video/face-of-a-woman-lying-down-trying-to-sleep-51390/
   - 장면 058 3:32 (5초부터); 장면 066 3:59 (16초부터)
22. 4809 Business people at work meeting — https://mixkit.co/free-stock-video/business-people-at-work-meeting-4809/
   - 장면 061 3:44 (1초부터)
23. 101412 Emotionally Disconnected Couple — https://mixkit.co/free-stock-video/emotionally-disconnected-couple-101412/
   - 장면 062 3:47 (1초부터)
24. 51429 A visible looking worried woman walking through her tiny apartment at night — https://mixkit.co/free-stock-video/a-visible-looking-worried-woman-walking-through-her-tiny-apartment-51429/
   - 장면 063 3:50 (2초부터); 장면 104 6:31 (8초부터)
25. 31413 Young man lying on his bed checking his smartphone — https://mixkit.co/free-stock-video/young-man-lying-on-his-bed-checking-his-smartphone-31413/
   - 장면 064 3:54 (1초부터); 장면 130 8:04 (7.5초부터)
26. 51389 Thoughtful woman in her bed trying to sleep dealing with insomnia — https://mixkit.co/free-stock-video/thoughtful-woman-in-her-bed-trying-to-sleep-dealing-with-51389/
   - 장면 065 3:56 (0초부터)
27. 42088 Close up of the flag of Australia waving — https://mixkit.co/free-stock-video/close-up-of-the-flag-of-australia-waving-42088/
   - 장면 067 4:02 (1초부터)
28. 4519 Students walking in a university — https://mixkit.co/free-stock-video/students-walking-in-a-university-4519/
   - 장면 068 4:06 (1초부터)
29. 100530 People running on treadmills at the gym — https://mixkit.co/free-stock-video/people-running-on-treadmills-at-the-gym-100530/
   - 장면 070 4:13 (1초부터)
30. 51121 A young smiling woman is texting on a mobile phone from the comfort of the couch — https://mixkit.co/free-stock-video/a-young-smiling-woman-is-texting-on-a-mobile-phone-51121/
   - 장면 071 4:17 (0.5초부터)
31. 28321 Frustrated student at his school studying his notes — https://mixkit.co/free-stock-video/frustrated-student-at-his-school-studying-his-notes-28321/
   - 장면 072 4:20 (1초부터)
32. 39958 Boy whispering something funny to a girl — https://mixkit.co/free-stock-video/boy-whispering-something-funny-to-a-girl-39958/
   - 장면 074 4:28 (1초부터)
33. 8757 Annoyed and frustrated man with his smartphone — https://mixkit.co/free-stock-video/annoyed-and-frustrated-man-with-his-smartphone-8757/
   - 장면 075 4:33 (0초부터)
34. 4560 Students walking through a college — https://mixkit.co/free-stock-video/students-walking-through-a-college-4560/
   - 장면 076 4:38 (1초부터); 장면 167 10:23 (8초부터)
35. 99890 Close up a hand writing notes on a notebook with a pen — https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/
   - 장면 079 4:53 (1초부터)
36. 4701 Worried and sad man with his head down — https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/
   - 장면 082 5:01 (1초부터)
37. 8743 Heartbroken crying woman slowly sits on the floor — https://mixkit.co/free-stock-video/heartbroken-crying-woman-slowly-sits-on-the-floor-8743/
   - 장면 083 5:04 (1초부터)
38. 8739 Worried and sad woman, outdoors — https://mixkit.co/free-stock-video/worried-and-sad-woman-outdoors-8739/
   - 장면 084 5:08 (1초부터); 장면 118 7:26 (6초부터)
39. 51395 Girl using her cell phone in her bed waiting to sleep — https://mixkit.co/free-stock-video/girl-using-her-cell-phone-in-her-bed-waiting-to-51395/
   - 장면 085 5:11 (15초부터); 장면 185 11:27 (8초부터)
40. 40421 Mother hugs her crying daughter — https://mixkit.co/free-stock-video/mother-hugs-her-crying-daughter-40421/
   - 장면 100 6:16 (1초부터)
41. 939 Couple silhouette walking through a neighborhood — https://mixkit.co/free-stock-video/couple-silhouette-walking-through-a-neighborhood-939/
   - 장면 102 6:25 (1초부터)
42. 4500 Upset woman sitting on the floor — https://mixkit.co/free-stock-video/upset-woman-sitting-on-the-floor-4500/
   - 장면 105 6:35 (1초부터)
43. 4549 Mother with her happy daughters — https://mixkit.co/free-stock-video/mother-with-her-happy-daughters-4549/
   - 장면 107 6:46 (1초부터)
44. 4624 Couple holding hands in a walk — https://mixkit.co/free-stock-video/couple-holding-hands-in-a-walk-4624/
   - 장면 108 6:50 (1초부터)
45. 25586 Sad girl sitting on the floor — https://mixkit.co/free-stock-video/sad-girl-sitting-on-the-floor-25586/
   - 장면 110 6:57 (0.5초부터)
46. 4401 Crowds of people cross a street junction — https://mixkit.co/free-stock-video/crowds-of-people-cross-a-street-junction-4401/
   - 장면 113 7:06 (2.65초부터, 가장자리 잘라 냄)
47. 26091 Man eats watching television on a rainy night — https://mixkit.co/free-stock-video/man-eats-watching-television-on-a-rainy-night-26091/
   - 장면 114 7:10 (1초부터)
48. 4700 Woman stressed and wailing, profile view — https://mixkit.co/free-stock-video/woman-stressed-and-wailing-profile-view-4700/
   - 장면 124 7:43 (1초부터)
49. 4764 Cute old couple in a park — https://mixkit.co/free-stock-video/cute-old-couple-in-a-park-4764/
   - 장면 127 7:54 (1초부터)
50. 4800 Woman meditating with her dog in the sunset — https://mixkit.co/free-stock-video/woman-meditating-with-her-dog-in-the-sunset-4800/
   - 장면 128 7:58 (1초부터)
51. 42904 Woman meditating and breathing deeply — https://mixkit.co/free-stock-video/woman-meditating-and-breathing-deeply-42904/
   - 장면 131 8:08 (6초부터); 장면 143 8:56 (9.8초부터)
52. 43846 Face of a scared and sad man — https://mixkit.co/free-stock-video/face-of-a-scared-and-sad-man-43846/
   - 장면 134 8:21 (0초부터)
53. 43396 Two actresses rehearsing a script together — https://mixkit.co/free-stock-video/two-actresses-rehearsing-a-script-together-43396/
   - 장면 137 8:33 (2초부터)
54. 43404 Face of a talented actress rehearsing her script — https://mixkit.co/free-stock-video/face-of-a-talented-actress-rehearsing-her-script-43404/
   - 장면 138 8:36 (0초부터)
55. 42903 Young woman meditating with incense — https://mixkit.co/free-stock-video/young-woman-meditating-with-incense-42903/
   - 장면 139 8:42 (17초부터)
56. 3110 Minimalist room with gray sofa — https://mixkit.co/free-stock-video/minimalist-room-with-gray-sofa-3110/
   - 장면 140 8:46 (7.9초부터)
57. 3132 Time lapse of a small town at night — https://mixkit.co/free-stock-video/time-lapse-of-a-small-town-at-night-3132/
   - 장면 141 8:51 (0초부터)
58. 8736 Profile of a distressed young woman — https://mixkit.co/free-stock-video/profile-of-a-distressed-young-woman-8736/
   - 장면 142 8:51 (0초부터)
59. 26090 Table in a living room with fast food while a man watches television — https://mixkit.co/free-stock-video/table-in-a-living-room-with-fast-food-while-a-26090/
   - 장면 144 8:57 (8.4초부터)
60. 42270 Face of a very worried girl — https://mixkit.co/free-stock-video/face-of-a-very-worried-girl-42270/
   - 장면 147 9:08 (1초부터)
61. 39780 Girl is awakened by messages that arrive on her cell phone — https://mixkit.co/free-stock-video/girl-is-awakened-by-messages-that-arrive-on-her-cell-39780/
   - 장면 152 9:25 (1초부터, 휴대폰 화면 글자 흐림)
62. 8744 Young man upset and frustrated receiving a message — https://mixkit.co/free-stock-video/young-man-upset-and-frustrated-receiving-a-message-8744/
   - 장면 154 9:33 (1초부터)
63. 4938 Hands of a girl working on a computer — https://mixkit.co/free-stock-video/hands-of-a-girl-working-on-a-computer-4938/
   - 장면 156 9:44 (1초부터)
64. 4761 Concentrated boy studying at home — https://mixkit.co/free-stock-video/concentrated-boy-studying-at-home-4761/
   - 장면 157 9:46 (0.91초부터)
65. 41638 Programmer using his cell phone while working at his desk — https://mixkit.co/free-stock-video/programmer-using-his-cell-phone-while-working-at-his-desk-41638/
   - 장면 158 9:51 (1초부터)
66. 4517 Annoyed woman working in a room — https://mixkit.co/free-stock-video/annoyed-woman-working-in-a-room-4517/
   - 장면 161 10:00 (1초부터)
67. 42655 A woman writing in her spiral notebook — https://mixkit.co/free-stock-video/a-woman-writing-in-her-spiral-notebook-42655/
   - 장면 164 10:09 (0초부터); 장면 165 10:11 (1.768초부터, 0.937배속)
68. 41180 Eye of a woman looking at a tablet — https://mixkit.co/free-stock-video/eye-of-a-woman-looking-at-a-tablet-41180/
   - 장면 169 10:28 (1초부터)
69. 4511 Sad girl looking out the window — https://mixkit.co/free-stock-video/sad-girl-looking-out-the-window-4511/
   - 장면 173 10:53 (1초부터)
70. 4656 Couple sitting watching a photo album — https://mixkit.co/free-stock-video/couple-sitting-watching-a-photo-album-4656/
   - 장면 175 10:59 (1초부터)
71. 101233 Girl Hugging Dog — https://mixkit.co/free-stock-video/girl-hugging-dog-101233/
   - 장면 176 11:00 (1초부터)
72. 4644 Photo album opened by a man — https://mixkit.co/free-stock-video/photo-album-opened-by-a-man-4644/
   - 장면 177 11:01 (0.93초부터)
73. 4840 Woman during a sunset on a rooftop — https://mixkit.co/free-stock-video/woman-during-a-sunset-on-a-rooftop-4840/
   - 장면 178 11:06 (1초부터)
74. 52419 The tree branches gently moving with the wind over a clear blue sky and the moon at daytime — https://mixkit.co/free-stock-video/the-tree-branches-gently-moving-with-the-wind-over-a-52419/
   - 장면 179 11:11 (1초부터)
75. 4547 People having a work meeting around a table — https://mixkit.co/free-stock-video/people-having-a-work-meeting-around-a-table-4547/
   - 장면 180 11:16 (1초부터)
76. 1623 People getting into the subway train — https://mixkit.co/free-stock-video/people-getting-into-the-subway-train-1623/
   - 장면 181 11:17 (1초부터)
77. 4231 Pedestrian walk in Tokyo — https://mixkit.co/free-stock-video/pedestrian-walk-in-tokyo-4231/
   - 장면 183 11:22 (11.3초부터)
78. 25592 Young stressed woman with headache — https://mixkit.co/free-stock-video/young-stressed-woman-with-headache-25592/
   - 장면 184 11:23 (1초부터)
79. 100067 A young smiling woman enjoys social media scrolling on her red phone laying on the comfy bed at midnight — https://mixkit.co/free-stock-video/a-young-smiling-woman-enjoys-social-media-scrolling-on-her-100067/
   - 장면 187 11:43 (1초부터)

## 13. AI 사진

RealVisXL V5.0 Lightning(SG161222, openrail++ 라이선스, 상업 이용 가능), scripts/gen_batch.py, 지시문은 ai_images.json. 실존 인물(로라, 연구자)은 그리지 않았고, 사람은 뒷모습만 넣었습니다(B07 뒤쪽의 작은 두 사람은 얼굴을 알아볼 수 없을 만큼 작고 흐림).

1. B01 — 장면 088 5:23 (B01_s1.png): 1952년 영국에서 공개된, 한 흑백 기록 영화 (영사기 스톡 4개가 모두 제한 라이선스)
   - 지시문: vintage 16mm film projector casting a bright beam of light across a dark room, dust in the beam / black and white documentary photo, 1950s, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
2. B05 — 장면 094 5:49 (B05_s1.png): 침대 난간을 붙잡고 엄마를 부르며 (아이는 그리지 않음: 실존 인물)
   - 지시문: close-up of the white iron bars of an old hospital crib, crumpled small blanket inside, dramatic window light / black and white documentary photo, 1950s Britain, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
3. B02 — 장면 090 5:33 (B02_s1.png), 장면 097 6:02 (B02_s1.png), 장면 098 6:04 (B02_s1.png): 로라는 작은 수술을 받기 위해, 8일 동안 병원에 입원 (병동, 사람 없음)
   - 지시문: 1950s hospital children's ward, rows of empty white iron cribs with folded blankets, tall windows, polished floor, no people / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
4. B06 — 장면 095 5:54 (B06_s1.png): 로라는 더 이상 울지도 않고, 멍하니 앉아 있습니다 (아이 대신 인형)
   - 지시문: a small worn teddy bear sitting alone in a white iron hospital crib, empty ward, quiet afternoon light / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
5. B07 — 장면 096 5:58 (B07_s1.png): 간호사들 눈에는, 병원 생활에 잘 적응한 아이처럼
   - 지시문: a 1950s nurse in a white uniform and cap walking away down a long hospital ward, seen from behind, iron beds / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
6. B08b — 장면 099 6:09 (B08b_s1.png): 간호사가 다정하게 다가와 말을 걸자 (B08을 다시 만듦: 뒷모습)
   - 지시문: back view of a 1950s nurse in a white uniform and cap, her back to the camera, bending over a white iron crib in a hospital ward, warm window light / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
7. B09c — 장면 045 2:30 (B09c_s2.png), 장면 051 2:51 (B09c_s2.png): 지금 여러분은, 실험실 의자에 앉아 있습니다 (B09 지시문에 화면의 바위를 더함) — 씨앗 2(B09c_s2)를 씀: 뒷모습 두 사람이 큰 화면의 바위를 봄. 씨앗 1은 사람이 화면 속에 들어가 쓰지 않음
   - 지시문: a person seen from behind sitting on a chair facing a large computer screen in a dim psychology lab, the screen shows a photo of two grey rocks, cables on the desk
   - 씨앗 1, 2, 1152x648, 5단계, CFG 1.0
8. C02 — 장면 021 1:12 (C02_s1.png): 같은 줄 후보 2: 알 수 없는 짙은 안개 앞에 선 뒷모습
   - 지시문: a lone person seen from behind standing on an empty road at night, facing a huge dense wall of dark fog, small figure, face not visible, ominous heavy atmosphere / cinematic photo, realistic, low key lighting, muted colors
   - 씨앗 1, 1152x648, 5단계, CFG 1.0

## 14. 운영자 사진

1. bowlby_v2.png — 장면 092 5:41 (bowlby_v2.png): 운영자가 보낸 사진(make_photos_v2.py로 16:9 화면에 맞춤, 커밋하지 않음)
2. ariely_v2.png — 장면 151 9:23 (ariely_v2.png): 운영자가 보낸 사진(make_photos_v2.py로 16:9 화면에 맞춤, 커밋하지 않음)

## 15. 배경음악 (Mixkit Stock Music Free License, -36 LUFS, 곡이 바뀔 때 3초 겹침)

1. 0:00~1:29 Pop Track 01 / Lily J (Mixkit 727, https://mixkit.co/free-stock-music/) — 도입 퀴즈: 궁금증과 가벼운 긴장 (Rhythmic Underscore, Neutral, Positive, Technology). 약 121 BPM, 8분음 하이햇으로 0초부터 박자가 또렷함(박자 선명도 0.91). 말소리 대역 1~4 kHz 0.022, 선율 0.07
2. 1:29~2:19 A Love Affair / Michael Ramir C. (Mixkit 1050, 곡 9초부터, https://mixkit.co/free-stock-music/) — 지우의 밤: 초조한 기다림 (Hip Hop, Serious, Slow, City / Insistent, Serious 목록). 약 79 BPM에 잘게 쪼갠 하이햇(초당 5.4타)이 쉬지 않음. 앞 11초의 조용한 전주를 건너뛰고, 12초에 들어오는 박자가 앵커에 맞도록 9초부터
3. 2:19~4:02 Moon Walk / Eugenio Mininni (Mixkit 609, 곡 65초부터, https://mixkit.co/free-stock-music/) — 실험 1 바위와 뱀: 박동이 있는 긴장 (Electronica, Disturbing, Synth, Cinematic, Medical / Suspenseful, Tension, Science 목록). 약 98 BPM. 앞 72초는 박자가 약한 깔림이라 건너뛰고, 73초에 들어오는 박자가 앵커에 맞도록 70초부터. 73~171초는 소리 크기가 고름. 말소리 대역 0.026, 선율 0.05 [v2 시각에 맞춘 조정: offset 70 -> 65.0 s: the part is 105.9 s with the v2 timing, the track is usable to 171 s]
4. 4:02~5:17 Trapanomics / Arulo (Mixkit 283, 곡 8.5초부터, https://mixkit.co/free-stock-music/) — 실험 2 문자 실험: 수상하고 리듬 있는 긴장 (Hip Hop, Mysterious, Disturbing, Bells / Serious, Tension, Investigation 목록). 약 80 BPM(160의 하프타임). 11.5초에 들어오는 박자가 앵커에 맞도록 8.5초부터. 곡 50~60초(구간 안 약 42~52초)에 드럼이 10초쯤 빠지지만 소리 크기는 그대로
5. 5:17~7:04 Drawing the Sky / Eugenio Mininni (Mixkit 606, 곡 11초부터, https://mixkit.co/free-stock-music/) — 로라와 애착: 감정은 있지만 앞으로 나아가는 곡, 피아노 독주 아님 (Orchestral Pop, Reflective, Cinematic, Drama / Dramatic, Serious 목록). 약 100 BPM의 가벼운 드럼. 14초에 드럼이 들어오도록 11초부터. 고른 9곡 중 선율이 가장 많음(선율 0.24, 말소리 대역 0.10): 목소리와 겹치는지 귀로 확인 필요
6. 7:04~7:45 Shame / Eugenio Mininni (Mixkit 553, 곡 45초부터, https://mixkit.co/free-stock-music/) — 개인차: 생각하게 하는 긴장 (Electronica, Pop, Mysterious, Disturbing / Investigation 목록). 약 120 BPM(60으로도 잡힘). 앞 30초는 박자 없는 깔림이라 박자가 고르게 이어지는 45초부터. 4초 사이 소리 크기 변화 1.3 dB
7. 7:45~9:19 Crying Sea / Michael Ramir C. (Mixkit 1023, 곡 8초부터, https://mixkit.co/free-stock-music/) — 희망과 해결책 1: 희망적이고 가볍게 들뜸 (Chillout, Corporate, Atmospheric, Positive, Motivational). 약 106 BPM, 초당 5.4타. 11초에 들어오는 박자가 앵커에 맞도록 8초부터, 곡 50초쯤(구간 약 40초)부터 한 단계 차오름
8. 9:19~11:05 Pop Two / Grigoriy Nuzhny (Mixkit 697, https://mixkit.co/free-stock-music/) — 해결책 2, 3: 긍정적인 그루브와 힘 (Corporate, Motivational, Lifestyle / Insistent 목록). 약 100 BPM, 0초부터 박자(초당 4.7타). 140초라 이 구간을 반복 없이 채움
9. 11:05~11:50 You and Me / Michael Ramir C. (Mixkit 1124, https://mixkit.co/free-stock-music/) — 마무리: 따뜻하고 희망적인 가벼운 박자 (Pop, Carefree, Relaxed / Warm 목록). 약 93 BPM, 0초부터 박자, 4초 사이 소리 크기 변화 1.3 dB. 말소리 대역 0.033, 선율 0.04

## 16. 효과음 (Mixkit Sound Effects Free License)

1. 2354 Message pop alert
2. 2357 Bubble pop up alert notification
3. 2365 Electric pop

넣은 자리(sfx_log_v2.json):
1. 0:04 (4.07초) 보냄: 오늘 퇴근하고 뭐할꺼야?
2. 0:13 (13.11초) 받음: 뭐 할껀 없어, 같이 저녁 먹을까?
3. 0:18 (18.91초) 받음: 헉 미안해..ㅜ회식 와서 연락을 이제 봤네
4. 1:37 (97.45초) 보냄: 오늘 하루 어땠어요?
5. 1:54 (114.01초) 보냄: 바쁘세요??
6. 2:11 (131.63초) 보냄: 자요..?
7. 2:47 (167.22초) 전기: 손등에 따끔한 전기가
