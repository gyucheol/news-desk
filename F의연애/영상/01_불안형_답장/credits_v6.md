# 01편 「불안형 답장」 v6 기록

작성 2026-10-25. 결과 파일: 01_불안형_답장_v6.mp4 (1920×1080, 30fps, H.264 + AAC 320kbps 48kHz 스테레오, 11분 51.6초, 331MB(330,611,162바이트), 소리 크기 -14.0 LUFS, 최고점 -1.5dBFS, 점검은 10장). 운영자 목소리와 운영자가 만든 사진이 들어 있어 영상, 녹음, 사진은 저장소에 커밋하지 않았습니다(SendUserFile로 전달). v5 기록은 credits_v5.md, v4는 credits_v4.md, v3는 credits_v3.md, v2는 credits_v2.md, v1은 credits.md입니다.

사용자 요청(2026-10-25): "녹음본 1~8번까지 내가 속도를 약간 올려서 녹음해왔음. 이 녹음본으로 적용해줘." 녹음 파일 8개(1~8번)를 메시지 두 개(1~5번, 6~8번)로 보냄(원문은 부록 A).

---

## 1. 한눈에

1. 새 녹음 8개를 순서대로 이어 영상의 녹음을 모두 바꿨습니다. 장면, 사진, 배경음악, 효과음은 v5와 같고 새 녹음의 시각에 맞춰 다시 놓았습니다.
2. 녹음 다듬기: v2 규칙대로 쉼을 줄였고(문장 사이 0.22초, 구간 사이 0.38초, 쉼표 자리와 줄 안 0.16초), '내가 연락을 너무 재촉하는 것처럼' 앞의 '하..' 숨소리를 v4처럼 지웠습니다. 잡음 제거, 속도 변경 같은 다른 처리는 하지 않았습니다(3장).
3. 자막: 504줄의 시작 시각을 새 녹음에 다시 맞췄습니다(4장). 대본과 다르게 읽은 곳은 '자 그렇다면'의 '자' 한 곳이라 자막을 '그렇다면'으로 바꿨습니다. '88명'은 '여든여덟 명'으로 읽어 정렬용 말만 바꿨습니다(2장).
4. 길이: 11분 51.6초입니다(v5는 11분 50.1초). 쉼을 줄인 뒤의 말 속도는 이전 녹음과 거의 같습니다(7장).

## 2. 새 녹음 확인

1. 받은 파일: m4a 8개(AAC 48kHz, 약 250kbps, ffmpeg Lavf60으로 저장). 길이는 1~8번 차례로 66.4, 56.1, 120.3, 98.6, 97.9, 116.3, 95.7, 91.0초(합계 742.3초)입니다.
   - 두 채널이 같은 소리여서 한 채널(모노)로 썼습니다.
   - 파일마다 이미 -14.1 LUFS, 최고점 -2.1dBFS로 맞춰져 있고, 소리가 잘린(클리핑) 곳은 없습니다.
   - 15.6kHz 위가 잘려 있습니다. 이전 녹음과 같이 앞 단계에서 손실 압축을 한 번 더 거친 것으로 보입니다(추론). 말이 없는 곳은 -65~-73dB입니다(잡음 게이트로 보임).
2. 각 파일이 대본의 어디인지(음성 인식 결과를 자막 줄과 맞춤). 빠지거나 겹친 줄은 없습니다.
   - 1번: 처음~'하며 자신을 탓합니다.'(L001~L048)
   - 2번: '하지만 이게 정말'~'보이면 어떡하지...'(L049~L087)
   - 3번: '9시 반이 되자'~'홀로 들여다보고 있는 셈입니다.'(L088~L174)
   - 4번: '게다가 이렇게'~'만나게 됩니다.'(L175~L239)
   - 5번: '영화의 주인공은'~'똑같은 비상벨이 울렸기 때문입니다.'(L240~L302)
   - 6번: '그런데 참 신기하죠'~'텔레비전이 있어.'(L303~L379)
   - 7번: '일주일 뒤'~'밤 9시 정각에 다시 확인한다.'(L380~L442)
   - 8번: '셋째'~'댓글로 공유해 주세요.'(L443~L504)
3. 읽은 말 확인: 음성 인식(whisper large-v3)으로 받아 적어 대본과 한 글자씩 비교했습니다. 다른 곳은 음절 인식 모델(wav2vec2 한국어)과 소리 크기로 다시 확인했습니다.
   - 대본과 다르게 읽은 곳: 1곳. 6번 녹음 65초의 '자 그렇다면'을 '그렇다면'으로 읽었습니다. 두 인식 모두 '자'가 없고, '그렇다면' 앞 0.3초의 소리는 -36dB로 같은 녹음의 다른 음절(-10dB 안팎)보다 20dB 넘게 작아 숨소리로 봤습니다(추론). 자막을 녹음에 맞춰 '그렇다면'으로 바꿨습니다(CLAUDE.md 영상 제작 6번).
   - 숫자를 다르게 읽은 곳: '88명을 모았습니다.'를 '여든여덟 명'으로 읽었습니다. 화면 글은 그대로 두고 정렬용 말만 바꿨습니다(subtitles_v6.txt의 { }).
   - 받아 적기에서 대본과 다르게 나온 나머지 8곳은 음성 인식이 만든 말이었습니다: '붙여서 붙잡고', '확실할 때였을까요 확실할 때는', '이렇게 작아졌을까요 왜 우리의 뇌는', '위하여', '경보 장치가 사라지지 않는다는 데 있습니다', '3시간 3번만', '거듭나가게 됩니다', 끝의 '다음 영상에서 만나요'. 대부분 길이가 0초인 낱말이었고, 음절 모델과 소리 크기에서도 그 말은 없었습니다.
   - 말이 걸리거나 같은 말을 다시 읽은 곳은 찾지 못했습니다. 귀로 들어 확인하지는 못했습니다.

## 3. 녹음 다듬기

