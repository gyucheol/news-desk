# Lump sum vs. dollar-cost averaging after a sharp selloff, and SPY/QQQ forward returns after Nov 5, 2026-type events

Scope note for the report writer: this file combines (a) published research and media-reported market statistics and (b) my own reproducible backtests on Yahoo Finance total-return (adjusted close) data. "Own calc" bullets cite the Yahoo data endpoint that the numbers came from; scripts, outputs and data paths are listed under the verification question. The abbreviations are: LS = lump sum (all money invested at the event-day close); DCA = dollar-cost averaging / "cost averaging" (CA in Vanguard's wording); pp = percentage points of the initial amount.

## Q1. What do Vanguard (2012, 2023), Morningstar and academic work conclude about lump sum vs. DCA? Does the answer change after crashes or in high volatility, and what do they say about regret and investor behavior?

### Takeaway
The research is consistent: lump sum beats DCA about two-thirds of the time, because stocks beat cash more often than not. The gap grows as the DCA period gets longer (US: 66% of the time with a 3-month split, 74% with a 6-month split). DCA does not raise expected returns. Its value is lower short-term risk and less regret, which matters most in falling markets and for loss-averse investors. None of the published studies I found tests whether starting right after a crash or a volatility spike changes the answer, which is why the new backtests below were run.

### Cited Findings
**Vanguard, February 2023 (Megan Finlay and Josef Zorn, "Cost averaging: Invest now or temporarily hold your cash?", doc. ISGCALS 022023)**
- Lump sum beat cost averaging 68% of the time. Test setup: 100% equity, MSCI World Index 1976–2022, a 3-month split (three equal parts invested a month apart), wealth compared after one year, no interest on uninvested cash. Cost averaging still beat holding cash 69% of the time, and lump sum beat cash 70% — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- Over 1976–2022, US stocks beat cash (3-month T-bills) 76% of the time and bonds beat cash 68% of the time. "A cash allocation, even if temporary, represents the opportunity cost of lost risk premium" — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- When idle cash earns the 3-month T-bill rate, lump sum still beats the 3-month split 65% of the time for an all-equity portfolio. Higher cash rates shrink lump sum's advantage — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- One-year wealth for a $100,000, 100% equity portfolio, lump sum vs. cost averaging: median $111,940 vs. $109,580 (2.2% higher with lump sum); 5th percentile $82,947 vs. $85,906 (cost averaging better in the worst outcomes); 95th percentile $139,453 vs. $131,012. For a 60/40 portfolio the average was $109,360 vs. $107,453 (1.8% more) — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- Lump sum's win rate ("hit ratio") rises as the split gets longer. US (Russell 3000, 1979–2022): 66.4% with a 3-month split, 69.9% with 4 months, 72.6% with 5 months, 73.7% with 6 months. Other markets with a 3-month split: UK 68.1%, Canada 67.2%, Europe 66.5%, Australia 67.5%, emerging markets 61.6%, global (USD) 67.7% — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- Once both portfolios are fully invested, "the portfolio with more assets at that point will stay ahead forever," so the holding period does not change the winner — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- In 10,000 simulations of a 60/40 portfolio over one year, cost averaging left the investor with less than lump sum: $504 less (per $100,000) for a 3-month split and $1,491 less for a 6-month split. In the simulations, the cost-averaging period "can safeguard in extreme down markets but hinders portfolio growth in the best up markets" — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- Vanguard's model that adds a penalty for losses (loss aversion) finds that some investors prefer cost averaging:
  - A moderately conservative investor (risk aversion 6) prefers lump sum without loss aversion, but prefers cost averaging once loss aversion is set to 2.5 (certainty-equivalent return 1.0102 for cost averaging vs. 1.0100 for lump sum).
  - A very conservative investor (risk aversion 10) prefers cost averaging either way.
  - An adventurous investor (risk aversion 3) prefers lump sum either way.
  - [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- On regret: "Particularly for loss-averse investors, lowering risk could limit drawdown and the accompanying investor regret in a severe market downturn, thus preserving commitment to the investment plan." Vanguard advises loss-averse investors who choose cost averaging to keep the period short, "such as three months," and notes that having a plan to invest cash matters more than the choice between lump sum and cost averaging — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)
- Vanguard says the literature "is generally in favor of lump-sum investing." Its reference list:
  - Constantinides (1979), *Journal of Financial and Quantitative Analysis* (JFQA) 14(2): 443–450
  - Rozeff (1994), *Journal of Portfolio Management* (JPM) (Winter): 45–50
  - Brennan, Li and Torous (2005), *Review of Finance* 9(4): 509–535
  - Shtekhman, Tasopoulos and Wimmer (2012), Vanguard. Vanguard's reference list spells the second author "Tasapoulos"; "Tasopoulos" appears to be the correct spelling.
  - Statman (1995), JPM 22(1): 70–78
  - [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)

**Vanguard, 2012 (Shtekhman, Tasopoulos and Wimmer, "Dollar-cost averaging just means taking risk later")**
- Morningstar describes the study as follows: "a portfolio combining 60% stocks and 40% bonds over rolling 10-year periods from 1926 to 2011 and found that dollar-cost averaging led to better returns only about one third of the time" — [Morningstar, Arnott 2020](https://www.morningstar.com/markets/when-dollar-cost-averaging-can-help-or-hurt)
- Press coverage at the time reported a similar roughly two-thirds win rate for lump sum across the US, UK and Australia. I saw this only in a search-result summary and did not open the article — [BenefitsPRO, Oct 31, 2012](https://benefitspro.com/2012/10/31/lump-sum-investing-vs-dollar-cost-averaging/?amp=1)

**Morningstar (Amy C. Arnott, CFA, Sep 4, 2020, "When Dollar-Cost Averaging Can Help (or Hurt)")**
- "The notion that dollar-cost averaging improves returns has been pretty thoroughly debunked … Statistically speaking, the market goes up more often than it goes down" — [Morningstar](https://www.morningstar.com/markets/when-dollar-cost-averaging-can-help-or-hurt)
- A 2019 Morningstar study (equity-only portfolio, periods of 2 to 120 months, data back to 1926) found that DCA improved returns in 27.8% of 10-month periods and only 10.0% of 10-year periods — [Morningstar](https://www.morningstar.com/markets/when-dollar-cost-averaging-can-help-or-hurt)
- "Dollar-cost averaging typically fares best in periods with negative total returns." From March 2000 to October 2002, investing monthly into an all-equity portfolio from a zero starting balance would have "limited losses to 1.75%," compared with an annualized loss of 13.84% for a lump sum. In 2020 through August, monthly investing earned an internal rate of return (IRR) of 3.4%, vs. about 9.7% for buy-and-hold. Note that this example is about investing new money periodically, not splitting a windfall — [Morningstar](https://www.morningstar.com/markets/when-dollar-cost-averaging-can-help-or-hurt)
- On behavior: in sector funds, a steady-investing scenario beat investors' actual dollar-weighted returns by about 1.3 pp a year (international equity funds: about 0.9 pp a year), because investors chase performance. Arnott calls a gradual approach reasonable for an inheritance or windfall: "if dipping a few toes in the water at a time is the only way you can ease yourself back into the pool, it's better than just sitting on dry land forever" — [Morningstar](https://www.morningstar.com/markets/when-dollar-cost-averaging-can-help-or-hurt)

**Academic literature**
The literature review in Cho and Kuvvet (2015), *Journal of Financial Planning* 28(10): 52–58, summarizes the main studies:
- Constantinides (1979) showed theoretically that DCA is dominated by sequential optimal strategies — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Williams and Bacon (1993), using US stock returns from 1926 to 1991, found that lump sum gave higher annualized returns "two-thirds of the time" — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Rozeff (1994) found in simulations that lump sum gives higher annualized returns than DCA. Knight and Mandell (1993) found DCA has no advantage over optimal rebalancing or buy-and-hold — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Statman (1995) attributed DCA's popularity to behavioral factors: prospect theory, regret aversion, cognitive errors and lack of self-control — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Leggio and Lien (2001, 2003) found lump sum beat DCA, including on downside-risk measures (the Sortino and upside-potential ratios), and that loss aversion alone does not explain DCA's popularity — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Trainor (2005) found that DCA "significantly" reduces the probability of losing a given amount during the investment period — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Brennan, Li and Torous (2005), using data from 1926 to 2003, concluded that prices tending to revert to their average may have helped DCA investors, especially those adding individual stocks to a diversified portfolio — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Dichtl and Drobetz (2011) found DCA inefficient even for investors with cumulative-prospect-theory preferences; a 50/50 buy-and-hold beat both DCA and lump sum. Dubil (2005) put DCA's expected return at "30 percent lower" than lump sum's — [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)
- Two findings depend on market conditions:
  - Greenhut (2006): DCA works best in down markets, lump sum in up markets.
  - Atra and Mann (2001): lump sum won when started October–January, DCA when started February–September.
  - [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)

Cho and Kuvvet's own model compares investing everything at once with investing in two halves six months apart:
- Annualized expected return / standard deviation: lump sum 8.16% / 19.19%; DCA 6.08% / 14.91%.
- An investor with a risk-aversion coefficient of 2.85 is indifferent between the two; anyone more risk-averse prefers DCA. The typical range of this coefficient in the literature is 2–4.
- [Cho & Kuvvet 2015](https://financialplanningassociation.org/article/journal/OCT15-dollar-cost-averaging-trade-between-risk-and-return)

**Statman's behavioral view (Meir Statman, *Journal of Financial Planning*, Oct 2018: "Dollar-Cost Averaging Is Not Rational, but It Is Normal and Can Be Wise")**
- "Both logic and simulations indicate that investors are more likely to increase their wealth with lump-sum investing" — [Statman 2018](https://financialplanningassociation.org/article/journal/OCT18-dollar-cost-averaging-not-rational-it-normal-and-can-be-wise)
- Framing: "DCA overcomes loss-aversion in a frame that highlights gains and obscures losses." Regret: regret over losses outweighs pride over equal gains, and splitting a purchase lets investors console themselves if prices fall. Self-control: after several down periods investors extrapolate losses and abandon their plans, and DCA's fixed schedule enforces discipline — [Statman 2018](https://financialplanningassociation.org/article/journal/OCT18-dollar-cost-averaging-not-rational-it-normal-and-can-be-wise)
- "Risk reduction cannot be the rationale for both DCA and reverse DCA." Statman likens DCA to corrective "financial" glasses that get normal investors to put part of their wealth into stocks — [Statman 2018](https://financialplanningassociation.org/article/journal/OCT18-dollar-cost-averaging-not-rational-it-normal-and-can-be-wise)

### Inferences
- The "two-thirds" result from these studies covers all starting dates, good times and bad. It mostly restates the fact that stocks beat cash in most 3–12-month windows. The winner is decided by the price path during the DCA window. With 0% cash yield, lump sum wins if and only if the entry price is below the harmonic mean of the tranche prices.
- Published research supports DCA as a way to manage behavior (regret, loss aversion, self-control) and to reduce losses during the period, not as a way to raise returns. It does not support the idea that DCA is systematically better right after a crash. Arguments in DCA's favor in down markets (Greenhut; Morningstar's 2000–02 example) are about periods that kept falling, which can only be identified afterward.
- Vanguard's practical compromise for loss-averse investors is a short period (about 3 months). My own backtests below show the same pattern: longer splits cost more in the median case.

### Gaps
- I could not open the 2012 Vanguard PDF. The legacy s315 URL returned a "Service Unavailable" page and a mirror rate-limited me. Its exact figures, such as the often-quoted average 12-month DCA shortfall of about 2.3%, are unverified; that figure came only from search-engine summaries.
- I did not read the original texts of Constantinides (1979), Williams and Bacon (1993), Rozeff (1994) or Statman (1995). The summaries above rely on Cho and Kuvvet's (2015) literature review and Vanguard's (2023) reference list.
- Search summaries mention Morningstar work by Maciej Kowara and Paul Kaplan ("Dollar-Cost Averaging: Truth and Fiction"; "The Case for Dollar-Cost Averaging"), but I did not open those pages, so their findings are not cited.
- I found no published study that tests lump sum vs. DCA specifically on starting points right after a ≥4% one-day drop or a VIX spike. The backtests in Q4 fill that gap.

## Q2. What do reputable market-data sources (LPL Research, Bespoke, Ned Davis, Dow Jones Market Data, Carson Group, Goldman Sachs) report about forward returns after VIX spikes, 4%+ S&P 500 down days and 10%+ Nasdaq corrections?

### Takeaway
The attributable statistics I could verify point the same way as my own calculations: after VIX spikes and Nasdaq corrections, 6–12-month returns have usually been positive and above average, but a meaningful minority of cases turned into bear markets (2000–02, 2008, 2022). For this episode I could not find primary or clearly attributed numbers from Bespoke, Ned Davis, Goldman Sachs or Carson Group. The LPL figure comes via a 2022 Cboe guest article, and the Dow Jones Market Data figure via a Motley Fool attribution.

### Cited Findings
**This week's selloff (Nov 5, 2026)**
- Index moves: the Nasdaq Composite fell about 5.5% and entered correction territory, its worst day since April 4, 2025 (-5.82%). The S&P 500 fell about 4.4%, its worst day since April 4, 2025 (-5.97%). The Dow fell about 1,833 points (3.4%) — [CNBC, Nov 5, 2026](https://www.cnbc.com/2026/11/05/stock-market-selloff-ai-fears.html)
- VIX and sectors: the VIX rose 11.57 points, its largest point gain since April 4, 2025 (+15.29), to its highest level since March 31. S&P 500 information technology fell 7.30% and the XLK tech ETF fell 8.04%, both their worst days since March 16, 2020. The "Magnificent 7" stocks lost more than $1 trillion of market value, Nvidia alone more than $440 billion — [CNBC, Nov 5, 2026](https://www.cnbc.com/2026/11/05/stock-market-selloff-ai-fears.html)
- The VIX's roughly 70% jump was described as its biggest one-day surge in almost two years. I saw this only in a search summary; my own data agree (the last bigger jump was Dec 18, 2024, +74.0%) — [CNN, Nov 5, 2026](https://www.cnn.com/2026/11/05/investing/tech-heavy-nasdaq-plunges)

**Nasdaq corrections (10%+)**
- CNBC (Deena Zaidi and Nick Wells, Nov 5, 2026) looked at 10 Nasdaq correction episodes over the last decade; no data source is named. Findings:
  - Average gain measured from the correction bottom: 9.41% over 3 months and 17.03% over 6 months.
  - Further selling followed in the near term in the 2025, 2022, 2020 and 2018 episodes.
  - In January 2022, the Nasdaq fell another 18.3% over the next six months and was down 24.3% a year later.
  - The Nasdaq was higher 12 months after the election in 12 of 13 midterm cycles since 1974 (Frank Cappelleri, CappThesis).
  - [CNBC](https://www.cnbc.com/2026/11/05/nasdaq-drops-into-correction-territory-heres-what-typically-happens-next.html)
- Motley Fool (Matt Frankel, Nov 5, 2026) cites several sources:
  - Reuters, using LSEG data: the Nasdaq entered a correction after a new high 24 times in 44 years (about once every 1.8 years).
  - Schaeffer's Research (data back to 1971): the average return one month after a 10% drop is "slightly negative"; six months later the average gain is 13.6% and the index was higher 73% of the time.
  - Corrections since 2011 (source not named): average gain of 22% over 12 months, higher in 11 of 12.
  - About 37% of Nasdaq corrections since 1971 became bear markets (20%+ declines), attributed to Dow Jones Market Data.
  - This is the Nasdaq Composite's third correction of 2026, after March and July; new records followed both earlier ones.
  - [Motley Fool](https://www.fool.com/investing/2026/11/05/nasdaq-stock-market-correction-history-says-this-is-what-happens-next/)

**VIX spikes**
- LPL Financial Research (via a Cboe guest article by Innovative Portfolios, July 15, 2022): when the VIX rose above 30 and stayed there for at least 10 days, the S&P 500's subsequent one-year return averaged 21.9% (source: "LPL Financial Research, FactSet 03/15/2022") — [Cboe](https://www.cboe.com/insights/posts/embracing-and-harnessing-volatility-feeling-confident-in-your-strategy/)
- The same article's own 1990–2021 analysis, which counts every qualifying day so the windows overlap: average one-year S&P 500 return of 23% after a VIX close above 30, 28% above 35 and 33% above 40 — [Cboe](https://www.cboe.com/insights/posts/embracing-and-harnessing-volatility-feeling-confident-in-your-strategy/)

### Inferences
- The media statistics use different indexes (Nasdaq Composite vs. Nasdaq-100/QQQ), different starting points (the correction bottom vs. the day the index enters correction) and price-only returns. They should be compared with the total-return SPY/QQQ backtests in Q4–Q5 only directionally.
- The CNBC "from the bottom" averages (+9.4% at 3 months, +17.0% at 6 months) cannot be used for an entry decision made today, because the bottom is only known afterward. My event-date numbers (Q5, and QQQ ≥10% below its 52-week high in Q4) are measured from the day the signal fires.
- The Dow Jones Market Data figure (37% of corrections became bear markets) matches the tail cases in my tables. QQQ fell further, more than 20% below its high, after many of its correction signals, including 2000, 2008 and 2022.

### Gaps
- I found no primary or clearly attributed 2025–2026 statistics from Bespoke, Ned Davis Research, Goldman Sachs or Carson Group (Ryan Detrick) on returns after VIX spikes, 4% down days or Nasdaq corrections. Searches returned mostly aggregator or low-quality pages.
- A Market Index (Australia) article about this week's roughly 70% VIX jump reportedly says the S&P 500 was higher a month later after 9 of the past 10 VIX spikes of 50%+. The page blocked my fetch (HTTP 403), so the figure is unverified — [Market Index](https://www.marketindex.com.au/news/wall-street-panic-sell-off-sends-vix-up-almost-70-heres-what-usually-happens-next)
- The Motley Fool's 12-month "+22%, 11 of 12" statistic has no named source.
- A search summary of a BIS Bulletin (No. 95) says the August 2024 VIX spike was partly driven by quote-setting and wide bid-ask spreads. I did not read the bulletin — [BIS](https://www.bis.org/publ/bisbull95.pdf)

## Q3. Do the earlier event-study numbers hold when the existing scripts are re-run?

### Takeaway
Yes. Every earlier number reproduced exactly. A fresh download on Nov 6 matched the earlier SPY and QQQ files exactly: identical closes, with adjusted-return differences of at most 2.1e-6. The VIX close (28.18, +69.7%) is confirmed from Yahoo's ^VIX data.

### Cited Findings
- I re-ran `basic.py`, `events.py` and `summary.py` with `python3 -I <script> <scratchpad>/data`. Results:
  - **SPY ≤-4% one-day drops** (first day of each cluster, 60-trading-day gap; 11 events from 2000 to 2025 with 12-month data, plus Nov 5, 2026 as event 12):
    - QQQ beat SPY over the next 12 months in 8 of 11.
    - 12-month medians: SPY +8.6%, QQQ +16.5%.
    - Worst 12-month results: SPY -14.6% (2001-09-17), QQQ -48.7% (2000-04-14).
    - The 3 cases where QQQ lagged were 2000-04-14, 2001-03-12 and 2001-09-17, all in the dot-com bust.
    - SPY was positive 8 of 11 times, QQQ 7 of 11.
    - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
  - **QQQ first close ≥15% below its trailing 252-day high** (re-armed after QQQ recovers above -5%; 11 events with 12-month data):
    - QQQ beat SPY in 8 of 11.
    - The worst was 2000-04-11: QQQ -58.1% and SPY -21.6% over 12 months.
    - The other laggards were 2008-01-15 (QQQ 0.8 pp behind) and 2022-01-27 (8.7 pp behind).
    - 12-month medians: SPY +26.1%, QQQ +32.2%.
    - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
  - **Rolling 10-year windows** (starting dates 1999-03 to 2016-10-26, 4,439 windows): QQQ's annual growth rate beat SPY's in 88% of windows. The worst gap was -8.1 pp a year (window starting 2000-03-08); the best was +7.4 pp a year (starting 2010-08-27) — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
- Nov 5, 2026 levels:
  - Closes: SPY 733.00 (-4.41%), QQQ 647.05 (-6.49%).
  - Total-return drawdowns from the Oct 6, 2026 record closes (779.09 / 759.66): SPY -5.9%, QQQ -14.8%.
  - The VIX closed at 28.18, up 69.7% from 16.61 on Nov 4, a day when it had fallen 20.3% during a post-election rally.
  - The 13-week T-bill yield (^IRX) was 3.99%.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)
- Data notes:
  - Yahoo's daily history ends Nov 4. The Nov 5 close comes from `meta.regularMarketPrice` (timestamped 21:00 UTC, i.e. the 4:00 pm ET close) and is appended to the series.
  - Treating that price as both close and adjusted close is valid because the last ex-dividend dates for SPY and QQQ were in September; adjusted close equals close for October–November.
  - SPY data start 1993-01-29 and QQQ 1999-03-10, so the common SPY/QQQ sample runs 1999-03-10 to 2026-11-05 (6,959 trading days).
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- Files used for the new work:
  - Data, each in its own new folder under `/tmp/claude-0/-home-user-news-desk/29636437-cb69-55dc-a285-2e079d1cebe8/scratchpad/`: `dl_spy_20261106/spy.json`, `dl_qqq_20261106/qqq.json`, `dl_vix_20261106/vix.json`, `dl_irx_20261106/irx.json`.
  - New scripts in `/tmp/claude-0/-home-user-news-desk/29636437-cb69-55dc-a285-2e079d1cebe8/scratchpad/scripts_lsdca/`: `yload.py`, `check_downloads.py`, `lsdca.py`, `tables_md.py`.
  - Full outputs in `/tmp/claude-0/-home-user-news-desk/29636437-cb69-55dc-a285-2e079d1cebe8/scratchpad/out_lsdca/` (`lsdca_out.txt`, `tables.md`).
  - Re-run with `python3 -I /tmp/claude-0/-home-user-news-desk/29636437-cb69-55dc-a285-2e079d1cebe8/scratchpad/scripts_lsdca/lsdca.py /tmp/claude-0/-home-user-news-desk/29636437-cb69-55dc-a285-2e079d1cebe8/scratchpad`.

### Inferences
- The earlier conclusions stand. Note that all three cases where QQQ lagged after a 4% SPY drop came from a single regime, the 2000–2001 bust, so the "8 of 11" figure is not 11 independent observations.

### Gaps
- None for this question. The data come from Yahoo only and were not cross-checked against a second vendor such as CRSP or Bloomberg.

## Q4. (New) Lump sum vs. 3-month and 6-month DCA entered on each event date, for SPY and QQQ: 12- and 24-month outcomes, win rates and worst cases

### Takeaway
After SPY's first ≥4% one-day drop, lump sum beat a 3-month monthly DCA only 6 of 11 times for both SPY and QQQ, essentially a coin flip and below the roughly two-thirds base rate. Against a 6-month DCA it won 7–8 of 11. Lump sum's median advantage was small (+0.1 to +5.3 pp), but DCA's wins were large when the crash continued; September 2008 was the extreme (DCA ahead by 18–33 pp). DCA did not help in the dot-com bust: its tranches were bought on bounces. For the April 2000 and September 2001 entries its 12-month results were 4–10 pp worse than lump sum; the March 2001 entry was roughly a wash. Entering when QQQ first closed 15% below its 52-week high, lump sum won 8–9 of 11 with median advantages of +3.6 to +13 pp; in the worst case (April 2000) DCA saved only about 3 pp. After VIX spikes lump sum won 10–13 of 18 (first VIX close >28) and 6–7 of 8 (VIX +50% day). DCA's dependable benefit was a shallower interim paper loss in crash-continuation episodes. For example, SPY entered in September 2008 at worst lost 42.5% as a lump sum vs. 25.5% with 6-month DCA. It was not a better 12- or 24-month result.

### Cited Findings
**Method and assumptions**
- Prices: Yahoo adjusted closes (dividends reinvested); trades at the daily close; no transaction costs or taxes. The common SPY/QQQ trading calendar starts 1999-03-10. Horizons are in trading days: 12 months = 252, 24 months = 504 — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- DCA schedules all invest the first tranche at the event-day close, the same moment as the lump sum.
  - 3-month monthly: 3 tranches at day 0, 21 and 42.
  - 6-month monthly: 6 tranches, every 21 days up to day 105.
  - 3-month weekly: 13 tranches every 5 days, the last at day 60.
  - 6-month weekly: 26 tranches every 5 days, the last at day 125.
  - Each tranche invests the cash balance divided by the number of tranches left.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- Idle cash is modeled two ways: 0%, or the 13-week T-bill discount yield (^IRX) accrued daily on an actual/360 basis. The T-bill yield was 5.64% on 2000-04-14, 0.81% on 2008-09-15, 4.18% on 2025-04-03 and 3.99% on 2026-11-05 — [Own calc, Yahoo ^IRX](https://query1.finance.yahoo.com/v8/finance/chart/%5EIRX)
- Event definitions, using the same 60-trading-day cluster rule as `events.py`:
  - E1: SPY ≤-4% one-day drop; 11 events with 12-month data.
  - E2: QQQ first close ≥15% below its 252-day high; 11 events.
  - E3: first VIX close >28 with no close >28 in the prior 60 trading days; 18 events with 12-month data, 20 in total including 2026-03-06 and 2026-11-05.
  - E4: VIX one-day jump ≥+50%; 8 events with data, plus 2026-11-05.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)
- Base-rate check against Vanguard (every trading day as a start date, 12-month horizon):
  - SPY 1993–2025 (8,249 starts): lump sum beat 3-month monthly DCA 67.7% of the time with 0% cash and 65.5% with T-bill cash. Vanguard reports 66.4% for the US and 65% (global) with T-bill interest.
  - Against 6-month monthly DCA: 72.6% / 69.0% (Vanguard US, 6-month split: 73.7%).
  - QQQ 1999–2025 (6,707 starts): 64.6% / 63.2% against 3-month DCA; 71.0% / 69.2% against 6-month DCA.
  - Median lump-sum advantage with T-bill cash: SPY +1.1 pp (3-month) and +2.3 pp (6-month); QQQ +1.5 pp and +3.5 pp.
  - Spread for 6-month DCA (5th / 95th percentile): SPY -7.7 / +10.7 pp; QQQ -12.9 / +16.2 pp.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY); compare [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf)

**Table A – entered on SPY ≤-4% days (first of cluster).** 12-month total return of $1 invested at the event-day close; idle cash earns the T-bill rate. "Paper loss" is the lowest portfolio value within 12 months relative to the amount committed. Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)

| Event date | SPY LS | SPY DCA 3M | SPY DCA 6M | QQQ LS | QQQ DCA 3M | QQQ DCA 6M | SPY paper loss LS / DCA6M | QQQ paper loss LS / DCA6M |
|---|---|---|---|---|---|---|---|---|
| 2000-04-14 | -11.4% | -15.5% | -16.9% | -48.7% | -52.9% | -54.5% | -18.0% / -23.0% | -57.6% / -62.4% |
| 2001-03-12 | +0.4% | -1.2% | -1.2% | -11.5% | -11.6% | -11.1% | -16.8% / -18.2% | -33.4% / -33.1% |
| 2001-09-17 | -14.6% | -18.7% | -19.7% | -28.9% | -36.4% | -38.9% | -22.3% / -26.9% | -31.3% / -41.0% |
| 2008-09-15 | -9.6% | +8.2% | +17.1% | -0.1% | +23.8% | +32.9% | -42.5% / -25.5% | -39.2% / -18.4% |
| 2011-08-04 | +18.3% | +21.7% | +17.1% | +22.3% | +24.4% | +20.2% | -8.1% / -2.4% | -7.6% / -1.5% |
| 2015-08-24 | +18.1% | +13.8% | +12.4% | +20.7% | +14.2% | +11.3% | -2.4% / -7.1% | -1.6% / -9.3% |
| 2018-02-05 | +5.3% | +4.7% | +3.2% | +8.8% | +6.9% | +3.5% | -9.5% / -11.3% | -8.5% / -12.9% |
| 2020-02-27 | +30.2% | +39.1% | +32.0% | +53.6% | +57.6% | +44.0% | -24.6% / -4.1% | -17.7% / -2.9% |
| 2022-05-18 | +8.6% | +10.8% | +9.3% | +16.5% | +17.3% | +16.3% | -8.2% / -7.0% | -10.2% / -10.3% |
| 2022-09-13 | +16.4% | +20.3% | +17.3% | +29.4% | +36.3% | +34.5% | -8.9% / -1.3% | -11.1% / -4.1% |
| 2025-04-03 | +24.2% | +18.6% | +12.6% | +31.2% | +22.0% | +14.3% | -7.5% / -1.2% | -7.7% / -1.2% |
| 2026-11-05 | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

**Table B – entered when QQQ first closed ≥15% below its 252-day high.** Same conventions as Table A. Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)

| Event date | SPY LS | SPY DCA 3M | SPY DCA 6M | QQQ LS | QQQ DCA 3M | QQQ DCA 6M | SPY paper loss LS / DCA6M | QQQ paper loss LS / DCA6M |
|---|---|---|---|---|---|---|---|---|
| 2000-04-11 | -21.6% | -18.5% | -18.8% | -58.1% | -54.6% | -54.9% | -25.8% / -23.2% | -65.2% / -62.5% |
| 2004-08-06 | +17.3% | +12.5% | +9.3% | +21.9% | +15.7% | +9.4% | +0.0% / -0.3% | -0.8% / -3.9% |
| 2006-07-13 | +27.2% | +24.2% | +19.8% | +37.7% | +34.1% | +26.4% | -0.5% / -0.1% | -1.7% / -0.2% |
| 2008-01-15 | -37.5% | -35.3% | -36.4% | -38.3% | -34.4% | -37.1% | -44.5% / -43.6% | -45.0% / -43.9% |
| 2010-06-30 | +29.2% | +25.6% | +19.4% | +32.9% | +29.0% | +19.6% | -1.0% / -0.4% | -0.6% / -0.6% |
| 2011-08-08 | +27.7% | +23.1% | +17.8% | +33.0% | +26.5% | +21.5% | -1.6% / -1.6% | -1.1% / -1.6% |
| 2016-02-08 | +26.1% | +19.1% | +14.8% | +32.2% | +23.6% | +20.3% | -1.4% / -0.2% | -0.3% / -1.9% |
| 2018-12-17 | +27.6% | +22.7% | +18.4% | +34.2% | +28.7% | +22.5% | -7.7% / -1.2% | -8.6% / -1.4% |
| 2020-03-09 | +43.8% | +42.7% | +31.6% | +62.0% | +54.1% | +37.6% | -18.2% / -3.0% | -12.5% / -2.1% |
| 2022-01-27 | -5.6% | -8.1% | -4.2% | -14.3% | -17.1% | -10.7% | -16.4% / -15.1% | -23.3% / -20.1% |
| 2025-04-03 | +24.2% | +18.6% | +12.6% | +31.2% | +22.0% | +14.3% | -7.5% / -1.2% | -7.7% / -1.2% |

**Win-rate summary, 12-month horizon.** "LS wins" means the lump sum ended with more wealth than DCA; "gap" is lump sum minus DCA in pp of the initial amount, with T-bill cash. Some weekly-schedule rows are omitted here; all 32 rows are in `/tmp/claude-0/-home-user-news-desk/29636437-cb69-55dc-a285-2e079d1cebe8/scratchpad/out_lsdca/tables.md`. Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)

| Event set (n) | Asset | DCA schedule | LS wins (cash 0%) | LS wins (T-bill) | Median gap | Largest DCA advantage | Largest LS advantage | Worst 12m LS | Worst 12m DCA |
|---|---|---|---|---|---|---|---|---|---|
| SPY ≤-4% day (11) | SPY | 3M monthly | 6/11 | 6/11 | +0.6pp | -17.7pp (2008-09-15) | +5.7pp (2025-04-03) | -14.6% (2001-09-17) | -18.7% (2001-09-17) |
| SPY ≤-4% day (11) | SPY | 6M monthly | 8/11 | 7/11 | +1.6pp | -26.7pp (2008-09-15) | +11.6pp (2025-04-03) | -14.6% | -19.7% (2001-09-17) |
| SPY ≤-4% day (11) | SPY | 3M weekly | 7/11 | 7/11 | +1.5pp | -21.3pp (2008-09-15) | +7.2pp (2025-04-03) | -14.6% | -18.7% |
| SPY ≤-4% day (11) | SPY | 6M weekly | 9/11 | 8/11 | +2.7pp | -31.3pp (2008-09-15) | +13.3pp (2025-04-03) | -14.6% | -20.4% |
| SPY ≤-4% day (11) | QQQ | 3M monthly | 6/11 | 6/11 | +0.1pp | -23.9pp (2008-09-15) | +9.2pp (2025-04-03) | -48.7% (2000-04-14) | -52.9% (2000-04-14) |
| SPY ≤-4% day (11) | QQQ | 6M monthly | 9/11 | 8/11 | +5.3pp | -33.0pp (2008-09-15) | +16.9pp (2025-04-03) | -48.7% | -54.5% |
| SPY ≤-4% day (11) | QQQ | 3M weekly | 8/11 | 8/11 | +2.8pp | -29.3pp (2008-09-15) | +11.7pp (2025-04-03) | -48.7% | -53.6% |
| SPY ≤-4% day (11) | QQQ | 6M weekly | 8/11 | 7/11 | +5.0pp | -37.2pp (2008-09-15) | +19.3pp (2025-04-03) | -48.7% | -53.7% |
| QQQ first -15% (11) | SPY | 3M monthly | 9/11 | 9/11 | +3.6pp | -3.1pp (2000-04-11) | +7.0pp (2016-02-08) | -37.5% (2008-01-15) | -35.3% (2008-01-15) |
| QQQ first -15% (11) | SPY | 6M monthly | 8/11 | 8/11 | +9.2pp | -2.7pp (2000-04-11) | +12.2pp (2020-03-09) | -37.5% | -36.4% |
| QQQ first -15% (11) | QQQ | 3M monthly | 9/11 | 9/11 | +5.5pp | -3.8pp (2008-01-15) | +9.2pp (2025-04-03) | -58.1% (2000-04-11) | -54.6% (2000-04-11) |
| QQQ first -15% (11) | QQQ | 6M monthly | 8/11 | 8/11 | +11.7pp | -3.5pp (2022-01-27) | +24.3pp (2020-03-09) | -58.1% | -54.9% |
| QQQ first -15% (11) | QQQ | 6M weekly | 8/11 | 8/11 | +13.1pp | -5.9pp (2022-01-27) | +25.9pp (2020-03-09) | -58.1% | -54.3% |
| VIX first >28 (18) | SPY | 3M monthly | 12/18 | 12/18 | +0.9pp | -8.8pp (2020-02-27) | +9.6pp (2016-02-11) | -24.2% (2008-07-14) | -25.9% (2008-07-14) |
| VIX first >28 (18) | SPY | 6M monthly | 11/18 | 11/18 | +1.2pp | -12.6pp (2008-07-14) | +13.4pp (2016-02-11) | -24.2% | -20.1% (2000-04-05) |
| VIX first >28 (18) | QQQ | 3M monthly | 11/18 | 11/18 | +2.3pp | -6.0pp (2002-06-26) | +10.1pp (2016-02-11) | -62.7% (2000-04-05) | -60.1% (2000-04-05) |
| VIX first >28 (18) | QQQ | 6M monthly | 12/18 | 12/18 | +5.2pp | -17.4pp (2008-07-14) | +17.2pp (1999-05-25) | -62.7% | -59.9% |
| VIX +50% day (8) | SPY | 3M monthly | 7/8 | 7/8 | +2.8pp | -0.6pp (2021-11-26) | +10.6pp (2025-04-04) | -12.4% (2021-11-26) | -11.9% (2021-11-26) |
| VIX +50% day (8) | SPY | 6M monthly | 6/8 | 6/8 | +6.2pp | -1.9pp (2024-12-18) | +18.3pp (2025-04-04) | -12.4% | -10.6% |
| VIX +50% day (8) | QQQ | 3M monthly | 6/8 | 6/8 | +2.1pp | -2.9pp (2021-11-26) | +14.8pp (2025-04-04) | -27.3% (2021-11-26) | -24.4% (2021-11-26) |
| VIX +50% day (8) | QQQ | 6M monthly | 6/8 | 6/8 | +5.2pp | -5.9pp (2021-11-26) | +24.8pp (2025-04-04) | -27.3% | -21.4% |

**24-month horizon** (T-bill cash, monthly schedules). The 2025 event has no 24-month data yet, so counts drop by one.
- SPY ≤-4% days: lump sum beat 3-month DCA 5 of 10 times (median -1.0 pp) and 6-month DCA 6 of 10 (+1.3 pp). Worst lump sum -23.9% vs. worst DCA -25.1% / -25.2%, all for the 2001-03-12 entry. Largest DCA advantage: 2008-09-15, by 19.3 / 29.1 pp — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- QQQ entered on SPY ≤-4% days: lump sum won 5 of 10 (median -0.6 pp) and 7 of 10 (+3.5 pp). Worst lump sum -58.9% (2000-04-14) vs. worst DCA -62.3% / -63.6%. Largest DCA advantage: 2008-09-15, by 27.5 / 38.0 pp — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
- QQQ first -15% events: lump sum won 8 of 10 for SPY (+3.4 pp) and 7 of 10 (+9.3 pp); for QQQ 8 of 10 (+5.1 pp) and 7 of 10 (+12.5 pp). Worst QQQ lump sum -64.9% vs. DCA -61.9% / -62.2% (2000-04-11 entry) — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
- VIX first close >28: lump sum won 11 of 17 / 10 of 17 for SPY and 10 of 17 / 11 of 17 for QQQ. VIX +50% days: SPY 5 of 6 / 5 of 6, QQQ 4 of 6 / 5 of 6. The 2007-02-27 entry is the worst 24-month case: SPY -43.5% lump sum vs. -45.0% / -45.8% DCA — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)
- The 12-month and 24-month winner was the same in 344 of 344 event/asset/schedule cases. This is expected: once DCA is fully invested, the ratio of lump-sum wealth to DCA wealth is fixed, so the outcome is decided within the first 2–6 months — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)

**Interim paper loss: the lowest portfolio value within 12 months vs. the amount committed** (T-bill cash, 6-month monthly DCA)

| Event set | Asset | Median: LS | Median: DCA | Worst: LS | Worst: DCA | DCA shallower |
|---|---|---|---|---|---|---|
| SPY ≤-4% days | SPY | -9.5% | -7.1% | -42.5% | -26.9% | 6/11 |
| SPY ≤-4% days | QQQ | -11.1% | -10.3% | -57.6% | -62.4% | 6/11 |
| QQQ first -15% | SPY | -7.5% | -1.2% | -44.5% | -43.6% | 9/11 |
| QQQ first -15% | QQQ | -7.7% | -1.9% | -65.2% | -62.5% | 7/11 |
| VIX first close >28 | SPY | -10.6% | -10.4% | -43.7% | -34.4% | 10/18 |
| VIX first close >28 | QQQ | -8.5% | -10.1% | -66.0% | -63.4% | 10/18 |
| VIX +50% day | SPY | -3.8% | -9.1% | -21.1% | -19.5% | 4/8 |
| VIX +50% day | QQQ | -5.1% | -8.8% | -33.0% | -27.5% | 4/8 |

Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)

**Base rates for comparison: every trading day as a start date** (T-bill cash, 12 months; overlapping start days, so the effective sample is roughly the number of episodes)
- Days with VIX close >28 (817 starts, about 18 episodes): lump sum beat 3-month DCA 71.1% of the time for SPY and 71.0% for QQQ; 6-month DCA 71.5% (SPY) and 81.0% (QQQ). Median gaps: +2.6 / +3.5 pp (3-month) and +5.0 / +8.1 pp (6-month). Bad cases (5th percentile): about -8 to -10 pp. By comparison, all days 1999–2025 give 63.9% (SPY) and 63.2% (QQQ) against 3-month DCA, and 66.4% / 69.2% against 6-month DCA — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)
- Days with VIX >40 (192 starts, about 9 episodes): 59.4% (SPY) / 66.1% (QQQ) against 3-month DCA; 63.5% / 84.4% against 6-month DCA — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)
- Every SPY ≤-4% day (45 starts, about 11 episodes): 66.7% / 66.7% against 3-month DCA and 64.4% / 71.1% against 6-month DCA. The tails are wide: 5th percentile about -26 to -28 pp for 6-month DCA — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- Every day with QQQ ≥15% below its 252-day high (1,441 starts, about 11 episodes): lump sum won only 48.1% (SPY) / 48.0% (QQQ) against 3-month DCA and 41.8% / 50.7% against 6-month DCA. Most of these days fall in the long 2000–02 and 2008 bear markets. Counting only starts from 2003 onward (763 starts), QQQ lump sum won 73.5% and SPY 61.3% against 6-month DCA — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
- Days with QQQ 10–20% below its 252-day high (719 starts, about 26 episodes): 65.4% (SPY) / 62.7% (QQQ) against 3-month DCA; 65.4% / 69.1% against 6-month DCA — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)

### Inferences
- In the historical record, a first ≥4% down day is where DCA has done relatively best: lump sum won only about 55% against 3-month DCA. The first big down day was often not the bottom (Lehman in September 2008, early COVID in February 2020, August 2011 before the US downgrade, and mid-bear-market days in 2022). Even so, lump sum's median advantage was positive and DCA did not reduce the worst 12-month outcome. In 2000–01 it made the worst outcome worse, because tranches were bought on relief rallies.
- At volatility-spike and "QQQ first -15%" signals, lump sum won more often than its unconditional base rate, and by larger margins. Higher subsequent returns raise the cost of waiting, and they outweigh the higher chance of further declines.
- What DCA reliably buys is a smaller interim paper loss when a crash continues: 2008 for SPY was -42.5% for lump sum vs. -25.5% with 6-month DCA, and 2020 was -24.6% vs. -4.1%. This is the regret and plan-commitment benefit described by Vanguard and Statman. It is not reliable in drawn-out tech busts: in 2000–01 QQQ DCA had deeper paper losses than lump sum.
- If an investor chooses DCA, a 3-month schedule costs much less in the median case than a 6-month one. With monthly tranches and T-bill cash, QQQ's median lump-sum advantage was +0.1 to +5.5 pp against 3-month DCA and +5.2 to +11.7 pp against 6-month DCA, across the four signals. That matches Vanguard's advice to keep the period short.
- The T-bill assumption matters little at today's 3.99% yield. Moving from 0% cash to T-bill cash changes event win counts by at most one, and lowers base-rate win rates by about 1–4 pp.

### Gaps
- I did not model other DCA variants, such as investing only on further dips, an all-at-once "buy-the-dip" rule, or a 12-month DCA. I also did not model taxes, fees or bid-ask spreads.
- Effective sample sizes are small (8–18 episodes, many from the same regimes). No formal significance tests were run; with this few episodes, differences of 1–2 wins are noise.

## Q5. (New) Forward 1-, 3-, 6- and 12-month returns of SPY and QQQ after the VIX closes above about 28 or jumps ≥50% in a day

### Takeaway
After the first VIX close above 28 (18 episodes with 12-month data since 1999), the median 12-month total return was +10.5% for SPY (positive 12 of 18 times) and +20.0% for QQQ (13 of 18), and QQQ beat SPY 14 of 18 times. The losses were concentrated in the 2000–02 bust, 2008 and late 2021, when QQQ's 12-month return fell as low as -62.7%. After one-day VIX jumps of +50% or more (8 prior episodes), SPY was higher one month later in all 8 cases (median +4.0%) and higher 12 months later in 7 of 8 (median +17.9%); QQQ was higher 12 months later in 7 of 8 (median +14.7%). The only loser was Nov 26, 2021 (Omicron), which led into the 2022 bear market: SPY -12.4%, QQQ -27.3%. Nov 5, 2026 is only the fourth day since 1999 with both a ≥4% SPY drop and a ≥50% VIX jump. The three earlier cases (2011, 2018, 2025) were all up at every horizon, but three is too few to rely on.

### Cited Findings
**Table C – after the first VIX close >28 (no close >28 in the prior 60 trading days).** Total return from the event-day close; 1m/3m/6m/12m = 21/63/126/252 trading days. Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)

| Date | VIX close | SPY day | SPY 1m | SPY 3m | SPY 6m | SPY 12m | QQQ 1m | QQQ 3m | QQQ 6m | QQQ 12m |
|---|---|---|---|---|---|---|---|---|---|---|
| 1999-05-25 | 28.9 | -1.6% | +2.7% | +6.5% | +11.1% | +8.1% | +9.9% | +20.8% | +49.7% | +50.1% |
| 2000-04-05 | 28.4 | -0.6% | -3.8% | -2.1% | -3.2% | -22.1% | -8.7% | -6.1% | -14.5% | -62.7% |
| 2000-10-12 | 30.5 | -2.5% | +2.6% | -0.5% | -11.2% | -18.3% | -4.5% | -16.5% | -46.4% | -55.6% |
| 2001-09-06 | 28.6 | -2.6% | -0.3% | +3.4% | +5.4% | -18.1% | +2.4% | +21.6% | +8.7% | -32.7% |
| 2002-06-26 | 28.4 | +0.2% | -12.4% | -13.3% | -7.7% | +2.8% | -11.6% | -14.7% | -1.2% | +17.8% |
| 2007-08-10 | 28.3 | -0.5% | +1.9% | +2.2% | -6.6% | -7.9% | +3.5% | +9.5% | -6.6% | +1.3% |
| 2008-07-14 | 28.5 | -0.9% | +5.4% | -27.5% | -28.2% | -24.2% | +8.1% | -29.1% | -33.1% | -18.8% |
| 2010-05-06 | 32.8 | -3.3% | -6.6% | +0.4% | +7.3% | +20.7% | -4.9% | +0.9% | +14.6% | +26.4% |
| 2011-03-16 | 29.4 | -1.9% | +4.7% | +1.1% | -4.5% | +13.9% | +4.9% | +0.4% | +2.6% | +24.3% |
| 2011-08-04 | 31.7 | -4.7% | -2.0% | +3.6% | +13.2% | +18.3% | -1.6% | +5.3% | +15.2% | +22.3% |
| 2015-08-21 | 28.0 | -3.0% | -1.5% | +6.0% | -1.7% | +12.9% | +1.9% | +11.3% | -0.3% | +15.9% |
| 2016-02-11 | 28.1 | -1.3% | +10.7% | +13.5% | +20.8% | +29.3% | +10.5% | +10.0% | +22.0% | +33.4% |
| 2018-02-05 | 37.3 | -4.2% | +3.4% | +1.5% | +8.8% | +5.3% | +6.8% | +5.3% | +15.0% | +8.8% |
| 2018-12-20 | 28.4 | -1.6% | +7.2% | +14.1% | +20.6% | +33.0% | +6.8% | +17.6% | +24.4% | +40.3% |
| 2020-02-27 | 39.2 | -4.5% | -14.3% | +2.4% | +18.0% | +30.2% | -9.7% | +12.1% | +42.5% | +53.6% |
| 2021-11-26 | 28.6 | -2.2% | +4.3% | -4.5% | -8.9% | -12.4% | +2.8% | -11.2% | -20.8% | -27.3% |
| 2024-08-05 | 38.6 | -2.9% | +6.5% | +10.7% | +17.5% | +23.7% | +5.8% | +12.1% | +21.4% | +31.5% |
| 2025-04-03 | 30.0 | -4.9% | +5.0% | +16.0% | +25.4% | +24.2% | +7.8% | +22.6% | +34.1% | +31.2% |
| 2026-03-06 | 29.5 | -1.3% | -1.7% | +10.0% | +15.2% | n/a | -1.7% | +17.7% | +20.2% | n/a |
| 2026-11-05 | 28.2 | -4.4% | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

Summary of Table C (median; number positive; minimum):

| Horizon | SPY median | SPY positive | SPY min | QQQ median | QQQ positive | QQQ min |
|---|---|---|---|---|---|---|
| 1m | +2.6% | 11/19 | -14.3% | +2.8% | 12/19 | -11.6% |
| 3m | +2.4% | 14/19 | -27.5% | +9.5% | 14/19 | -29.1% |
| 6m | +7.3% | 11/19 | -28.2% | +14.6% | 12/19 | -46.4% |
| 12m | +10.5% | 12/18 | -24.2% | +20.0% | 13/18 | -62.7% |

Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX). Means: SPY +0.6 / +2.3 / +4.8 / +6.6%; QQQ +1.5 / +4.7 / +7.8 / +8.9%. QQQ beat SPY over 12 months in 14 of 18. Two earlier SPY-only events: 1997-10-27 (SPY +9.2 / +12.5 / +26.2 / +24.4%) and 1998-08-04 (-7.2 / +4.9 / +19.9 / +23.6%) — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)

