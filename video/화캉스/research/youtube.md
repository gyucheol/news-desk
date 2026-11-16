# 화캉스: which related YouTube videos did well, and how they were made

Research date: 2026-11-03 (UTC). Prepared for the "INFJ입니다." topic 회사 '화캉스'. This covers YouTube benchmarks only; it proposes no angles.

## 0. Method (owner's rules followed)

- **Discovery:** WebSearch only, filtered to youtube.com. About 60 Korean phrasings, including every phrasing the owner listed: 화캉스, 회사 화장실, 직장인 화장실, 화장실에서 휴대폰, 화장실 핸드폰 직장인, 회사 화장실 꽉 참, 아침 9시 화장실, 출근하자마자 화장실, 월급루팡 화장실, 화장실 칸 직장인 공감, 회사 화장실 몰래, 화장실 휴식, 장 트러블 출근, 주식 화장실, 직장인 공감 숏츠 화장실, 숏박스 회사, 직장인 상황극 화장실, and others. Comedy and news/explainer variants were included, plus a few English queries (phone on the toilet, "bathroom camping") for comparison. No youtube.com page was fetched. There was no comment scraping and no thumbnail download.
- **Numbers:** taken only from `node video/tools/youtube_views.js`. **105 videos were checked, and all 105 returned a viewCount.** Raw output is in `/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/hwacance/yt/raw/batch0.jsonl` … `batch3.jsonl` and `/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/hwacance/yt/raw/all_checked.json`. The checker cuts titles that contain an escaped quote. For those 13 videos, the full title in the table comes from the search result or the metadata page. The numbers are unchanged.
- **Duration, description and tags (24 videos):** read with my own read-only Playwright script, `/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/hwacance/yt/scripts/meta.js`, on the mattw.io page. The script aborts every request to youtube.com, youtu.be, ytimg.com and googlevideo.com. Its log confirms those hosts were never contacted. View counts in this file still come only from the checker.
- **Captions:** fetched from yt-to-text.com one request at a time, with a 7-second pause between requests. **There were 12 requests for 12 videos, which is the cap.** 9 returned transcripts. 3 returned HTTP 403 with `{"code":"NO_SUBTITLES"}`. That is a no-captions answer, not a block: the request right after the first one succeeded. No block or rate limit was seen. Caption text was treated as data only. Transcripts are saved in `/tmp/claude-0/-home-user-news-desk/6ce83ec0-0608-598d-bae7-3d2c42c6eb05/scratchpad/hwacance/yt/captions/<id>/caption.json`. Auto-captions contain speech-recognition errors, so quotes below are lightly corrected where the word was obvious; these are marked "(ASR)".
- **Threshold:** long-form must have at least 500,000 views; Shorts at least 1,000,000. Format comes from the search-result URL (`/shorts/`) or the duration read.
  - "≤60 s, watch URL" means a video that cannot be told apart from a Short through the API. Every such video here has at least 1M views, so it qualifies under either rule.
  - "long-form?" means a watch URL whose duration was not read. None of these is in the 500K–1M zone where the format would change the verdict.
  - One borderline case is KNN `4TOxizhmGF4`: 2:02 long, posted after Shorts were allowed up to 3 minutes, with 801K views. It qualifies as long-form but would not as a Short.
- **Limits:**
  - The shared web-search budget (200 calls per turn across all agents) ran out before 3 last queries: office-bathroom skits from big comedy channels such as 웃소, plus "화장실 가는 척 쉬는 직원". An earlier search of 숏박스's catalogue found no bathroom sketch.
  - Search-engine coverage of YouTube is partial. A video missing from this list is not proof that it does not exist.

## 1. Every video checked with the tool (105: 90 Korean, 15 international)

Views, publish date (UTC) and check time come from `youtube_views.js` output. **Meets?** applies the owner's threshold.

- **Format column:** "Shorts (URL)" means the search result was a `/shorts/` link and the duration was not read. "long-form?" means a watch link whose duration was not read.
- **Framing column:** my one-line classification. "ADJACENT" marks a video about rest or breaks rather than the bathroom.
- **Captions column:** fetched, no subtitles, or not requested (shown for qualifiers only).

**Totals:** 20 meet the threshold: 19 Korean and 1 international (SNL). KNN `4TOxizhmGF4` meets it only under the long-form rule.

### 1a. Korean videos (sorted by views)