1. 잇기(join_narration_v6.py)
   - 8개를 순서대로 이었습니다. 처음에 0.20초 무음을 두고, 파일 사이에 0.50초 무음을 넣었습니다. 이 무음도 다른 쉼처럼 아래 2번에서 줄어듭니다.
   - 파일마다 시작에 0.015초, 끝에 0.020초 페이드를 줬습니다. 7번 파일은 소리가 남은 채(-41dB) 끝나서, 이음새에서 딸깍 소리가 나지 않게 하려는 것입니다.
   - 이은 녹음에서 한 표본짜리 튐(딸깍 소리)은 찾지 못했습니다.
2. '하..' 숨소리(sigh_v6.json): 2번 녹음 53.21~53.72초의 숨소리(가장 큰 곳 -18.7dB, 음성 인식에는 '아...'로 나옴)를 지웠습니다. '내가'가 53.74초에 시작해, 그 0.02초 앞의 가장 조용한 곳에서 잘랐습니다. 앞 문장과의 쉼은 1.09초에서 다른 문장 사이처럼 0.22초가 되었습니다.
3. 쉼 줄이기(edit_narration_v6.py, v2와 같은 규칙): 195곳에서 34.5초를 줄였습니다.
   - 문장 사이 85곳: 줄이기 전 중앙값 0.47초 → 0.22초
   - 구간이 시작하는 곳 9곳: 0.38초
   - 쉼표 자리 57곳, 줄 안 44곳: 0.16초
   - 말 뒤 0.06초와 다음 말 앞 0.05초, 숨소리는 남기고, 소리 없는 가운데만 잘라 0.015초 겹쳐 이었습니다.
   - 쉼의 종류는 이은 녹음에서 먼저 맞춘 자막 시각으로 나눴습니다(v2와 같음). 처음에는 대략 맞춘 시각으로 나눴는데, 문장 사이 쉼 여러 곳이 줄 안 쉼으로 잘못 나뉘어서 다시 했습니다.
4. 마지막 말 뒤 3.0초에서 끝나고, 전체에 한 가지 크기만 줘 -14 LUFS로 맞췄습니다(+0.1dB). 746.2초 → 711.6초입니다.
5. 기록: edit_log_v6.json(줄인 쉼 전부), 영상 폴더 밖의 work/v6/timemap.json(시각 대응표).

## 4. 자막 시각

1. 방법은 v2와 같습니다. 자막 첫 음절의 위치를 음절 정렬 모델로 찾고 실제 소리로 미세 조정했습니다(scripts/onsets_v2.py). 결과는 쉼 뒤에 소리가 시작하는 곳 367줄, 이어 말하는 곳의 골짜기 125줄, 바람 소리(ㅅ·ㅈ·ㅊ) 시작 9줄, 모델 위치 3줄입니다.
2. 두 번 맞춰 비교했습니다.
   - 쉼을 줄이기 전 녹음에서 맞춘 시각을 줄인 녹음 시각으로 옮긴 것과, 줄인 녹음에서 새로 맞춘 것을 비교했습니다.
   - 504줄 중 483줄은 0.01초 안으로 같았습니다. 0.03초 넘게 다른 8줄은 소리 크기 곡선과 음절 인식으로 하나씩 봤습니다.
   - '자요..?': 줄인 녹음에서는 음성 인식의 낱말 위치가 줄어든 쉼 안에 있어서, 시작이 '요'에 잡혔습니다(0.30초 늦음). 줄이기 전 녹음의 시각('ㅈ'이 시작하는 곳)을 썼습니다(make_align_v6.py).
   - '바쁘세요??': 줄인 녹음 쪽이 '바'의 시작(110.72초)이고, 다른 쪽은 'ㅃ' 뒤를 잡아서 줄인 녹음 쪽을 썼습니다.
   - 나머지 6줄(차이 0.03~0.07초, 영상 1~2장)은 줄인 녹음 쪽이 목소리가 커지기 시작하는 곳이라 그대로 썼습니다.
3. 줄마다 길이와 말 속도도 봤습니다. 0.3초보다 짧은 줄이나, 초당 2음절보다 느리거나 11.5음절보다 빠른 줄은 없습니다(중앙값 초당 6.8음절).
4. 자막 문구는 '자 그렇다면' → '그렇다면'(가운데 자막) 한 곳만 바뀌었습니다. 나머지 503줄은 v5와 같습니다.

## 5. 소리

1. 배경음악: v3~v5와 같은 곡(Mixkit 6곡, 9구간, -36 LUFS)을 새 시각에 맞춰 다시 놓았습니다. 4구간(River Flow)과 6구간(Xanthos)은 구간이 조금 길어져 곡 시작점을 각각 0.5~1초 앞당겼습니다(곡의 쓸 수 있는 끝을 넘지 않게, make_bgm_segments_v6.py).
2. 효과음: v4·v5와 같은 6곳의 같은 줄에, 새 시각으로 넣었습니다(sfx_log_v6.json).
3. 섞은 소리는 -14 LUFS입니다(10장).

## 6. 장면

1. v5의 장면 계획을 그대로 썼습니다(190개). 장면은 자막 줄에서 시작하므로 새 녹음의 시각을 그대로 따라갑니다. 바뀐 것은 '그렇다면' 장면의 첫 줄 이름뿐입니다(build_spec_v6.py).
2. 영상 장면 20개가 v5보다 0.15~0.54초 길어졌습니다. 스톡 맞추기 도구(fit_clips.py)가 시작점을 당기거나 조금 느리게 틀어 영상 끝을 넘지 않게 했습니다.
   - 4560(걸어가는 학생들): 0.916배속(v5 0.948배속)
   - 42655(수첩에 쓰는 사람): 0.898배속(v5 0.937배속)
   - 나머지는 원래 속도입니다.
3. 빠르게 감긴 구간이 있는 51399는 7.8~11.25초만 써서 그 구간(11.5초부터)을 피했습니다.

## 7. 말 속도와 길이

말씀하신 "속도를 약간 올려서"에 관해 잰 값입니다.

