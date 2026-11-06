# SPY (S&P 500) vs QQQ (Nasdaq-100): composition, concentration, overlap, and ETF product facts (as of early Nov 2026)

Method note for the report writer: where Invesco's site blocked automated download (HTTP 406), QQQ weights come from stockanalysis.com (data vendor Finnhub, "Updated Nov 4, 2026") and an undated Zacks table. Figures labelled "computed" are my own arithmetic on the cited primary files (SSGA SPY daily holdings, Nasdaq's official constituent list). They are not published figures. To map GICS sub-industries I used Wikipedia's S&P 500 list. As a check, the SPY sector weights it produced matched SSGA's official Nov 4 sector breakdown within ±0.04 pp (IT 36.63% computed vs 36.67% official).

## 1. Top 10 holdings, combined top-10 weight, and number of holdings

### Takeaway
As of Nov 4, 2026 SPY's top 10 were 37.5% of a 504-stock fund, and QQQ's top 10 were 46.8% of a 101-security index. QQQ holds only slightly more of the three giants than SPY does (Apple 8.26% vs 7.69%, Nvidia 7.81% vs 7.30%, Microsoft 6.68% vs 6.22%). QQQ's extra concentration sits in the next tier: Micron 4.01%, AMD 3.57%, Tesla 3.28%, Walmart 2.81% and SpaceX 2.61%. SPY's next tier is Eli Lilly, Berkshire and JPMorgan.