**Table D – after a one-day VIX jump of +50% or more (first of cluster).** Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)

| Date | VIX close | SPY day | SPY 1m | SPY 3m | SPY 6m | SPY 12m | QQQ 1m | QQQ 3m | QQQ 6m | QQQ 12m |
|---|---|---|---|---|---|---|---|---|---|---|
| 2007-02-27 | 18.3 | -3.9% | +2.1% | +9.6% | +6.2% | +0.9% | +0.8% | +8.4% | +11.0% | +2.9% |
| 2011-08-08 | 48.0 | -6.5% | +7.2% | +12.4% | +21.5% | +27.7% | +8.0% | +14.5% | +23.5% | +33.0% |
| 2018-02-05 | 37.3 | -4.2% | +3.4% | +1.5% | +8.8% | +5.3% | +6.8% | +5.3% | +15.0% | +8.8% |
| 2021-01-27 | 37.2 | -2.4% | +1.6% | +11.8% | +18.0% | +17.3% | -1.7% | +6.3% | +14.8% | +8.4% |
| 2021-11-26 | 28.6 | -2.2% | +4.3% | -4.5% | -8.9% | -12.4% | +2.8% | -11.2% | -20.8% | -27.3% |
| 2024-08-05 | 38.6 | -2.9% | +6.5% | +10.7% | +17.5% | +23.7% | +5.8% | +12.1% | +21.4% | +31.5% |
| 2024-12-18 | 27.6 | -3.0% | +3.8% | -1.5% | +4.5% | +18.6% | +3.1% | -4.7% | +5.0% | +20.7% |
| 2025-04-04 | 45.3 | -5.9% | +10.6% | +23.1% | +33.7% | +35.3% | +13.9% | +30.8% | +44.1% | +44.1% |
| 2026-11-05 | 28.2 | -4.4% | n/a | n/a | n/a | n/a | n/a | n/a | n/a | n/a |