1. 완성 길이는 11분 51.6초로 v5(11분 50.1초)와 비슷합니다.
2. 쉼을 줄인 뒤 말소리가 있는 시간은 649.1초로 이전 651.2초와 비슷합니다. 자막 줄 기준 말 속도도 초당 6.83음절로 이전 6.87음절과 같습니다.
3. 받은 그대로의 녹음은 합계 742.3초로 이전 녹음(723.6초)보다 길었습니다. 쉼이 더 길어서이고, 줄인 쉼도 34.5초로 이전(11.6초)보다 많았습니다.
4. 추론(유추): 이전 녹음 파일이 이미 1.1배속이었기 때문에(credits_v2.md 2장), 이번에 조금 빠르게 읽은 녹음과 결과 말 속도가 비슷하게 나온 것으로 보입니다.
5. 더 빠르게 원하시면 두 가지 방법이 있습니다. 원하시는 쪽을 알려 주시면 그대로 하겠습니다.
   - 녹음 전체를 일정 비율로 빠르게(예: 1.05배). 속도를 바꾸는 처리는 소리가 조금 금속성으로 들릴 수 있습니다(credits_v2.md 2장).
   - 쉼을 더 짧게(예: 문장 사이 0.22초 → 0.15초).

## 8. Claude가 해석해서 정한 곳 (확인 부탁드립니다)

1. '자 그렇다면'을 녹음대로 '그렇다면'으로 바꿨습니다(2장 3번). 자막에 '자'를 다시 넣길 원하시면 되돌리겠습니다. 다만 그 경우 목소리에는 '자'가 없습니다.
2. '하..' 숨소리는 v4 요청("'하..' 숨소리 빼기")을 이번 녹음에도 적용해 지웠습니다(3장 2번).
3. 쉼은 v2 요청("문장 사이의 빈 시간이 있다면 줄이되, 최대한 자연스럽게")대로 이번 녹음에도 줄였습니다(3장 3번). 새 녹음은 줄 안의 쉼이 많아 줄 안 44곳도 0.16초로 줄였습니다.
4. 녹음에는 위의 두 가지 말고는 처리를 하지 않았습니다(속도, 음색, 잡음).
5. v5에서 확인을 부탁드린 것(credits_v5.md 8장)은 이번에 바꾸지 않았습니다.

## 9. 다시 만드는 순서

run_v6.sh 하나로 v5 준비물(사용자 사진, 스톡, 음악)과 새 녹음에서 v6 영상까지 만듭니다. run_v5.sh를 먼저 돌려야 합니다.

1. 녹음: 대화에 첨부된 8개를 work/rec_v6/in/rec1.m4a~rec8.m4a로 꺼내 둡니다(커밋하지 않음). WAV로 바꾸고 transcribe.py로 받아 적습니다.
2. join_narration_v6.py로 잇고, make_lines.py 01_불안형_답장 subtitles_v6.txt lines_v6.json
3. 이은 녹음에서 자막 시각: align_words.py → onsets.py → ctc_align.py → onsets_v2.py
4. edit_narration_v6.py(숨소리 sigh_v6.json, 쉼 줄이기, -14 LUFS) → work/v6/narration.wav, timemap.json, edit_log_v6.json
5. 줄인 녹음에서 자막 시각: map_words.py → align_words.py → onsets.py → ctc_align.py → onsets_v2.py → make_align_v6.py → lines_align_v6.json
6. make_audio_v6.sh: make_bgm_segments_v6.py → bgm_sequence.py --constant → make_sfx_v6.py → mix_audio.py
7. build_spec_v6.py → fetch_stock.sh v6 → build_timeline.py → fit_clips.py → render_parallel.py --video-only → ffmpeg로 소리 합치기(AAC 320kbps)
8. 기록: make_credits.py 01_불안형_답장 $VIDEO_ROOT --v6 → 이 문서 11~17장

## 10. 점검

1. 파일: ffprobe로 1920×1080, 30fps, 21,349장, 화면 711.633초(소리 711.635초), H.264 High + AAC 48kHz 스테레오(320kbps로 지정, 실제 약 302kbps)를 확인했습니다.
2. 소리: ebur128로 -14.0 LUFS, 최고점 -1.5dBFS, LRA 4.0 LU입니다(v5는 3.5 LU). 영상 속 소리의 압축 오차(4~15kHz)는 중앙값 -28.6dB이고, 오차가 신호의 1/4을 넘는 0.02초 구간은 16,676곳 중 2곳입니다(v5는 -30.6dB, 2곳).
3. 숨소리를 지운 곳(1:53.7 '내가 연락을 너무 재촉하는 것처럼'): 다듬은 녹음을 0.02초 간격으로 쟀습니다. '밀려옵니다.'가 끝난 뒤 '내가'가 시작할 때까지 소리가 -56dB 아래이고(방 소리와 무음), 숨소리는 없습니다. 귀로 들어 확인하지는 못했습니다.
4. 멈춤과 검은 화면: freezedetect·blackdetect가 찾은 35곳 중 34곳은 검은 카드와 아이콘 화면(원래 정지 화면)입니다. 1곳(2:57.9~3:01.0)은 v5와 같은 화면 반 나누기 시작 부분입니다. 사진 장면과 스톡 영상에서는 잡힌 곳이 없습니다.
5. 완성본 화면: 30초마다 24장, 세 조각 이음새 4장, 끝부분 4장, 바뀌거나 따로 확인한 줄 4장('그렇다면', '88명을 모았습니다.', '자요..?', '내가 연락을 너무 재촉하는 것처럼')을 완성 파일에서 뽑아 봤습니다.
6. 자막: 504줄이고, 글자가 v5와 다른 줄은 '그렇다면' 한 줄입니다.
7. 다시 만들기: run_v6.sh의 단계는 이번에 돌린 명령을 옮긴 것입니다. 처음부터 한 번에 다시 돌려 보지는 않았습니다(녹음 받아 적기만 약 30분 걸림).

## 11. 스톡 영상 (65개, Mixkit)

모두 영상 페이지의 copyrightNotice가 "Free"(Mixkit Stock Video Free License)인 것을 확인했습니다(2026-10-24, 받아 둔 페이지 기준). 유튜브·상업 이용이 가능하고 출처 표기는 필요 없습니다. 시각은 영상 안에서 장면이 시작하는 때입니다.

1. 4548 Woman lying on a sofa — https://mixkit.co/free-stock-video/woman-lying-on-a-sofa-4548/
   - 장면 010 0:38 (2초부터)
2. 26092 Young man eating while watching television — https://mixkit.co/free-stock-video/young-man-eating-while-watching-television-26092/
   - 장면 013 0:42 (1초부터)
