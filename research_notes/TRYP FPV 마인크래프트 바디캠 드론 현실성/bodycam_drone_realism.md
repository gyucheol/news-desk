# Bodycam drone realism, 11–12 Nov 2026: the live v0.8 flight model, what v0.9 promises, the 24-hour playtest, TRYP FPV's role and pilots' verdicts

**Research window:** 2026-11-12 00:02–00:10 UTC (09:02–09:10 KST).
- That is just after the end of 11 Nov UTC, about 15 hours into the 24-hour v0.9 playtest, which closes 12 Nov 09:00 UTC (18:00 KST).
- v0.9 is not out until Fri 13 Nov 2026, so everything about v0.9 below is **[pre-release]**.

**"Earlier notes"** means the four files named in the assignment. Facts they already establish are only referenced here, not re-argued.

**Labels:**
- **[official claim]**: Reissad or TRYP statements. These are claims, not proof.
- **[page-read]**: I read the text on the page or in the raw API.
- **[snippet-only]**: seen only in a search-engine summary.

**Bottom line for the writer.** In this window nothing had changed in Bodycam's live drone handling since v0.8 shipped on 2 Sep 2026:
- no new patch;
- no v0.9 patch notes;
- no official list of flight-model changes;
- nobody has publicly described flying v0.9 with a real radio.

"Very close to real FPV" therefore rests on developer and partner claims, plus mild verdicts on v0.8 from a few pilots.

## 1. What the live (v0.8) drone flight model does today, and what v0.9 says will change in flight and controls

### Takeaway
**Today's handling is v0.8's.** The live build is v0.8 "Locked & Loaded" (2 Sep 2026). The last patch on Steam is hotfix #6 (25 Sep), and as of 12 Nov 00:02 UTC there are no v0.9 patch notes.

**What v0.8 is documented to do:**
- a stabilized "casual" mode, which a fan wiki says holds altitude and position;
- a manual Acro mode;
- Betaflight-style rates (earlier notes);
- momentum ("keeps going until you correct");
- per one anonymous player, an "instantaneous" throttle in Acro.

**What is not documented:**
- Pre-release footage shows battery voltage on the HUD, but no source says battery, wind, drag, prop wash or signal range actually shape the flight.
- Durability is described only as impact detonation (Kamikaze) and "one bullet" (earlier notes).

**What v0.9 promises [pre-release]:** v0.9 still has only Reissad's general promise of radio support and "a lot of feedback on how our drone flies". Nobody, official or fan, has published:
- supported radios or protocols;
- calibration;
- rate defaults;
- camera angle;
- latency details.

**The contrast with TRYP's own simulator.** TRYP FPV openly claims to model per-propeller prop wash, LiPo voltage sag, ONERA-derived aerodynamics and optional video-delay effects. Bodycam makes no such specific claims.