| # | Title | Channel | ID | Format (duration) | Views | Published | Checked (UTC) | Meets? | Framing | Captions |
|---|---|---|---|---|---:|---|---|---|---|---|
| 1 | 화장실 공감 만화 | 소맥거핀 | `tsz0xe26Bho` | long-form (1:42) | 23,662,189 | 2021-06-23 | 2026-11-03 23:21 | **yes** | animation: relatable bathroom gags (MapleStory-style '병맛' cartoon, BGM only per description; no subtitles) | no subtitles |
| 2 | Toilet Awkward Situation 화장실 난감한 상황 #shorts | ODS | `1aI0bggfa54` | Shorts (0:16) | 14,982,361 | 2025-07-01 | 2026-11-03 23:25 | **yes** | wordless cartoon Short: one awkward toilet moment (not office) | not requested |
| 3 | 실패 없는 화캉스 공식? 브레프 디럭스! | Henkel Consumer Brand Korea | `oet-Xb6JCjI` | ≤60 s, watch URL (0:31) | 11,496,209 | 2025-08-22 | 2026-11-03 23:22 | **yes** | brand ad (Henkel Bref toilet freshener) built on the word 화캉스; views likely ad-driven (same ad as a Short: 135K) | fetched |
| 4 | 아뿔싸 화장실이 만석이다. (그런 당신을 위한 괄약근 댄스) | 빵쏭bbangsong | `5DJvA_1RjdA` | long-form (2:09) | 9,228,555 | 2022-02-09 | 2026-11-03 23:24 | **yes** | original comic song + animation: stuck on a highway bus, every rest-stop stall full | fetched |
| 5 | "일상 공감" 시리즈 몰아보기 | 소맥거핀 | `jXamLDR0roQ` | long-form (51:54) | 5,292,580 | 2026-09-25 | 2026-11-03 23:25 | **yes** | animation compilation of the channel's '일상 공감' series | not requested |
| 6 | [스튜디오 장삐쭈] 화장실 | 장삐쭈 | `qN48B8YDpwM` | ≤60 s, watch URL (1:00) | 4,742,317 | 2022-12-20 | 2026-11-03 23:25 | **yes** | 60-s animated office sketch: the studio's single bathroom (sign, light, knocking rules) | fetched |
| 7 | 화장실을 위한 첫 번째 럭셔리 향수, 브레프 디럭스! | Henkel Consumer Brand Korea | `A4-oaCy7jWc` | ≤60 s, watch URL (0:41) | 4,596,585 | 2021-07-21 | 2026-11-03 23:25 | **yes** | brand ad (Henkel Bref, 2021), bathroom as luxury space; not 화캉스 | not requested |
| 8 | 허름한 화장실에만 줄을 선 이유 | 노후웃음 | `HH41iRNdm4I` | Shorts (0:47) | 2,813,899 | 2026-02-27 | 2026-11-03 23:31 | **yes** | story Short, senior humor: only the shabby toilet has a line; graffiti twist | not requested |
| 9 | 급똥 애니메이션 몰아보기 | 키에커 | `Rm_CDiTqHi4` | long-form (40:49) | 2,380,418 | 2026-01-17 | 2026-11-03 23:25 | **yes** | animation compilation: urgent-poop episodes (incl. '여자들의 화장실 심리전') | not requested |
| 10 | '남자 급똥' (급똥 마려울 때) -홍팸 | 홍팸 | `YPjS2RAl1x8` | long-form (5:51) | 1,871,523 | 2024-03-16 | 2026-11-03 23:23 | **yes** | live-action sketch: obstacle chain on the way to a toilet (proselytizer, friend, grandma, zipper) | fetched |
| 11 | 여자 화장실의 민낯 | 99.9도 | `iW-tdqKf9Nc` | long-form (4:49) | 1,421,936 | 2025-11-30 | 2026-11-03 23:23 | **yes** | near-wordless live-action sketch: '여자화장실 특' montage | fetched |
| 12 | 아무리 쉬어도 피곤한 당신에게. 뇌를 회복시키는 '진짜' 휴식법 | 뇌과학 쓸래요? | `k1UFksi3-2g` | long-form (6:46) | 1,410,820 | 2026-03-09 | 2026-11-03 23:32 | **yes** | psychology/neuroscience explainer on rest (ADJACENT: calls short-form scrolling fake rest) | fetched |
| 13 | 운행 중 갑자기 배가 아프다. 철도 기관사는 화장실 어떻게 해결하는지 봤더니｜화장실 전쟁｜다큐프라임｜#골라듄다큐 | EBSDocumentary (EBS 다큐) | `OnwnPqyZC5w` | long-form (11:06) | 1,339,319 | 2025-12-20 | 2026-11-03 23:22 | **yes** | TV documentary excerpt: train drivers who cannot get to a toilet at work (EBS 다큐프라임) | fetched |
| 14 | 잠보다 강력하다! 뇌를 회복시키는 진짜 휴식 루틴, 딱 5분만 해보세요 ｜ 직장인 스트레스 번아웃 ｜ 인생질문 290회 | 세바시 인생질문 | `9rHpeKlCPTA` | long-form (20:50) | 1,152,669 | 2025-05-20 | 2026-11-03 23:26 | **yes** | psychiatrist interview on rest (ADJACENT: guilt about resting, scrolling, micro-breaks) | fetched |
| 15 | [SNS 시트콤]  쾌한상사  '제1화 화장실 습격사건' | pasteurkorea | `PcK-zmezH2Y` | long-form (7:45) | 1,151,714 | 2013-07-11 | 2026-11-03 23:21 | **yes** | branded office sitcom (Pasteur 쾌변 yogurt), office workers and the bathroom, 2013; no subtitles | no subtitles |
| 16 | 남자들이 유일하게 오래 걸리는곳 | 유머너굴 | `pqdCtJP9luE` | Shorts (0:18) | 1,078,051 | 2026-09-30 | 2026-11-03 23:22 | **yes** | couple-relatable Short: husband vanishes into the bathroom, comes out with his phone | no subtitles |
| 17 | "점심시간, 5분 거리 집에서 쉬다 오는 게 잘못인가요?" / SBS / 뉴스딱 | SBS 뉴스 | `lKM5l2Z-CLk` | long-form (1:21) | 1,002,757 | 2023-03-06 | 2026-11-03 23:32 | **yes** | news (뉴스딱): community-post dilemma, resting at home during lunch, boss objects | not requested |
| 18 | "퇴근 전 저녁 먹다 들켰는데…담배타임 더 길지 않나요?" / SBS / 뉴스딱 | SBS 뉴스 | `sURBM42ynXE` | long-form (1:33) | 930,524 | 2023-07-04 | 2026-11-03 23:31 | **yes** | news (뉴스딱): Blind post, non-smoker caught eating vs. smokers' breaks | not requested |
| 19 | 남성 공무원이 받은 황당 메일 "점심 시간에 쉬어야 해서...보건실 사용 자제 부탁" / KNN | KNN NEWS | `4TOxizhmGF4` | long-form (2:02) | 801,320 | 2024-12-12 | 2026-11-03 23:32 | yes* (long-form rule; if it is a ≤3-min Short: no) | news: notice asking male civil servants not to use the 보건실 at lunch (rest-space fairness) | not requested |
| 20 | "그냥 놀겠다는 거지"…직장인 '담배 타임' 갑론을박 / SBS / 모아보는 뉴스 | SBS 뉴스 | `I6wa-zZJ9qM` | long-form (4:46) | 301,677 | 2024-05-12 | 2026-11-03 23:31 | no | news compilation: are smoke/coffee breaks work time? (labor ministry Q&A) |  |
| 21 | 방귀소리 대처법. 화장실 똥쌀때 유형별 특징. 방귀뀌는 유형.. | 마짱TV | `-4AO2N0O33A` | long-form? (watch URL; duration not read) | 227,086 | 2019-06-28 | 2026-11-03 23:31 | no | talk/comedy '유형' video: bathroom noise and fart etiquette |  |
| 22 | 식중독 배탈! 전쟁 같은 화장실 쟁탈전 급똥 Bathroom toilet battle Poop #shorts | B-House 비하우스 | `9j-gvKN6lMY` | Shorts (URL) | 164,470 | 2023-03-30 | 2026-11-03 23:31 | no | sketch Short: fight over the only toilet (food poisoning) |  |
| 23 | 실패 없는 화캉스 공식? 브레프 디럭스! | Henkel Consumer Brand Korea | `S2GTqlusosc` | Shorts (0:31) | 135,076 | 2025-08-26 | 2026-11-03 23:25 | no | brand ad (same 31-s 화캉스 Bref ad uploaded as a Short) |  |
| 24 | 서점이 똥스팟인 사람들이 있다? /스브스뉴스 | 스브스뉴스 SUBUSUNEWS | `xbEtw5dhdZY` | long-form? (watch URL; duration not read) | 117,134 | 2019-03-17 | 2026-11-03 23:22 | no | news explainer (스브스뉴스): bookstores trigger the urge to poop |  |
| 25 | 남자라면 화장실에서 꼭 경험해 본 적 있는 상황! | 이런 사이다 | `MadQlO-ocDo` | long-form? (watch URL; duration not read) | 106,010 | 2022-10-27 | 2026-11-03 23:23 | no | relatable sketch: men's room situations |  |
| 26 | 회사 화장실에서 뒷담 까다 걸린 직원들 참교육 하기😎 ｜ #다시보는김비서 | tvN D ENT | `h-ZPuPWia0o` | long-form? (watch URL; duration not read) | 84,760 | 2020-03-24 | 2026-11-03 23:21 | no | drama clip (김비서가 왜 그럴까): gossip in the office bathroom backfires |  |
| 27 | 자연스럽게 직장에서 잠자는 연기 [실용연기학원] | 김해준 | `x1wtUCsIICY` | long-form? (watch URL; duration not read) | 77,353 | 2024-04-02 | 2026-11-03 23:26 | no | comedy: acting class on napping at your desk unnoticed (adjacent) |  |
| 28 | 화장실 유형 시리즈 몰아보기 | 김켈리 Kellyfornia | `7lTcZoyTFcY` | long-form? (watch URL; duration not read) | 73,633 | 2024-05-17 | 2026-11-03 23:23 | no | '유형' sketch compilation: bathroom types |  |
| 29 | 화장실 급할 때 #다우소 #스케치코미디 | 삼물가게 | `9zhcKXXS4UY` | Shorts (URL) | 72,926 | 2023-11-16 | 2026-11-03 23:23 | no | corporate sketch Short (삼성물산 x 다우소): construction workers when nature calls |  |
| 30 | [자막뉴스] 끝도 없는 화장실 대기줄에...'벽 미세요' 상상초월 해법 등장 / YTN | YTN | `LJKOX95T8d8` | long-form? (watch URL; duration not read) | 58,575 | 2026-06-28 | 2026-11-03 23:25 | no | news (자막뉴스): endless women's restroom lines |  |
| 31 | 스마트폰 세균 '득실'…화장실 변기의 10배 / YTN 사이언스 | YTN 사이언스 | `fXL423nV1uw` | long-form? (watch URL; duration not read) | 58,298 | 2015-08-17 | 2026-11-03 23:21 | no | science news: phones carry more germs than toilets |  |
| 32 | [하우투] '2가지만 기억'…변비와 치질 고치는 마법의 자세 / 연합뉴스 (Yonhapnews) | 연합뉴스 Yonhapnews | `AVNEe83f-0M` | long-form? (watch URL; duration not read) | 51,401 | 2018-05-18 | 2026-11-03 23:31 | no | health how-to (연합뉴스): toilet posture for constipation/hemorrhoids |  |
| 33 | "9시 출근 · 5시 퇴근 너무 힘들어"… 사회초년생 눈물 영상 화제 / SBS / 실시간 e뉴스 | SBS 뉴스 | `rRr3tNL7QeY` | long-form? (watch URL; duration not read) | 45,190 | 2023-10-25 | 2026-11-03 23:25 | no | news: young worker's viral '9-to-5 is too hard' video (adjacent) |  |
| 34 | 여자들이 같이 화장실 가면 하는 일 | 진주특별시 | `dVXT6huu1C8` | long-form? (watch URL; duration not read) | 40,227 | 2021-07-07 | 2026-11-03 23:25 | no | relatable sketch: what women do when they go to the bathroom together |  |
| 35 | 여행도, 장거리 운전도 화장실 때문에 포기하고 산다? 당신은 고칠 수 있습니다│과민성 대장 증후군 완벽 솔루션│귀하신 몸│#골라듄다큐 | EBSDocumentary (EBS 다큐) | `jOjF9HFv_k8` | long-form? (watch URL; duration not read) | 32,221 | 2023-06-14 | 2026-11-03 23:23 | no | health documentary (EBS 귀하신 몸): IBS, life planned around toilets |  |
| 36 | 남자 화장실에서 이 행동을 한다고? | 도넛펭귄 | `iJu_KfZ1Zrs` | Shorts (URL) | 31,721 | 2026-08-17 | 2026-11-03 23:23 | no | sketch Short: a hand-washing gag in the men's room |  |
| 37 | 약으로도 못 고친 과민성 대장 증후군, 호흡법 하나로 화장실 탈출 성공? ｜ 장염 치료제 지사제 많이 먹으면 장 마비까지? ｜ 귀하신몸 ｜ EBS 건강 | EBS 건강 | `0VIhq5Gq92s` | long-form? (watch URL; duration not read) | 27,512 | 2023-09-24 | 2026-11-03 23:26 | no | health documentary (EBS): IBS and breathing |  |
| 38 | 혼자 있는 게 외롭지 않고 오히려 편한 사람들의 심리 | 라이프룰 | `LMWu3FjfoDE` | long-form? (watch URL; duration not read) | 25,492 | 2026-01-02 | 2026-11-03 23:32 | no | psychology explainer: people who like being alone (adjacent) |  |
| 39 | "화장실 갈 때 보고" "실적 줄면 내근"…이상한 재택근무 / JTBC 뉴스룸 | JTBC News | `r1aamssLSJA` | long-form? (watch URL; duration not read) | 24,933 | 2021-01-26 | 2026-11-03 23:22 | no | news: remote workers made to report bathroom trips |  |
| 40 | 화장실에서 장난치는 유형?! 화장실에서 장난치면 이렇게 된다고?? ㅋㅋㅋ | 슬기로운 초등생활 | `JmLSA6ObnZc` | long-form? (watch URL; duration not read) | 23,509 | 2025-11-29 | 2026-11-03 23:23 | no | kids' sketch: pranks in the school bathroom |  |
| 41 | 화장실에서 뒷담화를 듣게 된 뚱남 | 크크조이 : KBS Joy 종합 예능 채널 | `WK4uFz0ra64` | Shorts (URL) | 21,907 | 2025-12-05 | 2026-11-03 23:32 | no | variety clip Short (KBS Joy): overhearing gossip from a stall |  |
| 42 | 건설 현장에 존재한다는 똥방의 진실｜신축 아파트 공사장 화장실 실제 모습｜다큐프라임｜#골라듄다큐 | EBSDocumentary (EBS 다큐) | `jHPsHGT_ESs` | long-form? (watch URL; duration not read) | 17,886 | 2026-01-01 | 2026-11-03 23:31 | no | TV documentary excerpt (EBS): toilets on apartment construction sites |  |
| 43 | 오늘의 직장인 출근일기💼 #직장인 #직장인브이로그 #직장인의하루 #직장인쇼츠 #vlog | 리미Limmy | `3BXML2soESk` | long-form? (watch URL; duration not read) | 13,200 | 2026-08-06 | 2026-11-03 23:24 | no | office vlog Short with a gut-health product plug |  |
| 44 | 몰래 사내연애 하는 커플이 회사 화장실에서 양치하는데 ㅋㄷ을 챙기는 이유ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ | 코믹마트 | `GrBxKy6UaUk` | Shorts (URL) | 12,743 | 2025-12-26 | 2026-11-03 23:31 | no | drama-style Short: secret office couple in the company bathroom |  |
| 45 | 변기에 오래 앉아 있으면 안되는 이유 [의사결정] #shorts | CBS 경제연구실 | `9nnwvKbH7b8` | Shorts (URL) | 12,555 | 2024-05-02 | 2026-11-03 23:22 | no | doctor Short: why not to sit on the toilet long (5-min rule) |  |
| 46 | [71회] 화장실 5분 이상 앉아 있으면 치질 걸릴 수 있다? | KBS News | `w6p9abFQU8o` | long-form? (watch URL; duration not read) | 11,611 | 2013-12-09 | 2026-11-03 23:23 | no | health Q&A (KBS, 2013): 5+ minutes on the toilet and hemorrhoids |  |
| 47 | 긴장할 때 마다 찾아오는 급똥! 원인과 해결책은 무엇일까?! | 김원장네 건강해우소 | `CfYf7-2sLUQ` | long-form? (watch URL; duration not read) | 9,435 | 2019-12-25 | 2026-11-03 23:22 | no | doctor (Korean medicine) explainer: urgent bowels when nervous |  |
| 48 | 회사에서 🐶빡칠 때 몰래 욕하는 법🤬 직장인 분노 꿀팁🍯 고맙ㅅ브니다 안녕히개새야~^___^ | 입사동기 | `L--4LpyGrII` | long-form? (watch URL; duration not read) | 9,215 | 2021-08-06 | 2026-11-03 23:26 | no | comedy tips: how to swear secretly at work (adjacent) |  |
| 49 | 나는 '혼자' 일하고 싶다 | 곰기사 | `kGNuNPWNwT4` | long-form? (watch URL; duration not read) | 6,897 | 2025-05-31 | 2026-11-03 23:32 | no | talk: 'I want to work alone' (adjacent) |  |
| 50 | [스마트 리빙] 화장실에 스마트폰 가져가지 마세요 (2020.03.09/뉴스투데이/MBC) | MBCNEWS | `tIbFzN0BfLo` | long-form? (watch URL; duration not read) | 6,451 | 2020-03-08 | 2026-11-03 23:21 | no | news (MBC 스마트 리빙): don't take your phone into the toilet |  |
| 51 | "화장실 급해서" 개찰구 나왔어도…지하철 '10분 내 재승차' 무료 / JTBC 뉴스룸 | JTBC News | `l1NXh46TofA` | long-form? (watch URL; duration not read) | 6,299 | 2023-06-28 | 2026-11-03 23:26 | no | news: Seoul subway free re-entry within 10 min for toilet trips |  |
| 52 | [와글와글 플러스] "쉬러 화장실 가요"‥'화캉스' 유행 (2025.07.17/뉴스투데이/MBC) | MBCNEWS | `ukK65Jo57_A` | long-form (1:14) | 6,244 | 2025-07-16 | 2026-11-03 23:20 | no | news (MBC 와글와글): the 화캉스 trend, quotes a post 'this time slot is always full' |  |
| 53 | [직장인 모먼트] 직장에서 유일하게 행복한 순간 (직장인 공감 콘텐츠/웹드라마) | 뷰리플 | `40GCLMk28tI` | long-form? (watch URL; duration not read) | 4,841 | 2021-02-16 | 2026-11-03 23:25 | no | web-drama sketch: the only happy moment at work |  |
| 54 | 스마트폰 세균 '득실'...화장실 변기의 10배 / YTN | YTN | `o05szjOavwE` | long-form? (watch URL; duration not read) | 4,649 | 2015-08-17 | 2026-11-03 23:21 | no | news (YTN): phone germs vs toilet |  |
| 55 | 엑셀하는 줄 알았더니…"일하면서 몰래 보는" 위장 주식 사이트 등장｜지금 이 쇼츠 | JTBC News | `yLnKZRC8m6k` | long-form? (watch URL; duration not read) | 4,428 | 2026-05-29 | 2026-11-03 23:31 | no | news Short-style clip: stock-ticker site disguised as Excel for watching at work |  |
| 56 | (플래시 애니메이션) 화장실 | 수원삼성 승격 | `1W8vfwYX230` | long-form? (watch URL; duration not read) | 4,217 | 2022-02-16 | 2026-11-03 23:25 | no | old flash animation: struggling to get to a toilet |  |
| 57 | 회사에서 우는 직원 대처법 + 회사에서 울고 싶을 때 꿀팁 | 세자리 | `Ld38Jc0FtE8` | long-form? (watch URL; duration not read) | 4,017 | 2025-03-26 | 2026-11-03 23:22 | no | talk/tips: crying at work and how to handle it (adjacent) |  |
| 58 | 툭하면 복통·설사… '과민성 대장증후군', 내 성격 탓일까?  ｜ 소화기내과 김동우 교수 | 건강의학전문채널 하이닥 | `Aq9l4KPWUg8` | long-form? (watch URL; duration not read) | 3,516 | 2026-05-24 | 2026-11-03 23:22 | no | doctor interview (하이닥): IBS and personality |  |
| 59 | 회사에서 졸릴 때 몰래 자는 방법 | 대처법 | `IKZXs9We_eA` | Shorts (URL) | 2,930 | 2026-01-20 | 2026-11-03 23:23 | no | tips Short: napping secretly at work (adjacent) |  |
| 60 | "이게 주식 사이트라고?"..감쪽같은 위장 '화제' / SBS / 실시간 e뉴스 | SBS 뉴스 | `QQ8824qC96Q` | long-form? (watch URL; duration not read) | 2,886 | 2026-05-29 | 2026-11-03 23:31 | no | news: same disguised stock site |  |
| 61 | [잇슈#태그] “왜 흡연자들만 쉬냐”…직장인들 ‘담타’ 사이트 접속하는 이유 / KBS 2026.05.03. | KBS News | `da11LubhRPQ` | long-form? (watch URL; duration not read) | 2,768 | 2026-05-03 | 2026-11-03 23:31 | no | news (KBS): non-smokers visit a fake 'smoke break' site |  |
| 62 | (공감주의) 지하철에서 갑자기 똥이 마려울 때...! #shorts | 메이플스토리 월드 (MapleStory Worlds) | `-DEXq78jl60` | Shorts (URL) | 2,536 | 2023-04-12 | 2026-11-03 23:26 | no | game-brand animated Short: sudden urge on the subway |  |
| 63 | 쇼츠 영상 시청, 정말 도파민 중독될까? 과도한 노출이 뇌에 미치는 영향은?│귀하신 몸│#EBS건강 | EBS 건강 | `ZGhfTt2_ljc` | long-form? (watch URL; duration not read) | 2,379 | 2025-04-14 | 2026-11-03 23:32 | no | health documentary (EBS 귀하신 몸): short-form videos and dopamine |  |
| 64 | 김다영 아나운서 / '화캉스' 란? 🤔 직장연애보고서 :  왜 예쁘게 웃었게요?^^💕 | [철파엠] 김영철의 파워FM 공식계정 | `Fei9Pa2oCsw` | long-form? (watch URL; duration not read) | 2,106 | 2024-08-12 | 2026-11-03 23:22 | no | radio clip (SBS 파워FM 철파엠): announcer explains '화캉스' |  |
| 65 | 남편들은 왜 화장실에 오래 있는가? - 대한민국 교육위원회 시즌2-3회 | JTBC Entertainment | `YI_TIZ87xq8` | long-form? (watch URL; duration not read) | 2,021 | 2013-04-17 | 2026-11-03 23:22 | no | TV talk-show clip (JTBC, 2013): why husbands stay long in the bathroom |  |
| 66 | [대결! 애니메이션] 직장인 공감 쇼츠짤 | 블루라벨픽쳐스 | `g9-g90KmxOI` | long-form? (watch URL; duration not read) | 1,826 | 2024-02-19 | 2026-11-03 23:25 | no | animation Short-style clip: office-worker relatable memes |  |
| 67 | 스트레스가 호르몬을 자극해 배변 이상을 일으킨다 - (2017.2.8_609회 방송)_화장실의 고통, 과민성 장 증후군 | KBS 생로병사의 비밀 | `ZMGhweAKkoU` | long-form? (watch URL; duration not read) | 1,722 | 2020-08-25 | 2026-11-03 23:25 | no | health documentary (KBS 생로병사): stress and bowel trouble |  |
| 68 | [제보M] "화장실 갈 곳이 없어요" 12시간 운행에도 쉴 곳 없는 택시 [MBN 종합뉴스] | MBN News | `FUmK2Q632_g` | long-form? (watch URL; duration not read) | 1,722 | 2021-12-22 | 2026-11-03 23:32 | no | news (MBN): taxi drivers with nowhere to use a toilet |  |
| 69 | '직장인 담배타임' 휴식일까? 근무 태만일까? | 법무법인(유한) 대륜 SJKP Korea | `ZHNy1VhUBdc` | long-form? (watch URL; duration not read) | 1,673 | 2024-10-14 | 2026-11-03 23:31 | no | law-firm explainer: is a smoke break rest or slacking? |  |
| 70 | 변기에서 폰 보면 생기는 일 🚽 범인은 폰이 아니라 시간 | 도트박사 | `fChfMFe_8lc` | long-form? (watch URL; duration not read) | 1,415 | 2026-10-15 | 2026-11-03 23:21 | no | doctor explainer: phone on the toilet, time is the culprit (cites 125-person study) |  |
| 71 | [AI영상] 급똥 직장인 | 직하법 - 코리아 존맛탱 | `r9xeLuk1aFA` | long-form? (watch URL; duration not read) | 1,413 | 2026-02-07 | 2026-11-03 23:21 | no | AI-generated video: office worker with urgent bowels |  |
| 72 | 감춰진 산재 ‘화장실 직업병’ / KBS  2021.11.16. | KBS News | `tm6v9NThUuQ` | long-form? (watch URL; duration not read) | 1,327 | 2021-11-15 | 2026-11-03 23:26 | no | news (KBS): hidden occupational disease, workers who can't use toilets |  |
| 73 | 30분에 7,900원 직장인 꿀잠..😴 강남 한복판 수면 카페에서 낮잠 자봤습니다 | 수면은 현도진 | `-G8qNBlsu34` | long-form? (watch URL; duration not read) | 1,165 | 2025-07-16 | 2026-11-03 23:24 | no | vlog: office workers' nap café (adjacent) |  |
| 74 | 마트·다이소 가면 똥 마려운 현상, 당신만 그런 게 아닙니다 | 마인드브릭 | `saW_53Y590c` | long-form? (watch URL; duration not read) | 971 | 2026-03-22 | 2026-11-03 23:22 | no | explainer: why marts/Daiso trigger the urge |  |
| 75 | 혹시 이 영상을 화장실에서 보고 계신가요? - 항문외과 의사가 직접 알려주는 변기에 오래 앉아있으면 안 되는 이유 🚨 | 백발백중_닥터신 | `sdsVfelRepI` | long-form? (watch URL; duration not read) | 915 | 2026-03-30 | 2026-11-03 23:23 | no | doctor explainer (proctologist): 'are you watching this on the toilet?' |  |
| 76 | 당신이 일할 때 가끔은 '멍 때려줘야 하는 이유' / YTN | YTN | `9PGzvCNCwAI` | long-form? (watch URL; duration not read) | 829 | 2015-11-18 | 2026-11-03 23:32 | no | science news (YTN, 2015): why zoning out at work helps (adjacent) |  |
| 77 | 출근길마다 복통... 과민성 대장증후군의 관리법은? ㅣ 내과 김영집 원장 | 건강의학전문채널 하이닥 | `nd5a_CG8N_Y` | long-form? (watch URL; duration not read) | 749 | 2025-05-08 | 2026-11-03 23:21 | no | doctor interview (하이닥): stomach aches on every commute (IBS) |  |
| 78 | 화장실을 너무 자주 가는 사람들 #과민성대장증후군 | CM병원 | `h1y5GkEbBG0` | Shorts (URL) | 638 | 2024-11-30 | 2026-11-03 23:22 | no | hospital Short: people who go to the toilet too often (IBS) |  |
| 79 | [온갖이슈] 근무 중 휴대폰 금지, 점심은 책상에서,, 한 기업의 직원 길들이기 | JTV ON | `-H7fg0MpLn0` | Shorts (URL) | 590 | 2025-04-08 | 2026-11-03 23:24 | no | news Short: company bans phones during work (adjacent) |  |
| 80 | 회사에서 몰래 쇼핑 / 게임 안걸리고 하는법 (월급 루팡 꿀팁) | 전파남 | `YvYRxa906so` | long-form? (watch URL; duration not read) | 583 | 2019-09-29 | 2026-11-03 23:24 | no | tips: shopping/gaming at work without getting caught (월급루팡) |  |
| 81 | [포인트 경제] “화장실도 가지 마라”…‘직장 내 괴롭힘’ 사라질까? / KBS뉴스(News) | KBS News | `WSigF5p8k4Q` | long-form? (watch URL; duration not read) | 507 | 2019-05-07 | 2026-11-03 23:23 | no | news (KBS): 'don't even go to the toilet' workplace bullying law |  |
| 82 | 월급루팡 | 닥터 | `4G9RremPhAo` | long-form? (watch URL; duration not read) | 434 | 2026-02-27 | 2026-11-03 23:25 | no | short clip titled '월급루팡' |  |
| 83 | 화장실 갈 때도 보고해, '직장갑질' | KBS뉴스 경남 | `3jiPr_5coBQ` | long-form? (watch URL; duration not read) | 364 | 2019-07-17 | 2026-11-03 23:21 | no | news (KBS 경남): company logged workers' toilet trips |  |
| 84 | [항문원큐] 하루종일 앉아서만 일을 하는데 치질 가능성은? | 엉덩이대장 | `db0sp7Td8mw` | long-form? (watch URL; duration not read) | 330 | 2023-06-18 | 2026-11-03 23:23 | no | doctor Q&A: desk job and hemorrhoids |  |
| 85 | "근무중 용변시간 제한"…中 회사 '뭇매' / 연합뉴스TV (YonhapnewsTV) | 연합뉴스TV | `Zsm09EUiJVk` | long-form? (watch URL; duration not read) | 294 | 2025-02-23 | 2026-11-03 23:22 | no | news: Chinese company limits toilet trips |  |
| 86 | 출근길에 지하철타면 3번은 내려요, 설사 때문에 ｜ 과민성대장염, 정이안 한의사. | Doctalk | `YnPMlbVZuoU` | long-form? (watch URL; duration not read) | 216 | 2021-10-12 | 2026-11-03 23:21 | no | doctor Q&A (Korean medicine): getting off the subway 3 times for diarrhea |  |
| 87 | “월급루팡에 대한 생각은?” | 잡플러스TV | `vhTrMibRD6I` | long-form? (watch URL; duration not read) | 214 | 2023-11-06 | 2026-11-03 23:25 | no | street/job-channel clip: what do you think of 월급루팡? |  |
| 88 | 진정한 직장인들을 위한 쉼터, 화장실! | 타일퀸 | `0iHcyC7SeRI` | long-form? (watch URL; duration not read) | 185 | 2021-10-15 | 2026-11-03 23:21 | no | interior design: office restroom as the workers' real rest space |  |
| 89 | 화장실 매매 직장인의 주식투자 2주차 | K L | `YP47jWhgNFc` | long-form? (watch URL; duration not read) | 53 | 2021-02-28 | 2026-11-03 23:22 | no | personal stock-trading log: 'bathroom trading' office worker, week 2 |  |
| 90 | 화장실 매매 직장인의 주식투자 | K L | `fmnDRncNZrk` | long-form? (watch URL; duration not read) | 24 | 2021-02-21 | 2026-11-03 23:22 | no | personal stock-trading log: 'bathroom trading' office worker |  |

### 1b. International videos (format reference only; sorted by views)

| # | Title | Channel | ID | Format (duration) | Views | Published | Checked (UTC) | Meets? | Framing | Captions |
|---|---|---|---|---|---:|---|---|---|---|---|
| 1 | Undercover Office Potty - SNL | Saturday Night Live | `KUzGrzsYqH4` | long-form (3:02) | 7,918,168 | 2018-03-18 | 2026-11-03 23:26 | **yes** | INTL comedy sketch (SNL): fake ad for a lamp that is secretly an office toilet | fetched |
| 2 | Never watch YouTube on the toilet. This is why. | Brew | `57v5vs_xcdc` | long-form (8:06) | 334,998 | 2024-05-30 | 2026-11-03 23:26 | no | INTL explainer (Brew): 'never watch YouTube on the toilet', opens at work |  |
| 3 | The dark side of taking your phone into the bathroom (You're Doing It All Wrong!) | CNET | `tG7-eR1_5jQ` | long-form? (watch URL; duration not read) | 118,887 | 2015-08-02 | 2026-11-03 23:26 | no | INTL tech-news explainer (CNET): the dark side of phones in the bathroom |  |
| 4 | Scrolling on the Toilet? This Is What It’s Doing to Your Body ｜ Dr. Mandell | motivationaldoc | `uEIPaAI1z9w` | long-form? (watch URL; duration not read) | 53,474 | 2026-10-09 | 2026-11-03 23:27 | no | INTL doctor explainer: what scrolling on the toilet does to your body |  |
| 5 | KOREY’S OFFICE BATHROOM STORY AND TAKING A POOP IN PUBLIC | Double Toasted Bites | `dAV_4MIE7Mk` | long-form? (watch URL; duration not read) | 13,530 | 2026-09-13 | 2026-11-03 23:32 | no | INTL podcast clip: a host's office bathroom story |  |
| 6 | Have You Heard of 'Bathroom Camping?' | TODAY with Jenna & Sheinelle | `zu4pR2X8jpo` | Shorts (URL) | 10,231 | 2025-12-12 | 2026-11-03 23:26 | no | INTL TV news Short (TODAY): 'bathroom camping' |  |
| 7 | Why you should NEVER use your phone on the toilet 😨 #health #habits #shorts | Luke Coutinho | `8J1vv70DlTE` | Shorts (URL) | 8,342 | 2026-06-14 | 2026-11-03 23:27 | no | INTL health Short: never use your phone on the toilet |  |
| 8 | Have you ever gone 'bathroom camping' when emotional or overstimulated? | 7NEWS Australia | `8zSw_bSipes` | Shorts (URL) | 7,566 | 2025-07-23 | 2026-11-03 23:26 | no | INTL TV news Short (7NEWS): 'bathroom camping' when overstimulated |  |
| 9 | #GenZ “discovers” hiding in bathrooms 😂 they call it bathroom camping, and yes they’re doing it at | Kelly Manno | `ONm018QSNBE` | Shorts (URL) | 6,876 | 2025-07-30 | 2026-11-03 23:26 | no | INTL creator Short: Gen Z 'discovers' hiding in bathrooms |  |
| 10 | Poop at work. It’s good for you! | Washington Post | `N4S2Cd_z1jw` | Shorts (URL) | 5,133 | 2025-06-06 | 2026-11-03 23:27 | no | INTL newspaper Short (Washington Post): poop at work, it's good for you |  |
| 11 | Why Is He Using His Phone In The Bathroom So Much? | Dr. Doug Weiss | `y4Vyfi2NHC4` | long-form? (watch URL; duration not read) | 1,404 | 2026-02-13 | 2026-11-03 23:32 | no | INTL therapist clip: why is he using his phone in the bathroom so much? |  |
| 12 | Gen Z’s Bathroom Camping Trend: Funny Escape Or Silent Cry For Peace? ｜ What’s Behind It | Times Now | `BDU0dwco4LY` | long-form? (watch URL; duration not read) | 1,078 | 2025-07-20 | 2026-11-03 23:26 | no | INTL TV news (Times Now): Gen Z bathroom camping, escape or cry for peace |  |
| 13 | Bathroom Camping | Iowa Everywhere | `T1qjFt7DQOA` | Shorts (URL) | 830 | 2025-08-05 | 2026-11-03 23:26 | no | INTL local TV Short: bathroom camping |  |
| 14 | Phone on the Throne? Hemorrhoid Risk | Medscape | `xVX3BaO5d-o` | long-form? (watch URL; duration not read) | 284 | 2026-04-18 | 2026-11-03 23:27 | no | INTL medical news (Medscape): phone on the throne, hemorrhoid risk |  |
| 15 | Psychology of People Who Cry in Private, Then Smile Like Nothing Happened | The Blank Face | `RwYwaP80cF8` | long-form? (watch URL; duration not read) | 8 | 2026-10-25 | 2026-11-03 23:26 | no | INTL psychology narration: people who cry in private, then smile |  |

## 2. How the qualifying videos are made

### 2a. Qualifiers with fetched captions (9)

**A. 운행 중 갑자기 배가 아프다. 철도 기관사는 화장실 어떻게 해결하는지 봤더니｜화장실 전쟁｜다큐프라임 (EBSDocumentary `OnwnPqyZC5w`, 11:06, 1,339,319 views, 2025-12-20)**
- **Format:** an excerpt of a TV documentary (EBS 다큐프라임 「싸느냐, 참느냐 화장실 전쟁」, aired 2025-12-08), re-cut for the 골라듄다큐 channel. It mixes ride-along footage, interviews and narration.
- **Who appears:** a 3rd-year 한국철도공사 train driver, a second subway driver, an off-screen interviewer, the narrator, and dispatcher voices on the radio.
- **First 10 s (hook):** the driver introduces himself: "안녕하세요. 저는 한국 철도공사에서 3년차 기관사로…" (ASR). The confession lands at 0:10–0:23: "그렇게 많이 참아야 될 줄은 상상을 못 한 거 같아요."
- **Flow:**
  1. The problem: the cab is open and he can make eye contact with passengers, so using a portable toilet there is hard.
  2. His coping kit: a portable toilet and anti-diarrhoea pills bought in Japan.
  3. A real-time ride-along. He radios for a toilet break at the terminal. A delay leaves about 7 minutes; walking the 200 m train for the cab change takes about 5, which leaves about 3. He sprints off the platform.
  4. The cost: a health check flagged an inflammation, ASR "관광염", most likely 방광염 (bladder inflammation), so "참으면 안 되겠다." The drivers' toilets at the terminus are unflushable units that hardly anyone uses.
  5. The second driver shows the in-cab portable-toilet routine. Hands may not leave the controls for more than 5 seconds.
  6. The labour angle: a colleague was disciplined after a 5–10 minute delay caused by a toilet trip. Drivers started a work-to-rule campaign asking for longer turnarounds and proper toilets: "인권의 문제기도 하지만 승객 안전과도 직결".
- **Recurring details:** countdowns ("7밖에 안 남았네요"), radio calls, running on stairs, and the repeated verb 참다.
- **Facts cited:** from the description, adults use the toilet 4–8 times a day and spend about one year of life there. From the footage: 8-minute turnarounds, a 200 m train, the 5-second hands-off limit, and more than 1,000 passengers at rush hour.
- **Ending:** a narrator line contrasting a public toilet that crowds use every day with the workers there, for whom getting to it "쉽지 않은…".

**B. 잠보다 강력하다! 뇌를 회복시키는 진짜 휴식 루틴, 딱 5분만 해보세요 (세바시 인생질문 `9rHpeKlCPTA`, 20:50, 1,152,669 views, 2025-05-20). Adjacent: about rest, not the bathroom.**
- **Format:** a single-expert talking-head interview. The host's questions do not appear in the captions, so they seem to be cut out.
- **Who appears:** 김은영, professor of psychiatry at 서울대 and author of 『나는 왜 마음 놓고 쉬지 못할까』, per the description.
- **First 10 s (hook):** a cold-open montage of her sound bites voicing patients' fears: "우울증이나 조울증에 걸린 거 같다", "ADHD나 치매가 아닌지", "내가 지금 긴장을 놓거나 쉬면은 불행한 일이 벌어질 것이다" (ASR).
- **Flow:**
  1. Clinic stories: burnout, chronic fatigue, shallow sleep, and doctor-shopping before ending up in psychiatry.
  2. Why we cannot rest: perfectionism, catastrophising ("쉬면 큰일 난다" becomes a learned link), guilt, and family and workplace culture.
  3. Fake rest: short-form scrolling ("10분만 봐야지 했는데… 30분 한 시간"), shopping and alcohol, with dopamine and loss of control.
  4. What works: micro-breaks, "5분이나 10분처럼 굉장히 짧은 시간을 쉬어도… 회복에 어느 정도 효과가 있다라고 많이 연구가 되어 있어요". Also breath focus, and her own one-minute breathing breaks between patients.
  5. Relearning: notice the pattern, then teach the nervous system "쉬어도 괜찮다".
- **Facts cited:** general mentions of micro-break research. No named study and no numbers.
- **Ending:** reassurance and a reframe: "잘 쉬어야 … 더 오랫동안 더 꾸준히 … 해 나가실 수 있다".

**C. 아무리 쉬어도 피곤한 당신에게. 뇌를 회복시키는 '진짜' 휴식법 (뇌과학 쓸래요? `k1UFksi3-2g`, 6:46, 1,410,820 views, 2026-03-09). Adjacent: about rest.**
- **Format:** a narrated explainer with one voice. The description lists chapters. Visuals were not inspected.
- **Who appears:** the narrator only. He uses first-person examples ("저 같은 경우에는 햇볕을 쬐면서 걷다가 찜질방…").
- **First 10 s (hook):** "여러분은 요즘 제대로 쉬고 계신가요? 현대인에게 휴식은 가장 어려운 숙제가 돼 버린 것 같습니다." It then names students and office workers ("직장인이라면 주말에도 업무 생각이…").
- **Flow:**
  1. Avoidant rest: "침대에 누워서 쇼츠를 계속 스크롤…", so "몸은 쉬고 있는데 뇌는 전혀 쉬지 못하는 상태".
  2. The default mode network (DMN), described as the brain's background clean-up, which can tip into rumination (반추).
  3. Step 1: digital detox, which cuts input. Dopamine is called "저렴한 자극".
  4. Step 2: shift from thoughts to senses through walking, stretching, tea, or instrumental music.
  5. Step 3: "serotonin rest". Check how you feel afterwards; ranked games, alcohol and shorts leave you worse.
  6. Rules: work 50 minutes then rest 5–10, or work 25 then rest 5. One phone-free hour on weekday evenings; half a day off on weekends.
- **Facts cited:** concepts only (DMN, dopamine versus serotonin). No studies or numbers.
- **Ending:** a recap of the 3 principles, "우리는 결국 스스로의 의사가 되어야 합니다", then a request to subscribe.

**D. [스튜디오 장삐쭈] 화장실 (장삐쭈 `qN48B8YDpwM`, 1:00, 4,742,317 views, 2022-12-20)**
- **Format:** a 60-second animated workplace sketch. The studio's own staff are the characters, and they share one bathroom. It has voice acting.
- **Who appears:** a boss voice and staff characters (names from the captions: 성은, 주형).
- **First 10 s (hook):** the boss walks in on an employee: "깜짝이야 성은아, 팻말 '사용 중'으로 이거 해놓고 써라". The employee pushes back politely: "불 켜져 있으면 사람 있나 보다 해야 되는 거 아닌가…" (ASR).
- **Flow:**
  1. Day 1, sign versus light.
  2. Day 2, the light is off and he walks in again; "문 닫혀 있으면 노크라도 하셔야".
  3. A new protocol: knock, "똑똑똑 누구 있어?", nobody answers, fine.
  4. Next day: knock, announce, count "하나 둘 셋", and the reply is "다 여기 있는데요" (everyone is inside).
  5. Closing line: "아 오줌보 터질 뻔했네".
- **Recurring jokes:** passive-polite office pushback ("그런 생각도 조금 들기도 합니다"), and rules that keep escalating, decided like meeting items ("다음날 보고 결정하자").
- **Facts cited:** none.
- **Ending:** an absurd punchline followed by a relief line.

**E. 아뿔싸 화장실이 만석이다. (그런 당신을 위한 괄약근 댄스) (빵쏭bbangsong `5DJvA_1RjdA`, 2:09, 9,228,555 views, 2022-02-09)**
- **Format:** an original comic song with animation. The description says lyrics, music and animation are all by 빵쏭. The caption service returned an English subtitle track, so the quotes are translations.
- **Who appears:** animated characters and the 빵쏭 vocals.
- **First 10 s (hook):** the dance chorus first: "Two legs twist, twist / To the butts hip hip … On the sphincter hop hop".
- **Flow:**
  1. The chorus.
  2. Verse 1: on a bus on a jammed highway after milk and cream bread.
  3. Pre-chorus: stomach growling, sweating, "it turns yellow in front of me", then "Sphincter dance!".
  4. Verse 2: rushes to the rest-stop toilet, knocks 12 times, "It's full", "Why aren't they coming out?".
  5. The chorus again.
  6. An outro pun, "Don't give me that shit", and an end card asking viewers to subscribe.
- **Relatable details:** knocking on every stall, nobody coming out, cold sweat.
- **Facts cited:** none.
- **Ending:** the pun outro and the subscribe card.

**F. '남자 급똥' (급똥 마려울 때) -홍팸 (홍팸 `YPjS2RAl1x8`, 5:51, 1,871,523 views, 2024-03-16)**
- **Format:** live-action sketch comedy. Mostly physical, set to music, with sparse lines.
- **Who appears:** the protagonist and a chain of obstacle characters: a street proselytiser, a friend (박홍구), and a grandmother.
- **First 10 s (hook):** "배 아파… 잠깐 어디 화장실 없나… 이러면 안 되는데" (ASR).
- **Flow:**
  1. A sudden urge.
  2. A proselytiser blocks him: "10분이라도", "5분이면 되거든요", "도에 대한 설명을…". This parodies the classic "도를 아십니까" street approach.
  3. A friend with food tempts him.
  4. A grandmother asks for help down the stairs ("젊은 녀석이 나보다 늦게 내려가면…").
  5. His zipper sticks.
  6. Someone discovers that a person has pooped on the spot, followed by applause.
- **Recurring jokes:** "5분이면 돼요" under time pressure, strangers who will not let go, smell gags.
- **Facts cited:** none.
- **Ending:** the discovery gag and [박수].

**G. 여자 화장실의 민낯 (99.9도 `iW-tdqKf9Nc`, 4:49, 1,421,936 views, 2025-11-30)**
- **Format:** a near-wordless live-action "코믹숏무비": a montage of women's-restroom habits ("여자화장실 특"), set to music.
- **Who appears:** several actresses. The tags suggest 그냥필름 produced it.
- **First 10 s (hook):** a sound gag ("똥똥… 똥"), then at 0:14 the seat-disinfecting ritual "소독 소독 소독…".
- **Flow:**
  1. Sanitising the seat.
  2. Mirror and make-up talk ("언니 오늘 화장 잘 먹으셨네요").
  3. Waiting for a stall.
  4. No toilet paper ("휴지도 없어… 여분이 없네").
  5. Improvising and relief, ending on a startle beat ("어머 깜짝").
- **Recurring jokes:** muttered swearing and sound gags.
- **Facts cited:** none.
- **Ending:** the startle gag.

**H. 실패 없는 화캉스 공식? 브레프 디럭스! (Henkel Consumer Brand Korea `oet-Xb6JCjI`, 0:31, 11,496,209 views, 2025-08-22)**
- **Format:** a 31-second product ad for the Bref toilet freshener. The identical ad uploaded as a Short (`S2GTqlusosc`) has 135,076 views. That 85× gap suggests the watch version was served as a paid ad; this is an inference, not verified.
- **Who appears:** ad actors and a voice-over.
- **First 3 s (hook):** "실패없는 화캉스 공식."
- **Flow:**
  1. The tagline.
  2. The product with music.
  3. "물을 내릴 때마다 깨끗하고 향기롭게".
  4. A reaction: "변기 청소했지? … 향긋해".
  5. The product sign-off. The auto-captions are partly garbled.
- **Note:** here 화캉스 means a pleasant (home) bathroom moment, not office escape. Still, it shows the coinage had reached ad copy by August 2025, about a month after MBC's July 2025 news item.
- **Facts cited:** none.

**I. Undercover Office Potty - SNL (Saturday Night Live `KUzGrzsYqH4`, 3:02, 7,918,168 views, 2018-03-18). International reference.**
- **Format:** a parody commercial with infomercial voice-over set in an office.
- **Who appears:** the SNL cast (the tags list Bill Hader, Beck Bennett and others) and a voice-over.
- **First 10 s (hook):** "Hey Johnson, don't forget, we need those reports by the end of the day." Then the voice-over: "Need to go to the bathroom, but you have a lot of work to do, and it's all the way down the hall."
- **Flow:**
  1. The setup: a deadline versus a toilet far down the hall.
  2. The product: a lamp that is secretly a toilet, "so you can go whenever you want, and no one has to know".
  3. A success beat: "I had plenty of time."
  4. Escalation: too many lamps, a smell, coworkers investigate, and the boss steps in.
  5. A sequel product: a stapler, tape dispenser and pencil sharpener in disguise. He is caught again and fired.
  6. The slogan.
- **Recurring jokes:** "I guess I like a lot of light / tape" and the repeated alibi "I go to the bathroom all the way down the hall".
- **Facts cited:** none.
- **Ending:** "Be bold, be true. Make the bathroom come to you."

### 2b. Qualifiers without captions (metadata and description only, so no first-10-s quote)

- **화장실 공감 만화 (소맥거핀 `tsz0xe26Bho`, 1:42, 23,662,189 views, 2021-06-23):** short animation in the channel's MapleStory-style "병맛" look (per the tags), with BGM credited to 브금대통령 ("Black Comedy"). There were no subtitles, so the content is not verified beyond the title "화장실 공감 만화". The channel's 51:54 compilation `jXamLDR0roQ` ("일상 공감" 시리즈 몰아보기, 5,292,580 views, 2026-09-25) repackages the same series.
- **[SNS 시트콤] 쾌한상사 '제1화 화장실 습격사건' (pasteurkorea `PcK-zmezH2Y`, 7:45, 1,151,714 views, 2013-07-11):** branded web sitcom for Pasteur's 쾌변 yogurt. The description says "직장인들의 웃기고 슬픈 이야기", "실제상황을 극화" and "업무에 지친 직장인들이여". The tags include 무한상사 (a parody reference), 변비 and 화장실. It is the only big hit set squarely in an office bathroom, but it is 13 years old and an ad. There were no subtitles.
- **남자들이 유일하게 오래 걸리는곳 (유머너굴 `pqdCtJP9luE`, Shorts 0:18, 1,078,051 views, 2026-09-30):** couple-relatable Short. From the description: a husband does everything at LTE speed, "그런데 왜 화장실만 들어가면 함흥차사", and he "무려 3시간 만에 폰 들고 나오는" — the phone-in-the-bathroom refuge, set at home rather than the office. There were no subtitles.
- **Toilet Awkward Situation 화장실 난감한 상황 (ODS `1aI0bggfa54`, Shorts 0:16, 14,982,361 views, 2025-07-01):** wordless cartoon whose metadata language is English. It travels internationally. Captions were not requested because there is no speech.
- **허름한 화장실에만 줄을 선 이유 (노후웃음 `HH41iRNdm4I`, Shorts 0:47, 2,813,899 views, 2026-02-27):** narrated "senior humour" story. From the description: during training in the mountains, the line forms only at the shabby toilet, and a line of graffiti flips the story. It ends by asking viewers to comment.
- **급똥 애니메이션 몰아보기 (키에커 `Rm_CDiTqHi4`, 40:49, 2,380,418 views, 2026-01-17):** compilation of 10 animated "급똥" episodes, one titled "여자들의 화장실 심리전". The audio language is marked zxx (no speech).
- **화장실을 위한 첫 번째 럭셔리 향수, 브레프 디럭스! (Henkel `A4-oaCy7jWc`, 0:41, 4,596,585 views, 2021-07-21):** an earlier Bref ad that does not use the word 화캉스.
- **"점심시간, 5분 거리 집에서 쉬다 오는 게 잘못인가요?" / SBS / 뉴스딱 (`lKM5l2Z-CLk`, 1:21, 1,002,757 views, 2023-03-06)** and **"퇴근 전 저녁 먹다 들켰는데…담배타임 더 길지 않나요?" / SBS / 뉴스딱 (`sURBM42ynXE`, 1:33, 930,524 views, 2023-07-04):** both are anchor-read stories, and each description carries the full script.
  - Both follow the same template: (1) a community or Blind post from an office worker; (2) a boss objects to an informal break; (3) the worker's rebuttal: "점심시간은 법적으로 주어진 자유시간이 아니냐", or "과장님이 담배 피운다고 나가는 시간을 합치면 나보다 더 많은 거 아닌가"; (4) netizens split ("지나친 간섭" vs "외출 시엔 보고는 해야"); (5) a vote result (the majority said the worker should not eat dinner on the clock).
  - The titles are written as the worker's own question.
- **남성 공무원이 받은 황당 메일 "…보건실 사용 자제 부탁" / KNN (`4TOxizhmGF4`, 2:02, 801,320 views, 2024-12-12; qualifies only under the long-form rule):** news item from a community post. Male civil servants were asked not to use the health room at lunch so that female staff could rest there, which raises the question of who gets the office's only rest space.


## 3. Patterns across the qualifying videos

There are 20 qualifiers: 19 Korean plus SNL. Of these, 9 have fetched captions and 11 are described from metadata only.

### What wins

1. **Animation and near-wordless comedy dominate the top.**
   - Animated (6 of the 19 Korean qualifiers): 소맥거핀 23.7M and its compilation 5.3M, ODS 15.0M, 빵쏭 9.2M, 장삐쭈 4.7M, 키에커 2.4M.
   - Live-action, mostly wordless and set to music: 홍팸 1.87M, 99.9도 1.42M.
   - Wordless or translated pieces also travel abroad: ODS has English metadata, and 빵쏭 has an English subtitle track. That likely inflates their counts.
2. **The situation is the hook, not the label.** Winning titles name a bodily emergency or a scene: 화장실이 만석이다, 급똥 마려울 때, 남자들이 유일하게 오래 걸리는곳, 허름한 화장실에만 줄을 선 이유.
   - In 4 of the 6 captioned comedy and ad videos (빵쏭, 장삐쭈, 홍팸, SNL), the first seconds put the body under pressure against an obstacle or a clock. Examples: "배 아파… 화장실 없나", knocking on full stalls, a boss's deadline against a distant toilet.
   - The structure is escalation: rules that keep changing (장삐쭈), a chain of obstacles (홍팸), a product that keeps failing (SNL), then a punchline or slogan.
3. **Workplace-break moral dilemmas do very well as news.** SBS 뉴스딱 (1.0M and 0.93M) and KNN (0.80M) all use the same template.
   - Template: a community post, then a boss against a worker over an informal break (lunch at home, dinner on the clock versus smoke breaks, who may use the rest room), then netizens split.
   - Each title is phrased as the worker's question ("~잘못인가요?", "~더 길지 않나요?").
   - **Contrast:** MBC's "'화캉스' 유행" item, which announces a trend rather than a conflict, has 6,244 views. That is roughly 1/150 of the dilemma items.
4. **Real worker plus ticking clock plus dignity works as documentary.** The EBS train-driver clip has 1.34M views, against 32K and 18K for two other EBS bathroom and IBS excerpts I checked. It opens with a confession ("그렇게 많이 참아야 될 줄은…"), follows the minutes left, and ends on rights and safety.
5. **Psychology works when it is about rest, framed as a problem.** 세바시 (1.15M) and 뇌과학 쓸래요? (1.41M) are not about bathrooms.
   - Both open on the viewer's fatigue or fear ("제대로 쉬고 계신가요?", "쉬면 불행한 일이 벌어질 것이다").
   - Both name **short-form scrolling as fake rest**, then give simple rules: micro-breaks of 5–10 minutes, breath focus, 50/10 or 25/5, a phone-free hour.
   - Both end by giving permission to rest ("쉬어도 괜찮다", "스스로의 의사").
   - Neither cites specific studies or numbers; 세바시 alludes only generally to micro-break research.
6. **Office-set bathroom hits are few, and short or old.** Only 장삐쭈 (60 s, the studio's own bathroom), 쾌한상사 (2013, a branded sitcom) and SNL (from the US). The phone-in-the-bathroom refuge appears only in a home and couple setting (유머너굴: "3시간 만에 폰 들고 나오는" husband).

### What underperforms

- **Health warnings about phones on the toilet** (hemorrhoids, germs, the 5-minute rule) stay small in Korean: YTN 사이언스 58K (2015), CBS Shorts 12.5K, KBS 11.6K, 도트박사 1.4K, 항문외과 닥터신 915.
  - The best English ones are Brew at 335K (its description opens "You're at work when nature calls") and CNET at 119K.
  - The 2025 125-person single-hospital study (5× more likely to sit over 5 minutes, 46% higher hemorrhoid risk) appears in 도트박사's 1.4K video. It has not driven views.
- **"Bathroom camping"**, the English-language Gen-Z framing of hiding in bathrooms to decompress: 830–10K views across four Shorts (TODAY, 7NEWS, a creator, a local station) and one TV-news segment (Times Now, 1,078).
- **Office-worker coping and slacking tips** (월급루팡, napping and swearing at work): 200–77K.
- **Stock-at-work content:** the "위장 주식 사이트" news pieces got 2.9–4.4K, and personal "화장실 매매" logs got 24–53.
- **Term-led videos:** "화캉스" news got 6.2K (MBC) and a radio clip got 2.1K (철파엠). The coinage has no organic pull on YouTube. Its big number (11.5M) is a likely paid ad that uses it in a home-bathroom sense.

### What is missing (gaps)

- **No Korean video was found that explains 화캉스, or hiding in the office bathroom with a phone, through psychology.** Missing framings include the need for privacy and unobserved time, recovery and micro-breaks, social or emotional exhaustion, autonomy and control, why scrolling there does not refresh, and the guilt of "월급루팡".
  - Searches included 화장실 심리, 화장실에 숨는 심리, 혼자 있고 싶은 심리, 마이크로 브레이크 직장인 and 화장실 휴식 스트레스.
  - The two psychology hits supply the missing half: demand for office-worker rest psychology, with scrolling already named as fake rest.
- **Nothing ties the 9 a.m. full stalls to the market open.** MBC's piece quotes a post saying "이 시간대는 항상 만석" without giving a time. Stock-at-work coverage exists but is tiny.
  - Unverified context from search snippets: the alternative exchange has run 08:00–20:00 trading since March 2025, and KRX after-hours trading to 20:00 started on 2026-09-14 (KBS). That weakens a pure "9 a.m. open" story; check before using it.
- **No office-worker voice in the high-view set.** No interviews, vlogs or confessions from people who 화캉스 got traction: office vlogs reached at most 13K. The successful real-person piece is about workers who can't get to the toilet at all (EBS).

### Channel-relative outliers (from other checked videos of the same channel)

- **EBSDocumentary:** 화장실 전쟁 clip 1,339,319, against 32,221 (IBS, 귀하신 몸) and 17,886 (construction-site toilets). That is 42–75× higher.
- **SBS 뉴스:** the two 뉴스딱 break dilemmas got 1,002,757 and 930,524. Other SBS items checked: a 담배타임 compilation at 301,677, "9시 출근 5시 퇴근" at 45,190, and the 위장 주식 사이트 item at 2,886.
- **Henkel Consumer Brand Korea:** the same 31-s 화캉스 ad got 11,496,209 as a watch video and 135,076 as a Short, which likely reflects paid distribution.
- **MBCNEWS** (both items checked are low): 화캉스 6,244 and 스마트 리빙 phone-in-toilet 6,451.
