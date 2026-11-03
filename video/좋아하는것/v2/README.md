# 04편 「좋아하는 것」 전체 영상 v2 기록 (2026-11-02)

부분 영상 v1(사진 50번까지)에 사진 51~76번과 나머지 녹음(2편 44.2초부터, 3편 전체)을 더해 만든 전체 영상의 기록입니다.
영상, 녹음, 사진, 스톡 원본, 음악 원본은 올리지 않았습니다. v1 기록은 ../v1/README.md.

요청(2026-11-02)
- "50번부터 사진 이어서 줄께" (메시지 3개, 11장 + 10장 + 6장 = 27장)
- 앞선 요청: "일단 50번까지 ai 사진 없는 건 스톡에서 영상 가져와서 사진 50번까지만 영상 만들어줘. (그 뒤는 내가 내일 주겠음)"

파일과 순서(작업 폴더 scratchpad/ep4/v1에서. v1 파일은 그대로 두고 _full, 2가 붙은 이름으로 새로 만듦)
1. photo_map2.py: 받은 순서(in51~in77) -> 대본 번호 51~76. in54는 in53(53번, 엄지 든 손과 새 그림)과 같은 사진이 한 번 더 온
   것이라 쓰지 않음.
2. 별 표시 지우기: 같은 도구(wm_remove_v3.py, wm_post.py, wm_choose.py). 새 사진은 크기가 달라(2752x1536 17장, 1376x768 10장)
   별 투명도를 새 사진들에서 다시 구함. 남은 자국: 56번(밝고 어두운 경계)은 wm_dir.py, 59·60·72번은 wm_patchfill.py.
   (wm_bh.py는 이 크기에서 별 모양 얼룩을 만들어서 쓰지 않음. 나머지는 아주 강하게 대비를 올려야 보이는 정도라 그대로 둠)
3. make_photos2.py: photos_final/P51~P76.png, 상표·로고 4곳 흐림(60·61번 모니터 작업 표시줄, 67번 기타 케이스의 필기체 글자,
   74번 헤드폰 머리띠 글자).
4. join_full.py: 1편 + 쉼 0.20초 + 2편 전체 + 쉼 0.27초 + 3편 전체 + 끝 무음 3초 -> rec_full.wav, join_full.json
   (자르거나 속도를 바꾸지 않음. 이은 자리의 쉼은 둘 다 약 0.47초로 이 녹음의 가장 긴 쉼과 비슷함)
5. plan_full.py: v1 문장과 조각은 그대로, 뒤에 2편 44.2초부터와 3편을 더함 -> lines_full.json, units_full.json (자막 460줄).
   11초가 넘는 스톡 구간 중 내용이 바뀌는 4곳은 둘로 나눔(st18b, st43b, st47b, st51b).
6. run_align_full.sh -> onsets_v2_full.json (v1과 같은 도구). 앞 185줄은 v1과 시각이 같음(차이 2ms 이하).
7. build_segments_full.py -> segments_full.json, build_spec_full.py -> spec_full.json
8. audio/bgm_segments_full.json: 배경음악 7곡(-36 LUFS, 곡마다 고정 크기), prep_audio.py(목소리 -14 LUFS), mix_audio.py
9. build_timeline.py, fit_clips.py, render_parallel.py(3조각, 영상만) + ffmpeg로 소리 합침(AAC 320kbps)

