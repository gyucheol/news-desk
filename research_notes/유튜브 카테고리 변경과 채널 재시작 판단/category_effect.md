# 동영상 카테고리 설정(인물/블로그 vs 교육)이 추천·발견·조회수에 미치는 영향

조사일: 2026-11-06. 근거 라벨: **[공식/Official]** YouTube·Google 1차 자료 · **[2차/Secondary]** 공식 발언을 전한 보도 · **[제3자/Third-party]** 도구업체·교육자 의견/실험 · **[커뮤니티/Community]** 개인 경험담·SNS 주장. 날짜 표기가 없는 공식 페이지는 "날짜 없음, 접속일 2026-11-06"으로 기록. 인용문은 원문 언어 그대로 둠.

## 1. YouTube/Google은 카테고리 필드의 목적과 효과를 공식적으로 뭐라고 하는가? 랭킹·추천 신호로 명시된 적이 있는가?

### Takeaway
공식 문서가 밝히는 카테고리의 목적은 "시청자가 동영상을 더 쉽게 찾도록" 분류하는 것뿐이다. 추천/검색 랭킹을 설명하는 공식 페이지(검색 및 발견 팁, 추천 시스템 'Good to know', How YouTube Works)와 Data API 문서 어디에도 카테고리는 랭킹 신호로 나오지 않는다. 공식적으로 열거된 신호는 시청자 반응(시청 시간, 시청 비율, 좋아요·싫어요, 만족도 설문), 개인화(시청·검색 기록), 맥락(시간대, 기기)이다. 알고리즘 관점에서 카테고리를 직접 다룬 공식 발언은 2024년 8월 Todd Beaupré의 "minor consideration" 하나뿐이다(2번 질문 참조).