3. 51394 Woman with insomnia lying in her bed trying to sleep — https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/
   - 장면 017 0:53 (12초부터); 장면 037 2:03 (3초부터); 장면 114 7:06 (32.5초부터); 장면 120 7:29 (28초부터)
4. 4897 Girl reading a book in nature — https://mixkit.co/free-stock-video/girl-reading-a-book-in-nature-4897/
   - 장면 024 1:21 (1초부터); 장면 130 7:58 (8초부터)
5. 39826 Alarm clock outside, time lapse — https://mixkit.co/free-stock-video/alarm-clock-outside-time-lapse-39826/
   - 장면 030 1:37 (0초부터, 가장자리 잘라 냄)
6. 43381 Woman at night lying down using her cell phone — https://mixkit.co/free-stock-video/woman-at-night-lying-down-using-her-cell-phone-43381/
   - 장면 033 1:49 (8초부터); 장면 060 3:30 (10초부터)
7. 4708 Girl regretting regret and sad — https://mixkit.co/free-stock-video/girl-regretting-regret-and-sad-4708/
   - 장면 034 1:51 (2.5초부터); 장면 172 10:30 (6초부터)
8. 39789 Girl lying down chatting on her cell phone before sleeping — https://mixkit.co/free-stock-video/girl-lying-down-chatting-on-her-cell-phone-before-sleeping-39789/
   - 장면 035 1:56 (0초부터, 휴대폰 뒷면 로고를 지운 판(logo_patch.py))
9. 51399 Restless woman with insomnia trying to sleep — https://mixkit.co/free-stock-video/restless-woman-with-insomnia-trying-to-sleep-51399/
   - 장면 039 2:11 (7.8초부터)
10. 4457 Tower Bridge in London during sunset — https://mixkit.co/free-stock-video/tower-bridge-in-london-during-sunset-4457/
   - 장면 041 2:20 (1초부터)
11. 51390 Face of a woman lying down trying to sleep — https://mixkit.co/free-stock-video/face-of-a-woman-lying-down-trying-to-sleep-51390/
   - 장면 059 3:25 (5초부터); 장면 069 3:50 (16초부터)
12. 4809 Business people at work meeting — https://mixkit.co/free-stock-video/business-people-at-work-meeting-4809/
   - 장면 062 3:37 (1초부터)
13. 101412 Emotionally Disconnected Couple — https://mixkit.co/free-stock-video/emotionally-disconnected-couple-101412/
   - 장면 063 3:39 (1초부터)
14. 51429 A visible looking worried woman walking through her tiny apartment at night — https://mixkit.co/free-stock-video/a-visible-looking-worried-woman-walking-through-her-tiny-apartment-51429/
   - 장면 064 3:42 (2초부터); 장면 103 6:25 (8초부터)
15. 31413 Young man lying on his bed checking his smartphone — https://mixkit.co/free-stock-video/young-man-lying-on-his-bed-checking-his-smartphone-31413/
   - 장면 066 3:46 (1초부터); 장면 131 8:02 (7.5초부터)
16. 42088 Close up of the flag of Australia waving — https://mixkit.co/free-stock-video/close-up-of-the-flag-of-australia-waving-42088/
   - 장면 070 3:55 (1초부터)
17. 100530 People running on treadmills at the gym — https://mixkit.co/free-stock-video/people-running-on-treadmills-at-the-gym-100530/
   - 장면 072 4:06 (1초부터)
18. 51121 A young smiling woman is texting on a mobile phone from the comfort of the couch — https://mixkit.co/free-stock-video/a-young-smiling-woman-is-texting-on-a-mobile-phone-51121/
   - 장면 073 4:09 (0.5초부터)
19. 28321 Frustrated student at his school studying his notes — https://mixkit.co/free-stock-video/frustrated-student-at-his-school-studying-his-notes-28321/
   - 장면 074 4:12 (1초부터)
20. 39958 Boy whispering something funny to a girl — https://mixkit.co/free-stock-video/boy-whispering-something-funny-to-a-girl-39958/
   - 장면 076 4:21 (1초부터)
21. 8757 Annoyed and frustrated man with his smartphone — https://mixkit.co/free-stock-video/annoyed-and-frustrated-man-with-his-smartphone-8757/
   - 장면 077 4:26 (0초부터)
22. 4560 Students walking through a college — https://mixkit.co/free-stock-video/students-walking-through-a-college-4560/
   - 장면 078 4:32 (0초부터, 0.916배속); 장면 171 10:27 (8초부터)
23. 99890 Close up a hand writing notes on a notebook with a pen — https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/
   - 장면 080 4:47 (1초부터)
24. 8743 Heartbroken crying woman slowly sits on the floor — https://mixkit.co/free-stock-video/heartbroken-crying-woman-slowly-sits-on-the-floor-8743/
   - 장면 083 4:58 (1초부터)
25. 8739 Worried and sad woman, outdoors — https://mixkit.co/free-stock-video/worried-and-sad-woman-outdoors-8739/
   - 장면 084 5:02 (1초부터)
26. 51395 Girl using her cell phone in her bed waiting to sleep — https://mixkit.co/free-stock-video/girl-using-her-cell-phone-in-her-bed-waiting-to-51395/
   - 장면 085 5:05 (15초부터); 장면 188 11:30 (8초부터)
27. 4513 Worried and sad woman hugging a cushion — https://mixkit.co/free-stock-video/worried-and-sad-woman-hugging-a-cushion-4513/
   - 장면 086 5:09 (6초부터)
28. 40421 Mother hugs her crying daughter — https://mixkit.co/free-stock-video/mother-hugs-her-crying-daughter-40421/
   - 장면 100 6:10 (1초부터)
29. 939 Couple silhouette walking through a neighborhood — https://mixkit.co/free-stock-video/couple-silhouette-walking-through-a-neighborhood-939/
   - 장면 102 6:20 (1초부터)
30. 4500 Upset woman sitting on the floor — https://mixkit.co/free-stock-video/upset-woman-sitting-on-the-floor-4500/
   - 장면 104 6:29 (1초부터)