녹음과 대본(2편 44.2초부터와 3편. 사용자가 보낸 대본과 다르게 읽힌 곳은 녹음대로 자막을 씀)
- "나도 한번 그려 보고 싶어졌다고 생각해 보겠습니다" -> 녹음 "싶어졌다고 해 보겠습니다"
- "자라기 시작한 관심을 지키는 방법입니다" -> 녹음 "지키는 데 관한 것입니다" ('잘하기'와 비슷하게 들리지만 뜻으로 '자라기')
- "악기를 연주한 것도" -> 녹음 "악기를 연주한 시간도"
- 녹음에만 있는 6문장(표시 없음 -> 스톡): "예를 들어 오늘은 10분 동안 마음에 드는 색을 써 보고 그 종이는 그대로 덮어 두는 겁니다. /
  끝난 뒤 잘했는지보다 어떤 색을 고를 때 좋았는지 떠올려 보세요. / 10분은 정답이 아니라 남의 반응 없이 해 볼 시간을 정하기 위한
  예시입니다. / 혼자만 즐기라는 뜻은 아닙니다. / 친구와 함께하는 시간이 좋다면 그것도 내 취미의 중요한 즐거움입니다. /
  다만 다른 사람이 반응하지 않는 날에도 내가 좋아했던 부분을 알아볼 수 있었으면 합니다."
- "즉, 취미가 있다는 것은 ... 알고 있다는 말이죠" -> 녹음 "취미가 있다는 것은 ... 알고 있다는 말일 수도 있겠습니다."
- "뛰어난 사람만은 아닙니다" -> 녹음 "아니었습니다"
- "처음 시도한 날과" -> 녹음 "처음 골라 보던 날과"
- 녹음에만 있는 3문장(표시 없음 -> 스톡): "취미를 묻는 말에 꼭 완성된 대답을 준비할 필요도 없겠습니다. / 요즘은 이것을 조금씩 해 보고
  있어요. / 그 정도의 대답으로도 지금의 나를 충분히 이야기할 수 있습니다."
- "점점 좋아진 취미가 있나요?" -> 녹음 "점점 좋아진 활동이 있나요?"
- "여러분들의 취미를 댓글로 공유해 주세요." -> 녹음 "여러분들만의 경험이 있다면 댓글로 공유해 주세요."
- 숫자는 자막에 아라비아 숫자(일흔여덟 명 -> 78명, A그룹, B그룹).

배경음악(Mixkit Stock Music Free License, 곡마다 고정 크기, 배경음악 전체 -36 LUFS, 곡 사이 3초 겹쳐 바꿈, 끝 4초 줄임)
- 0:00~1:12.3 Fallen (Asper) / Eugenio Mininni (565): ① 도입 (v1과 같음)
- 1:12.3~1:59.5 Classical 7 / Jonny S. (714): ② 주말 오후와 그림 장면 (v1과 같음)
- 1:59.5~3:30.8 Tapis / Eugenio Mininni (615): ③ 블랙홀 실험 (v1과 같음)
- 3:30.8~5:06.2 Staring at the Night Sky / Alejandro Magaña (168): ④ 상 실험과 해석
- 5:06.2~7:14.3 Forest Mist Whispers / Alejandro Magaña (148): ⑤ 호출기 실험과 그림 예시 (차분한 다큐 느낌, 크기 변화가 작음)
- 7:14.3~9:50.6 Miss You / Eugenio Mininni (592): ⑥ 해결책 세 가지 (희망적이고 차분함)
- 9:50.6~끝 Rebecca on the Shore / Eugenio Mininni (545): ⑦ 마무리 (곡의 끝이 영상 끝과 맞음)