### Cited Findings
- **SPY top 10, Nov 4, 2026 (SSGA daily holdings file "As of 04-Nov-2026"):** AAPL 7.690%, NVDA 7.302%, MSFT 6.222%, AMZN 3.937%, GOOGL 2.556%, AVGO 2.334%, META 2.094%, GOOG 2.059%, LLY 1.710%, TSLA 1.637%. Next five: BRK.B 1.626%, JPM 1.411%, MU 1.354%, AMD 1.203%, V 1.121% — [SSGA SPY daily holdings (xlsx)](https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx)
- The SSGA SPY product page shows the same list ("Fund Top Holdings as of Nov 04 2026": Apple 178,914,348 shares, 7.69%; Nvidia 296,675,198 shares, 7.30%; Microsoft 91,031,295 shares, 6.22%). It shows **504 fund holdings**, and **503** under "Index Statistics as of Nov 04 2026" — [SSGA SPY page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-500-etf-trust-spy)
- **SPY top-10 combined, Nov 4: 37.54%** (computed by summing the SSGA file). Counting Alphabet as one company (GOOGL+GOOG = 4.61%), the top 10 companies including BRK.B come to about 39.2% (computed) — [SSGA SPY daily holdings](https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx)
- **SPY top 10, Sep 30, 2026 fact sheet:** NVDA 8.38%, AAPL 7.37%, MSFT 5.77%, AMZN 3.71%, GOOGL 3.06%, AVGO 2.53%, GOOG 2.46%, META 2.42%, MU 1.82%, TSLA 1.52%. Combined 39.04% (computed). Number of holdings 504 — [SSGA SPY fact sheet, 9/30/2026](https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-spy.pdf)
- **QQQ top 25, "Updated Nov 4, 2026" (data source Finnhub):**
  - Top 10: AAPL 8.26%, NVDA 7.81%, MSFT 6.68%, AMZN 4.65%, MU 4.01%, AMD 3.57%, TSLA 3.28%, META 3.03%, WMT 2.81%, GOOGL 2.75%.
  - Ranks 11–25: SPCX (Space Exploration Technologies) 2.61%, GOOG 2.57%, AVGO 2.51%, COST 2.07%, CSCO 1.83%, PLTR 1.77%, INTC 1.37%, AMAT 1.31%, TXN 1.27%, PANW 1.27%, LRCX 1.24%, NFLX 1.24%, AMGN 1.16%, CRWD 1.10%, LIN 1.08%.
  - The page gives "Top 10 Percentage 46.84%", "Total Holdings 104" (which includes cash and futures lines), and Alphabet at 5.32% combined — [stockanalysis.com QQQ holdings](https://stockanalysis.com/etf/qqq/holdings/)
- **Nasdaq-100 index top 10, Sep 30, 2026:** NVDA 8.36%, AAPL 7.38%, MSFT 5.78%, MU 5.04%, AMD 4.19%, AMZN 4.08%, META 3.27%, GOOGL 3.07%, GOOG 2.86%, TSLA 2.83%. Combined 46.86% (computed). "Securities: 101" — [Nasdaq-100 fact sheet (FS_NDX), data as of 09/30/2026](https://indexes.nasdaqomx.com/docs/FS_NDX.pdf)
- **Nasdaq's official constituent list (start of day Nov 5, 2026) has 101 symbols.** Among them are SPCX (SpaceX), WMT, HONA, ALAB, CRWV, NBIS, RKLB, SNDK, LITE and MRNA — [Nasdaq Global Indexes, NDX weighting/constituents](https://indexes.nasdaqomx.com/Index/Weighting/NDX)
- **Zacks QQQ table (holdings date not shown; weights closely match the 9/30/2026 index fact sheet).** It lists 101 stocks plus three non-stock lines: cash (USD 0.24%), December 2026 Nasdaq-100 futures ("NQZ6", 0.10%) and futures collateral cash (0.10%). It shows NVDA 8.43%, AAPL 7.28%, MSFT 5.75%, MU 5.01%, AMD 4.27% and SPCX 2.81% — [Zacks QQQ holdings](https://www.zacks.com/funds/etf/QQQ/holding)

### Inferences
- **The three giants are weighted almost the same in both funds.** Apple, Nvidia and Microsoft are 21.2% of SPY and 22.8% of QQQ (Nov 4). So "QQQ is a bigger Nvidia bet" is barely true for single names. The real difference starts at rank 4: QQQ holds about 3x SPY's weight in Micron and AMD, 2x in Tesla, and has 2.6% in SpaceX, which SPY does not own.
- **Counting Alphabet as one company,** QQQ's top 10 is about 49.4% vs about 39.2% for SPY (computed).
- **Weights shifted sharply in October 2026.** In SPY, Nvidia went from 8.38% to 7.30% and Micron from 1.82% to 1.35%. Quoting 9/30 fact sheets would overstate today's chip weights. Weights after the Nov 5 selloff are lower still.

### Gaps
- Invesco's own QQQ holdings file and fact sheet could not be retrieved (HTTP 406 to automated requests). QQQ weights therefore come from secondary vendors (stockanalysis/Finnhub, Nov 4; Zacks, undated).
- No post-Nov 5 holdings were available.

## 2. Sector weights: S&P 500 by GICS, Nasdaq-100 by ICB and approximate GICS

### Takeaway
SPY on Nov 4, 2026 was 36.7% Information Technology plus 8.6% Communication Services (45.3% together), with semiconductors about 15.5% (computed). The Nasdaq-100 is 68.0% "Technology" under Nasdaq's own ICB classification (Sep 30). On an approximate GICS basis QQQ is about 58% IT and 11% Communication Services, with semiconductors about 30%, roughly double SPY's. QQQ holds essentially no financials, against 12.6% in SPY.

### Cited Findings
- **SPY GICS sectors, "Fund Sector Breakdown as of Nov 04 2026":** IT 36.67%, Financials 12.56%, Health Care 10.36%, Consumer Discretionary 9.48%, Communication Services 8.60%, Industrials 8.12%, Consumer Staples 5.05%, Energy 3.49%, Utilities 2.07%, Real Estate 1.85%, Materials 1.76%. The index breakdown on the same date has IT 36.64% and Industrials 8.13%; other sectors are identical — [SSGA SPY page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-500-etf-trust-spy)
- **SPY GICS sectors, Sep 30, 2026:** IT 39.71%, Financials 11.40%, Communication Services 9.95%, Health Care 9.26%, Consumer Discretionary 8.60%, Industrials 8.05%, Consumer Staples 4.37%, Energy 3.40%, Utilities 1.88%, Real Estate 1.70%, Materials 1.70% — [SSGA SPY fact sheet 9/30/2026](https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-spy.pdf). The SPYM fact sheet shows the same weights — [SSGA SPYM fact sheet 9/30/2026](https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-spym.pdf)
- **Nasdaq-100 ICB industries, Sep 30, 2026 (weight, number of securities):** Technology 68.01% (47), Consumer Discretionary 15.14% (15), Telecommunications 5.91% (5), Health Care 3.78% (9), Industrials 2.82% (12), Consumer Staples 1.73% (5), Basic Materials 1.16% (2), Utilities 1.01% (4), Energy 0.44% (2), Financials 0.00%, Real Estate 0.00%. The index "does not contain securities of financial companies" — [Nasdaq-100 fact sheet](https://indexes.nasdaqomx.com/docs/FS_NDX.pdf)
- **SPY semiconductors, Nov 4 (computed): 15.46%.** That is GICS "Semiconductors" 14.20% plus "Semiconductor Materials & Equipment" 1.25%. Main names: NVDA 7.30%, AVGO 2.33%, MU 1.35%, AMD 1.20%, AMAT 0.44%, INTC 0.44%, TXN 0.43%, LRCX 0.42%, ADI 0.30%, KLAC 0.30%, QCOM 0.28%, MRVL 0.21%; the rest are each under 0.11% — computed from [SSGA SPY holdings](https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx) with sub-industry tags from [Wikipedia S&P 500 list](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
- **QQQ semiconductors (computed, GICS basis):**
  - **About 29.7% on Nov 4.** This uses the Nov 4 top-25 weights plus the Zacks tail rescaled to fit. It counts ARM, ASML and Astera Labs as semis.
  - Main names: NVDA 7.81%, MU 4.01%, AMD 3.57%, AVGO 2.51%, INTC 1.37%, AMAT 1.31%, TXN 1.27%, LRCX 1.24%, plus KLAC, MRVL, ADI, QCOM, ASML, ARM, TER, MPWR, ALAB, NXPI and MCHP.
  - The earlier (about end-September) Zacks snapshot gives 33.8%.
  - Sources: [stockanalysis QQQ holdings](https://stockanalysis.com/etf/qqq/holdings/), [Zacks QQQ holdings](https://www.zacks.com/funds/etf/QQQ/holding), [Wikipedia S&P 500 list](https://en.wikipedia.org/wiki/List_of_S%26P_500_companies)
- **QQQ approximate GICS sectors, Nov 4 (computed, same sources):**
  - IT about 58.2%, Communication Services about 11.2%, Consumer Discretionary about 11.2%, Consumer Staples about 6.7%, Health Care about 4.0%, Industrials about 3.3%.
  - SpaceX (2.6%) is left unclassified.
  - Materials about 1.1%, Utilities about 1.1%, Energy about 0.5%, Financials about 0.2%.
  - The 15 non-S&P names were assigned sectors by hand (e.g., ARM/ASML/SHOP to IT, MELI/PDD to Consumer Discretionary).

### Inferences
- **Tech plus communication services:** about 69% of QQQ vs 45% of SPY. **Defensive and value sectors are mostly absent from QQQ:** financials about 0.2% vs 12.6%, health care about 4% vs 10.4%, energy about 0.5% vs 3.5%.
- **Excluding Nvidia, QQQ's chip weight is about 22% vs about 8% for SPY, nearly 3x.** This tier (Micron, AMD, Broadcom, Intel, the equipment makers Applied Materials, Lam and KLA, and Texas Instruments) drives QQQ's higher beta in chip selloffs.
- **ICB "Technology" (68%) is not comparable with GICS "IT".** ICB Telecommunications holds only 5 securities at 5.91%, so Alphabet (about 5.9%) and Meta (about 3.3%) cannot be there. They appear to sit inside ICB Technology. GICS puts both in Communication Services.

### Gaps
- Invesco's official QQQ GICS sector breakdown could not be retrieved.
- Neither S&P DJI nor Nasdaq publishes a semiconductor sub-sector weight in the fact sheets reviewed. All semis figures are my own computations.
- SpaceX's official GICS and ICB classifications were not verified.

## 3. How much SPY and QQQ overlap by weight

### Takeaway
About 52.8% of SPY's weight (86 stocks) is in Nasdaq-100 members. About 93% of QQQ's weight is in S&P 500 members. The 15 Nasdaq-100 stocks outside the S&P 500 (SpaceX 2.6%, Shopify, ASML, Arm, MercadoLibre, CoreWeave, Nebius, etc.) total about 7% of QQQ. The "sum of the smaller weight" overlap is about 52.7%. Nearly every shared stock carries more weight in QQQ than in SPY, so QQQ is in effect a reweighted subset of SPY.

### Cited Findings
- **Count of shared stocks (computed):** 86 of the 101 Nasdaq-100 securities (Nasdaq list, Nov 5) are SPY holdings (SSGA file, Nov 4). Their combined weight in SPY is **52.79%** — [Nasdaq NDX constituents](https://indexes.nasdaqomx.com/Index/Weighting/NDX); [SSGA SPY holdings](https://www.ssga.com/us/en/intermediary/library-content/products/fund-data/etfs/us/holdings-daily-us-en-spy.xlsx)
- **The 15 Nasdaq-100 members not in SPY (computed):** ALAB, ALNY, ARM, ASML, CCEP, CRWV, FER, MELI, MSTR, NBIS, PDD, RKLB, SHOP, SPCX, TRI — same sources.
- **Their QQQ weights:**
  - Nov 4 estimates: SPCX 2.61%, SHOP about 0.80%, ASML about 0.76%, ARM about 0.58%, MELI about 0.37%, ALAB about 0.26%, MSTR about 0.25%, NBIS about 0.25%, PDD about 0.22%, CCEP about 0.19%, RKLB about 0.19%, CRWV about 0.18%, FER about 0.17%, TRI about 0.16%, ALNY about 0.13%.
  - Total about 7.1%, so **about 92.9% of QQQ is in S&P 500 members**.
  - In the Zacks snapshot alone the non-S&P share is 7.09% and the S&P share 92.33%, with about 0.44% in cash and futures.
  - Sources: [stockanalysis QQQ holdings](https://stockanalysis.com/etf/qqq/holdings/); [Zacks QQQ holdings](https://www.zacks.com/funds/etf/QQQ/holding)
- **Sum-of-minimum-weights overlap (computed): about 52.7%** using the Nov 4 QQQ weights. Using the Zacks snapshot instead it is 51.8%. Same sources.
- **SpaceX entered the Nasdaq-100 under the new Fast Entry rule:**
  - It joined on July 7, 2026 — [Motley Fool, Jul 6, 2026](https://www.fool.com/investing/2026/07/06/spacex-joins-the-nasdaq-100-on-july-7-here-is-what/)
  - That was less than a month after its IPO — [RTTNews](https://www.rttnews.com/3663388/spacex-joins-nasdaq-100-less-than-a-month-after-going-public.aspx?type=corp)
  - Its weight was reported to rise to 2.82% after the September quarterly rebalance — [Business Today, Sep 20, 2026](https://www.businesstoday.in/markets/story/spacex-weight-in-nasdaq-100-to-jump-to-2-82-following-quarterly-index-rebalance-report-556678-2026-09-20). That matches the 2.81% in the Zacks table.
- **S&P Dow Jones Indices refused to fast-track mega-IPOs into the S&P 500.** In June 2026 it kept its seasoning and financial-viability rules, so SpaceX is not yet eligible — [Axios, Jun 4, 2026](https://axios.com/2026/06/04/musk-spacex-ipo-sp-investors); [ThinkAdvisor/Bloomberg, Jun 5, 2026](https://www.thinkadvisor.com/amp/2026/06/05/spacex-other-mega-ipos-denied-fast-index-entry-by-sp/). Search summaries of this coverage say S&P kept its 12-month seasoning period and rejected cutting it to six months. That detail was not checked against S&P's own announcement.

### Inferences
- **Owning both funds mostly doubles up on about 86 stocks.** About 93% of QQQ's dollars go to S&P 500 stocks, and most of those are weighted more heavily in QQQ. The SPY sleeve that QQQ lacks (about 47% of SPY: Berkshire, JPMorgan, Lilly, Visa, Exxon, banks, insurers, energy, real estate) is the diversifier.
- **The overlap is asymmetric.** "About half of SPY is in QQQ" and "about 93% of QQQ is in SPY" are both true. The report should not quote one overlap number without saying which direction it measures.
- **QQQ's unique exposure is small (about 7%) but very AI- and growth-heavy.** It includes SpaceX and AI-infrastructure names that are not in the S&P 500: CoreWeave, Nebius, Astera Labs, Arm and ASML total about 2.0% (computed).

### Gaps
- The ETF Research Center (etfrc.com) overlap figure was not retrieved. All overlap numbers above are my own computations on the cited files.
- The non-S&P stocks outside QQQ's top 25 use rescaled weights from the undated Zacks snapshot. Their total (about 4.5%) is approximate.

## 4. How much of the S&P 500's Nov 5, 2026 decline came from Nvidia, the Magnificent 7 and AI-linked stocks

### Takeaway
I found no outlet that reported a point-by-point attribution, so the figures below are my estimates (Nov 4 SPY weights × Nov 5 returns). The S&P 500 fell about 335 points (−4.36%). Nvidia accounted for about 52 points (about 15.5%). The Magnificent 7 accounted for about 110 points (about 33%, roughly in line with their 33.5% weight). Nvidia, Broadcom, Micron and AMD together accounted for about 105 points (about 31%). The IT sector accounted for about 206 points (about 61%). QQQ (about −6.5%) fell about 2.1 pp more than SPY. Most of that gap came from QQQ's heavier Micron and AMD weights (about 0.87 pp), not from Nvidia (about 0.05 pp).

### Cited Findings
- **Index move:** the S&P 500 closed at 7,353.73, down 4.36%. It was the steepest one-day drop since the April 2025 tariff rout — [yournews (citing Investing.com)](https://yournews.com/2026/11/05/7254835/s/); [Spectrum News](https://spectrumlocalnews.com/us/snplus/business/2026/11/05/stock-market-ai-chip-selloff)
- **Nvidia:** fell 9.26% to $181.60 — [Motley Fool, Nov 5, 2026](https://www.fool.com/coverage/stock-market-today/2026/11/05/stock-market-today-nov-5-nvidia-slides-on-ai-chip-selloff-as-election-uncertainty-weighs/)
- **CNBC statistics, Nov 5, 2026:**
  - The Magnificent 7 lost more than $1 trillion of market cap; Nvidia lost more than $440 billion.
  - The S&P 500 IT sector fell 7.30%, its worst day since March 16, 2020. XLK fell 8.04%. Industrials fell 4.12%.
  - All 11 sectors fell. NYSE decliners outnumbered advancers 2,344 to 416.
  - The article gives no point attribution.
  - Source: [CNBC](https://www.cnbc.com/2026/11/05/stock-market-selloff-ai-fears.html)
- **Nasdaq-100:** suffered its worst day since 2020 — [investinglive](https://investinglive.com/stocks/nasdaq-100-suffers-worst-day-since-2020/)
- **Individual stock moves on Nov 5.** These come from the stockanalysis QQQ table and use last prices, which may include after-hours trading. Nvidia's −9.14% there compares with −9.26% at the close.
  - Down 13–18%: MU −17.16%, AMD −17.55%, LRCX −16.46%, AMAT −13.54%.
  - Down 9–11%: TSLA −10.78%, TXN −10.69%, AVGO −10.43%, INTC −10.38%, CRWD −10.12%, PLTR −9.75%, PANW −9.68%, SPCX −9.22%.
  - Smaller moves: CSCO −7.56%, META −3.87%, MSFT −3.52%, GOOGL −2.19%, AMZN −2.06%, AAPL −1.39%, COST +1.91%.
  - Source: [stockanalysis QQQ holdings](https://stockanalysis.com/etf/qqq/holdings/)
- **ETF closing prices:**
  - QQQ: previous close $691.95; after-hours $651.16, up $4.11 on its close. That implies a regular-session close of about $647.05 (−6.49%) — [stockanalysis QQQ](https://stockanalysis.com/etf/qqq/)
  - SPY: previous close $766.81; after-hours $734.39, up $1.24. That implies about $733.15 (−4.39%) — [stockanalysis SPY](https://stockanalysis.com/etf/spy/)
  - Zacks's delayed quote shows QQQ at $650.96 (−5.92%) "as of 4:00 PM ET". This appears to reflect after-hours trading rather than the close — [Zacks](https://www.zacks.com/funds/etf/QQQ/holding)

### Inferences
- **Estimated S&P 500 contributions (all computed).** Method: S&P prior close of about 7,689 (7,353.73 ÷ 0.9564), so a drop of about 335 points. Each contribution is the stock's Nov 4 SPY weight × its Nov 5 return.

  | Stock or group | Contribution (pp) | Points | Share of decline |
  |---|---|---|---|
  | Nvidia | −0.68 | ≈52 | ≈15.5% |
  | Broadcom | −0.24 | | ≈5.6% |
  | Micron | −0.23 | | ≈5.3% |
  | AMD | −0.21 | | ≈4.8% |
  | Nvidia + Broadcom + Micron + AMD | −1.36 | ≈105 | ≈31% |
  | Magnificent 7 (incl. both Alphabet classes) | −1.44 | ≈110 | ≈33% |
  | IT sector (36.67% × −7.30%) | −2.68 | ≈206 | ≈61% |
  | 19 large tech/AI names (Mag 7 plus 11 chip and AI-software stocks) | −2.52 | | ≈58% |

  Within the Magnificent 7, Nvidia and Tesla fell far more than the index, while Apple, Amazon and Alphabet fell much less.
- **Estimated QQQ contributions (computed with Nov 4 QQQ weights).**

  | Group | Contribution (pp) | Share of QQQ's ≈6.5% drop |
  |---|---|---|
  | Top 25 holdings | −4.82 | ≈74% |
  | Nvidia + Micron + AMD + Broadcom | −2.29 | ≈35% |
  | 8 chip stocks in the top 25 | −2.95 | ≈45% |
  | Magnificent 7 | −1.75 | ≈27% |

- **Where QQQ's extra loss of about 2.1 pp vs SPY came from (computed).**

  | Source | Extra loss in QQQ (pp) |
  |---|---|
  | Micron + AMD | ≈0.87 |
  | AMAT + LRCX | ≈0.25 |
  | SpaceX (not in SPY) | ≈0.24 |
  | Tesla | ≈0.18 |
  | Intel + TI | ≈0.19 |
  | Nvidia | ≈0.05 |

  The rest is SPY's ballast of financials, health care and staples. The day's lesson is that the QQQ–SPY gap is a second-tier-semis and high-beta-growth story, not an Nvidia story, because the Nasdaq-100's caps keep Nvidia's QQQ weight close to its SPY weight.
- **The QQQ −6.49% and SPY −4.39% computed here match the session's verified figures (−6.5% and −4.4%).** Zacks's −5.92% should not be used.

### Gaps
- No reported point attribution (Dow Jones Market Data, S&P DJI, Bloomberg or Reuters) was found. All attribution figures above are estimates. They use Nov 4 closing weights and some returns that may include small after-hours moves. Remaining S&P 500 names were not individually computed.
- No SOX or semiconductor-index closing figure was captured in this pass. The session context gives −11% to −12% for semiconductor ETFs.

## 5. Nasdaq-100 weighting rules (caps, quarterly and special rebalances, December reconstitution) and 2025–2026 rule changes

### Takeaway
The Nasdaq-100 is a modified market-cap-weighted index of the 100 largest non-financial Nasdaq-listed companies.
- **Every quarterly rebalance:** if any company exceeds 24% it is cut to 20%; if companies above 4.5% together reach 48% or more, that group is cut to 40%.
- **December reconstitution only:** an extra security-level step caps any security at 14% and cuts the five largest to 38.5% if they total 40% or more.
- **Special rebalance:** triggered whenever 24% or 48% is breached at end of day.
- **2026 overhaul (effective May 1, 2026):** added "Fast Entry" for top-40-size new listings (which let SpaceX in within 15 trading days), a 3x-free-float cap on weights of low-float stocks, removal of the 10% minimum float, and rank-based removals (outside the top 125).
- **2025:** I found no weighting-rule change.

### Cited Findings
- **Index scope:** "100 of the largest domestic and international non-financial companies listed on The Nasdaq Stock Market based on market capitalization." It excludes financials — [Nasdaq-100 fact sheet](https://indexes.nasdaqomx.com/docs/FS_NDX.pdf)
- **Weighting basis:** weights use "Modified Market Capitalization" and count only eligible listed share classes. Each low-float security's total shares are capped at "three times the number of its free-floating shares". "There is no minimum free float criterion." The current methodology document is © 2026 — [Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf)
- **Fast Entry:** a non-member is added on an expedited basis if its Full Market Capitalization ranks within the top 40 current constituents. No other member has to be removed, so the count may temporarily exceed 100 — [Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf). Since May 1, 2026, such candidates "may be added to the index after 15 trading days, subject to the 3x float cap" — [Nasdaq 2026 NDX Changes FAQ (July 2026)](https://indexes.nasdaqomx.com/docs/2026_NDX_Changes_FAQ.pdf)
- **Seasoning and liquidity:**
  - Normal seasoning is three full calendar months on an eligible exchange. An IPO is ranked as of the end of its seventh trading day. Average daily traded value must be at least $5 million — [Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf)
  - The FAQ says only companies of roughly $100 billion or more in full market cap (as of March 2026) would qualify for Fast Entry — [2026 NDX Changes FAQ](https://indexes.nasdaqomx.com/docs/2026_NDX_Changes_FAQ.pdf)
- **December annual reconstitution, selection:**
  - Companies are ranked by Full Market Capitalization. Selection order: the top 75; then current members ranked within the top 100; then members ranked 101–125 if they were top-100 at the prior reconstitution or were added since; then other top-100 companies, until 100 are selected.
  - Reference date: last trading day of November. Effective: market open on the first trading day after the third Friday of December. Announced after the close on the sixth trading day before the effective date.
  - Source: [Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf)
- **December annual reconstitution, weighting:**
  - Company-level: if any company's initial weight exceeds 24%, weights are adjusted so no company exceeds 20%. If companies above 4.5% sum to 48% or more, that group is cut to 40%.
  - Security-level: if any security exceeds 15%, it is cut to 14%. If the five largest securities sum to 40% or more, they are cut to 38.5%, and any security outside the top five is capped at the lesser of 4.4% or the fifth-largest weight.
  - Source: [Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf)
- **March, June and September rebalances:**
  - Share counts and float adjustments are updated. Members ranked outside the top 125 are removed and replaced if the count falls below 100. Non-members ranked in the top 40 are added.
  - Additions get weights by linear interpolation. The same company-level constraints apply (24%→20%; ≥48%→40%).
  - Source: [Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf)
- **Special rebalance:** may be triggered if, at end of day, any company exceeds 24% or companies above 4.5% together exceed 48% — [Nasdaq-100 methodology](https://indexes.nasdaqomx.com/docs/Methodology_NDX.pdf)
- **The 2026 consultation (February 2026):**
  - It proposed counting listed plus unlisted shares for eligibility and ranking, and Fast Entry (top 40, at least five trading days' notice, added after 15 trading days, exempt from seasoning).
  - It proposed weighting stocks with less than 20% float at 5x their free-float percentage.
  - It also proposed dropping the 10% minimum float and replacing other ad-hoc rules.
  - Source: [NDX Consultation, February 2026](https://indexes.nasdaqomx.com/docs/NDX_Consultation-February_2026.pdf)
- **Adopted rules (FAQ dated July 2026, with Q&As added 7/31/2026):**
  - Fast Entry and the 3x float cap took effect May 1, 2026, so stocks with less than 33⅓% float are weighted down.
  - The "10 basis point rule" and intra-quarter share-count adjustments ended May 1.
  - From the June 22, 2026 quarterly review, ranking uses total (listed plus unlisted) shares, and the 10 bp rule is replaced by removal of companies ranked outside the top 125.
  - The 10% minimum float requirement was removed.
  - Source: [2026 NDX Changes FAQ](https://indexes.nasdaqomx.com/docs/2026_NDX_Changes_FAQ.pdf)
- **Earlier example:** the December 2024 annual rebalance shrank the weights of Tesla, Meta and Broadcom (headline) — [Bloomberg, Dec 23, 2024](https://www.bloomberg.com/news/articles/2024-12-23/tesla-meta-and-broadcom-weights-shrink-in-nasdaq-100-rebalance)
- **S&P 500 for contrast:** it is "float-adjusted market capitalization weighted" — [SSGA SPY fact sheet](https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-spy.pdf). In June 2026 S&P declined to change its seasoning and viability rules to admit mega-IPOs early — [Axios](https://axios.com/2026/06/04/musk-spacex-ipo-sp-investors)

### Inferences
- **The caps explain why QQQ's top three weights are close to SPY's.** The 4.5%/48%→40% and top-five 38.5% rules compress the largest names at each reset, and the excess flows to smaller members. That puts Micron and AMD at about 4% and 3.6%, and keeps Broadcom (2.5%) below Meta (3.0%) in QQQ, even though Broadcom is bigger than Meta in SPY.
- **On Nov 4 no special rebalance was near.** The names above 4.5% (AAPL, NVDA, MSFT, AMZN) summed to about 27.4% (computed), far below 48%.
- **Next reconstitution dates (computed from the methodology calendar):** reference date Monday Nov 30, 2026; announcement about Friday Dec 11, 2026; effective at the open on Monday Dec 21, 2026, after the third Friday, Dec 18. This will be the first December reconstitution under the 2026 rules (3x float cap, total-share ranking). SpaceX's index weight can grow as lock-ups expire and its float rises.

### Gaps
- No Nasdaq-100 weighting-rule change dated 2025 was found. The 24%/4.5%/48%/40% and 14%/38.5% rules appear in the current (2026) methodology; I did not establish exactly when each was introduced.
- The May 1, 2026 effective-methodology PDF ("2026 May NDX Changes FAQ") returned 404. Details come from the July 2026 FAQ and the current methodology.
- SpaceX's initial weight at entry was not confirmed from a primary Nasdaq notice.

## 6. Product facts: fees, structure, AUM, yield and distribution frequency

### Takeaway
SPY charges 0.0945% and is still a unit investment trust. It cannot reinvest dividends between quarterly payouts (they sit in a non-interest-bearing account), does not hold futures, and, per secondary sources, cannot lend securities. VOO and IVV charge 0.03% and SPYM (formerly SPLG) 0.02%. QQQ became an open-end fund on Dec 22, 2025 and now charges 0.18%; it can reinvest dividends and lend securities. QQQM charges 0.15%. All six pay quarterly. Trailing yields are about 1.0–1.1% for the S&P 500 funds and about 0.5% for QQQ and QQQM.

### Cited Findings
- **SPY (State Street SPDR S&P 500 ETF Trust):**
  - Gross and net expense ratio 0.0945%; 30-day SEC yield 0.96%; Index Dividend Yield 1.10%; 504 holdings (all as of 9/30/2026) — [SSGA SPY fact sheet](https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-spy.pdf)
  - AUM $818,538.75M as of Nov 4, 2026; shares outstanding 1,067.98M; distribution yield 0.99%; distribution frequency quarterly; listed on NYSE Arca Jan 22, 1993. SSGA calls it "a unit investment trust", and notes SSGA is now State Street Investment Management — [SSGA SPY page](https://www.ssga.com/us/en/intermediary/etfs/state-street-spdr-sp-500-etf-trust-spy)
  - Trailing-12-month dividend $7.58 (1.03%); last ex-dividend date Sep 18, 2026; AUM shown $801.86B (likely after the Nov 5 drop) — [stockanalysis SPY](https://stockanalysis.com/etf/spy/)
- **SPY structural limits (prospectus dated Jan 27, 2025):**
  - "(A Unit Investment Trust)"; "The Trust does not hold or trade futures or swaps."
  - Dividends are paid quarterly on the last business day of April, July, October and January.
  - "No dividend reinvestment services are provided by the Trust."
  - Dividends received are "credited by the Trustee to a non-interest-bearing account" and held "without interest until distributed".
  - Source: [SPY prospectus, SEC Form 497](https://www.sec.gov/Archives/edgar/data/884394/000119312525013533/d875286d497.htm)
  - A secondary source says SPY cannot lend its securities either — [ETF Central](https://www.etfcentral.com/news/3-things-you-didnt-know-spdr-sp-500-etf-trust-spy)
- **IVV (iShares Core S&P 500):**
  - Expense ratio 0.03%; net assets $849,980,834,760 as of Nov 5, 2026; shares outstanding 1,154,350,000 (Nov 5, 2026).
  - 30-day SEC yield 0.95% and 12-month trailing yield 1.10% (as of Sep 30, 2026); distribution frequency quarterly; inception May 15, 2000.
  - Source: [iShares IVV page](https://www.ishares.com/us/products/239726/ishares-core-sp-500-etf)
  - Trailing-12-month dividend $8.40 (1.14%); last ex-dividend date Sep 15, 2026 — [stockanalysis IVV](https://stockanalysis.com/etf/ivv/)
- **VOO (Vanguard S&P 500 ETF):** expense ratio 0.03%; AUM $1.04T; trailing-12-month dividend $7.43 (1.10%); quarterly payouts; last ex-dividend date Sep 28, 2026 — [stockanalysis VOO](https://stockanalysis.com/etf/voo/)
- **SPYM (formerly SPLG; State Street SPDR Portfolio S&P 500 ETF, "ETF Share Class"):**
  - Gross expense ratio 0.02%; 30-day SEC yield 1.04%; 505 holdings; inception 11/08/2005 (all as of 9/30/2026) — [SSGA SPYM fact sheet](https://www.ssga.com/us/en/intermediary/library-content/products/factsheets/etfs/us/factsheet-us-en-spym.pdf)
  - AUM $181.05B; trailing-12-month dividend $0.91 (1.06%); quarterly — [stockanalysis SPYM](https://stockanalysis.com/etf/spym/)
  - Secondary sources date the SPLG→SPYM name and ticker change to Oct 31, 2025 — [Motley Fool, Dec 26, 2025](https://www.fool.com/coverage/etfs/2025/12/26/spy-vs-spym-two-ways-to-own-the-s-and-p-500); [Optimized Portfolio](https://www.optimizedportfolio.com/spym/)
- **QQQ (Invesco QQQ Trust):**
  - Shareholders approved converting from a unit investment trust to an open-end fund. It began trading as an open-end fund on Dec 22, 2025. Total expense ratio cut from 0.20% to 0.18%. The new structure allows dividend reinvestment and securities lending. The change was not a tax realization event — [Invesco press release](https://www.invesco.com/hk/en/investment-ideas/press-and-media/2025/invesco-qqq-shareholders-vote-to-approve-modernization.html); [Invesco proxy material, SEC DEFA14A](https://www.sec.gov/Archives/edgar/data/1067839/000119312525255488/d22028ddefa14a.htm); [iTiger summary](https://www.itiger.com/news/1148706660)
  - The Zacks holdings table shows a Nasdaq-100 futures position (NQZ6, 0.10%) plus cash lines — [Zacks QQQ holdings](https://www.zacks.com/funds/etf/QQQ/holding)
  - AUM $461.49B; expense ratio 0.18%; trailing-12-month dividend $3.09 (0.48%); quarterly; last ex-dividend date Sep 21, 2026; beta 1.24 — [stockanalysis QQQ](https://stockanalysis.com/etf/qqq/)
- **QQQM (Invesco Nasdaq 100 ETF):** expense ratio 0.15%; AUM $105.25B; trailing-12-month dividend $1.32 (0.49%); quarterly; last ex-dividend date Sep 21, 2026; inception October 2020 — [stockanalysis QQQM](https://stockanalysis.com/etf/qqqm/)

### Inferences
- **Annual cost per $10,000 (simple arithmetic):** SPY $9.45, QQQ $18, QQQM $15, VOO and IVV $3, SPYM $2. Switching QQQ→QQQM saves 3 bp; SPY→VOO/IVV saves about 6.5 bp; SPY→SPYM saves about 7.5 bp.
- **Rough asset ranking:** VOO is now the largest at about $1.04T. IVV ($850B, Nov 5) appears to have overtaken SPY ($819B on Nov 4, about $802B after Nov 5).
- **Yield gap:** QQQ yields about half as much as SPY (about 0.48% vs about 1.03% trailing). SPY's slightly lower yield than IVV and VOO fits its higher fee and its dividend cash drag.
- **Structure:** after QQQ's conversion, SPY is the only one of the six still using the UIT structure. That leaves it unable to reinvest dividends or hold futures (and, per secondary sources, to lend). Its main remaining advantage is trading liquidity; liquidity data are not covered here.
- **The futures line shows the new structure in use.** A position in Nasdaq-100 futures is something a UIT like SPY says it does not do. That suggests QQQ is using its open-end flexibility for cash equitization.

### Gaps
- VOO figures are from stockanalysis, not Vanguard (Vanguard's data endpoint returned 404). It is unclear whether $1.04T is the ETF share class alone or the whole Vanguard 500 Index Fund. Vanguard's SEC yield was not retrieved.
- QQQ and QQQM figures (AUM, yield) are from stockanalysis because Invesco blocked retrieval. Invesco's official 30-day SEC yields and AUM were not obtained.
- Whether QQQ is actually lending securities since the conversion, and how much income that brings, was not verified.
- The exact prospectus wording on SPY's inability to lend securities was not found in the sections reviewed. Only the dividend-reinvestment and futures/swaps limits are quoted from the prospectus.
- SPYM's fee cut to 0.02% was not dated from a primary SSGA source.