Summary of Table D:

| Horizon | SPY median | SPY positive | SPY min | QQQ median | QQQ positive | QQQ min |
|---|---|---|---|---|---|---|
| 1m | +4.0% | 8/8 | +1.6% | +4.4% | 7/8 | -1.7% |
| 3m | +10.1% | 6/8 | -4.5% | +7.4% | 6/8 | -11.2% |
| 6m | +13.2% | 7/8 | -8.9% | +14.9% | 7/8 | -20.8% |
| 12m | +17.9% | 7/8 | -12.4% | +14.7% | 7/8 | -27.3% |

Source: [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX). QQQ beat SPY over 12 months in 6 of 8. Requiring the VIX also to close at 25 or higher drops 2007-02-27 and leaves 7 events, with 12-month medians of +18.6% (SPY) and +20.7% (QQQ), 6 of 7 positive.

**Context and related event sets**
- Largest one-day VIX % jumps since 1993 (Yahoo closes):
  1. 2018-02-05: +115.6% (17.31 → 37.32)
  2. 2024-12-18: +74.0%
  3. 2026-11-05: +69.7% (16.61 → 28.18)
  4. 2024-08-05: +64.9%
  5. 2007-02-27: +64.2%
  6. 2021-01-27: +61.6%
  7. 2021-11-26: +54.0%
  8. 2025-04-04: +50.9%
  9. 2011-08-08: +50.0%
  10. 2016-06-24: +49.3%

  No single-day close-to-close jump in 2008 or 2020 reached +50%. Nov 5 started from a low base: the VIX had fallen 20.3% on Nov 4 — [Own calc, Yahoo ^VIX](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)
