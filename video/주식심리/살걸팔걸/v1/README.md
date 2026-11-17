# 살걸·팔걸 편 영상 v1 기록 (2026-11-06)

사용자께서 보내 주신 최종 대본(../대본_최종_사용자.txt, 사진 번호는 ../대본_사진표시.md), AI 사진 47장, 녹음 3개로 만든 첫 영상의 기록입니다.
영상, 녹음, 사진, 스톡 원본, 음악 원본은 올리지 않았습니다.

요청(2026-11-06)
- "대본, 녹음본, 사진 줄테니 영상제작 바로 돌입. 대본은 너가 가지고 있고, 사진은 내가 여기에 넣는 순서대로 번호 매겨서 쓰면됨."
- 사진은 메시지 세 개(17 + 20 + 10장)로 받아 받은 순서대로 1~47번. 녹음은 세 개(1_1, 2_1, 3_1).
- "47,48번은 동일한 사진을 쓰던, 아니면 스톡 영상을 활용하던 해줘": 48번 사진은 만들지 않음. 47번 사진은 '셋째. 오답노트를
  작성하세요'와 첫 혼잣말까지 쓰고, 48번 자리('그때 내가 너무 좋은 쪽으로만 / 생각했었던 것 같아.')는 스톡 영상(st32b).

파일과 순서(작업 폴더 scratchpad/salgeol/v1, 전체 순서는 run_v1.sh)
1. 사진: 받은 순서 = 대본 번호(photos_in/P01~P47.png, 모두 1024x572).
2. 별 표시 지우기: 03·04편, 수면 편과 같은 도구(wm_remove_v3.py, wm_post.py, wm_choose.py). 03편 2000 크기의 깨끗한 별 모양을
   1024 크기로 줄여 씀(별 중심 934.5, 482.5). 사진마다 고른 방법(메움 또는 되살림)은 wm_choose_1024.txt(1~37번),
   wm_choose_1024_b.txt(38~47번). 별 자리를 크게 본 점검 시트에서 자국이 보이지 않음.
3. make_photos.py: photos_final/PNN.png. 흐림: 37번 상자 옆면의 쇼핑몰 로고와 글자, 29번 간판의 전화번호처럼 보이는 숫자 두 곳.
4. 녹음: 48 kHz 모노로만 바꿈(자르거나 속도를 바꾸지 않음). join_narration.py로 세 파일을 이어 rec/rec.wav(468.90초).
   세 파일 모두 말이 0.05초 안에 시작하고 끝에서 약 0.2초 안에 끝나서, 이음매에 무음을 넣어 쉼을 맞춤(1→2 0.70초, 2→3 0.50초;
   녹음 안 문장 사이 쉼은 0.25~0.59초). 목소리 끝 468.72초(rec/voice_end.json), 영상 끝 = 목소리 끝 + 3초 = 471.72초.
5. 받아쓰기(faster-whisper large-v3, rec/partN_words_seg.json)와 대본 대조. 숫자와 알파벳은 ko_words.py로 읽는 말(30% -> 삼십
   퍼센트, A -> 에이)로 바꿔 맞춤(rec/partN_words_ko.json).
   - 받아쓰기가 지어낸 말 두 곳은 음절 모델(w2v_ko)로 소리가 없음을 확인하고 맞춤에서 뺌: 1번 파일 170.8초 뒤(파일 끝),
     2번 파일 87.2~87.67초('상처를 겪었습니다'; '상철은'은 한 번만 읽힘).
   - 녹음과 대본이 다른 곳(ctc_check_batch.py, rec/checks1~3.json):
     '답한 람이 76%였습니다'(대본의 '람이'를 그대로 읽은 것으로 보임, 두 모델 모두 '사' 없음) -> 자막은 '답한 사람이 76%였습니다.',
     맞춤은 녹음대로. '것 같애' -> 녹음이 '같아'에 가까워 자막 '같아'. 대본 '* 016년' -> 녹음 '이천십육 년' -> 자막 '2016년'.
     '팔지말껄' -> 자막 '팔지 말걸'.
