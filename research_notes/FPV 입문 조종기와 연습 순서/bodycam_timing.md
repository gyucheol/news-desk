# Bodycam drones for an FPV beginner: when to start, and what v0.9 changes for practice

Research window: 2026-11-11, about 11:40–12:00 UTC (20:40–21:00 KST). Steam's news API, store API and discussion pages were pulled at 11:48–11:53 UTC. Times are UTC unless marked KST. "Earlier notes" means this session's files in `research_notes/바디캠 드론과 실제 FPV 조종 비교/`. I re-verified the official Steam lines, the store data, Rotor Village and Oscar Liang today. Items marked "(earlier notes)" were not re-opened today.

## 1. What is confirmed about v0.9 "The Dead & Damned" (radio support, radios and protocols, calibration, flight model, the lobby circuit and race, practice area), and what Steam has published since the morning of 2026-11-11

### Takeaway
**Confirmed:**
- v0.9 is out on Friday 13 Nov 2026. No release hour is stated.
- The lobby gets its "biggest room yet", for drones and RC cars, "with a circuit for each".
- The TRYP FPV team helped "add support for FPV radio controllers". It gave "a lot of feedback on how our drone flies" and helped build "the drone race you'll find in the lobby".
- The full patch notes come only "on release day".

**Not confirmed:**
- Which radios or protocols work, and how calibration, arming and Acro switching work with a radio.
- Whether the flight model or the default rates actually changed.
- Whether the room allows free flight, and whether it has a respawn delay, lap timer or leaderboard.

**Since the morning of 11 Nov:** Steam has one new post, the 09:07 UTC "playtest is live" notice. It says nothing about drones.

### Cited Findings
**Steam news feed for app 2406770, v0.9-era items in order** (pulled 2026-11-11 11:48 UTC) — [ISteamNews feed](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2406770&count=25&maxlength=0)
- **2026-10-29 18:35 UTC (10-30 03:35 KST), account "cdechabert", "BODYCAM V0.9 THE DEAD & DAMNED - RELEASE DATE & WHAT'S COMING"** — [Steam announcement](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)
  - "Bodycam v0.9 releases on Friday, November 13." / "0.9 is a smaller, in-between update."
  - "The lobby gets its biggest room yet, dedicated to drones and RC cars, with a circuit for each."
  - "For the drone, we teamed up with the team behind TRYP FPV. They helped us add support for FPV radio controllers and gave us a lot of feedback on how our drone flies. They also helped us put together the drone race you'll find in the lobby. If you have a radio controller, plug it in and give it a go."
  - "Full patch notes on release day."
  - Other v0.9 content: Zombie Trenches mode; Village and Asylum return; weapon boxes; Public Pool rework; crossbow and TEC-9; "Easy Anti-Cheat arrives with 0.9"; "The party system won't be in 0.9"; "Quick Play and Server Browser stay solo queue for now"; "You'll still need to host your own game to play with up to 10 friends."