- Base rates (all days from 1999-03-10, overlapping windows), median return / share positive:

  | Horizon | SPY | QQQ |
  |---|---|---|
  | 1m | +1.3% / 64% | +1.6% / 63% |
  | 3m | +3.5% / 69% | +4.5% / 69% |
  | 6m | +6.3% / 73% | +9.1% / 73% |
  | 12m | +12.8% / 78% | +16.8% / 79% |

  [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- All days with VIX >28 (11.8% of days; overlapping windows): 12-month median SPY +22.2% (82% positive, minimum -42.3%) and QQQ +33.1% (83% positive, minimum -62.7%). Medians at 1/3/6 months: SPY +3.3 / +6.7 / +12.6%, QQQ +4.3 / +9.9 / +19.1%. Counting every high-VIX day lets the deepest crisis periods (2008–09, 2020) dominate, which is why these medians sit above the first-signal medians — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/%5EVIX)
- Same day with SPY ≤-4% and VIX ≥+50%: 2011-08-08, 2018-02-05 and 2025-04-04, before 2026-11-05. 12-month returns: SPY +27.7%, +5.3%, +35.3%; QQQ +33.0%, +8.8%, +44.1%. All three were positive at 1, 3, 6 and 12 months — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- QQQ ≤-6% one-day drops (first of cluster; 8 with data: 2000-01-04, 2000-04-10, 2000-09-21, 2001-09-17, 2008-09-29, 2011-08-08, 2020-03-09, 2025-04-04): 12-month median SPY -2.4% (3 of 8 positive) and QQQ -8.3% (4 of 8 positive, minimum -67.5%). The four cases after 2001 were all positive for QQQ (+12.2%, +33.0%, +62.0%, +44.1%). Nov 5, 2026 (-6.49%) is QQQ's first such day since April 2025 — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
- QQQ first close ≥10% below its 252-day high (35 events; 32 with 12-month data):
  - 12-month median: QQQ +22.2% and SPY +21.1%, both positive 27 of 32 times; QQQ beat SPY 20 of 32.
  - 6-month: QQQ median +16.7% (mean +13.6%, positive 28 of 33).
  - Worst: QQQ -66.3% over 12 months (2000-04-03 entry).
  - This episode's -10% signal fired on 2026-11-02. The March and July 2026 signals were followed by rallies: QQQ +28.8% three months after 2026-03-27, and +9.1% three months after 2026-07-29.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