스톡(Mixkit, 모두 라이선스 Free, 2026-11-02~03 확인. 고른 기록은 stock/picks/group_C·D·E.json, 앞부분 st01~st17은 v1과 같음)
- st18 262.3초부터 8.9초, Mixkit 43350 "Little girl drawing with her father in front" (1.0초부터): 상을 받은 아이들이 / 더 자주 그림을 그렸을까요? / 놀랍게도 미리 상 | 상표·글자 자리 흐림
- st18b 271.2초부터 5.5초, Mixkit 44849 "A girl's hands embellishing a Valentine's Day card" (1.5초부터): 똑같이 상을 받았어도 / 예상하지 못한 상을 받은 / B그룹에서는 / 그 | 상표·글자 자리 흐림
- st19 276.8초부터 11.1초, Mixkit 43353 "Young father working alongside his daughter" (7.0초부터): 이 연구는 과잉정당화 효과를 / 보여 주는 대표적인 사례입니다. / 원래 | 상표·글자 자리 흐림
- st20 287.8초부터 10.2초, Mixkit 100467 "Painter's Hand Softly Brushing a Canvas" (0.2초부터): 이 장면을 보며 우리 취미에도 / 질문 하나를 가져와 볼 수 있습니다. 
- st21 300.7초부터 5.5초, Mixkit 100483 "Finished Still Life Painting on an Easel" (0.5초부터): 다만 그 이유만 남는다면 / 아무도 봐 주지 않는 날에는 / 다시 시작할
- st22 306.2초부터 9.1초, Mixkit 4726 "Drunk young man watching television" (2.0초부터): 그런데 평가를 내려놓고 / 자유시간까지 생겼는데도 / 무엇을 해야 즐거울
- st23 353.8초부터 6.0초, Mixkit 44588 "A person turning up the volume on the TV" (1.6초부터): 일에서 벗어나 자유롭게 / 시간을 보내고 싶은 마음과 / 실제로 몰입하는 | 상표·글자 자리 흐림
- st24 359.9초부터 8.9초, Mixkit 772 "Wood lathe in action" (0.5초부터): 취미를 찾을 때도 여기서 / 한 가지 질문을 가져와 볼 수 있습니다. /
- st25 376.9초부터 8.3초, Mixkit 41199 "Young man browsing the Internet with a tablet" (0.3초부터): 그럴 때는 머릿속으로 / 잘 맞을 취미를 고르는 것만으로는 / 답을 찾기
- st26 402.8초부터 11.2초, Mixkit 41603 "Focus on the hand of an artist girl painting with watercolor" (2.5초부터): 시작하기 전에는 / 그저 그림을 그려 보고 싶었습니다. / 해 보고 나니 | 상표·글자 자리 흐림
- st27 414.0초부터 16.0초, Mixkit 2851 "A person sowing a seed" (9.8초부터): 이런 경험이 쌓이면서 / 막연했던 관심은 / 조금씩 구체적인 취향이 되어
- st28 439.0초부터 4.5초, Mixkit 42189 "Hands of a girl putting together the edge of a puzzle" (7.0초부터): 처음이 매끄럽지 않았다는 사실만으로 / 나와 맞지 않는다고 / 결론 내릴
- st29 448.2초부터 4.2초, Mixkit 265 "Guy texting at sunset" (8.5초부터): 사진이 궁금하다면 / 지금 쓰는 휴대폰으로 / 마음에 드는 빛을 찍어 볼
- st30 460.1초부터 6.3초, Mixkit 43432 "Painting a picture with a palette knife" (3.0초부터): 색을 고를 때는 좋았는데 / 얼굴을 똑같이 그리는 게 답답했다면 / 다음
- st31 466.4초부터 6.0초, Mixkit 4793 "Happy young man writing with pen and paper" (0.0초부터): 좋았던 순간을 알아내면 / 다음 시도에 남길 것이 생깁니다. / 불편했던
- st32 472.4초부터 8.0초, Mixkit 649 "Man packing his saxophone" (6.5초부터): 여러 번 해 봐도 / 마음이 가지 않는다면 / 다른 활동으로 옮겨 가도  | 상표·글자 자리 흐림
- st33 480.5초부터 6.7초, Mixkit 39846 "Trash basket of an office with paper balls" (0.0초부터): 하지만 다시 해 볼 마음이 생겨도 / 매번 너무 어렵다면 / 금세 지치기 | 속도 0.86
- st34 487.1초부터 4.0초, Mixkit 50917 "A young man firmly grips the training climbing wall" (0.0초부터): 둘째. / 지금 할 수 있는 것보다 / 조금만 어려운 목표를 만들어 보세
- st35 507.8초부터 7.4초, Mixkit 42824 "Skillful guitarist playing a black guitar" (0.2초부터): 오늘은 두 코드를 바꿀 때 / 소리가 끊기지 않게 해 보는 겁니다. / 
- st36 515.2초부터 9.4초, Mixkit 44140 "Close view of a keyboard player's hands playing" (1.0초부터): 해 보니 여전히 어렵다면 / 더 쉬운 부분으로 바꿔 보세요. / 이미 너
- st37 524.6초부터 4.5초, Mixkit 50299 "Long-Haired Guitarist Tuning Electric Guitar in Store" (0.0초부터): 어제는 구분하지 못했던 소리가 들리거나 / 전에는 놓쳤던 모양이 / 보일 | 상표·글자 자리 흐림
- st38 529.1초부터 8.8초, Mixkit 42843 "Playing chords on the electric guitar in the dark" (1.0초부터): 처음부터 큰 열정이 없어도 / 이런 작은 궁금증을 / 따라가 볼 수 있습
- st39 537.9초부터 4.9초, Mixkit 4838 "Photographing a delicious dessert" (5.0초부터): 그런데 작은 진전이 생기면 / 또다시 남에게 보여 줄 결과에만 / 마음이 | 상표·글자 자리 흐림
- st40 542.8초부터 7.6초, Mixkit 808 "Steaming mug" (0.0초부터): 마지막 방법은 / 그렇게 자라기 시작한 관심을 / 지키는 데 관한 것입니
- st41 555.9초부터 3.8초, Mixkit 41709 "Violinist carefully removing his violin from its case" (0.6초부터): 취미에서도 내가 무엇을 기대하며 / 시작하는지 살펴볼 수 있겠습니다.
- st42 562.8초부터 3.7초, Mixkit 44161 "Close view of a musician playing a Spanish guitar" (0.0초부터): 악기를 연주한 시간도 / 녹음해서 누군가에게 / 들려줄 필요는 없죠.
- st43 566.5초부터 4.9초, Mixkit 41602 "Hand of a woman painting with watercolors" (5.0초부터): 예를 들어 오늘은 10분 동안 / 마음에 드는 색을 써 보고 / 그 종이
- st43b 571.4초부터 8.3초, Mixkit 5257 "Mixing colors in a paint palette" (0.5초부터): 끝난 뒤 잘했는지보다 / 어떤 색을 고를 때 좋았는지 / 떠올려 보세요.
- st44 579.7초부터 6.0초, Mixkit 3272 "Amateur band playing rock" (1.0초부터): 혼자만 즐기라는 뜻은 아닙니다. / 친구와 함께하는 시간이 좋다면 / 그 | 상표·글자 자리 흐림
- st45 585.8초부터 4.9초, Mixkit 100473 "Artist Working on a Painting" (2.0초부터): 다만 다른 사람이 반응하지 않는 날에도 / 내가 좋아했던 부분을 / 알아
- st46 590.6초부터 5.1초, Mixkit 43935 "Demonstration video of a steaming cup of coffee" (0.3초부터): 취미가 있다는 것은 / 내가 어떤 시간을 좋아하는지 / 조금 더 알고 있
- st47 595.7초부터 4.7초, Mixkit 44135 "Talented drummer playing in a close shot" (0.5초부터): 생각해 보면 우리가 부러워했던 사람은 / 꼭 취미 실력이 뛰어난 사람만은
- st47b 600.4초부터 7.2초, Mixkit 41846 "Two friends chatting happily" (0.5초부터): 다음 주말에 무엇을 할지 이야기할 때 / 표정이 밝아지는 사람 / 별것 
- st48 607.7초부터 11.7초, Mixkit 4409 "Modern buildings at dusk" (7.0초부터): 그런 마음이 언제부터 생겼는지는 / 겉으로 잘 보이지 않습니다. / 지금 | 상표·글자 자리 흐림
- st49 626.8초부터 8.0초, Mixkit 41059 "Two mountaineers putting away their things during the sunset" (0.5초부터): 물론 모든 활동을 오래 붙잡는다고 / 좋아하게 되는 것은 아닙니다. / 
- st50 634.8초부터 4.0초, Mixkit 43735 "Portrait of a man breathing while meditating" (0.3초부터): 관심을 키운다는 것은 / 내 마음을 무시한 채 / 버틴다는 뜻이 아니니까
- st51 638.7초부터 5.9초, Mixkit 39845 "Man in an office throws a ball of paper into the trash can" (0.5초부터): 다만 작은 관심이 생겼을 때 / 아직 잘하지 못한다는 이유로 / 너무 빨 | 속도 0.8
- st51b 644.6초부터 5.4초, Mixkit 1780 "Watering a flower pot" (0.0초부터): 무엇이 좋았는지 살펴보고 / 나에게 맞는 방식을 바꿔 가며 / 조금 더 
- st52 650.0초부터 9.3초, Mixkit 43264 "Person stirring latte art in a cup" (0.0초부터): 취미를 묻는 말에 / 꼭 완성된 대답을 준비할 필요도 / 없겠습니다. / | 속도 0.8
- st53 659.3초부터 7.6초, Mixkit 1086 "Sunrise on the ocean" (0.5초부터): 좋아하는 마음이 분명해진 뒤에만 / 시작할 수 있는 것은 아닙니다. / 
- st54 667.0초부터 9.7초, Mixkit 3977 "View of a window with a curtain" (0.3초부터): 여러분에게도 처음에는 / 별생각 없이 시작했다가 / 점점 좋아진 활동이 
- 고르는 기준(v1과 같음): 대사를 그대로 보여 주는 장면, 어둡고 따뜻한 밤 실내 느낌, 주인공 대신 나오는 사람은 손·뒷모습 위주,
  글자와 상표가 없을 것(있으면 흐림 상자). 무료(Free) 라이선스만 쓰고 Restricted는 쓰지 않음.