- **2026-11-02 06:10 UTC and 2026-11-05 19:54 UTC:** two items from the Russian outlet PlayGround.ru, carried in the Steam feed, relay the same features. The 11-02 item says the developers "внедрят управление дронами с помощью радиопультов" (will introduce drone control with radio transmitters) with TRYP FPV's help. Neither adds drone detail. — [ISteamNews feed](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2406770&count=25&maxlength=0)
- **2026-11-05 19:48 UTC, "WATCH Bodycam Zombie: 'The Dead and Damned' Devlog 1/2":** links a video that YouTube oEmbed titles "Bodycam Zombie - Official 'The Dead and Damned' Behind the Scenes Look" (IGN channel). It is zombie-focused, and I did not watch it. — [Steam](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1848664643342937); [YouTube](https://www.youtube.com/watch?v=5AWugRmrn0g)
- **2026-11-10 17:05 UTC (11-11 02:05 KST), "The Dead & Damned Playtest: Zombies Are Back, 24 Hours Only":** under "What's new in v0.9" it lists "Drone and RC lobby: a new room with a drone circuit and an RC car circuit, FPV controllers supported". — [Steam](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1848664643360428)
- **Since the morning of 11 Nov:** only one post, at **2026-11-11 09:07 UTC (18:07 KST)**: "The Bodycam v0.9 Playtest is LIVE: bring your 3 friends".
  - Its "What's in the playtest" section lists only "Zombie Trenches, a new co-op mode for up to 4 players" and "Village and Asylum, reworked with new lighting, materials and audio".
  - It does not mention drones, radios or the lobby room.
  - No patch notes or other developer posts had appeared by 11:48 UTC.
  - [Steam](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1849192144177820)
- **TRYP FPV's own Steam feed** (app 1881200) has no post about Bodycam. Its latest item is "HOTFIX 260609" (2026-06-15). — [ISteamNews feed, TRYP FPV](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=15&maxlength=0)

**Press relaying v0.9 (no new drone facts)**
- 경향게임스 (mirror on DCInside's khgames board, posted 2026-11-11 15:41 KST): "로비에는 드론과 무선조종 자동차를 체험할 수 있는 전용 공간이 추가되며, 각각 전용 주행 코스가 마련된다. 일인칭 시점 조종기 연결도 지원해 보다 현실적인 드론 조작을 경험할 수 있다." — [경향게임스 via DCInside khgames](https://gall.dcinside.com/board/view/?id=khgames&no=12268)
- iGameMag (published 2026-11-09 17:53 UTC, modified 2026-11-11 11:31 UTC): "Reissad worked with the team behind TRYP FPV to add support for FPV radio controllers and build a drone race". — [iGameMag](https://igamemag.com/bodycam-update-0-9-the-dead-and-damned/)

**Practice space before v0.9 (what the new room replaces)**
- v0.8 notes (2026-09-02, re-verified today): "Some areas are currently closed for maintenance, including the obstacle course, shoot house, and drone and RC car rooms." — [Steam](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- The room was still closed on 4 Nov. A thread titled "… HELL OPEN THE DRONE ROOM AND KILL HOUSE--- LAZY DEVS????!" (OP "ZALO", 2026-11-04 17:48 UTC) got the reply "they are adding the RC track if that helps" ("sugarNuts"). — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563672611395077500/)
- Workarounds in v0.8, from the thread "FPV Training" (2026-09-28) — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/587313051305508524/):
  - "try to host a private bot-only deathmatch and fly all you want" ("pngun")
  - "Just host a privat match. You can choose the map and train fpv" ("BastaPasta")
  - "Practice best on the trench map . Later on cqb" ("Humperdoo")
  - "There should be a large map with high sky limits" ("realrazer3")
  - "there is a very big cooldown from when you use a drone and can again… i also wish there was a way to practice" ("Brezeld")
- In v0.8 the firing range had "a respawn timeout after the drone explodes" (earlier notes; Steam thread, 2026-09-03). — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
- The store still says the hub lets players "practice your shooting, fly FPV drones, or simply spend time with other players" (re-verified 11:48 UTC). — [Steam appdetails (EN)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english)
- The v0.8 Trenches map has "Dedicated areas designed for FPV drones and RC cars." (Devlog 3/4, 2026-08-25, re-verified in the feed). — [Steam](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1841579228678435)

### Inferences
- The v0.9 lobby room will be the first official space in Bodycam built for repeated flying, and it opens to everyone on 13 Nov. How useful it is for practice depends on details not yet published (respawn delay, free flight, difficulty of the TRYP-built race).
- "Plug it in and give it a go" suggests plug-in USB support. It does not say which radios, which USB mode, or how calibration works. Any report sentence on these points must wait for the 13 Nov notes.
- "Gave us a lot of feedback on how our drone flies" is not a statement that the flight model changed. The patch notes may or may not list physics or rate changes.

### Gaps
- Unpublished: supported radios and protocols (e.g., USB joystick/HID, EdgeTX/OpenTX, DJI radios), channel mapping, calibration UI, arm and Acro switch handling, radio-specific rate defaults.
- The release hour on 13 Nov is not stated.
- Unpublished: whether the drone room has a respawn delay, free-flight space, lap timer, leaderboard or difficulty levels.
- Not opened: the Games Press release "Bodycam v0.9 Zombie Update & Public Playtest" — [Games Press](https://www.gamespress.com/en-US/Bodycam-v09-Zombie-Update-Public-Playtest). Also not opened: dlcompare, PlayInsider and bodycamzombie.wiki v0.9 articles.
- Caution for the writer: TRYP FPV's own simulator has a controller-calibration step, according to its 2024 Steam forum threads. Nothing says Bodycam adopts it, so do not infer that it does.

## 2. The 24-hour v0.9 playtest (2026-11-11 09:00 UTC to 2026-11-12 09:00 UTC; 18:00 to 18:00 KST): first impressions of the drones with real radios?

### Takeaway
I found **no first impressions** of the drones or radio support as of 11:53 UTC, about three hours into the playtest.

The developer also **has not clearly confirmed that the playtest build contains the drone room**:
- The 10 Nov post listed the drone room among v0.9 features.
- The 11 Nov "What's in the playtest" list names only zombie content.

The earlier session note saying the playtest "includes a drone lobby", and the earlier report's line "지금 바로 맛보고 싶다면 무료 v0.9 플레이테스트가 있다", go beyond what the posts say.

Impressions may still appear later. Access opens in waves by time zone, and Korean press reports there is no NDA.

### Cited Findings
- **Access:**
  - "Access is granted progressively, in waves, time zone by time zone, so each region gets in at a good time to play."
  - "More players get in every few hours throughout the playtest."
  - Players can invite "up to 3 friends".
  - Feedback goes to Discord, and "your feedback shapes the full release this Friday, November 13".
  - [Steam, 2026-11-11 09:07 UTC](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1849192144177820)
- **Purpose:** "Places are limited and not everyone will get access." / "This playtest is here to catch the last bugs before release." — [Steam, 2026-11-10 17:05 UTC](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1848664643360428)
- **No NDA, per Korean press:** "별도의 비밀유지협약이 적용되지 않아 참가자는 게임 플레이를 자유롭게 방송하거나 공유할 수 있다." The article gives the KST window as 11 Nov 18:00 to 12 Nov 18:00. — [경향게임스 via DCInside khgames, 2026-11-11 15:41 KST](https://gall.dcinside.com/board/view/?id=khgames&no=12268)
- **Steam General Discussions** (pages 1–2, newest thread 11:36 UTC): no thread about drones, radios or the drone room. Topics were zombies, crashes, servers and anti-cheat. — [Steam discussions](https://steamcommunity.com/app/2406770/discussions/0/)
- **Steam discussion search** for "fpv", "drone", "radio" and "playtest drone": the newest drone-related matches date from before the playtest (the newest "fpv" match is 2026-11-10). — [Steam search "fpv"](https://steamcommunity.com/app/2406770/discussions/search/?q=fpv); [Steam search "drone"](https://steamcommunity.com/app/2406770/discussions/search/?q=drone)
- **The separate "Bodycam Playtest" app (2746700):** its news feed is empty, and its community page returned no threads. — [ISteamNews feed, 2746700](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2746700&count=10&maxlength=0)
- **Web:** an extended web search found no hands-on drone or lobby impressions, only pre-playtest feature coverage — e.g., [dlcompare](https://www.dlcompare.com/gaming-news/bodycam-the-dead-damned-update-brings-back-zombies-89288), [PlayInsider](https://playinsider.net/newsberichte/bodycam-zombies-update-0-9-zombie-trenches/), [iGameMag](https://igamemag.com/bodycam-update-0-9-the-dead-and-damned/).
- **Not reachable:** Reddit (r/BodycamGame new posts, r/fpv search) returned HTTP 403. YouTube watch pages hit a bot check, and X was not reachable. I could only confirm titles via YouTube oEmbed.

### Inferences
- If the playtest build has the drone room, credible radio impressions could appear before 12 Nov 09:00 UTC (18:00 KST). If not, they will appear only after the 13 Nov release. The report should not promise reviews or describe how v0.9 feels with a radio.

### Gaps
- Whether the playtest build includes the drone room and native radio support.
- Impressions on Reddit, X, YouTube and Discord. Discord is where the developer collects feedback, and I could not access it.

## 3. What flying Bodycam's drone in Acro mode in matches demands

### Takeaway
In a match, the drone is a short-lived kamikaze or recon gadget:
- Launches are rationed by cooldowns.
- Players hear it easily and call it easy to shoot ("gigantic hitbox").
- The Kamikaze detonates on impact.
- Your character stands exposed while you fly.

So success means fast Acro flying close to cover, fine throttle and attitude control, and a precise final dive onto a moving player, all with very few attempts. That is a skill set beyond the beginner basics.

Creator settings point the same way:
- An unofficial tool's documentation says Bodycam's default rates are "very high (RC Rate 2.0, which is about 1100°/s at full stick)".
- DRONARCHY's "Final Boss Rates" 1.88/0.80/0.10 come to about **1,880°/s** by Betaflight's formula (my calculation). That is nearly three times Betaflight's own default maximum of 670°/s.

### Cited Findings
**Official game rules**
- v0.8 notes (re-verified):
  - "Added a deployment cooldown system for both drones and RC cars, including an additional cooldown on loadout change to prevent abuse."
  - "Added a cooldown indicator with an audio notification when the gadget becomes available again."
  - [Steam, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- Store: drones "scout enemy positions, gather intelligence, strike targets, and support your squad." — [Steam appdetails (EN)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english)
- Tech Times: both gadgets are "intentionally capped in per-match availability" (earlier notes). — [Tech Times, 2026-08-19](https://www.techtimes.com/articles/324962/20260819/bodycam-v08-devlog-stress-driven-reloads-lead-locked-loaded-overhaul.htm)

**Third-party guides**
- GamesFuze (updated 2026-09-15; earlier notes) — [GamesFuze](https://gamesfuze.com/guides/bodycam-how-to-use-fpv-drones-and-rc-cars/):
  - The Kamikaze is "designed around reaching an enemy and detonating on impact".
  - Angle mode is "slower and easier for enemies to shoot down".
  - FPV Acro is full manual.
  - Its suggested starting values are RC Rate 1.50 and Super Rate 0.50. A search-result summary of the guide (today, page not re-opened) says these give "a good starting point without making the drone excessively sensitive" and that rates can be raised later.
- bodycamgame.wiki (unofficial; earlier notes): your character "stands still in the world" while you fly, and the tablet does not pause the game. — [bodycamgame.wiki](https://bodycamgame.wiki/guides/drones-and-rc-vehicles/)
- ExitLag blog (a network-tool vendor; the page returned 403, so this is from a search summary only) — [ExitLag](https://www.exitlag.com/blog/bodycam-fpv/):
  - It recommends practising Acro in Deathmatch as "a lower-stakes environment to build manual flight muscle memory".
  - Flying the drone does not protect your body.
  - "any connection hiccup can turn smooth Acro Mode flying into a frustrating, jittery mess".

**Unofficial radio tool "Bodycam FPV Fix"** (GitHub README and guide, read today; third-party, describes the v0.8 build) — [GitHub README](https://github.com/lukas-Logikfabrik/bodycam-fpv-fix); [GUIDE.md](https://github.com/lukas-Logikfabrik/bodycam-fpv-fix/blob/main/docs/GUIDE.md)
- **How Bodycam reads input:**
  - "Bodycam only understands Xbox controllers."
  - Acro layout: throttle and yaw on the left stick, pitch and roll on the right; "RB arms the drone, LB toggles Acro mode."
  - "Only Acro mode uses the four sticks like a real quad. In Bodycam's normal mode the left stick moves forward and back and the right stick moves the camera."
  - "Left stick Y over its full travel is throttle: down = 0 %, center = 50 %, up = 100 %."
- **Rates:**
  - "Bodycam's default drone rates are very high (RC Rate 2.0, which is about 1100°/s at full stick)."
  - Its table gives defaults of Super Rate 0.64–0.69 and RC Expo 0.22–0.24.
  - It suggests RC Rate 1.0, Super Rate 0.65, Expo 0.15 and camera tilt 25° to "feel like a normal freestyle quad".
- **Radios and safety:**
  - RadioMaster Pocket: "Tested by a user, works after calibration".
  - "8 of 71 engines" on VirusTotal flag v1.0.1, which the README calls generic machine-learning or reputation verdicts.
  - The exe is not code-signed and needs the ViGEmBus driver.

**FPV creators**
- DRONARCHY FPV, Instagram reel, 2026-09-08 00:47 UTC (earlier notes; caption verbatim): "Ruthless rips with a 7" drone. Proving you can fly here full acro with a real drone controller. Practice and enjoy FPV. / 🤌 Using my Final Boss Rates: (all rows) 1.88, 0.80, 0.10". — [Instagram reel](https://www.instagram.com/reel/DdAazp8N6O1/)
- Dronarchy YouTube titles, confirmed by oEmbed today. Contents were not viewable. Upload dates are relative, from earlier notes: about 2 months, 1 month and 2 weeks before 11 Nov.
  - "Bodycam Final Boss Rates & Tips" — [YouTube](https://www.youtube.com/watch?v=B2PnpkPOHLU)
  - "Bodycam PRO FPV Tutorial (Setups & Tricks) - Dronarchy" — [YouTube](https://www.youtube.com/watch?v=_uKgYhxVi-Q)
  - "Bodycam Master FPV (Tips & Drills)" — [YouTube](https://www.youtube.com/watch?v=oPEfwj6ePyY)
- Marcus Daelander:
  - Short, 2026-09-13 (earlier notes): "Want clean, surgical control in Bodycam instead of floaty movement? Here are the exact rate settings, camera angles, and physics tips I use as a real FPV pilot." — [YouTube Short](https://www.youtube.com/shorts/mMfWLxVADkc)
  - Titles confirmed today: "Real FPV Pilot's Guide to Flying in Bodycam (Settings & Physics)" — [YouTube](https://www.youtube.com/watch?v=fC0fVJtG3oQ); "Did Bodycam Accidentally Create the Best Combat FPV Sim?" — [YouTube](https://www.youtube.com/watch?v=nwkjwMOAB_4)
- Sloo: "MASTER the FPV Kamikaze Drone on Controller with these Settings [BODYCAM]" (title only). — [YouTube](https://www.youtube.com/watch?v=VzGcMDmGtnk)
- A Steam user pointed someone asking about controller settings for "drone mode 4" to NitroOnAir's "You Are Flying FPV Drones Wrong". The asker replied: "wow that helped me a lot, thank you very much" (2026-10-15). — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/567048404944918168/); [YouTube](https://www.youtube.com/watch?v=LrYk_IDKEYQ)

**Players on Steam** (anonymous; weigh lightly)
- "Jastool", 2026-09-03: "Pro pilot here and agree. Its in some wierd horizon mode by default. If you hit left bumper on your controller you can switch to acro. It flies decent. The drones are easier to shoot than people are. Also it takes forever to be able to use a drone." — [Steam "FPV FLYING"](https://steamcommunity.com/app/2406770/discussions/0/580555398932833398/)
- "Jastool", 2026-09-02 (earlier notes): "the drones fly okay using a xbox controller if you already know how to fly". — [Steam "Drone feedback"](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/)
- Steam thread "DRONES." — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563667534781906775/):
  - "VirpZ", 2026-09-21: "They are easy to shot because they have that gigantic hitbox."
  - "p.", 2026-09-13: "In 20 games i die maybe 2-3 times to drones. Just l2p."
  - "sugarNuts", 2026-09-21: "I also think they are too agile for a drone with a bomb and huge batteries strapped to them."
- Steam thread "Drones" — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/567046289380896675/):
  - "{FU}TheForgeryTTV", 2026-09-20: "The drones are extremely loud, blaring a siren every time they fly around."
  - "KOOCHIE KOOUUZIEE": "you can hear them just fine… there not that hard to shoot. just have to be patient".
  - "CQB", 2026-09-21: "i have no trouble hearing the kamikaze coming from 10 miles and it actually feels like they make you auto-hit when shooting at them".
- "Panzer_181", 2026-09-09: "I use them but It's hard to crash into player" / "Drones are interesting, but not really deadly". — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563667534781429767/)
- "Elijah", 2026-10-06: "You just have to pay attention and shoot them before it's too late, and they also have cooldowns." — [Steam "Delete Drones"](https://steamcommunity.com/app/2406770/discussions/0/587313700791465996/)
- Thread title only (I could not read the body): "I bought tryp fpv. The drone throttle is instantaneous in acro mode on here" ("Alley", 2026-09-09). — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563667534781369291/)
- "PotHat" (earlier notes): "Press right on the D-pad to toggle lower rates to make it easier to fly with a gaming controller." — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)

**Rate arithmetic** (my calculation, using Betaflight's source code)
- **The formulas:**
  - Betaflight's "Betaflight rates" function computes `angleRate = 200 × RC Rate × stick`, then multiplies by `1 / (1 − |stick| × Super Rate)`, after applying expo. — [Betaflight rc.c](https://github.com/betaflight/betaflight/blob/master/src/main/fc/rc.c)
  - Betaflight's default profile uses "Actual" rates with values 7 and 67. The code scales these ×10, giving a centre sensitivity of 70°/s and a maximum of **670°/s**. — [Betaflight controlrate_profile.c](https://github.com/betaflight/betaflight/blob/master/src/main/fc/controlrate_profile.c); [Betaflight rc.c (applyActualRates)](https://github.com/betaflight/betaflight/blob/master/src/main/fc/rc.c)
- **Full-stick rotation rates:**

  | Settings | Full-stick rate |
  |---|---|
  | DRONARCHY 1.88 / 0.80 / 0.10 | about 1,880°/s |
  | README's Bodycam defaults 2.0 / 0.64–0.69 | about 1,110–1,290°/s |
  | README's "normal freestyle" suggestion 1.0 / 0.65 | about 570°/s |
  | GamesFuze gamepad starting values 1.5 / 0.50 | 600°/s |
  | Betaflight firmware default (Actual rates) | 670°/s |

- **Sensitivity near centre** (degrees per second per full stick deflection): about 338 for DRONARCHY's settings versus about 170 for the README's suggestion.
- **Caveat:** this assumes Bodycam uses Betaflight's formula, which no source confirms. The README's "about 1100°/s" for RC Rate 2.0 matches the formula, which suggests its author applied the same formula rather than measuring it in-game.

### Inferences
- **Skills a match demands:**
  - Acro control of throttle and attitude together, at speed.
  - Flying low and close to cover, because the drone is loud and players call its hitbox generous.
  - A precise final dive onto a moving person with impact detonation ("hard to crash into player").
  - All of this while your own character is exposed, with only a few launches per match.

  These correspond to the later stages of educator progressions ("fly through gaps and avoid obstacles", then freestyle), not to hovering and first laps. See Q4.
- **Matches make a poor practice loop for a beginner:**
  - Few repetitions, because of cooldowns and per-match caps.
  - Each attempt ends in a detonation or a shoot-down.
  - Failure costs the team.
  - No source says this outright; it follows from the cited rules and player reports.
- **DRONARCHY's rates are expert-level sensitivity.** A beginner who copies them would get a very twitchy drone. Starting lower (the README's 1.0/0.65/0.15 or GamesFuze's values) and raising rates later is the safer path. This is my judgement, consistent with GamesFuze's advice.
- **Time in Bodycam's normal or casual mode is not FPV stick practice.** Per the README, its stick layout is not a quadcopter layout. On a gamepad the throttle sits at 50% when the stick is released, unlike a radio's throttle, which stays where you leave it.

### Gaps
- No official numbers for cooldown length, drones per match, blast radius or hitbox size.
- The contents of the creator videos (DRONARCHY's drills, Marcus Daelander's physics notes) were not viewable. Only titles and short descriptions are confirmed.
- Unknown whether v0.9 changes default rates, cooldowns, hitbox or throttle response.
- Unknown whether Bodycam's rate math matches Betaflight's.
- The body of the "throttle is instantaneous" thread could not be read.

## 4. Readiness milestones FPV educators use, and how they map to a sensible point to start Bodycam

### Takeaway
**Evidence: Rotor Village**
- At least 3 hours in the simulator.
- 10–15 hours bridge the gap.
- Drills go from hovering in one spot to flying through a single gate, then laps.
- "a few consecutive laps without a major 'reset'" means ready for a first real flight.

**Evidence: Oscar Liang**
- Ideally 5–10 hours; his TL;DR says 10+ hours learning Acro.
- His progression: controls and muscle memory → Acro through gaps and around obstacles → basic freestyle.
- 100+ crashes before buying an expensive drone.
- "Avoid using Xbox controllers or keyboards".

Neither source mentions games or a "fun" stage, so **any mapping to Bodycam is judgement.**

**My judgement:**
- Try the v0.9 lobby circuit (radio, Acro) once the user can fly consecutive simulator laps without a major reset, which is about 10–15 hours.
- Use drones in matches only after he can fly Acro through gaps and around obstacles. Start in self-hosted or bot games.
- At 30–60 minutes per evening, that is about 10–30 practice evenings from the start, which puts it at the end of November or in December 2026. By then the v0.9 notes and early impressions will exist.

### Cited Findings
**Educator evidence**
- **Rotor Village** (retailer blog, fetched 2026-11-11; no author or date shown) — [Rotor Village](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/):
  - "Spend at least three hours in the simulator."
  - "By putting in just 10 to 15 hours in a simulator, you bridge the gap" (earlier notes describe the gap as between "basic survival" and "basic control").
  - "Practice hovering in one spot, then practice flying through a single gate."
  - "Once you can fly a few consecutive laps without a major 'reset,'… you are officially ready for your first 'Maiden Flight' with a real drone."
  - On controllers: "Gaming controllers have spring-loaded sticks that snap back to the center on both sides" and "A real FPV radio has a 'friction' throttle on the left side that stays exactly where you put it."
  - It sets no milestone for freestyle or "fun" flying, and it does not mention Bodycam or games.
- **Oscar Liang** (byline 19 Apr 2025, edit log "Apr 2025 – Updated guide"; fetched 2026-11-11) — [Oscar Liang, FPV drone guide](https://oscarliang.com/fpv-drone-guide):
  - "ideally at least 5 to 10 hours"
  - "Dedicate 10+ hours to simulator training, master flying in Acro mode (aka manual mode)"
  - "Aim for 100+ crashes under your belt before investing in a premium or more expensive model"
  - "Auto-level mode acts like a pair of crutches, helpful for balance but limiting in more dynamic situations"
  - Simulator goals, listed as bullets that read as a progression: "master the controls and develop basic muscle memory" / "learn manual mode (aka acro mode), fly through gaps and avoid obstacles and try not to crash" / "attempt basic freestyle maneuvers and techniques, such as flips, rolls and split-S"
  - "Avoid using Xbox controllers or keyboards, as they won't provide the same benefits."
- **Unmanned Tech** (earlier notes, snippet only): on the real drone, "fly in angle mode until you are comfortable switching to acro". — [Unmanned Tech](https://blog.unmanned.tech/common-mistakes-fpv-drone-beginners-make-and-how-to-avoid-them/)

**People who enjoy Bodycam's drone already had skills**
- "Jastool": "if you already know how to fly" (Q3).
- NitroOnAir practised in the simulator Uncrashed before testing Bodycam (earlier notes, description snippet). — [YouTube](https://www.youtube.com/watch?v=kqvw-i8uxKg)
- A DCInside user wrote "드론 시뮬레이터 질린 참이었는데 이 게임이 딱이네" (2026-09-07; earlier notes). — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=bodybodycam&no=2037)

**Bodycam-specific low-pressure options**
- v0.8 players' advice: host a private bot-only Deathmatch (Q1, "FPV Training" thread).
- ExitLag suggests Deathmatch (search summary only).
- v0.9 keeps self-hosted games ("host your own game to play with up to 10 friends"). — [Steam, 2026-10-29](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)

### Inferences
Everything in this section is **judgement, not evidence.** The gates borrow the educators' milestones because no source sets one for games.

**Gate A, the first ~3 hours (Rotor Village's minimum): no Bodycam drone time needed.**
- Goal: radio and simulator set up, flying in Acro, hovering and passing a single gate.
- Bodycam adds little at this stage. Its casual mode builds no FPV stick skill.
- At 30–60 minutes per evening, this is about 3–6 evenings, roughly the first week.

**Gate B, at about 10–15 hours: the v0.9 lobby drone circuit, with the same radio, in Acro, alone.**
- Trigger: a few consecutive simulator laps without a major reset (Rotor Village's "maiden flight" bar; Oscar Liang's 10+ hours).
- Why: the circuit is a lap course, so it tests the same skill, and with a radio the stick feel matches.
- Treat it as a reward or variety session, not the main practice. Its respawn and feedback loop are unknown.
- At 30–60 minutes per evening this is about 10–30 evenings, roughly 2–6 weeks at five evenings a week.

**Gate C, after Acro gap and obstacle flying is comfortable (Oscar Liang's second goal): drones in matches.**
- Start in a self-hosted bot game or Deathmatch, then move to public matches.
- Use moderate rates (e.g., the README's 1.0/0.65/0.15), not 1.88/0.80/0.10.
- No hour count can be sourced for this gate.

**Timing relative to v0.9**
- A user who starts the simulator now reaches Gate B around the end of November or in December 2026. By then the v0.9 patch notes, radio compatibility and first pilot impressions will be public.
- So nothing about practice requires buying or playing Bodycam on 13 Nov.
- Radio delivery time is not included in these estimates; another researcher covers radios.

**Exception**
- If the user wants Bodycam as a Call of Duty–style shooter, playing it does no harm.
- He just should not count casual-mode or gamepad drone time as FPV training (Rotor Village and Oscar Liang on gamepads; the README on Bodycam's normal-mode layout).

### Gaps
- No educator source addresses games like Bodycam or sets a "fun" or freestyle gate. The mapping above is ours.
- No study measures skill transfer between Bodycam and dedicated simulators or real flight.
- The Rotor Village page shows no date or author.
- The difficulty of the TRYP-built lobby race is unknown until people fly it.

## 5. Practical limits: PC, price, Korean support, mature content, and whether keyboard or gamepad play remains possible

### Takeaway
- **PC:** Windows 10/11 only. Minimum: Ryzen 7 3700X / i7-9700K, 8 GB RAM, RX 5700 / RTX 2070 (8 GB), 50 GB, SSD recommended. Recommended: RTX 3060 12 GB / RX 6600 XT, 16 GB RAM.
- **Price:** ₩37,500, no discount (re-checked 11:48 UTC).
- **Language:** Korean text; voice is English only.
- **Mature content:**
  - Steam descriptors are "Frequent Violence or Gore" and "General Mature Content".
  - Rated 18 in Brazil, Germany and Indonesia.
  - Steam's data shows **no Korean rating**, and Steam applies no age gate.
  - v0.9 adds zombie horror.
- **Controls:** keyboard/mouse and gamepad stay supported for the game; the developer calls gamepad support "rough around the edges". Nothing official says gamepad or keyboard drone control goes away in v0.9; the radio is presented as optional. Whether Acro works on keyboard/mouse is still disputed.
- **Anti-cheat:** Easy Anti-Cheat arrives with v0.9. Its effect on unofficial virtual-controller tools is unknown.

### Cited Findings
- **Steam appdetails, cc=kr, pulled 2026-11-11 11:48 UTC (20:48 KST)** — [Steam appdetails (KR)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean):
  - Price: `price_overview` initial 3750000, final 3750000, discount_percent 0, "₩ 37,500".
  - Platforms: windows true, mac false, linux false.
  - Minimum: "Windows 10/11 … AMD Ryzen 7 3700X, Intel Core i7-9700K … 8 GB RAM … AMD Radeon RX 5700 (8 GB), NVIDIA GeForce RTX 2070 (8 GB) … 초고속 인터넷 연결 … 50 GB 사용 가능 공간 … SSD 권장".
  - Recommended: "AMD Ryzen 7 3800X, Intel Core i7-10700K … 16 GB RAM … AMD Radeon RX 6600 XT (8 GB), NVIDIA GeForce RTX 3060 (12 GB)".
  - Languages: "영어*, 프랑스어, 이탈리아어, 독일어, 스페인어 - 스페인, 아랍어, 일본어, 한국어, 러시아어, 중국어 간체 / *음성이 지원되는 언어".
  - `content_descriptors` ids [2, 5], with the note "Game contains shooting and killing events of other players as it involves gunfights in order to progress in the game." (Steam IDs 2 and 5 are "Frequent Violence or Gore" and "General Mature Content".)
  - `ratings`: dejus 18 ("Violência Extrema / Linguagem imprópria / Atos criminosos"); steam_germany 18 ("Drastische Gewalt / Derbe Sprache"); igrs 18 ("Kekerasan / Horor / Penggunaan bahasa"). No Korean entry. `required_age` 0.
  - Categories include "컨트롤러 완벽 지원", "DualSense 컨트롤러 지원", "Steam Input API 지원", "앱 내 구매" and "가족 공유". Genres include "앞서 해보기". Release date "2024년 6월 7일".
- The Korean store text is machine-translated; "rates" became "속도" (earlier notes). — [Steam appdetails (KR)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- **v0.8 notes (re-verified):** "Settings and controls received a major overhaul, including keyboard and mouse, gamepad, audio, video, graphics, and key rebinding." / "Gamepad support is playable but still rough around the edges, and you may encounter issues." / "FPV drones cannot use dedicated radio controllers in this update. They can currently be controlled with standard Xbox and PlayStation controllers." — [Steam, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- **Forum, 2026-11-07 to 11-09, on controllers** — [Steam "Controller support?"](https://steamcommunity.com/app/2406770/discussions/0/563672718159245875/):
  - "Humperdoo": "Yes, but it's Beta and not final… I play m+k"
  - "CAPERJIM": "The regular game has full contoller support… I use controller only on PC."
  - "Spector3": "the controller is ok just wish there was a way to tweak certain settings"
  - "UncleSam": "it does not have 'full controller support'. apparently it's 'full controller support for drones'"
- **Keyboard/mouse drone flying is disputed** (earlier notes):
  - "You cant fly MnK, thats super dumb" ("fud", 2026-09-08) — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
  - "anathema" says he flies on keyboard — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/)
  - GamesFuze lists keyboard/mouse binds — [GamesFuze](https://gamesfuze.com/guides/bodycam-how-to-use-fpv-drones-and-rc-cars/)
  - A DCInside wish asks for "FPV드론 키마로 속도 똑같이 낼수 있게 지원" — [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=bodybodycam&no=1857)
- **v0.9 (official):** "If you have a radio controller, plug it in and give it a go." / "Easy Anti-Cheat arrives with 0.9." / The party system is not in 0.9. — [Steam, 2026-10-29](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981). On the solo zombie mode: "It is a lot scarier." — [Steam, 2026-11-11 09:07 UTC](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1849192144177820)
- **Reception figures:**
  - 경향게임스 (figures the article attributes to the developer): "7만2,900건 이상의 유저 리뷰를 바탕으로 81%의 긍정 평가", wishlists of more than 3.7 million, and a peak of more than 38,900 concurrent players. — [경향게임스 via DCInside khgames](https://gall.dcinside.com/board/view/?id=khgames&no=12268)
  - Earlier notes (11 Nov store page): Korean-language reviews "복합적 (748)", 69% positive; recent reviews 87% of 3,075. — [Steam store KR](https://store.steampowered.com/app/2406770/?cc=kr&l=korean)
- **Korean rating:** a web search found no GRAC (게임물관리위원회) classification for Bodycam. — [search result set incl. Steam page](https://store.steampowered.com/app/2406770)

### Inferences
- For a Korean adult beginner, the main practical hurdles are the PC (an RTX 2070-class GPU and 50 GB on an SSD) and the fact that the drone is one gadget inside a ₩37,500, 18+-rated (abroad), violent Early Access shooter.
- Gamepad and keyboard remain usable for the game itself. For FPV practice value, what matters is the radio (other researchers cover radios).
- Once v0.9's native radio support arrives, a beginner should not need the unofficial "Bodycam FPV Fix": an unsigned exe plus a virtual-controller driver, with some antivirus flags. This is my judgement.

### Gaps
- Korea's GRAC rating status is unknown: I did not query the GRAC database, and Steam KR shows no rating.
- Not verified in-game: how the Korean UI translates drone settings (rates, expo, throttle mid).
- Unknown whether gamepad or keyboard drone controls change in v0.9.
- Unknown whether Easy Anti-Cheat affects ViGEm-based virtual controllers such as the unofficial radio tool. Do not predict either way.