31. 4549 Mother with her happy daughters — https://mixkit.co/free-stock-video/mother-with-her-happy-daughters-4549/
   - 장면 106 6:40 (1초부터)
32. 4624 Couple holding hands in a walk — https://mixkit.co/free-stock-video/couple-holding-hands-in-a-walk-4624/
   - 장면 107 6:44 (1초부터)
33. 25586 Sad girl sitting on the floor — https://mixkit.co/free-stock-video/sad-girl-sitting-on-the-floor-25586/
   - 장면 109 6:52 (0.5초부터)
34. 4401 Crowds of people cross a street junction — https://mixkit.co/free-stock-video/crowds-of-people-cross-a-street-junction-4401/
   - 장면 112 7:00 (2.65초부터, 가장자리 잘라 냄)
35. 26091 Man eats watching television on a rainy night — https://mixkit.co/free-stock-video/man-eats-watching-television-on-a-rainy-night-26091/
   - 장면 113 7:04 (1초부터)
36. 4700 Woman stressed and wailing, profile view — https://mixkit.co/free-stock-video/woman-stressed-and-wailing-profile-view-4700/
   - 장면 124 7:40 (1초부터)
37. 4764 Cute old couple in a park — https://mixkit.co/free-stock-video/cute-old-couple-in-a-park-4764/
   - 장면 128 7:50 (1초부터)
38. 4800 Woman meditating with her dog in the sunset — https://mixkit.co/free-stock-video/woman-meditating-with-her-dog-in-the-sunset-4800/
   - 장면 129 7:55 (1초부터)
39. 42904 Woman meditating and breathing deeply — https://mixkit.co/free-stock-video/woman-meditating-and-breathing-deeply-42904/
   - 장면 132 8:06 (6초부터); 장면 145 8:56 (9.8초부터)
40. 43396 Two actresses rehearsing a script together — https://mixkit.co/free-stock-video/two-actresses-rehearsing-a-script-together-43396/
   - 장면 140 8:33 (2초부터)
41. 43404 Face of a talented actress rehearsing her script — https://mixkit.co/free-stock-video/face-of-a-talented-actress-rehearsing-her-script-43404/
   - 장면 141 8:36 (0초부터)
42. 42903 Young woman meditating with incense — https://mixkit.co/free-stock-video/young-woman-meditating-with-incense-42903/
   - 장면 142 8:42 (17초부터)
43. 3110 Minimalist room with gray sofa — https://mixkit.co/free-stock-video/minimalist-room-with-gray-sofa-3110/
   - 장면 143 8:46 (7.9초부터)
44. 26090 Table in a living room with fast food while a man watches television — https://mixkit.co/free-stock-video/table-in-a-living-room-with-fast-food-while-a-26090/
   - 장면 146 8:57 (8.4초부터)
45. 42270 Face of a very worried girl — https://mixkit.co/free-stock-video/face-of-a-very-worried-girl-42270/
   - 장면 149 9:09 (1초부터)
46. 4915 Hands of a person typing on a cell phone — https://mixkit.co/free-stock-video/hands-of-a-person-typing-on-a-cell-phone-4915/
   - 장면 150 9:12 (10.87초부터)
47. 39780 Girl is awakened by messages that arrive on her cell phone — https://mixkit.co/free-stock-video/girl-is-awakened-by-messages-that-arrive-on-her-cell-39780/
   - 장면 155 9:26 (1초부터, 휴대폰 화면 글자 흐림)
48. 8744 Young man upset and frustrated receiving a message — https://mixkit.co/free-stock-video/young-man-upset-and-frustrated-receiving-a-message-8744/
   - 장면 157 9:35 (1초부터)
49. 4938 Hands of a girl working on a computer — https://mixkit.co/free-stock-video/hands-of-a-girl-working-on-a-computer-4938/
   - 장면 159 9:46 (1초부터)
50. 4761 Concentrated boy studying at home — https://mixkit.co/free-stock-video/concentrated-boy-studying-at-home-4761/
   - 장면 160 9:49 (0.89초부터)
51. 41638 Programmer using his cell phone while working at his desk — https://mixkit.co/free-stock-video/programmer-using-his-cell-phone-while-working-at-his-desk-41638/
   - 장면 161 9:54 (1초부터)
52. 100053 A young smiling woman sitting on a comfy couch using her phone — https://mixkit.co/free-stock-video/a-young-smiling-woman-sitting-on-a-comfy-couch-using-100053/
   - 장면 162 9:57 (6초부터)
53. 4517 Annoyed woman working in a room — https://mixkit.co/free-stock-video/annoyed-woman-working-in-a-room-4517/
   - 장면 164 10:03 (1초부터)
54. 42655 A woman writing in her spiral notebook — https://mixkit.co/free-stock-video/a-woman-writing-in-her-spiral-notebook-42655/
   - 장면 166 10:13 (0초부터); 장면 167 10:14 (1.634초부터, 0.898배속)
55. 41180 Eye of a woman looking at a tablet — https://mixkit.co/free-stock-video/eye-of-a-woman-looking-at-a-tablet-41180/
   - 장면 173 10:32 (1초부터)
56. 4511 Sad girl looking out the window — https://mixkit.co/free-stock-video/sad-girl-looking-out-the-window-4511/
   - 장면 177 10:58 (1초부터)
57. 4656 Couple sitting watching a photo album — https://mixkit.co/free-stock-video/couple-sitting-watching-a-photo-album-4656/
   - 장면 179 11:03 (1초부터)
58. 101233 Girl Hugging Dog — https://mixkit.co/free-stock-video/girl-hugging-dog-101233/
   - 장면 180 11:05 (1초부터)
59. 4644 Photo album opened by a man — https://mixkit.co/free-stock-video/photo-album-opened-by-a-man-4644/
   - 장면 181 11:06 (0.79초부터)
60. 4840 Woman during a sunset on a rooftop — https://mixkit.co/free-stock-video/woman-during-a-sunset-on-a-rooftop-4840/
   - 장면 182 11:10 (1초부터)
61. 52419 The tree branches gently moving with the wind over a clear blue sky and the moon at daytime — https://mixkit.co/free-stock-video/the-tree-branches-gently-moving-with-the-wind-over-a-52419/
   - 장면 183 11:15 (1초부터)
