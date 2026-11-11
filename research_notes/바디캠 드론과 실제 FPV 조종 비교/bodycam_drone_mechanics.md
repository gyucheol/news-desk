# Bodycam (Reissad Studio): official facts and how its FPV drones are controlled and simulated

Research date: 2026-11-11 (Steam API/store data pulled 2026-11-11 06:53–06:56 UTC = 15:53 KST). Primary sources are the official Steam store API/page and Reissad's own Steam announcements, pulled raw through Steam's `ISteamNews` API. Third-party guides and forum posts are labelled as such. Times are UTC unless marked KST.

## 1. What is Bodycam? (developer, publisher, genre, status, platforms, app ID, Korean price, Korean support, ratings)

### Takeaway
Bodycam (Steam app 2406770) is a Windows-only, Unreal Engine 5, "ultra-realistic" multiplayer FPS shown through a body-camera view. It is made and self-published on Steam by Reissad (Reissad Studio), a studio started by two French brothers, Luca and Léo. It has been in Early Access since 7 June 2024 and is still in Early Access as of 2026-11-11. On 2026-11-11 the Korean Steam price was ₩37,500 with no discount. Korean is supported as text only (no Korean voice). Several foreign rating boards rate it 18+, but no Korean (GRAC) rating appears on the Steam data.