### Cited Findings
- [공식] YouTube 고객센터 "Edit video settings – Computer"(동영상 설정 수정)의 카테고리 항목 원문: "Select a category so viewers can find your video more easily." 한국어판 원문: "시청자가 동영상을 더 쉽게 찾을 수 있도록 카테고리를 선택하세요." 날짜 없음(푸터 ©2026), 접속일 2026-11-06, 원문 HTML 직접 확인. — [YouTube Help (en)](https://support.google.com/youtube/answer/57404?hl=en); [YouTube 고객센터 (ko)](https://support.google.com/youtube/answer/57404?hl=ko). 브리프에 있던 answer/187594 링크도 같은 "Edit video settings - Computer" 페이지와 같은 문장을 반환함 — [answer/187594](https://support.google.com/youtube/answer/187594?hl=en)
- [공식] YouTube Studio UI 문구. 2024년 8월 공식 클립에 삽입된 Studio 화면 캡처를 프레임 추출로 직접 판독: "Category — Add your video to a category so that viewers can find it more easily" (예시 선택값 "Entertainment"). — [X @YouTubeLiaison, 2024-08-21](https://x.com/YouTubeLiaison/status/1826056123897753609)
- [공식] 고객센터 "Search & discovery tips" 원문(날짜 없음, 접속일 2026-11-06, WebFetch로 재확인): "Videos are ranked based on performance and viewer personalization, including their watch and search history." / "Our system has no opinion about what type of video you make, and doesn't favor any particular format." / "Our systems use both avg. view duration and avg. % viewed as signals to inform ranking." / "Lastly, we look at whether or not viewers enjoyed the video using likes and post-watch survey results." 본문에 'category'라는 단어가 없고 tags, metadata, description도 언급하지 않음. 시청자 쪽 신호로는 과거에 즐긴 영상, 함께 시청되는 영상, 사용자가 특정 채널·주제(topic)를 얼마나 보는지를, 외부 요인으로는 주제 관심도·경쟁·계절성을 든다(이 문장은 원문이 아니라 의역). — [YouTube Help answer/11914225](https://support.google.com/youtube/answer/11914225?hl=en)
- [공식] 고객센터 "Good to know about recommendations for YouTube's recommendation system"(날짜 없음, ©2026, 한국어 URL도 영문 본문을 제공). 원문 HTML을 직접 확인한 결과 본문에 'category'와 '카테고리' 단어가 모두 없음. 주요 원문: "Our recommendation system aims to deliver the right content to the right viewer at the right time, optimized for each unique context. It learns from signals like time of day and device type to understand diverse viewing preferences." / "we use what a user discovers about topics or channels to inform recommendations across formats." — [YouTube Help answer/16559651](https://support.google.com/youtube/answer/16559651?hl=en)
- [공식] How YouTube Works의 Recommendations 페이지(날짜 없음, 접속일 2026-11-06). 신호로 "viewing behaviour, likes, dislikes, subscriptions and feedback, including from satisfaction surveys"를 들고, Watch Next 추천은 "guiding users to new content based on their watch history, broader viewer trends and current video topics."라고 설명함. 'category' 단어는 없음. — [How YouTube Works](https://www.youtube.com/howyoutubeworks/product-features/recommendations/)
- [공식] YouTube Data API 원문: "A videoCategory resource identifies a category that has been or could be associated with uploaded videos." snippet.assignable은 "Indicates whether videos can be associated with the category." 랭킹·추천 용도는 언급하지 않음(날짜 없음). — [Data API videoCategories](https://developers.google.com/youtube/v3/docs/videoCategories)
- [공식] Data API videos 리소스. snippet.categoryId는 "The YouTube video category associated with the video."이고, 영상마다 따로 있는 속성이며 videos.update를 호출할 때 필수값임("You must set a value for this property if you call the videos.update method"). 이와 별개로 topicDetails.topicCategories[]는 "A list of Wikipedia URLs that provide a high-level description of the video's content."임. relevantTopicIds는 2016-11-10에 지원 중단되었고, Freebase 폐기 후 2017-02-27부터 "a small set of curated topic IDs"만 반환됨. 문서는 topicDetails를 누가 부여하는지 밝히지 않음. — [Data API videos](https://developers.google.com/youtube/v3/docs/videos)

### Inferences
- 공식 문서들은 일관되게 시청자 반응, 개인화, 맥락을 랭킹 신호로 설명하고, 카테고리는 "찾기 쉽게 하는 분류"로만 설명한다. 카테고리를 주요 랭킹·추천 신호로 볼 공식 근거는 없다.
- 공식 문서와 논문이 말하는 "topic(주제)"은 크리에이터가 고르는 카테고리(categoryId)와 다른 개념일 가능성이 높다. Data API에 위키백과 URL 기반의 topicDetails가 따로 있고, 고객센터 설정 목록 중 추출한 범위에서는 topic 입력란이 보이지 않았다. 다만 topicDetails를 시스템이 자동으로 부여하는지는 문서에 명시되지 않았으므로 추론이다.

### Gaps
- 카테고리가 랭킹 신호인지에 대해 고객센터 문서에 "예/아니오"로 답한 문장은 없음. Beaupré 클립이 유일한 직접 발언.
- TeamYouTube(X)나 YouTube Help Community의 공식 직원(Community Manager)이 카테고리의 추천 효과를 답한 기록: 확인 불가(검색 범위 내 미발견).
- Creator Insider 롱폼 영상 중 카테고리를 다룬 회차: 확인 불가.

## 2. 2024-08-21 @YouTubeLiaison 게시물(Todd Beaupré 답변)의 정확한 원문과 기타 카테고리 관련 공식 발언

### Takeaway
그 답변은 이미지가 아니라 **13.7초짜리 세로 영상**이다. 화면 번인 자막을 프레임 단위로 판독한 원문은 **"I think we might look at that to understand what your video might be about, but it's really a minor consideration. So just choose the best one."** 즉 "영상이 무엇에 관한 것인지 이해하는 데 참고할 수는 있지만 매우 사소한 고려사항"이라는 답이다. 일부 2차 요약에 나온 "It is all about the audience"는 같은 시리즈의 **다른 질문**("알고리즘을 만족시키는 비결은?")에 붙은 요약으로, 카테고리 답변으로 인용한 것은 잘못이다.

### Cited Findings
- [공식] 게시물 본문 원문: "Does the algorithm care what category you choose for your video? I asked @hitsman ! https://t.co/JI9wGHWEJN". 작성 시각 2024-08-21T00:38:01Z(미 태평양시 2024-08-20 17:38). @hitsman의 표시명은 "Todd B."(X 사용자 ID 945961). 첨부 미디어는 type "video", 길이 13,680ms, 9:16(720×1280)으로 이미지가 아님. 2026-11-06 X syndication 데이터로 직접 조회. — [X 게시물](https://x.com/YouTubeLiaison/status/1826056123897753609); [syndication 데이터](https://cdn.syndication.twimg.com/tweet-result?id=1826056123897753609&lang=en&token=4)
- [공식] 영상 화면 문구를 직접 판독함(ffmpeg으로 전체 1fps, 자막 영역 10fps 프레임 추출). 질문 카드: "HEY TODD! DOES THE CATEGORY MATTER TO THE ALGORITHM?" 답변 자막은 한 단어씩 뜨는 번인 자막이며 구두점은 필자가 붙임: "I THINK WE MIGHT LOOK AT THAT TO UNDERSTAND WHAT YOUR VIDEO MIGHT BE ABOUT BUT IT'S REALLY A MINOR CONSIDERATION SO JUST CHOOSE THE BEST ONE". 문장으로 옮기면 "I think we might look at that to understand what your video might be about, but it's really a minor consideration. So just choose the best one." 중간에 Studio 카테고리 설정란 캡처("Add your video to a category so that viewers can find it more easily")가 삽입됨. — [X 게시물 영상](https://x.com/YouTubeLiaison/status/1826056123897753609/video/1)
  - 한계: 음성인식 도구가 없어 오디오는 따로 받아 적지 못했다. 위 원문은 공식 계정이 넣은 번인 자막 기준이며, 자막과 실제 발화가 미세하게 다를 가능성은 배제할 수 없다.
- [2차] Search Engine Roundtable(Barry Schwartz, 2024-09-03) "YouTube SEO Questions Answered" 원문: "(1) Does the algorithm care what category you choose for your video? A little bit?" SER도 답을 "조금"으로 요약함. 같은 글의 (2)는 "What's the secret to pleasing the algorithm? It is all about the audience:"(트윗 1826365170840662480, 2024-08-21). 즉 "It is all about the audience"는 카테고리 질문이 아니라 (2)번 질문의 요약이다. 같은 시리즈의 다른 답(모두 짧은 영상): 태그 "Not really important:"(08-22), 해시태그 "Same, not much:"(08-22), 업로드 주기 "Yes, but maybe more to you and your audience than the recommendation algorithm!"(08-26), 설명란 "Keywords do matter but do not stuff them:"(08-27), 파일명 "No."(08-19), 임베드 영상의 낮은 유지율 "Nope."(09-02), 유료 프로모션 체크 "Nope."(09-04). — [Search Engine Roundtable](https://www.seroundtable.com/youtube-algorithm-seo-questions-38003.html)
  - 참고: 해당 기사 URL은 -38003이다. 브리프의 -38004는 같은 날 데일리 리캡으로 연결되며 카테고리 내용이 없다. — [SER 리캡](https://www.seroundtable.com/youtube-algorithm-seo-questions-38004.html)
- [공식, 관찰 사실] 2026-11-06 현재 X syndication 데이터는 이 게시물 작성 계정(ID 1186083026633134080)의 이름과 핸들을 "YouTube Creator Insider" / @YouTubeInsider로 반환한다(미디어 URL에는 /YouTubeLiaison/ 경로가 남아 있음). 핸들이 언제, 왜 바뀌었는지는 확인 불가이며 관찰 사실만 기록한다. — [syndication 데이터](https://cdn.syndication.twimg.com/tweet-result?id=1826056123897753609&lang=en&token=4)
- [공식] 카테고리를 직접 언급하지는 않지만 메타데이터 변경 효과에 관한 2026년 고객센터 원문: "Changing a video's title or thumbnail can lead to a shift in its performance, potentially resulting in more or fewer views. This is because altering the video's presentation changes how viewers interact with it. The systems respond to these new viewer interactions rather than the act of changing the title or thumbnail itself." — [YouTube Help answer/16559651](https://support.google.com/youtube/answer/16559651?hl=en)
- [2차] SEJ "20 Confirmed Facts About YouTube's Algorithm"(Matt G. Southern, 2024-07-24)는 "Topic/Category Matching" 항목에서 알고리즘이 "looks for videos covering topics or categories similar to the video being watched currently."라고 쓴다. 그러나 Beaupré나 Ritchie의 직접 인용이 없고, 크리에이터가 고르는 카테고리 필드를 가리키는지도 불분명하다. — [SEJ](https://www.searchenginejournal.com/youtube-algorithm-facts/403984/)
- [2차] SEJ "YouTube Algorithm Myths Debunked: Insights From The Growth Team"(2024-03-04, Beaupré와 Ritchie 인터뷰 요약)은 카테고리, 태그, 메타데이터를 다루지 않는다. — [SEJ](https://www.searchenginejournal.com/youtube-algorithm-myths-debunked-insights-from-the-growth-team/510091/)

### Inferences
- Beaupré의 답은 "전혀 안 본다"가 아니라 "내용을 이해하는 데 참고할 수는 있지만 사소하다"이다. SER의 요약 "A little bit?"과도 맞는다. 공식 입장에 따르면 카테고리는 사소한 고려사항이고, 이것이 채널 전체를 망가뜨리는 메커니즘은 어디에도 제시되지 않았다. 따라서 "카테고리를 한 번 바꿔서 채널이 고장 났다"는 해석은 공식 발언과 맞지 않는다.
- "So just choose the best one"이 공식 권고다. 교육 콘텐츠에 교육 카테고리를 고르는 것 자체를 문제 삼는 공식 발언은 없다.
- 발언은 2024년 8월 것으로 2년 넘게 지났다. 이를 번복한 공식 발언은 찾지 못했고, 2026년 고객센터 페이지들에도 카테고리 언급은 없다.

### Gaps
- 오디오를 따로 받아 적어 자막과 발화가 일치하는지 대조: 확인 불가(음성인식 도구 부재).
- 같은 클립의 Threads, LinkedIn, Bluesky, YouTube Shorts 사본: 확인 불가(미발견).
- Rene Ritchie나 TeamYouTube가 카테고리에 대해 따로 추가 설명한 기록: 확인 불가.

## 3. 공개된 YouTube 추천 시스템 논문은 어떤 입력 특성을 언급하나? (카테고리/메타데이터 vs 행동 신호)

### Takeaway
2016년 Covington 논문은 시청한 영상 ID, 검색어 토큰, 인구통계, 지역·기기, 언어, 채널·주제와 사용자의 과거 상호작용 같은 **행동 중심 특성**을 명시하고, 콘텐츠 메타데이터는 "poorly structured"라고 평가한다. 2019년 Zhao 논문은 "video meta-data and video content signals"와 "title and description"을 언급하고, 후보를 뽑는 알고리즘 중 하나로 "matching topics of query video"를 든다. **두 논문 모두 크리에이터가 고르는 카테고리 필드를 특성으로 명시하지 않는다.** 둘 다 7~10년 된 자료라 현재 시스템과 다를 수 있다.

### Cited Findings
- [공식/Google 연구] Covington, Adams, Sargin, "Deep Neural Networks for YouTube Recommendations", RecSys '16 (2016년 9월, Boston, DOI 10.1145/2959100.2959190). 원문:
  - "metadata associated with content is poorly structured without a well defined ontology."
  - "The similarity between users is expressed in terms of coarse features such as IDs of video watches, search query tokens and demographics."
  - "Demographic features are important for providing priors so that the recommendations behave reasonably for new users. The user's geographic region and device are embedded and concatenated."
  - 랭킹 단계: "consider the user's past history with the channel that uploaded the video being scored - how many videos has the user watched from this channel? When was the last time the user watched a video on this topic? These continuous features describing past user actions on related items are particularly powerful because they generalize well across disparate items."
  - "Our features are segregated with the traditional taxonomy of categorical and continuous/ordinal features." 여기서 'categorical'은 머신러닝 용어인 '범주형 특성'(예: 로그인 여부, 마지막 검색어)이며 YouTube 카테고리 필드가 아니다. 랭킹 구조도에는 "user language"와 "video language" 임베딩이 들어 있다.
  — [논문 PDF](https://static.googleusercontent.com/media/research.google.com/en//pubs/archive/45530.pdf)
- [공식/Google 연구] Zhao et al., "Recommending What Video to Watch Next: A Multitask Ranking System", RecSys '19 (2019년 9월, Copenhagen, DOI 10.1145/3298689.3346997). 원문:
  - "for each video, we extract features such as video meta-data and video content signals as its representation. For context, we use features such as user demographics, device, time, and location, etc."
  - "one algorithm generates candidates by matching topics of query video. Another algorithm retrieves candidate videos based on how often the video has been watched together with the query video."
  - "feature space generated from multiple modalities, e.g., video content, thumbnail, audio, title and description, user demographics."
  - 학습 라벨: "We use user behaviors as training labels"를 "engagement objectives and satisfaction objectives"의 두 범주로 나누고, "Engagement objectives capture user behaviors such as clicks and watches."라고 설명. 여기서 'two categories'는 목표를 나눈 것일 뿐 카테고리 필드가 아니다.
  — [논문 PDF(미러 사본)](https://daiwk.github.io/assets/youtube-multitask.pdf); [ACM DOI](https://doi.org/10.1145/3298689.3346997)
- 두 PDF 전문을 'categor'로 직접 검색한 결과(2026-11-06), 모든 용례가 '범주형 특성' 또는 '목표의 두 범주'라는 뜻이었고 크리에이터 지정 카테고리 필드는 나오지 않았다. — 위 두 PDF 링크

### Inferences
- 논문에 '주제(topic)' 매칭은 있지만, 그 주제가 크리에이터가 고르는 소수의 카테고리인지 시스템이 콘텐츠·제목·설명 등에서 뽑아낸 주제인지는 밝히지 않았다. 다음 세 가지를 종합하면 주제 이해는 주로 더 풍부한 신호(제목, 설명, 콘텐츠, 시청 행동)로 이루어지고 카테고리는 보조 정보일 가능성이 높다(추론): Data API에 topicDetails(위키백과 URL)가 따로 있다는 점, Covington의 "metadata... poorly structured" 평가, Beaupré의 "minor consideration".
- Covington이 인구통계를 "new users"를 위한 prior로 든 것은 시청자 쪽 콜드스타트 이야기이며, 신규 '채널'의 카테고리와는 무관하다.
- 논문이 나온 2016·2019년과 현재(2026년) 사이에 시스템이 많이 바뀌었다. 2026년 고객센터 페이지는 시간대·기기 같은 맥락 신호와 포맷을 넘나드는 관심 학습을 설명한다. 논문은 당시 구조를 보여주는 참고자료로만 써야 한다.

### Gaps
- 2020년 이후 YouTube 엔지니어 논문 중 크리에이터 카테고리 필드를 특성으로 명시한 자료: 확인 불가(이번 조사에서 미검토).
- 현재 운영 중인 시스템의 특성 목록은 비공개.

## 4. '교육'을 고르면 특별 처리나 별도 노출면이 생기는가? (아동용, 학습·강좌, YouTube Kids, 광고) 업로드 후 카테고리 변경이나 영상마다 다른 카테고리를 쓰는 것에 문서화된 효과가 있는가?

### Takeaway
공식 문서상 '교육'을 고르면 선택 입력란(교육 유형, 문제, 교육 제도, 등급, 시험·과정·기준)이 추가로 열린다. 그 외에 추천에서 특별히 다르게 처리된다는 문서는 없다. **아동용(Made for Kids)은 카테고리와 무관한 별도의 필수 '시청자층' 설정이다.** 업로드 후 카테고리를 바꾸거나 영상마다 다른 카테고리를 쓰는 것의 효과를 다룬 공식 문서는 없다. 공식 원칙은 "각 콘텐츠를 개별적으로 평가한다"와 "영상 하나의 성과가 저조하다고 채널 전체에 불이익을 주지 않는다"이다.

### Cited Findings
- [공식] 교육 카테고리 전용 옵션, 고객센터 원문: "For Education, you can choose the following options: Type: Select activity, concept overview, how-to, lecture, problem walkthrough, real life application, science experiment, tips, or other as your education type. Problems: Add the timestamp and the question that is answered in your video. Note: this option is only available for the problem walkthrough education type. Academic system: Select the country/region that your video aligns to. This allows you to further specify the level and exam, course, or academic standard. Note: This may be automatically selected based on your channel's default country/region. Level: Choose the level for your video, such as Grade 9 or advanced. Exam, course, or standard: Search our database to add an academic standard, exam, or course that relates to your video." 한국어판 원문: "교육용인 경우 다음 옵션을 선택할 수 있습니다. 유형: 교육 유형으로 활동, 개념 개괄, 가이드, 강의, 문제 풀이, 실생활 응용, 과학 실험, 팁 등을 선택합니다. … 교육 제도: 동영상에 맞는 국가/지역을 선택합니다. … 채널의 기본 국가/지역에 따라 자동으로 선택될 수 있습니다. 등급: 중학교 3학년 또는 고급과 같이 동영상의 수준을 선택합니다." 페이지는 이 필드들이 추천이나 검색에 어떻게 쓰이는지 설명하지 않는다. — [YouTube Help (en)](https://support.google.com/youtube/answer/57404?hl=en); [YouTube 고객센터 (ko)](https://support.google.com/youtube/answer/57404?hl=ko)
- [공식] 업로드 후에도 수정 가능: "After you upload a video, you can change your video details in YouTube Studio." (WebFetch로 추출) — [answer/187594](https://support.google.com/youtube/answer/187594?hl=en)
- [공식] 아동용은 별도 설정이다. 업로드할 때 "Basic info" 탭의 "Audience"에서 "Yes, it's 'Made for Kids'." 또는 "No, it's not 'Made for Kids'."를 고르고, 이미 올린 영상은 Content > Edit > Audience에서 바꾼다. "Settings for individual videos will override the channel setting." 아동용으로 지정하면 홈 자동재생, 카드·최종 화면, 워터마크, 멤버십, 댓글, 후원 버튼, 라이브 채팅, 상품, **알림 벨**, **맞춤형 광고**, 미니플레이어, Super Chat, 재생목록·나중에 볼 동영상 저장 등이 제한된다. 이 페이지는 카테고리 필드를 언급하지 않는다(WebFetch로 추출). — [YouTube Help answer/9527654](https://support.google.com/youtube/answer/9527654?hl=en)
- [공식] 아동용 판단 기준 페이지는 주제 예시로 "educational content for preschoolers"를 들지만, 이런 요소가 있다고 자동으로 아동용이 되지는 않는다고 설명한다. 아동용 영상은 "are more likely to be recommended alongside other kids' videos." 카테고리 필드는 언급하지 않는다. — [YouTube Help answer/9528076](https://support.google.com/youtube/answer/9528076?hl=en)
- [공식] Data API에서도 아동용 여부는 status.madeForKids와 status.selfDeclaredMadeForKids("allows the channel owner to designate the video as being child-directed")로, categoryId와 별개의 속성이다. — [Data API videos](https://developers.google.com/youtube/v3/docs/videos)
- [공식] 개별 평가 원칙, 2026년 고객센터 원문: "Experimenting with new content formats, such as Shorts, VODs, or livestreams, will not inherently confuse the algorithm or negatively impact a channel's overall performance. The system evaluates each piece of content individually, and its goal is to understand each user's preferred formats and topics." / "Any perceived effect on a channel from new formats is typically due to how viewers react to the new content, rather than a direct algorithmic penalty." / "An individual video's underperformance does not penalize a channel overall — What matters is how viewers respond to each video when it's recommended to them … Long-term channel performance can be affected, however, if a particular viewer consistently stops watching videos from a channel when they are recommended, or if viewers increasingly engage with content from other channels on YouTube." — [YouTube Help answer/16559651](https://support.google.com/youtube/answer/16559651?hl=en)
- [공식] 같은 페이지의 신규 채널 관련 원문: "For new channels, gaining this credibility and building a community takes time. A key factor here is developing a critical mass of content." — [YouTube Help answer/16559651](https://support.google.com/youtube/answer/16559651?hl=en)
- [공식] 메타데이터 변경의 효과는 '바꾸는 행위' 자체가 아니라 시청자 반응을 거쳐 나타난다(제목·썸네일 기준): "The systems respond to these new viewer interactions rather than the act of changing the title or thumbnail itself." — [YouTube Help answer/16559651](https://support.google.com/youtube/answer/16559651?hl=en)
- [제3자] vidIQ(2020-03-10, Carla Marshall): 카테고리는 Settings > Upload defaults에서 기본값으로 정할 수 있고("This is the video upload category default."), 이미 올린 영상은 하나씩 바꾼다. — [vidIQ](https://vidiq.com/blog/post/how-to-change-youtube-category-tutorial/)
- [제3자] 광고 관련: vidIQ는 "when it comes to advertisers finding the right videos to place their adverts on setting a video category is important."라고 주장한다(2020년, 근거 미제시). — [vidIQ](https://vidiq.com/blog/post/how-to-change-youtube-category-tutorial/)

### Inferences
- '교육' 카테고리를 고른다고 아동용으로 지정되거나 YouTube Kids에 노출된다는 공식 근거는 없다. 다만 영상 5·6이 카테고리와 별개로 실수로 Audience='Made for Kids'로 설정됐다면, 알림 벨·댓글·맞춤형 광고 등이 제한되어 노출이 크게 줄 수 있다. 분석 담당은 각 영상의 Audience 설정을 확인할 필요가 있다(카테고리와 별개의 점검 항목).
- 사용자 사례에서 영상 6을 인물/블로그로 되돌렸는데도 조회수가 약 20회였다는 사실은 오히려 카테고리 가설에 불리한 증거다. 카테고리가 원인이었다면 되돌린 영상은 회복했어야 한다(표본이 작아 단정은 불가).
- 공식 원칙(개별 평가, 영상 하나의 저조한 성과는 채널 페널티가 아님, 메타데이터 변경 효과는 시청자 반응을 거침)에 비추어 보면, "카테고리를 한 번 바꿔서 채널이 고장 났다"는 메커니즘은 공식 문서로 뒷받침되지 않는다.
- 교육 전용 필드는 교육 콘텐츠 관련 기능(문제 풀이, 학업 기준 연계 등)을 위한 구조화된 메타데이터로 보이지만, 그 용도는 공식적으로 설명되지 않았다(추론).

### Gaps
- 교육 전용 필드가 검색, 추천, 또는 교육 전용 노출면에 쓰이는지에 대한 공식 설명: 확인 불가.
- YouTube 'Courses(강좌)'나 학습 관련 기능이 카테고리와 연동되는지: 확인 불가(미조사).
- YouTube Kids 노출 기준과 카테고리의 관계: 확인 불가(공식 문서에서 카테고리 언급을 찾지 못함).
- Google Ads의 광고 타겟팅이나 광고 적합성 판단에 크리에이터가 지정한 카테고리를 쓰는지: 확인 불가(Google Ads 문서 미검토, vidIQ 주장만 있음).
- 업로드 후 카테고리를 바꿨을 때의 효과에 관한 공식 문서나 통제 실험: 발견하지 못함.
- (범위 밖, 미검증 단서) 한국어 검색 중 마케팅 블로그 두 곳이 2026년 8월경 롱폼 조회수 집계 기준이 바뀌었다고 주장함(재생이 시작되는 순간 1회로 집계). 영상 5·6 시기의 조회수 비교에 영향을 줄 수 있으므로 분석 담당이 공식 확인을 해야 한다. — [ampm 인사이트](https://inside.ampm.co.kr/insight/60783); [linkfarm.ai](https://linkfarm.ai/blog/youtube-view-count-change-creator-impact-2026)

## 5. 제3자(도구업체·교육자)의 주장과 한국 커뮤니티 통념, 그 근거 수준

### Takeaway
영어권 도구업체와 블로그는 대체로 "카테고리에 따른 알고리즘 가산점이나 불이익은 없거나 미미하고, 광고·분류용"이라고 말하지만 통제 실험 데이터는 내놓지 않는다. 한국어권 SNS에는 "카테고리가 매우 중요하고, 해당 카테고리를 좋아하는 시청자에게 뿌려진다"는 주장이 있으나 근거가 없다. 카테고리 변경 전후 조회수를 데이터로 보여준 한국어 자료는 찾지 못했다.

### Cited Findings
- [제3자] vidIQ(2020-03-10, 前 콘텐츠 마케팅 총괄 Carla Marshall): "to the best of our knowledge, there is no algorithmic boost or penalty if you do indeed put the video in the right or wrong category". 근거 데이터 없음, 6년 전 자료. — [vidIQ](https://vidiq.com/blog/post/how-to-change-youtube-category-tutorial/)
- [제3자] vidIQ 2020년 영상의 요약 사본도 같은 취지(검색 요약으로만 확인, 원문 미검토). — [rosetta.to/vidiq](https://rosetta.to/u/vidiq/how-to-change-your-youtube-video-category-in-2020-new-method)
- [제3자] Wild & Free Tools(2026)는 'Reddit 기반 분석'이라며, 카테고리가 첫 24~72시간의 초기 시청자 매칭 신호 중 하나라고 주장한다. 인물/블로그에서 더 구체적인 카테고리로 바꿨더니 조회수는 거의 그대로이고 RPM만 나아졌다는 사례도 든다. 출처 불명이고 검색 요약으로만 확인했으며(원문 미검토), 공식 근거는 없다. — [wildandfreetools (reddit 2026)](https://wildandfreetools.com/blog/youtube-category-reddit-2026/); [wildandfreetools](https://wildandfreetools.com/blog/does-youtube-video-category-matter/)
- [제3자] Veefly 가이드는 카테고리가 조회수에 영향을 준다고 주장한다. Veefly는 조회수 프로모션 판매 업체라 이해관계가 있는 홍보성 출처이고, 근거를 제시하지 않았다(검색 요약으로만 확인). — [Veefly](https://blog.veefly.com/guide/how-to-change-your-youtube-videos-category-in-just-a-few-steps/)
- [커뮤니티] Threads @sogumi.i(작성일은 게시물 ID를 디코딩해 약 2024-08-05로 추정, 추론). 검색 스니펫 원문이며 HTML에서 "카테고리 매우 중요하다." 문구를 확인함: "카테고리 매우 중요하다. 본인의 채널이 예를 들어 "엔터테인먼트"로 분류가 되어 있으면 유튜브 알고리즘이 시청자들에게 영상을 노출 해줄 때 엔터테인먼트를 좋아하는 사람들에게 뿌려줄 가능성이 높다. 그렇기 때문에 카테고리는 필수로 선택을 해줘야한다." 공식 출처나 데이터 같은 근거는 제시하지 않았다. — [Threads](https://www.threads.com/@sogumi.i/post/C-R-vr2Sw0G?hl=ko)
- [제3자] 블링(vling.net, Reean, 2023-05-24) "유튜브 알고리즘 타는 법"은 동영상 카테고리 설정을 언급하지 않고, "알고리즘이 작동하는 과정에서 SEO(검색 엔진 최적화), 시청 시간, 참여율이 중요하게 작용해요."라고 쓴다. 이 글에서 '카테고리'는 검색·홈·추천 영상 같은 노출 경로를 가리킨다. — [vling](https://vling.net/post/223110339184)
- [제3자/학술, 무관] 국내 학술 논문(정보과학회지, 2015) "사용자의 소셜 카테고리를 이용한 유튜브동영상 추천 알고리즘"은 외부 연구자가 제안한 알고리즘이라 YouTube 실제 시스템의 근거가 아니다(제목만 확인). '카테고리가 추천에 쓰인다'는 오해의 소지가 있다. — [KCI](https://www.kci.go.kr/kciportal/ci/sereArticleSearch/ciSereArtiView.kci?sereArticleSearchBean.artiId=ART001990971)
- [제3자] 한국어 키워드("유튜브 카테고리 변경 조회수 알고리즘 영향", "유튜브 카테고리 인물/블로그 교육 바꾸면 조회수", "카테고리 바꿨더니 조회수 유튜브 인물블로그", "유튜브 카테고리 설정 알고리즘 상관 없다")로 검색했지만, 카테고리 변경 전후 데이터를 제시한 한국어 사례나 실험은 나오지 않았다. 신한대 KOCW 강의 "유튜브 카테고리 설정으로 영상 분류하기"는 분류 방법만 설명한다. — [KOCW](http://www.kocw.net/home/cview.do?mty=p&kemId=1315051)

### Inferences
- 한국 커뮤니티의 "카테고리가 알고리즘 분류의 열쇠"라는 통념은 공식 발언(Beaupré: "minor consideration") 및 공식 문서(신호 목록에 카테고리 없음)와 맞지 않는다. 근거 수준은 개인 주장 정도다.
- 제3자 자료 중 "카테고리가 조회수를 의미 있게 바꾼다"는 쪽은 이해관계가 있는 홍보 업체이거나 출처가 불명하다. "영향 없음, 또는 미미"라는 쪽은 공식 발언과 일치한다. 어느 쪽도 같은 영상으로 A/B 비교하는 식의 통제 실험은 내놓지 않았다.

### Gaps
- TubeBuddy, Think Media, Film Booth의 카테고리 관련 구체 발언이나 실험: 확인 불가(이번 조사에서 원문을 찾지 못함).
- 네이버 블로그·카페, 한국어 YouTube 고객센터 커뮤니티의 카테고리 경험담: 검색 엔진(미국 기준) 노출 한계로 확인 불가.
- 카테고리 변경 효과를 통제 실험한 공개 데이터: 발견하지 못함.