6. plan_salgeol.py(문장, 자막 조각, 자리 b 아래 / c 가운데 / i 가운데 기울임, 화면 P 사진 / st 스톡) -> make_lines.py ->
   lines.json(자막 257줄), units.json. 03·04편, 수면 편과 같은 규칙: 숫자는 아라비아 숫자, 쉼표 없음, 질문·해석·제목·마무리는
   가운데, 따옴표 속 속마음은 가운데 기울임. 같은 번호가 바로 이어지면(40 -> 40, 41 -> 41, 47 -> 47) 앞 화면을 그대로 씀.
7. run_align.sh(04편과 같은 도구: align_words.py, onsets.py, ctc_align.py, onsets_v2.py) -> onsets_v2.json. ctc_recheck.py로
   모든 줄을 앞 줄과 함께 다시 맞춰 봄(recheck_all.json): V105('2016년 프리드먼과…')만 1.06초 늦게 잡혀(첫 낱말 뒤 쉼을 시작으로
   봄) fix_onsets.py로 189.58초로 고침 -> onsets_v3.json. 나머지 줄은 0.15초 안에서 같음.
8. build_segments.py -> segments.json(장면 97개: 사진 60, 스톡 37),
   build_spec.py -> spec.json(수면 편과 같은 방식: 사진은 아주 천천히 확대만, 가운데 자막 동안 그림을 흐리고 어둡게).
9. 소리: prep_audio.py(목소리 -14 LUFS, 이 녹음은 +3.2 dB), bgm_sequence.py(배경음악 6곡, -36 LUFS, 곡마다 고정 크기, 3초 겹쳐
   바꿈, 끝 4초 줄임), mix_audio.py(-14 LUFS, 끝 단계 제한기).
   - 제한기 메모: 목소리를 +3.2 dB 올리면 가장 큰 곳이 +1.2 dBTP가 되어, 끝 단계 제한기가 10 ms 구간의 약 17%에서 최대 2.7 dB
     줄임. 결과 -14.0 LUFS, true peak -1.5 dBFS.
10. build_timeline.py, fit_clips.py, render_parallel.py(3조각, 영상만) + ffmpeg로 소리 합침(AAC 320kbps).

배경음악(Mixkit Stock Music Free License, audio/bgm_segments.json)
- 0:00~1:12.5 Fallen (Asper) / Eugenio Mininni (565): ① 도입(03편 v2에서 사용자가 고른 도입 곡, 04편·수면 편 도입과 같음)
- 1:12.5~2:47.6 Staring at the Night Sky / Alejandro Magaña (168): ② 원인 1(오딘, 바버와 오딘)
- 2:47.6~4:02.9 Tapis / Eugenio Mininni (615): ③ 원인 2(판 뒤의 밤, 프리드먼과 캐머러 실험)
- 4:02.9~5:28.7 Classical 2 / Jonny S. (709): ④ 원인 3(폴과 조지 문항, 길로비치와 메드벡)
- 5:28.7~7:21.3 Miss You / Eugenio Mininni (592): ⑤⑥ 해결책 1·2
- 7:21.3~끝 Rebecca on the Shore / Eugenio Mininni (545): ⑦ 해결책 3과 마무리(곡의 끝이 영상 끝과 맞게 58초부터)

