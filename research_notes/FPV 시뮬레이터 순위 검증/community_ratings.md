# How the FPV community and players rate FPV simulators (as of 2026-11-11)

Scope: user reviews and community consensus only. Expert reviewers (Oscar Liang etc.) and objective features are covered by another researcher.

All Steam numbers were fetched **2026-11-11, about 07:23–07:40 UTC (16:23–16:40 KST)**.

How to weigh the sources:
- Forum and review quotes are anonymous handles unless noted. Weigh them lightly, as individual opinions.
- DCInside items come from the DCInside search-results listing (title, date and snippet only); full posts and comments were not read. They are marked "(snippet)".
- **Reddit (r/fpv, r/Multicopter) could not be reached** (see Gaps under Q2).

## Q1. Steam user review scores per title (overall and recent, % positive, count, language scope)

### Takeaway
**Liftoff: FPV Drone Racing** and **Uncrashed** have the strongest Steam records:
- Liftoff: 95% of 7,227 English reviews; 97% of 270 Korean reviews.
- Uncrashed: 94% of 2,490 English reviews; 95% of 8,288 all-language reviews.
- Both are about 95% positive in 2026 so far.

**Liftoff: Micro Drones** (93%) comes next. **TRYP FPV** (85%) and the free **FPV SkyDive** (83–84%) are a step below. **DCL – The Game** is the weakest of the established sims at 79% ("Mostly Positive").

**The DRL Simulator has collapsed.** Its all-time label still reads "Very Positive" (84% of English reviews). But only **41% of its last-30-day reviews are positive (12 reviews, "Mixed")**, and only **26% of its 2026 reviews (276)**. Reviewers say its online servers went down in December 2025.

**VelociDrone, Tiny Whoop GO and Propwash FPV are not on Steam**, so they have no Steam score.

### Cited Findings

**Method and scope notes**
- Steam's public `appreviews` JSON endpoint returned **HTTP 302 → storefront** for every request from this environment, so `purchase_type=all` / `language=all` counts were unavailable.
- Figures therefore come from three places:
  - **(a)** The summary rows on each store page, fetched in two views:
    - an English view (`?l=english&cc=us`);
    - a Korean view (`?l=koreana&cc=kr`).
  - **(b)** Steam's public review-histogram endpoint, `store.steampowered.com/appreviewhistogram/<appid>?l=english&review_score_preference=0`. It gives monthly or weekly up/down counts, which I summed.
  - **(c)** `api/appdetails?cc=kr&l=korean` for KRW prices.
- **Language scope of the store summary row:**
  - When a game has enough reviews in the viewer's language, Steam shows a language-specific row: "English Reviews" or "한국어 평가".
  - Otherwise it shows "All Reviews" / "모든 평가", which counts all languages.
  - Only **Liftoff (270)** and **Bodycam (749)** had a Korean-language row in the Korean view.
- **"Recent Reviews" (last 30 days)** showed identical numbers in the English and Korean views. They also roughly match the all-language histogram for the same period. They appear to count **all languages**; this is my inference.
- **Histogram sums run slightly higher than the store's all-language counts** (Uncrashed 8,426 vs 8,288; DRL 4,180 vs 4,067; TRYP 3,297 vs 3,204). The histogram probably also counts reviews that the store score excludes, such as key activations; this is my inference.

**Score table**

Each row's source is its Steam store page: `https://store.steampowered.com/app/<appid>/`. Histogram figures use the endpoint above with the same appid.

The histogram columns (all-time and Jan 1–Nov 11) sum all languages. "Not shown" in the Recent column means Steam displays no recent row for the title, because there are too few reviews.