### Cited Findings
**Identity and studio**
- Steam app ID **2406770**, name "Bodycam", type game. Steam lists **Developer: "Reissad"** and **Publisher: "Reissad"**. The legal notice reads "Reissad 스튜디오 / Reissad", and the website is https://www.reissad.com/ — [Steam appdetails API, cc=kr&l=korean, fetched 2026-11-11](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- The v0.8 patch notes open with "A Message from Luca, Léo & the Reissad Team": "It marks the transition from a game we developed as two brothers in our bedroom… into something much bigger… When Bodycam launched in Early Access in 2024, you trusted us." — [Steam announcement "Bodycam Major Update OUT NOW!", 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- Wikipedia says the studio was founded by French developers Luca and Leo, "aged 17 and 20" in 2024-era coverage, and that it uses Unreal Engine 5. A cited Les Echos article places them in Nanterre. — [Wikipedia: Bodycam (video game)](https://en.wikipedia.org/wiki/Bodycam_(video_game))
- An official press release has a Paris, France dateline and quotes **Luca Dassier, Studio Director**. The PR contact is Not A Shark (Vincent Gallopain). Note that Steam still lists Reissad as publisher; the release does not call Not A Shark the publisher. — [Games Press release, 2026-08-19](https://www.gamespress.com/Reissad-Studio-Releases-First-Devlog-for-Bodycams-Massive-Locked-and-L)
- Growth: the v0.8 release-date post says "Bodycam has grown from a project created by Luca and Leo into a full development studio" — [Steam announcement, 2026-08-06](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1840310314342178). An 80.lv interview (Jan 2026) reportedly says the studio grew "from 2 to 30 people". This comes from a search-result summary only; I did not open the page. — [80.lv](https://80.lv/articles/bodycam-developer-talks-the-studio-s-growth-bodycam-development-future-plans)

**Genre and status**
- English store text: "Bodycam is the first ultra-realistic multiplayer FPS built to recreate the intensity of real combat. Experience tactical firefights through the lens of a body camera… No crosshair. No ammo counter. No HUD." — [Steam appdetails API (English text), fetched 2026-11-11](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english)
- Korean store genres: 액션, 인디, 대규모 멀티플레이어, 시뮬레이션, 전략, **앞서 해보기**. Release date shown as "2024년 6월 7일" with coming_soon false. — [Steam appdetails API, KR](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- The Korean store page still shows the "앞서 해보기 게임" (Early Access) box: "참고: 앞서 해보기 게임은 완성된 게임이 아니며 개발이 진행됨에 따라 크게 바뀔 수 있습니다." — [Steam store page KR, fetched 2026-11-11](https://store.steampowered.com/app/2406770/?cc=kr&l=korean)
- The v0.8 notes call that update "a major step toward Bodycam 1.0". No 1.0 date was found. — [Steam announcement, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- Modes listed on the store: 2v2 Wingman (Search & Destroy), 5v5 Body Bomb, Team Deathmatch, Deathmatch, Hardpoint, Gun Game, and co-op Zombies. — [Steam appdetails API (English)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english)

**Platform and hardware**
- Platforms: Windows only (mac false, linux false). Minimum specs: Windows 10/11, Ryzen 7 3700X / i7-9700K, 8 GB RAM, RX 5700 / RTX 2070 (8 GB), 50 GB storage, SSD recommended. — [Steam appdetails API, KR](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- Controller categories: "컨트롤러 완벽 지원" (full controller support), "DualSense 컨트롤러 지원", "Steam Input API 지원". Other categories include "앱 내 구매" (in-app purchases). — [Steam appdetails API, KR](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)

**Korean price (as of 2026-11-11 06:53 UTC / 15:53 KST)**
- `price_overview`: currency KRW, initial 3750000, final 3750000, discount 0%, formatted **"₩ 37,500"** — [Steam appdetails API, cc=kr&l=korean](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean). The Steam storesearch API with cc=kr returned the same 3750000 / 3750000 — [Steam storesearch API, cc=kr](https://store.steampowered.com/api/storesearch/?term=bodycam&cc=kr&l=korean)
- The store page also offers a "Bodycam Playtest 참가" button (separate playtest app 2746700). — [Steam store page KR](https://store.steampowered.com/app/2406770/?cc=kr&l=korean)

**Korean language**
- Supported languages: "영어*, 프랑스어, 이탈리아어, 독일어, 스페인어 - 스페인, 아랍어, 일본어, **한국어**, 러시아어, 중국어 간체 / *음성이 지원되는 언어". Only English has an asterisk, so there is **no Korean voice**; Korean is text only. — [Steam appdetails API, KR](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- The Korean store description reads as machine-translated. "Miss a check, and you pay for it" became "수표를 놓치면 비용을 지불하게 됩니다", and in the drone paragraph the English "rates" became "속도". — compare [KR](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean) and [EN](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english) store text

**Age rating and content warnings**
- Steam `required_age`: 0 (no Steam age gate in the API data). Content descriptor IDs are 2 and 5 (Steam's "Frequent Violence or Gore" and "General Mature Content"). The developer's note says: "Game contains shooting and killing events of other players as it involves gunfights in order to progress in the game." — [Steam appdetails API, KR](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- Ratings in the Steam data:
  - Brazil (DEJUS): **18** ("Violência Extrema, Linguagem imprópria, Atos criminosos")
  - Germany (steam_germany): **18** ("Drastische Gewalt, Derbe Sprache")
  - Indonesia (IGRS): **18** ("Kekerasan, Horor, Penggunaan bahasa")

  The Korean store page's `game_rating` field is null, so no GRAC/게임물관리위원회 rating is shown. — [Steam appdetails API](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean); [Steam store page KR](https://store.steampowered.com/app/2406770/?cc=kr&l=korean)

**Commercial context**
- Wikipedia reports that Bodycam was Steam's best seller in its first EA week "despite mixed reviews" (citing Windows Central, 2024-06-08). It also reports 800,000 units and about €20 million by July 2024 (citing Les Echos, 2024-07-30). — [Wikipedia](https://en.wikipedia.org/wiki/Bodycam_(video_game))
- Official post title: "Bodycam Has Reached 3,000,000 Wishlists!" — [Steam announcement, 2026-08-30](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842212951308447)
- Other Steam titles also contain "Bodycam": Backrooms Bodycam (3746210), Bodycam 1997 (3824510), VHS Bodycam (3907620), BoneField: Bodycam Horror (2567770) and more. — [Steam storesearch API](https://store.steampowered.com/api/storesearch/?term=bodycam&cc=kr&l=korean)

### Inferences
- For a Korean beginner, Bodycam is a ₩37,500 Early Access military/police shooter. Drones are one gadget in it, not the main product. It also needs a fairly strong Windows PC (RTX 2070-class GPU minimum, 50 GB).
- The 18+ ratings abroad and the violence descriptors matter if the report is aimed at a younger reader. Korea's own rating status is unknown.
- Machine-translated Korean store text suggests in-game Korean terms for drone settings (e.g., "rates") may also be confusing. This has not been checked in-game.

### Gaps
- Korea GRAC rating not found. I did not check the GRAC database; the Steam KR page shows none.
- Steam's language table (interface vs subtitles split for Korean) was not separately confirmed. The API string only shows that Korean has no voice.
- No official 1.0 release date found.

## 2. The drone update: official name, version, date, and what the patch notes say

### Takeaway
Drones arrived in **v0.8 "Locked & Loaded"**, released **2 September 2026 at 17:00 UTC** (3 Sept 02:00 KST). At launch, the FPV drone worked only with standard Xbox/PlayStation gamepads. Real RC radio support was promised with help from the simulator **TRYP FPV**. That radio support, plus a drone race circuit in the lobby, comes in **v0.9 "The Dead & Damned"**. v0.9 is due **Friday 13 November 2026**, with a limited 24-hour playtest on 11–12 November. As of 2026-11-11, v0.9's full patch notes are not yet published.

### Cited Findings
**Timeline (official Steam announcements unless noted)**
- 2025-09-28, "Behind the Scenes: Our Journey & Next Steps" (posted by account "Lucadass11"): "We applied the same philosophy to the drones and the RCs… just like weapons, they come with their own loadout system. You'll be able to swap wheels, change the body shell, customize spoilers, add stickers, replace antennas, edit rotors, change cameras, and more. For drone and RC fans (like myself), the goal was simple: to allow you to recreate the drone or RC car you have at home inside Bodycam." — [Steam announcement, 2025-09-28](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1811772772353877)
- 2026-03-06, "BODYCAM 2026 ROADMAP PART 1" (posted by community manager account "NoAimGirlKane"): "Drones and RC-Cars can be unlocked through progression and are impactful tactical tools… Speaking of the drones, they've been upgraded with a brand-new realistic handling, based on real physical properties, like a real simulation, with the FPV Accro Modes. So if you're an experienced drone-pilot, it's your time to shine. Don't worry if you're not, the casual mode is still available." — [Steam announcement, 2026-03-06](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1826362059925643)
- 2026-08-06: "Bodycam Major Update v0.8: Locked & Loaded will release on September 2, 2026." — [Steam announcement, 2026-08-06](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1840310314342178)
- Devlogs:
  - 2026-08-18, Devlog 1/4: "The introduction of tactical gadgets, including FPV drones and RC cars." — [Steam, 2026-08-18](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1840944183788763)
  - 2026-08-25, Devlog 3/4 (Trenches map): "Dedicated areas designed for FPV drones and RC cars." — [Steam, 2026-08-25](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1841579228678435)
- 2026-08-19 press release: the update brings "new physics-based FPV drones and explosive RC-cars". — [Games Press, 2026-08-19](https://www.gamespress.com/Reissad-Studio-Releases-First-Devlog-for-Bodycams-Massive-Locked-and-L)
- 2026-09-02: "The Locked and Loaded update officially releases today at 17:00 UTC." — [Steam announcement, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814440084)

**v0.8 patch notes, "Drones & RC Cars" section, verbatim** — [Steam "Bodycam Major Update OUT NOW! | Trench Warfare, Loadout System & Much More!", 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
> "Drones and RC cars have been added as major new gameplay tools, expanding the tactical options available during a match. Players can now use remote controlled equipment to scout, create pressure, gather information, and interact with the battlefield in new ways. These additions were also supported by improvements to camera transitions, audio feedback, controls, and overall handling."
> Highlights: "Added Drones as a new gameplay feature." / "Added RC Cars as a new gameplay feature." / "Added dedicated drone and RC handling, camera support, and FPV presentation." / "Added a team LED identification system to drones and RC." / "Added a deployment cooldown system for both drones and RC cars, including an additional cooldown on loadout change to prevent abuse." / "Added a cooldown indicator with an audio notification when the gadget becomes available again."
> **Developer Note:** "FPV drones cannot use dedicated radio controllers in this update. They can currently be controlled with standard Xbox and PlayStation controllers. We have partnered with Tryp FPV, an ultra-realistic flight simulator, to help us implement dedicated radio controller support. This feature is already in development and will arrive in a future update."

- Other lines from the same v0.8 notes:
  - "Some areas are currently closed for maintenance, including the obstacle course, shoot house, and drone and RC car rooms. These rooms will open soon"
  - "Settings and controls received a major overhaul, including keyboard and mouse, gamepad, audio, video, graphics, and key rebinding."
  - "Gamepad support is playable but still rough around the edges, and you may encounter issues."

  — [Steam, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- v0.8 hotfix #1 includes "Fixed tablet inputs being consumed by gameplay controls." and "Improved drone audio." — [Steam "PATCH NOTES · V0.8 #1", 2026-09-03](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814444061). Hotfixes #2–#6 (09-04 to 09-25) contain no drone-flight changes; the only related lines cover tablet screen rendering and RC car textures. — [#4, 2026-09-11](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1843481262695778), [#5, 2026-09-18](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844115010495008), [#6, 2026-09-25](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844751498224827)

**v0.9 "The Dead & Damned", verbatim** — [Steam "BODYCAM V0.9 THE DEAD & DAMNED - RELEASE DATE & WHAT'S COMING", 2026-10-29, posted by account "cdechabert"](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)
> "Bodycam v0.9 releases on Friday, November 13." / "0.9 is a smaller, in-between update."
> "A new room in the lobby: The lobby gets its biggest room yet, dedicated to drones and RC cars, with a circuit for each. For the drone, we teamed up with the team behind TRYP FPV. They helped us add support for FPV radio controllers and gave us a lot of feedback on how our drone flies. They also helped us put together the drone race you'll find in the lobby. If you have a radio controller, plug it in and give it a go. The RC car got some love too. We reworked its game feel and controls so it's more fun to drive."
> "Full patch notes on release day."
- Playtest post: "free 24-hour playtest… Opens: Wednesday, November 11 at 09:00 UTC… Closes: Thursday, November 12 at 09:00 UTC… Places are limited and not everyone will get access." The feature list includes "Drone and RC lobby: a new room with a drone circuit and an RC car circuit, FPV controllers supported". In KST the window is 11 Nov 18:00 to 12 Nov 18:00. — [Steam "The Dead & Damned Playtest", 2026-11-10](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1848664643360428)
- Official trailers and videos on the "Bodycam Game" YouTube channel (@ReissadStudio):
  - "Bodycam Major Update Release Date Short Teaser | V0.8 Locked & Loaded" ([nLhNxUkAAX4](https://www.youtube.com/watch?v=nLhNxUkAAX4))
  - Playtest reactions compilation "We Didn't Pay Them to Say This" ([GaTzJzDq6GA](https://www.youtube.com/watch?v=GaTzJzDq6GA))
  - v0.9 video "We Added Zombies in the Trenches..." ([JEJxGCayPG4](https://www.youtube.com/watch?v=JEJxGCayPG4))
  - Playtest video "We Made a Zombie Game You Won't Want to Play" ([MUixsE-GaEU](https://www.youtube.com/watch?v=MUixsE-GaEU))

  Titles and channel come from the YouTube oEmbed API; I did not read the video descriptions.
- Korean press: Gamemeca (박재형 기자, 2026-08-25, "[오늘의 스팀] 더욱 극사실적으로, FPS '바디캠' 진화") wrote "이번 대규모 v0.8 업데이트는 다가오는 9월 2일에 적용된다" and "실제 물리 법칙이 적용된 FPV 드론 등이 추가된다." It gave no control details. — [게임메카, 2026-08-25](https://www.gamemeca.com/view.php?gid=1779585)

### Inferences
- In the public build on 2026-11-11, official radio support **does not exist yet** outside the closed 24-hour playtest. It lands for everyone only with v0.9 on 13 Nov 2026. Any report text saying "you can practise with a real radio in Bodycam" should be dated from 13 Nov 2026, and the details (which radios, calibration) will only be known from the v0.9 patch notes.
- The v0.9 note says TRYP FPV "gave us a lot of feedback on how our drone flies". That implies the flight model may have been retuned in v0.9. The v0.8 behaviour that players described (section 4) may not fully apply after 13 Nov.

### Gaps
- v0.9 full patch notes are not yet out ("Full patch notes on release day"). Unknown: supported radio types/protocols (e.g., USB joystick/HID mode), channel mapping and calibration UI, whether separate rate/expo profiles exist for radios, and whether the flight model changed.
- v0.9 release hour not stated in the posts I read.

## 3. Which drones exist, in which modes, and how they are used

### Takeaway
There is one FPV quadcopter gadget class, flown through the in-game tactical tablet. Third-party guides and players describe two variants: an explosive **Kamikaze** drone that detonates on impact, and a non-explosive **Sentinel** recon drone. A separate explosive **RC car** also exists. They sit in the loadout's gadget slot, are limited by cooldowns and per-match caps, carry team LEDs, and can be shot down. While flying, the player's body stays in the map and is exposed. I found no grenade-dropping drone and no DJI-style camera drone.

### Cited Findings
- Official uses: "scout, create pressure, gather information, and interact with the battlefield" — [v0.8 notes, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066). The store says: "Deploy FPV drones and reconnaissance RC vehicles to scout enemy positions, gather intelligence, strike targets, and support your squad." — [Steam appdetails API (EN)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english)
- Official on explosives and unlocks: "Drones and RC-Cars can be unlocked through progression… Get OMFOR out if they are camping with a drone or a RC-Car carrying an explosive." The Trenches map preview adds "The threat will also come vertically: watch out for the drones and the experienced pilots." — [Roadmap, 2026-03-06](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1826362059925643)
- The tablet is the hub: "You will be also able to use your gadgets and change your loadouts directly from the tablet." — [Roadmap, 2026-03-06](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1826362059925643)
- Variants (third-party guide, "Updated Sep 15, 2026", by Haider): **Kamikaze Drone**, offensive, "designed around reaching an enemy and detonating on impact", and you "sacrifice the drone when you make the attack". **Sentinel Drone**, reconnaissance, no explosive. Equip: tablet → Loadout → Gadget slot → "Swap Item" (default F). Deploy: press 5, then left click. Light strips show green (ready) or yellow (cooldown). The guide gives no cooldown length. — [GamesFuze](https://gamesfuze.com/guides/bodycam-how-to-use-fpv-drones-and-rc-cars/)
- Players on launch day agree:
  - "As far as I can tell it's impact detonation. That's why it has the wires coming off the front."
  - "You need to switch to the bomb drone on your item edit view."
  - One user hopes for "a drop-grenade option", which implies none exists.

  — [Steam discussion "Drone feedback", 2026-09-02](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/). Another player warns newcomers not to buy the Sentinel assuming only it can fly Acro, saying they "ended up with a bombless Kami". — [Steam discussion "Acro mode on drones how?", 2026-09-06 post](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
- Availability limits:
  - Tech Times: "Both gadgets are intentionally capped in per-match availability to keep them tactically meaningful rather than ubiquitous", and "RC cars can be equipped with explosives". — [Tech Times, Maxwell Templeton, 2026-08-19](https://www.techtimes.com/articles/324962/20260819/bodycam-v08-devlog-stress-driven-reloads-lead-locked-loaded-overhaul.htm)
  - Gaming Age: "Yes, everyone gets a drone on every loadout." — [Gaming Age, Austen Canupp, Sept 2026](https://gaming-age.com/2026/09/bodycam-locked-and-loaded-impressions-for-pc/)
- The operator's body is exposed: the drone "streams a first-person video feed to your screen while your character stands still in the world". The fan wiki notes that the tablet does not pause the game. — [bodycamgame.wiki (unofficial fan site), updated 2026-09-04](https://bodycamgame.wiki/guides/drones-and-rc-vehicles/)
- Practice locations:
  - At v0.8 launch the dedicated "drone and RC car rooms" were closed — [v0.8 notes](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066).
  - Players still flew in the firing range; one notes "the firing range has a respawn timeout after the drone explodes" — [Steam discussion, 2026-09-03](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/).
  - The store says you can "fly FPV drones" in the Shooting Range HUB — [Steam appdetails API (EN)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english).
  - v0.9 adds the drone circuit and a drone race — [Steam, 2026-10-29](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981).
- The official X account promotes drone kills, e.g., "His entire team got wiped out by a single FPV drone. Clip: Constant_Worry1061". This is the search-result title only; I did not open the post and its date is unknown. — [X @ReissadStudio](https://x.com/ReissadStudio/status/2095956982674936292)

### Inferences
- In matches, the drone is a short-lived, cooldown-gated **kamikaze/recon gadget** inside a shooter, flown while your own character is vulnerable. That is a very different practice context from open-ended flying sessions. Before v0.9, the only low-pressure flying space was the shooting range/lobby; v0.9's circuit and race are the first purpose-built practice course.
- The Kamikaze-FPV framing mirrors the military use of FPV drones (the store copy says "Modern warfare has been transformed by FPV drones"). It does not mirror hobby freestyle or racing.

### Gaps
- No official list of drone variants, unlock costs, cooldown seconds, blast radius or damage was found. Variant names (Kamikaze/Sentinel) come only from third-party guides and players.
- Which game modes allow drones (e.g., whether Zombies does) is not officially stated.
- Whether the 2025-promised drone part customization (rotors, cameras, antennas) actually shipped is not confirmed; players mention only an "item edit view".

## 4. How the drone is controlled and what physics are modelled

### Takeaway
Official sources confirm three things:
- "Stabilized and Full Manual (Acro) flight modes".
- "Advanced tuning options including rates, throttle curves, and flight profiles".
- Gamepad-only FPV control at v0.8 (Xbox/PlayStation), with real RC radio support arriving in v0.9 (13 Nov 2026).

Third-party guides and players describe the rest:
- A standard **Mode-2 stick layout** (left stick throttle/yaw, right stick pitch/roll), with **LB/L1 toggling Angle ↔ Acro** (stabilized mode is the default).
- **Betaflight-style rate settings**: RC Rate, Super Rate, RC Expo, Throttle Mid/Expo, camera tilt, and Low/Med/High sensitivity profiles.
- Momentum/inertia, and impact detonation on crash for the Kamikaze.

Keyboard & mouse support is disputed. I found no evidence of battery, wind, signal-range or video-interference modelling.

### Cited Findings
**Official (developer)**
- English store: "Bodycam faithfully recreates authentic FPV piloting with realistic flight physics, Stabilized and Full Manual (Acro) flight modes, and advanced tuning options including rates, throttle curves, and flight profiles." — [Steam appdetails API (EN), fetched 2026-11-11](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english)
- Korean store version: "Bodycam은 현실적인 비행 물리학, 안정화 및 완전 수동(Acro) 비행 모드, 속도, 스로틀 곡선 및 비행 프로필을 포함한 고급 튜닝 옵션을 통해 정통 FPV 조종을 충실하게 재현합니다." Here "rates" was translated as "속도". — [Steam appdetails API (KR)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- "FPV drones cannot use dedicated radio controllers in this update. They can currently be controlled with standard Xbox and PlayStation controllers." — [v0.8 notes, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- In v0.9, radio support comes via TRYP FPV: "If you have a radio controller, plug it in and give it a go." — [Steam, 2026-10-29](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)
- "brand-new realistic handling, based on real physical properties, like a real simulation, with the FPV Accro Modes… the casual mode is still available." — [Roadmap, 2026-03-06](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1826362059925643)
- Tech Times, citing a Steam news post: the drones "use real FPV flight physics" and include "an Accro mode (the unassisted manual flight mode experienced FPV pilots use)… alongside a more accessible casual mode." — [Tech Times, 2026-08-19](https://www.techtimes.com/articles/324962/20260819/bodycam-v08-devlog-stress-driven-reloads-lead-locked-loaded-overhaul.htm)

**Third-party guide: controls and settings (GamesFuze, updated 2026-09-15)** — [GamesFuze](https://gamesfuze.com/guides/bodycam-how-to-use-fpv-drones-and-rc-cars/)
- Gamepad mapping:
  - Left stick forward/back = **throttle**; left stick left/right = **yaw**.
  - Right stick forward/back = **pitch**; right stick left/right = **roll**.
  - **Left shoulder/bumper = flight-mode toggle** between "ANGL" (Angle) and "FPV Acro".
- Flight modes: ANGL is self-stabilizing and level, "slower and easier for enemies to shoot down". FPV Acro is full manual: the pilot manages level flight, throttle, pitch, roll and yaw.
- Keyboard & mouse: W/S/A/D move, Space ascends, Ctrl descends, mouse looks/aims. The author "strongly recommend[s]" a controller.
- Settings named in the guide:
  - Drone Camera Tilt (example value 15)
  - Sensitivity profiles Low/Medium/High (examples 70/110/150)
  - Roll/Pitch/Yaw **RC Rate** (1.50), **Super Rate** (0.50), **RC Expo** (0.25)
  - **Throttle Expo** (0.30), **Throttle Mid** (0.60)

  There is a separate table for FPV radios (e.g., RC Rate 1.00→1.85, Super Rate 0.50→0.80, RC Expo 0.50→0.10, Throttle Mid 0.30). The values are the author's suggestions, not official defaults.
- Real radios before native support: the guide describes mapping a radio as a virtual Xbox 360 controller with **x360ce**.

**Players (Steam forums, 2–8 Sept 2026)**
- "It's LB/L1 to toggle acro mode. FPV controllers aren't supported yet, only Xbox or PS controllers." The same poster says D-pad right toggles lower rates. Another says LB works on a PS5 controller. Players report starting "stuck in Angle mode". — [Steam "Acro mode on drones how?"](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
- Keyboard & mouse, conflicting reports:
  - "I don't think you can on M&K. Controller only" (2026-09-03).
  - "You cant fly MnK, thats super dumb" (2026-09-08).
  - Another user couldn't find the acro bind on M&K.

  — [same thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
  - Against this, a self-described drone pilot says they fly on keyboard & mouse and that the "twitchiness actually has made me more elusive tbh". — [Steam "Drone feedback", 2026-09-02](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/)
  - GamesFuze lists KB/M binds (above). **Conflict unresolved.**
- A self-described drone pilot (OP Jastool) says drones launch in a horizon-style mode, wants Acro as the default, and asks "Also please add 3D mode". 3D mode, meaning reversible motors for inverted flight, is therefore absent. — [Steam "Drone feedback", 2026-09-02](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/)

**Physics descriptions (third party)**
- Momentum: "If you push the drone forward and don't compensate for the movement, it keeps going." — [PixelNitro, 2026-09-03](https://pixelnitro.com/bodycam-game-2026-guide-to-explosive-fpv-drones-and-rc-vehicles/)
- Fan wiki on the modes:
  - Casual Mode: "stabilized flight. The drone maintains altitude and position automatically."
  - Acro Mode: "full manual control. No stabilization. You manage throttle, pitch, roll, and yaw yourself."

  — [bodycamgame.wiki (unofficial), 2026-09-04](https://bodycamgame.wiki/guides/drones-and-rc-vehicles/)
- Collisions: the Kamikaze detonates on impact (above). Drones can be shot down, and players call the hitbox "really generous". — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
- Drone audio is modelled and audible. It was improved in hotfix #1. — [Steam, 2026-09-03](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814444061)
- Unofficial radio mod: "Bodycam FPV Fix – Fly the drone with a real FPV radio" on Nexus Mods. A search-engine summary says it is MIT-licensed, made by a non-Reissad author, and turns a USB radio into a virtual Xbox controller with Bodycam's Acro layout. I could not verify this: the page returned HTTP 403. — [Nexus Mods](https://www.nexusmods.com/bodycam/mods/66)

### Inferences
- **Close to real FPV**:
  - Acro/rate mode exists.
  - Tuning uses Betaflight-style terms (RC Rate / Super Rate / RC Expo / Throttle Mid / Throttle Expo). Betaflight is the firmware most real FPV quads run.
  - Camera tilt is adjustable.
  - The gamepad layout matches Mode 2, which is what most FPV radios use.
  - Momentum is simulated.

  So the concepts a beginner learns (manual throttle, rate control, using camera uptilt) map onto real FPV. This rests on the official store wording plus third-party guides; I have not seen the menus myself.
- **Different from real FPV**:
  - Until v0.9 the official input was a gamepad. Thumbsticks are short and spring-centred, unlike a radio's non-centring throttle gimbal, so throttle muscle memory will not transfer directly. This is general hobby knowledge, not a Bodycam source.
  - The default mode is stabilized. The fan wiki says it holds altitude and position, which is more like a camera drone than an FPV quad. Real Betaflight Angle mode only self-levels.
  - No 3D mode.
  - There is no evidence of battery sag, flight-time limits, wind, signal range or analog/digital video break-up.
  - Flying happens in short, cooldown-gated bursts inside a firefight.
- The keyboard & mouse conflict is most likely explained this way: KB/M works in the stabilized mode with arcade-style ascend/descend keys, while Acro had no KB/M binding at launch. This is unconfirmed, and v0.8 hotfixes do not mention changing it.
- The developer chose to partner with a dedicated simulator (TRYP FPV) to tune its drone and add radio support. That implies the dedicated sim is the reference point, not the reverse.

### Gaps
- No official control documentation (bindings, default rate values, acro toggle) was found. Everything about stick mapping and setting names comes from third-party guides and players.
- I found nothing, official or credible, on battery/flight time, wind, gravity/thrust-to-weight numbers, prop damage, signal range, or video interference/static. There was also nothing on whether crashes destroy the non-explosive Sentinel.
- Whether v0.9 changes the flight model or adds radio-specific rate profiles is unknown until the 13 Nov patch notes.
- Whether "casual" mode truly holds altitude and position, or only self-levels, is reported only by the fan wiki.

## 5. Developer statements on realism, real pilots and drone operators

### Takeaway
Reissad markets the drone as "authentic FPV piloting" with "realistic flight physics… like a real simulation". The one concrete outside expert input is the partnership with the **TRYP FPV** simulator team. That team helped add radio support, "gave us a lot of feedback on how our drone flies", and built the v0.9 drone race. A studio lead describes himself as a drone/RC fan. I found no claim of working with military drone operators, and no marketing featuring named real FPV pilots.

### Cited Findings
- "We have partnered with Tryp FPV, an ultra-realistic flight simulator, to help us implement dedicated radio controller support." — [v0.8 notes, 2026-09-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
- "For the drone, we teamed up with the team behind TRYP FPV. They helped us add support for FPV radio controllers and gave us a lot of feedback on how our drone flies. They also helped us put together the drone race you'll find in the lobby." — [v0.9 announcement, 2026-10-29](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)
- TRYP FPV is itself a Steam FPV simulator. Its community hub is app 1881200 ("TRYP FPV General Discussions"). — [Steam Community, TRYP FPV](https://steamcommunity.com/app/1881200/discussions/0/4844274259591330535/)
- "For drone and RC fans (like myself), the goal was simple: to allow you to recreate the drone or RC car you have at home inside Bodycam." The post is by account "Lucadass11", which appears to be studio director Luca Dassier (an inference from the account name). — [Steam, 2025-09-28](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1811772772353877)
- "they've been upgraded with a brand-new realistic handling, based on real physical properties, like a real simulation… So if you're an experienced drone-pilot, it's your time to shine." — [Roadmap, 2026-03-06](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1826362059925643)
- "Modern warfare has been transformed by FPV drones. Bodycam faithfully recreates authentic FPV piloting…" — [Steam store (EN)](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=english)
- General realism framing: Luca Dassier, Studio Director: "Our relentless goal remains absolute realism and immersion, never seen or felt quite like this." The press release's drone line is only "new physics-based FPV drones and explosive RC-cars" and names no pilots or operators. — [Games Press, 2026-08-19](https://www.gamespress.com/Reissad-Studio-Releases-First-Devlog-for-Bodycams-Massive-Locked-and-L)
- Tech Times found no developer claims about consulting pilots; its realism wording comes from a Steam post. — [Tech Times, 2026-08-19](https://www.techtimes.com/articles/324962/20260819/bodycam-v08-devlog-stress-driven-reloads-lead-locked-loaded-overhaul.htm)

### Inferences
- The realism claims ("authentic", "like a real simulation") are developer marketing. No independent test (e.g., an FPV pilot reviewing for press) was found to back them. The concrete realism features are the acro mode, Betaflight-style rates, and the TRYP FPV tuning.

### Gaps
- No evidence of consultation with military/FPV drone operators, and no promotional campaign with named real pilots. The devlog video contents and trailer descriptions were not reviewed in full. A third-party video "Learn FPV on BODYCAM" exists, but its metadata could not be retrieved: [YouTube JAw6wrPTGgI](https://www.youtube.com/watch?v=JAw6wrPTGgI).
- TRYP FPV's own statements about the collaboration were not found.

## 6. How players and press received the drone update

### Takeaway
v0.8 sold well and recent reviews are strong overall, but drone-specific press coverage is thin. Most outlets mention drones only in passing, and no major English or Korean outlet reviewed the flight model.
- Players who fly real FPV said the drone "flies decent" or okay on a gamepad.
- Their complaints at launch: stabilized mode as default, no radio support, no 3D mode, no acro on keyboard & mouse, and drones being easy to shoot down with long cooldowns.

### Cited Findings
- Steam Global Top Sellers (SteamDB weekly list): Bodycam was **#4** for 1–8 Sep 2026 and **#3** for 8–15 Sep 2026. — [SteamDB weekly post, 2026-09-08](https://steamstore-a.akamaihd.net/news/externalpost/SteamDB/1842846814455661); [SteamDB weekly post, 2026-09-15](https://steamstore-a.akamaihd.net/news/externalpost/SteamDB/1843481262704621)
- Steam reviews as of 2026-11-11 (KR store page):
  - Recent: "최근 평가: 매우 긍정적 (3,075) – 지난 30일 동안의 사용자 평가 3,075개 중 87%가 긍정적입니다."
  - Korean-language: "한국어 평가: 복합적 (748) – … 748개 중 69%가 긍정적입니다."

  — [Steam store page KR](https://store.steampowered.com/app/2406770/?cc=kr&l=korean). Total recommendations: 68,697 — [Steam appdetails API](https://store.steampowered.com/api/appdetails?appids=2406770&cc=kr&l=korean)
- Pilot feedback, from posts dated 2–8 Sep 2026:
  - Self-described drone pilot OP: drones fly okay on an Xbox controller "if you already know how to fly"; wants Acro as default and "3D mode"; says "The drones are way to easy to shoot down" and the delay between drones is too long. Later: "Flies decent", and finds it easier to shoot drones than people.
  - Another pilot: flies on KB/M; owns a DJI controller and plays Liftoff and FPV Kamikaze; argues a shorter cooldown would lead to people "hanging out and sending drones all match".

  — [Steam "Drone feedback"](https://steamcommunity.com/app/2406770/discussions/0/580555398932735919/); [Steam "Acro mode on drones how?"](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
- Confusion and missing features at launch:
  - Players could not find the acro toggle ("stuck in Angle mode").
  - One guessed acro would come with "the actual Tx bindings with Tryp fpv".
  - One student pilot wanted to see "how my littlebird skills transfer".

  — [Steam "Acro mode on drones how?"](https://steamcommunity.com/app/2406770/discussions/0/580555398932743489/)
- Press:
  - Gaming Age (Austen Canupp, Sept 2026): "Bodycam in its current state is a solid 8/10 experience". Drones are mentioned only as a loadout item. — [Gaming Age](https://gaming-age.com/2026/09/bodycam-locked-and-loaded-impressions-for-pc/)
  - Tech Times (2026-08-19) and Gamemeca (2026-08-25) only relay the announced features. — [Tech Times](https://www.techtimes.com/articles/324962/20260819/bodycam-v08-devlog-stress-driven-reloads-lead-locked-loaded-overhaul.htm); [게임메카](https://www.gamemeca.com/view.php?gid=1779585)
  - Wikipedia summarises v0.8 as offering arcade-style or simulation handling for the drones, citing Tech Times. — [Wikipedia](https://en.wikipedia.org/wiki/Bodycam_(video_game))
- Official PR used a playtest reactions compilation titled "We Didn't Pay Them to Say This". — [YouTube, Bodycam Game](https://www.youtube.com/watch?v=GaTzJzDq6GA); [Steam "First Reactions", 2026-09-01](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842212951314690)
- Fan content exists, e.g., the Short "FPV in Bodycam #fpv #fpvdrone…" by Just_Gonz. — [YouTube](https://www.youtube.com/shorts/0fvbzgnVO2Y)

### Inferences
- The fact that real-radio users wrote x360ce guides and a Nexus mod within weeks shows real FPV pilots wanted to fly Bodycam's drone with their own radios. It also shows the v0.8 build did not support that natively.
- The Korean-language review score (69%, Mixed) is clearly lower than the recent global score (87%). The cause was not investigated; it may reflect older reviews from the 2024 launch.

### Gaps
- Drone-specific Steam review sentiment could not be quantified. The Steam reviews API redirected to the store homepage from this environment.
- I found no drone-focused coverage from PC Gamer, Rock Paper Shotgun, GamesRadar or 80.lv, and no Korean coverage beyond Gamemeca's preview (인벤, 디스이즈게임 and 루리웹 not found).
- v0.9 reception is unknown because it has not been released (due 2026-11-13).
