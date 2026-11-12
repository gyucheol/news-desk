# Where the "game drones now feel very close to real" claim comes from (TRYP FPV, Minecraft Propwash FPV, Bodycam), and a yardstick for judging it

Researched 2026-11-11/12. It reflects the state as of 2026-11-11 unless a later date is given. View counts were read on 2026-11-12. This file adds to, and does not repeat, the earlier notes `바디캠 드론과 실제 FPV 조종 비교/real_fpv_and_simulators.md`, `…/pilot_and_community_views.md`, `…/reels_content.md`, `FPV 시뮬레이터 순위 검증/community_ratings.md` and `…/reel_tier_list.md`. Where I lean on them I say "(earlier notes)".

Evidence labels:
- **(page)**: read on the page itself, or in its primary data such as the Steam API.
- **(RSS)**: full video description, publish time and view count from the channel's public YouTube RSS feed.
- **(TikTok data)**: caption, timestamp, counts and the `isAd` flag from TikTok's own page data.
- **(listing)**: title and view count from a YouTube search listing only.
- **(snippet)**: a search-engine summary or snippet only. Weigh these lightly.

I did not watch or transcribe any YouTube video's speech. A caption download was blocked by this session's permission system, and I did not retry it. So creators' spoken verdicts are unknown unless their written description states them.

Korean glosses for the writer:
- rates = 레이트
- expo = 엑스포
- thrust-to-weight = 추력 대 무게비
- inertia/momentum = 관성
- prop wash = 프롭워시. This is the wobble a quad gets from its own propellers' disturbed air, mainly when it drops or turns hard.
- ground effect = 지면 효과
- voltage sag = 전압 강하
- PID loop = 자세 제어 루프
- latency = 지연
- step response = 스텝 응답. This is how quickly and cleanly the quad follows a sudden stick command.
- blackbox log = 블랙박스 비행 기록

## Q1. Which 2026 posts claim that drones in TRYP FPV, Minecraft (Propwash) or Bodycam feel "real", in what exact words, by whom, and with what affiliation?

### Takeaway
I found **no source that says "very close to real", or "the same as real", about all three games together**. The claim looks like a compression of separate claims about each game. These fall into three tiers:

1. **Developers' own marketing has the strongest wording:**
   - TRYP: "the most realistic FPV flying experience ever created" and "adjusted every nuance… to match reality".
   - Bodycam narration: "Same movement, same precision, same everything".
   - Propwash: "realistic…", "checked against blackbox logs".
2. **Enthusiastic FPV content creators**, with no visible sponsorship:
   - DRONARCHY on Bodycam: "Ultra realistic" and "Learn FPV here if you want to".
   - SubTwoFifty on Propwash: "genuine FPV sim".
3. **A few hedged verdicts from self-described pilots.** For example, Bodycam "almost feels like Liftoff… Not quite Velocidrone level yet".

The **only source that rates all three, SubTwoFifty's tier list, ranks them far apart**: TRYP S, Propwash A, and Bodycam C ("Rubbish as a sim"). That contradicts a blanket "all three are close to real".

TRYP and Bodycam are also **commercial partners**. TRYP's team tuned Bodycam's drone for v0.9, so any "Bodycam flies like TRYP" claim from either side is not independent.

### Cited Findings

**A. Developer and marketing claims (affiliated by definition)**

