# How realistic FPV drone flight is in Minecraft as of 2026-11-11 (Propwash FPV and other mods)

**How I checked.** All pages were read on 2026-11-12 (UTC), one day after the as-of date. Propwash's last file is dated 2026-10-17, so nothing changed in between.

Sources read:
- **Developer site.** propwashfpv.com, including the JSON files behind its changelog and roadmap pages (both pages load by script).
- **CurseForge.** The page itself, plus the site's own API for the file list (with dates) and comments.
- **GitHub.** Raw files of `LardTom/propwash-fpv` at HEAD: README, CHANGELOG and the German developer docs. The developer publishes one source snapshot per release ("als Stand je Release"), and the site's changelog data names `"ref": "v0.5.2"`, so HEAD should be 0.5.2. German quotes are my translations.
- **Modrinth.** Its public API, for searches and the other mods' pages.
- **YouTube.** oEmbed metadata only.

Blocked or inaccessible: Reddit (HTTP 403), YouTube watch pages and yt-dlp ("Sign in to confirm you're not a bot"), the ModpackIndex page (403), Discord (needs login), and minecraft.net's store page (503). TikTok content is from search snippets only. I downloaded or ran no mod files.

This note does not repeat earlier notes. Those already cover SubTwoFifty's Reel 4 transcript and tier-A rating, his 2026-11-10 tier list, the site's badges, the 0.4.0 video and the "no Modrinth hit" result. See `바디캠 드론과 실제 FPV 조종 비교/reels_content.md` and `FPV 시뮬레이터 순위 검증/*.md`.

## 1. Propwash FPV: current version, supported Minecraft versions and loaders, update history, developer

### Takeaway
As of 2026-11-11 the latest release is **0.5.2**, uploaded to CurseForge on **2026-10-17**. It runs only on **Minecraft Java 26.3**, with **Fabric or NeoForge** and Java 25, and must be installed on both client and server.

It updated fast at first: five CurseForge releases in 23 days, from 0.3.2 (25 Sep) to 0.5.2 (17 Oct). Physics changed in most of them. It has been quiet for about 26 days since then, while the roadmap lists 0.6.0 as "in progress".

It is a solo project by **"lardtom"** (GitHub `LardTom`, CurseForge `tmlrd`), who writes his developer docs in German. The site links a Modrinth page, but no public Modrinth project exists.

### Cited Findings
- **CurseForge files, with exact upload times (UTC) and per-file downloads.** There are 10 files in total; the earliest on CurseForge is 0.3.2. — [CurseForge files (site API)](https://www.curseforge.com/api/v1/mods/1711041/files?pageIndex=0&pageSize=50&sort=dateCreated&sortDescending=true&removeAlphas=false)

  | Version | Date (UTC) | Fabric downloads | NeoForge downloads |
  |---|---|---|---|
  | 0.3.2 | 2026-09-25 09:20 | 2,013 | 2,520 |
  | 0.4.0 | 2026-10-05 21:46 | 2,094 | 2,354 |
  | 0.5.0 | 2026-10-11 18:30 | 20 | 12 |
  | 0.5.1 | 2026-10-12 14:48 | 83 | 72 |
  | 0.5.2 | 2026-10-17 18:15 | 1,957 | 1,749 |

- **Page details (2026-11-12).** Total downloads 12,876 ("12.8K"); the earlier notes recorded 12,740 a day before.
  - Project ID 1711041. Game version 26.3. Loaders Fabric and NeoForge. Environment "Client & Server". License "PolyForm Shield License 1.0.0".
  - Author "tmlrd" (Owner). Last updated October 17, 2026.
  - Links: wiki propwashfpv.com; source github.com/LardTom/propwash-fpv; a Discord for bug reports; a Ko-fi donation link; social accounts @propwash.fpv.minecraft.
  - Fetch-tool summary of the page. — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv)
- **Version history in the official CHANGELOG** (no dates given):
  - 0.1.0 "first public release"
  - 0.2.0, 0.2.1
  - 0.3.0, 0.3.1, 0.3.2
  - 0.4.0 "Parts API for add-ons, realistic flight times and battery…"
  - 0.5.0 "World rules, flight training, 59 freestyle tricks, 3D mode…"
  - 0.5.1
  - 0.5.2 "Fisheye lens, waterproof drones, turtle mode and zones"
  - So 0.1.0–0.3.1 came out before the first CurseForge file, on dates not given. — [CHANGELOG.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/CHANGELOG.md)