62. 4547 People having a work meeting around a table — https://mixkit.co/free-stock-video/people-having-a-work-meeting-around-a-table-4547/
   - 장면 184 11:19 (1초부터)
63. 1623 People getting into the subway train — https://mixkit.co/free-stock-video/people-getting-into-the-subway-train-1623/
   - 장면 185 11:21 (1초부터)
64. 25592 Young stressed woman with headache — https://mixkit.co/free-stock-video/young-stressed-woman-with-headache-25592/
   - 장면 187 11:26 (1초부터)
65. 100067 A young smiling woman enjoys social media scrolling on her red phone laying on the comfy bed at midnight — https://mixkit.co/free-stock-video/a-young-smiling-woman-enjoys-social-media-scrolling-on-her-100067/
   - 장면 190 11:45 (1초부터)

## 12. AI 사진

RealVisXL V5.0 Lightning(SG161222, openrail++ 라이선스, 상업 이용 가능), scripts/gen_batch.py, 지시문은 ai_images.json. 실존 인물(로라, 연구자)은 그리지 않았고, 사람은 뒷모습만 넣었습니다(B07 뒤쪽의 작은 두 사람은 얼굴을 알아볼 수 없을 만큼 작고 흐림).

1. B01 — 장면 088 5:17 (B01_s1.png): 1952년 영국에서 공개된, 한 흑백 기록 영화 (영사기 스톡 4개가 모두 제한 라이선스)
   - 지시문: vintage 16mm film projector casting a bright beam of light across a dark room, dust in the beam / black and white documentary photo, 1950s, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
2. B02 — 장면 090 5:27 (B02_s1.png), 장면 097 5:56 (B02_s1.png): 로라는 작은 수술을 받기 위해, 8일 동안 병원에 입원 (병동, 사람 없음)
   - 지시문: 1950s hospital children's ward, rows of empty white iron cribs with folded blankets, tall windows, polished floor, no people / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0
3. B07 — 장면 096 5:53 (B07_s1.png): 간호사들 눈에는, 병원 생활에 잘 적응한 아이처럼
   - 지시문: a 1950s nurse in a white uniform and cap walking away down a long hospital ward, seen from behind, iron beds / black and white documentary photo, 1950s Britain, soft natural light, realistic
   - 씨앗 1, 1152x648, 5단계, CFG 1.0

## 13. 운영자 사진

1. bowlby_v2.png — 장면 092 5:36 (bowlby_v2.png): 운영자가 보낸 사진(make_photos_v2.py로 16:9 화면에 맞춤, 커밋하지 않음)
2. ariely_v2.png — 장면 154 9:25 (ariely_v2.png): 운영자가 보낸 사진(make_photos_v2.py로 16:9 화면에 맞춤, 커밋하지 않음)

## 14. 운영자 AI 사진 1 (v3 요청과 함께 보내 주신 29장)

운영자가 직접 만들어 보낸 사진 29장(번호는 대본의 <대사>(번호)). 오른쪽 아래 별 모양 표시를 지우고(scripts/owner_wm_remove.py), 위아래 검은 띠를 잘라 냄(make_photos_v3.py). 커밋하지 않음.

1. 01.png — 장면 014 0:43 "하지만 3시간 4시간이 넘어가면"부터
2. 02.png — 장면 015 0:47 "5분마다 습관처럼"부터, 장면 117 7:21 "이런 분들은"부터, 장면 151 9:16 "6시 30분에 보낸 카톡이"부터
3. 03.png — 장면 019 0:58 "고작 연락 몇 시간 안 된다고"부터, 장면 118 7:24 "단순히 기분만 우울해지는 게 아니라"부터, 장면 169 10:22 "이미 마음이 무겁게 가라앉았다면"부터
4. 04.png — 장면 022 1:09 "원래 인간의 뇌는"부터, 장면 057 3:18 "한마디로 우리의 뇌는"부터
5. 05.png — 장면 026 1:27 "지우는 2주째"부터
6. 06.png — 장면 027 1:29 "오후 6시 30분"부터
7. 07.png — 장면 028 1:32 "휴대폰을 꺼내"부터, 장면 108 6:48 "지우가 줄어들지 않는 숫자 '1'을 보며"부터
8. 08.png — 장면 029 1:35 "집에 도착해 저녁을 먹고"부터
9. 09.png — 장면 031 1:40 "8시가 되자"부터, 장면 178 11:00 "답장 없는 그 사람의 프로필 사진을"부터
10. 10.png — 장면 032 1:46 "그렇게 9시가 되고"부터
11. 11.png — 장면 042 2:24 "지금 여러분은"부터
12. 12.png — 장면 043 2:27 "여러분의 왼쪽 손등에는"부터
13. 13.png — 장면 045 2:34 "눈앞의 큰 화면에"부터, 장면 054 3:00 화면 오른쪽, "아니면 나올지 안 나올지"부터, 장면 058 3:20 "아플지 안 아플지 모르는 상태를"부터, 장면 061 3:34 "이 실험 속 바위와"부터, 장면 065 3:43 "밑에 뱀이 있을지 없을지 모르는 바위를"부터
14. 14.png — 장면 046 2:37 "밑에 뱀이 없는 바위를 골라야 합니다."부터
15. 15.png — 장면 047 2:39 "만약 바위 밑에서 뱀이 나오면"부터, 장면 054 3:00 화면 왼쪽, "뱀이 나와서"부터
16. 16.png — v5에서는 쓰지 않음
17. 17.png — 장면 050 2:49 "긴장할 때 저절로 커지는"부터
18. 18.png — 장면 051 2:52 "손끝에 맺히는"부터
19. 19.png — 장면 052 2:54 "그리고 참가자들이 스스로 매긴"부터
20. 20.png — 장면 071 3:59 "실험에 참가한 학생은"부터
21. 21.png — 장면 081 4:51 "'휴대폰 고장' 같은"부터
22. 22.png — 장면 082 4:53 "내가 말을 재미없게 했나?"부터, 장면 123 7:38 "왜 연락이 없지?"부터
23. 23.png — 장면 089 5:23 "영화의 주인공은"부터, 장면 094 5:43 "입원 첫날"부터
24. 24.png — 장면 091 5:31 "당시 병원들은"부터
25. 25.png — 장면 093 5:39 "엄마와 연락이 완전히 끊긴 채"부터
26. (사진 없음: 대본의 두 번째 (23) 자리에 23번을 다시 씀)
27. 27.png — 장면 095 5:48 "그런데 사흘째가 되자"부터
28. 28.png — 장면 099 6:03 "실제로 간호사가 다정하게 다가와 말을 걸자"부터, 장면 110 6:54 "어릴 적 로라의 마음속에서"부터
29. 29.png — 장면 127 7:49 "나이가 들고 경험이 쌓일수록"부터
30. 30.png — 장면 153 9:22 "휴대폰을 언제 확인할지"부터, 장면 186 11:23 "갑자기 꺼져 버린 휴대폰 배터리 같은"부터