*TRYP FPV.* Developer and publisher UNDEAD BATTERY; on Steam since 2022-06-30 (Early Access).
- Steam store text (page, 2026-11-12):
  - "With TRYP FPV , immerse yourself in the most realistic FPV flying experience ever created."
  - "…this simulator pushes the boundaries of realism with stunning graphics and ultra-accurate flight sensations."
  - "ultra-realistic flight simulation manage with the PID loop : Inertia and gravity management: Every turn and speed change has been fine-tuned so your drone responds as it would in real-life conditions."
  - Short description: "hyper-realistic visuals and flight sensations".
  - Source: [Steam appdetails API, TRYP](https://store.steampowered.com/api/appdetails?appids=1881200&l=english)
- TRYP's own Steam news shows the claims escalating and then being walked back (page). Source for all four posts: [Steam News API, TRYP (22 items)](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
  - **2024-06-26**, "SOME LEAKS ABOUT OUR VISION":
    - "we want to give you the most realistic FPV Simulator ever."
    - "Our tool, "Physics Matcher", will analyze a blackbox to get the right aerodynamics, motors, acceleration, gyro, position, PID, Rates at each moment with decimeter precision."
  - **2024-12-19**, "ONLINE RACING (Leaderboard), PHYSICS IMPROVED…":
    - "we've unlocked an unprecedented level of realism through the innovative use of digital twins technology."
    - "Ultra-Realistic Flight Physics 🦾 Using digital twin technology, we've adjusted every nuance of the drone's behavior to match reality."
  - **2025-12-18**, "MAJOR IMMERSION UPDATE": "You will immedtialy feel the difference and the accuracy We still do not consider our physics to 1.0, as our PHYSICS MATCHER System is not yet deployed, and the customisation experience need more rework - use the simplified physics factor for an easy tweak."
  - **2026-06-02**, "MASSIVE UPDATE": "a complete aerodynamic rework covering propwash and prop grip (WIP, this will be improve in the next weeks after your feedbacks), a full LiPo battery simulation, propeller damage…"
- What the news feed does not contain (page):
  - The newest of TRYP's 22 Steam news items is the 2026-06-15 hotfix.
  - **None of the 22 items, from 2022-07-13 to 2026-06-15, mentions Bodycam or Reissad.**
  - None announces that the "Physics Matcher" has shipped.
  - Source: [Steam News API, TRYP](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)

*Bodycam (Reissad Studio, developer and publisher).* The wording is already recorded in the earlier notes:
- Store page: "faithfully recreates authentic FPV piloting with realistic flight physics".
- Roadmap, 2026-03-06: "realistic handling, based on real physical properties, like a real simulation".
- v0.8 note: calls TRYP "an ultra-realistic flight simulator".
- v0.9 note: TRYP "gave us a lot of feedback on how our drone flies".
- A narrated reel posted 2026-08-19 by a reactor account, apparently developer devlog material (unverified): "if you've already flown one in real life, you can do the same exact thing here. Same movement, same precision, same everything."
- Sources: [Steam store](https://store.steampowered.com/app/2406770/Bodycam/); [v0.9 Steam news](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981); [reel 2](https://www.instagram.com/reel/DcOcxWci_EO/) (earlier notes)
- Korean press relay: 경향게임스 (2026-11-11) says connecting an FPV controller lets players "보다 현실적인 드론 조작을 경험할 수 있다". This repeats the developer's announcement; it is not a test. — [경향게임스](https://khgames.co.kr/news/articleView.html?idxno=310235) (earlier notes)

*Propwash FPV (Minecraft mod).* Author "lardtom", GitHub LardTom; not on Steam.
- Official site (page, 2026-11-12):
  - "Propwash runs its own flight model."
  - **"Since 0.5.0 the physics is checked against blackbox logs of real drones from a 65 mm whoop to 7″."** The site gives no method, accuracy figure or drone list.
  - "If you want it easier, the world rules have the presets Training and Arcade."
  - "The world around it is still Minecraft, of course."
  - Current version 0.5.2.
  - It is "not affiliated with Betaflight, EdgeTX, OpenTX or any drone manufacturer".
  - Source: [propwashfpv.com](https://propwashfpv.com/)
- GitHub README (page):
  - "a realistic FPV drone simulator mod for Minecraft"
  - "Propwash has its own flight model with a Betaflight-style flight controller"
  - It contains no validation method or results, and no mention of TRYP, Bodycam or any sponsor.
  - Source: [GitHub LardTom/propwash-fpv](https://github.com/LardTom/propwash-fpv)
- **"Minecraft drones" is not one thing.** Other Minecraft FPV projects with their own physics include:
  - FPVCraft on CurseForge. A search summary says it has acro/angle modes, Betaflight rates and battery sag (snippet). — [CurseForge FPVCraft](https://www.curseforge.com/minecraft/mc-mods/fpvcraft)
  - The minecraftfpv.com server/mod, linked in a Korean creator's video (see B). — [YouTube 김아노](https://www.youtube.com/watch?v=GJQygVIGcV8) (listing)
  - Military add-ons, e.g. "Propwash: Payloads – Official Trailer | FPV Strike Drones in Minecraft" (Michalien112) — [YouTube](https://www.youtube.com/watch?v=FWM5HiqfCkU) (listing)

**B. Creator claims, Sep–Nov 2026, with affiliation checks**

*DRONARCHY* is the creator who most clearly covers two of the three games (Bodycam and Propwash).
- Accounts: TikTok @dronarchy, 29,500 followers, bio "👑 Raising the FPV Bar / 💥 Trick Architect | Dexpilot". Also on YouTube ("Dronarchy") and Instagram (dronarchy.fpv).
- **2026-09-06 04:31 UTC, TikTok:** "👑 BodyCam FPV Banger. Next gen FPV simulator within an FPS game. Ultra realistic vs real life footage. #bodycam #drone #fyp #gamers @Bodycam Game"
  - 22,000 views, 916 likes. TikTok `isAd: false`.
  - Source: [TikTok](https://www.tiktok.com/@dronarchy/video/7682275044445244702) (TikTok data)
- **2026-09-08 12:54 UTC, TikTok:** "👑 Bodycam FPV Maxxing. The physics feel and perform really good while flying the drone mod. Fun dexstyle acrobatics for the fam. Ruthless ripping in this game. Insame graphics and realism. @Bodycam Game #bodycam #drone #gaming #fps"
  - **658,700 views**, 41,800 likes, 905 comments, 5,741 shares. `isAd: false`.
  - Source: [TikTok](https://www.tiktok.com/@dronarchy/video/7683146943647730974) (TikTok data)
- **2026-10-02 02:11 UTC, TikTok:** "👑Top FPV Mod on Minecraft? Check @Propwash FPV new masterpiece. Tons of customizable options, and plenty of configurations to play with. #minecraft #game #gamers #drone #dronarchy"
  - 49,900 views. `isAd: false`.
  - Source: [TikTok](https://www.tiktok.com/@dronarchy/video/7691887226451496222) (TikTok data)
- **2026-10-25, YouTube "Bodycam Master FPV (Tips & Drills)":** "Fun drills, DeXstyle combos and basic acro tricks to practice… Practice and enjoy FPV!" — [YouTube](https://www.youtube.com/watch?v=oPEfwj6ePyY) (RSS)
- **2026-11-11, YouTube "Bando Mayhem Bodycam FPV"** (2,932 views): "This drone mod on Bodycam is out of this world. Ultra realism packed with tight architecture. Learn FPV here if you want to. Excellent first person shooter for the real gammers. @ReissadStudio" — [YouTube](https://www.youtube.com/watch?v=sq5UNdelWO8) (RSS)
- Affiliation check:
  - All three TikToks carry `isAd: false`, with no #ad or #sponsored. The captions tag the games' accounts (@Bodycam Game, @Propwash FPV, @ReissadStudio).
  - His Instagram Bodycam reel also tags @radiomasterrc, a radio maker (earlier notes). A web search found no RadioMaster sponsorship listing.
  - Sources: [TikTok](https://www.tiktok.com/@dronarchy/video/7683146943647730974) (TikTok data); [Instagram reel](https://www.instagram.com/reel/DdAazp8N6O1/) (earlier notes)

*SubTwoFifty* (Kyle Macinnes; UK; bio describes a drone photo and video business) is **the only source found that rates all three games**. Details are in the earlier notes.
- Part 9 (2026-09-29) on Propwash:
  - Caption: "A mod that turns Minecraft into a genuine FPV sim… real physics…"
  - Narration: "Genuinely close to perfect for what it's trying to do". Tier A.
- 24-sim tier list (2026-11-10):
  - TRYP: "After the new update, this is the best feeling sim I've tried." (S)
  - Propwash: "flies brilliantly" (A)
  - Bodycam: "A shooter with a kamikaze drone. Rubbish as a sim." (C)
- No sponsorship found. TikTok marks Part 9 `isAd: false`.
- Sources: [tier list](https://www.instagram.com/reel/Dfkss5XqOJt/); [Part 9](https://www.instagram.com/reel/Dd4og-ro2it/) (earlier notes)

*Other Bodycam pilot-creators, Sep 2026:*
- **Dre The Drone Guy**, "Real FPV Pilot Tries Bodycam Game Update - This is INSANE!" (2026-09-12; 6,169 views). Description, verbatim:
  - "DISCLAIMER: This is a video game… I connected my Tx16s MkIII radio. These are the first two days of me trying the new update to Bodycam by Reissad Studio."
  - "It feels pretty good and has lots of options to fine tune your controller through rates and expo. I am constantly changing these. I first started by using a PS4 controller so yes, some of these clips are from Radiomaster AND PS4."
  - **"It almost feels like Liftoff but needs a little adjusting. Not quite Velocidrone level yet with accuracy and racing."**
  - "But that being said, they did an INCREDIBLE job integrating FPV into a video game"
  - Source: [YouTube](https://www.youtube.com/watch?v=-OL_B01imJU) (RSS)
- **Gabrilov**, "How a 2000h FPV Pilot plays bodycam..." (2026-09-05; 2,096 views). The description says only that he flies "using a real FPV controller"; it gives no verdict. — [YouTube](https://www.youtube.com/watch?v=HXoahmgAFOM) (RSS)
- **Marcus Daelander**:
  - "Did Bodycam Accidentally Create the Best Combat FPV Sim?" has **736,626 views** (listing). It is not in his latest-15 feed; the earlier notes put it in early September 2026.
  - Sep 13 Shorts and guide (RSS): "clean, surgical control in Bodycam instead of floaty movement".
  - His descriptions carry a business/collaborations contact but no sponsorship disclosure.
  - Sources: [YouTube](https://www.youtube.com/watch?v=nwkjwMOAB_4) (listing); [YouTube guide](https://www.youtube.com/watch?v=fC0fVJtG3oQ) (RSS)
- **NitroOnAir**, "What Happens When You Actually Know How to Fly FPV in BODYCAM?" (246,034 views, listing).
  - The earlier notes say he trained in Uncrashed, a dedicated sim.
  - His channel's recent uploads are Arma Reforger and Bodycam milsim clips, so he is a milsim gamer, not a credentialed pilot.
  - Sources: [YouTube](https://www.youtube.com/watch?v=kqvw-i8uxKg); [channel RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UCwK0seYcYslGnbqMTEif7_A)

*Korean-language posts:*
- **쪼선생 JJO TEACHER**, "실사 현대전 게임에 들어간 FPV 드론은 어떤 느낌일까?" (2026-09-08; 120,616 views).
  - Chapters: "00:32 컨트롤러 연결 및 테스트 비행 / 02:24 실제 PVP 장면들 / **05:16 세팅 바꾸고 날렵해진 모습** / … / 10:28 총평".
  - **Despite "TEACHER" in the name, this is a Valorant/CS2 FPS channel, not a drone instructor.** His other uploads are about Valorant and CS pros. One of them discloses a sponsor in its title ("AMD Korea X 컴퓨존 협찬"); this Bodycam video carries no sponsorship tag.
  - The title is a question, not a claim.
  - Sources: [YouTube](https://www.youtube.com/watch?v=kmKlAzkwjFQ) (RSS); [channel RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC7vyTwJjcUdYsVQjiTHcPyg); channel video list (listing)
- **김아노**, "한국의 드론병이 전쟁을 나간다면 이런 느낌일까?" (2026-09-06; 1,013 views).
  - The description is a guide to running a real radio in Bodycam through the x360ce emulator: "Auto Map 오른쪽 Add... 을 눌러서 조종기를 연결하고 … 실제 조종기와 맵핑하시면 됩니다".
  - He also posted "발작하는 FPV 드론 날리기 | 바디캠 게임" (2026-09-08).
  - His separate Minecraft video links "서버 링크 : https://minecraftfpv.com/", a different project from Propwash.
  - Sources: [YouTube](https://www.youtube.com/watch?v=tCv06-4PAaA) (RSS); [YouTube Minecraft](https://www.youtube.com/watch?v=GJQygVIGcV8) (listing)
- **씨랙**, "[BODYCAM] 현실보다 더 현실같은 FPS가 초대형 대규모 업데이트로 돌아왔습니다.. 끔직한 참호전, 자폭드론 그리고 실제같은 CQB" (121,258 views; date not retrieved). "더 현실같은" refers to the game overall, not to drone handling. — [YouTube](https://www.youtube.com/watch?v=G3Pd52EeI3w) (listing)
- **Jsungho's Camera Drone**, "현실감 최강 FPV 시뮬레이터? TRYP FPV 건물 다이브 비행 연습!" (2026-08-02; 172 views).
  - The title ends in a question mark.
  - Description: "1위: Uncrashed FPV (가장 뛰어난 현실감) / 2위: TRYP FPV (훌륭한 그래픽과 조종감) / 3위: Velocidrone … / 4위: Liftoff"
  - Also: "TRYP FPV는 특유의 물리 엔진과 묵직한 조종감이 좋아서…"
  - Source: [YouTube](https://www.youtube.com/watch?v=2NWoN9RiUvo) (RSS)

**C. The TRYP–Bodycam link, and v0.9 timing**
- Bodycam's v0.9 post says TRYP's team:
  - added FPV radio support,
  - "gave us a lot of feedback on how our drone flies", and
  - built the lobby drone race.
  - Source: [Steam news](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981) (earlier notes)
- TRYP's own Steam news is silent on the partnership (see A).
- Playtest timing:
  - Search summaries of the press release and VR.one put the public v0.9 playtest at **2026-11-11 09:00 UTC to 2026-11-12 09:00 UTC** (snippet). The earlier notes said "11-10/11", so this may be a correction; verify before printing.
  - Full release is 2026-11-13.
  - Sources: [Games Press](https://gamespress.com/en-US/Bodycam-v09-Zombie-Update-Public-Playtest); [VR.one](https://vr.one/blog/bodycam-zombies-update) (snippet)

### Inferences
- **Likely origin of "very close to real":** a blend of:
  - SubTwoFifty's "genuine FPV sim" and "close to perfect for what it's trying to do" (Propwash), and his "best feeling sim" (TRYP);
  - DRONARCHY's "Ultra realistic" and "Learn FPV here" (Bodycam);
  - the developers' own copy.

  No single speaker said it of all three. The one person who rated all three put Bodycam two tiers below the others.
- **The more affiliated the speaker, the stronger the wording.** "Most realistic… ever created", "match reality" and "same everything" come from developers. Self-described pilots writing about their own play hedge: "almost feels like Liftoff", "Not quite Velocidrone level yet", and "Flies decent" (earlier notes).
- **TRYP's own timeline undercuts its marketing:**
  - Dec 2024: "match reality".
  - Dec 2025: "not… 1.0… PHYSICS MATCHER… not yet deployed".
  - Jun 2026: prop-wash rework still "WIP".
- **Tuning changes the verdict.** 쪼선생's chapter "세팅 바꾸고 날렵해진 모습" and Marcus Daelander's "instead of floaty movement" suggest that experienced players found Bodycam's default drone sluggish or floaty until they tuned it. This is inferred from chapter titles and descriptions; I did not watch the videos.
- **Visual realism gets mistaken for handling realism.** Unreal Engine 5 visuals and scanned locations drive much of the "real" language (DRONARCHY's "Insame graphics and realism", 씨랙). Looking real is not the same as handling like a real quad.

### Gaps
- I found no Sep–Nov 2026 post with the exact words "very close to real" or "실제랑 거의 똑같다" about these games. The specific post the user saw was not identified.
- Spoken verdicts are unknown, including 쪼선생's "총평" and the conclusions of Marcus Daelander, NitroOnAir and Gabrilov. YouTube captions were not retrievable.
- Instagram "Paid partnership" labels could not be checked. TikTok `isAd` was checked only for DRONARCHY's three posts (and SubTwoFifty Part 9, in the earlier notes).
- No credentials (race results, sponsor rosters) were verified for any creator.
- TikTok comment threads were not retrievable: the tool returned no comments.

## Q2. Yardstick: which components make up FPV "flight feel", which can software reproduce well, and what does no simulator or game reproduce?

### Takeaway
Named and dated 2026 sources, plus the developers' own feature lists, give a consistent set of components:
- rates and expo
- thrust-to-weight and throttle response
- inertia and momentum ("floaty" versus "heavy")
- drag and top speed
- prop wash and prop grip
- ground effect
- battery voltage sag
- motor and PID response
- input, frame and video latency
- video breakup, signal and range
- wind
- crash behaviour

Software can match **rates and expo and the flight-controller logic exactly**, because they are formulas. It **approximates** the aerodynamic, battery and latency items, and TRYP, Propwash and an Arma mod all advertise them. **None of these approximations has published validation**, and even a research lab reports that standard first-principles models break down at high speed.

What **no software reproduces** is the real-world side:
- the nerves that come with real hardware and "a total lack of a reset button";
- unpredictable real wind on a real field;
- crash retrieval, repair cost and losing the quad;
- real-world link failures.

The clearest dated statement is **Hucubama (2026-10-18)**: "Grinding for 50 hours in the FPV simulator prepares your thumbs, but nothing prepares your nervous system…"

### Cited Findings

**1. Rates, expo and the input chain**
- Dre The Drone Guy (2026-09-12): Bodycam "has lots of options to fine tune your controller through rates and expo. I am constantly changing these." — [YouTube](https://www.youtube.com/watch?v=-OL_B01imJU) (RSS)
- Rates are portable numbers. DRONARCHY publishes his "Final Boss Rates: (all rows) 1.88, 0.80, 0.10" for Bodycam. — [Instagram reel](https://www.instagram.com/reel/DdAazp8N6O1/) (earlier notes)
- Propwash (README):
  - "a Betaflight-style flight controller"
  - "The tune is stored on the drone, like on a real flight controller."
  - Source: [GitHub](https://github.com/LardTom/propwash-fpv)
- Arma Reforger mod "FPV Ultra Realism" (v1.2.8; created 08.09.2026, modified 24.10.2026; 3,354 downloads; by Smart Insights Apps):
  - "your Betaflight or Actual rates in Settings > FPV - Pilot"
  - "RadioMaster TX15 validated; other EdgeTX/OpenTX profiles beta; DJI RC3 via a Windows companion."
  - Source: [Arma Reforger Workshop](https://reforger.armaplatform.com/workshop/46505655524D3031-FPVUltraRealism) (page)

**2. Thrust-to-weight, throttle response, drag and top speed**
- Propwash (README):
  - "Every drone is derived from its parts: weight, thrust, hover throttle, top speed and flight time follow from the build."
  - Its drone editor covers "masses, inertia, motor positions, props with thrust and power coefficients, motors, battery, ESC, drag and camera".
  - Source: [GitHub](https://github.com/LardTom/propwash-fpv)
- Search summaries (snippets only, unverified):
  - The Propwash add-on "Just More Parts" builds parts "from real data: weight, thrust, KV, internal resistance, capacity, latency, field of view".
  - A release note says a built-in cinewhoop now reaches "a realistic 89 km/h instead of 62 km/h".
  - Source: [CurseForge: Propwash Just More Parts](https://www.curseforge.com/minecraft/mc-mods/propwash-just-more-parts)
- A real-flight example from the DCInside FPV gallery, "파보20 2엽 -> 3엽 교체후기" (2025.02.17): "3엽으로 바꾸니 쓰로틀 반응도 좀더 민감해졌고 추력도 좋고 … 소음, 진동, 프롭워시는 훨씬더 심해진 느낌?" Changing props alone changes the feel. — [DCInside search "프롭워시"](https://search.dcinside.com/post/q/프롭워시) (snippet)

**3. Inertia, momentum and gravity: "floaty" versus "heavy"**
- TRYP store: "Inertia and gravity management". — [Steam API](https://store.steampowered.com/api/appdetails?appids=1881200&l=english)
- TRYP Steam thread "Improved Physics?" (page, read through a fetch tool's extraction). Source: [Steam thread](https://steamcommunity.com/app/1881200/discussions/0/597388342426885464)
  - Opening post, "Lift Ticket" (2024-12-27): "a floaty hot mess of feeling like I was flying in low gravity or on the moon… Sure the controls feel similar but the physics are no where even close."
  - Reply (2025-02-10): "The physics in this game are no where near close to the real thing. It feels like you're flying a balloon in TRYP". The author label shows inconsistently on the page.
  - Contrary view, "MURDER WOLF" (2025-02-08): "I find this physics much better than Uncrashed".
  - Developer, TrypFPV-Team (2025-02-13): "We recently introduced simplified physics factors that allow you to tweak the drone's feel to your liking!"
- TRYP hotfix (2025-12-19): "The new simplified physics settings are designed to help you quickly dial in the feel you want without dealing with complex "detailed physics"." — [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- The opposite impression of the same sim:
  - Jsungho (2026-08-02): TRYP's "묵직한 조종감" (heavy feel). — [YouTube](https://www.youtube.com/watch?v=2NWoN9RiUvo) (RSS)
  - Oscar Liang: TRYP quads feel "slightly heavier than in real life". — [Oscar Liang](https://oscarliang.com/fpv-simulator/) (earlier notes)
- Bodycam: Marcus Daelander (2026-09-13) sells settings for "clean, surgical control… instead of floaty movement". — [YouTube](https://www.youtube.com/watch?v=fC0fVJtG3oQ) (RSS)

**4. Prop wash, prop grip and vortex ring state**
- TRYP (2026-06-02):
  - "Propwash (VRS) - Each prop now analyzes its own airflow in real time (angle of attack, neighbor turbulence, PID reaction)."
  - "You feel the traction through tight corners, the difference between clean flying and pushing too hard."
  - "Move GRIP or PROPWASH to adjust". These are user sliders.
  - Source: [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- Arma mod: "Realistic physics (rotor drag, prop wash, vortex ring, ground effect, voltage sag)". — [Workshop](https://reforger.armaplatform.com/workshop/46505655524D3031-FPVUltraRealism)
- A real pilot's description, DCInside FPV gallery (2025.12.13, an Avata 2 review): "정자세로 추력만 빼고 고도만 내릴때도 프롭워시로 인한 불안정한 진동이 보이기도 하는데". — [DCInside search "프롭워시"](https://search.dcinside.com/post/q/프롭워시) (snippet)

**5. Ground effect**
- Listed as modelled by Propwash and by the Arma mod. — [propwashfpv.com](https://propwashfpv.com/); [Workshop](https://reforger.armaplatform.com/workshop/46505655524D3031-FPVUltraRealism)
- Hucubama's first-flight rule (2026-10-18): "Pop straight up to 20–30 feet immediately to escape ground turbulence". — [YouTube](https://www.youtube.com/watch?v=7k38HQW0I3g) (RSS)

**6. Battery, voltage sag and motor heat**
- TRYP (2026-06-02): "a full LiPo battery simulation". — [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- Propwash (README):
  - Models "voltage sag".
  - World rules include "motor overheating and burnt ESCs on too many cells".
  - Source: [GitHub](https://github.com/LardTom/propwash-fpv)
- Hucubama (2026-10-18): "Start setting up your landing approach as soon as your average cell voltage hits 3.5V – 3.6V while cruising." — [YouTube](https://www.youtube.com/watch?v=7k38HQW0I3g) (RSS)

**7. Motor and PID response, and how to measure it**
- TRYP: a "PID loop" (store), and a Steam news post on 2023-12-14 titled "NEW PHYSICS SYSTEM with Betaflight". — [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- The concrete objective metric, from the open-source project open-fpv-sim (issue #51, "Simulated vs real Blackbox step responses", opened 2026-10-16 by maintainer hugowis):
  - Method: "Fly the same setpoint step in the simulator (with Betaflight SITL and the matching config diff) and in a real quad" and "compare the Blackbox gyro/setpoint traces: delay, overshoot, settling."
  - Status: open, labelled `needs-data` and `help wanted`.
  - Source: [GitHub issue #51](https://github.com/hugowis/open-fpv-sim/issues/51) (page)
- Research-grade modelling limits: Bauersfeld, Kaufmann, Foehn, Sun & Scaramuzza, "NeuroBEM: Hybrid Aerodynamic Quadrotor Model" (RSS 2021; arXiv 2021-06-15):
  - "classic first-principle-models come to their limits"
  - Aerodynamic effects become the dominant modelling error at high speed.
  - "First principles fail to capture such aerodynamic effects, rendering traditional approaches inaccurate" for simulation.
  - Evaluated in a large motion-capture arena at "speeds up to 65km/h".
  - Hybrid model: "50% reduced prediction errors".
  - Source: [arXiv:2106.08015](https://arxiv.org/abs/2106.08015)

**8. Latency: input, frame and video**
- TRYP developer (2025-02-13) on V-Sync: it "can significantly affect the flight feel for some players". He advised turning V-Sync off. — [Steam thread](https://steamcommunity.com/app/1881200/discussions/0/597388342426885464)
- TRYP (2025-12-18): "analog and digital effect with optional input delay". — [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- Propwash: "latency per video system". — [GitHub](https://github.com/LardTom/propwash-fpv)
- The earlier notes already record that sims normally lack real latency (Oscar Liang), and that DJI O4 has about 24 ms.

**9. Video image, signal and range**
- Propwash:
  - "Analog and digital video that breaks up the way a real video link does"
  - "The FPV picture looks through a fisheye lens like a real FPV camera"
  - "a signal model with range and obstacles"
  - "Outside creative, the radio link reaches about 1,200 blocks"
  - Sources: [GitHub](https://github.com/LardTom/propwash-fpv); [propwashfpv.com](https://propwashfpv.com/)
- TRYP (2025-03-28, "MEGABANDO"): "Now you can experience flying with signal interference, just like in real life." — [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- Arma mod: "separate control and video links with terrain masking, VTX power and jamming." — [Workshop](https://reforger.armaplatform.com/workshop/46505655524D3031-FPVUltraRealism)
- Camera uptilt, Hucubama: "Hovering is actually one of the hardest skills in FPV because of your camera uptilt." — [YouTube](https://www.youtube.com/watch?v=7k38HQW0I3g) (RSS)

**10. Wind**
- Propwash models "wind and gusts". — [GitHub](https://github.com/LardTom/propwash-fpv)
- A real flight, DCInside FPV gallery, "프롭워시 개쫄앗네" (2026.03.21): "갑자기 바람 후우우욱 불더니 그대로 덜덜덜". — [DCInside search](https://search.dcinside.com/post/q/프롭워시) (snippet)
- The earlier notes already record Oscar Liang's view that wind "simply" doesn't exist in sims.

**11. Crash behaviour and damage**
- TRYP (2026-06-02): "propeller damage". — [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- Propwash: burnt ESCs when a build uses too many cells. — [GitHub](https://github.com/LardTom/propwash-fpv)
- The earlier notes already record "crashes were a mess" (WebFPV, SubTwoFifty) and "bouncing… like it's made of rubber" (Uncrashed review, 2026-10-29).

**12. What named 2026 sources say no sim reproduces**
- **Hucubama, "Why Your First Real FPV Flight Feels Nothing Like the Sim"** (2026-10-18; 10,461 views):
  - "Grinding for 50 hours in the FPV simulator prepares your thumbs, but nothing prepares your nervous system for pulling down the goggles on your very first real-life flight."
  - "Transitioning from the computer desk to a real field means dealing with wind, physical momentum, battery sag, and a total lack of a reset button."
  - "Take 3–5 deep breaths with your goggles down before arming to stop thumb tremors."
  - Source: [YouTube](https://www.youtube.com/watch?v=7k38HQW0I3g) (RSS)
- **RuffsFPV** (TikTok @ruffiexfpv, 2026-04-22; 7,695 views):
  - "…AND PROCEED TO IMMEDIATELY RUN YOUR DRONE INTO THE WALL BREAKING IT INTO A MILLION PIECES!"
  - "…it's the number 1 motivation killer, you won't want to fly your drone again because you're scared of breaking it.. Or worse.. Completely lose it.."
  - "This is why I always advocate simulator first! Real drone second!" The post carries the hashtag #velocidrone.
  - Source: [TikTok](https://www.tiktok.com/@ruffiexfpv/video/7631283872944229650) (TikTok data)
- Propwash's own caveat: "The world around it is still Minecraft, of course." — [propwashfpv.com](https://propwashfpv.com/)
- Bodycam-specific game rules that real flight doesn't have (earlier notes):
  - respawn and launch timers;
  - "One bullet and it's gone";
  - a "very precise hitbox system".
  - Source: [reel 2](https://www.instagram.com/reel/DcOcxWci_EO/)

**Discarded:** an earlier search summary said the Arma mod's page calls its physics "not certified training instruments". The page fetched on 2026-11-12 does not contain that wording, so do not use it. — [Workshop](https://reforger.armaplatform.com/workshop/46505655524D3031-FPVUltraRealism)

### Inferences
**Yardstick table for the report** (my synthesis of the findings above):

| Component | Can software reproduce it? | Status in the three games (claims, not tests) |
|---|---|---|
| Rates and expo; Betaflight-style controller logic | **Yes, exactly.** These are formulas. | Bodycam: rates and expo are adjustable (Dre). Propwash: Betaflight-style FC. TRYP: Betaflight-based since 2023. |
| Input device (real radio, non-centring throttle) | **Yes**, if the game accepts a radio | Propwash: radio over HID. TRYP: radio. Bodycam: native radio only from v0.9 (2026-11-13); before that through x360ce or Steam Input workarounds. |
| Thrust-to-weight, throttle, drag, top speed | **Approximated.** Needs real part data. | Propwash derives these from the parts. TRYP has "digital twin" claims. Bodycam: unknown. |
| Inertia and momentum ("floaty"/"heavy") | **Approximated, and a matter of taste.** It is often a user setting. | TRYP has physics sliders and gets both "floaty" and "heavy" verdicts. Bodycam's default was called floaty until tuned. |
| Prop wash, prop grip, vortex ring, ground effect | **Approximated.** Hardest at high speed (NeuroBEM). | TRYP: rework still "WIP" (Jun 2026). Propwash and the Arma mod list them. Bodycam: not stated. |
| Voltage sag, motor heat | **Approximated** | TRYP: LiPo simulation (Jun 2026). Propwash: sag and burnt ESCs. Bodycam: not stated. |
| Latency (input, frame, video) | **Approximated, but distorted by the PC.** V-Sync and frame rate change the feel. | TRYP: optional delay. Propwash: latency per video system. |
| Video breakup, signal, range | **Partly** | TRYP: interference. Propwash: range and obstacles. Arma mod: jamming. |
| Real wind, weather, light | **No.** Some sims offer scripted wind; the real thing is unpredictable. | Propwash: "wind and gusts". |
| Crash consequences (repair, cost, a lost quad) and nerves | **No** | All three have a reset or respawn. |

- **"Feels real" depends partly on settings.** TRYP sells sliders so you can "tweak the drone's feel to your liking". Propwash has "Training and Arcade" presets. Bodycam has a casual mode and lower rates for gamepads (earlier notes). One sim can be called both "floaty" and "heavy" by different pilots. So a "very close to real" verdict is only meaningful if the speaker states the settings and the real quad they compare against (whoop, 5-inch or 7-inch).
- **Practical test for a beginner:** of the components above, a beginner can only check the first two personally: acro mode, a real radio, and rates that match the real quad. The aerodynamic items need a real quad for comparison, and the real-world items can't be practised in any game.

### Gaps
- I found no dated statement from a named FPV instructor or school listing these components. Joshua Bardwell's relevant livestream clips exist ("Can You Start FPV Sims With A Video Game Controller?"; "How Long Should You Practice In An FPV Simulator…"), but I couldn't read their content. — [YouTube](https://www.youtube.com/watch?v=aGLZWwEqPgY); [YouTube](https://www.youtube.com/watch?v=cIzrdlMhaOM) (listing)
- I found no sourced statement on flying sims in goggles versus on a monitor. I make no claim either way.
- Many search hits were low-quality blogs (zbotic, buzz-drones, srizfly, UAVMODEL). They cited unsourced percentages such as "80–90% transfer" and "87% visual accuracy", which I excluded.
- Hucubama's and RuffsFPV's credentials are unverified.

## Q3. Are there objective tests of simulator realism, and any direct comparisons between these games or against real flight?

### Takeaway
**No objective test covers TRYP FPV, Propwash or Bodycam.** By an objective test I mean a published blackbox overlay, a step-response match, a sim-versus-real trajectory comparison, a controlled transfer study, or a blind handling test.
- **Propwash** says its physics has been "checked against blackbox logs of real drones" since v0.5.0, but publishes no method or results.
- **TRYP** announced a blackbox-driven "Physics Matcher" in June 2024 and claimed "digital twin" physics in December 2024. In December 2025 it said the matcher was "not yet deployed".
- **Bodycam** has only TRYP's informal "feedback".
- Open-source sim projects define the right test, matching step responses on the same quad, and label it "needs-data". Research shows standard models miss high-speed aerodynamics.

All the **direct comparisons I found are opinions or visual side-by-sides**:
- SubTwoFifty's tier list, the only one covering all three;
- Dre The Drone Guy: Bodycam against Liftoff and VelociDrone;
- Jsungho: TRYP against other sims;
- DRONARCHY: Bodycam footage against real night footage, a visual comparison;
- HenFPV (2025): a casual "spot the sim" footage quiz using TRYP clips.

### Cited Findings

**Developer validation claims (unpublished)**
- Propwash: "Since 0.5.0 the physics is checked against blackbox logs of real drones from a 65 mm whoop to 7″." No method, accuracy figures or drones are listed. — [propwashfpv.com](https://propwashfpv.com/) (page)
- TRYP, in its own words:
  - 2024-06-26: the "Physics Matcher" "will analyze a blackbox…"
  - 2024-12-19: "Using digital twin technology, we've adjusted every nuance of the drone's behavior to match reality."
  - 2025-12-18: "We still do not consider our physics to 1.0, as our PHYSICS MATCHER System is not yet deployed".
  - Its Steam news through 2026-06-15 contains no later deployment notice.
  - Source: [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=40&maxlength=0)
- Bodycam: the developer says TRYP "gave us a lot of feedback on how our drone flies". This is not a measurement. The v0.9 flight model had not been released as of 2026-11-11. — [Steam news](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)

**How an objective test would look, and that it is still undone**
- open-fpv-sim issue #51 (opened 2026-10-16): fly "the same setpoint step" in the sim, with Betaflight SITL and a matching config, and on a real quad, then compare "delay, overshoot, settling". The issue is open and labelled `needs-data`. — [GitHub #51](https://github.com/hugowis/open-fpv-sim/issues/51) (page)
- Other open-source FPV sims say the same, per search snippets:
  - gilboash/fpv-naive-sim: "Not validated against a real Blackbox log".
  - fpv-digital-twin: lists its "blackbox replay and sim-vs-real overlay" phase as not started.
  - ShramkoGSFPV: blackbox tools are ready but "waiting for logs from the real quads".
  - Sources: [fpv-naive-sim](https://github.com/gilboash/fpv-naive-sim); [fpv-digital-twin](https://github.com/sshaizkhan/fpv-digital-twin); [ShramkoGSFPV](https://github.com/AndriiShramko/ShramkoGSFPV) (snippets)
- Research benchmark: NeuroBEM (2021). First-principles quadrotor models are "inaccurate" for simulation at high speed. A hybrid model validated with motion capture up to 65 km/h cut prediction errors by 50%. — [arXiv:2106.08015](https://arxiv.org/abs/2106.08015)
- An unverified statistic keeps spreading. The "about 2 vs 20 crashes in the first 10 flights" figure attributed to "UAVMODEL Insights" is still untraceable; the earlier notes flagged it. It is now repeated by Flight Division, a browser-sim maker and so not a neutral source. Do not use it. — [Flight Division blog](https://www.flightdivision.com/blog/fpv-drones-complete-beginners-guide) (snippet)

**Direct comparisons (opinion or visual only)**
- **All three games:** SubTwoFifty's tier list (2026-11-10): TRYP S ("best feeling sim"), Propwash A ("flies brilliantly"), Bodycam C ("Rubbish as a sim"). — [Instagram](https://www.instagram.com/reel/Dfkss5XqOJt/) (earlier notes)
- **Bodycam against dedicated sims:** Dre The Drone Guy (2026-09-12): "It almost feels like Liftoff but needs a little adjusting. Not quite Velocidrone level yet with accuracy and racing." — [YouTube](https://www.youtube.com/watch?v=-OL_B01imJU) (RSS)
- **Bodycam against real footage:** DRONARCHY TikTok (2026-09-06), "Ultra realistic vs real life footage". I downloaded the 55-second clip and checked one frame every 4 s:
  - The first ~32 s are Bodycam gameplay in a sunlit piazza with a BODYCAM logo. An inset shows hands on a RadioMaster TX16S radio.
  - At ~36 s an overlay reads "IMAGINE IN REAL LIFE".
  - The last ~15–20 s are darker, grainier night footage of a colonnaded building and street, with streetlights and a car. Overlays read "SO MOTE IT BE" and "FOLLOW FOR FPV".
  - This is a **visual side-by-side only**: no handling data, and no claim that both clips were flown the same way. That the night footage is real-camera footage is my reading of the frames.
  - Source: [TikTok](https://www.tiktok.com/@dronarchy/video/7682275044445244702) (TikTok data plus frame check)
- **TRYP against other sims:** Jsungho (2026-08-02) ranks feel as Uncrashed ("가장 뛰어난 현실감"), then TRYP, VelociDrone, Liftoff. — [YouTube](https://www.youtube.com/watch?v=2NWoN9RiUvo) (RSS)
- **Informal blind test (visual, 2025):** HenFPV, "Can people tell the difference between FPV simulators and real life?" (2025-09-04; 68 views): "I tested clips, 2 real 2 fake and I posted them on the r/fpv discord server and I saw if they could see if it was a simulator or a real flight." Tagged #trypfpv. The result isn't in the description. — [YouTube](https://www.youtube.com/watch?v=yHki6TDygW0) (RSS)
- **Input devices in another shooter:** Marcus Daelander, "I Used a Real FPV Drone Controller in Wardogs..." (2026-09-22; 141,003 views): "Can real-world FPV drone muscle memory translate into tactical helicopter dominance?… I test whether real-life RC transmitter gimbals give an unfair advantage over traditional controllers." — [YouTube](https://www.youtube.com/watch?v=LpgdYZybHpk) (RSS)
- **Sim-trained skill carried into Bodycam:** NitroOnAir (Uncrashed-trained; 246,034 views). — [YouTube](https://www.youtube.com/watch?v=kqvw-i8uxKg) (earlier notes; listing)
- **No source compares Propwash directly with TRYP or Bodycam** apart from SubTwoFifty's list. DRONARCHY covers Bodycam and Propwash in separate posts and never compares them.

### Inferences
- **"Very close to real" can't currently be verified for any of the three games.** The only realism evidence is subjective feel, and visual realism (UE5 graphics, scanned spots) is easily mistaken for flight realism.
- The two developers who say they use blackbox data, Propwash and TRYP, could settle the question by publishing sim-versus-real step-response overlays for a named quad. Until they do, treat "checked against blackbox logs" and "match reality" as unverified marketing.
- For Bodycam, the fairest current summary is "pilots say it is roughly Liftoff-like after tuning, not VelociDrone-level" (Dre). v0.9's TRYP-tuned model (2026-11-13) is untested.

### Gaps
- No blackbox, step-response or trajectory data has been published for TRYP, Propwash or Bodycam.
- HenFPV's quiz result is unknown, and it tested footage, not handling.
- I found no peer-reviewed study of human acro-FPV sim-to-real transfer from 2025–2026. This confirms the earlier notes.

## Q4. What do FPV communities say in 2026 about game drones (Bodycam, Minecraft mods, Battlefield, CoD, Arma) as FPV practice, compared with dedicated simulators?

### Takeaway
The 2026 consensus among pilots and FPV educators is still **dedicated simulator plus a real radio first, with game drones as a fun supplement**.
- **The pro-practice voice for Bodycam is mainly DRONARCHY** ("Learn FPV here if you want to", "Practice and enjoy FPV").
- Self-described pilots' written verdicts are **lukewarm to positive** ("feels pretty good… almost feels like Liftoff… not quite Velocidrone").
- Educator-style creators push **dedicated sims** and stress what sims can't teach (Hucubama; RuffsFPV with #velocidrone).
- New searches confirm the earlier notes: **no IntoFPV or DCInside FPV-gallery thread recommends Bodycam or Minecraft mods as practice**.
- **Reddit and Naver cafés were unreachable.**
- Beyond Bodycam, using real radios in shooters is spreading (Wardogs; Arma Reforger mods that claim Betaflight rates and prop wash), but I found no practice verdicts. **For Battlefield and Call of Duty I found nothing.**

### Cited Findings

**For game drones as practice (creator side)**
- DRONARCHY on Bodycam:
  - "Learn FPV here if you want to." (2026-11-11) — [YouTube](https://www.youtube.com/watch?v=sq5UNdelWO8) (RSS)
  - "basic acro tricks to practice… Practice and enjoy FPV!" (2026-10-25) — [YouTube](https://www.youtube.com/watch?v=oPEfwj6ePyY) (RSS)
  - "The physics feel and perform really good" (2026-09-08; 658.7K views) — [TikTok](https://www.tiktok.com/@dronarchy/video/7683146943647730974) (TikTok data)
- 김아노 (2026-09-06) published a Korean step-by-step x360ce guide for flying Bodycam with a real radio. — [YouTube](https://www.youtube.com/watch?v=tCv06-4PAaA) (RSS)

**Measured or sceptical pilot views**
- Dre The Drone Guy (2026-09-12): "It feels pretty good… almost feels like Liftoff but needs a little adjusting. Not quite Velocidrone level yet with accuracy and racing." — [YouTube](https://www.youtube.com/watch?v=-OL_B01imJU) (RSS)
- SubTwoFifty: Bodycam "Rubbish as a sim" (C). Another combat-style title, Firehawk, is "a wicked time, but not for learning how to fly" (C). — [Instagram](https://www.instagram.com/reel/Dfkss5XqOJt/) (earlier notes)
- Steam's self-described pilots ("fly okay", "Flies decent") and the Korean Bodycam gallery are covered in the earlier notes and are not repeated here. — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/)

**Educator-style creators favour dedicated sims**
- Hucubama's October 2026 series:
  - "Why Your First Real FPV Flight Feels Nothing Like the Sim" (2026-10-18)
  - "Stop Wasting Time in the Simulator: The Advanced Routine" (2026-10-22; 18,959 views)
  - "3 Simulator Exercises That Will Change How You Fly FPV" (2026-10-27; 18,820 views)
  - The last two are titles only.
  - Sources: [YouTube](https://www.youtube.com/watch?v=7k38HQW0I3g); [channel RSS](https://www.youtube.com/feeds/videos.xml?channel_id=UC3eHT9hTB2qjjQjeVbsj5XA) (RSS)
- RuffsFPV (2026-04-22): "simulator first! Real drone second!… So do your simulator races! Every week, every day if you can!" with #velocidrone. — [TikTok](https://www.tiktok.com/@ruffiexfpv/video/7631283872944229650) (TikTok data)

**Korean communities**
- DCInside searches on 2026-11-12:
  - "프롭워시" returned only real-flight posts: 2026.03.21, 2025.12.13, 2025.02.17.
  - "마크 FPV" returned no Minecraft drone posts. Its hits were military or "landmark" noise, plus one 2026.08.04 request for a low-spec PC sim.
  - Neither search turned up a Minecraft or TRYP game-practice discussion.
  - Sources: [DCInside "프롭워시"](https://search.dcinside.com/post/q/프롭워시); [DCInside "마크 FPV"](https://search.dcinside.com/post/q/마크%20FPV) (snippets)
- The earlier notes record that DCInside FPV-gallery beginners start on Liftoff and move to Uncrashed or VelociDrone. They also record one Bodycam-gallery hope to use the game "as a simulator if the flight feel is OK". — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=fpv&no=1724) (earlier notes)
- Naver café search: the fetch was refused (search.naver.com unreachable).

**Other games with FPV drones**
- Arma Reforger, "FPV Ultra Realism" mod (created 2026-09-08; 3,354 downloads):
  - Claims "Realistic physics (rotor drag, prop wash, vortex ring, ground effect, voltage sag)" and Betaflight or Actual rates.
  - "RadioMaster TX15 validated".
  - "Not affiliated with Bohemia Interactive."
  - I found no community verdict on whether it is good practice.
  - Source: [Workshop](https://reforger.armaplatform.com/workshop/46505655524D3031-FPVUltraRealism) (page)
- Other Arma Reforger drone packs (titles only): "Realistic Combat Drones-MANW" and "Realistic Combat Drones - RHS". — [Workshop](https://reforger.armaplatform.com/workshop/65EA144B050DC1F7); [Workshop](https://reforger.armaplatform.com/workshop/65D08E0825A12E2C) (snippet)
- Wardogs: Marcus Daelander's real-radio test (2026-09-22; 141K views; see Q3). — [YouTube](https://www.youtube.com/watch?v=LpgdYZybHpk) (RSS)
- War Thunder (titles only): "Real Free FPV Drone in War Thunder?" (Zenturion7; 22,209 views) and "The FPV Drone is RUINING War Thunder" (ShorThunder). — [YouTube](https://www.youtube.com/watch?v=lm885pR2H1M); [YouTube](https://www.youtube.com/watch?v=Fd7fGtZrTYE) (listing)
- Battlefield and Call of Duty: no 2026 source found that discusses their drones as FPV practice.

**Reddit and IntoFPV**
- old.reddit.com fetch: refused. Web search returned no r/fpv threads on Bodycam or Minecraft. — attempted [old.reddit.com search](https://old.reddit.com/r/fpv/search?q=bodycam&restrict_sr=on&sort=new&t=year)
- IntoFPV: a domain-restricted search returned no Bodycam or Minecraft threads. — [IntoFPV](https://intofpv.com/)

### Inferences
- **For the Korean beginner report:** treat Bodycam and Propwash as motivating side-practice, not as the main trainer. If they are used at all, use acro mode, a real radio and realistic rates.
  - In Bodycam, use v0.9 or later, which has native radio support (2026-11-13).
  - Propwash is free and models many components, but it has no independent pilot review, and its "Training/Arcade" presets and Minecraft world rules can make it easier than reality.
  - The core trainer should stay a dedicated sim. This matches every hobbyist source found, in this and earlier notes.
- **Combat games add rules** (respawn, hitboxes, launch timers) and reward different skills, such as hitting a target, rather than flying smooth lines and managing throttle. That limits their practice value even when the physics is decent.
- **"Real pilots like it" is not the same as "good practice."** The most-viewed endorsements (DRONARCHY's 658.7K-view TikTok; Marcus Daelander's 736K-view video, verdict unknown) come from experienced pilots enjoying the game. They are not beginners showing skill carrying over to real flying.

### Gaps
- Reddit (r/fpv, r/Multicopter), Naver cafés and Discord were unreachable, so the largest English and Korean hobby communities' 2026 views are unknown.
- I found no 2026 poll or survey on game drones as practice.
- I found nothing on Battlefield or Call of Duty drones as FPV practice. War Thunder appears in titles only.
- Opinions on Bodycam's TRYP-tuned v0.9 drone don't exist yet; it releases 2026-11-13.