| Title (appid) | Steam KR price, 2026-11-11 | English-view all-time row | Korean-view all-time row | Recent 30 days | Histogram all-time | Histogram Jan 1–Nov 11, 2026 |
|---|---|---|---|---|---|---|
| [Liftoff: FPV Drone Racing (410340)](https://store.steampowered.com/app/410340/) | ₩25,000 | English: Overwhelmingly Positive, 95% of 7,227 | 한국어: 매우 긍정적, 97% of 270 | Overwhelmingly Positive, 95% of 184 | 94.7% of 14,231 | 95.2% of 2,034 |
| [Liftoff: Micro Drones (1432320)](https://store.steampowered.com/app/1432320/) | ₩17,500 | All languages: Very Positive, 93% of 1,512 | same (모든 평가) | Very Positive, 98% of 50 | 92.1% of 1,539 | 94.5% of 489 |
| [Uncrashed (1682970)](https://store.steampowered.com/app/1682970/) | ₩11,990 (25% off ₩15,990) | English: Very Positive, 94% of 2,490 | 모든 평가: 압도적으로 긍정적, 95% of 8,288 | Very Positive, 91% of 340 | 94.1% of 8,426 | 95.6% of 2,516 |
| [TRYP FPV (1881200)](https://store.steampowered.com/app/1881200/), Early Access since 2022-06-30 | ₩18,500 | English: Very Positive, 85% of 1,295 | 모든 평가: 매우 긍정적, 85% of 3,204 | Very Positive, 88% of 26 | 83.0% of 3,297 | 85.6% of 417 |
| [FPV SkyDive (1278060)](https://store.steampowered.com/app/1278060/) | Free (paid DLC) | English: Very Positive, 84% of 1,923 | 모든 평가: 매우 긍정적, 83% of 3,198 | Very Positive, 90% of 65 | 82.1% of 3,349 | 84.4% of 732 |
| [DRL Simulator (641780)](https://store.steampowered.com/app/641780/) | ₩10,500 (still sold) | English: Very Positive, 84% of 2,229 | 모든 평가: 대체로 긍정적, 79% of 4,067 | **Mixed, 41% of 12** | 78.9% of 4,180 | **26.1% of 276** |
| [DCL – The Game (964570)](https://store.steampowered.com/app/964570/), has Korean UI | ₩35,400 | All languages: Mostly Positive, 79% of 952 | same | not shown | 79.1% of 991 | 84.6% of 91 |
| [FPV Freerider (854250)](https://store.steampowered.com/app/854250/) | ₩6,500 | All languages: Very Positive, 89% of 351 | same | not shown | 88.5% of 358 | 91.9% of 37 |
| [FPV Freerider Recharged (813530)](https://store.steampowered.com/app/813530/) | ₩10,500 | All languages: Very Positive, 88% of 220 | same | not shown | 86.4% of 228 | 95.0% of 20 |
| [Bodycam (2406770)](https://store.steampowered.com/app/2406770/), whole game, not drone-specific; Early Access | ₩37,500 | English: Mostly Positive, 79% of 38,471 | **한국어: 복합적, 69% of 749** | Very Positive, 87% of 3,075 | 79.3% of 71,990 | 84.7% of 33,383 |

**DRL's monthly histogram** shows when it turned — [histogram](https://store.steampowered.com/appreviewhistogram/641780?l=english&review_score_preference=0):
- Before the turn: Nov 2025, 17 up / 5 down.
- **Dec 2025: 20 up / 53 down. Jan 2026: 15 up / 66 down.**
- It stayed net-negative every month through Nov 2026 (Oct 2026: 6 up / 8 down).

**Uncrashed's October 2026 dip:** 309 up / 32 down (90.6%), against Sep 2026 at 198 up / 10 down (95.2%) — [histogram](https://store.steampowered.com/appreviewhistogram/1682970?l=english&review_score_preference=0).

**Other FPV titles that show up in Steam search, often combat-themed** (same method; each links to its store page):
- [FPV Kamikaze Drone (2707940)](https://store.steampowered.com/app/2707940/)
  - ₩6,700; Early Access since 2023-12-15.
  - English: 82% of 2,488. All languages: 86% of 12,372 (매우 긍정적).
  - Recent: 85% of 138. 2026 so far: 82.4% of 2,749.
  - It has the **second-largest review count among dedicated drone titles** checked: 13,728 in the all-language histogram, behind Liftoff's 14,231.
- [The Zone – FPV Drone Simulator (3491280)](https://store.steampowered.com/app/3491280/)
  - Developer Nils Vollenbruch; Early Access since 2025-03-07; ₩15,500.
  - All languages: **97% of 487**. Recent: 98% of 56. 2026 so far: 97.3% of 413.
- [FPV LOGIC (2398030)](https://store.steampowered.com/app/2398030/): ₩21,500; Early Access; 88% of 744; recent 91% of 12.
- [Ukrainian Fight Drone Simulator (2862860)](https://store.steampowered.com/app/2862860/): ₩32,000; released 2025-12-10; 80% of 926; recent 75% of 81 ("Mostly Positive").
- [Remote Reaper: FPV Combat Drone Simulator (3295810)](https://store.steampowered.com/app/3295810/): ₩21,000; 91% of 296; recent 80% of 36.
- [SPLIT FPV: Drone Racing (4348580)](https://store.steampowered.com/app/4348580/): free; Early Access since 2026-08-28; Mixed, 66% of 121; recent 64% of 51.
- [FPV Drone Simulator by DreamEscape (691730)](https://store.steampowered.com/app/691730/): free; Mixed, 67% of 553.
- [FPV Labs (4038160)](https://store.steampowered.com/app/4038160/): Mixed, 65% of 106.
- [ACRODRIFT (3698490)](https://store.steampowered.com/app/3698490/): 80% of 21.

**Not on Steam:**
- **VelociDrone** and **Tiny Whoop GO** returned no results in Steam's store search (`api/storesearch`, terms "Velocidrone", "Tiny Whoop", "Tiny Whoop GO", "TinyWhoop").
  - VelociDrone is sold from its own site — [velocidrone.com](https://velocidrone.com).
  - One DCInside user says they bought it via PayPal ("벨로시드론 다운로드 중..", 2026.05.05) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=3100).
- **Propwash FPV** is a Minecraft mod — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv):
  - 12.7K downloads (12,740 on the Details panel); author "tmlrd"; created "1 month ago"; last updated Oct 17, 2026.
  - Minecraft 26.3 only, Fabric/NeoForge.
  - 70 comments (text not visible) and **no visible ratings**.
  - It is not listed on Modrinth: an API search for "propwash" returned no hits (api.modrinth.com, 2026-11-11).

**Developer attribution check:** the brief says "FPV Freerider (CurryKitten)". Steam lists the developer of both FPV Freerider titles as **"John Holmvall"** — [Steam](https://store.steampowered.com/app/854250/). Verify before printing the CurryKitten attribution.

### Inferences
- Rough Steam tiers by user score in 2026:
  - **≈95%:** Liftoff, Uncrashed, Micro Drones, The Zone (small sample).
  - **≈85%:** TRYP, SkyDive, FPV Kamikaze Drone.
  - **≈80%:** DCL.
  - **Broken:** DRL.
- A creator tier list that puts DRL high in 2026 contradicts current user experience. One that puts DCL top-tier is also out of line with Steam users.
- Steam scores measure buyer satisfaction, including fun. They do not measure physics fidelity: combat-themed titles score in the 80s–90s too. So for "realism", forum opinion (Q2–Q3) matters more than Steam percentages.
- For a Korean user, the Korean store view shows **Liftoff's Korean-only score (97% of 270)**. For most other sims it shows the all-language score. That is why numbers seen in Korea can differ from English-language articles.

### Gaps
- I could not get `purchase_type=all` / `language=all` counts from the official reviews API; it redirected. The histogram is the closest substitute.
- I have no 30-day "recent" figure for small titles (Freerider, DCL), because Steam does not show one.
- There is no public user-score data for VelociDrone, Tiny Whoop GO or Propwash, beyond Propwash's download count.

## Q2. Community consensus on the best sim for beginners, freestyle, racing and tiny whoops

### Takeaway
No forum crowns a single "best" sim. Consensus splits by use:

| Use | Community pick |
|---|---|
| Starting out / all-rounder | **Liftoff** (plus **Liftoff: Micro Drones**) |
| Racing, and "physics reference" | **VelociDrone**, though some veterans dislike it |
| Freestyle and scenery | **Uncrashed** and **TRYP**. **The Zone** is a 2026 newcomer said to have very realistic physics but "far from bedding in" |
| Tiny whoops | **Liftoff: Micro Drones** vs **Tiny Whoop GO** (one veteran preferred GO in 2024 but withdrew his recommendation in 2026) |
| Weak PCs | **FPV Freerider (Recharged)** |

**DRL**, once recommended for its structured tutorial, is now advised against because its servers are down.

In Korea's DCInside FPV gallery, 2026 beginners mostly start on **Liftoff**, then move to or ask about **Uncrashed** and **VelociDrone**. One post explicitly ranks VelociDrone first for racing, with TRYP or FPV Logic for freestyle.

### Cited Findings

**IntoFPV forum, 2025–2026 threads** (anonymous members; small samples)

"First paid FPV sim: Uncrashed or The Zone?" (Jun 27–29, 2026) — [IntoFPV](https://intofpv.com/t-first-paid-fpv-sim-uncrashed-or-the-zone)
- OP **DroneKoorts** has 100 hours in free sims and wants a sim for freestyle/cinematic flying. He wrote: "I will be getting Velocidrone for racing and the community". He ended: "UPDATE: I got Uncrashed!"
- **BadRaven:** "The Zone is new and is IMO far from bedding in. It may make it in time. Uncrashed is well proven and has an active community making scenery, a lot of which is professional standard."
- **Nostradamus:** "The Zone is supposed to have the most realistic physics; it is supposed the feel the most like a real Quad." He added that he has only used Liftoff and The Zone.
- **Bad Raven** (member since 2016): "For years Velocidrone was touted as the most realistic for physics. Likely still is so. I spent ages getting the figures in to "mimic" my Mk5 5" X's and was never fully convinced."
- **Pathfinder075:** "I now keep Liftoff and Micro, for fun and for learning new tricks."
- Thread poll: Uncrashed 1 vote (100%), The Zone 0. Trivially small.

"DRL Drone Racing League Sim Frustration" (Jun 27, 2025 – Jan 17, 2026) — [IntoFPV](https://intofpv.com/t-drl-drone-racing-league-sim-frustration)
- **PBax**, a beginner: "DRL is frequently suggested for its stand-out structured "training" aspect". He returned DRL and bought Liftoff Micro Drones: "Definitely more satisfied".
- **Pathfinder075:** "Liftoff or Liftoff Micro is pretty much where it's at for learning on a semi modern machine. If you have something older Freerider Recharged will work as well."
- **hugnosed_bat:** "i overal like the physics of fpv freerider"
- **QuadFlyer68** (Jan 17, 2026), on DRL: "it fails to "connect to server". Oh joy - they pulled the plug."
- **BadRaven** (Jan 17, 2026):
  - "Prefer Uncrashed for 4" up"
  - On what he calls "Mr Whoop Jesse's Whoop Go" (apparently Tiny Whoop GO): after it "was changed to enforced career and half the sites I'd got (inc bought ones ) suddenly became barred till I "progressed" to them … I lost interest and cannot recommend, shame."
  - "Do not like DRL's physics, IMO very unrealistic." / "Like Velocidrone even less."

"DRL vs LiftOff vs Uncrashed" (Jun–Aug 2024; listed at 21,107 views) — [IntoFPV](https://intofpv.com/t-drl-vs-liftoff-vs-uncrashed)
- **FPVme:** "I like drl the best". Also: "liftoff micro drones. If you fly whoops this is the best sim for that, and the small scale maps really force you to use fine control." But: "I can't say I like liftoff very much, just doesn't feel right to me".
- **BadRaven:**
  - "Uncrashed is my favourite"
  - "DRL is wholly unrealistic IMO"
  - "With Whoop flying, its surprising how little Tiny Whoop Go gets a mention, as IMO its WAY better than LiftOff Micro."
  - "Freerider Rech arged is IMO best choice for budget price and less able computers."
- **props_go_bzzz:** "the one that has improved my flying the most is Velocidrone"
- **Pums:** "Get TRYP. Really nice to tune. Developement is very active. Flight model already very good"

"What's your favorite sim?" (Mar 2023, older) — [IntoFPV](https://intofpv.com/t-what-s-your-favorite-sim)
- **Fret**, not yet flying real quads: "TrypFPV … feels so damn good, and looks the best (Unreal engine 5)". He also reports that "many also say that Tryp feels like the most realistic". This is hearsay.
- **BadRaven:** "Lots of people rate Velocidrone, I don't........... at all."
- **fpvapnea:** "Sim wise i love Tryp and Uncrashed. Do some race practicing in Velocidrone but keep returning to Tryp." On DRL: "its so floaty".
- **Gruv:** "If you are racing, Velocidrone is the way to go. Lots of online racing to get you geared to IRL races."

The only "poll" found is old and tiny. An IntoFPV event poll, "Which simulator do you want to use for our racing event?" (thread started Nov 26, 2017), shows Liftoff 6 votes (66.67%) and VelociDrone 3 (33.33%) — [IntoFPV](https://intofpv.com/t-intofpv-simulator-racing-tournament)

**Korean community: DCInside 1인칭 시점 무인기(FPV) minor gallery and 드론 gallery** (snippets; anonymous)
- "이제막 입문한 사람들 벨로시드론 사라" (2025.10.02) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=1724). The clearest Korean ranking:
  - "언크래쉬드,리프트오프,카미카제 시뮬, FPV logic,tryp 다 해본 소감으로는 벨로시가 1빠따임"
  - "레이싱하고 싶으면 벨로시하고 프리스타일 하고 싶으면 tryp나 로직 ㄱㄱ"
- "좃뉴비는 시뮬레이터 추천이 필요해" (드론 gallery, 2025.03.15): "시뮬 벨로시드론 언크래시드 DRL liftoff 4개 보통 추천 많이하던데" — [DCInside](https://gall.dcinside.com/board/view/?id=drone&no=13942)
- "행님덜 FPV시뮬 벨로시드론 할라카는데" (2025.03.20): "벨로시드론이 LIFT OFF보다 현실성있고 물리엔진 짱짱하대서". This is hearsay. The poster also finds the foreign site hard to buy from and asks for a Korean-translated alternative — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=567)
- "시뮬추천좀유" (2026.07.02): "리프트오프 vs 벨로시드론 vs 언크래쉬드 현실성 1순위". This is a **question** asking which is most realistic, not a verdict — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=3556)
- "안녕하세요 fpv 입문하려는데요." (2026.09.17): "우선 liftoff 인가, 시뮬 있길래 그걸로 입문하려는데 조종기는 라디오마스터 포켓? 얘로 시작하면 될까요?" — [DCInside search](https://search.dcinside.com/post/q/FPV%20시뮬)
- "안녕하세요 드린이입니다…" (2026.10.05–06): "리프트오프로 시뮬하면서 어느정도 넓은공간에서의 비행은 가능한데 좁은..." — [DCInside search](https://search.dcinside.com/post/q/FPV%20시뮬)
- "언크래쉬드 구매해따" (2026.10.30): "리프트 오프 20시간 하고 쉬다가 언크래쉬드 한번 사서 3시간 해봤는데 이게 리프트 오프보다 더 어렵네" — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=4475)
- "이제 벨로시드론으로 넘어갈 때인가" (2026.07.21): "기본 조작과 드론 반응을 익혔고". Per the listing summary, the poster had moved from Uncrashed to VelociDrone gate racing — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=3740)
- "벨로시드론 다운로드 중.." (2026.05.05): "리프트오프, 더 존, 언크레쉬드 하구 있는데" — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=3100)
- "아바타2 시뮬 뭐가 좋나요" (2026.04.21): "레딧에서 벨로시드론 쓰는 사람 설정값 맞춰서 연습해보고 있음". This is indirect evidence that Korean beginners follow Reddit settings — [DCInside](https://gall.dcinside.com/mgallery/board/view?id=fpv&no=2995)
- "저사양 컴퓨터 돌아가는 FPV 시뮬 추천" (2026.08.04): "노트북 구닥다리써서... 어떤 시뮬 써야함? 흙수저 시뮬 알려줘라" — [DCInside search](https://search.dcinside.com/post/q/FPV%20시뮬)
- "폰 FPV 시뮬중에 레전드 찾음" (2026.10.26) recommends the phone app **feelFPV** — [DCInside search](https://search.dcinside.com/post/q/FPV%20시뮬)
- The FPV gallery keeps a beginner info compilation, "FPV입문자를 위한 정보글 모음 (26.10.26 최신화)", which includes "벨로시드론 입문팁" — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=1784)

**Steam store signals by use case** (see the Q1 table): Uncrashed (freestyle) and Liftoff (all-round) score about 95% in 2026. Micro Drones (whoops) scores 94.5% in 2026. TRYP sits at 85.6% — [Steam](https://store.steampowered.com/app/1682970/), [Steam](https://store.steampowered.com/app/410340/), [Steam](https://store.steampowered.com/app/1432320/), [Steam](https://store.steampowered.com/app/1881200/)

### Inferences
- **Beginner:** Liftoff is the community's default "first sim", in both English and Korean forums. The free FPV SkyDive is a common no-cost entry (Q3). Korean posters also push VelociDrone on beginners, but beginners report it is hard (see Q3), so it reads more as "where you go next / for racing".
- **Freestyle:** Uncrashed is the most consistently recommended paid freestyle sim in 2025–26, for its community maps, graphics and score. TRYP is the "looks best / tunable" alternative, but its physics are disputed. The Zone is a promising but young option.
- **Racing:** VelociDrone remains the reference for racing and online competition. It is also the sim veterans most often call "most realistic", although some (BadRaven) dislike it.
- **Whoops:** Liftoff: Micro Drones is the mainstream answer. Tiny Whoop GO has a vocal fan base, but at least one long-time fan now "cannot recommend" it after a career-mode change.
- **2026-specific:** DRL should be in the bottom tier, or flagged "don't buy", for any 2026 list.

### Gaps
- **Reddit was not reachable.** Web search restricted to reddit.com returned "The following domains are not accessible to our user agent: ['reddit.com']". An earlier session note records that old.reddit.com fetches were also blocked.
  - So **no r/fpv or r/Multicopter threads, polls or wiki content are included**.
  - Any claim about "Reddit consensus" in the final report would be unsupported by these notes.
- **RCGroups:** no relevant threads surfaced in search, and none were read.
- **Naver cafes** were not reached; they are typically login-gated. I found no 2026 Korean poll.
- I found **no large-sample poll** (hundreds of votes or more) of which sim pilots use. The only polls found had 1–9 votes.
- I found no official or news confirmation of *why* DRL's servers went down. User reviews report a 503 error from api.drlgame.com since about Dec 17–18, 2025, and one claims the "Company closed". A web search on 2026-11-11 returned no shutdown news.

## Q3. Common complaints and praise per simulator

### Takeaway
- **Liftoff:** praised as a learning tool; criticised for its tutorial flow, optimisation and developer tone.
- **Uncrashed:** praised for graphics, maps and community scenery; criticised for an Oct 2026 update ("bouncing… like it's made of rubber"), older "teaches bad habits" and asset-flip complaints, and difficulty.
- **TRYP:** praised for graphics and Betaflight-style tuning; the most frequent "floaty / moon gravity" physics complaints, plus performance.
- **Micro Drones:** praised for whoop-specific feel; criticised as "should've been a DLC", for thin maps, and for some over-powered models.
- **SkyDive:** praised as free and well optimised; criticised for maps moved behind DLC.
- **DRL:** praised historically for its physics and tutorial; **now unusable online**, with settings not saving.
- **DCL:** launch-era complaints of wrong speed, "no weight" and "moon-like gravity".
- **VelociDrone:** praised for racing and physics; seen as hard and English-only, with an awkward purchase route for Koreans.

### Cited Findings

The Steam reviews below are ranked "most helpful" (English) on each game's community hub unless noted. A date without a year means 2026.

**Liftoff: FPV Drone Racing**
- Praise:
  - "Drunkenly buy this simulator so I can not crash my brand new adult money toy > Spend ~10 hours figuring out how to fly these things > see improvement within days" (May 2, 2023; 200 helpful) — [Steam review](https://steamcommunity.com/id/McDonalds_security/recommended/410340/)
  - "Liftoff taught me to fly, tune, and adjust my Taranis settings" (2,780 h, 2018) — [Steam review](https://steamcommunity.com/profiles/76561198354802849/recommended/410340/)
- Tutorial complaints:
  - "it pauses you and shows a message. You then have to TAKE YOUR HANDS OFF THE CONTROLLER to click "next"" (Feb 1, 2024) — [Steam review](https://steamcommunity.com/profiles/76561198150010359/recommended/410340/)
  - "The way tutorial is organized is absolute rubbish." (May 14, 2026) — [Steam review](https://steamcommunity.com/profiles/76561199835131856/recommended/410340/)
- Optimisation, from a self-described "freestyle/race pilot of 3 years": "absolutely TERRIBLE optimization" (Dec 9, 2019; 309 helpful) — [Steam review](https://steamcommunity.com/profiles/76561198326193524/recommended/410340/)
- Developer conduct: "The game itself is fun and the flying feels great, but … They are extremely defensive and rude whenever anyone leaves a negative review." (May 6, 2026) — [Steam review](https://steamcommunity.com/profiles/76561199059052216/recommended/410340/)
- Korean (snippet): "리프트오프 삿는데 먼가먼가 맘에 안드네" — "그냥 먼가 별로임... 언크래쉬드나 사볼까...." (2026.09.28) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=4280)

**Liftoff: Micro Drones**
- Praise:
  - "Finally a sim that replicate the tricky flight differences between whoops and 5" quad copter sims correctly. You feel that battery sag and throttle control quirks" (Dec 1, 2021) — [Steam review](https://steamcommunity.com/id/buglish/recommended/1432320/)
  - "Piloting one of these drones with a regular controller is not easy" (Dec 1, 2021) — [Steam review](https://steamcommunity.com/id/bloodyspasm/recommended/1432320/)
- Value and map complaints:
  - "why is this a standalone game with so few (and small) maps instead of a DLC" (Mar 14, 2025) — [Steam review](https://steamcommunity.com/profiles/76561198046649313/recommended/1432320/)
  - "with the thin map lineup, mid graphics and price I can't recommend this over base Liftoff. This should've been a DLC." (Jul 3, 2025) — [Steam review](https://steamcommunity.com/id/ProtoFinnoYakubianSnowDemon/recommended/1432320/)
- Physics complaints:
  - "the physics is horrible … The Air65 in the game should be called Air6500 … I clocked 80km/h with it" (May 22, 2026) — [Steam review](https://steamcommunity.com/profiles/76561198009529495/recommended/1432320/)
  - "too drifty … Way harder than my real Moblite 7 and tinyhawk 3 tinywhoops" (Feb 17, 2022) — [Steam review](https://steamcommunity.com/profiles/76561198914077709/recommended/1432320/)

**Uncrashed**
- Praise:
  - "Great for practicing FPV!" (Apr 26, 2024) — [Steam review](https://steamcommunity.com/profiles/76561199447525289/recommended/1682970/)
  - "Very very cool sim Only problem is the gravity, to simulate it as close to reality set it at 13.84" (Nov 23, 2025) — [Steam review](https://steamcommunity.com/profiles/76561198427360041/recommended/1682970/)
  - IntoFPV: "UnCrashed has some of the most fantastic graphics" (SeismicCWave, Jun 27, 2025) — [IntoFPV](https://intofpv.com/t-drl-drone-racing-league-sim-frustration)
  - IntoFPV: "active community making scenery, a lot of which is professional standard" (BadRaven, Jun 27, 2026) — [IntoFPV](https://intofpv.com/t-first-paid-fpv-sim-uncrashed-or-the-zone)
- Recent update complaint: "After the latest update, the game is absolute garbage … the drone behaves like it's made of rubber, bouncing all over the place" (Oct 29, 2026) — [Steam review](https://steamcommunity.com/profiles/76561199887743239/recommended/1682970/)
  - The negative share rose in Oct 2026 (Q1).
- Realism (older): "it doesn't fly like a real drone at all. If you intend to train in this game before you first real FPV flight, don't, because this gamer will teach you bad habits" (Nov 5, 2021) — [Steam review](https://steamcommunity.com/id/echeion/recommended/1682970/)
- Launch-era asset complaint: environments "purchased and put in the game", e.g. "Urban Bando" said to be "Urban Abandoned District" by Scans Factory (Sep 2, 2021; 358 helpful) — [Steam review](https://steamcommunity.com/id/BlueCheese420/recommended/1682970/)
- Handling detail: SeismicCWave flagged Uncrashed's roll/yaw coupling (Aug 3, 2024) — [IntoFPV](https://intofpv.com/t-drl-vs-liftoff-vs-uncrashed)
- Korean (snippets):
  - Harder than Liftoff (2026.10.30) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=4475)
  - "메인으로는 물리엔진이 v2 버전이 나옴 크게 개선한 버전으로" (2024.12.10) — [DCInside](https://gall.dcinside.com/board/view/?id=drone&no=13303)
  - "4시간 연습해봤는데 칸 하나 통과하기도" (2025.03.30) — [DCInside](https://gall.dcinside.com/board/view/?id=drone&no=14076)
  - "그땐 언크래쉬드 튜토리얼도 제대로 못 했음" (2025.07.21) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=1303)

**TRYP FPV** (still Early Access)
- Praise:
  - "the addition of Beta flight Code and PIDs have set this simulator above the rest. Velocidrone has taken a back seat to TRYP" (1,132 h; Dec 16, 2023) — [Steam review](https://steamcommunity.com/profiles/76561199382919249/recommended/1881200/)
  - "Probably the best FPV simulator on Steam. I am as a professional FPV pilot I highly recommend it!" (self-described, unverified; Dec 4, 2023) — [Steam review](https://steamcommunity.com/id/spar44/recommended/1881200/)
- Physics complaints:
  - "Physics- awful - nothing like the real thing" (refunded; Sep 20, 2025) — [Steam review](https://steamcommunity.com/profiles/76561198210425221/recommended/1881200/)
  - "Feels like you're on the moon. If you practice on this and get used to it you'll likely perform worse in real life" (Dec 19, 2024) — [Steam review](https://steamcommunity.com/profiles/76561198056778352/recommended/1881200/)
  - "recent physics updates make it feel very sluggish … the drone still "floats" to the side unrealisticly" (Mar 7, 2025) — [Steam review](https://steamcommunity.com/profiles/76561199209458868/recommended/1881200/)
  - Even a positive review says "a little too floaty" (Apr 3, 2023) — [Steam review](https://steamcommunity.com/profiles/76561199379730265/recommended/1881200/)
- Performance: "best looking sim for FPV...thats everything positiv". The game advises against a "resolution scale over 60% because of performance issues" (Jun 22, 2024) — [Steam review](https://steamcommunity.com/id/extrezzcs/recommended/1881200/)
- Context: TRYP's studio helped Bodycam add radio support and tune its drone. See the earlier session notes — [Steam news](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)

**FPV SkyDive (Orqa, free)**
- Praise:
  - "Free - Great graphics - Well optimized (over 600 fps …)". The same reviewer adds: "somethig off with the physics … too much inertia" (May 1, 2020) — [Steam review](https://steamcommunity.com/profiles/76561198079779621/recommended/1278060/)
  - "Very very good for FPV beginners" (May 17, 2020) — [Steam review](https://steamcommunity.com/profiles/76561199023054337/recommended/1278060/)
  - "they fixed all of my complaints" (Jul 11, 2023) — [Steam review](https://steamcommunity.com/id/KAIN_-/recommended/1278060/)
- Monetisation complaints:
  - "They also put my favorite map behind a paywall". The same reviewer says it "won't run on Mac anymore" (Sep 25, 2023) — [Steam review](https://steamcommunity.com/profiles/76561198025017108/recommended/1278060/)
  - "Free, yet still a poor value. The game comes with one machine and only a few small maps" (Dec 18, 2023) — [Steam review](https://steamcommunity.com/id/katanah/recommended/1278060/)

**DRL Simulator**
- Historic praise:
  - "Physics 3.0 update of the DRL simulator makes it closer to real life than it has ever been. Excellent tutorial mode for new pilots" (Mar 14, 2019). The review is from Steam profile id "joshuabardwell"; that it belongs to the YouTuber Joshua Bardwell is unverified — [Steam review](https://steamcommunity.com/id/joshuabardwell/recommended/641780/)
- Server collapse:
  - "The API[api.drlgame.com] is giving a 503: Server Error code, and the main game website[thedroneracingleague.com] is giving a 403 … The game hangs on launch" (Dec 18, 2025; 63 helpful) — [Steam review](https://steamcommunity.com/id/arduino_88/recommended/641780/)
  - "requires connecting to it for most of it's functionality, even saving your own race times and drone settings" (Jan 3, 2026) — [Steam review](https://steamcommunity.com/profiles/76561198070122257/recommended/641780/)
  - "it was a good game before the servers went down. The physics feel accurate … you will need to enter all your settings every time you play" (Mar 11, 2026) — [Steam review](https://steamcommunity.com/profiles/76561199778157851/recommended/641780/)
  - "will let you play 8 missions. after that, requires online and cant connect" (Sep 21, 2026) — [Steam review](https://steamcommunity.com/id/desmodus/recommended/641780/)
  - "Online server no exist. Game no fun now. Get yourself Uncrashed or Tryp FPV instead!" (Oct 8, 2026) — [Steam review](https://steamcommunity.com/id/roartiz/recommended/641780/)
  - "Company closed, online mode no longer available" (Sep 13, 2026). This is **unverified**: a web search on 2026-11-11 surfaced no news report of a DRL company or simulator shutdown — [Steam review](https://steamcommunity.com/profiles/76561198984770857/recommended/641780/)
- Workaround: "The official servers are down, but the community has created custom servers. You just need to install a simple patch" (Jun 20, 2026, Recommended) — [Steam review](https://steamcommunity.com/id/L1nc3d/recommended/641780/)
- Older physics criticism:
  - "DRL is wholly unrealistic IMO with its throttle giving little or no reaction" (BadRaven, 2024) — [IntoFPV](https://intofpv.com/t-drl-vs-liftoff-vs-uncrashed)
  - "its so floaty" (fpvapnea, 2023) — [IntoFPV](https://intofpv.com/t-what-s-your-favorite-sim)

**DCL – The Game** (all launch-week reviews, Feb 18–19, 2020)
- "They have got the speed way wrong, you feel like a tractor at 130kph. Back to liftoff it is!" — [Steam review](https://steamcommunity.com/id/bossjamienl/recommended/964570/)
- "no weight to it … a bit lifeless" — [Steam review](https://steamcommunity.com/id/ckyman/recommended/964570/)
- "constantly asking me to reconnect to online and race times not saving … Got to fly full throttle or u fall out the sky" — [Steam review](https://steamcommunity.com/profiles/76561198929976374/recommended/964570/)
- A SkyDive reviewer contrasts SkyDive with "DCL with its "moon like" gravity" (May 1, 2020) — [Steam review](https://steamcommunity.com/profiles/76561198042623305/recommended/1278060/)
- There is little 2026 activity: 91 reviews this year (Q1).

**VelociDrone** (no Steam reviews; forum opinions)
- Pro:
  - "If you are racing, Velocidrone is the way to go" — [IntoFPV](https://intofpv.com/t-what-s-your-favorite-sim)
  - "improved my flying the most" — [IntoFPV](https://intofpv.com/t-drl-vs-liftoff-vs-uncrashed)
  - "touted as the most realistic for physics. Likely still is so" (2026) — [IntoFPV](https://intofpv.com/t-first-paid-fpv-sim-uncrashed-or-the-zone)
- Con: "Like Velocidrone even less" (BadRaven, 2026) — [IntoFPV](https://intofpv.com/t-drl-drone-racing-league-sim-frustration)
- Korean posts (snippets):
  - "벨로시드론 원래 어려움?" (2026.03.31): beginner maps feel hard — [DCInside search](https://search.dcinside.com/post/q/벨로시드론)
  - "어으 멀미 너무 심하다;;" (2026.08.16): motion sickness — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=3937)
  - Mobile version: "결제했는데 들어가니깐 다 영어여서" (2026.08.31) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=4074)
  - Mobile price doubt: "무료 시뮬에 비해 물리 법칙 좋겠지? 하 씨 치킨 하나 값인데" (2025.03.16) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=535)

**FPV Freerider / Freerider Recharged**
- "best choice for budget price and less able computers" (BadRaven, 2024) — [IntoFPV](https://intofpv.com/t-drl-vs-liftoff-vs-uncrashed)
- "Freerider will run on a 2nd Gen Intel Laptop with Intel Graphics" (Pathfinder075, 2023) — [IntoFPV](https://intofpv.com/t-what-s-your-favorite-sim)
- On physics, two members disagree:
  - "As Hug mentioned the physics isn't great, but you are learning to fly and gaining muscle memory" (Pathfinder075, 2025) — [IntoFPV](https://intofpv.com/t-drl-drone-racing-league-sim-frustration)
  - hugnosed_bat, in the same thread: "i overal like the physics of fpv freerider" — [IntoFPV](https://intofpv.com/t-drl-drone-racing-league-sim-frustration)

**Tiny Whoop GO** (not on Steam)
- 2024: "IMO its WAY better than LiftOff Micro" — [IntoFPV](https://intofpv.com/t-drl-vs-liftoff-vs-uncrashed)
- 2026, the same member, after a career-mode change locked previously owned sites: "I lost interest and cannot recommend" — [IntoFPV](https://intofpv.com/t-drl-drone-racing-league-sim-frustration)

**The Zone** (new, Early Access)
- Steam: 97% of 487 — [Steam](https://store.steampowered.com/app/3491280/)
- Forum: "supposed to have the most realistic physics" vs "new and is IMO far from bedding in" (Jun 2026) — [IntoFPV](https://intofpv.com/t-first-paid-fpv-sim-uncrashed-or-the-zone)

**Combat-themed titles** (FPV Kamikaze Drone, UFDS, Remote Reaper)
- They have big Steam numbers (Q1), but show up only marginally in hobbyist threads:
  - A 2025 Korean post lists "카미카제 시뮬" among sims tried, then ranks VelociDrone first — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=1724)
  - A 워리어플랫폼 gallery post (2026.04.21): "나는 언크래쉬드 라는 시뮬레이션 외에도 참고로 자폭드론 시뮬레이터 연습중임" — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=warriorplatform&no=79876)

### Inferences
- **"Floaty" is the most common physics complaint across sims.** It is most often aimed at TRYP, then DRL and DCL ("moon-like"). Uncrashed's 2026 complaints are about crash and bounce behaviour after an update, not floatiness.
- **Price complaints** focus on DLC models (SkyDive maps behind paywalls; Micro Drones "should've been a DLC"), not on the base price. Most base games are ₩6,500–₩25,000 on Steam KR. DCL (₩35,400) and Bodycam (₩37,500) are the dearest titles checked.
- **"Server status" is now a real buying criterion**, because of DRL. Sims that need online accounts carry this risk; DCL reviewers also complained about forced reconnects in 2020.
- **Controller setup** comes up mostly as beginners asking which radio to buy (Radiomaster Pocket/Boxer, DJI FPV Controller 3) and as "gamepad is hard" comments. No sim is praised for gamepad play.

### Gaps
- Steam "most helpful" lists skew toward older reviews. 2026-dated quotes exist for DRL, Liftoff, Micro Drones and Uncrashed. For TRYP, SkyDive and DCL the most helpful critical reviews are from 2020–2025.
- I could not read full DCInside posts or comments, only search snippets.
- I found no community evaluation of FPV Kamikaze Drone, UFDS or Remote Reaper from FPV hobbyist forums.

## Q4. Community views on using non-simulator games (Bodycam, Minecraft mods) as FPV practice

### Takeaway
I found **no FPV-hobbyist thread** (IntoFPV, or the DCInside FPV gallery) **recommending Bodycam or a Minecraft mod as a substitute for a dedicated simulator**.

On Bodycam, self-described pilots give moderate verdicts ("fly okay", "Flies decent"), and the game lacked native radio support until v0.9, due 2026-11-13. Korean Bodycam players like the drone as a game element, and one hopes to use it "as a simulator if the flight feel is OK".

For Propwash FPV, the only claims are the mod author's own. Its 12.7K downloads and 70 comments give no readable verdict.

The broader forum view: even dedicated sims "aren't real life", and a poor flight model "will teach you bad habits". By that logic, game modes are weaker training tools.

### Cited Findings

**Bodycam** (from this session's earlier notes; anonymous Steam users; v0.8 flight model)
- "the drones fly okay using a xbox controller if you already know how to fly" (Jastool, Sep 2, 2026) — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/)
- "Flies decent" (Jastool, Sep 3, 2026) — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
- The developer's own note: "FPV drones cannot use dedicated radio controllers in this update" (2026-09-02). Native radio support, built with TRYP FPV, comes with v0.9 (due 2026-11-13) — [Steam news](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066); [Steam news](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)

**Korean Bodycam gallery** (snippets)
- "이렇게 그래픽 좋은 시뮬이 없어서 비행감만 괜찮으면 그냥 시뮬레이터로 쓰고싶다" ("fpv 보고 헐레벌떡 달려옴", 2026.08.25). This is a conditional hope, not a verdict — [DCInside search](https://search.dcinside.com/post/q/FPV%20시뮬)
- "FPV 시뮬은 보통 2~3만원대 가격으로 형성되어있음" ("밑에 FPV 개발자 영상에 관하여 궁금해 할만한 것들 답", 2026.08.26) — [DCInside search](https://search.dcinside.com/post/q/FPV%20시뮬)
- From the earlier session notes: "드론 시뮬레이터 질린 참이었는데 이 게임이 딱이네" (2026.09.07) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=bodybodycam&no=2037)
- The Korean FPV gallery's only Bodycam post found was a kill clip: "게임이 너무 리얼해서 소름돋음ㄷㄷ" (2026.09.13) — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=4175)

**Bodycam Steam score in Korea:** the whole game is 한국어 평가 복합적, 69% of 749. This is not drone-specific — [Steam KR](https://store.steampowered.com/app/2406770/?l=koreana)

**Minecraft: Propwash FPV**
- The author's claims: "A realistic FPV drone racing and freestyle simulator"; "Rigid-body flight model with motor/ESC/battery physics, rotor aerodynamics, ground effect, prop wash, wind and gusts"; radios supported only in "USB Joystick (HID) mode" — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv)
- The listing has no visible ratings, and its 70 comments are not readable — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv)
- Other Minecraft drone mods exist, per a search summary only: "FPV Drones" on Modrinth, "FPV Drones: Acro & Racing", and military-themed packs — [Modrinth](https://modrinth.com/mod/fpvdrones); [ModpackIndex](https://www.modpackindex.com/mod/233359/fpv-drones-acro-racing)

**General forum stance on sims vs. reality**
- "sims are just about getting the muscle memory for tricks and having a sandbox that you can train in. They aren't real life and never will be" (Pathfinder075, 2024) — [IntoFPV](https://intofpv.com/t-drl-vs-liftoff-vs-uncrashed)
- "You can spend 100 hours in Sims, but in that first hour of real flight you will learn more about flying than you could in the previous 100." (Pathfinder075, Jun 28, 2026) — [IntoFPV](https://intofpv.com/t-first-paid-fpv-sim-uncrashed-or-the-zone)
- "don't accept the default as being "it"" — tune settings and weather (BadRaven, 2023) — [IntoFPV](https://intofpv.com/t-what-s-your-favorite-sim)
- Steam reviewers warn that unrealistic physics trains bad habits:
  - "this gamer will teach you bad habits" (Uncrashed, 2021) — [Steam review](https://steamcommunity.com/id/echeion/recommended/1682970/)
  - "you'll likely perform worse in real life" (TRYP, 2024) — [Steam review](https://steamcommunity.com/profiles/76561198056778352/recommended/1881200/)

### Inferences
- Community evidence supports treating Bodycam and Minecraft mods as **fun side-practice at best, not a replacement** for a dedicated sim plus a real radio.
  - Bodycam's v0.9 radio support may change pilot opinion. No reception data exists yet as of 2026-11-11.
- A creator tier list that ranks Bodycam or Propwash above dedicated sims would be out of step with every hobbyist source found here. This is an inference from absence of support, not from an explicit poll.

### Gaps
- Reddit was inaccessible, so r/fpv views on Bodycam or Minecraft mods are unknown.
- I found no IntoFPV or RCGroups thread on Bodycam or Minecraft as practice.
- I found no independent pilot review of Propwash's flight model.