- Which event sets Nov 5, 2026 triggered:
  - SPY ≤-4% day: yes, the first since April 2025.
  - First VIX close >28: yes, the first since the March 2026 episode.
  - VIX +50% day: yes.
  - QQQ ≤-6% day: yes.
  - QQQ first close ≥15% below its 52-week high: no. QQQ is at -14.8%, so this signal has not fired.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)

### Inferences
- The best-matched comparison groups (VIX +50% days, and same-day SPY ≤-4% plus VIX +50%) have been followed by mostly positive 1–12-month returns. But they include only 3–8 episodes, nearly all after 2007 and therefore mostly in the post-2009 bull market, so they likely overstate the odds.
- Groups that include the 2000–02 bust (first VIX close >28, QQQ ≤-6% days) show much worse QQQ tails (-55% to -68% over 12 months). If the current AI-led selloff turns out to be the start of a dot-com-style deflation, the relevant history is those cases, not 2011/2018/2025. The data cannot tell which regime we are in.
- After VIX signals, QQQ's median outperformance of SPY held up (14 of 18 for first VIX close >28; 6 of 8 for VIX +50%). Its downside was 2–3 times SPY's in the bad cases.

### Gaps
- The VIX data start in 1993 in my download, so VIX +50% jumps from 1990–1992, if any, are not checked. QQQ history starts in March 1999, so pre-1999 events have SPY only.
- I did not compute intraday-based or 3-day VIX spike definitions; media studies often use them, which partly explains why their counts differ from mine.