### Cited Findings
**The live build is unchanged**
- **Bodycam Steam news feed, pulled 2026-11-12 00:02 UTC [page-read]:**
  - The newest item is still "The Bodycam v0.9 Playtest is LIVE: bring your 3 friends", 2026-11-11 09:07:51 UTC (18:07 KST).
  - Before it: the playtest notice (11-10 17:05 UTC), Devlog 1/2 (11-05), the v0.9 date post (10-29) and "Bodycam PATCH NOTES · V0.8 #6" (2026-09-25 14:55 UTC), which is the last patch.
  - There is no v0.9 patch-notes post and no drone-flight post.
  - Sources: [ISteamNews feed, app 2406770](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2406770&count=12&maxlength=0); [hotfix #6](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1844751498224827)
- **Store text re-pulled 2026-11-12 is unchanged [official claim]:** "Bodycam faithfully recreates authentic FPV piloting with realistic flight physics, Stabilized and Full Manual (Acro) flight modes, and advanced tuning options including rates, throttle curves, and flight profiles."
  - It still says nothing about radio controllers.
  - The category list is "Full controller support; DualSense Controller Support; Steam Input API Support…" with **no VR category**.
  - Source: [Steam appdetails API, cc=us, English](https://store.steampowered.com/api/appdetails?appids=2406770&cc=us&l=english)

**How v0.8 flies, as described by others**
- **Fan wiki, read today** [page-read; it calls itself "an unofficial fan-made resource"; last updated 2026-09-04]. Lines not quoted in the earlier notes:
  - "Push the drone forward and it keeps going until you correct."
  - Drone "Can hover and ascend" and "Can hold position in the air".
  - "Aggressive Profile — higher sensitivity for fast attacks and close-range maneuvers"
  - "Precision Profile — lower sensitivity for controlled scouting and precise positioning"
  - "Adjust in the tablet settings before you fly."
  - The page has **nothing** on battery or flight time, range or signal loss, top speed, altitude ceiling, wind, prop wash, crash damage or hit counts.
  - Source: [bodycamgame.wiki](https://bodycamgame.wiki/guides/drones-and-rc-vehicles/)
- **Throttle response.** Anonymous player "Alley", Steam thread posted 2026-09-09 01:17 UTC (10:17 KST), 0 replies [page-read]:
  - Title: "I bought tryp fpv. The drone throttle is instantaneous in acro mode on here"
  - Body: "So if your bummed like me the acro mode is not like the playtest so the next thing to do is get tryp fpv game."
  - "The playtest" here means the pre-release v0.8 playtest of late August, not the current one.
  - Source: [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563667534781369291/)
- **VidaExtra** (Alberto Martín, 2026-09-08 08:13 UTC). The earlier notes flagged this wording as unverified; I re-checked it today by asking WebFetch for the verbatim Spanish:
  - "Los desarrolladores también implementaron el Modo Manual/Realista, que desactiva todas las asistencias y simula la física de vuelo de un dron real de estas características."
  - "El modo estabilizado/arcade cuenta con ayudas de autonivelación"
  - "Sobra decir que no es una simulación 1:1, pero numerosos comentarios señalan que está muy bien conseguido."
  - Source: [VidaExtra](https://www.vidaextra.com/fps/piloto-drones-real-ha-probado-drones-fpv-bodycam-se-ha-sacado-mejores-jugadas-que-veras-mucho-tiempo)

**The community radio bridge "Bodycam FPV Fix"** (third party; describes how v0.8 reads input) [page-read]
- Releases since the earlier notes (which cited v1.0.1): v1.0.0 (8 Oct), v1.0.1 (9 Oct), v1.1.0 (9 Oct), v1.2.1 (12 Oct) and **v1.2.2 (14 Oct 2026, latest)**.
- v1.2.2 notes:
  - "Arm, Acro and button taps always end after 150 ms, also with radios that only send a report when something changes."
  - "RadioMaster Pocket confirmed working."
- Every release repeats: "Keep the Arm switch off whenever you are on foot." / "While Arm is on, the throttle stick goes to the game and your character walks backwards."
- No release mentions v0.9, the playtest, native support or TRYP.
- Source: [GitHub releases](https://github.com/lukas-Logikfabrik/bodycam-fpv-fix/releases)
- The earlier notes cite this tool's README for two points. Bodycam's default rates are "RC Rate 2.0, which is about 1100°/s at full stick". On the left stick, down = 0%, centre = 50% and up = 100% throttle.
- **Nexus Mods page [snippet-only]:** a search summary says only "the BETAFPV LiteRadio has been tested in the game so far". That conflicts with the GitHub v1.2.2 note on the RadioMaster Pocket, and is probably older text. — [Nexus Mods](https://www.nexusmods.com/bodycam/mods/66)

**What v0.9 says will change** [pre-release, official claims]
- The only official v0.9 drone wording is still the 29 Oct post (earlier notes):
  - "They helped us add support for FPV radio controllers and gave us a lot of feedback on how our drone flies."
  - "If you have a radio controller, plug it in and give it a go."
  - "Full patch notes on release day."
  - Source: [Steam, 2026-10-29](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)
- **Games Press release "Bodycam v0.9 Zombie Update & Public Playtest"** (read today; no date shown in what I read):
  - The only drone line is "A new lobby room for drones and RC cars."
  - It says nothing about FPV, radios, TRYP, a circuit or a race.
  - It confirms "The update goes live on Steam on Friday, November 13, 2026."
  - Source: [Games Press](https://www.gamespress.com/en-US/Bodycam-v09-Zombie-Update-Public-Playtest)
- **bodycamzombie.wiki** (undated fan wiki, "not affiliated with or endorsed by Reissad Studio"):
  - It restates the announcement: "That partnership added support for FPV radio controllers, flight feedback, and the drone race placed in the lobby."
  - Its tips "Plug in before you queue, not mid-match" and "A few clean laps to feel the flight model" are the wiki's own advice, not official.
  - It gives no calibration or physics detail.
  - Source: [bodycamzombie.wiki](https://www.bodycamzombie.wiki/en/updates/bodycam-zombie-update)
- **What I searched for and did not find**, officially or in previews:
  - supported radios or protocols (USB HID/joystick, ELRS/EdgeTX, DJI);
  - a calibration screen;
  - arm and Acro switch mapping;
  - rate defaults for radios;
  - camera-angle changes;
  - latency changes;
  - any flight-model change list.
  - Sources: [ISteamNews feed](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2406770&count=12&maxlength=0); [Games Press](https://www.gamespress.com/en-US/Bodycam-v09-Zombie-Update-Public-Playtest)

**Partner contrast: what TRYP FPV says its own simulator models** [official claims about TRYP, not about Bodycam]
- **2026-06-02 "MASSIVE UPDATE – New Locations, Battery System, OSD Editor & More":**
  - "Battery Simulation (Activable in gameplay settings) Real LiPo behavior in flight. Amperage and current draw vary dynamically with motor effort. Full throttle costs amps. Voltage SAG under load."
  - "Propwash (VRS) - Each prop now analyzes its own airflow in real time (angle of attack, neighbor turbulence, PID reaction). The quad fights itself exactly like on the field."
  - Source: [TRYP Steam post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1833968530900390)
- **2025-12-18 "MAJOR IMMERSION UPDATE":**
  - "a major physics & aerodynamics rework"
  - "analog and digital effect with optional input delay"
  - "thanks to ONERA's Data and +90 beta testers feedbacks"
  - "We still do not consider our physics to 1.0, as our PHYSICS MATCHER System is not yet deployed"
  - Source: [TRYP Steam post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1819386365090550)
- **TRYP store text:** "Wind effects, air resistance, and acceleration are carefully calibrated using digital twin technology". — [Steam appdetails, app 1881200](https://store.steampowered.com/api/appdetails?appids=1881200&cc=us&l=english)

### Inferences
- **Two different questions.** "Is Bodycam close to real FPV today?" has two halves:
  - Physics concept: manual Acro, Betaflight-style rates and momentum are present, so there is partial support for "close".
  - Controls: the official input is still a gamepad until 13 Nov, so there is no support for "close" yet.

  The report should keep these apart.
- **Throttle.** If "instantaneous" throttle is accurate, it is a simplification. In real quads, throttle response depends on motor and propeller inertia and on battery sag. This is general FPV knowledge, not a Bodycam source, and the claim comes from one anonymous player.
  - "not like the playtest" also hints that Acro handling changed between the late-August v0.8 playtest build and the 2 Sep release. Single source, unverified.
- **Simpler than a dedicated sim.** TRYP explicitly describes per-prop prop wash, voltage sag and wind. No equivalent Bodycam claims or guide descriptions exist. That suggests Bodycam's model is simpler than a dedicated simulator, but missing documentation does not prove the features are missing.
- **Arm and Acro are buttons in v0.8.** The bridge sends 150 ms button "taps" for Arm and Acro. So in v0.8 these are gamepad toggles, not radio switch positions.
  - The throttle-walks-the-character warning shows the drone shares the character's input map.
  - Whether native radio support in v0.9 changes this (proper switch channels, separate input mapping) is unknown.
- **Korean glosses for the writer:**
  - prop wash: 프롭워시, the shake when the drone drops into its own propeller turbulence
  - voltage sag: 전압 강하, power fading under load
  - rates: 레이트, how fast the drone rotates per stick input (the Korean store mistranslates this as "속도")

### Gaps
- v0.9 patch notes are due 13 Nov (release hour not stated). Until then these are unknown: radio list and protocols, calibration, rate defaults, camera tilt, latency and any flight-model changes.
- No source either way on whether Bodycam simulates battery depletion, wind, drag, prop wash or signal range. No numbers for top speed, altitude ceiling, drone HP or the Sentinel's crash durability.
- The "instantaneous throttle" and "not like the playtest" claims are unverified (one anonymous post, 0 replies).

## 2. Does the 24-hour v0.9 playtest (11 Nov 09:00 UTC – 12 Nov 09:00 UTC) include drones, and what first impressions were posted?

### Takeaway
**Still unconfirmed** as of 2026-11-12 00:09 UTC (09:09 KST), about 15 hours in:
- Reissad has posted nothing since 11 Nov 09:07 UTC (18:07 KST).
- That post's "What's in the playtest" list names only zombie content (earlier notes).

**No first impressions of the drone room or radio support found** in any source I could reach:
- Steam forums (100 most recently active threads);
- the playtest app;
- Games Press;
- extended web searches.

Reddit, YouTube, X, Discord and Twitch were not reachable. **The report cannot cite any hands-on v0.9 radio impression.**

### Cited Findings
- **Official posts unchanged** [page-read]:
  - The 10 Nov post lists "Drone and RC lobby: a new room with a drone circuit and an RC car circuit, FPV controllers supported" under v0.9 features.
  - The 11 Nov 09:07 UTC post's "What's in the playtest" lists only Zombie Trenches and the reworked Village and Asylum (earlier notes).
  - No newer post existed at 00:02 UTC 12 Nov.
  - Sources: [Steam, 2026-11-10 17:05 UTC](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1848664643360428); [Steam, 2026-11-11 09:07 UTC](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1849192144177820); [ISteamNews feed](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2406770&count=12&maxlength=0)
- **Games Press playtest release:**
  - "a public playtest runs for 24 hours, from Wednesday, November 11 at 09:00 UTC to Thursday, November 12 at 09:00 UTC"
  - "Places are limited."
  - "There is no NDA: players are free to stream and share what they see."
  - It does not list what the playtest contains.
  - Source: [Games Press](https://www.gamespress.com/en-US/Bodycam-v09-Zombie-Update-Public-Playtest)
- **Steam General Discussions**, Steam's forum JSON pulled about 00:05 UTC 12 Nov [page-read]:
  - The 100 most recently active threads have last posts from 2026-11-04 13:39 UTC to 2026-11-11 23:49 UTC (12 Nov 08:49 KST); 47 had a post on 11 Nov UTC.
  - **No thread title** contains drone, FPV, radio, TRYP, transmitter, gimbal, ELRS, EdgeTX, Acro, TX16, RadioMaster, controller, RC car, circuit, race or stick.
  - The newest threads were "Anti Cheat & Linux" (23:49 UTC), "Can you play the Zombies Solo or with a Duo?" (23:33 UTC), a Russian-language community thread, and "DO NOT BUY! BROKEN GAME, FAKE PLAYTIME BUG, AND ZERO SUPPORT." (23:24 UTC).
  - Sources: [Steam forum JSON](https://steamcommunity.com/forum/44020457/General/render/0/?start=0&count=100); [Steam General Discussions](https://steamcommunity.com/app/2406770/discussions/0/)
- **The only drone-room thread** ("… HELL OPEN THE DRONE ROOM AND KILL HOUSE--- LAZY DEVS????!") has no reply after 2026-11-06 04:13 UTC. That last reply ("Spector3") reads: "theres soon to be a second dev log for purely pvp." — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563672611395077500/)
- **The "Bodycam Playtest" app (2746700):**
  - Its news feed is empty and its discussions page returned no topics.
  - The store API gives the name "Bodycam Playtest" with an empty description.
  - Sources: [ISteamNews feed, app 2746700](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=2746700&count=12&maxlength=0); [Steam forum, app 2746700](https://steamcommunity.com/app/2746700/discussions/); [appdetails, app 2746700](https://store.steampowered.com/api/appdetails?appids=2746700&cc=us&l=english)
- **Other channels checked:**
  - Steam's reviews JSON endpoint returned no data (non-JSON): [endpoint](https://store.steampowered.com/appreviews/2406770?json=1&filter=recent&language=english&num_per_page=100)
  - Reddit's public JSON returned HTTP 403: [r/BodycamGame](https://www.reddit.com/r/BodycamGame/new.json?limit=50)
  - Extended web searches found only pre-playtest coverage and guides, e.g. [iGameMag](https://igamemag.com/bodycam-update-0-9-the-dead-and-damned/) and [dlcompare](https://www.dlcompare.com/gaming-news/bodycam-the-dead-damned-update-brings-back-zombies-89288).
- **YouTube:** I could not get date-sorted search results, video pages or captions. YouTube's bot check blocks normal requests. An attempt with yt-dlp's alternative player clients was refused by this session's permission system, and I did not pursue it further.
- **X, Discord and Twitch** were not reachable or not checkable. This includes @ReissadStudio and @TRYPFPV on X, and Discord, where Reissad collects playtest feedback.

### Inferences
- If the drone room were in the playtest build, it would be odd for Reissad's own "What's in the playtest" list to leave it out. That points toward drones not being a playtest focus, but it is not proof.
- With no NDA and feedback routed to Discord, impressions may exist on Discord, Twitch or X where I cannot see them. "None found" here means "none in reachable public sources by 00:09 UTC 12 Nov", not "none exist".
- For the report: the first trustworthy radio impressions will most likely come after the 13 Nov release, alongside the patch notes.

### Gaps
- Whether the playtest build contains the drone room and native radio support.
- Any Discord, X, Twitch, YouTube or Reddit posts from 11–12 Nov.
- Anything posted after 00:10 UTC 12 Nov, including the last ~9 hours of the playtest.

## 3. TRYP FPV's role: shared physics code, or tuning feedback and radio support only?

### Takeaway
**Only Reissad has described the collaboration.** Its words cover three things:
- help implementing radio-controller support;
- "a lot of feedback on how our drone flies";
- help building the lobby drone race.

It **never says** TRYP supplied physics code or a flight engine.

**TRYP has said nothing about Bodycam in any source I could read.** TRYP FPV (Steam developer and publisher "UNDEAD BATTERY") has posted nothing about Bodycam on Steam (newest post 15 Jun 2026). Its X account surfaced in search with no Bodycam mention [snippet-only].

**So the supported description is "partner feedback on handling + radio support + race design".** "Bodycam uses TRYP's physics" is unsupported.

### Cited Findings
- **Reissad** [official claims; the earlier notes have the full text]:
  - v0.8 developer note (2 Sep 2026): "We have partnered with Tryp FPV, an ultra-realistic flight simulator, to help us implement dedicated radio controller support." — [Steam v0.8 notes](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
  - v0.9 post (29 Oct 2026): "For the drone, we teamed up with the team behind TRYP FPV. They helped us add support for FPV radio controllers and gave us a lot of feedback on how our drone flies. They also helped us put together the drone race you'll find in the lobby." — [Steam v0.9 post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981)
- **Press goes further than Reissad.** VR.one (earlier notes) says TRYP "tuned how the drone flies", which is stronger than Reissad's "gave us a lot of feedback". — [VR.one](https://vr.one/blog/bodycam-zombies-update)
- **TRYP's side:**
  - Steam feed (app 1881200), checked 2026-11-12 00:02 UTC [page-read]: the newest post is "HOTFIX 260609" (2026-06-15, author "TRYP DEV TEAM"). No post in the feed mentions Bodycam or Reissad. — [ISteamNews feed, app 1881200](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=1881200&count=12&maxlength=0)
  - Search summary of X @TRYPFPV [snippet-only; X not fetchable]: it posts about its own racing work ("a race it designed on a helicopter carrier"), with no Bodycam mention in the results. — [X @TRYPFPV](https://x.com/trypfpv?lang=en)
- **Who TRYP is:**
  - Steam lists "TRYP FPV: Drone Racer Simulator" with developer and publisher **"UNDEAD BATTERY"**, release date "Jun 30, 2022", and categories "Single-player; Partial Controller Support; Family Sharing". — [Steam appdetails, app 1881200](https://store.steampowered.com/api/appdetails?appids=1881200&cc=us&l=english)
  - A French FPV retailer sells TRYP bundled with a RadioMaster T8L ELRS radio [snippet-only]. — [lacameraembarquee.fr](https://www.lacameraembarquee.fr/en/simulator/19519-tryp-fpv-simulator-pack-with-radiomaster-t8l-elrs-24ghz-radio-controller.html)
- **TRYP's physics credentials** [TRYP's own claims about its own simulator]:
  - 2024-12-19: "Thanks to an unexpected partnership with ONERA (the French Aerospace Research Center), our R&D team will be now externalized…" — [TRYP post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1786573930630486)
  - 2025-02-11: "our partnership with ONERA (french National Office for Aerospace Studies and Research) and access to a wind tunnel will allow us to bring even more accurate physics to the game in the future!" — [TRYP post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1790848102780269)
  - 2025-12-18: per-component drag and lift "thanks to ONERA's Data and +90 beta testers feedbacks", and "We still do not consider our physics to 1.0". — [TRYP post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1819386365090550)

### Inferences
- **What the evidence supports:** TRYP acted as an expert partner on input (radios) and handling feel, and as course designer for the lobby race. It does not support shared code. Reissad could have adopted TRYP techniques without saying so, but no source says it did.
  - Writer: avoid "built on TRYP's physics" or "the same physics as TRYP FPV".
- **Commercial context:** TRYP gains exposure to Bodycam's large audience, and Reissad gains credibility with pilots. Any TRYP-side praise would be partner promotion, not independent assessment.
- **Who flew v0.9 early:** "Gave us a lot of feedback on how our drone flies" implies TRYP's team flew pre-release builds. They are the only known pre-release v0.9 flyers, and they are an affiliated party.
- **Nationality:** TRYP looks French-linked (the ONERA partnership, French retailers, a GMIF 2022 French video in search results). That is an inference, and the studio's location is unconfirmed.

### Gaps
- No TRYP or Undead Battery statement about Bodycam: X, Instagram and Discord were not readable.
- No statement from either side on whether code, physics parameters or input libraries were shared.
- Undead Battery's location and size are unconfirmed.

## 4. What named real FPV pilots say about the drone feel, including anyone who tested v0.9 before release

### Takeaway
**No named pilot verdict could be read today.** I still found no detailed, independent, quotable verdict on the flight feel from a named real FPV pilot, and no named pilot or creator has publicly reported flying a v0.9 build.

**One correction to the earlier notes.** VidaExtra's text shows that **Just_Gonz himself gave no opinion** in the featured video ("No ofrece opiniones al respecto"). The "no es una simulación 1:1" verdict is the journalist's, not the pilot's.

**What remains:**
- Steam handles: "Flies decent" (Jastool, earlier notes) and the anonymous "throttle is instantaneous" post.
- Kyle Macinnes / SubTwoFifty placing Bodycam in **tier C** of his FPV-simulator tier list (earlier notes).
- Videos by ItsJackFPV, Marcus Daelander and NitroOnAir whose verdicts stayed inaccessible.

### Cited Findings
- **Just_Gonz** ("piloto de drones FPV experimentado alemán y creador de contenido", per VidaExtra):
  - "No ofrece opiniones al respecto, pero sí un tutorial de cómo conectar un mando especializado a Steam"
  - "Hace exactamente lo mismo e incluso cosas más locas en la vida real con el mismo mando."
  - Source: [VidaExtra, 2026-09-08](https://www.vidaextra.com/fps/piloto-drones-real-ha-probado-drones-fpv-bodycam-se-ha-sacado-mejores-jugadas-que-veras-mucho-tiempo)
  - Affiliation: per the earlier notes, his Instagram caption tags @reissad.studio, with no paid-partnership label seen.
- **VidaExtra's own judgement:** "Sobra decir que no es una simulación 1:1, pero numerosos comentarios señalan que está muy bien conseguido."
  - The article's comment section contained no comments, so "numerosos comentarios" refers to comments elsewhere and is unsourced in the article.
  - Source: [VidaExtra](https://www.vidaextra.com/fps/piloto-drones-real-ha-probado-drones-fpv-bodycam-se-ha-sacado-mejores-jugadas-que-veras-mucho-tiempo)
- **ItsJackFPV, Marcus Daelander and NitroOnAir:** today's searches returned no transcript, review or quote of their verdicts (search results did not even mention ItsJackFPV or Marcus Daelander by name). Only titles and description snippets are known (earlier notes). — [ItsJackFPV, YouTube](https://www.youtube.com/watch?v=gHGbrgvHm9g); [Marcus Daelander, YouTube](https://www.youtube.com/watch?v=nwkjwMOAB_4)
- **Anonymous Steam user "Alley"** (not a verified pilot; owns TRYP FPV), 2026-09-09: "The drone throttle is instantaneous in acro mode on here" and "the acro mode is not like the playtest". — [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563667534781369291/)
- **v0.9 pre-release testers:** the only party known to have flown v0.9 builds is "the team behind TRYP FPV" ("gave us a lot of feedback on how our drone flies"). They are a partner, and no individuals are named. — [Steam v0.9 post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981). No creator v0.9 preview video or post was found in reachable sources as of 00:09 UTC 12 Nov (see Q2).
- **Context from the earlier notes, not re-verified today:**
  - Jastool (self-described "Pro pilot"): "Flies decent" and "fly okay using a xbox controller if you already know how to fly".
  - DRONARCHY FPV: "Proving you can fly here full acro with a real drone controller". Flown on a TX16S via x360ce; the post tags @radiomasterrc.
  - Marcus Daelander: his settings promise "clean, surgical control in Bodycam instead of floaty movement".
  - SubTwoFifty: Bodycam in tier C.

### Inferences
- **The evidence base is thin, all from v0.8, mostly with workaround radios.** The creators who flew with real radios (Gonz, DRONARCHY) show that the game can be flown in full Acro with a radio. Neither, in what can be read, says how close it feels to a real quad.
- **Affiliation flags for the report:**
  - TRYP FPV: commercial partner; the only v0.9 pre-release flyers.
  - Reissad: the developer; "same everything" style claims come from its own promotion (earlier notes).
  - DRONARCHY: tags radio maker RadioMaster.
  - Just_Gonz: tags Reissad's Instagram.
  - Marcus Daelander: has a business-inquiry line.
  - No paid-promotion disclosure was found for any of them, and none could be fully checked.
- **Reading the creator signals:**
  - "Floaty" (Marcus, as a problem his settings fix) and "instantaneous throttle" (Alley) point in different directions.
  - Both suggest the default feel differs from a tuned real quad.
  - Neither is a measured comparison.

### Gaps
- Actual verdicts in ItsJackFPV's, Marcus Daelander's and NitroOnAir's videos (YouTube inaccessible; see Q2).
- Creators' real-world credentials (race results, professional work) are unverified.
- Anyone besides TRYP who flew v0.9 before release.

## 5. Deliberate gameplay departures from real FPV

### Takeaway
**Departures already sourced:**
- launches rationed by cooldowns and per-match caps;
- drones made "very easy to destroy" ("One bullet and it's gone", pre-release narration);
- a hitbox players call generous;
- impact detonation;
- an assisted mode that holds position;
- loud drone audio;
- the feed shown on the monitor, with no VR or goggles category on Steam;
- "CAM DISCONNECTED" static;
- map sky limits;
- the pilot's body left exposed while flying.

**Undocumented either way:** battery-time limits, signal range, wind, simulated video latency and hard speed caps.

**New today:** nothing in the v0.9 material says any of these will change.

**Even TRYP makes realism optional.** TRYP's own simulator makes battery sag and video input delay optional settings.

### Cited Findings
- **Official rules** (earlier notes) [official claim]:
  - "Added a deployment cooldown system for both drones and RC cars, including an additional cooldown on loadout change to prevent abuse."
  - "Added a team LED identification system to drones and RC."
  - Source: [Steam v0.8 notes](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1842846814441066)
  - Tech Times: "intentionally capped in per-match availability". — [Tech Times](https://www.techtimes.com/articles/324962/20260819/bodycam-v08-devlog-stress-driven-reloads-lead-locked-loaded-overhaul.htm)
- **Pre-release narration** (earlier notes; it speaks as the makers but its official source is unverified):
  - "We built a very precise hitbox system so they're actually very easy to destroy. One bullet and it's gone."
  - "A casual mode, it's simple, accessible and very efficient for newer players."
  - Source: [Instagram reel 2](https://www.instagram.com/reel/DcOcxWci_EO/)
- **Assisted flight and the screen-only feed** (fan wiki, unofficial):
  - Casual mode "maintains altitude and position automatically"; drone "Can hold position in the air".
  - "It streams a first-person video feed to your screen while your character stands still in the world."
  - Source: [bodycamgame.wiki](https://bodycamgame.wiki/guides/drones-and-rc-vehicles/)
- **No VR support listed:** Bodycam's Steam categories include no VR entry. — [Steam appdetails](https://store.steampowered.com/api/appdetails?appids=2406770&cc=us&l=english)
- **Input sharing in v0.8** (third-party tool, not a design statement): "While Arm is on, the throttle stick goes to the game and your character walks backwards." — [GitHub releases](https://github.com/lukas-Logikfabrik/bodycam-fpv-fix/releases)
- **Speed and agility, conflicting anonymous claims** (earlier notes):
  - A DCInside post says drone "피격범위랑 속도" are nerfed.
  - Steam user sugarNuts: "too agile for a drone with a bomb and huge batteries strapped to them".
  - Sources: [DCInside](https://gall.dcinside.com/mgallery/board/view/?id=bodybodycam&no=1983); [Steam thread](https://steamcommunity.com/app/2406770/discussions/0/563667534781906775/)
- **Sky limits:** a request for "a large map with high sky limits" implies an altitude ceiling on current maps (earlier notes). — [Steam "FPV Training"](https://steamcommunity.com/app/2406770/discussions/0/587313051305508524/)
- **v0.9 material changes none of this:**
  - No v0.9 source mentions changes to cooldowns, hitbox, durability, battery or speed.
  - Only the RC car gets a stated handling pass: "We reworked its game feel and controls so it's more fun to drive."
  - Sources: [Steam v0.9 post](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1847920302235981); [Games Press](https://www.gamespress.com/en-US/Bodycam-v09-Zombie-Update-Public-Playtest)
- **Dedicated-sim contrast** [TRYP's claims]:
  - "Battery Simulation (Activable in gameplay settings)" — [TRYP post, 2026-06-02](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1833968530900390)
  - "analog and digital effect with optional input delay" — [TRYP post, 2025-12-18](https://steamstore-a.akamaihd.net/news/externalpost/steam_community_announcements/1819386365090550)

### Inferences
- **Why these departures exist:** they serve shooter balance (cooldowns, caps, one-shot fragility, generous hitbox, loud audio) and accessibility (casual mode, gamepad play). They are not realism failures in the physics code. A beginner should read Bodycam's drone as "FPV physics inside a shooter's rules".
- **What a beginner would notice going from Bodycam to a real FPV drone** (general FPV knowledge, not from a Bodycam source):
  - you fly with goggles over a radio video link that can lag or break up;
  - the battery visibly limits each flight;
  - crashes cost money rather than a cooldown;
  - there is no position-hold "casual" mode on a typical FPV quad.

  Another researcher's sources should back these points if the report states them.
- **The v0.9 lobby race may relax combat limits.** It is a practice space, so its rules on respawns and cooldowns could differ from matches. No source says how it works.

### Gaps
- Official numbers for cooldown length, drone HP, top speed, altitude ceiling, battery time and range: none found.
- Whether the v0.9 drone room has cooldowns, respawn delay, lap timing or free flight.
- Whether "CAM DISCONNECTED" signals range loss, a crash or only the launch transition. The earlier notes saw it in clips without context.
