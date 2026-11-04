# 수면 편 영상 v1 기록 (2026-11-04)

사용자께서 보내 주신 대본(../대본_원본.txt, 사진 번호는 ../대본_사진표시.md), AI 사진 49장, 녹음 1개로 만든 첫 영상의 기록입니다.
영상, 녹음, 사진, 스톡 원본, 음악 원본은 올리지 않았습니다.

요청(2026-11-04)
- "대본, 녹음본, ai사진 줄께. 영상 제작 요청 / 대본에서 문장 옆에 적힌 번호가 사진에 매겨진 번호임. 그 사진을 배경화면으로 쓰면 됨"
- 사진은 메시지 세 개(20 + 20 + 9장), 녹음은 따로 한 개("녹음본 줄께", 407.4초).

파일과 순서(작업 폴더 scratchpad/sleep/v1)
1. photo_map.py: 받은 사진 49장 -> 대본 번호. 파일에 번호가 없어서 내용으로 맞춤(사진 목록 ../대본_사진표시.md 5장과 대조).
   - 22번은 받지 못함. 3번과 8번은 두 장씩 옴(03b, 08b): 같은 번호가 다시 나오는 자리에 두 번째 사진을 씀.
2. 별 표시 지우기: 03·04편 도구(wm_remove_v3.py, wm_post.py, wm_choose.py). 이번 사진(1376x768)의 별은 앞 편보다 옅어서
   (가운데 투명도 약 0.30, 04편 약 0.51) 사진들에서 바로 구한 모양은 네모 얼룩을 남김. 03편 2000 크기의 깨끗한 별 모양
   (wm_sheet_2000_alpha.npy)을 줄여 쓰고 세기만 사진마다 맞춤(k 0.48~0.56). 고른 방법은 wm_choose_t.txt(19번은 메움이 어두운
   자국을 남겨 되살림으로 바꿈).
3. make_photos.py: photos_final/PNN.png. 상표 흐림(12번 모니터 상표와 메일 화면 로고, 14번 두 모니터 상표), 메움(16번 문 없는
   오른쪽 끝에 하나 더 그려진 '8 HOURS' 팻말, 19번 졸림 눈금 맨 앞에 하나 더 그려진 '1', 35번 TV 상표). 29번 혈당 측정기의
   작은 지어낸 글자는 영상 크기에서 읽히지 않고 흐림·메움 모두 얼룩이 더 눈에 띄어 그대로 둠.
4. 녹음: rec/rec.wav(48 kHz 모노로만 바꿈, 자르거나 속도를 바꾸지 않음). 0초에 말이 바로 시작하고 파일 끝(407.3초)에서 끝남
   (rec/voice_end.json). 영상 끝 = 목소리 끝 + 3초 = 410.36초.
5. 받아쓰기(faster-whisper large-v3, rec/words.json)와 대본 대조: 녹음은 대본과 글자가 같음.
   - 받아쓰기가 다르게 적은 곳은 음절 모델(w2v_ko)로 대본과 같음을 확인: '잠자리 준비도'(받아쓰기 '그 준비도', 298.2~298.6초에
     '잠자리' 세 음절이 있음), '수면 일정을'(받아쓰기 '수면일을, 일정을', 음절 간격이 고름), 그 밖에 발음대로 적힌 곳
     (앞에/앞의, 세운/새운, 새 집단/세 집단, 코고리/코골이).
6. plan_sleep.py: 문장, 자막 조각, 자리(b 아래, c 가운데, i 가운데 기울임), 화면(P 사진, st 스톡). make_lines.py -> lines.json,
   units.json(자막 276줄, 90문장). 03·04편과 같은 규칙: 숫자는 아라비아 숫자(7시, 6시간, 36명, 30분), 질문·해석·제목·마무리는
   가운데, 따옴표 속 속마음은 가운데 기울임.
   - 22번 자리('열나흘 뒤에는 … 비슷한 수준까지 떨어졌습니다'): 21번을 이어 쓰고 '하룻밤을 꼬박 새운 집단의 성적과'부터 20번
     (밤샘 집단)을 다시 씀. 22번 사진을 받으면 바꿈.
7. run_align.sh -> onsets_v2.json(04편과 같은 도구: align_words.py, onsets.py, ctc_align.py, onsets_v2.py).
8. build_segments.py -> segments.json(장면 105개: 사진 63, 스톡 42), build_spec.py -> spec.json(04편 build_spec_full.py와 같은 방식).
9. 소리: prep_audio.py(목소리 -14 LUFS, 이 녹음은 이미 -14.0 LUFS라 이득 0 dB), bgm_sequence.py(배경음악 5곡, -36 LUFS, 곡마다
   고정 크기, 3초 겹쳐 바꿈, 끝 4초 줄임), mix_audio.py(-14 LUFS, 끝 단계 제한기).