## 15. 운영자 AI 사진 2 (v5)

운영자가 v5 요청과 함께 새로 만들어 보낸 사진 29장(번호는 v5 대본의 <대사>(번호), 14번은 없음, 27번은 두 곳). 오른쪽 아래 별 모양 표시를 지우고(scripts/owner_wm_remove.py), 4번과 21번의 검은 띠를 잘라 냄(make_photos_v5.py). 커밋하지 않음.

1. 01.png — 장면 001 0:00 "금요일 저녁 7시 퇴근길에"부터
2. 02.png — 장면 002 0:02 "당신은 애인에게 카톡을 보냅니다."부터
3. 03.png — 장면 003 0:05 "이 메시지를 보낸 뒤"부터
4. 04.png — 장면 007 0:25 "여러분은 어떤 상황에 가장 마음이 쓰이셨나요?"부터
5. 05.png — 장면 011 0:39 "야근이 길어지나?"부터
6. 06.png — 장면 012 0:40 "배터리가 없나?"부터
7. 07.png — 장면 018 0:55 "그러다 문득"부터
8. 08.png — 장면 021 1:07 "심리학은 아니라고 대답합니다."부터
9. 09.png — 장면 023 1:16 "오늘은 답장이 늦어질 때"부터
10. 10.png — 장면 025 1:24 "3가지 현실적인 방법을"부터
11. 11.png — 장면 036 2:01 "어제 내가 한 그 농담이"부터
12. 12.png — 장면 038 2:07 "그렇게 보낸 3줄의 메시지 옆에"부터
13. 13.png — 장면 044 2:29 "이건 실험 전에"부터
14. (대본에 14번이 없고 사진도 없음)
15. 15.png — 장면 048 2:43 "이 과정을 무려"부터
16. 16.png — 장면 049 2:45 "연구진은"부터
17. 17.png — 장면 056 3:10 "우리 몸의 긴장도는"부터
18. 18.png — 장면 067 3:47 "홀로 들여다보고 있는 셈입니다."부터
19. 19.png — 장면 068 3:48 "게다가 이렇게"부터
20. 20.png — 장면 075 4:17 "장장 8분 동안"부터
21. 21.png — 장면 098 5:58 "아무리 불러도 엄마가 오지 않자"부터
22. 22.png — 장면 121 7:32 "상대의 의도를 알 수 없는"부터
23. 23.png — 장면 126 7:44 "수십 년간"부터
24. 24.png — 장면 135 8:13 "애써 괜찮아라고 본인을 다독이는 대신"부터
25. 25.png — 장면 136 8:16 "차라리 나 지금 불안해라고"부터
26. 26.png — 장면 137 8:19 "2012년 키르칸스키 연구팀은"부터
27. 27.png — 장면 139 8:31 "참가자들에게"부터, 장면 144 8:51 "일주일 뒤"부터
28. 28.png — 장면 148 9:02 "내 감정에 정확한 이름을 붙이는 순간"부터
29. 29.png — 장면 165 10:05 "만약 어떤 상황이 오면"부터
30. 30.png — 장면 170 10:24 "나를 무조건적으로 편안하게 해 주는"부터

## 16. 배경음악 (Mixkit Stock Music Free License, -36 LUFS, 곡이 바뀔 때 3초 겹침)