- **Changelog lines on physics and controls, verbatim.** — [changelog data](https://propwashfpv.com/assets/data/changelog.json); [CHANGELOG.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/CHANGELOG.md)
  - **0.1.0:**
    - "Flight model with motors, ESC, battery, rotor aerodynamics, ground effect, prop wash, wind and turbulence."
    - "Flight controller with Betaflight and Actual rates, PID tuning, Acro, Angle and Horizon, airmode, failsafe and GPS Rescue."
    - "EdgeTX and OpenTX radios over USB and gamepads, with a receiver wizard…"
    - "about 800 blocks of full radio range."
  - **0.4.0:**
    - "Battery level, OSD warnings and brownouts follow realistic power draw…"
    - "The built-in cinewhoop reaches a realistic 89 km/h instead of 62 km/h."
    - "Motors heat up under load…"
    - "*Gravity* slider… (0.80× to 1.50×) for pilots who find the drones a little floaty."
    - "Radios such as the Radiomaster Pocket are now detected on macOS."
    - "The receiver wizard reads the throttle and its direction from your movement…"
  - **0.5.0:**
    - "Flight physics checked against blackbox logs of real drones from whoop to 7″: no more floaty drops when you lower the throttle, whoops drop and dive like real ones (65 mm whoop 36 → 48 km/h), and punch-outs pull harder."
    - "The FPV image reacts more directly: your video system's delay no longer counts twice, so the picture arrives up to 12 ms (analog) or 10–20 ms (digital) sooner."
    - "Race drones carry their battery under the frame like real race quads: a lower center of gravity, a little snappier on roll and pitch…"
    - "Blackbox: every armed flight as a `.bbl` log for Blackbox Explorer or PIDtoolbox."
    - "3D mode…"
    - World-rule presets "*Realistic*, *Training* or *Arcade*"; "*Gravity* goes from 0 to 1000 %."
    - "Fly with mouse and keyboard…"
    - "The receiver wizard no longer stores the throttle the wrong way round."
  - **0.5.2:**
    - "Batteries discharge like real packs: nearly flat for most of the flight, a steep drop in the last ~10 %, and you feel the end of the pack in every punch."
    - "Drones touch down on their real frame… crashes end like real ones…"
    - "The 5″ race frame is a true X… about 147 km/h top speed instead of 168."
    - "Turtle mode."
    - "*Stick mode* 1–4."
    - "Zones… zero gravity in a race passage – race-legal or counted as assisted."
- **Compatibility is strict.** Network protocol 2 in 0.1.0 became 6, then 8 in 0.4.0, then 16. For 0.5.2: "client and server must both run 0.5.2 – 0.5.0 and 0.5.1 can't join a 0.5.2 server and the other way round." — [CHANGELOG.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/CHANGELOG.md); [RELEASE-NOTES.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/RELEASE-NOTES.md)
- **Requirements**, verbatim from the README: "Minecraft 26.3"; "Fabric Loader 0.19.5+ and Fabric API 0.161.0+26.3"; "NeoForge 26.3.0.10-beta or newer"; "Java 25"; "Required on both client and server"; Known limitations: "Only Minecraft 26.3." — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- **Roadmap.** "In the next release: 0.6.0 — Share codes, race data and add-on API", every item marked "progress":
  - "Share codes for every add-on", "More add-on API", "Add-on guidelines"
  - "Velocity vector in the OSD", "Freecam drone", "RX block"
  - "Race data for servers and bots", "Better courses"
  - No date is given. — [roadmap data](https://propwashfpv.com/assets/data/roadmap.json) ([page](https://propwashfpv.com/roadmap/))
- **Ports, in the developer's own replies:**
  - "not planned yet. maybe I'll make one. 1.21.1 is planned though" (to a Forge 1.20.1 request, 2026-10-16)
  - "it is coming in the future" (to "1.20.1 or 1.21.1?", 2026-10-26)
  - [CurseForge comments (site API)](https://www.curseforge.com/api/v1/mods/1711041/comments?pageIndex=0&pageSize=50)
- **Development time, per the developer.** "hard to say since it was an project which i paused multiple times before a release but 2-3 month maybe" (tmlrd, 2026-10-22). — [CurseForge comments](https://www.curseforge.com/api/v1/mods/1711041/comments?pageIndex=0&pageSize=50)
- **Developer identity:**
  - The site names the developer "lardtom", GitHub handle "LardTom" (fetch-tool summary). — [propwashfpv.com](https://propwashfpv.com/)
  - The code package is `de.lardtom.propwash`.
  - The binding flight-model spec is written in German and dated "Stand 2026-09-23". — [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
  - The site is in English and German and links "impressum/" and "datenschutz/" pages. — [propwashfpv.com](https://propwashfpv.com/)
  - The YouTube channel is "PropwashFPV" (@propwash.fpv.minecraft). — [YouTube oEmbed](https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=KSFZQzm-cxM&format=json)
- **License and source.**
  - "Ab 0.5.0 erscheint der Quellcode öffentlich auf GitHub, als Stand je Release ohne die interne Entwicklungsgeschichte." (From 0.5.0 the source appears publicly on GitHub, one snapshot per release, without the internal history.) — [RELEASE-NOTES.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/RELEASE-NOTES.md)
  - "The new license applies from 0.5.0 on; 0.4.0 and older stay All Rights Reserved." — [CHANGELOG.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/CHANGELOG.md)
  - The add-on API is MIT-licensed. — [propwashfpv.com](https://propwashfpv.com/)
- **Modrinth (conflicting evidence):**
  - The site links "https://modrinth.com/mod/propwash-fpv". — [propwashfpv.com](https://propwashfpv.com/)
  - A Modrinth API search for "propwash" returned 0 hits on 2026-11-12, and the slugs propwash-fpv, propwashfpv and propwash return 404. — [Modrinth API search](https://api.modrinth.com/v2/search?query=propwash&limit=10); [project lookup](https://api.modrinth.com/v2/project/propwash-fpv)
  - Modrinth user "LardTom" exists (created 2024-12-24). Its only public project is "Tom's Biome Mobs", a 2024 datapack. — [Modrinth API user projects](https://api.modrinth.com/v2/user/lardtom/projects)
  - This contradicts the 0.4.0 video's "Out now on Modrinth & CurseForge" (from earlier notes). — [YouTube KSFZQzm-cxM](https://www.youtube.com/watch?v=KSFZQzm-cxM)
- **Official add-on.** "Propwash: Just More Parts" 1.1.1 adds 143 parts and 22 presets and is made for Propwash 0.4.0–0.5.2 (fetch-tool summary). — [propwashfpv.com](https://propwashfpv.com/); [CurseForge JMP](https://www.curseforge.com/minecraft/mc-mods/propwash-just-more-parts)

### Inferences
- The mod's whole public life spans only about seven weeks (CurseForge since 25 Sep). Its physics was retuned in 0.4.0, 0.5.0 and 0.5.2.
  - SubTwoFifty's Part 9 (2026-09-29) and Dronarchy's clips (1–3 Oct) came out while **0.3.2 was the only CurseForge build** (0.4.0 arrived 5 Oct). They therefore judged a version from before the blackbox-log retune. The current feel may differ from what they flew.
- The download pattern (about 4.5K for 0.3.2, 4.4K for 0.4.0, 3.7K for 0.5.2, but about 190 for 0.5.0 and 0.5.1) suggests most users stay on the version current when they arrive. That matters, because servers require identical versions.
- "26.3 only" is probably tied to 26.3 replacing GLFW with SDL3 for input (see Q5).
  - Propwash's input module says "Funke/Gamepad (SDL3 bzw. GLFW, je nach 26.3-Stand)" (radio/gamepad via SDL3 or GLFW, depending on the 26.3 build). — [ARCHITECTURE.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/ARCHITECTURE.md)
  - The developer never states this as the reason.
- The Impressum/Datenschutz pages and the German docs point to a developer based in Germany. I did not open the Impressum, to avoid collecting personal data.

### Gaps
- Release dates of 0.1.0–0.3.1 are unknown. They are not on CurseForge, and the changelog has no dates.
- Why Propwash is missing from Modrinth (in review, private or removed) is unknown.
- Discord devlogs and announcements could not be read, because they need a login.

## 2. What it claims to model, and how its physics runs inside Minecraft

### Takeaway
**Developer claim:** a full sim-grade model, covering:
- a rigid body with motor, ESC and battery physics;
- rotor aerodynamics, ground effect, prop wash, voltage sag, wind and gusts;
- a Betaflight-style flight controller (Betaflight/Actual rates, PID+FF, TPA, airmode, Acro/Angle/Horizon);
- part-derived performance across 65 mm whoop to 7″.

**How it is implemented, from the public spec and source docs:**
- A pure-Java flight model steps at a **fixed 2,000 Hz on the pilot's own client**, independent of Minecraft's 20 Hz tick. The flight controller runs at 2k/1k/500 Hz, with a one-sample loop delay like real hardware.
- In multiplayer the client sends its state and the **server only checks plausibility** and relays it.
- The developer measured about 0.3 ms from the game's input poll to the simulation, and about 30 ms total from stick to picture with an HD video module, at about 120 fps. The USB/OS polling of the radio and the monitor's own lag are not included.

**Developer self-test:** a comparison with **19 public Betaflight blackbox logs**. Rates and 5″/7″ behaviour match well. For 2–3″ cinewhoop props, thrust and RPM were off by large factors. All of this is the developer's own measurement, not independent proof.

### Cited Findings
**Claims (developer marketing and docs)**
- "Real flight model: rigid body with motor, ESC and battery physics, rotor aerodynamics, ground effect, prop wash, voltage sag, wind and gusts. Every drone is derived from its parts: weight, thrust, hover throttle, top speed and flight time follow from the build." — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- "Betaflight-style flight controller: Betaflight and Actual rates, PID with feed-forward, I-term relax, anti-gravity, TPA, airmode, Acro/Angle/Horizon, 3D mode with reversible motors, arming checks, failsafe, flip-upright after a crash and GPS Rescue… The tune is stored on the drone, like on a real flight controller." — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- **Parts:** "five frames from a 65 mm whoop to a 7″ long range, flight controllers, six motors, six props, batteries and video units." — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
  - Minor conflict: CurseForge's description, via fetch summary, says "Five frame sizes, six motor types, five props". It may predate the 5129 race prop added in 0.5.2. — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv)
  - Add-ons can add frames "X-Class up to 13″" and batteries "up to 12S". — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- **Drone Editor (creative only)** exposes "masses, inertia, motor positions, props with thrust and power coefficients, motors, battery, ESC, drag and camera". — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- "Not an official Minecraft product, and not affiliated with Betaflight, EdgeTX, OpenTX, or drone manufacturers" (fetch summary). — [propwashfpv.com](https://propwashfpv.com/)

**Physics rate and loop (developer spec, German; my translation, with Korean glosses)**
- "**Takt:** Physik fest 2000 Hz (h = 0,5 ms), FC in jedem Substep (einstellbar 2k/1k/500 Hz). Frame-dt 0–50 ms wird über einen Nanosekunden-Akkumulator in Substeps zerlegt (max. 100), Sticks werden innerhalb des Frames linear interpoliert. Gleiche Gesamtzeit ergibt unabhängig von der Frame-Aufteilung denselben Zustand."
  - English: physics is fixed at 2,000 Hz (0.5 ms steps). The FC runs every substep (2k/1k/500 Hz selectable). Each frame's 0–50 ms is split into at most 100 substeps, and sticks are interpolated linearly within the frame. The same total time gives the same state however it is split into frames.
  - Korean: 물리 2000 Hz 고정, 비행제어기 2k/1k/500 Hz, 프레임 시간을 0.5 ms 단위로 쪼개 계산.
  - [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
- **Reason given for 2 kHz:** "D-Term und 1-Sample-Latenz wie echter 2k-Loop; Kosten bei 50-ms-Frames < 0,2 ms" (D-term and one-sample latency like a real 2k loop; costs under 0.2 ms even with 50 ms frames). Also "≈ 1,5 µs pro Substep" (about 1.5 µs per substep). — [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
- **One-sample delay:** "Das berechnete `dutyNext` wirkt ab dem **nächsten** Substep (1 Sample Latenz wie ein echter Loop)". The motor command takes effect from the next substep, a one-sample latency like a real loop. — [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
- **Threading:** "Einfädig (Render-Thread des Piloten)". The sim is single-threaded on the pilot's render thread. — [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
- **Origin of the model:** "nur öffentliche Physik (Impulstheorie, DC-Motormodell, Starrkörpermechanik, Impulsverfahren, Bodeneffektmodell nach Sanchez-Cuevas et al.) und die öffentlich dokumentierten Betaflight-Konzepte… Kein Code, keine Konstanten und keine Strukturen aus anderen FPV-Mods."
  - English: only public physics (momentum theory, a DC motor model, rigid-body mechanics, impulse methods, the Sanchez-Cuevas ground-effect model) and publicly documented Betaflight concepts, with no code, constants or structures taken from other FPV mods.
  - [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
- **How the effects are modelled** (spec §0, §5) — [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
  - **Motors and battery:** a DC motor model per motor, with implicit RPM integration. "Akku ↔ 4 ESC geschlossen gelöst (sonst instabil)": the battery and four ESCs are solved together in closed form, because the explicit coupling is unstable.
  - **Ground effect:** "Bodeneffekt pro Rotor" (Sanchez-Cuevas). For the freestyle quad, f_ge = 1.114 at half a prop diameter above ground.
  - **Prop wash:** a "Wirbelring pro Rotor" (vortex ring per rotor), computed from the previous substep's thrust, descent ratio and crossflow, plus band-limited noise per rotor. "Die ungleichen Schübe erzeugen über die Hebelarme Roll-/Nick-/Gierstörungen, die der PID sichtbar ausregelt; nichts davon ist gescriptet." The uneven thrusts create roll, pitch and yaw disturbances that the PID visibly corrects; nothing is scripted. A wake field of 32 packets updates at 250 Hz.
  - **Gusts:** "Alle 8 Substeps (250 Hz), je Weltachse PT1-gefiltertes Rauschen, Zeitkonstante 1,2 s". Every 8 substeps (250 Hz), PT1-filtered noise per world axis with a 1.2 s time constant. Gusts need wind and turbulence switched on.
  - **Default PIDs** are derived per build in closed form, for example "FREESTYLE: Roll P42 I49 D31 F120".
  - **Collision simplification:** "Entity bewegt sich mit MC-Blockkollision (feste AABB)". The drone uses Minecraft's block collision with a fixed axis-aligned box. The sim then adds impulse, tumbling and crash classification.
- **Client-side flight, server checks** (ARCHITECTURE "Datenfluss beim Fliegen") — [ARCHITECTURE.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/ARCHITECTURE.md)
  - Step 2: "Client: `PilotSession` liest pro Frame die Funke, steppt `sim` mit Frame-dt (intern fester Takt), bewegt die Drohnen-Entity mit Blockkollision". The client reads the radio every frame, steps the sim with the frame time at a fixed internal rate, and moves the drone entity with block collision.
  - Step 3: "Client sendet Zustand (Position, Orientierung, armed, Motorleistung, Akku) an den Server; der Server prüft Plausibilität… und verteilt an andere Spieler." The client sends position, orientation, armed state, motor power and battery to the server, which checks plausibility and relays it to other players.
- **Server role:** "server-side validation of pilot movement" and "the server streams chunks around the drone". — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
  - Pilotless GPS Rescue: "fliegt der Server die Drohne mit demselben Flugmodell weiter". The server keeps flying the drone with the same flight model. — [ARCHITECTURE.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/ARCHITECTURE.md)
- **Multiplayer limits:** "Other players see the sticks of your in-game radio in the center position"; "Spectators see the pilot's OSD approximately"; "One pilot per drone"; "Outside creative, the radio link reaches about 1,200 blocks; servers can limit it further." — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)

**Input and display latency (developer's measured chain)** — [fpv-feel.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/fpv-feel.md)
- **Order of each frame:**
  1. Sticks are read via SDL3 at the start of the main loop.
  2. Minecraft's client tick runs "nur in Bildern mit fälligem Tick, 20 Hz" (only in frames where a 20 Hz tick is due).
  3. The sim then advances "in festen 2000-Hz-Substeps, Knüppel linear über die Substeps des Bilds" (in fixed 2,000 Hz substeps, sticks spread linearly over the frame's substeps).
- **RC smoothing:** a "PT2 40 Hz wie Betaflights Setpoint-Glättung, Gruppenlaufzeit ≈ 5 ms". This adds about 5 ms of group delay, like Betaflight's setpoint smoothing.
- **Video latency is modelled as the real system's glass-to-glass figure:** "analog 12 ms, digital Lite 26 ms, digital HD 30 ms".
  - Since 0.5.0 the mod subtracts its measured render pipeline and half the monitor scan-out, so the delay is not counted twice.
  - "Nicht abgezogen wird, was das Spiel nicht messen kann (GPU-Arbeit nach `present`, Compositor des Betriebssystems, Eingangsverzögerung des Monitors)." Not subtracted is what the game cannot measure: GPU work after present, the OS compositor and monitor input lag.
- **Measured** on a Mac with a 120 Hz display at about 120 fps, freestyle quad with the HD module:
  - Input (pollEvents → sim): **0.27 ms mean, 1.57 ms max**.
  - Total chain: **41.4–42.2 ms before** the 0.5.0 fix and **29.1–30.0 ms after**.
- **Developer admits the floaty complaint:** "Viele Spieler beschreiben die Drohnen als „zu floaty". Dieses Dokument behandelt alles, was das Gefühl formt, ohne das Flugmodell anzufassen…"
  - English: many players describe the drones as "too floaty"; this document covers everything that shapes feel without touching the flight model.
  - Korean: 많은 플레이어가 드론이 "너무 둥둥 뜬다"고 말한다.
  - [fpv-feel.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/fpv-feel.md)

**Validation against real flight logs (developer self-test, dated 08.10.2026)**
- **Method:** "Es liest echte Betaflight-Blackbox-Logs (`.bbl`, `.bfl`)". The tool reads real Betaflight blackbox logs. — [blackbox-calibration.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/tools/blackbox-calibration.md)
  - The logs are public, gathered from issues and pull requests of `betaflight/betaflight`, `blackbox-log-viewer`, `bluejay`, PIDtoolbox and others: "rund 880 Anhänge, 994 Logs" (about 880 attachments, 994 logs).
  - Adopted logs include BetaFPV Meteor75 and Meteor75 Pro, BetaFPV Pavo Pico and Pavo20 Pro II, Flywoo Firefly 25, a GEPRC 3″ cinewhoop, iFlight Nazgul Evoque F5 V2, a 5″ LR Li-ion build, a REKON-7 and a MicoAir 7″.
  - Weights are rated "hoch/mittel/niedrig" (high/medium/low confidence); "niedrig" means estimated from typical builds.
- **Release notes:** "Der Abgleich mit 19 echten Betaflight-Logs (Whoop bis 7″) zeigte, dass die Sim beim Steigen für alle Größen zu viel Schub verliert (echt/Sim 1,03–1,36 bei 1,5–3,5 m/s)… 5″ jetzt 0,97–1,00."
  - English: comparison with 19 real logs showed the sim lost too much thrust in climbs at every size. After a momentum and blade-element fix, the 5″ matches at 0.97–1.00. — [RELEASE-NOTES.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/RELEASE-NOTES.md)
- **Results table (median, real/sim; 1.0 = match; above 1 = the sim has less thrust)** — [blackbox-calibration.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/tools/blackbox-calibration.md)

  | Size | Thrust real/sim | Other figures |
  |---|---|---|
  | Whoop 75 mm 1S | 0.94 | punch 2.24 g real vs 2.66 g sim |
  | 2″ cinewhoop | 1.42 | RPM real/sim 0.66 |
  | 2.5″ 3S | 2.10 | hover duty 30.5 % real vs 45.7 % sim |
  | 3″ cinewhoop (estimated build only) | 2.34 | — |
  | 5″ 6S | 1.16 | climb 0.97 / 1.00 |
  | 7″ LR (estimated builds only) | 1.02 | — |

- **Developer's own conclusions** — [blackbox-calibration.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/tools/blackbox-calibration.md)
  - "**Props 45–76 mm zu schwach – Teiledaten, nicht in 0.5.0.**" (45–76 mm props too weak; a parts-data issue, not fixed in 0.5.0.)
  - "Die Sim dreht beim Schweben 30–85 % höher als echt" (the sim hovers at 30–85 % higher RPM than real).
  - "Ab 56 mm braucht sie 27–55 % mehr Duty" (from 56 mm, it needs 27–55 % more duty).
  - Whoop 75 mm: "Punch 19 % zu stark" (punch 19 % too strong).
  - **Rates:** "folgt der echte Sollwert der ACTUAL-Kurve von Propwash auf 0,3–0,7 °/s (Median, sechs Logs)". The real setpoint follows Propwash's ACTUAL rate curve within 0.3–0.7 °/s (median, six logs).
  - **Limits:**
    - "Gewichte sind bei den meisten Logs geschätzt" (weights are estimated for most logs).
    - "Die Sim hält die Lage ideal; Manöver mit Flips werden verworfen" (the sim holds attitude ideally; manoeuvres with flips are discarded).
    - "ESC-Eigenheiten (Bluejay/AM32-Kurven, Startleistung) sind nicht im Modell" (ESC quirks such as Bluejay/AM32 curves and start-up power are not modelled).
- **0.5.0 whoop retune:** fall after 1 s "5,98 (0.4.0) → 7,30 m/s", top speed "36 → 48 km/h (Werkbank; im Flug gemessen 47,2 km/h)". The "less floaty" check was run against "ein Referenzmodell aus Prüfstand, Windkanal-Daten zum Wirbelring…" (a reference model from test-stand and wind-tunnel data on the vortex ring). — [RELEASE-NOTES.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/RELEASE-NOTES.md)
- **Motor response in the model:** "Whoop hoch 64 ms / runter 45 ms, 5″ 33 / 16 ms" (whoop 64 ms up / 45 ms down; 5″ 33 / 16 ms). For the 2.5″, motor slow-down to 63 % takes 21 ms real versus 34 ms in the sim. — [blackbox-calibration.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/tools/blackbox-calibration.md)
- **Unnamed playtesters cited by the developer:**
  - "Zwei Rückmeldungen eines erfahrenen FPV-Piloten aus dem Spieltest der 0.5.0" (two pieces of feedback from an experienced FPV pilot in the 0.5.0 playtest). Both were about UI.
  - "Rückmeldung eines Rennpiloten" (a race pilot's feedback): "5″-Racer fliegen heute True-X…, flache Props wie der „5129"". This led to the true-X race frame and the 5129 prop.
  - "Rückmeldung eines Creators, der Piloten coacht" (a creator who coaches pilots), about new-school tricks.
  - [RELEASE-NOTES.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/RELEASE-NOTES.md)

### Inferences
- On paper the design is far closer to a dedicated simulator than to a typical Minecraft "flying camera":
  - physics decoupled from the 20 TPS game tick and run at a 2 kHz flight-controller rate;
  - Betaflight-structured rate formulas that match real logs to within a degree per second;
  - part-derived inertia and thrust.
- Stick-to-rotation mapping is the main thing acro muscle memory transfers through, so it is plausibly faithful.
- Absolute thrust, RPM and hover throttle were still off by large margins for 2–3″ cinewhoops, by the developer's own table (as of 08.10). Whether 0.5.1 or 0.5.2 fixed this is not stated.
- Because the sim runs on the pilot's client, your own drone should feel the same in single-player and on a server. Other pilots' drones arrive through the server relay. This is inferred from the data flow; remote smoothing was not checked.
- The sim advances only in rendered frames, and frame time is capped at 50 ms. Below about 20 fps the simulated time would run slower than real time, and low frame rates sample the sticks less often.
  - This is my inference from `MAX_FRAME_DT = 0.05` and per-frame input. The developer's figures were measured at about 120 fps on an Apple-silicon Mac.
- Remaining realism limits come from Minecraft itself: blocky geometry, a fixed collision box, and chunk streaming. The developer's own "Realistic / Training / Arcade" switches also mean "realism" depends on settings.

### Gaps
- No independent measurement exists of Propwash's flight model, latency or log agreement. Every number above comes from the developer.
- I could not see whether the small-prop thrust deficit was fixed in 0.5.1/0.5.2. Neither changelog mentions it.
- How remote drones are smoothed or interpolated for other players was not examined.
- Discord devlogs were not accessible.

## 3. What identifiable FPV pilots and players say about the feel (and affiliations)

### Takeaway
Named praise comes only from **short-form FPV creators**, and none of them published a measured comparison against real quads or dedicated sims:
- SubTwoFifty: tier A, "right up there with the zone". The earlier notes cover him.
- Dronarchy: "Top Minecraft FPV Mod?", "Super detailed and configurable options…".

Dronarchy's spoken verdict could not be accessed. The 70 CurseForge comments that I could read (the seven newest threads) are enthusiastic, but they are about fun, bugs and version ports, not realism. No Reddit discussion was found.

The developer's own docs concede that "many players" found the drones "too floaty" before 0.5.0. I found no disclosed sponsorship, but Dronarchy's caption gives a "Shoutout to the creator".

### Cited Findings
- **Dronarchy's YouTube video.** oEmbed confirms the title "Top Minecraft FPV Mod? Propwash", channel "Dronarchy" (@dronarchy). — [YouTube oEmbed](https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=qQVbF787iRo&format=json)
  - Date (3 Oct 2026) and the description line "On this video you will se the best FPV mod for Minecraft" come from earlier notes. — [YouTube qQVbF787iRo](https://www.youtube.com/watch?v=qQVbF787iRo)
  - The watch page returned only site chrome to the fetch tool, and yt-dlp was refused with "Sign in to confirm you're not a bot". No transcript, likes or comments were obtainable.
- **Dronarchy's TikToks (search-snippet captions only, not opened):**
  - Video 7691688088283647263: "💎 New Minecraft FPV Mod (PropwashFPV). Super detailed and configurable options for an immersive drone experience. Stay tunned for a fun tutorial. Shoutout to the creator: @Propwash FPV #minecraft #game #gamers #drone #dronarchy" — [TikTok](https://www.tiktok.com/@dronarchy/video/7691688088283647263)
  - Video 7691887226451496222: "Top FPV Drone Mod for Minecraft — Propwash FPV Overview". The search summary adds that it says the mod has "tons of customizable options, and plenty of configurations to play with". — [TikTok](https://www.tiktok.com/@dronarchy/video/7691887226451496222)
  - Posting times decoded from the TikTok IDs (top 32 bits = Unix time): 2026-10-01 13:18 UTC and 2026-10-02 02:10 UTC.
  - Method check: the same decoding gives 20:39:49 UTC for SubTwoFifty's Part 9, against the 20:39:58 UTC recorded in earlier notes. — [TikTok Part 9](https://www.tiktok.com/@subtwofifty/video/7691059739349830934)
- **Dronarchy praises Bodycam in similar words (search snippet):** "👑 Bodycam FPV Maxxing. The physics feel and perform really good while flying the drone mod… Insame graphics and realism." — [TikTok](https://www.tiktok.com/@dronarchy/video/7683146943647730974)
- **Correction to a search summary.** The YouTube video "Propwash FPV mod for Minecraft" (Yqvp9ykZiXU) belongs to the **developer's own channel "PropwashFPV"**, not to Dronarchy. It is marketing, not a review. — [YouTube oEmbed](https://www.youtube.com/oembed?url=https://www.youtube.com/watch?v=Yqvp9ykZiXU&format=json)
- **Unverified.** A search summary described "a reviewer clip" scoring the mod "9/10, with physics at 9/10 and beginner accessibility at 6/10", with unclear attribution. A follow-up search found no source, so treat it as unverified.
- **CurseForge comments.** These are the seven most recent threads, 2026-10-08 to 2026-10-26. The API returned only the newest page of 70 comments. — [CurseForge comments (site API)](https://www.curseforge.com/api/v1/mods/1711041/comments?pageIndex=0&pageSize=50)
  - "THIS is so peak, i had to make an account, i was playing on outdated bad fpv minecraft mods in like 1.16.x This is insane, how long did it take to make?" (user_k13xh9b11c42pciw, 2026-10-20)
  - "i cant arm the drone back on again it i disarm it mid air…" (same user, 2026-10-24). Developer: "you can set the arm angle to 180° then it is possible" (2026-10-25).
  - "Hey, the mod is great, i saw a clip of it on instagram and i made an account just to comment." (Rotrival, 2026-10-11)
  - "every time i put on the goggles i get a very zoomed in picture that dosnt update as i fly" (user_h2wtrfxk3tyiqu92, 2026-10-23). A second user replies "same". The developer asks for a Discord bug ticket.
  - "Is there any toggle for 3d mode instead of acro?" (2026-10-08). Developer: "3d mode drops with the next release".
  - Several requests for 1.20.1, 1.21.1 or Forge, answered as in Q1.
  - None of these comments compares the feel with real quads or other sims.
- **Developer documents player criticism:** "Viele Spieler beschreiben die Drohnen als „zu floaty"" (many players describe the drones as "too floaty"). — [fpv-feel.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/fpv-feel.md)
  - 0.4.0 added a gravity slider "for pilots who find the drones a little floaty". — [CHANGELOG.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/CHANGELOG.md)
- **Reddit.** A search engine query for Propwash on Reddit returned no Reddit threads. Reddit's own search endpoint returned HTTP 403 on 2026-11-12. — [Reddit search](https://www.reddit.com/search.json?q=propwash%20minecraft&sort=new&limit=25)

### Inferences
- **SubTwoFifty in context.** His "right up there with the zone" line (Reel 4, from earlier notes) most plausibly means the dedicated sim **The Zone**. His 2026-11-10 ranking places it in the same A tier as Propwash, below his S tier (TRYP FPV, Liftoff, Uncrashed). — [Ranking reel](https://www.instagram.com/reel/Dfkss5XqOJt/); [Reel 4](https://www.instagram.com/reel/Dd4og-ro2it/)
  - So even Propwash's most prominent fan does not rank it with the most realistic dedicated sims.
- **Dronarchy is a real-radio FPV hobbyist** (earlier notes show him flying with a TX16S). His captions are promotional in tone ("Shoutout to the creator", "Stay tunned for a fun tutorial"), and he uses the same "physics feel… really good" praise for Bodycam.
  - Treat his verdict as enthusiasm, not a calibrated realism rating.
  - I found no evidence of payment or sponsorship, but no disclosure either way.
- Both creators reviewed **0.3.2**, the only build available on 29 Sep–3 Oct (see Q1), before the 0.5.0 "less floaty" retune. Their impressions describe an older flight model.
- **Bottom line for the report's question.** Minecraft now has one mod whose design and documentation are those of a serious FPV sim, which was not true before this autumn. But "very close to real FPV" is only:
  - asserted by the developer and his self-measurements;
  - echoed by two enthusiastic short-form creators who reviewed an early build and rank it below the top dedicated sims;
  - not confirmed by any independent long-form pilot test or community consensus I could find.

### Gaps
- Dronarchy's spoken verdict and the YouTube comments (YouTube blocked).
- Instagram comments on Reel 4 (484, unread).
- Older CurseForge comments (25 Sep–8 Oct), because API paging did not advance.
- Discord, r/fpv, r/feedthebeast and r/Minecraft could not be read. I found no long-form review by an established FPV reviewer; the earlier notes found the same.

## 4. Other Minecraft drone mods and add-ons, and how they compare

### Takeaway
There are many drone mods, mostly for Minecraft 1.20.1/1.21.1 and mostly military-themed. Only a handful claim **acro flight with a real radio**:
- **FPVCraft:** 1.21.1, Fabric/NeoForge, 0.3.0 beta, Nov 2026.
- **AcroFPV:** 26.2, Fabric, 142 downloads.
- **"FPV Drones: Acro & Racing":** details from a search snippet only.
- **Quadz:** the 2021 Fabric 1.16.5 predecessor.

Military packs (Shaded War, the SBW add-ons, jaaager's "FPV Drones") advertise "real acro flight physics" or "realistic" flight, but focus on combat and mouse/keyboard play. Create: Droneworks is redstone-driven aircraft building. No competitor publishes a physics spec comparable to Propwash's, and I found no independent realism review of any of them. For Bedrock, I found no FPV/acro add-on.

### Cited Findings
- **FPVCraft** (CurseForge; author tweedlex; 1.21.1, NeoForge and Fabric; FPVCraft 0.3.0 files dated Nov 7, 2026; 2,411 downloads). Fetch-tool summary with short verbatim fragments. — [CurseForge FPVCraft](https://www.curseforge.com/minecraft/mc-mods/fpvcraft)
  - Says the drone "is not a flying camera with a drone skin".
  - Radios: EdgeTX/OpenTX over USB as a joystick (HID).
  - Modes: Angle, with Acro on a key. Rate presets include Freestyle at Betaflight defaults "70 / 670 / 0.54".
  - Simulates a 5″ freestyle quad (650 g, thrust-to-weight 6, about 120 km/h) with motor lag, drag, prop wash and 6S sag.
  - No keyboard flying ("a quad simply cannot be flown well with on/off keys").
  - Range limited to render distance, up to 200 blocks. Server checks flight data. Early beta.
  - Its own FAQ recommends a dedicated simulator for serious training.
- **AcroFPV** (Modrinth "acro-fpv"; Redboiguy; Fabric 26.2; v1.9.1, 2026-08-18; 142 downloads). — [Modrinth API: acro-fpv](https://api.modrinth.com/v2/project/acro-fpv)
  - "Real flight physics: 6DOF rigid-body sim with thrust, drag, gravity and momentum."
  - "Fly it on your radio: plug in an EdgeTX/OpenTX transmitter over USB."
  - "Betaflight-style tuning: Rate model, expo, centre sensitivity."
  - "Acro, Angle & Horizon flying modes."
- **FPV Drones: Acro & Racing** (ModpackIndex #233359; author Restor_0o0). Search summary only; the page returned 403. Build a drone from parts and fly "full acro mode" with an RC radio or mouse and keyboard, plus gates, strike missions and guardian/scout/trader drones. Version and loader unknown. — [ModpackIndex](https://www.modpackindex.com/mod/233359/fpv-drones-acro-racing)
- **Quadz** (LazuriteMC; Fabric 1.16.5; v1.0.1, 2021-05-24; 4,363 Modrinth downloads). Uses "Rayon, a rigid body simulation library for minecraft" and "Lattice which allows chunks to be loaded around the player's camera". — [Modrinth API: quadz](https://api.modrinth.com/v2/project/quadz)
  - The CurseForge commenter's "outdated bad fpv minecraft mods in like 1.16.x" fits this era (my inference).
- **FPV Drones** (Modrinth "fpvdrones"; team of "the developers of MCSP and Immersive vehicles"; Forge 1.20.1; v1.1.8, 2026-08-14; 11,037 downloads). — [Modrinth API: fpvdrones](https://api.modrinth.com/v2/project/fpvdrones)
  - Claims "battery voltage simulation", "realistic movement & flight", "joystick support… even mouse & keyboard", "an immersive flying expereicne that closley mirrors real life drone piloting instead of arcadey and unrealistic controls".
  - The changelog also lists military drones (Orlan-10, Lancet) and explosive payloads.
- **Shaded War / FPV / SHAHED** (fullfud; Forge 1.20.1; 3.0.0-BETA.629, 2026-10-28; 38,136 downloads; source on GitHub). — [Modrinth API: shaded-war](https://api.modrinth.com/v2/project/shaded-war)
  - "FPV drones with real acro flight physics", 7″, Tiny Whoop and interceptor drones.
  - An "FPV Configurator: tune rates and flight physics in game". A Betaflight-style OSD on the interceptor.
  - Default controls: "FPV is flown mainly with the mouse"; Space = throttle.
  - Main theme: Shaheds, missiles and jammers.
- **Other military packs.** [SBW] Drone Warfare (111,550 downloads; Forge/NeoForge 1.20.1/1.21.1, "tactical FPV drones, LUCAS UAVs, fiber links"), [SBW] Skyfront, [SBW] Electronic Warfare, Uncomplicated FPV and MH Warfare are all combat add-ons. — [Modrinth API search "fpv drone"](https://api.modrinth.com/v2/search?query=fpv%20drone&limit=20)
- **Create: Droneworks Simulated** (LowTierChud; NeoForge 1.21.1; v0.1.1, 2026-07-09; 16,607 downloads). "Droneworks is an add-on for Aeronautics that lets you build aircraft from redstone-controlled parts"; "Propellers actually push, torque has to be balanced"; a "Drone Camera" gives an FPV feed with "stabilised and high-sensitivity modes". No radio or acro claim. — [Modrinth API: create-droneworks-simulated](https://api.modrinth.com/v2/project/create-droneworks-simulated)
- **Arcade-style mods:**
  - "FPV Drone" (getulain1; Fabric 1.20.1; 2026-02-24): past 150 blocks "the drone will hover in place"; a battery gives "exactly 2 minutes". — [Modrinth API: fpv-drone](https://api.modrinth.com/v2/project/fpv-drone)
  - "FPV Drones" (marden14111; Fabric 1.20.1; 2026-07-29): "realistic WASD and mouse controls" with an explosion on impact. — [Modrinth API: fpv-drones](https://api.modrinth.com/v2/project/fpv-drones)
  - "Fpv Elytra" (2024): "make the elytra feel like an fpv drone". — [Modrinth API search](https://api.modrinth.com/v2/search?query=fpv%20drone&limit=20)
- **MC-Drone** (Westmoon05; a Fabric 1.21.6 modpack, 2025-12-14): "an FPV simulator modpack… in-game flight instructions… Inspired by Ro-Drone"; "Better With Controller (Tested With PS5 Dualsence)". — [Modrinth API: mc-drone](https://api.modrinth.com/v2/project/mc-drone)
- **"Minecraft FPV"** (CurseForge slug fpv-drone). Search summary only: "supports multiplayer and has racing leaderboards on its server". Not opened. — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/fpv-drone)
- **Bedrock (search summaries only):**
  - No FPV/acro add-on was found on the Marketplace.
  - Marketplace worlds "Working Drones" (Dodo Studios) and "Drones" (Cubed Creations) cost 830 Minecoins.
  - The CurseForge Bedrock add-on "Drone v2.7, TNT drones" offers camera drones with a controller.
  - None claims acro or radio support.
  - [chunk.gg Working Drones](https://chunk.gg/@dodo-studios/working-drones); [minecraftpal Drones](https://www.minecraftpal.com/marketplace/item/8b1562b2-a791-47ce-9ab0-ec811d1211b5/drones); [CurseForge Bedrock Drone](https://www.curseforge.com/minecraft-bedrock/addons/drone)

### Inferences
- Propwash is the only Minecraft drone mod I found that documents its physics loop, validates it against real logs, and has a wide part catalogue. No other Minecraft mod appears anywhere in SubTwoFifty's 24-program list (from earlier notes), so his A rating is not a head-to-head win over other Minecraft mods.
- FPVCraft is the nearest like-for-like rival: radio-only acro with Betaflight rates and sag. Its own FAQ advises a dedicated sim for serious training, which matches the hobby consensus in earlier notes.
- The military packs have much higher download counts (SBW Drone Warfare about 111K) than any realism-focused mod. Minecraft's drone audience is mostly about combat play, not pilot training.

### Gaps
- Valkyrien Skies drone builds were not checked.
- The version and loader of "FPV Drones: Acro & Racing" are unknown (page 403).
- Radio support in Shaded War and the SBW packs was not verified.
- I found no independent realism reviews of any competitor.
- CurseForge's site-API search returned non-JSON, so CurseForge-only mods may be missing from this list.

## 5. Practical setup for a beginner with a real radio

### Takeaway
You need **Minecraft: Java Edition**, because Fabric and NeoForge are Java loaders. It must be exactly **version 26.3**, running on **Java 25**, with Fabric Loader 0.19.5+ and Fabric API 0.161.0+26.3, or NeoForge 26.3.0.10-beta+.

- **Cost.** The mod is a free download from CurseForge, with Ko-fi donations optional. The Java & Bedrock PC bundle is reported at about **US$29.99**; I could not confirm this on the official page.
- **Radio connection.** An EdgeTX or OpenTX radio connects by USB in **"USB Joystick (HID)"** mode. It is detected automatically with AETR channels and AUX defaults, then set up in a wizard. Gamepads and mouse/keyboard also work.
- **Official sources.** The CurseForge page and the GitHub source. Support is on Discord. The Modrinth link on the site is not live.

### Cited Findings
- **Requirements**, verbatim: Minecraft 26.3; "Fabric Loader 0.19.5+ and Fabric API 0.161.0+26.3"; "NeoForge 26.3.0.10-beta or newer"; Java 25; "Required on both client and server." — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- **Radio setup**, verbatim. — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
  - "EdgeTX/OpenTX radios: connect the radio via USB and choose **USB Joystick (HID)** on the radio. Propwash detects it automatically and starts with AETR channel order, AUX1 = arm, AUX2 = flight mode (low Acro, middle Horizon, high Angle), AUX3 = beeper, AUX4 = rescue and full-travel throttle."
  - Limitation: "A radio has to run in USB joystick (HID) mode; the mod does not talk to receivers or radio protocols directly."
  - The site adds that charging or USB storage mode is not enough (fetch summary). — [propwashfpv.com](https://propwashfpv.com/)
- **Receiver wizard and switches** (Configurator key `K` → Receiver). — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
  - The wizard steps through stick mode, device, channels, a live check page with "Inv.", calibration and switch assignment.
  - "Stick mode (Mode 1–4)… Mode 2 (throttle and yaw left, pitch and roll right) is the default."
  - "Max arm angle… like Betaflight's small_angle, 25° by default."
  - On macOS, radios "such as the Radiomaster Pocket show up".
- **Other input devices:** "Gamepads are detected automatically"; "Keyboard flight starts in Angle mode"; "Mouse + keyboard… the mouse steers pitch and roll like aiming in a shooter". — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- **Binding and arming:**
  - Since 0.5.0: "Binding made simple: click the drone with your remote and it remembers you… Goggles are no longer bound: wear ones that match the drone's video system and you fly FPV, take them off and you fly line of sight." — [CHANGELOG.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/CHANGELOG.md)
  - CurseForge describes arming as right-clicking into the air with the radio in hand (fetch summary). — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv)
- **Beginner aids** — [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md); [CHANGELOG.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/CHANGELOG.md)
  - Creative mode has "five ready-to-fly drones (Whoop, Cinewhoop, Freestyle, Racer, …)".
  - "Flight training: 20 hands-on lessons in five chapters – from hovering to gates, flips and a final exam."
  - World-rule presets "Realistic, Training or Arcade". Laps flown "with altitude or position hold, GPS Rescue or modified physics" are counted as assisted.
  - "Good first steps: build the Drone Workbench and the Battery Charger, then a whoop with a radio and analog goggles."
- **Optional extras and caveats:**
  - "With an active shader pack (Iris/Oculus)… the video effect falls back to a simpler overlay."
  - Flashback (Fabric only) for replays. LambDynamicLights optional.
  - Recording with the GPU encoder needs the free program ffmpeg.
  - [README](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/README.md)
- **PC requirements.** None are published by the mod; the README and site list only software versions.
  - The developer quotes "≈ 1,5 µs pro Substep" for the flight model. — [flight-model-spec.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/design/flight-model-spec.md)
  - He reports a recording self-test on an "Apple M4 Pro, 1080p60… Spiel bei 118 FPS" (game at 118 FPS). — [RELEASE-NOTES.md](https://raw.githubusercontent.com/LardTom/propwash-fpv/HEAD/docs/RELEASE-NOTES.md)
- **Minecraft 26.3 itself:** "Minecraft now uses SDL3 instead of GLFW for window management, input, and platform integration" (GamingOnLinux, 17 Sep 2026). — [GamingOnLinux](https://www.gamingonlinux.com/2026/09/minecraft-java-edition-26-3-wilderness-bound-update-released/page=1/)
- **Price (secondary sources only).** About $29.99 for "Minecraft: Java & Bedrock Edition for PC" and $39.99 for Deluxe, from retailer and listing snippets. minecraft.net's store page returned HTTP 503 to my fetch. — [TrueAchievements](https://www.trueachievements.com/products/85542/Minecraft-Java-and-Bedrock-Edition-for-PC); [Walmart](https://www.walmart.com/ip/Minecraft-Java-and-Bedrock-Edition-Microsoft-PC/980394609)
- **Is it free?** No price or paywall appears on CurseForge or the site; the files download from CurseForge. The license is the source-available PolyForm Shield, and there is a "Donation: ko-fi.com/propwashfpv" link. — [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv)
- **Official sources:**
  - Files: the CurseForge project (ID 1711041). Source: github.com/LardTom/propwash-fpv. Docs: propwashfpv.com/docs. Support: Discord (discord.gg/bNhkSXYSgZ). — [propwashfpv.com](https://propwashfpv.com/); [CurseForge](https://www.curseforge.com/minecraft/mc-mods/propwash-fpv)
  - Third-party mirrors such as moddex.gg list it (search result only). — [moddex](https://moddex.gg/mod/propwash-fpv)

### Inferences
- **A beginner's realistic path:**
  1. Buy Java Edition.
  2. Install a Minecraft **26.3** profile with Fabric or NeoForge and Java 25. The CurseForge app can do this.
  3. Add Propwash 0.5.2 (plus Fabric API on Fabric).
  4. Set the radio's USB mode to Joystick (HID) and run the receiver wizard.
  5. Start in creative with a preset whoop and the Flight training lessons.
  6. Switch world rules to "Realistic" when practising for real flying.
- Avoid newer Minecraft versions until Propwash supports them, and match the mod version exactly on servers.
- The radio requirement is identical to dedicated sims: USB HID joystick from EdgeTX or OpenTX. A beginner's radio bought for sims works here too.
- The only extra cost over a sim is the Minecraft licence, about US$30. For comparison, a DCInside user quoted in earlier notes put typical FPV sims at ₩20–30K; that is an anonymous user's figure, not a checked price. The mod itself is free.

### Gaps
- The official KRW or USD price was not confirmed on minecraft.net (503).
- No minimum PC specification is published.
- Support for DJI controllers or other non-EdgeTX devices was not verified. SubTwoFifty's desk showed a "dji"-logo controller (earlier notes), but which device he used is unknown.
- Whether ExpressLRS-only radios need special settings beyond HID was not checked.

## 6. Has vanilla Minecraft added a drone in 2025–2026?

### Takeaway
**No.** None of the 2026 drops add a drone:
- **26.1 "Tiny Takeover"** (24 Mar 2026): baby-mob redesigns.
- **26.2 "Chaos Cubed"** (mid-2026): adds the Sulfur Cube.
- **26.3 "Wilderness Bound"** (Sep 2026): no new mobs; the SDL3 input switch.

Minecraft Live on 26 Sep 2026 previewed an Ice Caves drop and "The Sift" dimension for 2027, with no drone. 2025's additions such as the happy ghast and the copper golem are mobs, not drones. Drone flight in Minecraft therefore exists only through mods.

### Cited Findings
- **26.3 "Wilderness Bound"**, article of 17 Sep 2026 (fetched).
  - Lists the Dappled Forest biome, poplar trees, cushions, straw beds and abandoned camps.
  - Mobs: "None listed". No drone, flying robot or RC vehicle appears. — [GamingOnLinux](https://www.gamingonlinux.com/2026/09/minecraft-java-edition-26-3-wilderness-bound-update-released/page=1/)
- **26.1 "Tiny Takeover".** Launched 24 Mar 2026 (Java 26.1, Bedrock 26.10), centred on redesigned baby mobs. Search summaries only. — [Minecraft Feedback, "Posted: 24 March 2026"](https://feedback.minecraft.net/hc/en-us/articles/44418129038733); [Nodecraft](https://nodecraft.com/support/games/minecraft/general/minecraft-tiny-takeover-update-overview)
- **26.2 "Chaos Cubed".** Headline mob is the passive Sulfur Cube in new Sulfur Caves. Search summaries only. — [BisectHosting](https://www.bisecthosting.com/blog/minecraft-26-2-chaos-cubed-update-release-date-patch-notes-more); [InGameNews](https://ingamenews.com/2026/06/minecraft-java-edition-262-chaos-cubed.html)
- **Minecraft Live (26 Sep 2026).** Ice Caves (next drop), frozen zombies, "The Sift" (a new dimension, 2027), Minecraft Dungeons II. Search summaries only. — [Windows Central](https://www.windowscentral.com/gaming/minecraft/minecraft-live-2026-everything-announced); [BisectHosting](https://www.bisecthosting.com/blog/minecraft-live-announcements-september-2026-the-sift-ice-caves-more)
- **2025.** The happy ghast (Chase the Skies, a rideable flying mob with a harness), the copper golem (The Copper Age, an item-sorting mob) and the parched (Mounts of Mayhem, December 2025). None is a drone. Search summaries only. — [Minecraft.net: happy ghast](https://www.minecraft.net/sv-se/article/happy-ghast); [Sportskeeda 2025 mobs](https://widgets.sportskeeda.com/minecraft/minecraft-list-new-mobs-2025); [Windows Central: Mounts of Mayhem](https://www.windowscentral.com/gaming/minecraft/minecraft-mounts-of-mayhem-game-drop-release)
- A search for a vanilla drone mob in 2026 found no report, official or otherwise. — [search results incl. PlayNews](https://www.playnews.gg/en/guides/minecraft-mob-vote-2026-why-mojang-put-an-end-to-it)

### Inferences
- The only vanilla change relevant to drone mods is technical: 26.3's move to SDL3 input. It plausibly helps radio and gamepad detection in mods such as Propwash, which reads radios through SDL3.

### Gaps
- I did not read Mojang's full official changelogs for 26.1, 26.2 and 26.3. Only the 26.3 article was fetched; the rest come from search summaries.
- Bedrock-only features and the release date of the Ice Caves drop are unconfirmed.