10. build_timeline.py, fit_clips.py, render_parallel.py(3조각, 영상만) + ffmpeg로 소리 합침(AAC 320kbps).

배경음악(Mixkit Stock Music Free License, audio/bgm_segments.json)
- 0:00~0:46.5 Fallen (Asper) / Eugenio Mininni (565): ① 도입(03편 v2에서 사용자가 고른 도입 곡, 04편 도입과 같음)
- 0:46.5~1:50.8 Staring at the Night Sky / Alejandro Magaña (168): ② 평일 오후 메일, ③ 반 동겐 실험
- 1:50.8~3:22.0 Tapis / Eugenio Mininni (615): ④ '괜찮다'의 기준, ⑤ 데프너 실험, ⑥ 해석
- 3:22.0~5:57.4 Miss You / Eugenio Mininni (592): ⑦⑧⑨ 해결책 세 가지
- 5:57.4~끝 Rebecca on the Shore / Eugenio Mininni (545): ⑩ 마무리(곡의 끝이 영상 끝과 맞게 56초부터)

스톡(Mixkit, 모두 라이선스 Free, 2026-11-04 확인. 고른 기록은 stock/picks/group_A·B·C.json, 바꾼 것은 stock_overrides.json)
- st01 9.7초부터 3.5초, Mixkit 914 "Open office space" (2.0초부터): 어제도 그만큼 잤고 / 오늘도 별문제 없이 / 하루를 보냈으니까요. | 상표·글자 자리 흐림
- st02 18.7초부터 1.8초, Mixkit 4827 "Hands of a man typing on a laptop" (0.5초부터): 직장인이 다 그렇지 싶습니다.
- st03 20.5초부터 2.1초, Mixkit 100825 "Sky on a Night to Sunrise Transition" (3.3초부터): 그렇게 평일을 보내고 / 토요일이 됩니다.
- st04 27.6초부터 2.2초, Mixkit 3112 "Interior of a department room" (0.0초부터): 쉬는 날이 아깝지만 / 이렇게 생각합니다. | 바꿈: 고른 4548(밝은 방 소파에 누운 여자, 얼굴 보임)은 주인공의 생각을 말하는 문장에 다른 사람이 나와 헷갈려서, 얼굴 없는 해 질 녘 침실(3112)로
- st05 41.1초부터 5.4초, Mixkit 3111 "Master bedroom and window" (1.0초부터): 오늘은 이 두 가지 질문을 살펴보고 / 잠자는 습관을 바꿔 볼 / 방법 3가지를 / 이야기해 보겠습니다.
- st06 57.2초부터 7.2초, Mixkit 4835 "Office workers hands typing on their devices" (0.5초부터): 그래서 잠이 부족하다는 생각까지는 / 하지 않습니다. / 그런데 잠이 부족해도 / 본인은 그 영향을 / 충분…
- st07 104.4초부터 6.4초, Mixkit 28894 "Hourglass in the dark finishes its count" (3.0초부터): 잠을 줄인 초기에는 졸림이 늘었지만 / 그 뒤로는 검사 성적이 / 계속 나빠지는 동안에도 / 졸림이 크게 늘… | 모래시계에 빛이 가득한 3~10초 쪽을 씀(실제 길이가 짧아 느리게 하지 않음)
- st08 110.8초부터 4.2초, Mixkit 4808 "Silhouette of a man texting during the sunset" (2.0초부터): 이 결과를 생각하면 / 우리가 말하는 “괜찮다”의 기준도 / 돌아볼 필요가 있습니다.
- st09 124.9초부터 8.3초, Mixkit 1808 "Close up shot of a person typing on a laptop" (0.1초부터): 집중이 끊기는 이유는 여러 가지입니다. / 다만 이런 일이 반복된다면 / 직장인은 원래 피곤하지 / 하고 넘…
- st10 133.3초부터 1.7초, Mixkit 3110 "Minimalist room with gray sofa" (0.5초부터): 그러면 이렇게 생각할 수 있습니다.
- st11 137.8초부터 3.6초, Mixkit 3978 "View from a window of the night outside" (0.3초부터): 평일에 덜 잔 만큼 / 주말에 더 자면 / 결국 비슷하지 않을까요?
- st12 171.9초부터 4.8초, Mixkit 3768 "Glucose molecule" (0.5초부터): 혈당을 조절하는 호르몬인 / 인슐린에 몸이 반응하는 정도도 / 실험 전보다 낮아졌습니다. | 흰 바탕이라 전체 밝기를 0.55배로(점검 뒤)
- st13 176.7초부터 6.7초, Mixkit 42896 "Young woman laying on a white soft bed slowly wakes up in the morning" (0.5초부터): 이 연구에서는 / 주말에 잠을 보충하는 것만으로 / 이런 변화를 막지 못했습니다. / 주말에 더 자는 것이 …
- st14 183.4초부터 8.7초, Mixkit 1623 "People getting into the subway train" (5.0초부터): 주말 이후 다시 잠을 줄이는 생활로 / 돌아갔다는 점을 봐야 합니다. / 우리도 주말에 얼마나 잤는지와 함께… | 창 너머 티셔츠 그림(2.2~5.0초)을 건너뛰어 흐림 없이
- st15 195.0초부터 7.0초, Mixkit 42343 "Movement in a city at night in an aerial shot" (13.0초부터): 이런 생각이 반복되면 / 주말의 휴식이 / 평일의 잠을 계속 미루는 이유가 / 될 수 있습니다. / 그렇다면…
- st16 210.0초부터 3.6초, Mixkit 51394 "Woman with insomnia lying in her bed trying to sleep" (1.0초부터): 밤중에 오래 깨어 있었거나 / 낮잠을 잤다면 / 그것도 함께 남겨 보세요.
- st17 213.6초부터 4.1초, Mixkit 28900 "Digital clock in the dark marking midnight" (0.5초부터): 밤마다 시계를 확인하지 말고 / 다음 날 아침 기억나는 범위에서 / 적으면 됩니다.
- st18 222.0초부터 4.0초, Mixkit 42664 "Professional woman working in an office" (0.5초부터): 낮에 유난히 졸렸던 때나 / 집중이 어려웠던 순간도 / 짧게 적어 봅니다. | 상표·글자 자리 흐림
- st19 230.5초부터 4.8초, Mixkit 3213 "Woman falls asleep in her bed" (6.2초부터): 미국 국립보건원은 성인에게 / 대체로 하루 7시간에서 9시간의 / 수면을 권합니다. | 바꿈: 고른 51383은 st16(51394)과 같은 사람이라 두 번 나와서, 다른 사람이 태블릿을 치우고 잠드는 영상(3213)으로
- st20 235.3초부터 7.5초, Mixkit 4433 "Full moon with a soft haze" (5.0초부터): 개인마다 차이는 있지만 / 6시간이면 충분하다고 / 결론 내리기 전에 / 충분히 잘 시간을 꾸준히 / 확보하…
- st21 247.8초부터 3.8초, Mixkit 40734 "Large buildings of a city at dusk" (0.5초부터): 잠을 더 자야 한다는 것을 알아도 / 밤이 되면 이런 마음이 듭니다.
- st22 261.4초부터 5.4초, Mixkit 1711 "A person texting on a smartphone" (0.2초부터): 이때 무조건 휴대폰을 내려놓으라는 말은 / 남은 즐거움마저 / 포기하라는 말처럼 들릴 수 있습니다.
- st23 266.8초부터 4.8초, Mixkit 99910 "Beside a modern laptop the hands write a note on a yellow page notebook with a pen" (6.0초부터): 그래서 잠들 시각만 정하기보다 / 저녁을 어떻게 보낼지도 / 함께 정해 보는 겁니다.
- st24 280.6초부터 4.1초, Mixkit 4948 "Blonde woman reading a book" (0.8초부터): 내가 좋아하는 시간을 보내되 / 하루를 마칠 시점도 / 함께 정하는 겁니다.
- st25 284.7초부터 3.9초, Mixkit 42653 "Woman finishes working on her computer" (3.0초부터): 처음에는 평소보다 30분 먼저 / 저녁 일과를 마무리해 볼 수 있습니다. | 노트북을 닫는 순간(원본 5.9~6.9초)이 장면 끝에 오게; 상표·글자 자리 흐림
- st25b 288.6초부터 5.4초, Mixkit 28885 "Circular clock a very close shot illuminated in the dark" (1.0초부터): 30분만 더 자면 / 충분하다는 뜻은 아닙니다. / 필요한 수면 시간을 / 확보해 가기 위한 첫 단계입니다.
- st26 300.3초부터 3.2초, Mixkit 52255 "A young mother working on a laptop at a tiny desk in the room corner looks on her back to check on her little daughter laying on the bed" (0.4초부터): 야근이나 돌봄으로 / 시간을 조정하기 어려운 날도 있습니다.
- st27 303.5초부터 4.5초, Mixkit 42629 "Checking the calendar on a tablet" (0.5초부터): 그런 상황까지 의지의 문제로 / 돌리지 말고 / 바꿀 수 있는 일정부터 살펴보세요. | 상표·글자 자리 흐림
- st28 312.4초부터 5.8초, Mixkit 100067 "A young smiling woman enjoys social media scrolling on her red phone laying on the comfy bed at midnight" (3.0초부터): 주말에는 늦게 자고 / 늦게 일어나는 생활이 이어지기 쉽습니다. / 이런 변화는 / 수면 리듬을 흔들 수 있…
- st29 326.1초부터 6.8초, Mixkit 39826 "Alarm clock outside, time lapse" (1.0초부터): 미국 국립보건원은 / 평일과 주말의 수면 일정을 / 비슷하게 유지하고 / 그 차이를 대략 1시간 이내로 / …
- st30 332.9초부터 4.8초, Mixkit 4749 "Woman waking up while turning off her alarm clock" (1.2초부터): 다만 이미 잠이 부족한데 / 기상 시각만 맞추려고 / 필요한 잠까지 줄이지는 마세요.
- st31 337.8초부터 5.2초, Mixkit 3208 "Man falls asleep hugging his wife" (0.0초부터): 평일의 수면 시간을 늘리면서 / 주말에도 지나치게 늦게 잠들지 않도록 / 함께 조정하는 겁니다.
- st32 349.0초부터 6.7초, Mixkit 42981 "Loving couple sleeping together at night" (0.0초부터): 충분히 잘 시간을 확보했는데도 / 낮에 심하게 졸리거나 / 큰 코골이와 함께 / 자는 동안 숨이 멎는다는 이… | 바꿈(점검 뒤): 고른 4834(밝은 진료실에서 의사가 카메라를 보며 웃고 말함)는 광고처럼 보이고 문장과 분위기가 달라서, 밤에 함께 자는 두 사람(곁에서 코골이를 알아채는 상황)으로
- st32b 355.7초부터 1.7초, Mixkit 4795 "Young doctor listening through his stethoscope" (0.5초부터): 진료를 받아 볼 필요도 있습니다. | 새로 나눔(점검 뒤): 진료 문장 한 줄만, 청진기로 듣는 의사의 옆얼굴(카메라를 보지 않음)
- st33 357.4초부터 2.3초, Mixkit 31407 "Woman stretching in the morning before starting her day" (0.0초부터): 이제 처음의 토요일로 / 돌아가 보겠습니다.
- st34 361.6초부터 7.7초, Mixkit 41375 "Tour high above a city at dusk" (0.5초부터): 우리는 주말을 또 날렸다고 / 생각하기 쉽습니다. / 하지만 늦게 일어난 자신을 탓하기 전에 / 지난 닷새의…
- st35 369.3초부터 4.4초, Mixkit 39828 "Alarm clock on a table while time flies by" (2.0초부터): 일어날 시간은 정해 둔 채 / 잠들 시간만 계속 뒤로 미루고 / 있지는 않았을까요? | 상표·글자 자리 흐림
- st36 377.3초부터 6.8초, Mixkit 28342 "Slow aerial tour through a mist-covered forest" (3.0초부터): 그 시간은 분명하게 눈에 보입니다. / 하지만 다음 날 어떤 상태로 / 하루를 보내게 될지는 / 그 순간에는…
- st37 384.1초부터 5.0초, Mixkit 402 "Man stands in the shadows" (2.0초부터): 얼마나 오래 깨어 있었는지와 함께 / 어떤 상태로 하루를 보냈는지도 / 돌아보면 좋겠습니다.
- st37b 389.1초부터 6.0초, Mixkit 52452 "Gliding along a quiet asphalt road at dawn, the soft, golden light of the rising sun iluminates the highway." (8.0초부터): 6시간으로도 버틸 만하다는 이유만으로 / 나에게 충분한 잠이라고 / 너무 빨리 결론 내리지는 / 않았으면 합…
- st38 395.1초부터 5.4초, Mixkit 3132 "Time lapse of a small town at night" (0.3초부터): 오늘은 내일 몇 시에 일어날지 정하면서 / 오늘 몇 시부터 하루를 마무리할지도 / 함께 정해 보세요.
- st39 400.6초부터 9.8초, Mixkit 4148 "Milky way seen at night" (1.0초부터): 여러분은 평일과 주말에 / 자는 시간이 얼마나 다른가요? / 잠자는 습관을 바꾸고 / 달라진 경험이 있다면 …

점검
- (렌더링 중. 점검 결과는 렌더링 뒤에 적음)
