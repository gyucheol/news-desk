# Real FPV flying vs camera-drone flying, and how well dedicated FPV simulators train it (baseline for judging a game's drone mode)

_Researched 2026-11-11. Steam Korea prices re-checked via the Steam store API (cc=kr, l=korean) at 2026-11-11 06:53 UTC (15:53 KST). Notes are in English, with Korean glosses for the report writer. "Via search summary" means the fact came from a search-engine summary of that page, not from opening the page in full, so it carries less weight._

## 1. What makes real FPV flying different (acro/rate vs self-levelling, manual throttle, momentum, video latency, Mode 2), and why acro is the core skill

### Takeaway
Hobby FPV quads (Betaflight firmware) are flown almost entirely in **acro/rate mode (아크로/레이트 모드)**. A stick movement sets how fast the quad rotates, nothing levels the quad automatically, and throttle is fully manual. The pilot therefore has to manage attitude, throttle and momentum all the time. They do it through a first-person video feed, with a Mode 2 radio (throttle and yaw on the left stick, pitch and roll on the right) whose throttle stick does not spring back to centre. Experienced educators call acro the core skill for three reasons: real FPV flying happens in acro, self-levelling habits don't carry over, and acro is what trains throttle control, momentum management and smooth camera lines.

### Cited Findings
**Flight modes**
- **Angle mode** levels itself and caps the tilt angle: "Angle mode can only tilt so far and you cannot do flips or rolls accidentally." **Horizon mode** levels itself near centre stick but allows flips and rolls with large inputs, and it "can feel inconsistent." **Acro mode** does not level itself. Moving the stick sets a rotation rate, and when the stick is released the quad holds whatever attitude it has reached. — [Oscar Liang, "Why You Should Fly Acro Mode and NOT Angle or Horizon Mode" (dated 12 Jun 2026)](https://oscarliang.com/acro-angle-horizon-modes/)
- Acro is Betaflight's fallback mode: if neither Angle nor Horizon is switched on, the quad is in acro when armed. Betaflight's docs list ANGLE as a "Legacy auto-level flight mode" and HORIZON as an "Auto-level flight mode." — [Oscar Liang, Betaflight Modes](https://oscarliang.com/betaflight-modes); [Betaflight docs: Modes](https://betaflight.com/docs/wiki/guides/current/Modes) (both via search summary)
- A retailer's plain-language version: an FPV drone in Acro mode "is entirely manual". If "you tilt it forward, it stays tilted until you manually level it back." — [Rotor Village (Canadian FPV shop) blog](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/)

**Why acro is treated as the core skill**
- Oscar Liang's reasons:
  - Self-levelling modes build habits that don't carry over to FPV, because the quad keeps correcting for you.
  - Angle mode is fine as a short training tool, but don't "get too comfortable" with it if your goal is freestyle or racing.
  - Many pilots are better off learning acro as soon as possible and skipping Horizon entirely.
  - He keeps Angle mode on a switch for emergencies but flies about 99% of the time in acro.
  - Source: [Oscar Liang (2026)](https://oscarliang.com/acro-angle-horizon-modes/)
- Skills he ties to acro: throttle control, momentum management, coordinated turns, proper recovery, smooth and precise camera-angle control, spatial awareness, and "full freedom for freestyle." — [Oscar Liang (2026)](https://oscarliang.com/acro-angle-horizon-modes/)
- Beginner ready-to-fly kits follow the same path. The BETAFPV Cetus FPV kit has a 3-position switch: Normal (N), Sport (S) and Manual (M). In Normal mode the quad "maintains a fixed altitude when both joysticks are moved to the center" (an altitude-hold training mode), and the guide recommends a windless space and 0.3–3 m altitude. Reviewers describe Sport as roughly angle mode and Manual as acro with no assistance. — [BETAFPV Cetus FPV Kit user manual (manuals.online mirror)](https://manuals.online/betafpv/quadcopter/cetus-fpv-kit/user-manual/1it24); [Cetus quick start guide (manuals.plus mirror)](https://manuals.plus/betafpv/cetus-fpv-kit-manual) (via search summary)

**Stick layout and throttle**
- In Mode 2 (the standard layout), "the left stick controls the throttle and rudder [yaw]" and "the right stick controls the elevator [pitch] and ailerons [roll]." — [Academy of Model Aeronautics, AMA Flight School](https://www.amaflightschool.org/diy/heavy-lift-challenge-lesson-4-radio-control)
- "Mode 2 is by far the most common" for multirotors. — [George Hawkins, ARF drone stick-setup guide](https://george-hawkins.github.io/arf-drone/docs/stick-setup) (via search summary)
- DJI camera-drone controllers use the same default: "The default mode is Mode 2." — [DJI Mini 2 User Manual v1.2 (2021.01)](https://cdn.shopify.com/s/files/1/1163/1976/files/DJI_Mini_2_User_Manual.pdf)
- FPV radios have a non-centring "friction" throttle that "stays exactly where you put it." Gamepad sticks "snap back to the center on both sides." — [Rotor Village](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/)

**Momentum, environment and the video feed**
- Simulators are "way more predictable and easier than in real life," because wind, latency and video glitches "simply don't exist in simulators." Nerves during real flights are "something simulators can never really prepare you for, and it takes actual flight time to get used to it." — [Oscar Liang, "The Best FPV Drone Simulators" (29 Aug 2026)](https://oscarliang.com/fpv-simulator/)
- Digital FPV video links have low but non-zero delay. DJI says the O4 link on Avata 2 has "a transmission latency as low as 24 ms," measured on a production model in a controlled environment. — [DJI Avata 2 launch release (11 Apr 2024)](https://www.dji.com/mobile/newsroom/news/dji-launch-avata-2-en)
- How experienced racers look ahead: 21 experienced pilots were tracked in a realistic drone-racing simulator.
  - Their eyes followed upcoming gates. Each gate was first fixated on average about 1.5 s and 16 m before the pilot reached it.
  - In turns and climbs/descents, pilots looked at the inside of the future flight path.
  - Eye movements correlated strongly with the commanded flight direction, with an average visual-motor response latency of about 220 ms.
  - Source: [Pfeiffer & Scaramuzza, "Human-Piloted Drone Racing: Visual Processing and Control," IEEE RA-L 2021 (arXiv:2103.04672)](https://arxiv.org/abs/2103.04672)
- How true to life momentum and weight feel varies between sims. Oscar Liang says:
  - Liftoff can feel "slightly 'floaty'".
  - Liftoff: Micro Drones whoops "seem to carry slightly more momentum than in real life".
  - TRYP FPV quads "feel slightly heavier than in real life".
  - Source: [Oscar Liang (Aug 2026)](https://oscarliang.com/fpv-simulator/)

### Inferences
- A baseline checklist for judging any game's drone mode as "real FPV" (my synthesis of the sources above):
  1. Rate/acro control with no automatic levelling.
  2. Fully manual throttle against gravity, with no altitude hold.
  3. Believable momentum and inertia (drift, overshoot, prop wash).
  4. Mode 2 four-axis input on analogue sticks, with a throttle that doesn't spring back.
  5. Adjustable rates and camera uptilt.
  6. Real-world video-feed traits such as delay and breakup. Even dedicated sims leave these out, along with wind.
- In acro the quad holds its tilt after the stick is released. So the core motor skill is coordinating throttle with pitch and roll all the time (for example, adding throttle while tilted forward). A self-levelling or arcade flight model takes exactly this skill away. This is an inference from Oscar Liang's description, not a direct quote.
- The gaze study suggests FPV piloting is anticipatory: pilots look about 1.5 s ahead. That may overlap with an FPS player's habit of scanning ahead, but this is a hypothesis that nobody has tested.

### Gaps
- I found no current primary source comparing analogue and digital FPV video delay, or showing how video delay affects beginners.
- I didn't open Betaflight's official Modes page in full; it is cited via a search summary.
- I found no source that measures how closely any sim's momentum or inertia matches real quads. Comments on "floaty" or "heavy" physics are expert opinion.

## 2. How flying a GPS-stabilised camera drone differs from FPV, and how DJI's beginner FPV options (Avata 2, Neo 2 with goggles, Motion Controller) differ from acro

### Takeaway
Camera drones such as the DJI Mini series use GPS and downward cameras to hold their position, hover and brake on their own, and they limit speed and tilt. The pilot moves a stable camera around rather than controlling the aircraft's attitude. DJI's FPV-style products run in stabilised Normal or Sport modes by default, or with the Motion Controller, which lets you fly by pointing and do one-push "Easy ACRO" tricks. The acro-like Manual (M) mode needs a separate stick controller: the DJI FPV Remote Controller 3 (or FPV Remote Controller 2 for Avata 2), plus goggles for Neo 2.

### Cited Findings
**Camera drones (DJI Mini 2 manual as the example)**
- "Normal Mode: The aircraft utilizes GPS and the Downward Vision System to locate itself and stabilize." Normal mode caps tilt at 25° and speed at 10 m/s.
- Sport mode (16 m/s) is "more responsive to control stick movements" but still uses GPS and vision positioning.
- Cine mode limits speed to 6 m/s, making the aircraft "more stable during shooting."
- Source: [DJI Mini 2 User Manual v1.2](https://cdn.shopify.com/s/files/1/1163/1976/files/DJI_Mini_2_User_Manual.pdf)
- From the same manual:
  - The Flight Pause button makes the aircraft "brake and hover in place (only when GPS or Downward Vision System are available)."
  - "The aircraft hovers in place after takeoff."
  - Without GPS or vision positioning it drops to ATTI mode, where it "cannot position itself or brake automatically" and wind can cause "horizontal shifting."
  - Source: [DJI Mini 2 User Manual](https://cdn.shopify.com/s/files/1/1163/1976/files/DJI_Mini_2_User_Manual.pdf)

**DJI Avata 2**
- DJI's launch release (11 Apr 2024):
  - "In addition to Normal and Sport modes, the DJI FPV Remote Controller 3 offers Manual mode," which is "better suited for advanced pilots to practice and master more sophisticated skills."
  - RC Motion 3 gives newer pilots "Easy ACRO": one-push 360° flips, one-push rolls and a one-push 180° drift. Pressing its lock button stops the drone.
  - Source: [DJI Avata 2 launch release](https://www.dji.com/mobile/newsroom/news/dji-launch-avata-2-en)
- DJI's Avata 2 FAQ:
  - M mode "Requires DJI FPV Remote Controller 2 or DJI FPV Remote Controller 3."
  - In N and S modes the drone uses downward and backward visual positioning.
  - Asked about obstacle avoidance, the FAQ answers "No."
  - With RC Motion 3, "users can quickly learn to fly without complicated and extensive instructions."
  - DJI states: "We recommend practicing with the following four simulators: Liftoff, Uncrashed, The Drone Racing League, and DCL."
  - Source: [DJI Avata 2 FAQ](https://www.dji.com/au/avata-2/faq)
- DJI's own simulator: users can "try out the Avata 2 virtually in the Virtual Flight section" of the DJI Store app. — [DJI Avata 2 launch release](https://www.dji.com/mobile/newsroom/news/dji-launch-avata-2-en)

**DJI Neo 2**
- DJI's official release notes (2025.11.07, firmware V01.00.0400): "Added Manual mode when used with DJI Goggles N3/DJI Goggles 3 and DJI FPV Controller 3." — [DJI Neo 2 Release Notes (PDF)](https://dl.djicdn.com/downloads/DJI_Neo_2/RN/20251107/DJI_Neo_2_Release_Notes_en.pdf); also reported by [DroneDJ, 27 Nov 2025](https://dronedj.com/2025/11/27/dji-neo-2-manual-fpv/)
- A third-party guide adds:
  - The standard RC-N3 controller and the DJI Motion Controller 3 cannot switch Neo 2 into Manual mode.
  - Manual mode turns off precise hovering, auto-brake, self-levelling and obstacle avoidance.
  - The Motion Controller's "Easy ACRO" (front flips, backflips, rolls, 180° drift) is not Manual mode.
  - Source: [HireDronePilot](https://hiredronepilot.uk/blog/how-to-fly-dji-neo-2-in-manual-mode/) (via search summary)

### Inferences
- **Camera drones:** the sticks command movement relative to a held position, and the drone hovers on its own. A DJI camera drone teaches framing and awareness of the surrounding airspace, but very little of the acro throttle-and-attitude skill.
- **Avata 2 / Neo 2 in N, S or Motion modes:** these give a stabilised first-person view, not acro. Only M mode, flown with the FPV Remote Controller, comes close to hobby-FPV acro. "Easy ACRO" automates tricks instead of training them.
- **For this user (wants FPV, beginner):** a DJI FPV-style kit can be flown on day one with the Motion Controller. Learning "real" FPV on it needs the FPV Remote Controller 3 and simulator practice, which DJI itself recommends (Liftoff, Uncrashed, DRL, DCL).
- **Conflict with §4:** DJI's FAQ still lists The Drone Racing League Simulator, which Oscar Liang warned in Jan 2026 not to buy because its server shut down. DJI's FAQ probably predates that.

### Gaps
- I couldn't confirm whether DJI Virtual Flight supports Manual mode with the FPV Remote Controller 3.
- I couldn't get DJI's own Avata 2 or Neo 2 user manual wording on practising M mode first. The DJI manual PDFs returned HTTP 403.
- I couldn't confirm whether the DJI FPV Remote Controller 3's throttle stick can be set not to spring back for M mode. The DJI store page redirected to a login.
- I didn't check newer Mini models (Mini 4 Pro / Mini 5 Pro). The Mini 2 manual stands in as an example of how a GPS camera drone behaves.

## 3. What the community and manufacturers recommend for learning (simulator first, with a real radio), and why they warn against keyboard or gamepad practice

### Takeaway
Educators, retailers, simulator developers and DJI all say the same thing: learn in a simulator first, ideally with the same RC radio you will fly with (it plugs in by USB and shows up as a joystick). They warn off gamepads and keyboards because those lack precision and because gamepads spring the throttle back to centre. A real radio builds muscle memory that carries straight over to the real drone. Hour targets are rules of thumb (one retailer says at least 3 h before a first flight and 10–15 h to get past the basics), not research findings.

### Cited Findings
**Oscar Liang**
- On input devices:
  - "I don't recommend using gaming consoles (such as PlayStation or Xbox) or a keyboard"; they lack the precision needed and don't translate well to real flying.
  - "Using a proper radio controller helps build muscle memory and maximizes the benefits of your simulator training."
  - A radio "will appear as a gaming joystick on your computer". EdgeTX radios need the "USB Joystick" option selected, and DJI RC2/RC3 controllers are plug-and-play.
- On sims versus reality:
  - Sims will "never fully replace real-world flying."
  - He advises "consistent practice rather than worrying too much about simulator physics."
  - He gives no hour target.
- Source: [Oscar Liang, Best FPV Simulators (29 Aug 2026)](https://oscarliang.com/fpv-simulator/)
- Practise acro in a simulator before flying a real drone, and keep rates manageable (defaults are usually fine). On real drones, expect crashes, fly over soft ground such as grass, and stay low. — [Oscar Liang, acro article (12 Jun 2026)](https://oscarliang.com/acro-angle-horizon-modes/)
- Radios can also connect to sims without a cable: through a Betaflight flight controller acting as an HID joystick, through ELRS Bluetooth, or through dongles. — [Oscar Liang](https://oscarliang.com/betaflight-fc-fpv-simulator) (via search summary)

**Rotor Village (FPV retailer)**
- Gamepad sticks "snap back to the center on both sides." You could use one, but "we don't recommend it." A radio's throttle "stays exactly where you put it."
- "You need to develop 'muscle memory' in your thumbs (or fingers, if you're a 'pincher')."
- "By putting in just 10 to 15 hours in a simulator" you get past basic control. Its "3-Hour Rule" says to "Spend at least three hours in the simulator" before your first real flight.
- Radios connect "via a simple USB-C cable" and "are recognized instantly as a joystick."
- Source: [Rotor Village](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/)

**Simulator developers (Steam store text)**
- Liftoff: "requires a remote or controller to play"; system notes say "Only playable with a game or radio c[ontroller]". — [Liftoff Steam page](https://store.steampowered.com/app/410340/)
- Liftoff: Micro Drones: "Recommended to be played with an RC transmitter." — [Steam](https://store.steampowered.com/app/1432320/)
- Uncrashed: "A radio controller is highly recommended for the full FPV experience" and "Only playable with a game controller or remote." — [Steam](https://store.steampowered.com/app/1682970/)
- TRYP FPV: "RC transmitter is recommended." — [Steam](https://store.steampowered.com/app/1881200/)
- FPV SkyDive: "Preferably a transmitter radio is wanted for best flying experience," while also advertising native PlayStation, Xbox and ORQA FPV.Ctrl support. — [Steam](https://store.steampowered.com/app/1278060/)
- Nuance: Steam metadata tags Liftoff and Liftoff: Micro Drones "Gamepad Recommended" with DualShock/DualSense support. That means a gamepad is preferred over keyboard and mouse. It is not a claim that gamepads beat RC radios. — [Steam appdetails API, Liftoff](https://store.steampowered.com/api/appdetails?appids=410340&cc=kr&l=korean); [Micro Drones](https://store.steampowered.com/api/appdetails?appids=1432320&cc=kr&l=korean)

**Manufacturers**
- DJI recommends simulator practice for its FPV products: "We recommend practicing with the following four simulators: Liftoff, Uncrashed, The Drone Racing League, and DCL." — [DJI Avata 2 FAQ](https://www.dji.com/au/avata-2/faq)
- BETAFPV:
  - The LiteRadio 2 SE "also functions as a USB joystick, allowing seamless connection to a PC for FPV simulator practice." — [LiteRadio 2 SE listing (manuals.plus)](https://manuals.plus/asin/B095BQNPLF) (via search summary)
  - BETAFPV sells a dedicated LiteRadio 2 SIM controller. — [BETAFPV product page](https://betafpv.com/collections/radio-controllers/products/literadio-2-sim-controller) (via search summary)
  - The Cetus Lite manual: "it is recommended to begin flying without using fpv goggles for practice. Be familiar with the controls and sensitivity of the joysticks." — [Cetus Lite FPV Kit manual (2022)](https://www.rc-airstage.com/pdf/Cetus%20Lite%20FPV%20Kit%20-%20User%20Manual%20(2022).pdf) (via search summary)

**Community and Joshua Bardwell**
- A Steam forum reply to an Xbox-pad user recommends a proper FPV controller because "you need that Zero Throttle control." — [Steam Uncrashed discussion](https://steamcommunity.com/app/1682970/discussions/0/4635989156416208126) (via search summary)
- Joshua Bardwell's "Ultimate FPV Shopping List" (updated Nov 2026) lists RadioMaster radios (TX16S Mk3, GX12, Boxer Crush, TX15, GX15). The page says nothing about simulators or gamepads. — [fpvknowitall.com](https://www.fpvknowitall.com/ultimate-fpv-shopping-list/)

**Unverified claims to avoid**
- A widely repeated hobby-blog figure says sim-trained pilots crash about 2 times in their first 10 real flights, versus about 20 without a simulator. It is attributed to "UAVMODEL Insights" (2026). I could not trace it to any study, so treat it as unverified and do not use it. — seen in search results around [UAVMODEL Insights blog](https://blog.uavmodel.com/fpv-simulator-training-liftoff-vs-velocidrone-vs-uncrashed-building-real-world-muscle-memory-2026-guide/) (page not opened)

### Inferences
- The sources give two concrete reasons for the gamepad warning:
  - A throttle that springs back to centre can't be parked at a hover point or at zero.
  - Lower precision and shorter stick travel mean muscle memory won't match a radio's sticks.
- Mode 2 is the same on both devices. A Call of Duty player's thumb habits on a pad map to the same axes, but not to the same throttle behaviour.
- The radio is the one purchase that carries over to the real drone (Oscar Liang). For a home learner, buying a radio first is the efficient route. A gamepad is acceptable only for trying a free sim.

### Gaps
- I couldn't retrieve a direct, citable Joshua Bardwell statement on gamepads versus radios or on acro, because YouTube content wasn't accessible. Forums often recommend his "Learn to fly an FPV drone TODAY (for total beginners)" series ([IntoFPV thread](https://intofpv.com/archive/index.php/thread-15583.html), via search summary), but I didn't verify what it says. **Don't attribute specific quotes to Bardwell.**
- I didn't access the r/fpv wiki. GetFPV's learning pages returned HTTP 403.
- I found no primary source that measures gamepad stick resolution or travel against RC radio sticks.
- Recommended simulator hours have no research basis.

## 4. Which simulators are closest to real FPV physics and best for learning: platform, controller support, rate settings, realism, current Steam Korea prices

### Takeaway
Oscar Liang's August 2026 roundup gives these verdicts:
- **Liftoff:** best for beginners (structured tutorials; physics slightly "floaty").
- **VelociDrone:** best and most realistic for racing.
- **Uncrashed and TRYP FPV:** strong for freestyle and visuals.
- **FPV SkyDive:** best free option, with "mediocre" physics.
- **DRL Simulator:** do not buy; he reports its server shut down in January 2026.

All of them work with RC radios over USB and say a radio is better than a gamepad. TRYP FPV and FPV SkyDive advertise adjustable rates, and Liftoff uses Betaflight-style rates according to a 2021 developer note. Steam Korea prices re-checked on 2026-11-11 are unchanged from the 2026-11-10 check: Liftoff ₩25,000, Liftoff: Micro Drones ₩17,500, Uncrashed ₩11,990 on sale (−25% from ₩15,990), DRL ₩10,500, TRYP ₩18,500, FPV SkyDive free. VelociDrone is not on Steam; its base licence costs £16.99 on velocidrone.com (about ₩30,500).

### Cited Findings
**Comparison table** (Steam data fetched 2026-11-11 06:53 UTC; review figures from the Steam store pages the same day)

| Simulator (Steam app ID) | Developer / release | Price, Korea (2026-11-11) | Platforms | Controller notes (developer text, Steam tags) | Rate settings | Steam reviews | Oscar Liang verdict (29 Aug 2026) | Sources |
|---|---|---|---|---|---|---|---|---|
| **Liftoff: FPV Drone Racing** (410340) | LuGus Studios, 13 Sep 2018 | **₩25,000** (no discount) | Win / Mac / Linux | "requires a remote or controller"; "seamless integration with transmitters"; tagged Gamepad Recommended, DualShock/DualSense | Betaflight-style rates (2021 dev note: Betaflight rates only, no Actual rates; may be outdated) | 95% positive of 7,227 English reviews; 95% of 184 in last 30 days | "Best for beginners"; "one of the best all-around FPV simulators"; "Excellent training tutorials"; con: "slightly 'floaty'"; "from $19.99" | [Steam](https://store.steampowered.com/app/410340/), [API](https://store.steampowered.com/api/appdetails?appids=410340&cc=kr&l=korean), [Steam rates thread](https://steamcommunity.com/app/410340/discussions/0/3123801577566057498) (via search summary), [Oscar](https://oscarliang.com/fpv-simulator/) |
| **Liftoff: Micro Drones** (1432320) | LuGus Studios; Steam release date 4 Aug 2025 | **₩17,500** | Win / Mac / Linux | "Recommended to be played with an RC transmitter"; tagged Gamepad Recommended, DualShock/DualSense | not stated on Steam | 93% of 1,512 (all languages); 98% of 50 in last 30 days | Best Tiny Whoop sim; whoops "seem to carry slightly more momentum than in real life"; "from $5.99" | [Steam](https://store.steampowered.com/app/1432320/), [API](https://store.steampowered.com/api/appdetails?appids=1432320&cc=kr&l=korean), [Oscar](https://oscarliang.com/fpv-simulator/) |
| **Uncrashed: FPV Drone Simulator** (1682970) | Luminite, 1 Sep 2021 | **₩11,990 on sale** (−25%; list ₩15,990) | Win / Mac | "Only playable with a game controller or remote"; "A radio controller is highly recommended"; DualShock/DualSense | "PHYSICS 3.0" (updated thrust and prop-wash simulation, PID tuning); rate system not stated on Steam | 94% of 2,490 English; 91% of 340 in last 30 days | "Best for freestyle"; physics "average, not quite as realistic" as established sims; needs a powerful PC; no structured beginner programme; "from $14.99" | [Steam](https://store.steampowered.com/app/1682970/), [API](https://store.steampowered.com/api/appdetails?appids=1682970&cc=kr&l=korean), [Oscar](https://oscarliang.com/fpv-simulator/) |
| **VelociDrone** (not on Steam) | VelociDrone, sold at velocidrone.com | **£16.99 base licence** (≈₩30,500); add-on packs £4–£8 | Win 7–11 64-bit / macOS High Sierra+ / Linux | not stated on shop page | not verified | n/a (not on Steam) | "Best for racing"; "top-notch physics"; runs on relatively modest PCs; "an unparalleled choice" for realistic racing physics; "barebones tutorials"; "from $19.99" | [VelociDrone shop](https://velocidrone.com/shop), [Oscar](https://oscarliang.com/fpv-simulator/) |
| **The Drone Racing League Simulator** (641780) | The Drone Racing League, 1 Nov 2017 | **₩10,500** | Win / Mac | "connect your transmitter"; claims "one-to-one physics with data from real life drones"; built-in interactive training tutorial | not verified | 84% of 2,229 English, **but only 41% of 12 in last 30 days** | "feels dated in both graphics and physics"; "Warning (17 Jan 2026): DO NOT purchase this sim for now! Server has shut down."; offline play reportedly broken | [Steam](https://store.steampowered.com/app/641780/), [API](https://store.steampowered.com/api/appdetails?appids=641780&cc=kr&l=korean), [Oscar](https://oscarliang.com/fpv-simulator/) |
| **TRYP FPV: Drone Racer Simulator** (1881200) | UNDEAD BATTERY, 30 Jun 2022 (Steam genres include "Early Access") | **₩18,500** | Win / Mac | "RC transmitter is recommended" | "Adjust your rates to refine the responsiveness" | 85% of 1,295 English; 88% of 26 in last 30 days | "Best for cinematic flying"; "arguably one of the best freestyle simulators"; physics "reasonably accurate" but quads "feel slightly heavier than in real life"; training programme "falls short"; weaker for racing; "from $14.99" | [Steam](https://store.steampowered.com/app/1881200/), [API](https://store.steampowered.com/api/appdetails?appids=1881200&cc=kr&l=korean), [Oscar](https://oscarliang.com/fpv-simulator/) |
| **FPV SkyDive** (1278060) | ORQA, 31 May 2021 | **Free-to-play**. Paid add-ons: Flight School ₩12,500, Micro Drone Edition ₩11,000, Drone Soccer ₩8,900, Track Builder ₩6,700 | Win / Mac / Linux | native PlayStation, Xbox and ORQA FPV.Ctrl support; "Preferably a transmitter radio" | "Calibrate and fine-tune your rates" | 84% of 1,923 English; 90% of 65 in last 30 days | "Best free simulator"; physics "mediocre"; suitable only as a basic entry point, not for serious progression | [Steam](https://store.steampowered.com/app/1278060/), [store search API](https://store.steampowered.com/api/storesearch/?term=skydive%20fpv&l=korean&cc=kr), [Oscar](https://oscarliang.com/fpv-simulator/) |

**Prices and purchase details**
- The re-checked Steam Korea prices match the 2026-11-10 figures exactly. The API's price fields are KRW × 100; for example, Liftoff's `final: 2500000` is `₩ 25,000`. The appdetails API does not give an end date for Uncrashed's 25% sale. — [Steam store search API](https://store.steampowered.com/api/storesearch/?term=liftoff&l=korean&cc=kr); [Uncrashed price API](https://store.steampowered.com/api/appdetails?appids=1682970&cc=kr&l=korean&filters=price_overview)
- Liftoff add-ons in Korea: Slipstream ₩4,500 and Night Fever ₩6,700. A "Liftoff® – DJI FPV" add-on is also listed, but the API returned no price for it. — [Steam store search API](https://store.steampowered.com/api/storesearch/?term=liftoff&l=korean&cc=kr)
- **VelociDrone shop prices:** base licence £16.99 ("required to run velocidrone and a pre-requisite to installing any premium content"); Freestyle Pack £5.00; Combat £8.00; Micro Class Quads, Mega Class Quads and Champions Series £4.00 each. — [VelociDrone shop](https://velocidrone.com/shop)
- **VelociDrone in won:** the ECB reference rate for 2026-11-10 was 1 GBP = 1,797.31 KRW (and 1.3423 USD). That puts £16.99 at about ₩30,536 (≈$22.81), and the base licence plus the Micro pack (£20.99) at about ₩37,726, before any card or PayPal foreign-exchange fees. — [Frankfurter API (ECB rates)](https://api.frankfurter.dev/v1/latest?from=GBP&to=KRW,USD). Oscar Liang's "from $19.99" doesn't match the official GBP price at today's rate.
- **How to buy VelociDrone** (third-party walkthrough):
  1. Register an account on velocidrone.com.
  2. Open "Shop" and add the licence to the cart.
  3. Pay by card through "PAY WITH STRIPE" or by PayPal.
  4. Go to "My Licenses" and download the launcher, which then downloads the game (over 2 GB).
  - The licence is tied to the first PC it is installed on; "UN-ASSIGN LICENSE" lets you move it to another PC.
  - Only paid downloads are offered now; there is no free trial.
  - Source: [Apollomaniacs VelociDrone guide](https://www.apollomaniacs.com/ipod/howto_ar_drone_velocidrone_download_en.htm). The end of the free trial is also reported in [IntoFPV news](https://intofpv.com/t-news-velocidrone-ends-free-trial-option?pid=56694) (via search summary).

**Minimum PC specs**

| Simulator | Minimum CPU | RAM | GPU | Storage | Notes | Source |
|---|---|---|---|---|---|---|
| Liftoff | Intel 8th gen / Ryzen 1st gen, 2.4 GHz | 8 GB | **RTX 2060 / RX Vega 56, 4 GB VRAM** | 25 GB | — | [Steam](https://store.steampowered.com/app/410340/) |
| Liftoff: Micro Drones | not listed | 3 GB | not listed | 15 GB | "Integrated Intel HD graphics cards not recommended" | [Steam](https://store.steampowered.com/app/1432320/) |
| Uncrashed | i5 2.6 GHz | 4 GB | GTX 770, 2 GB | 30 GB | — | [Steam](https://store.steampowered.com/app/1682970/) |
| DRL Simulator | i5-4460 | 8 GB | GTX 650, 2 GB | 15 GB | — | [Steam](https://store.steampowered.com/app/641780/) |
| TRYP FPV | quad-core 2.4 GHz | 8 GB | GTX 960 / RX 460 | 25 GB | DirectX 12 | [Steam](https://store.steampowered.com/app/1881200/) |
| FPV SkyDive | Intel Core i5 | 8 GB | GTX 650, 2 GB | 2 GB | — | [Steam](https://store.steampowered.com/app/1278060/) |
| VelociDrone | 1.7 GHz | 4 GB | Intel HD 530 | 37 GB (55 GB during install) | Recommended: GTX 1050 Ti | [VelociDrone shop](https://velocidrone.com/shop) |

**Other realism opinions**
- Oscar Liang on sims outside the list: FPV Logic has physics "similar to VelociDrone" with a freestyle lean ("from $19.99"); FPV Freerider is a "simple, basic sim"; DCL has "unrealistic physics"; WebFPV is free and runs in a browser, but its "physics are still a work in progress." Default settings "aren't optimal," and rates are "One important setting to customize early." — [Oscar Liang (Aug 2026)](https://oscarliang.com/fpv-simulator/)
- Rotor Village's view: VelociDrone is "Known for having the most 'true-to-life' physics"; Liftoff is "The most popular choice with a massive community"; Uncrashed has "Stunning graphics"; TRYP has "massive maps"; DIYFPV is a free browser sim. — [Rotor Village](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/)

**DRL Simulator status: conflicting signals**
- Oscar Liang warns that its server shut down (17 Jan 2026). — [Oscar Liang](https://oscarliang.com/fpv-simulator/)
- Steam still sells it at ₩10,500. — [Steam API](https://store.steampowered.com/api/appdetails?appids=641780&cc=kr&l=korean)
- Its last Steam news post was "DRL SIM 4.1 Release Announcement" (18 May 2023). — [Steam News API](https://api.steampowered.com/ISteamNews/GetNewsForApp/v2/?appid=641780&count=8)
- Recent reviews have dropped to 41% positive. — [Steam](https://store.steampowered.com/app/641780/)
- No Steam discussion title explicitly announces a shutdown. Undated recent threads include "Community Server" and "Offline Mode." — [Steam discussions](https://steamcommunity.com/app/641780/discussions/)
- DJI's Avata 2 FAQ still recommends DRL. — [DJI FAQ](https://www.dji.com/au/avata-2/faq)

### Inferences
- An evidence-based shortlist for a Korean beginner learning at home:
  - **Liftoff (₩25,000):** best structured tutorials and biggest community. Check the high minimum GPU (RTX 2060).
  - **Uncrashed (₩11,990 while on sale):** freestyle-oriented, but with weaker beginner structure.
  - **FPV SkyDive (free):** a zero-cost first try.
  - **VelociDrone (about ₩30,500 plus FX fees):** if racing realism matters. Bought on its own website, not through Steam.
  - **DRL Simulator (₩10,500):** avoid for now, even though it's the cheapest, given the reported server shutdown and falling recent reviews.
- These "realism" rankings are expert and retailer opinion. No source in this research measured any sim's physics against real quads.

### Gaps
- Uncrashed's sale end date isn't available from the API.
- I couldn't verify from primary sources which rate systems (Actual, Betaflight, KISS) Uncrashed, VelociDrone, Micro Drones and DRL support. The Liftoff rate information dates from 2021.
- The DRL server shutdown comes from one source (Oscar Liang) and isn't independently confirmed.
- I don't know whether VelociDrone adds VAT at checkout for Korean buyers.
- I didn't verify Steam Deck or VR support.
- An Apple App Store listing named "VelociDrone" appeared in search results, but I didn't check what it is.

## 5. Evidence on simulator-to-real transfer, and on how gamers perform

### Takeaway
The evidence is thin and mostly indirect:
- **Gamers:** a few small studies link video-game experience to better performance on *simulated* drone tasks (military UAS cognitive tasks, a desktop search-and-rescue task, a camera-drone simulator).
- **Sim training:** two recent studies (2024, 2026) suggest structured simulator training improves basic (non-acro) drone control, or matches hands-on physical training.
- **Hobby acro FPV:** I found **no controlled study** of whether simulator practice carries over to real acro flying for hobbyists. Popular claims that sims "cut crashes" are unverified.

### Cited Findings
**Gamers versus non-gamers**
- **McKinley, McIntire & Funke (2011), *Aviation, Space, and Environmental Medicine* 82(6):635–642.** — [PubMed 21702315](https://pubmed.ncbi.nlm.nih.gov/21702315/) (doi:10.3357/asem.2958.2011)
  - Context: US Air Force research on a shortage of operators for large military drones (Predator/Reaper).
  - Design: 30 participants in 3 groups (experienced pilots, experienced video-game players, controls), each trained on 8 cognitive tasks relevant to unmanned flight.
  - Pilots significantly outperformed gamers and controls on multi-attribute (multitasking) cognitive tasks.
  - Gamers outperformed pilots on visually acquiring, identifying and tracking targets.
  - On the simulated UAS landing task, gamers and pilots performed similarly and both beat the controls.
  - Conclusion (hedged): "Cognitive skills learned in video game play **may** transfer to novel environments and improve performance in UAS tasks over individuals with no video game experience."
  - Strength: about 10 per group, a one-time group comparison (not a training study), military UAS tasks, no FPV, no real flight.
- **Ferraro, Mouloua, Mangos & Matthews (2022), *Ergonomics* 65(12):1659–1671.** — [PubMed 35297326](https://pubmed.ncbi.nlm.nih.gov/35297326/) (doi:10.1080/00140139.2022.2048896)
  - Design: 49 participants each flew 9 trials of a simulated search-and-rescue UAS mission on a desktop computer.
  - Gaming experience correlated with *lower* self-reported workload and *better* performance on multiple measures.
  - Nearly all gender differences disappeared once gaming experience was controlled for.
  - Strength: correlational, desktop mission-control task, no real flight.
- **Ramallo-Luna, González-Torre, Núñez-Molleda & De la Torre (2025), *Apuntes de Psicología* 43(2):143–155 (University of Cádiz).** — [Apuntes de Psicología article page](https://apuntesdepsicologia.es/index.php/revista/article/view/1633) (doi:10.70478/apuntes.psi.2025.43.13); [Infocop coverage](https://www.infocop.es/la-experiencia-en-videojuegos-un-activo-estrategico-en-el-pilotaje-de-drones-implicaciones-psicologicas-para-la-formacion-y-seleccion-de-operadores/)
  - Title: "Ventaja estratégica en el cielo: experiencia en juegos y eficiencia operativa…"
  - Design: a self-described **pilot study** of 22 video-game players and 29 non-players (51 volunteers; Infocop says they had no prior drone experience). They flew simulated tasks in the **AeroSIM RC** simulator using a modelled **DJI Phantom 3**, a GPS camera drone.
  - Gamers finished the simulated flights faster (Mann-Whitney z = −4.168, p < 0.01).
  - Gamers made fewer errors (z = −4.690, p < 0.01).
  - Gamers reported lower workload on all AWT scales (a NASA-TLX-derived test).
  - **No real drone was flown.**
  - Strength: small, non-randomised, simulator only, camera-drone model rather than acro.

**How experienced FPV racers fly**
- **Pfeiffer & Scaramuzza (2021), IEEE Robotics and Automation Letters.** — [arXiv:2103.04672](https://arxiv.org/abs/2103.04672)
  - 21 *experienced* (not necessarily expert) pilots in a realistic drone-racing simulator.
  - Their gaze tracked future gates, first fixating each one about 1.5 s and 16 m ahead.
  - Visual-motor latency averaged about 220 ms, and performance improved over time.
  - This describes expert strategy; it is **not** a study of training carrying over to real flight.

**Simulator training and real flight**
- **Somerville, Lynar, Joiner & Wild (2024), "Use of Simulation for Pre-Training of Drone Pilots," *Drones* 8(11):640.** — [doi:10.3390/drones8110640](https://doi.org/10.3390/drones8110640) (abstract via [Crossref](https://api.crossref.org/works/10.3390/drones8110640); 25 citations per [Semantic Scholar](https://api.semanticscholar.org/graph/v1/paper/DOI:10.3390/drones8110640))
  - Design: described by the authors as a "true-experimental" design, with structured, instructor-led simulator training.
  - Outcome measure: how precisely participants returned the aircraft to a set point after a standard manoeuvre.
  - Result: "a significant improvement in flight performance among participants undergoing simulator training, reflected in a 32% reduction in mean final displacement."
  - The abstract frames the aim as improving "real-world drone operation proficiency."
- **Su, Li, Chang & Tarng (2026), "Development and Evaluation of a Virtual UAV Training System for Flight Skill Acquisition," *Electronics* 15(18):4133 (published 12 Sep 2026).** — [doi:10.3390/electronics15184133](https://doi.org/10.3390/electronics15184133) (abstract via Crossref)
  - System: a Unity-based virtual UAV trainer that stays synchronised with a physical drone.
  - Design: quasi-experimental; 60 university students with no UAV experience, split into a virtual-training group and a physical-training group (30/30 per search summary).
  - Both groups improved significantly in knowledge and flight performance, "with statistical/practical equivalence within a prespecified margin."
  - The virtual group scored higher on "Relevance" (ARCS motivation scale) but had more extraneous cognitive load. The physical group showed higher technology acceptance.
  - Strength: not randomised, modest sample, educational drone tasks rather than acro FPV.

**Expert caveats on how far sims transfer**
- Sims lack wind, video delay and glitches, and the nerves of real flight, so they "never fully replace real-world flying." — [Oscar Liang (Aug 2026)](https://oscarliang.com/fpv-simulator/)

### Inferences
- **Evidence-strength summary for the report:**
  - *That gamers do better on simulated drone tasks:* consistent but weak. There are 3 small studies (n = 30, 49, 51), all cross-sectional or correlational and all in simulation. None tested acro FPV or real flight, and the drone types differ (military UAS, desktop search-and-rescue, a GPS camera drone).
  - *That simulator training improves real flight:* emerging and moderate for **basic, stabilised drone control** (Somerville 2024; Su 2026). It is **unstudied for acro FPV**. The universal advice to "learn in a sim with a real radio" rests on expert consensus and developer guidance, not on controlled trials.
- **For this user (Call of Duty player):** FPS experience may help with visual attention, target tracking and handling workload (McKinley; Ferraro; Ramallo-Luna). Nothing shows it substitutes for practising acro stick-and-throttle coordination, so the report shouldn't claim "gamers are naturally good FPV pilots."
- **Unverified claim:** the hobby-blog "2 vs 20 crashes" figure (§3) should not be presented as evidence.

### Gaps
- **Somerville et al. 2024:** I couldn't verify the sample size, the drone used, or whether the final test was flown on a real drone or in simulation. MDPI blocked automated access to the full text, and I didn't attempt to work around that block. The abstract only implies a real-world aim.
- **No randomised or controlled study** of hobby acro-FPV simulator-to-real transfer for novices turned up in PubMed, Crossref or web searches.
- **Ramallo-Luna 2025:** I couldn't confirm how "gamer" was defined (self-report thresholds) or what limitations the authors listed.
- **Not reviewed:** the same Cádiz group's related paper, "Neurocognitive factors of new drone Pilots: Identifying candidates with expert potential" (*Computers in Human Behavior Reports*, 2025), surfaced in search ([library record](https://library.kab.ac.ug/Record/doaj-art-4b5ecd6dc52544ffa7a5447877517aa0)).
- **Not used:** the transfer-of-training literature from manned aviation (for example, [ERAU transfer-of-training report](https://commons.erau.edu/cgi/viewcontent.cgi?article=1189&context=publication)), since it falls outside the hobby FPV scope.