스톡(Mixkit, 모두 라이선스 Free, 2026-11-06 확인. 고른 기록은 stock/picks/group_A·B·C.json, 바꾼 것은 stock_overrides.json.
앞 편에서 쓴 영상은 stock/used_before.txt(229개)로 거름)
- st01 47.3초부터 6.0초, Mixkit 2374 "DSRL camera shutter opening and closing" (0.3초부터): 나만 사면 떨어지고 / 나만 팔면 오르는 것 같습니다. / 누군가 내 계좌만 / 지켜보고 있는 걸까요?
- st02 56.7초부터 4.5초, Mixkit 4326 "Numbers in a nixie tube counter" (0.3초부터): 오늘은 내가 사면 떨어지고 / 팔면 오르는 것처럼 느껴지는 / 이유를 살펴보고
- st03 61.2초부터 5.1초, Mixkit 106 "Water drops creating ripples" (6.6초부터): 살걸 팔걸 하는 후회에 / 덜 흔들리는 방법 3가지를 / 이야기해 보겠습니다. | 아주 밝은 물이라 밝은 영상 색 보정에 밝기 0.78배를 더함
- st04 66.4초부터 6.2초, Mixkit 41638 "Programmer using his cell phone while working at his desk" (3초부터): 어떤 종목을 사라거나 / 팔라는 이야기는 아닙니다. / 사고파는 순간에 벌어지는 / 심리에 대한 이야기입니다. | 고른 사람이 4915(번아웃 편 영상)를 빼고 고름; 상표·글자 자리 흐림
- st05 72.5초부터 7.0초, Mixkit 21595 "Reverse tour of a library full of books" (1초부터): 먼저 조금 뜻밖의 이야기부터 / 해 보겠습니다. / 내가 사면 떨어진다는 말이 / 꼭 기분 탓만은 아닐 수 있습니다. | 고른 사람이 21587(번아웃 편 영상)을 빼고 고름; 상표·글자 자리 흐림
- st06 92.7초부터 6.6초, Mixkit 308 "Man working on his laptop" (2초부터): 산 것은 덜 오르고 / 판 것은 더 오른 셈이죠. / 그렇다면 우리는 언제 / 어떤 종목을 사게 될까요? | 고른 사람이 42665(그래프를 보는 여성)를 주인공과 헷갈리지 않게 빼고 고름; 상표·글자 자리 흐림
- st07 110.5초부터 6.1초, Mixkit 4308 "Aerial view of a city during the night" (5초부터): 주식 시장에는 / 수천 개의 종목이 있습니다. / 그 많은 종목을 하나하나 비교해 보고 / 고르기는 어렵죠. | 바꿈: 고른 4192(숫자와 글자가 번쩍이는 화면 모음 애니메이션)는 채널의 차분한 실사 화면과 맞지 않아, 해 질 녘에서 밤으로 넘어가며 수많은 건물에 불이 켜지는 도시 전경(4308)으로
- st08 116.6초부터 2.3초, Mixkit 50111 "Student makes a note over wooden desk filled with mathematical books and a calculator" (2.5초부터): 오딘은 이 문제도 살펴봤습니다. | 같은 촬영의 다른 장면(50110, 50113)을 앞 편에서 씀(2.3초로 짧아 그대로 둠)
- st09 134.7초부터 2.4초, Mixkit 4454 "People in the subway hall in Tokyo" (2초부터): 개인 투자자들은 / 어떻게 움직였을까요? | 상표·글자 자리 흐림
- st10 146.0초부터 5.5초, Mixkit 4188 "Stage of an electronic music festival" (1초부터): 오른 종목만 산 게 아니었던 거죠. / 오르든 떨어지든 / 눈에 띄면 사는 쪽이 많았습니다.
- st11 157.1초부터 4.4초, Mixkit 41190 "Young man from behind reading newspaper" (3.5초부터): 연구진은 그런 소식이 / 주가에 먼저 반영돼 있을 수 있다고 / 짚었습니다. | 고른 사람이 41201(태블릿을 보는 여성의 손)을 주인공과 헷갈리지 않게 빼고 고름
- st12 161.5초부터 6.1초, Mixkit 1038 "Dancer in the dark back view" (0.3초부터): 한마디로 내가 사고 싶어지는 순간은 / 그 종목이 가장 눈에 띄는 순간과 / 겹치기 쉽다는 것입니다. | 설명의 'brightens'라는 말 때문에 밝은 영상 보정이 걸리지 않게 기본 보정으로 정함(어두운 조명 장면)
- st13 167.6초부터 4.0초, Mixkit 4377 "Neighborhood in a city at dusk" (23.8초부터): 그렇다면 내가 팔면 / 오르는 것처럼 느껴지는 건 왜일까요? | 상표·글자 자리 흐림
- st14 210.2초부터 2.3초, Mixkit 3916 "Hand of a person in the dark through colored lights" (4초부터): 참가자들은 어떻게 했을까요?
- st15 237.9초부터 5.0초, Mixkit 99839 "Raindrops on a window with blurred lights in the background" (2초부터): 판 뒤에 오른 날이 / 유독 오래 기억에 남는 것도 / 이런 후회 때문일 수 있습니다.
- st16 242.9초부터 3.7초, Mixkit 49815 "Timelapse of a crossroads in a city at night" (0.5초부터): 그런데 같은 후회라도 / 더 아픈 쪽이 있습니다. | 상표·글자 자리 흐림
- st17 267.3초부터 4.2초, Mixkit 18306 "Pennies falling on a reflective surface with a dark background" (3초부터): 당신과 상철이 놓친 돈은 같습니다. / 누가 더 후회할까요?
- st18 275.9초부터 6.2초, Mixkit 100113 "A hand moves a white chess piece and takes a black one to the side of the board" (0.3초부터): 사람들은 가만히 있다가 놓친 것보다 / 직접 움직였다가 놓친 것을 / 더 후회할 일로 보는 거죠.
- st19 282.1초부터 2.0초, Mixkit 4519 "Students walking in a university" (9초부터): 또 다른 실험 하나를 보겠습니다. | 상표·글자 자리 흐림
- st20 296.5초부터 4.4초, Mixkit 1692 "Dry leaves from autumn on the ground" (1초부터): 이후에 두 사람 모두 / 자신의 선택이 잘못됐다는 걸 알게 됩니다.
- st21 316.1초부터 6.3초, Mixkit 28889 "Glass hourglass close up on a black background" (1.5초부터): 무언가를 해서 생긴 후회는 / 당장 아프고 / 하지 않아서 생긴 후회는 / 오래 남는 경향이 있다는 거죠.
- st22 328.7초부터 5.6초, Mixkit 3006 "Forest illuminated by the sun's rays" (2초부터): 그렇다면 살걸 팔걸 하는 후회에 / 덜 흔들리려면 / 무엇부터 해 보면 좋을까요?
- st23 347.4초부터 7.9초, Mixkit 100228 "Sunset Through A Car Side Mirror" (0.5초부터): 게다가 결과를 알고 나면 / 처음부터 알 수 있었던 일처럼 / 느껴지기 쉽습니다. / 이것을 사후 확신 편향이라고 부릅니다.
- st24 364.9초부터 6.1초, Mixkit 1744 "A person writing on a notebook at a coffee shop" (4.5초부터): 이유를 적다 보면 / 단톡방에서 다들 산다는 것 말고는 / 이유가 없다는 걸 알게 될 때도 있습니다. | 바꿈: 고른 144(창가에서 휴대폰을 치는 손)는 번아웃 편에서 쓴 영상이라, 카페에서 노트에 적는 남자의 손(1744)으로
- st25 371.0초부터 4.2초, Mixkit 818 "Coffee in green mug" (3.5초부터): 그걸 알아차리는 것만으로도 / 한 번 더 생각해 볼 틈이 생깁니다.
- st26 378.5초부터 5.2초, Mixkit 5248 "Poker chips and a pair of dice" (2초부터): 샀던 이유가 그대로인데 떨어졌다면 / 내가 어쩔 수 없는 / 운의 몫일 수 있습니다.
- st26b 383.7초부터 3.5초, Mixkit 100868 "Focus Pull from Raindrops to Payphone" (1초부터): 이유부터 흐릿했다면 / 다음에 고칠 점이 생긴 거고요. | 상표·글자 자리 흐림
- st27 387.1초부터 5.6초, Mixkit 101529 "Distorted Leaf Reflections on Lake" (1초부터): 그런데 이유를 적어 두어도 / 판 종목이 오르는 걸 보면 / 마음은 또 흔들립니다.
- st28 396.5초부터 5.1초, Mixkit 4423 "Electrical storm in the mountains" (2초부터): 앞의 실험에서 후회 신호가 나타난 건 / 판 종목이 오른 걸 보는 순간이었습니다.
- st29 418.0초부터 4.9초, Mixkit 28897 "Slowly approaching a clock on a black background" (1초부터): 일주일이 정답은 아닙니다. / 후회를 곱씹는 횟수를 줄이기 위한 / 예시입니다.
- st30 422.9초부터 2.5초, Mixkit 269 "A guy texting on his smartphone" (0.5초부터): 그리고 다시 볼 때는 / 이렇게 물어보세요.
- st31 431.6초부터 4.3초, Mixkit 1622 "Train arriving to a subway station" (6초부터): 실제로 후회 신호가 강했던 사람일수록 / 더 나은 선택을 놓쳤죠.
- st31b 435.9초부터 5.5초, Mixkit 51662 "A picturesque small creek with calm waters and steam at dawn" (2초부터): 후회와 지금의 판단을 / 나눠 보는 것만으로도 / 결정이 조금 덜 흔들릴 수 있습니다.
- st32 441.3초부터 5.0초, Mixkit 3147 "Clouds passing over the moon" (2초부터): 하지만 이미 지나간 / 살걸 후회와 팔걸 후회는 / 어떻게 하면 좋을까요? | 바꿈: 고른 1013(해변을 걷는 맨발)은 번아웃 편에서 쓴 영상이라, 고른 사람의 예비 영상인 달과 구름(3147)으로
- st32b 452.1초부터 3.4초, Mixkit 4644 "Photo album opened by a man" (0.5초부터): 그때 내가 너무 좋은 쪽으로만 / 생각했었던 것 같아. | 48번 사진 자리. 바꿈: 고른 4511(창가의 여성 뒷모습)은 주인공(남성)의 속마음 문장과 맞지 않고 번아웃 편에서도 쓴 영상이라, 남자의 손이 옛 앨범을 여는 영상(4644)으로(지난 일을 돌아봄)
- st33 458.4초부터 3.8초, Mixkit 4113 "Sun rays pass through the clouds in the mountains" (2초부터): 이렇게 후회를 / 다음에 쓸 기준 하나로 바꾸는 겁니다.
- st34 462.2초부터 9.5초, Mixkit 1704 "Night sky with stars at a calm lake, time lapse" (1초부터): 여러분에게도 가장 아쉬웠던 / 살걸 후회한 순간이나 / 팔걸 후회한 순간이 있나요? / 댓글로 공유해 주세요.