## Q6. What are the key caveats (small samples, overlapping events, regime dependence)?

### Takeaway
Every conditional result above rests on 3–18 episodes, many of them clustered in the same few regimes, so the win rates are not stable estimates. The robust findings are structural: lump sum wins about two-thirds of the time unconditionally, DCA mainly reduces interim losses and regret, and the outcome is decided within the DCA window. The conditional numbers are not reliable forecasts.

### Cited Findings
- Small samples: 11 SPY ≤-4% events, 11 QQQ -15% events, 18 VIX >28 events and 8 VIX +50% events with 12-month data. Win counts move by 1–2 depending on the schedule (weekly or monthly) and the cash assumption — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- Overlap and clustering:
  - Several events belong to the same episode: 2011-08-04/08, 2018-02-05 and 2025-04-03/04 appear in several event sets.
  - Some 12-month windows overlap, for example 2000-04-05/11/14 and 2022-05-18/09-13.
  - The all-days base rates count thousands of overlapping start days but represent only about 9–26 episodes.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- Regime dependence: QQQ's laggard and catastrophic cases are almost all from 2000–2002, with 2008 and 2022 as smaller tails. Starting the sample in 2003 raises QQQ lump sum's win rate against 6-month DCA (start days with QQQ ≥15% below its high) from 50.7% to 73.5% — [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)
