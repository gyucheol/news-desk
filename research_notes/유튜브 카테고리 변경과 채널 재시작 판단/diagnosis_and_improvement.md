# 특정 영상 조회수 급감의 진단과 개선 방법 — YouTube Studio 분석·공식 도구 기준 (2026년 11월 6일 조사)

> 증거 라벨: [공식/Official] = YouTube 고객센터·공식 블로그 원문 / [2차/Secondary] = YouTube 직원 발언을 제3 매체가 전한 것 / [제3자/Third-party] = 외부 기업·교육자 의견·실험 / [커뮤니티] = 개인 일화 / [추론/Inference] = 본 조사자의 추론.
> 고객센터(support.google.com) 페이지들은 게시·수정일이 본문에 없고 하단에 "©2026 Google"만 표기됨 → 모두 "날짜 표기 없음, 2026-11-06 접속"으로 기록. 따옴표 인용은 WebFetch로 확인한 원문이며, 도구의 인용 길이 제한으로 일부 문장은 "…"로 잘라 인용함.
> **UI 변경 경고 [공식]:** "Starting July 2026, we are gradually rolling out an updated YouTube Studio experience. … your Analytics page may look different than before." (한국어판: "2026년 7월부터 업데이트된 YouTube 스튜디오 환경이 단계적으로 출시됩니다.") — 아래 메뉴 경로·라벨은 계정에 따라 다르게 보일 수 있음. — [Get started with YouTube Analytics](https://support.google.com/youtube/answer/9002587?hl=en) / [한국어판](https://support.google.com/youtube/answer/9002587?hl=ko)

## Q1. 특정 영상의 조회수 하락을 진단하려면 YouTube Studio에서 어떤 보고서·측정항목을 봐야 하나 (공식 정의·메뉴 경로·한국어 라벨)

### Takeaway
진단은 채널 전체가 아니라 **동영상별 분석**(콘텐츠 → 해당 동영상 → 분석)에서 해야 하며, 핵심은 개요(일반적인 실적) → 도달범위(노출수·노출 클릭률·트래픽 소스) → 참여도(평균 시청 지속 시간·시청 지속 시간 보고서·주요 순간) → 시청자층(신규/일반/정기 시청자) 탭이다. 2026년에는 ① 7월부터 Studio UI가 단계적으로 바뀌고 있고 ② **2026년 8월 24일부터 공개 조회수가 '재생 시작 시점' 기준으로 집계**되며 예전 정의는 '유효 조회수(engaged views)'로 분리됐으므로, 영상 간 비교 시 같은 정의의 지표를 써야 한다.

### Cited Findings
**A. 분석 탭 구조와 메뉴 경로**
- [공식] 채널 분석: "In the left Menu, select Analytics" → "The Overview tab will open by default." — [Get an overview of channel performance](https://support.google.com/youtube/answer/9314414?hl=en) (날짜 표기 없음)
- [공식] 동영상 분석: YouTube 스튜디오 로그인 → 왼쪽 메뉴 **콘텐츠** → 동영상에 마우스를 올리고 **분석** 선택. 한국어판 문구: "왼쪽 메뉴에서 **콘텐츠**"를 선택한 뒤 동영상 위에 마우스를 가져가 **분석** 선택. — [9002587 영문](https://support.google.com/youtube/answer/9002587?hl=en), [한국어판](https://support.google.com/youtube/answer/9002587?hl=ko)
- [공식] 각 탭 설명 (영문 원문 / 한국어 라벨):
  - Overview/**개요**: "The Overview tab shows you a summary of how your channel and videos are performing." "You can view reports such as Realtime and Typical performance." (한국어판: "실시간 실적 및 일반적인 실적" 보고서)
  - Content/**콘텐츠**(채널 단위): "Channel Impressions are segmented by New and Returning users."
  - Reach/**도달범위**: "The Reach tab gives you a summary of how your audience is discovering your channel." "The key metrics card shows your impressions, impressions click-through-rate, views, and unique viewers." (한국어 라벨: 노출수, 노출 클릭률, 조회수, 순 시청자 수)
  - Engagement/**참여도**: "The Engagement tab gives you a summary of how long your audience is watching your videos." "The key metrics card shows your watch time and average view duration." (한국어 라벨: 시청 시간, 평균 시청 지속 시간, '유효 조회수')
  - Audience/**시청자층**: "The Audience tab shows you who is watching your videos." "You can also view what percentage of your audience are new, casual, and regular viewers."
  - Trends/**트렌드**: "The Trends tab gives you a summary of what your audience and viewers across YouTube are searching for."
  - Advanced Mode/**고급 모드**: "…you can use Advanced Mode to view an expanded analytics report…" (특정 데이터 확인·실적 비교·내보내기)
  — 출처 모두 [9002587 영문](https://support.google.com/youtube/answer/9002587?hl=en) / [한국어판](https://support.google.com/youtube/answer/9002587?hl=ko) (날짜 표기 없음). ※ 한국어판에서 engaged views가 "유효 조회수"로 표기됨(Studio 실제 UI 라벨은 미확인).

**B. 개요 탭: '일반적인 실적(Typical performance)'·실시간**
- [공식] "You may see personalized overview reports that show comparisons to your typical performance." "These insights will explain why your views may be higher or lower than usual." — [9314414](https://support.google.com/youtube/answer/9314414?hl=en)
- [공식] 최신 콘텐츠 카드: "This report gives you a snapshot of your latest video's views." "The report also gives you info on impressions click-through rate and average view duration." — [9314414](https://support.google.com/youtube/answer/9314414?hl=en)
- [공식] 실시간: "The Realtime report gives you early insights into the performance of your recently published videos." "You can view the expanded analytics report to compare 60 minute and 48 hour performance." — [9314414](https://support.google.com/youtube/answer/9314414?hl=en)
- [공식] '일반적인 실적'의 계산식(기준 영상 수·시간 창)은 공식 문서에서 확인되지 않음. 유일하게 정의된 기준선은 **일반적인 시청 지속 시간(typical retention)**: "the engagement that the last 10 of your videos of a similar length have maintained." — [Content tab analytics tips](https://support.google.com/youtube/answer/12942217?hl=en&co=YOUTUBE._YTVideoType%3Dvideo)

**C. 도달범위 탭: 노출수·노출 클릭률·노출 기반 조회수 (2026년 문서는 'thumbnail impressions' 용어 사용)**
- [공식] 페이지 제목 "Check your YouTube thumbnail impressions and watch time". 정의:
  - Thumbnail impressions: "How many times your thumbnails were shown to viewers on YouTube through registered thumbnail impressions."
  - Thumbnail impressions click-through-rate: "How often viewers watched a video after seeing a thumbnail."
  - Views from thumbnail impressions: "Views that originated from thumbnail impressions for the selected date range."
  - Watch time from thumbnail impressions: "Watch time that originated from thumbnail impressions for the selected date range."
  - 메뉴: Studio → Analytics → 상단 Content (동영상 단위는 Reach 탭), 보고서명 "Impressions and how they led to watch time". 한국어 보고서명: "노출수 및 노출수가 시청 시간에 미치는 영향도".
  — [9314486](https://support.google.com/youtube/answer/9314486?hl=en), 한국어 라벨은 [9314355 한국어 데스크톱판](https://support.google.com/youtube/answer/9314355?hl=ko&co=GENIE.Platform%3DDesktop) (날짜 표기 없음)
- [공식] CTR FAQ의 정의: "Impressions click-through rate measures how often viewers watched a video after seeing a registered impression on YouTube." (한국어: "노출 클릭률은 YouTube에 등록된 노출이 표시된 후 시청자가 동영상을 시청한 빈도를 측정합니다.") — [7628154 영문](https://support.google.com/youtube/answer/7628154?hl=en), [한국어판](https://support.google.com/youtube/answer/7628154?hl=ko)
- [공식] 키 측정항목 카드는 보고서보다 자주 갱신됨: "This difference is because the data in the key metrics card is updated more often." 카드 데이터는 게시 후 몇 시간 내 제공. — [9314486](https://support.google.com/youtube/answer/9314486?hl=en)
- ⚠️ 용어 변경 가능성 [추론]: 2026년 고객센터는 "impressions" 대신 "thumbnail impressions"로 표기 → Studio UI 라벨도 바뀌었을 수 있음(한국어 UI 라벨 미확인).

**D. 트래픽 소스 (도달범위 탭 "시청자가 이 동영상을 찾는 방법" 카드)**
- [공식] 데스크톱 경로(한국어판): YouTube 스튜디오 로그인 → 왼쪽 메뉴 **콘텐츠** → 동영상에서 **분석** → 상단 메뉴 **도달범위**. 도달범위 탭 보고서 한국어 라벨: "시청자가 이 동영상을 찾는 방법", "외부 사이트 또는 앱", "이 동영상을 추천하는 콘텐츠", "이 동영상을 추천하는 재생목록", "전송된 종 모양 아이콘 알림", "YouTube 검색어". — [9314355 한국어 데스크톱판 "YouTube 동영상 도달범위 이해하기"](https://support.google.com/youtube/answer/9314355?hl=ko&co=GENIE.Platform%3DDesktop)
- [공식] 트래픽 소스 정의 (영문은 Android판 페이지 "Understand your YouTube video reach - Android phone & tablet"에서 확인, 한국어는 데스크톱판):
  - Browse features / **탐색 기능**: "Traffic from the Home, subscriptions, Watch Later, Trending/Explore, and other browsing features." / "홈, 구독, 나중에 볼 동영상, 인기 급상승/탐색 및 기타 둘러보기 기능에서 발생한 트래픽입니다."
  - Suggested videos / **추천 동영상**: "Traffic from suggestions that appear next to or after other videos, and from links in video descriptions." / 한국어판은 "추천 동영상에서 발생한 트래픽입니다."로 더 짧음(버전 간 차이).
  - YouTube search / **YouTube 검색**: "Traffic from YouTube search results." / "YouTube 검색 결과에서 발생한 트래픽입니다."
  - Channel pages / **채널 페이지**: "Traffic from your YouTube channel or other YouTube channels."
  - Notifications / **알림**: "Traffic from notifications and emails sent to your subscribers." (영문판에는 "Notifications to belled subscribers", "Other app notifications" 하위 항목도 있음)
  - Playlists / **재생목록**: "Traffic from any playlist that included one of your videos."
  - End screens / **최종 화면**, Video cards / **동영상 카드**, Shorts, Other YouTube features / **기타 YouTube 기능**, YouTube advertising / **YouTube 광고**, Campaign cards / **캠페인 카드**, Remixed video / **리믹스 동영상**, Sound pages / **사운드 페이지**, Product pages / **제품 페이지**
  - External / **외부 소스**: "Traffic from websites and apps that have your YouTube video embedded or linked to." / "YouTube 동영상을 퍼가거나 동영상으로 연결되는 링크를 추가한 웹사이트 및 앱에서 발생한 트래픽입니다."
  - Direct or unknown / **직접 입력 또는 알 수 없는 소스**: "Traffic from direct URL entry, bookmarks, signed out viewers, and unidentified apps." / "URL 직접 입력, 북마크, 로그아웃 상태의 시청자, 미확인 앱에서 발생한 트래픽입니다."
  — [9314355 영문(Android)](https://support.google.com/youtube/answer/9314355?hl=en), [한국어 데스크톱판](https://support.google.com/youtube/answer/9314355?hl=ko&co=GENIE.Platform%3DDesktop) (날짜 표기 없음)
- ⚠️ [공식 확인 결과] 현재 두 페이지 모두 "Hashtag pages"(해시태그 페이지) 항목이 없음 → 과거 목록에서 변경되었을 가능성. "Direct or unknown"의 정확한 한국어 명칭은 "직접 입력 또는 알 수 없는 소스". — [한국어 데스크톱판](https://support.google.com/youtube/answer/9314355?hl=ko&co=GENIE.Platform%3DDesktop)

**E. 참여도 탭: 평균 시청 지속 시간·시청 지속 시간(audience retention)·주요 순간**
- [공식] 경로: 콘텐츠 → 동영상 → 분석 → **개요** 또는 **참여도** 탭의 시청 지속 시간 보고서(한국어판 페이지명 "시청 지속 시간의 주요 순간 측정하기"); 한국어판은 '세그먼트' 드롭다운으로 시청자 그룹 선택 가능. — [9314415 영문](https://support.google.com/youtube/answer/9314415?hl=en), [한국어판](https://support.google.com/youtube/answer/9314415?hl=ko)
- [공식] 평균 시청 지속 시간: "Average minutes watched among those who stayed to watch." "This is calculated from engaged views and their corresponding watch time." (한국어: "시청을 지속한 사용자의 평균 시청 시간(단위: 분)입니다.") 시청 시간: "The amount of time viewers have watched your video." — [9314415](https://support.google.com/youtube/answer/9314415?hl=en), [12220281](https://support.google.com/youtube/answer/12220281?hl=en)
- [공식] 비교 기준: "You can click SEE MORE to see how your video compares to all YouTube videos of similar length." "You can also use typical retention to compare your 10 latest videos of similar length." (한국어: "일반적인 시청 지속 시간을 사용해 길이가 비슷한 최신 동영상 10개를 비교할 수도 있습니다.") — [9314415](https://support.google.com/youtube/answer/9314415?hl=en), [한국어판](https://support.google.com/youtube/answer/9314415?hl=ko)
- [공식] 주요 순간(영문 / 한국어 라벨):
  - Intro / **인트로**: "Intro tells you what percentage of your audience still watched your video after the first 30 seconds." / "인트로는 동영상 초반부 30초 후에도 시청을 지속한 시청자의 비율을 나타냅니다."
  - Top moments / **인기 장면**: "Top moments are moments in your video where almost no one dropped off while watching."
  - Spikes / **급상승 구간**: "Spikes are moments in your video that were rewatched or shared."
  - Dips / **하락 구간**: "Dips highlight moments in your video that were either skipped or moments where viewers stopped watching your video completely."
  — [9314415](https://support.google.com/youtube/answer/9314415?hl=en), [한국어판](https://support.google.com/youtube/answer/9314415?hl=ko)
- [공식] 데이터 조건: "Note that audience retention data typically takes 1–2 days to process." "The audience retention report is only available at the video level of YouTube Analytics." "Your video should also be at least 60 seconds long and have at least 100 views." "Your video may not have all these moments; they're only highlighted if they're detected in a video." (한국어: "동영상 길이는 60초 이상이고 조회수가 100회 이상이어야 합니다.") — [9314415](https://support.google.com/youtube/answer/9314415?hl=en), [한국어판](https://support.google.com/youtube/answer/9314415?hl=ko)

**F. 시청자층 탭: 신규/일반/정기적으로 방문하는 시청자**
- [공식] 정의(영문): New viewers "watched your content for the first time" (1년 넘게 안 본 시청자도 신규로 분류: "haven't watched your channel in over a year are considered new viewers"); Casual viewers "have watched your channel at least once per month for one to 5 months in the past year"; Regular viewers "have watched a video on your channel at least once per month for more than 6 months in the past year." — [10246996](https://support.google.com/youtube/answer/10246996?hl=en)
- [공식] 한국어 라벨: 페이지 제목 "신규 시청자, 일반 시청자, 정기적으로 방문하는 시청자 이해하기"; **일반 시청자** = "지난 1년간 1~5개월 동안 한 달에 한 번 이상 내 채널을 시청한 시청자입니다."; **정기적으로 방문하는 시청자** = "지난 1년간 6개월 넘게 한 달에 한 번 이상 내 채널의 동영상을 시청한 시청자를 의미합니다." — [10246996 한국어판](https://support.google.com/youtube/answer/10246996?hl=ko)
- [공식] "Audience segments do not affect reach or monetization." (한국어: "시청자 세그먼트는 도달범위 또는 수익 창출에 영향을 미치지 않습니다.") — [10246996](https://support.google.com/youtube/answer/10246996?hl=en)
- [공식] 기타 정의: Unique viewers "Estimated number of viewers that watched your content within the selected date range."; Unique reach "Estimated total number of individual people who saw your video or channel."; Engaged views "How many times viewers stayed to watch past the initial seconds, not including any loops." — [Understand your YouTube content performance (12220281)](https://support.google.com/youtube/answer/12220281?hl=en)

**G. 2026년 8월 24일 조회수 집계 변경 (영상 간 비교의 전제)**
- [공식] "Beginning August 24, 2026, views are counted the moment a video starts to play across all formats" / YPP 수익은 여전히 "engaged views"·"engaged watch hours", 자격은 "qualified views" 기준. — [How engagement metrics are counted (2991785)](https://support.google.com/youtube/answer/2991785?hl=en)
- [공식] YouTube 공식 블로그(2026-08-19): "Starting August 24, 2026, views across YouTube are counted from the first frame going forward." "the previous definition of a view will now be called an 'engaged view.'" engaged view = "clicking to watch or watching past the initial seconds." "the vast majority of analytics remain anchored on engaged views." "the way metrics like CTR, AVD, and retention are calculated hasn't changed." "there's no change to recommendations — the algorithm —." — [What are 'Engaged' Views on YouTube? (blog.youtube, 2026-08-19)](https://blog.youtube/inside-youtube/engaged-views-youtube-explained/)
- [공식] 과거 조회수 재집계 여부·과거/현재 데이터 비교 가능성에 대한 언급은 블로그에 없음. — [blog.youtube](https://blog.youtube/inside-youtube/engaged-views-youtube-explained/)
- [공식] 조회수 검증: "To verify that metrics are accurate, we may temporarily slow down, freeze, or change your metric count" "…and discard low-quality playbacks." "Realtime activity only shows estimates of potential view activity." "It may take time for your metrics to appear in our system during the first few hours your video is published." — [2991785](https://support.google.com/youtube/answer/2991785?hl=en)

### Inferences
- [추론] 6개 영상의 업로드일이 2026-08-24 전후로 걸쳐 있다면 공개 조회수의 정의가 섞여 있을 수 있다(집계 변경은 "going forward"). 영상 간 비교는 공개 조회수 대신 분석의 **유효 조회수(engaged views)**·노출수·CTR·평균 시청 지속 시간처럼 정의가 바뀌지 않은 지표로 하는 것이 안전하다.
- [추론] 8/24 이후에는 '재생 시작'만으로도 조회수가 잡히므로 집계가 오히려 관대해졌다. 그런데도 새 영상의 조회수가 낮다면 집계 방식 탓이 아니라 실제 노출·클릭이 적었다는 신호일 가능성이 크다.
- [추론] 조회수 약 20회인 6번 영상은 시청 지속 시간 보고서 조건(조회수 100회 이상)에 못 미쳐 주요 순간·일반적인 시청 지속 시간 비교가 아예 안 나올 수 있다. 이 경우 진단은 노출수·CTR·트래픽 소스 위주로 해야 한다.
- [추론] 채널에 영상이 6개뿐이면 "길이가 비슷한 최신 동영상 10개" 기준선이 성립하기 어렵고, '일반적인 실적' 비교도 기준이 얇다.

### Gaps
- '일반적인 실적(Typical performance)'의 계산 방식(기준 영상 수, 게시 후 같은 시점 정렬 여부, 범위 표시 방식): 공식 문서에서 확인 불가 (unverified).
- "Ranking by views(예: 10개 중 N위)" 카드의 공식 정의: 확인 불가. vidIQ 영상 전사본에는 "최근 10개 영상 중 해당 기간 조회수 순위"라는 설명이 있으나(검색 요약 기반, 원문 미검증), 공식 근거는 못 찾음.
- "Average percentage viewed(평균 조회율)"와 "relative/absolute audience retention"의 2026년 현재 공식 정의: 확인한 페이지에 없음 → 확인 불가.
- 2026년 7월 UI 개편 뒤의 실제 탭·버튼 한국어 라벨(예: "thumbnail impressions"의 한국어 UI 표기, '고급 모드' '비교 대상' 위치): 고객센터 텍스트로만 확인했고 실제 Studio 화면은 확인 불가.

## Q2. 이 지표들을 어떻게 해석하라는 공식 가이드가 있나 (CTR 범위, 노출 확대 시 CTR 하락, 노출 집계 기준, 공식 트러블슈팅 페이지)

### Takeaway
공식 문서는 ① 전체 채널·동영상의 절반이 노출 CTR 2~10%이고, 신규(1주 미만)이거나 조회수 100회 미만인 영상은 이보다 범위가 더 넓으며 ② 홈처럼 노출이 많은 곳에서는 CTR이 낮은 게 자연스럽고(노출이 10배 늘며 CTR이 9%에서 3.5%로 내려간 예시) ③ CTR은 트래픽 소스를 고려해 장기간 비교해야 한다고 명시한다. 공식 트러블슈팅 문서로는 "Watchtime drop tips"(15086271)와 Studio 앱 "YouTube performance FAQ & Troubleshooting"(141805)이 있다.

### Cited Findings
**A. CTR 범위와 해석 (Impressions & click-through-rate FAQs, 7628154)**
- [공식] "Half of all channels and videos on YouTube have an impressions CTR that can range between 2% and 10%." (한국어판: "YouTube의 모든 채널과 동영상 중 절반은 노출 CTR이 2%에서 10% 사이입니다.") — [7628154 영문](https://support.google.com/youtube/answer/7628154?hl=en), [한국어판](https://support.google.com/youtube/answer/7628154?hl=ko) (날짜 표기 없음)
- [공식] "New videos or channels (like those less than a week old), or videos with fewer than 100 views can see an even wider range." (한국어판은 "이 범위를 초과할 수 있습니다"로 번역 — 영문은 '더 넓은 범위') — [7628154](https://support.google.com/youtube/answer/7628154?hl=en), [한국어판](https://support.google.com/youtube/answer/7628154?hl=ko)
- [공식] "If a video gets a lot of impressions (such as if it appears on the Home Page), it's natural for the CTR to be lower." 반대로 CTR이 높은 경우는 "These higher numbers are because they've been viewed by a narrower, more loyal audience." "Videos where most of the impressions are from sources like your channel page may have a higher rate." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] "Impressions click-through rate will vary based on the type of content, audience, and where on YouTube the impression was shown." "…compare CTRs between videos over the long-term and keep in mind how their traffic sources will affect their CTRs." "…look over your click-through-rate after getting a substantial number of impressions" "Improvements might be helpful if a change in click-through-rate is statistically significant." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] FAQ 질문 목록(순서대로): "Why does my video have a high click-through-rate and average view duration but low impressions?" / "What should I avoid doing with my click-through-rate data?" / "How do I know if my impressions click-through rate is high or low?" / "Why do I have more views than impressions?" / "Why doesn't the click-through-rate metric match my calculations?" / "How do impressions relate to monetization?" — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] "It's also common for videos with fewer impressions and views to have higher click-through-rates and average view duration." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] 클릭베이트 경고: "Avoid trying to increase your CTR using thumbnails or titles that are clickbait." "Clickbait videos tend to have low average view duration and therefore are less likely to get recommended by YouTube." 판별 신호: "…getting high CTR but low average view duration and lower than expected Impressions." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] 하지 말아야 할 것: "Testing several thumbnails or titles on the same video." 이유: "It's difficult to make sure each video is being seen by the same audience." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)

**B. 노출 확대 → CTR 하락 예시 (Decoding CTR & impressions in your Analytics, 16767369)**
- [공식] "Imagine that one of your videos generates 10,000 impressions in its initial period." "This initial reach is primarily among your most loyal fans, so your CTR sits at a high 9%." "As a result of this tenfold expansion into new, less familiar audiences" … "your CTR has settled at 3.5%." (문서는 이 하락을 성공의 신호로 설명) — [16767369](https://support.google.com/youtube/answer/16767369?hl=en) (날짜 표기 없음)
- [공식] 노출 위치별: "you might observe fewer impressions but a higher CTR in Search results." "surfaces like the Homepage typically yield a high volume of impressions but often a lower CTR." "it's important not to view either in isolation." (노출수·CTR·평균 시청 지속 시간·트래픽 소스를 함께 보라는 취지) — [16767369](https://support.google.com/youtube/answer/16767369?hl=en)
- [공식, 요약] 아주 좁은 주제는 CTR과 평균 시청 지속 시간이 높아도 관심 있는 시청자 풀이 작아 노출이 적을 수 있다고 설명. 정해진 '좋은 CTR' 수치는 제시하지 않음. — [16767369](https://support.google.com/youtube/answer/16767369?hl=en)

**C. 노출 집계 기준·제외 항목 (9314486)**
- [공식] "Impressions are counted if the thumbnail is shown for more than 1 second" and "at least 50% of the thumbnail is visible on the screen". — [9314486](https://support.google.com/youtube/answer/9314486?hl=en)
- [공식] 집계되는 곳: "YouTube on computers, TVs, game consoles, Android, iPhone, and iPad", "YouTube Search", "YouTube homepage (includes auto-play)", "YouTube feeds (subscriptions, trending, history, Watch Later)", ""Up Next" recommendations on the right side of the video player (includes autoplay)", "Playlists". — [9314486](https://support.google.com/youtube/answer/9314486?hl=en)
- [공식] 집계되지 않는 곳: "External websites and apps (for example, links and embeds outside of the YouTube website)", "YouTube mobile website", "YouTube Kids app", "YouTube Music app", "Content within the video player (for example, in cards or end screens)", "Email or notifications", "Videos that play in the background tab (no visible impression)", "Videos whose thumbnails are less than 50% visible or visible for less than 1 second", "TrueView video discovery ads". — [9314486](https://support.google.com/youtube/answer/9314486?hl=en) (※ 도구 출력에서 '집계됨/안 됨' 소제목 일부가 잘려 순서로 대응시킴)
- [공식] "Not every instance where a viewer sees a video thumbnail will count as an impression" "Some views do not originate from thumbnail impressions." 노출 CTR은 "likely represents a subset of your channel's total views, since not all impressions are counted in this metric, such those on external websites or end screens." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)

**D. 공식 트러블슈팅 문서**
- [공식, 요약 — 도구가 전문 인용을 거부해 비원문] "Watchtime drop tips" (15086271): 실적이 크게 바뀌면 원인을 찾아 전략을 조정하라고 하며 다음을 점검하라고 함. ① 콘텐츠 전략 변화(주제, 편집 스타일, 썸네일 디자인, 출연자, 업로드 빈도·양, 영상 길이). 썸네일을 바꿨다면 노출수·CTR 확인 ② 주제의 인기 변화(Google Trends 활용 권장) ③ 시청자층 탭에서 어느 그룹이 줄었는지: 일반·정기 시청자 감소는 채널 콘텐츠가 그들에게 덜 매력적이라는 뜻일 수 있고, 신규 시청자 감소는 넓은 시청자를 끌지 못한다는 뜻일 수 있음 ④ 계절성(학기, 휴일 등). 권고: 한 번에 여러 가지를 바꾸지 말 것(어떤 변화가 원인인지 알 수 있도록), 콘텐츠가 같아도 시청자 관심은 바뀔 수 있음, 계절 변동을 예상할 것. 관련 영상 "YouTube Search & Discovery: 'The Algorithm' and Performance FAQs" 링크. — [Watchtime drop tips](https://support.google.com/youtube/answer/15086271?hl=en) (날짜 표기 없음)
- [공식] Studio 앱 고객센터 "YouTube performance FAQ & Troubleshooting":
  - "If one of my videos under-performs, is that going to hurt my channel?" → "What can lead to a decline in overall channel views is when viewers stop watching most of your videos"
  - 홈·추천 트래픽 감소 원인 중 하나: "a video went 'viral' but those viewers didn't return to watch more." (그 밖에 시청자가 다른 콘텐츠를 더 보거나 YouTube 이용 시간이 줄거나 업로드가 뜸해지거나 주제 인기가 떨어진 경우를 듦 — 요약)
  - "Not all videos are eligible to be recommended." "Keep in mind that not all content is eligible to be recommended on the YouTube Home page."
  - "Does changing a video's title or thumbnail re-rank the video in the algorithm?" → "Changing your video title and thumbnail can be an effective way to get more views, but don't change what's working."
  — [141805](https://support.google.com/youtubecreatorstudio/answer/141805?hl=en) (날짜 표기 없음)
- [공식] 추천 시스템 관점 문서: "These signals help us predict how likely a user is to watch and enjoy a piece of content." 신호는 세 가지: Appeal("Did people choose to watch the content or did they ignore or click 'not interested?'"), Engagement("Once viewers start watching, do they stick around?"), Satisfaction("Did viewers enjoy the video?"). "Use Analytics to measure audience retention at key moments and understand how your audience reacts." — [Understand your content performance for YouTube's recommendation system (16559650)](https://support.google.com/youtube/answer/16559650?hl=en) (날짜 표기 없음)

### Inferences
- [추론] 공식 문서의 Appeal → Engagement → Satisfaction 틀은 Studio 지표와 대략 이렇게 짝지을 수 있다: Appeal = 노출수·노출 클릭률, Engagement = 평균 시청 지속 시간·시청 지속 시간 보고서, Satisfaction = 직접 지표 없음(좋아요·댓글·재방문은 간접 신호). 문서가 직접 연결해 준 지표는 시청 지속 시간뿐이므로 나머지 짝은 조사자의 해석이다.
- [추론] 채널 초기에는 노출이 구독자·채널 페이지 같은 '좁고 충성도 높은' 경로에 몰려 CTR이 높게 나오기 쉽다. 그래서 초기 영상의 CTR이 높고 나중 영상의 CTR이 낮다는 사실만으로 나중 영상의 패키징이 나쁘다고 단정하면 안 된다. 같은 트래픽 소스끼리 비교해야 한다(공식 근거: 7628154, 16767369).
- [추론] CTR FAQ의 "같은 영상에 여러 썸네일 테스트 금지"는 수동으로 기간을 나눠 썸네일을 바꿔 가며 CTR을 비교하는 것을 경계하는 말로 읽힌다(기간마다 시청자가 다름). 같은 기간에 시청자를 나눠 보여 주는 Studio의 A/B 테스트 도구(Q3)와는 다르다.

### Gaps
- 15086271 "Watchtime drop tips"의 원문 문장은 확보하지 못했다(도구가 전문 인용을 거부해 요약만 있음). 보고서에서는 원문 인용 대신 '요약'으로 표기해야 한다.
- 이번 조회수 하락이 '노출이 적어서'인지 '추천 대상이 아니어서'인지 분석에서 바로 구분하는 공식 방법은 없음. "Not all videos are eligible to be recommended"라고만 하고 판별 기준은 제시하지 않음 → 확인 불가.
- 고객센터 페이지들은 게시·수정일이 없어 각 문구가 언제부터 유효했는지는 확인 불가.

## Q3. 2026년 기준, 결과를 개선하는 공식 도구와 가이드는 무엇인가 (Test & Compare, Inspiration/Research/Trends, Ask Studio, 제목·썸네일·훅·타깃)

### Takeaway
2026년 11월 현재 공식 도구는 ① **제목·썸네일 A/B 테스트**(옛 "Test & Compare". 최대 3개 변형, '시청 시간 점유율'로 승자 판정, 데스크톱 전용, 고급 기능 필요, 최대 2주, 노출이 부족하면 결론이 안 날 수 있음) ② **트렌드 탭**(옛 Research 탭. 일부 국가·언어로 제한) ③ **Ask Studio**(데스크톱·만 18세 이상, 지원 언어 목록은 공개되지 않음) ④ 2026년 8월부터 단계적으로 종료 중인 **Inspiration 탭**(아이디어는 영어로만 제공) ⑤ 소수 사용자 대상 실험 중인 새 **Research 탭**이다. 한국어 채널에서는 아이디어·검색 트렌드 도구의 지원이 제한되거나 확인되지 않는다. 제목·썸네일·첫 30초에 관한 공식 팁은 고객센터 여러 페이지에 흩어져 있다.

### Cited Findings
**A. 제목·썸네일 A/B 테스트 (고객센터 제목 "A/B test titles & thumbnails", 13861714)**
- [공식] "Creators can test and compare up to 3 different titles and thumbnails." 방식: "Title only, Thumbnail only, Title and thumbnail." — [13861714](https://support.google.com/youtube/answer/13861714?hl=en) (날짜 표기 없음)
- [공식] 자격·제한: "This feature is currently only available on computers through YouTube Studio." "You need to enable advanced features to be eligible." "You are not able to A/B test Shorts, Scheduled Lives, and Premiere videos at this time." (Live Archive는 가능, Premiere는 종료 후 일반 동영상으로 전환되면 가능) "You cannot use this feature on videos that are made for kids, mature audiences, or are private." 연령 제한(18+) 영상에서는 "the test will not run." — [13861714](https://support.google.com/youtube/answer/13861714?hl=en)
- [공식] 승자 판정: "We optimize tests for overall watch time over other metrics, like click-through-rate." "…the title or combination of title and thumbnail with the highest watch time will be shown to all viewers." Winner = "This option clearly outperformed the others based on watch time share." Performed Same = "This result means that the test ran and all your options performed about the same." Inconclusive = "There was no strong statistical difference in engagement between your options." (이 경우 처음 올린 안이 기본값) — [13861714](https://support.google.com/youtube/answer/13861714?hl=en)
- [공식] 기간·소규모 채널 관련: "Your A/B test can take a few days or up to 2 weeks to complete." "Not enough impressions: It may be that your videos are not generating a sufficient amount of impressions." "If your video receives a higher number of views, then the more likely a 'Winner' will be declared." "Testing titles and thumbnails that are too similar to each other can cause tests to run for longer." "We may maintain a small percentage of traffic as a control group of viewers that are excluded from the experiment." — [13861714](https://support.google.com/youtube/answer/13861714?hl=en)
- [공식] 설정: studio.youtube.com → Content → 동영상(또는 CREATE → Upload videos) → Title 상자 또는 Thumbnail 아래 **A/B Testing** → 방식 선택 → 최대 3개 업로드 → Done. 확인·중지: 동영상 Analytics → **Reach** 탭 → "How your A/B test is going" 아래 **Manage test**. — [13861714](https://support.google.com/youtube/answer/13861714?hl=en)
- [2차] 연혁: 썸네일 A/B 테스트는 VidCon 2023에서 발표(Tubefilter 2023-06-27 기사 언급)되고 2024년에 배포 시작. 2025-07-16 Tubefilter는 제목 테스트를 포함한 "test and compare" 실험을 YouTube 고객센터 문구("starting to experiment", "a small percentage of creators")를 근거로 보도. — [Tubefilter, 2025-07-16](https://www.tubefilter.com/2025/07/16/youtube-feature-test-and-compare-titles-thumbnails/)
- [공식, 날짜 주의] 2026년 고객센터 페이지는 제목·썸네일·둘 다 테스트를 일반 기능으로 설명하며, '소수 크리에이터 실험'이라는 문구는 이번 조회에서 확인되지 않음 → 2025년 7월 실험 이후 확대된 것으로 보이나 정확한 확대 날짜는 확인 불가. — [13861714](https://support.google.com/youtube/answer/13861714?hl=en)

**B. 트렌드 탭 (옛 Research 탭, 11962757 "Explore trends on YouTube")**
- [공식] 경로: YouTube Studio → 왼쪽 메뉴 Analytics → 상단 **Trends** 탭(한국어 탭명 **트렌드**). 카드: "Top searches"(최근 28일), "Breakout videos", "Recent videos", "Content gaps for Shorts". "A content gap happens when viewers can't find enough quality search results on YouTube for a specific search." — [11962757](https://support.google.com/youtube/answer/11962757?hl=en), [9002587 한국어판](https://support.google.com/youtube/answer/9002587?hl=ko)
- [공식] 제한: "Currently, some of the insights are limited to certain countries, languages, and devices." (지원 국가·언어 목록은 없음 → 한국어 지원 여부 확인 불가) "If there are no relevant videos at the moment, you might not see some of the sections." "Starting July 2026, … your Trends tab may look different than before." — [11962757](https://support.google.com/youtube/answer/11962757?hl=en)

**C. Inspiration 탭 (15575509 "Explore Inspiration tab on YouTube") — 단계적 종료 중**
- [공식] 경로: Studio → Content → 하단 "Get Inspired"; 데스크톱 전용, "available in all global markets only on desktop." AI가 아이디어·제목·썸네일·개요·훅을 제안. — [15575509](https://support.google.com/youtube/answer/15575509?hl=en)
- [공식] 언어 제한: "The tool can only give you content ideas in English." AI 결과는 "may be inaccurate or inappropriate and vary in quality." — [15575509](https://support.google.com/youtube/answer/15575509?hl=en)
- [공식] 종료: "Starting August 2026, we are gradually deprecating the Inspiration tab." 브레인스토밍에는 Ask Studio를 쓰라고 안내. — [15575509](https://support.google.com/youtube/answer/15575509?hl=en)

**D. Ask Studio (16291691)**
- [공식] "an AI creative partner built directly into YouTube Studio" — 아이디어 브레인스토밍, 채널 인사이트, 실적 분석, "Summarize comments" 같은 추천 프롬프트 제공. 위치: 페이지 오른쪽 위, 분석 페이지 안, 또는 studio.youtube.com/?d=as. — [16291691](https://support.google.com/youtube/answer/16291691?hl=en) (날짜 표기 없음)
- [공식] 이용 가능 범위: "available to most YouTube creators globally"; "If you are in an eligible country, you can use any supported language"(지원 언어 목록 없음 → 한국어 지원 확인 불가); "creators under the age of 18 do not have access to Ask Studio."; "It is available only on web browsers on your computer."; Official Artist Channel·Made for Kids 채널은 이용 불가; "Quality and accuracy of responses may vary." — [16291691](https://support.google.com/youtube/answer/16291691?hl=en)
- [제3자, 검색 요약 기반·원문 미확인] 2026년 초 일부 제3자 블로그는 Ask Studio를 "미국·캐나다·뉴질랜드·인도 + 영어 위주"로 소개했으나, 현재 공식 문구("available to most YouTube creators globally")와 다름 → 최신 공식 문구를 우선. — (검색 결과 예: [OutlierKit Ask Studio 글](https://outlierkit.com/resources/youtube-ask-studio-ai-analytics-2026/), [Social Media Today Ask Studio 해설](https://www.socialmediatoday.com/news/youtube-ask-studio-ai-chatbot-explainer-analytics/803682/) — 어느 글이 해당 국가 목록을 썼는지는 미확인)

**E. 새 Research 탭 (실험)**
- [2차] Tubefilter(2026-08-05): 다른 크리에이터 영상과 공개 데이터를 보여 주는 새 Research 탭. 해당 크리에이터의 다른 영상 대비 성과를 배수로 보여 주는 "outlier multiplier"(기사 예시 4x~132x)와 "Watched by my viewers" 필터가 있음. YouTube 대변인은 "a small number of users"를 대상으로 한 실험이고 확대 계획 정보는 없다고 밝힘. 공식 고객센터·블로그 문서는 없음. — [Tubefilter, 2026-08-05](https://www.tubefilter.com/2026/08/05/youtube-research-tab-outlier-multipliers-viewer-comparison-data/)

**F. 제목·썸네일·훅·타깃에 관한 공식 팁**
- [공식] "Thumbnail & title tips" (12340300): "Content targeting your subscribers might highlight familiar features, like your best friend." "Content targeting casual viewers might focus on actions and emotions" + "that are more universally relatable, like a shocked face." "If you add text, make sure to use a font that's easy to read." "Try not to make the design too complex." "Thumbnails show up differently across devices, so make sure your thumbnail image is as large as possible." "We also recommend experimenting with updating older thumbnails to increase your video's appeal to new viewers." 제목: "Be accurate. Make sure your title accurately represents the video." "Be succinct. Viewers may only see part of your title." "So aim to keep it short and put the most important words near the beginning." "Save episode numbers and branding for the end." "Limit ALL CAPS and emoji." — [12340300](https://support.google.com/youtube/answer/12340300?hl=en) (날짜 표기 없음)
- [공식] 측정 기준(같은 경과 시간 비교의 공식 근거): "For general audiences, look at the click-through rate (CTR) on Home and Suggested in the first 24 hours after publication." "For subscribers, look at the click-through rate (CTR) in the Subscriptions Feed in the first 24 hours after publication." — [12340300](https://support.google.com/youtube/answer/12340300?hl=en)
- [공식] "Content tab analytics tips": CTR — "This metric helps indicate how appealing the thumbnail, title, and video content is to viewers. Adopt patterns from your popular videos to improve CTR." 평균 시청 지속 시간 — "It could also be a good indicator of how long your videos should be." 트래픽 소스 — "Find ideas for new content in the search terms viewers are using to find you." 비교 — "If you produce multiple content formats, it's key to compare videos of the same type." — [12942217](https://support.google.com/youtube/answer/12942217?hl=en&co=YOUTUBE._YTVideoType%3Dvideo)
- [공식] 훅·초반부(시청 지속 시간 문서): 인트로 비율이 높으면 초반 30초가 썸네일·제목이 준 기대와 맞았다는 뜻일 수 있다고 하며, 인트로 비율을 높이려면 썸네일·제목을 내용과 맞추고 첫 30초를 실험하라고 권함. 원문 예: "If the top moments are occurring in a later portion in the video, consider introducing the compelling content earlier in the video—audience sizes typically decrease over the length of the video." "When the line on the chart is flat, it means viewers are watching that part of your video from start to finish. Gradual declines mean that viewers are losing interest over time." (원문 문장은 검색 스니펫 기준이며, 본문 fetch에서 같은 취지 확인) — [9314415](https://support.google.com/youtube/answer/9314415?hl=en)
- [공식] 추천 시스템 문서: "Your title and thumbnail are vital for communicating value, sparking intrigue, and setting clear expectations for viewers." "Tags can be helpful but are not essential for discovery." 기획은 "identifying your core and potential audience"부터 시작하라고 권함. — [16559650](https://support.google.com/youtube/answer/16559650?hl=en)
- [공식] 시청자 세그먼트 활용: "you can build loyalty by creating consistent content or you can experiment with new topics to attract new viewers." 정기 시청자를 늘리려면 "consistent content about similar topics, or in a familiar format" + 게시물·댓글·라이브/Premiere 채팅·일관된 브랜딩. — [10246996](https://support.google.com/youtube/answer/10246996?hl=en), [한국어판](https://support.google.com/youtube/answer/10246996?hl=ko)
- [공식] Studio 앱 FAQ: 알고리즘 세부보다 시청자를 이해하는 데 집중하고, 새 주제·형식을 계속 실험하라고 조언(요약). — [141805](https://support.google.com/youtubecreatorstudio/answer/141805?hl=en)

### Inferences
- [추론] 조회수가 20~300회 수준인 채널은 A/B 테스트가 "Not enough impressions" 때문에 Inconclusive로 끝나거나 2주를 다 쓸 가능성이 높다. 결과가 나와도 승자 판정 기준은 CTR이 아니라 시청 시간이므로, 결과를 '클릭을 더 받은 썸네일'로 읽으면 안 된다.
- [추론] 한국어 채널에서는 Inspiration 아이디어(영어 전용, 종료 중)를 쓰기 어렵고, 트렌드 탭·Ask Studio의 한국어 데이터·응답 지원도 공식 확인이 안 된다. 그래서 가장 확실한 '수요' 데이터는 자기 영상의 **YouTube 검색어** 보고서(도달범위 탭)와 외부 도구(Google Trends 등. 공식 "Watchtime drop tips"도 Google Trends를 권함)다.
- [추론] 공식 팁 가운데 소규모 신규 채널에 바로 쓸 만한 것: ① 제목은 정확·간결하게, 중요한 단어를 앞에 ② 첫 30초가 제목·썸네일 약속과 맞는지 확인 ③ 기존 시청자를 노릴지(익숙한 요소) 새 시청자를 노릴지(보편적 감정·행동)를 정한 뒤 썸네일 구성.

### Gaps
- youtube.com/creators(YouTube Creators 사이트)의 제목·썸네일·훅 가이드 페이지는 이번 조사에서 직접 열어 보지 못함 → 고객센터 문서로 대신함.
- A/B 테스트 한국어 UI 라벨, 제목 테스트를 모든 적격 채널에 연 날짜, 고급 기능 외 최소 구독자·조회수 조건 유무: 확인 불가.
- Ask Studio·트렌드 탭의 한국어·한국 데이터 지원 여부: 공식 문서에 목록이 없어 확인 불가.
- Rene Ritchie의 "The algorithm follows the audience, so please the audience" 같은 발언은 검색 요약으로만 접해 원문·날짜를 검증하지 못함 → 인용 금지 권장.

## Q4. 20~300회 수준에서 영상 간 차이를 어떻게 해석하나 — 같은 경과 시간 비교, 장기 누적, 작은 표본

### Takeaway
공식 문서는 작은 표본에서 지표가 불안정하다고 여러 번 경고한다. 조회수 100회 미만·게시 1주 미만이면 CTR 범위가 더 넓어지고, 시청 지속 시간 보고서는 조회수 100회 이상이어야 나오며, A/B 테스트는 노출이 부족하면 결론이 안 난다. YouTube의 Todd Beaupré는 2026년 9월 Creator Insider에서 시스템이 "첫 1시간이나 처음 본 1,000명만으로 결정하지 않는다", 에버그린 콘텐츠는 "한 달 이상 지나서" 조회수 대부분이 나오기도 한다고 말했다(2차 보도). 따라서 6개 영상은 **같은 경과 시간(첫 24시간, 7일, 28일)으로 맞춰** 비교해야 하고, 작은 표본을 해석하는 공식 방법론은 없으므로 아래 통계 메모는 추론으로 표시했다.

### Cited Findings
**A. 작은 표본 관련 공식 경고**
- [공식] "New videos or channels (like those less than a week old), or videos with fewer than 100 views can see an even wider range." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] "…look over your click-through-rate after getting a substantial number of impressions" / "Improvements might be helpful if a change in click-through-rate is statistically significant." — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] 시청 지속 시간 보고서: "at least 60 seconds long and have at least 100 views", 처리에 "1–2 days". — [9314415](https://support.google.com/youtube/answer/9314415?hl=en)
- [공식] A/B 테스트: "Not enough impressions…", "If your video receives a higher number of views, then the more likely a 'Winner' will be declared." — [13861714](https://support.google.com/youtube/answer/13861714?hl=en)
- [공식] 초기 데이터 지연·추정치: "It may take time for your metrics to appear in our system during the first few hours your video is published." "Realtime activity only shows estimates of potential view activity." — [2991785](https://support.google.com/youtube/answer/2991785?hl=en)

**B. 같은 경과 시간으로 비교하는 방법**
- [공식] 제목·썸네일 성과는 "in the first 24 hours after publication" 기준으로 홈·추천(일반 시청자) 또는 구독 피드(구독자)의 CTR을 보라. — [12340300](https://support.google.com/youtube/answer/12340300?hl=en)
- [공식] 실시간 보고서에서 "compare 60 minute and 48 hour performance". — [9314414](https://support.google.com/youtube/answer/9314414?hl=en)
- [2차, 2021년 — UI 변경 가능] Social Media Today(2021-02-22): 동영상 분석 기간 "Since published"를 "First 24 hours"로 바꾼 뒤 Advanced mode → "Compare to"로 이전 영상과 비교할 수 있고, 채널 분석 Advanced mode의 다중 영상 차트는 게시일 기준으로 정렬해 첫 24시간·7일·28일 지표(조회수, 노출수, 평균 시청 지속 시간 등)를 최대 100개 영상까지 비교한다. 이 기사는 YouTube가 첫 24시간 데이터가 추천 시스템에 크게 중요하지 않고 향후 성과를 예측하지도 않는다는 취지로 말했다고 전함(요약). — [Social Media Today, 2021-02-22](https://www.socialmediatoday.com/news/youtube-adds-new-comparative-data-tools-in-youtube-studio-and-info-on-othe/595416/)
- [공식] "If you produce multiple content formats, it's key to compare videos of the same type." — [12942217](https://support.google.com/youtube/answer/12942217?hl=en&co=YOUTUBE._YTVideoType%3Dvideo)

**C. 롱폼 조회수의 장기 누적 — YouTube 직원 발언**
- [2차] Todd Beaupré(YouTube), Creator Insider 영상(2026-09-01, https://www.youtube.com/watch?v=rHLjxrbXmmY), OutlierKit(2026-09-07) 인용: "Creators do tend to overfocus on the immediate data." "we're not basing decisions just on those initial moments." "A lot of videos have their peak moments in the first day" … "a lot of videos also get the majority of their views a month or later if it's evergreen content." "We're not going to stop trying to see if there's viewers that would be interested in it." "We're not going to decide just based on the first hour or first 1,000 people who see a video" "It takes a few tries." — [OutlierKit, 2026-09-07](https://outlierkit.com/resources/youtube-video-slow-start/) (※ 원본 영상 페이지를 직접 열어 확인하지는 못함. 출처는 OutlierKit 창업자의 글이며 자사 도구 홍보가 섞여 있음)
- [2차] Todd Beaupré, Search Engine Journal(2024-03-04): "If your last video wasn't so great and your next video is great, we want to realize the potential of each video," "For the most part, the algorithm for Discovery is focused more on individual videos." "We aim to not overemphasize historical data if that data isn't particularly predictive of future video performance," "A lot of creators think of YouTube as pushing videos out to a bunch of people, but it's actually more the reverse." (기사는 관심이 되살아나거나 트렌드가 바뀌면 영상이 나중에 반응을 얻을 수 있다고 요약) — [SEJ, 2024-03-04](https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/)
- [2차] Rene Ritchie(YouTube Creator Liaison), SEJ(2025-11-12): "The recommendation system is largely based on audience behavior." "Waiting 24 to 48 hours is no different than waiting 24 to 48 seconds or weeks or months." — [SEJ, 2025-11-12](https://www.searchenginejournal.com/youtube-debunks-24-48-hour-upload-delay-recommendation/560613/)
- [공식] "An old video recently took off, why?" → "It's common for viewers to start showing more interest in old videos." (원인으로 주제 관심 증가, 몰아보기, 시리즈 신규 에피소드 등을 듦 — 요약) — [141805](https://support.google.com/youtubecreatorstudio/answer/141805?hl=en)
- [2차, 2021년] YouTube가 오래된 영상(evergreen)이 채널 성장에 얼마나 기여하는지 보여 주는 Studio 분석 요소를 일부 크리에이터 대상으로 테스트(Conor Kavanagh 발언 인용: "Insights around evergreen videos as additional drivers to help you understand how overall channel performance, specifically…"). 현재 제공 여부는 확인 불가. — [Social Media Today, 2021-08-04](https://www.socialmediatoday.com/news/youtube-tests-new-insights-around-evergreen-videos-in-studio-analytics/)

**D. 제3자 데이터 (참고용, 비공식)**
- [제3자] OverseerOS(2026-09-02), 2026년 8월 20~30일 공개된 181개 영상(61개 채널) 추적. 롱폼(>180초) 37개 기준: 72시간 조회수 = 24시간 조회수의 1.58배, 48시간 = 1.41배. 72시간 조회수 중 63.2%가 24시간 안에 발생. 2일째 증가 속도는 1일째의 0.40배. 24시간 뒤 오히려 가속한 영상 8.1%. 72시간까지 2배가 된 영상 24.3%. 한계(본문 명시): "not a random sample of all YouTube uploads", 72시간까지만 추적, 노출수·CTR·시청 지속 시간·트래픽 소스는 측정 안 함. — [OverseerOS, 2026-09-02](https://www.overseeros.com/blog/why-youtube-views-stop-after-24-hours)
- [제3자, 원문 미확인] 같은 회사의 다른 분석(90일 이상 된 영상 367개 중 47.7%가 나중에 가속, 3.8%만 하루 100회 이상으로 속도 2배)은 검색 요약으로만 확인 → 인용하지 않는 것을 권장. — (검색 결과: [overseeros.com/blog/do-old-youtube-videos-still-get-views](https://www.overseeros.com/blog/do-old-youtube-videos-still-get-views))

### Inferences
- [추론/계산 — 공식 방법론 아님] CTR은 비율이므로 노출 수가 적으면 오차가 크다(정규근사 95% 신뢰구간, 실제 CTR 5% 가정): 노출 200회 → 약 ±3.0%p(2.0~8.0%), 500회 → 약 ±1.9%p(3.1~6.9%), 1,000회 → 약 ±1.35%p, 5,000회 → 약 ±0.6%p. 노출이 수백 회인 영상끼리 CTR 4%와 6%를 '차이'로 해석하기 어렵다는 뜻이다(공식 FAQ의 "statistically significant" 요구와 같은 방향).
- [추론] 반면 조회수 20회와 150회의 차이는 우연으로 설명하기엔 크다(포아송 근사로 20회의 표준편차는 약 4.5). 진짜 문제는 '차이가 있느냐'가 아니라 **원인을 무엇으로 볼 수 있느냐**다. 영상이 6개뿐이고 카테고리·주제·썸네일·업로드 시점·영상 길이·경과 시간이 동시에 다르면, 카테고리 변경 하나를 원인으로 지목할 통계적 근거가 없다. 공식 "Watchtime drop tips"의 "한 번에 여러 가지를 바꾸지 말 것"이 같은 원리다.
- [추론] 6번 영상(약 20회)의 게시 경과 시간을 모르므로 1~4번의 '전체 기간' 조회수와 비교하면 안 된다. 동영상 분석에서 같은 창(첫 24시간 → 7일 → 28일)으로 맞추고, 6번이 7일·28일이 지나기 전이면 그 시점에 다시 비교해야 한다(근거: 12340300, SMT 2021, Beaupré 2026 발언).
- [추론] 초기 영상 몇 개의 조회수가 만든 이의 지인 네트워크(카톡·블로그·SNS 공유 → 트래픽 소스 '외부'·'직접 입력 또는 알 수 없는 소스')에서 나오는 일은 업계에서 흔히 거론된다(업계 관행 수준의 관찰이며 정량 근거는 없음). 그 유입이 줄면 알고리즘과 무관하게 조회수가 떨어져 보일 수 있으므로 트래픽 소스 확인이 먼저다.

### Gaps
- 작은 표본(수십~수백 회)을 어떻게 해석하라는 YouTube의 공식 방법론은 없음(통계 기준·최소 노출 수 제시 없음) → 확인 불가. 위 계산은 추론.
- '일반적인 실적' 비교가 게시 후 같은 시점으로 맞춰지는지는 공식 확인 불가.
- Beaupré의 2026-09-01 발언은 원본 영상을 직접 확인하지 못했고 2차 출처(OutlierKit)만 확인했다. 보고서에는 '2차 보도'로 표기해야 한다.
- 롱폼 조회수가 몇 주·몇 달에 걸쳐 쌓이는 평균 곡선에 대한 공식 통계: 없음 → 확인 불가.

## Q5. 단계별 진단 흐름: 증상 → 가능한 원인 → 조치 (각 단계에 [공식 가이드] / [업계 관행·추론] 표시)

### Takeaway
권장 순서는 (0) 같은 조건으로 비교 → (1) 노출수 → (2) 노출 클릭률(같은 트래픽 소스, 첫 24시간) → (3) 시청 지속(인트로·평균 시청 지속 시간) → (4) 트래픽 소스 구성 → (5) 시청자층(신규/일반/정기) → (6) 바뀐 요소·주제 수요·계절성 점검 → (7) 한 번에 하나씩 바꾸고 같은 창으로 재측정이다. 1·2·3·5·6단계는 공식 문서에 직접 근거가 있고, 순서 자체와 이 채널 사례에 대입한 해석은 추론이다.

### Cited Findings
- [공식] 노출수·노출 클릭률·조회수·순 시청자 수는 도달범위 탭, 시청 시간·평균 시청 지속 시간은 참여도 탭, 신규·일반·정기 시청자는 시청자층 탭에 있음. — [9002587](https://support.google.com/youtube/answer/9002587?hl=en)
- [공식] 썸네일을 바꿨다면 노출수·CTR을 확인하고, 시청자층 탭에서 어느 세그먼트가 줄었는지 보고, Google Trends로 주제 관심 변화를 확인하고, 한 번에 여러 가지를 바꾸지 말라(요약). — [15086271](https://support.google.com/youtube/answer/15086271?hl=en)
- [공식] 높은 CTR + 낮은 평균 시청 지속 시간 + 예상보다 낮은 노출 = 클릭베이트 신호. — [7628154](https://support.google.com/youtube/answer/7628154?hl=en)
- [공식] 높은 CTR·평균 시청 지속 시간인데 노출이 낮은 경우는 흔하며(FAQ 질문 "Why does my video have a high click-through-rate and average view duration but low impressions?"), 주제가 지나치게 좁으면 관심 시청자 풀이 작다는 설명. — [7628154](https://support.google.com/youtube/answer/7628154?hl=en), [16767369](https://support.google.com/youtube/answer/16767369?hl=en)
- [공식] 인트로 비율과 첫 30초, 인기 장면이 뒤에 있으면 앞당기기. — [9314415](https://support.google.com/youtube/answer/9314415?hl=en)
- [공식] 첫 24시간 홈·추천 CTR(일반 시청자), 구독 피드 CTR(구독자). — [12340300](https://support.google.com/youtube/answer/12340300?hl=en)
- [공식] 영상 하나가 부진해도 채널 전체가 손해 보는 것은 아님("What can lead to a decline in overall channel views is when viewers stop watching most of your videos"). "Not all videos are eligible to be recommended." — [141805](https://support.google.com/youtubecreatorstudio/answer/141805?hl=en)
- [공식] 2026-08-24 이후 공개 조회수는 재생 시작 기준이고 분석 대부분은 유효 조회수 기준이며, CTR·평균 시청 지속 시간·시청 지속 시간 계산은 그대로. — [blog.youtube, 2026-08-19](https://blog.youtube/inside-youtube/engaged-views-youtube-explained/)

### Inferences
**진단 흐름 (각 단계 라벨 표시)**

| 단계 | 볼 곳 (한국어 UI 기준, 2026년 7월 개편으로 다를 수 있음) | 증상 | 가능한 원인 | 조치 | 근거 라벨 |
|---|---|---|---|---|---|
| 0. 비교 조건 맞추기 | 동영상 분석 기간을 '첫 24시간'·'7일'·'28일'로 맞춤, 고급 모드 '비교' (2021년 기준 UI) | 6번이 1~4번보다 훨씬 짧은 기간만 집계됨 | 경과 시간 차이(아직 덜 쌓임) | 같은 창으로 다시 비교. 6번은 7일·28일 시점에 재확인 | [공식] 12340300·9314414 / [2차] SMT 2021 / [추론] 적용 |
| 0-b. 지표 정의 맞추기 | 참여도 탭 '유효 조회수' | 8/24 전후로 공개 조회수 정의가 다름 | 집계 방식 변경 | 영상 비교는 유효 조회수·노출수·CTR·평균 시청 지속 시간으로 | [공식] blog.youtube·2991785 / [추론] 적용 |
| 1. 노출수 | 도달범위 → 노출수, "노출수 및 노출수가 시청 시간에 미치는 영향도" | 같은 창에서 5·6번 노출수가 1~4번보다 크게 적음 | 시스템이 아직 보여 줄 시청자를 못 찾음, 주제 수요가 작음(좁은 주제), 추천 대상이 아님, 초기 노출이 구독자·채널 페이지에만 머묾 | 주제·검색 수요 재검토(YouTube 검색어 보고서, Google Trends). 제목에 핵심어를 앞에 두고 정확하게 | [공식] 16767369·141805·12340300·15086271 / [추론] 원인 순서 |
| 2. 노출 클릭률 | 도달범위 → 노출 클릭률 (가능하면 트래픽 소스별: 탐색 기능/추천 동영상/YouTube 검색) | 노출은 비슷한데 같은 소스 기준 CTR이 채널 내 다른 영상보다 확연히 낮음(노출이 수천 회 이상일 때만 의미) | 썸네일·제목 매력 부족, 기존 시청자에게 익숙한 요소 부족 | 썸네일 단순화·가독성, 대상(구독자 vs 새 시청자)에 맞춘 구성. 노출이 충분하면 A/B 테스트 | [공식] 7628154·12340300·13861714 / [추론] 노출 수 기준선 |
| 3. 시청 지속 | 참여도 → 평균 시청 지속 시간, 시청 지속 시간 보고서(인트로·하락 구간), '일반적인 시청 지속 시간' | CTR은 높은데 인트로(30초 후 유지율)·평균 시청 지속 시간이 낮음 | 제목·썸네일과 내용 불일치, 초반 전개가 느림 | 첫 30초를 제목·썸네일 약속과 맞추기, 핵심 내용을 앞으로. 조회수 100회 미만이면 보고서가 안 나오므로 다음 영상에서 확인 | [공식] 9314415·7628154 |
| 4. 트래픽 소스 구성 | 도달범위 → "시청자가 이 동영상을 찾는 방법" | 1~4번 조회수가 대부분 외부·직접 입력(공유·링크)이고, 5·6번은 그런 유입이 없음 | 알고리즘 문제가 아니라 외부 유입(지인·커뮤니티 공유)이 소진됨 | 조회수를 외부 유입과 YouTube 내부 유입(탐색 기능·추천 동영상·검색)으로 나눠 평가. 내부 유입만으로 비교 | [공식] 9314355 정의 / [업계 관행·추론] 해석 |
| 5. 시청자층 | 시청자층 → 신규/일반/정기적으로 방문하는 시청자 | 5·6번에서 기존 시청자(일반·정기) 비율이 급감 | 주제·형식 변화로 기존 관심층과 어긋남 | 기존 시청자를 지킬지 새 시청자를 끌지 정하고 일관성 또는 실험을 의도적으로 선택 | [공식] 15086271·10246996 / [추론] 적용 |
| 6. 바뀐 요소 점검 | 업로드 기록 대조 | 5번에서 카테고리·주제·썸네일 스타일·길이·업로드 요일 등 여러 개가 함께 바뀜 | 원인 분리 불가 | 변경 목록을 표로 정리. 카테고리가 원인이라는 가설은 다른 연구자 결과와 교차 확인 | [공식] 15086271 / [추론] 적용 |
| 7. 재측정 | 같은 창(7일·28일)으로 비교 | — | — | 다음 영상에서는 한 가지만 바꾸고 같은 창으로 측정. 오래된 영상은 나중에도 추천될 수 있으므로 삭제·성급한 재업로드는 피함 | [공식] 15086271·141805 / [2차] Beaupré 2024·2026 / [추론] 적용 |

- [추론] 위 표를 이 채널에 대입한 최우선 확인 3가지: ① 6번 영상의 게시 경과 시간과 1~4번의 '같은 경과 시간' 조회수·노출수 ② 1~4번 조회수의 트래픽 소스 구성(외부·직접 비중이 크면 '하락'의 상당 부분은 외부 유입 소진으로 설명될 수 있음) ③ 5·6번의 노출수 자체가 적은지(노출 문제), 노출은 있는데 CTR이 낮은지(패키징 문제), CTR은 정상인데 시청 지속이 낮은지(내용·기대 불일치)의 구분.
- [업계 관행·추론] '노출 → CTR → 시청 지속 → 트래픽 소스 → 시청자층' 순서는 YouTube가 공식 진단 순서로 제시한 것이 아니다. 공식 Appeal → Engagement → Satisfaction 틀(16559650)과 지표 위치(9002587)를 조사자가 묶어 만든 순서다.

### Gaps
- YouTube가 '노출 → CTR → 시청 지속 시간' 순서의 진단 체크리스트를 공식 문서로 낸 것은 찾지 못함 → 순서 자체는 추론.
- 영상이 추천 대상(eligible)에서 빠졌는지 분석에서 직접 확인하는 방법: 공식 문서에 없음 → 확인 불가.
- 카테고리 필드가 노출에 미치는 영향은 이 조사의 범위 밖(다른 연구자 담당)이라 표에서 '원인 후보'로만 둠.

## Q6. 신규 채널이 시청자를 찾기까지 필요한 업로드 수·기간에 대한 YouTube 공식 언급이 있나

### Takeaway
**확인 불가.** 신규 채널이 자리 잡는 데 필요한 업로드 수나 기간을 숫자로 밝힌 YouTube 공식 발언·문서는 찾지 못했다. 관련 공식 발언은 '업로드 간격과 조회수 성장은 상관이 없다', '영상 하나가 부진해도 채널 전체가 손해 보지 않는다', '각 영상의 잠재력을 개별적으로 평가한다' 같은 정성적 내용뿐이다.

### Cited Findings
- [공식] "Do I need to upload daily or at least once a week?" → "…found that growth in views across uploads is not correlated with time between uploads." — [141805](https://support.google.com/youtubecreatorstudio/answer/141805?hl=en)
- [공식] "We studied thousands of channels that took a break and found no correlation between break length and changes in views." — [141805](https://support.google.com/youtubecreatorstudio/answer/141805?hl=en)
- [공식] "If one of my videos under-performs, is that going to hurt my channel?" → "What can lead to a decline in overall channel views is when viewers stop watching most of your videos" — [141805](https://support.google.com/youtubecreatorstudio/answer/141805?hl=en)
- [2차] Beaupré: "If your last video wasn't so great and your next video is great, we want to realize the potential of each video," "We aim to not overemphasize historical data if that data isn't particularly predictive of future video performance," — [SEJ, 2024-03-04](https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/)
- [2차] Beaupré: "We're not going to decide just based on the first hour or first 1,000 people who see a video" — [OutlierKit, 2026-09-07 (Creator Insider 2026-09-01 인용)](https://outlierkit.com/resources/youtube-video-slow-start/)
- [공식] 시청자 세그먼트는 "do not affect reach or monetization." — [10246996](https://support.google.com/youtube/answer/10246996?hl=en)

### Inferences
- [추론] 공식 발언들을 종합하면 YouTube는 '채널이 N개를 올려야 풀린다' 식의 관문을 공식적으로 인정하지 않고, 영상 단위로 시청자를 찾는다고 설명한다. 따라서 "영상 6개면 아직 이르다/충분하다"는 판단은 공식 근거로 내릴 수 없고, 같은 창 기준 노출·CTR·시청 지속 추세로 판단해야 한다.
- [추론] 영상 6개, 조회수 20~300회 수준의 데이터는 Q4의 작은 표본 한계 때문에 채널 방향을 확정하기엔 부족하다. 다만 '관찰 → 한 가지 변경 → 재측정'을 시작하기에는 충분하다.

### Gaps
- 신규 채널이 시청자를 찾는 데 필요한 업로드 수·기간에 대한 공식 수치: **확인 불가 (unverified)**.
- Rene Ritchie가 신규 채널 성장 기간을 언급했다는 2차 요약(예: "Small creators grow their channels from zero subscribers to several thousand every year")은 원문·날짜를 검증하지 못해 근거로 쓰지 않음.