- 무료 클립이 없어 가까운 장면으로 대신한 곳: st19(트로피·메달·스티커 클립이 모두 Restricted -> 아빠가 아이 그림을 크게 칭찬하는
  장면, 가운데 자막 밑이라 흐림), st28(지우개·구긴 종이 -> 퍼즐 조각을 맞춰 보는 손), st29(휴대폰으로 사진 찍기 -> 노을빛에 휴대폰을
  든 손), st33(답답한 표정 -> 구긴 종이가 가득한 휴지통).
- 같은 촬영에서 나온 클립이 두 번 나오는 곳: st33(휴지통)과 st51(종이를 휴지통에 던지는 사람), st20·st21(화실)과 st45(같은 화실),
  st26과 st43(같은 수채화 촬영). 장면 내용은 서로 다름.
- st52는 도입부 카페 장면(st01·st02)에 쓴 라테 영상을 다시 씀(취미를 묻는 대답으로 돌아오는 장면).

결과(2026-11-03)
- 04_좋아하는것_v2_전체.mp4: 1920x1080, 30fps, H.264 + AAC 320kbps 48kHz 스테레오, 11분 16.6초(20,299프레임), 384MB,
  -14.0 LUFS, 최고 -1.5 dBFS. 운영자 목소리와 사용자 사진이 들어 있어 저장소에 올리지 않고 SendUserFile로 전달.
- 장면 135개(사진 77장면: 사진 75장, 52·57번은 대본 표시대로 두 번씩 / 스톡 58장면), 자막 460줄.
- 렌더링: 앞 3분의 1(0:00~3:47)은 스톡을 고르는 동안 먼저 만들고, 나머지 두 조각을 나중에 만들어 다시 인코딩하지 않고 이어 붙임
  (앞 조각의 장면 60개와 자막 166줄이 최종 명세와 같음을 확인).
- 점검: 스톡 41곳을 실제 화면(색, 흐림, 자막)으로 뽑아 봄(checkframes.py). 완성본에서 15곳(사진 51~76번 자리, 끝 장면)을 뽑아
  사진과 자막이 맞는지, 별 표시가 남지 않았는지 봄. 곡이 바뀌는 자리의 음악 크기는 v1과 같은 방식(3초 겹침)임을 확인.
- 남은 일: '싫어진 걸까요'(3:08, 녹음은 '쉬워진'으로 들림)를 다시 녹음해 주시면 그 자리만 바꿔 넣음.