- How the window is measured matters. CNBC's Nasdaq correction averages are measured from the correction bottom (+9.41% at 3 months, +17.03% at 6 months) and cannot be achieved by a buyer today — [CNBC](https://www.cnbc.com/2026/11/05/nasdaq-drops-into-correction-territory-heres-what-typically-happens-next.html)
- About 37% of Nasdaq corrections since 1971 became bear markets (Dow Jones Market Data, as cited) — [Motley Fool](https://www.fool.com/investing/2026/11/05/nasdaq-stock-market-correction-history-says-this-is-what-happens-next/)
- Vanguard's own caveat: lump sum underperforms cost averaging in the worst (5th-percentile) outcomes, and higher cash yields narrow lump sum's edge. Today's 13-week T-bill yield is 3.99% — [Vanguard 2023](https://corporate.vanguard.com/content/dam/corp/research/pdf/cost_averaging_invest_now_or_temporarily_hold_your_cash.pdf); [Own calc, Yahoo ^IRX](https://query1.finance.yahoo.com/v8/finance/chart/%5EIRX)
- Modeling assumptions:
  - Buying exactly at the event-day close assumes the investor acts at 4 pm on the signal day; a next-day entry would change individual results.
  - Yahoo adjusted closes are the total-return proxy, with no fees or taxes.
  - ^IRX is a discount yield, used as an approximation for T-bill cash.
  - The 60-day cluster rule and the -15% / 28 thresholds were chosen with knowledge of the current event (QQQ -14.8%, VIX 28.18), which creates some data-snooping risk.
  - [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/SPY)
- Index mismatch: media statistics refer to the Nasdaq Composite or the S&P 500 index (price only), while these backtests use the SPY and QQQ ETFs (Nasdaq-100, total return). QQQ's 1999 launch, just before the 2000 peak, weighs heavily on its history — [Motley Fool](https://www.fool.com/investing/2026/11/05/nasdaq-stock-market-correction-history-says-this-is-what-happens-next/); [Own calc, Yahoo data](https://query1.finance.yahoo.com/v8/finance/chart/QQQ)

### Inferences
- For the report: present lump sum's historical edge as "usually, modestly." Present DCA as insurance against the scenario where Nov 5 is not the low (2008-, 2020- or 2000-style continuation). Its median cost (lump sum minus DCA, T-bill cash, monthly tranches) ranged from +0.1 to +5.5 pp for a 3-month schedule and from +1.2 to +11.7 pp for a 6-month schedule across the four signals and two ETFs. Unconditionally it was about +1–1.5 pp (3-month) and +2–3.5 pp (6-month).
- The one hard conclusion is behavioral: the larger historical cost comes from never investing at all. Vanguard reports that lump sum and cost averaging both beat cash about 70% of the time, and Morningstar finds performance-chasing investors lag a mechanical schedule.

### Gaps
- No bootstrap or statistical significance analysis was done.
- Valuation (P/E, AI concentration) and macro conditioning (rates, recessions) were not tested; they may matter more than the volatility signals but were outside this scope.