점검
- 렌더링 전: 스톡마다 쓰는 구간의 처음·가운데·끝 프레임을 한 줄에 놓은 시트(pick_sheet.py)로 얼굴, 글자, 상표, 컷 전환을 봄.
- 앞 편 영상 목록 보완: used_before.txt(190개)에 번아웃 편(첫 편) 영상 39개가 빠져 있던 것을 찾아 넣음(229개). 그래서 st04(4915),
  st05(21587), st24(144), st32(1013)를 바꿈. 고른 사람들의 예비 영상 가운데 번아웃 편 영상(4397, 28893, 144)은 쓰지 않음.
- 주인공은 남성(사진 1, 3, 20, 46 등)이라, 주인공의 속마음 자리(st32b)와 주인공처럼 보일 수 있는 자리(st06, st11)에 여성이 나오지
  않게 고름.
- 장면마다 가운데 시각의 프레임을 뽑아 봄(scene_sheet.py): 사진 번호, 자막 자리와 글자, 가운데 자막 밑 흐림, 상표.
- 완성: 살걸팔걸_v1.mp4(올리지 않음), 1920x1080, 30fps, 14,152프레임(471.73초, 7분 52초), 소리 AAC(320kbps로 설정, 실제 평균 303kbps) 48 kHz 스테레오, -14.0 LUFS, true peak -1.5 dBFS.
- 남은 것: '답한 람이 76%였습니다' 문장을 다시 녹음할지(사용자 답 기다림, 다시 녹음하지 않으면 지금 녹음 그대로).
  24번 사진은 머리에 뇌파 측정 모자(EEG)를 쓴 모습이지만 실제 연구(프리드먼과 캐머러 2016)는 MRI 장치 안에서 함(사진 목록도 MRI).