1. 0:00~1:26 Nield Grohm Hanging 3 / Eugenio Mininni (Mixkit 540, 곡 98초부터, https://mixkit.co/free-stock-music/) — 도입: 답장을 기다리는 조용한 긴장 (World, Disturbing, Percussion, Investigation / Suspenseful, Tension, Mysterious 목록). 낮은 지속음 위에 짧게 뜯거나 두드리는 소리(스펙트로그램으로 본 추정), 드럼 비트 없음(박자 선명도 0.45). D 단조 쪽(+0.10), 중심 892 Hz, 2 kHz 이상 0.004, 1~4 kHz 0.018, 선율 0.13, 타악 0.07, 리듬 흔들림 0.29, 4초 변화 1.6 dB. 189초부터 서서히 작아짐
2. 1:26~2:14 Daniel & Me / Eugenio Mininni (Mixkit 566, 곡 109초부터, https://mixkit.co/free-stock-music/) — 지우의 밤: 어둡고 느린 단조 화음 (Atmospheres, Atmospheric, Meditative, Piano, Synth, Space, Documentary / Science, Documentary 목록). 약 3초마다 화음이 바뀜(스펙트로그램으로 본 추정). E 단조 쪽(+0.16), 중심 372 Hz, 2 kHz 이상 0.000, 1~4 kHz 0.009, 선율 0.07, 타악 0.06, 리듬 흔들림 0.12, 4초 변화 1.9 dB. 이 부분은 5구간(로라)에서 다시 나옴
3. 2:14~3:54 Xanthos / Eugenio Mininni (Mixkit 633, 곡 149초부터, https://mixkit.co/free-stock-music/) — 실험 1 바위와 뱀: 실험실의 낮은 긴장 (Drone Music, Eerie, Sound Effects, Synth, Medical, Space / Tension, Sombre, Science 목록). 지속음과 잘게 떨리는 질감(스펙트로그램으로 본 추정), 박자 없음(박자 선명도 0.27). E 단조 쪽(+0.16), 중심 631 Hz, 2 kHz 이상 0.001, 1~4 kHz 0.022, 선율 0.51, 타악 0.09, 리듬 흔들림 0.27, 4초 변화 2.7 dB. 107~148초에 크게 작아지는 곳이 있어 149초부터. 선율 값은 500~1000 Hz의 긴 지속음 때문(스펙트로그램으로 본 추정)
4. 3:54~5:11 River Flow / Eugenio Mininni (Mixkit 594, 곡 116초부터, https://mixkit.co/free-stock-music/) — 실험 2 문자 실험: 8분의 침묵과 자책, 무겁고 슬픈 긴장 (Electronica, Disturbing, Reflective, Strings, Synth, Cinematic / Sad, Tension, Serious 목록). 현악·신스 깔림과 약한 박동(박자 선명도 0.52). C 단조 쪽(+0.10), 중심 846 Hz, 2 kHz 이상 0.006, 1~4 kHz 0.013, 선율 0.02, 타악 0.07, 리듬 흔들림 0.08, 4초 변화 2.0 dB. 앞 116초는 작다가 커지고 196초 무렵부터 높은 음과 박동 베이스로 밝아져 117~196초만 씀 [v6 시각에 맞춘 조정: offset 117 -> 116.0 s: the part is 79.9 s, the track is usable to 196 s]
5. 5:11~6:59 Daniel & Me / Eugenio Mininni (Mixkit 566, 곡 57초부터, https://mixkit.co/free-stock-music/) — 로라와 애착: 2구간(지우)의 곡을 앞부분부터 다시 씀. 이 구간 끝의 '지우 = 로라와 똑같은 비상벨' 대목에서 지우 장면의 소리가 다시 나오게 함. E 단조 쪽(+0.09), 중심 409 Hz, 2 kHz 이상 0.000, 1~4 kHz 0.012, 선율 0.07, 타악 0.05, 리듬 흔들림 0.13, 4초 변화 4.3 dB. 4초 변화 값은 73~84초(83초에 1초쯤 작아지는 곳)에서 나옴. 94초부터 깊은 저음이 더해짐(소리 크기는 고름)
6. 6:59~7:42 Xanthos / Eugenio Mininni (Mixkit 633, 곡 13.5초부터, https://mixkit.co/free-stock-music/) — 개인차: 3구간 실험실 곡의 앞부분(3구간이 쓰지 않은 14~58초)으로 '연구들을 살펴보면' 대목의 과학 설명 느낌을 이음. 박자 없음(박자 선명도 0.27). F 단조 쪽(+0.24), 중심 682 Hz, 2 kHz 이상 0.003, 1~4 kHz 0.012, 선율 0.23, 타악 0.06, 리듬 흔들림 0.18, 4초 변화 3.5 dB. 61초부터 10초쯤 작아지므로 60초까지 [v6 시각에 맞춘 조정: offset 14 -> 13.5 s: the part is 46.4 s, the track is usable to 60 s]
7. 7:42~9:21 Sonor 07 / Eugenio Mininni (Mixkit 585, 곡 36초부터, https://mixkit.co/free-stock-music/) — 희망과 해결책 1: 어둡지만 따뜻한 희망 (New Age, Reflective, Acoustic Guitar, Synth, Slow, Arthouse, Hopeful / Hopeful, Warm, Documentary 목록). 낮은 베이스와 기타가 천천히 움직임(스펙트로그램으로 본 추정), 드럼 없음. A 단조 쪽(+0.07), 중심 489 Hz, 2 kHz 이상 0.000, 1~4 kHz 0.030, 선율 0.12, 타악 0.03, 리듬 흔들림 0.14, 4초 변화 3.1 dB. 앞 34초의 작은 전주는 건너뜀
8. 9:21~11:10 Voxscape / Eugenio Mininni (Mixkit 571, 곡 99초부터, https://mixkit.co/free-stock-music/) — 해결책 2, 3: 설명을 받쳐 주는 정적인 깔림 (Ambient, Atmospheric, Mystical, Synth, Background / Neutral, Calm, Meditative 목록). 고른 곡 중 가장 고르고 고요함(초당 0.1타). F 장조 쪽(-0.20), 중심 658 Hz, 2 kHz 이상 0.001, 1~4 kHz 0.022, 선율 0.13, 타악 0.05, 리듬 흔들림 0.09, 4초 변화 0.6 dB. 유일하게 장조 쪽이라 해결책 구간에 둠. 앞 55초는 서서히 커지는 전주
9. 11:10~11:51 Sonor 07 / Eugenio Mininni (Mixkit 585, 곡 140초부터, https://mixkit.co/free-stock-music/) — 마무리: 7구간의 곡이 7구간이 쓰지 않은 140초부터 돌아와 따뜻하지만 밝지 않게 맺음 (Hopeful, Warm, Reflective). A 단조 쪽(+0.02), 중심 415 Hz, 2 kHz 이상 0.000, 1~4 kHz 0.006, 선율 0.03, 타악 0.03, 리듬 흔들림 0.13, 4초 변화 2.7 dB. 199초부터 작아짐, 끝 3초 페이드는 bgm_sequence.py가 처리

## 17. 효과음 (Mixkit Sound Effects Free License)

1. 2354 Message pop alert
2. 2357 Bubble pop up alert notification
3. 2365 Electric pop

넣은 자리(sfx_log_v6.json):
1. 0:03 (3.95초) 보냄: 오늘 퇴근하고 뭐할꺼야?
2. 0:18 (18.05초) 받음: 헉 미안해..ㅜ회식 와서 연락을 이제 봤네
3. 1:34 (94.44초) 보냄: 오늘 하루 어땠어요?
4. 1:50 (110.72초) 보냄: 바쁘세요??
5. 2:07 (127.20초) 보냄: 자요..?
6. 2:41 (161.33초) 전기: 손등에 따끔한 전기가

## 부록 A. 사용자 요청 원문 (2026-10-25, 녹음 파일 8개는 빼고 글만)

```
(첫 메시지, 녹음 파일 1~5번 첨부)
녹음본 1~8번까지 내가 속도를 약간 올려서 녹음해왔음. 이 녹음본으로 적용해줘.

(두 번째 메시지, 녹음 파일 6~8번 첨부, 글 없음)
```
