# A practical at-home path for a Korean beginner: from a PC simulator to a first small real FPV flight, and what to buy in Korea

Research date: 2026-11-11. All pages accessed 2026-11-11. "(fetched)" means I read the page itself. "(snippet only)" means I saw the fact only in a search-result summary and did not open the page, so treat it as weaker. Prices are list prices shown on the day and change often. Stock status is as displayed on the day.

## Q1. Which radio transmitters work as USB joysticks (HID) with PC simulators and can later fly real drones? Protocol, Mode 2, Korean price and seller, KC status

### Takeaway
The RadioMaster Pocket (ELRS) is the most practical "one radio for sim and real drone" buy in Korea. At least five Korean RC shops list it at the same 129,000원 (ELRS, Mode 2), and one shop (링크드론) labels its listing "KC 인증 제품". Its USB-joystick use is documented by the EdgeTX firmware project and by retailers, not on RadioMaster's own product page. BETAFPV's LiteRadio 3 is the only radio here whose maker page says "USB Joystick" outright, but I found no Korean domestic listing for it. The TBS Tango 2 is confirmed as a joystick by TBS, but it costs about 2.5× more in Korea and uses Crossfire instead of ELRS. The Jumper T-Lite V2 is listed as discontinued.

### Cited Findings

**RadioMaster Pocket (main candidate)**
- Maker spec: internal RF is either "CC2500 multi-protocol / ELRS 2.4GHz". The ELRS LBT (EU) version is "Limited to 100mw power output". X5 Hall-effect nano gimbals. Runs EdgeTX, preinstalled. Two 18650 cells, not included. USB-C with QC3 charging. 288 g. SKUs carry "M2" (Mode 2), and a gimbal switch changes whether the throttle stick self-centres (M1/M2). Price on RadioMaster's site: $59.99 (CC2500) to $71.50 (ELRS). — [RadioMaster Pocket product page (fetched)](https://www.radiomasterrc.com/products/pocket-radio-controller-m2)
- RadioMaster's product page does not itself claim USB joystick/HID simulator use. It only mentions USB for firmware updates. It names no FCC/CE/KC certificate in the text, though it links a "Certification Document" whose contents I could not read. — [RadioMaster Pocket product page (fetched)](https://www.radiomasterrc.com/products/pocket-radio-controller-m2)
- The EdgeTX firmware manual documents a "USB Joystick" mode with Classic and Advanced settings, and advises "Please try the classic mode first". EdgeTX radios report to the PC as a USB HID joystick/gamepad (VID 1209 / PID 4F54). The manual also says to turn RF modules off for best results while the radio is used as a joystick. — [EdgeTX manual: USB Joystick (snippet only)](https://manual.edgetx.org/color-radios/model-settings/model-setup/usb-joystick); [EdgeTX joystick mapping for game developers (snippet only)](https://manual.edgetx.org/edgetx-how-to/joystick-mapping-information-for-game-developers)
- A Pocket user manual copy says to check that the transmitter is in Joystick mode in the EdgeTX USB settings. — [manuals.plus Pocket manual (snippet only)](https://manuals.plus/asin/B0DXPHC2TW)
- Retailer Rotor Village: radios such as the RadioMaster Pocket, T8L or TX15 connect over USB-C and are "recognized instantly as a joystick". — [Rotor Village blog (fetched)](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/)
- Oscar Liang, replying to a reader, called the Pocket "a pretty good choice, affordable and compact". His guide tells beginners to pick a sim-compatible ELRS 2.4 GHz radio. — [Oscar Liang FPV beginner guide (fetched)](https://oscarliang.com/fpv-drone-guide)
- **Korean prices, Pocket ELRS:**
  - 링크드론 (LINKDRONE): "라디오마스터 Pocket 포켓 차콜 버전 조종기 (ELRS, KC 인증 제품)", 129,000원. The main unit is not marked sold out. No KC certificate number is visible on the page. The same shop lists "Pocket Classic (CC2500, KC)" at 99,000원. — [링크드론 (fetched)](https://www.linkdrone.co.kr/shop/goods/goods_view.php?goodsno=100061774)
  - 엑스캅터 (xcopter): "Pocket Controller (모드 2 / ELRS)" 129,000원 and "Pocket Crush (ELRS)" 129,000원, both **품절** (sold out). CC2500 versions are 109,000원, also sold out. No KC mention. — [엑스캅터 라디오마스터 category (fetched)](https://xcopter.com/category/%EB%9D%BC%EB%94%94%EC%98%A4%EB%A7%88%EC%8A%A4%ED%84%B0/10404/)
  - 드론몰 (DRON MALL, (주)마이로봇): "라디오마스터 포켓 조종기 | ELRS, FCC (모드 2)" 129,000원, **SOLD OUT**. No KC statement; the product name says "FCC". — [드론몰 (fetched)](https://dronmall.com/product/%EB%9D%BC%EB%94%94%EC%98%A4%EB%A7%88%EC%8A%A4%ED%84%B0-%ED%8F%AC%EC%BC%93-%EC%A1%B0%EC%A2%85%EA%B8%B0-elrs-fcc-%EB%AA%A8%EB%93%9C-2/9668/)
  - 퍼스트알씨 (1strc): Pocket ELRS 투명, 129,000원. — [퍼스트알씨 (snippet only)](https://m.1strc.co.kr/product/%ED%8F%AC%EC%BC%93pocket-%EC%A1%B0%EC%A2%85%EA%B8%B0-%EB%8B%A8%ED%92%88-%EB%9D%BC%EB%94%94%EC%98%A4%EB%A7%88%EC%8A%A4%ED%84%B0radiomaster-elrs-%ED%83%91%EC%9E%AC-%ED%88%AC%EB%AA%85/12310/display/1/)
  - 수성RC: Pocket (ELRS) in 차콜/클리어쉘, 129,000원, shipping 3,500원. — [수성RC (snippet only)](https://susungrc.com/product/%EB%9D%BC%EB%94%94%EC%98%A4%EB%A7%88%EC%8A%A4%ED%84%B0-pocket-%EC%A1%B0%EC%A2%85%EA%B8%B0-elrs/2385/)
- No 쿠팡, 다나와, 11번가 or 네이버 스마트스토어 listing for the Pocket came up in two searches. — [search returned only RC-shop pages; e.g. 퍼스트알씨 (snippet only)](https://m.1strc.co.kr/product/%ED%8F%AC%EC%BC%93pocket-%EC%A1%B0%EC%A2%85%EA%B8%B0-%EB%8B%A8%ED%92%88-%EB%9D%BC%EB%94%94%EC%98%A4%EB%A7%88%EC%8A%A4%ED%84%B0radiomaster-elrs-%ED%83%91%EC%9E%AC-%ED%88%AC%EB%AA%85/12310/display/1/)

**RadioMaster Boxer and Zorro (Korean prices only; maker pages not checked)**
- 엑스캅터: "BOXER 클리어쉘 버전 조종기 (ELRS)" 295,000원, sold out. "Boxer Crush 조종기 (ELRS)" 355,000원, sold out. "ZORRO 조종기 (배터리 포함)" 199,000원, version not stated, not marked sold out. — [엑스캅터 라디오마스터 category (fetched)](https://xcopter.com/category/%EB%9D%BC%EB%94%94%EC%98%A4%EB%A7%88%EC%8A%A4%ED%84%B0/10404/)
- 링크드론: Radiomaster Zorro (battery included, **CC2500 module**) 199,000원. No Boxer listed. — [링크드론 (fetched)](https://www.linkdrone.co.kr/shop/goods/goods_view.php?goodsno=100061774)

**BETAFPV LiteRadio 3**
- Maker states: "USB Joystick support for most practice simulators". It names VelociDrone, Liftoff, TRYP, DRL, DCL and DJI. Protocols: ExpressLRS 2.4G, or FrSky D8/D16 and Futaba S-FHSS. ELRS power 25/50/100 mW. Mode 2 and Mode 1 are sold as separate variants. USB Type-C. Built-in 2000 mAh 1S battery. $32.99. The FAQ covers PCs with AMD processors that fail to connect (flash the latest firmware). No FCC/CE/KC statement. — [BETAFPV LiteRadio 3 (fetched)](https://betafpv.com/products/literadio-3-radio-transmitter)
- The Cetus X kit page (which bundles LiteRadio 3) gives a different version of the caveat. It says the radio "isn't compatible with Windows 11/Windows 10 systems running on AMD CPUs", and that sim connection may require you to "revert it to the ELRS 2.0 firmware". This conflicts with the LiteRadio 3 page's advice to flash the latest firmware. — [BETAFPV Cetus X FPV Kit (fetched)](https://betafpv.com/products/cetus-x-fpv-kit)
- No Korean retailer price was found in two searches. Only EU/NZ shops came up. — [search; e.g. FPV24 (snippet only)](https://www.fpv24.com/en/betafpv/betafpv-lite-radio-3-radio-remote-control-elrs)

**BETAFPV LiteRadio 4 / 4 Neo / 4 SE**
- Maker spec: ExpressLRS 2.4G, 25/50/100 mW. Mode 2 and Mode 1 variants. Potentiometer gimbals. LiteRadio 4 has "Bluetooth and USB-cable connection"; the Neo has "USB-cable connection" only. "Bluetooth Joystick Mode connects wirelessly to FPV simulators on PC, mobile, or tablet" (LiteRadio 4 only). Weight about 210 g. Prices: LiteRadio 4 $44.99, Neo $32.99. The page does not use the words "USB HID". No FCC/CE/KC statement. — [BETAFPV LiteRadio 4 (fetched)](https://betafpv.com/products/literadio-4-radio-transmitter)
- The LiteRadio 4 SE manual says it connects to computers, phones and tablets for sims. In USB-cable mode it appears as a "BETAFPV Joystick", and it also supports Bluetooth joystick mode. — [manuals.plus LiteRadio 4 SE (snippet only)](https://manuals.plus/m/9587a8b3ac650109aae28ce014fda48776078d3e4afd7e082be0734b7d74fc5c)
- No Korean retailer listing found.

**TBS Tango 2 / Tango 2 Pro**
- TBS manual: plug in USB-C and a menu appears where you can activate USB joystick mode, which "will work with the most common simulators". — [TBS Tango 2 manual (snippet only)](https://www.team-blacksheep.com/media/files/tbs-tango2-manual.pdf)
- TBS support article: choose "[USB Joystick (HID)]" with the scroll wheel. — [TBS support: Tango2 for Velocidrone (snippet only)](https://team-blacksheep.freshdesk.com/support/solutions/articles/4000152741-setting-up-the-tango2-for-velocidrone-or-other-simulators)
- Protocol: TBS Crossfire built in, not ELRS. Korean price: 드론파일럿, "TBS TANGO 2 PRO 탱고2 프로 크로스파이어", 322,000원, sold as a 해외직구 (overseas direct-purchase) item. — [드론파일럿 (snippet only)](https://dpilot.co.kr/product/tbs-tango-2-pro-%ED%83%B1%EA%B3%A02-%ED%94%84%EB%A1%9C-%ED%81%AC%EB%A1%9C%EC%8A%A4%ED%8C%8C%EC%9D%B4%EC%96%B4/220/)

**Jumper T-Lite V2**
- A UK retailer lists it as "Discontinued: Jumper T-Lite V2 4-in-1 Multi-Protocol / ELRS 2.4Ghz". — [Flying Tech (snippet only)](https://www.flyingtech.co.uk/product/jumper-t-lite-v2-4-in-1-multi-protocol-elrs-2-4ghz)
- Retailer listings describe it as OpenTX-based, with Hall gimbals, a JP4IN1 multi-protocol or ELRS module, "Mode 2", and PC simulator use. — [FPV Faster listing (snippet only)](https://www.fpvfaster.com.au/products/jumper-t-lite-v2-radio-controller-transmitter-hall-sensor-gimbals-opentx-jp4in1-multi-protocol-elrs-module-mode-2-new-2022)
- No Korean listing found.

**Radios bundled in ready-to-fly kits**
- Cetus X FPV Kit includes the LiteRadio 3 (ELRS 2.4G or FrSky). BETAFPV: "LiteRadio 3 is available to play FPV simulators like DRL/DCL/Uncrashed/Liftoff". — [BETAFPV Cetus X FPV Kit (fetched)](https://betafpv.com/products/cetus-x-fpv-kit)
- The Cetus FPV Kit includes the LiteRadio 2 SE and VR02 goggles. — [BETAFPV Cetus FPV Kit (snippet only)](https://betafpv.com/products/cetus-fpv-kit)

**Wireless alternatives (optional)**
- ExpressLRS radios can act as a Bluetooth joystick: select "BLE Joystick" in the ELRS Lua script. — [Oscar Liang: ELRS Bluetooth joystick (snippet only)](https://oscarliang.com/expresslrs-bluetooth-joystick/)
- USB ELRS receiver dongles such as the "Squid Stick" also exist. — [GetFPV Squid Stick (snippet only)](https://www.getfpv.com/accessories/flight-simulators/squid-stick-wireless-usb-simulator-dongle-elrs-2-4ghz.html)

### Inferences
- In Korea, the price of the Pocket ELRS is effectively uniform at 129,000원 across 링크드론, 엑스캅터, 드론몰, 퍼스트알씨 and 수성RC. Stock is patchy: three of the fetched or snippet listings were sold out on 2026-11-11, and 링크드론 was not marked sold out.
- Buy the **ELRS** version, not CC2500. Both work as sim joysticks. But beginner whoops sold today are mostly ELRS (Cetus X Betaflight version and Meteor75 Pro are ELRS), so an ELRS radio can later bind directly to an ELRS BNF whoop. The CC2500 Pocket or Zorro would suit only FrSky-type receivers, such as the FrSky D8 Cetus versions.
- The Tango 2 is a poor fit for this user. It costs 322,000원 as a 해외직구 item and uses Crossfire, so most ELRS whoops would need a receiver change. The Boxer is shown only as sold out in Korea.
- LiteRadio 3 or 4 is the cheapest sim radio by list price ($32.99–$44.99). But there is no confirmed Korean domestic stock, its gimbals are potentiometer type (LR4 stated), and LR3 has a documented AMD-PC connection caveat. It makes most sense when it comes bundled in a kit.
- All radios here present to a **PC** (or Mac, phone or tablet for LR4's Bluetooth mode) as a joystick. Nothing found says they work with game consoles. If the user plays Call of Duty only on a console, they would still need a PC for this path.

### Gaps
- No manufacturer page for RadioMaster Pocket, Boxer or Zorro was found that itself states "USB joystick / HID". The confirmation is via EdgeTX documentation (snippet), a manual copy (snippet) and retailers. The Boxer and Zorro maker pages were not checked.
- Only 링크드론 says KC for the Pocket, and only in product titles; no certificate number is visible. No KC or 적합성평가 status was found for BETAFPV radios, the TBS Tango 2 or the Jumper T-Lite. I did not look up the 국립전파연구원 적합성평가 database.
- No 쿠팡, 11번가, 다나와 or 스마트스토어 prices were retrievable. Searches surfaced only RC-shop sites.
- Not checked: whether an ELRS Zorro version is sold in Korea, and whether the Tango 2 supports Mode 2 or switchable gimbals.
- Not verified: the rules for 해외직구 of radio transmitters (e.g., whether 전파법's personal-use exemption from 적합성평가 applies).

## Q2. Can these transmitters or a gamepad be used in Bodycam's drone mode? (Only what a source states)

### Takeaway
No source found says an RC transmitter or USB-joystick radio works in Bodycam. Third-party guides say a gamepad can fly the drone only through Steam Input remapping, without official full controller support. A June 2024 article said controllers were "not viable" and that the developers prioritise mouse and keyboard on PC. Another researcher covers Bodycam controls in depth.

### Cited Findings
- Gamepressure (11 June 2024, days after the 7 June 2024 Early Access release): "it is not viable to play Bodycam using controllers". Gamepads work for menu scrolling; the gamepad settings are unfinished and mostly can't be rebound. The developers "have very clearly confirmed that the weight is put on keyboard and mouse support" and focus on PC, leaving consoles behind "at least for now". The article does not mention the drone or RC transmitters. — [Gamepressure (fetched)](https://www.gamepressure.com/newsroom/controller-support-in-bodycam-explained/za6ef9)
- ExitLag guides (undated, from a network-tool vendor) say there is no official native controller support on Steam and you rely on Steam Input remapping. They recommend an Xbox or standard gamepad if you fly the drone a lot. They say the drone has an easier "ANGL" mode and an "FPV Acro Mode". — [ExitLag: Bodycam FPV (snippet only)](https://www.exitlag.com/blog/bodycam-fpv/); [ExitLag: controller (snippet only)](https://www.exitlag.com/blog/can-you-play-bodycam-with-a-controller/)
- SteamInputDB hosts community controller layouts for the game. — [SteamInputDB app 2406770 (snippet only)](https://www.steaminputdb.com/app/2406770)
- For general FPV sim training, Oscar Liang says to avoid Xbox controllers and keyboards. — [Oscar Liang (fetched)](https://oscarliang.com/fpv-drone-guide)
- Rotor Village explains why: "Gaming controllers have spring-loaded sticks that snap back to the center on both sides", whereas "A real FPV radio has a 'friction' throttle on the left side that stays exactly where you put it." — [Rotor Village (fetched)](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/)

### Inferences
- The recommended practice radio should be justified by dedicated FPV simulators, not by Bodycam. If Bodycam turns out not to accept a USB-joystick radio, the radio is still the right tool for real FPV skills, because gamepads lack the non-centring throttle.
- Bodycam is PC-focused per Gamepressure, so a console-only player could not use it or the sim radios. Whether the user plays CoD on PC or console is unknown.

### Gaps
- No developer statement or tested report was found on generic HID joysticks or EdgeTX radios in Bodycam, through Steam Input or otherwise. Both 2024 sources may be out of date after later Early Access patches; defer to the Bodycam-controls researcher.

## Q3. Beginner indoor FPV kits that share the same radio: Korean availability and price, flight time, weight

### Takeaway
BETAFPV's tiny whoops weigh roughly 30–55 g, far under 250 g, and fly about 5–6.5 minutes per 1S battery. The ELRS versions bind to the same ELRS radio the user practises with. But I found no Korean domestic retail listing for a complete Cetus kit or Meteor75 Pro. Korean shops show mainly parts, plus one sold-out Meteor65 PRO semi-assembled kit, and the official BETAFPV listings were mostly "Sold Out" on 2026-11-11. Practically, the buyer faces 해외직구 or a hunt through Korean shops' Meteor categories.

### Cited Findings
- **Cetus X FPV Kit (all-in-one):**
  - Contents: Cetus X drone, LiteRadio 3 (ELRS 2.4G or FrSky), VR03 goggles with DVR (no microSD included), 4 × BT2.0 450 mAh 1S batteries, charger and voltage tester, spare props, tools and bag.
  - Flight time 5 min per battery.
  - Modes: Betaflight FC version has Angle/Horizon/Air/Turtle. Cetus FC version has N/S/M/Turtle with SLOW/MID/FAST and barometer position hold in N mode. BETAFPV calls the Cetus FC version "easier and more suitable for initial pilots".
  - Price $309.99 regular, $259.99 sale (Cetus FC); $239.99 (Betaflight FC). Marked "Sold Out".
  - [BETAFPV Cetus X FPV Kit (fetched)](https://betafpv.com/products/cetus-x-fpv-kit)
  - Note: my page extraction returned a weight of "1499.7 g" for the kit page. That is clearly not the drone (likely a package figure or parse error), so use the drone-page figure below.
- **Cetus X drone:** 55 g (the page does not say whether the battery is included). 5 min flight. BT2.0 450 mAh 1S, with 550 mAh recommended for longer flights. ELRS 2.4G (Betaflight FC) or FrSky D8 (Cetus FC). $149.99 regular, variants from $64.99 to $149.99, all sold out. BETAFPV calls it "a primary choice for beginners who want to get advanced flight skills". — [BETAFPV Cetus X quadcopter (fetched)](https://betafpv.com/products/cetus-x-brushless-quadcopter)
- **Meteor75 Pro (BNF, ELRS):** 30.5 g (battery inclusion unstated). Flight time 6:30, with the LAVA II 1S 580 mAh listed next to it. 1S only. ELRS 2.4 GHz serial receiver. Analog C03 camera with 400 mW 5.8 GHz VTX. BNF $109.99. "RTF Kit" $208.99, listed as including batteries, charger, props and tools. All variants "Sold Out". Described as "ideal for both indoor and outdoor FPV racing and freestyle", with the Matrix FC "ideal for beginners". — [BETAFPV Meteor75 Pro (fetched)](https://betafpv.com/products/meteor75-pro-brushless-whoop-quadcopter)
- **Meteor75 Pro HD FPV Kit:** goggles, radio and carry bag included, $318.99, shown as sold out on a collection page. — [BETAFPV Meteor75 Pro HD FPV Kit (snippet only)](https://betafpv.com/products/meteor75-pro-hd-fpv-kit)
- **Cetus / Cetus Lite / Cetus Pro kits:**
  - The Cetus FPV Kit (LiteRadio 2 SE and VR02 goggles) was $159.99 regular, $149.99 sale. — [BETAFPV Cetus FPV Kit (snippet only)](https://betafpv.com/products/cetus-fpv-kit)
  - The Cetus Lite kit is quoted at 4–5 min per charge. — [Fly In Tunnel listing (snippet only)](https://flyintunnel.com/products/betafpv-cetus-lite-fpv-kit)
  - A Korean article put the Cetus Pro kit (drone, transmitter and FPV goggles) at $189.99 (약 26만원) and called it aimed at beginners. — [더드라이브 (snippet only)](https://www.thedrive.co.kr/news/newsview.php?ncode=1065586144455570)
- **Korean shops:**
  - 수성RC's Meteor65 category shows "BETAFPV Meteor65 PRO 반조립버전 (ELRS, DJI O4 Air Unit)" at 149,000원, **품절**. The rest of the category is parts: Meteor65/75 canopies 11,500원, Meteor65 PRO frame kit 9,700원, 0802SE motors 67,500원, a 1S 6-port BT2.0 charging hub 14,000원; shipping 3,500원. — [수성RC Meteor65 category (fetched)](https://susungrc.com/category/meteor65/354/)
  - 엑스캅터's "FPV 드론 키트" category (page 1 of 7) shows "BETAFPV 파보 펨토 드론키트" (Pavo Femto, semi-assembled, ELRS receiver plus DJI O4 Air Unit Lite) at 186,000원, but no Cetus or Meteor complete kit. A Meteor sub-category with 10 items exists but was not inspected. — [엑스캅터 FPV 드론 키트 (fetched)](https://xcopter.com/category/fpv-%EB%93%9C%EB%A1%A0-%ED%82%A4%ED%8A%B8/5961/)
  - Cetus kit pages in Korean exist on rcdrone.top, an overseas store. Prices are in USD, e.g. Cetus Lite FPV kit $158.95. — [rcdrone.top/ko Cetus Lite (snippet only)](https://rcdrone.top/ko/products/betafpv-cetus-lite-kit-fpv-kit-rc-quadcpoter-drone)
- Before a first flight, BETAFPV says its drones are configured to arm on AUX1 by default, so you must map a switch to AUX1 on the radio. — [BETAFPV support (snippet only)](https://support.betafpv.com/hc/en-us/articles/900004741583)

### Inferences
- Weight: every whoop found (Meteor75 Pro 30.5 g, Cetus X 55 g, both possibly without battery; a 1S 450–580 mAh pack adds tens of grams) is far below the 250 g threshold.
- Radio sharing: a Pocket ELRS (or LiteRadio 3/4 ELRS) used in the simulator can bind directly to an ELRS BNF whoop such as the Meteor75 Pro ELRS or the Cetus X Betaflight/ELRS. So "sim radio first, whoop later" avoids buying a second radio. Goggles must be bought separately with a BNF whoop. The Meteor75 Pro is analog 5.8 GHz, so it needs analog goggles, which were not priced in this pass.
- Two realistic Korean purchase paths:
  - (a) Pocket ELRS from a Korean shop (129,000원) now, then an ELRS BNF whoop plus analog goggles later. Korean stock of complete whoops is uncertain, so 해외직구 is likely.
  - (b) An all-in-one kit (Cetus X / Cetus Pro, about $190–$310 list) bought abroad. Its bundled radio doubles as a sim controller, but it is a cheaper potentiometer-class radio with the AMD-PC caveat.
- DJI O4-based whoops sold in Korea (Meteor65 PRO O4, Pavo Femto) need DJI digital goggles. That is a much more expensive goggle system than a beginner kit, and less suitable as a first purchase.

### Gaps
- No Korean domestic retail price or stock was found for any complete Cetus kit, for the Meteor65/75 BNF (analog), or for analog FPV goggles (e.g., BETAFPV VR03). 쿠팡, 11번가, 다나와 and 스마트스토어 were not retrievable.
- Not checked: whether the Meteor75 Pro or Cetus weights include the battery, and the exact all-up weight.
- Not researched: Korean legal status of 5.8 GHz analog video transmitters (VTX power such as 400 mW, and whether a 아마추어무선 licence or 적합성평가 applies). This could matter for a Korean report and should be flagged as unverified.

## Q4. A staged learning plan used by educators: sim hours before the first real flight, starting modes, first drills

### Takeaway
Reputable guides converge on **roughly 3 hours as a bare minimum and about 10 to 15 hours of simulator time** before a first real flight. They advise using a real radio rather than a gamepad, starting on a tiny whoop indoors, and expecting many crashes. Oscar Liang stresses learning Acro (manual) mode in the sim. Other beginner guides say to fly the real drone in Angle (self-level) mode until comfortable. The two are compatible: Acro in the sim, an assisted mode for the first real hops.

### Cited Findings
- **Oscar Liang** (guide dated 19 April 2025):
  - Hours: the body says "ideally at least 5 to 10 hours" in a sim before buying or building a first drone; the TL;DR says "Dedicate 10+ hours to simulator training". Also aim for "100+ crashes under your belt" before buying a more expensive model.
  - Modes: "it's crucial to learn Acro Mode (aka manual mode)"; "Auto-level mode acts like a pair of crutches, helpful for balance but limiting in more dynamic situations". Betaflight's Acro Trainer mode can ease the transition. For the DJI Avata 2, "start in Normal Mode and spend plenty of time in simulators before attempting Manual Mode".
  - Sim goals: master the controls and build muscle memory; fly through gaps while avoiding obstacles; then basic freestyle (flips, rolls, split-S).
  - First drone and backup skills: "Tiny Whoop is great as your first drone". Line-of-sight skills "can help you regain control in an emergency".
  - Steps: (1) buy a sim-compatible ELRS radio, (2) download a sim, (3) log 10+ hours learning Acro, (4) buy an RTF drone or build one.
  - [Oscar Liang FPV guide (fetched)](https://oscarliang.com/fpv-drone-guide)
- **Rotor Village** (retailer blog, no author or date shown, refers to 2026):
  - The "3-Hour Rule": "Spend at least three hours in the simulator"; "By putting in just 10 to 15 hours in a simulator, you bridge the gap" between basic survival and basic control.
  - Drills: hover in one spot; fly through a single gate; readiness check before a first real flight is "a few consecutive laps without a major 'reset'".
  - Real radio, not gamepad: the throttle on a radio stays where you put it, while gamepad sticks spring back to centre.
  - [Rotor Village (fetched)](https://rotorvillage.ca/blog/why-every-fpv-beginner-should-start-with-a-simulator-and-a-real-radio/)
- **Unmanned Tech** blog: calibrate and bind with a failsafe that cuts throttle on signal loss, and "fly in angle mode until you are comfortable switching to acro". It recommends a forgiving indoor space with spare props and batteries. — [Unmanned Tech blog (snippet only)](https://blog.unmanned.tech/common-mistakes-fpv-drone-beginners-make-and-how-to-avoid-them/)
- **Flite Test**: fly line of sight first before jumping to FPV. — [Flite Test: Quad Basics (snippet only)](https://flitetest.com/articles/how-to-fly-a-drone-quad-basics)
- **Kit-side assisted modes:** the Cetus FC version offers N mode with barometer position hold, plus S/M modes and SLOW/MID/FAST speed. The Betaflight version offers Angle/Horizon/Air. — [BETAFPV Cetus X FPV Kit (fetched)](https://betafpv.com/products/cetus-x-fpv-kit)
- **Wider ranges:** search summaries show commercial blogs quoting 10–20, 15–30 or 40–60+ hours, often without citation. I treat these as unreliable. — [search result set incl. zbotic.in (snippet only)](https://zbotic.in/fpv-drone-simulator-training-best-apps-before-flying-real/)

### Inferences
A staged plan the report can propose, built from the sources above:
1. **Stage 0 (buy):** an ELRS Mode 2 radio that doubles as a USB joystick. In Korea the Pocket ELRS is 129,000원. Use it with a PC FPV simulator; sim choice and prices are covered by another researcher.
2. **Stage 1, sim basics (first ~3 h, Rotor Village minimum):** throttle control and hover in one spot, gentle forward flight, single gate passes. Oscar Liang would have this done in Acro.
3. **Stage 2, sim fluency (to ~10–15 h, Oscar Liang 5–10/10+ and Rotor Village 10–15):** consecutive laps without resets, flying through gaps around obstacles. Optionally, basic freestyle later.
4. **Stage 3, first real flight:** a sub-250 g tiny whoop indoors in an enclosed room. Map the arm switch (AUX1). Start in Angle (or Cetus N mode) for the first battery packs, then move to Acro as the sim habit transfers. Practise a little line-of-sight hovering as an emergency skill. Expect frequent crashes (Oscar Liang: 100+ before upgrading).
5. **Stage 4, outdoors:** only after indoor comfort, and only where legal (see Q5).
- For a user who prefers short at-home evening sessions: about 30–60 minutes per evening would reach the 10-hour mark in roughly 2–3 weeks. This is my arithmetic, not a source claim.

### Gaps
- No fetched source names "figure eights" as a drill. Joshua Bardwell and BETAFPV-official drill curricula were not retrieved: Bardwell's material is mostly video, and BETAFPV's own blog guide was not found.
- No primary educator source quantifies sim-to-real transfer. The hour figures are expert recommendations, not studies.

## Q5. Korean rules a beginner must know for a first real flight

### Takeaway
For a sub-250 g whoop flown **indoors in a room enclosed on all sides and above**, MOLIT's policy Q&A indicates **no flight approval is needed**, and indoor night flight with adequate lighting is fine. The item was seen via two search summaries of the MOLIT page; the page itself failed to load (redirect loop). Non-business drones of 2 kg or less also need no 기체신고 (device registration), per the same MOLIT page in summary. Combined with the coordinator's previously verified rule that ≤250 g needs no pilot certificate, an indoor whoop at home is the legally simplest first flight. Outdoor goggles-only flight raises the unresolved line-of-sight question.

### Cited Findings
- MOLIT policy Q&A: "사방ㆍ천장이 막혀있는 실내 공간에서의 비행은 승인을 필요로 하지 않습니다", and "적절한 조명장치가 있는 실내 공간이라면 야간에도 비행이 가능합니다". — [국토교통부 정책Q&A idx=584 (snippet only; page fetch failed with a redirect loop on two URLs)](https://www.molit.go.kr/USR/policyTarget/dtl.jsp?idx=584)
- Same MOLIT page, per summary: drones over 2 kg MTOW, and all business-use drones regardless of weight, must be registered with 한국교통안전공단 via 드론원스톱. Flying without displaying the registration number risks a fine of up to 1,000,000원 (항공안전법 제166조). — [국토교통부 정책Q&A idx=584 (snippet only)](https://www.molit.go.kr/USR/policyTarget/dtl.jsp?idx=584)
- A secondary summary cites 항공안전법 제122조 제1항 and 시행령 제24조 for the same 2 kg / business-use registration thresholds. — [nepla.ai 일문일답 (snippet only)](https://www.nepla.ai/wiki/it-정보-방송통신/로봇-드론/-일문일답-드론-구매-후-신고를-해야-하는-드론은-gy380o1e8rxk)
- Carried over from the coordinator brief (verified earlier in this conversation as of 2026-11-10; not re-fetched in this pass):
  - ≤250 g MTOW needs no pilot certificate; 250 g–2 kg needs only the free online 4종 course.
  - Regardless of weight, approval is needed in no-fly zones, within 9.3 km of airports, and above 150 m.
  - Night flight and beyond-visual-line-of-sight flight are prohibited without special approval.
  - Since 2026-09-17, unapproved flight in a no-fly zone is a criminal offence (up to 1 year or 10 million won).
  - Seoul treats the whole city as approval-required.
  - 한강드론장 at 광나루 is a free bookable flying field (rules last updated 2024).
  - No official source found settles whether goggles-only outdoor FPV counts as beyond visual line of sight.

### Inferences
- For this user (apartment-based, hobby at home after work), the first real flight is best framed as **indoors, in an enclosed room, with a sub-250 g whoop**. On the sources above that needs no certificate, no registration and no flight approval. Outdoor flight in Seoul brings in approval requirements and the unresolved goggles/line-of-sight question. The low-friction outdoor option is a designated field such as 한강드론장, ideally with a spotter. Whether a spotter satisfies the visual-line-of-sight rule is unconfirmed.

### Gaps
- The MOLIT page could not be loaded directly (redirect loop), so exact wording and date are unconfirmed beyond the search snippets.
- No source addresses whether pilot rules such as the line-of-sight requirement apply to indoor goggle flight. The MOLIT text found covers only approval.
- Korean radio-law status of 5.8 GHz analog VTXs and of 해외직구 radios was not verified (see Q1 and Q3 gaps).
