import json, re, sys

OUT = '/home/user/news-desk/data/mix-2026-10-14c/out2/W1.json'
TAIL = re.compile(r' \((제목 기준|채널 전언)\)$')

def plain(s):
    return s.replace('{{', '').replace('}}', '')

def body(s):
    return TAIL.sub('', s)

def chunks(s):
    return re.findall(r'\{\{(.*?)\}\}', s)

def check_text(label, s, lo, hi, end_da=True):
    issues = []
    b = body(s)
    p = plain(b)
    ch = chunks(b)
    n = len(p)
    r = (sum(len(c) for c in ch) / n) if n else 0
    if not (lo <= n <= hi):
        issues.append(f'len {n} not in {lo}-{hi}')
    if not (0.50 <= r <= 0.66):
        issues.append(f'ratio {r:.2f}')
    if s.count('{{') != s.count('}}'):
        issues.append('unbalanced')
    if re.search(r'\{\{[^}]*\{\{', s):
        issues.append('nested')
    for c in ch:
        if len(c) > 30:
            issues.append(f'chunk>30: {c}')
        if c != c.strip():
            issues.append(f'chunk space: [{c}]')
        if c and c[-1] in ',.·…':
            issues.append(f'punct end: {c}')
    m = TAIL.search(s)
    if m and '{{' in m.group(0):
        issues.append('tail emph')
    if end_da and not p.endswith('다'):
        issues.append('not ending with 다')
    return n, r, issues

def validate(items):
    bad = 0
    for x in items:
        cid = x['cid']
        single = len(x['items']) == 1 and not x['attachTo']
        rep = []
        n, r, iss = check_text('title', x['title'], 20, 50, end_da=False)
        rep.append(f'  title {n}자 {r:.2f} {iss}')
        bad += len(iss)
        lo, hi = (80, 130) if single else (90, 160)
        n, r, iss = check_text('one', x['one'], lo, hi)
        rep.append(f'  one {n}자 {r:.2f} {iss}')
        bad += len(iss)
        if not (2 <= len(x['facts']) <= 5):
            rep.append('  facts count'); bad += 1
        for f in x['facts']:
            if '{{' in f or '|' in f or '**' in f or not re.search(r'\[(사실|채널|제목|추론|미확인)\]$', f):
                rep.append(f'  fact issue: {f[:40]}'); bad += 1
        if not x['facts'][0].startswith('무엇이:'):
            rep.append('  first fact not 무엇이'); bad += 1
        if single:
            if x.get('added') or any('s' in it for it in x['items']):
                rep.append('  single item must not have s/added'); bad += 1
        else:
            n, r, iss = check_text('added', x.get('added', ''), 60, 140)
            rep.append(f'  added {n}자 {r:.2f} {iss}')
            bad += len(iss)
        for it in x['items']:
            tl = len(it['t'])
            if not (25 <= tl <= 60):
                rep.append(f'  t len {tl}: {it["t"]}'); bad += 1
            if not single:
                n, r, iss = check_text('s', it['s'], 45, 110)
                rep.append(f'  s {n}자 {r:.2f} {iss}')
                bad += len(iss)
        ds = [it['d'] for it in x['items']]
        if ds != sorted(ds):
            rep.append('  items not in time order'); bad += 1
        if x['basis'] == 'title' and not x['one'].endswith(' (제목 기준)'):
            rep.append('  title basis tail missing'); bad += 1
        if x['basis'] == 'channel' and not x['one'].endswith(' (채널 전언)'):
            rep.append('  channel basis tail missing'); bad += 1
        print(cid, x['basis'])
        print('\n'.join(rep))
    print('TOTAL ISSUES', bad)

ITEMS = []
SKIPPED = []

# ---------------- C001 ----------------
ITEMS.append({
 "cid": "C001", "attachTo": "n-tg-0221",
 "title": "{{애플}}, {{299달러 '홈뷰'}}로 시리 AI 스마트홈 {{첫선}}…{{OLED 맥북}}은 {{27일께}}",
 "one": "{{애플}}이 {{시리 AI}}를 앞세운 {{299달러 스마트홈 허브 '홈뷰'}}와 {{149달러 홈팟 미니 2}}를 {{공개}}하고 {{10월 27일께}}엔 첫 {{OLED 맥북 프로}}도 내놓을 예정이어서, {{아마존·구글}}과의 {{스마트홈 경쟁}}이 {{본격화될}} 전망이다",
 "facts": [
  "무엇이: 애플이 10월 13일 7인치 화면을 단 299달러 스마트홈 허브 '홈뷰'(11월 13일 출시)와 새 애플TV 4K, 149달러 홈팟 미니 2(10월 30일 출시)를 공개했다 [사실]",
  "기능: 홈뷰는 베타로 들어간 시리 AI를 중심에 두고 가족 최대 6명을 얼굴로 알아보며 Matter·Thread를 지원하지만, 모든 사용자에게 최신 OS 아이폰이 필요하고 EU에서는 출시 때 팔지 않는다 [사실]",
  "시장 시각: 로이터는 홈뷰가 아마존·구글에 맞선다고, 블룸버그는 비싼 애플 주가를 되살리려면 아이폰과 스마트홈 성과가 필요하다고 짚었다 [제목]",
  "기존: 애플은 10월 27일 전후 행사에서 첫 터치스크린 OLED 맥북 프로와 OLED 아이패드 미니, M6 칩 아이맥 등을 내놓을 계획으로 알려졌다 [사실]"
 ],
 "basis": "verified",
 "check": "홈뷰 가격(299달러)·7인치 화면·11월 13일 출시·얼굴 인식 6명·시리 AI 베타·EU 미출시·Matter/Thread 지원, 홈팟 미니 2(149달러·10월 30일)는 검색 결과 요약(CNBC·기즈모도·쿼츠·CNN)으로 확인. 새 애플TV 4K의 가격·출시일은 한 곳에서만 봐 쓰지 않음. 주가 관련 블룸버그 글은 제목만 근거.",
 "src": [
  {"o": "CNBC", "d": "2026-10-13", "u": "https://www.cnbc.com/2026/10/13/apple-homeview-smart-home-siri-ai.html"},
  {"o": "기즈모도", "d": "2026-10", "u": "https://gizmodo.com/homeview-apple-smart-home-hub-2000824152"},
  {"o": "쿼츠", "d": "2026-10-13", "u": "https://qz.com/apple-homeview-smart-home-hub-299-101326"},
  {"o": "CNN 언더스코어드", "d": "2026-10", "u": "https://www.cnn.com/cnn-underscored/electronics/apple-homeview-hands-on"}
 ],
 "inds": ["tech"], "nodes": [],
 "added": "이번 블룸버그 2건·로이터 2건으로 {{애플}}의 {{299달러 스마트홈 허브 '홈뷰'}}·{{홈팟 미니 2}} {{공개}}와 {{시리 AI}}를 앞세운 {{아마존·구글과의 경쟁}}, {{주가 반등 과제}}가 추가됐다",
 "items": [
  {"t": "애플, 비싼 주가 되살리려면 아이폰·스마트홈 성과 필요", "o": "블룸버그", "d": "2026-10-13",
   "u": "https://www.bloomberg.com/news/articles/2026-10-13/apple-needs-phones-and-smart-homes-to-revive-pricey-stock",
   "s": "{{비싼 애플 주가}}를 {{되살리려면}} {{아이폰}}과 {{스마트홈}}에서 {{성과}}가 {{필요}}하다는 {{분석}}이 나오면서, {{이달 신제품}}이 {{주가 반등의 시험대}}에 {{올랐}}다 (제목 기준)"},
  {"t": "애플, 299달러 스마트홈 허브 '홈뷰'·새 애플TV 4K·홈팟 미니 2 공개", "o": "블룸버그", "d": "2026-10-13",
   "u": "https://www.bloomberg.com/news/features/2026-10-13/apple-unveils-299-homeview-smart-home-hub-new-apple-tv-4k-homepod-mini-2",
   "s": "{{애플}}이 {{299달러 스마트홈 허브 '홈뷰'}}와 {{새 애플TV 4K}}, {{홈팟 미니 2}}를 함께 {{공개}}하면서 {{홈 기기 제품군}}을 한꺼번에 새로 짰다"},
  {"t": "애플 홈뷰, 개인화 시리로 스마트홈 공략…아마존·구글에 도전", "o": "로이터", "d": "2026-10-14",
   "u": "https://www.reuters.com/business/retail-consumer/apples-homeview-brings-personalized-siri-smart-home-takes-amazon-google-2026-10-13/",
   "s": "{{애플 홈뷰}}가 {{가족 최대 6명}}을 얼굴로 알아보는 {{개인화 시리}}를 {{스마트홈}}에 들이면서 {{아마존·구글}}의 {{스마트홈 기기}}에 {{정면으로 맞선}}다"},
  {"t": "애플, 업데이트된 시리 AI 내세운 스마트홈 신제품 공개", "o": "로이터", "d": "2026-10-14",
   "u": "https://www.reuters.com/business/retail-consumer/apple-unveil-new-smart-home-products-showcasing-updated-siri-ai-2026-10-13/",
   "s": "{{애플}}이 {{업데이트된 시리 AI}}를 내세운 {{스마트홈 신제품}}을 {{공개}}했지만 {{시리 AI}}는 {{베타}}로 시작하고 {{EU}}에서는 {{출시 때 팔지 않아}} {{초기 보급}}이 {{제한될}} 수 있다"}
 ]
})

# ---------------- C007 ----------------
ITEMS.append({
 "cid": "C007", "attachTo": "n-rtr-0127",
 "title": "{{로슈·질랜드}}, {{비만약}} 잇따라 {{도입}}…{{中 로나}}·{{제너레이트}}와 최대 {{11억~12억 달러}} 계약",
 "one": "{{로슈}}가 {{中 로나 테라퓨틱스}}와 {{최대 11억 6,000만 달러}}, {{질랜드파마}}가 {{제너레이트}} 바이오메디슨과 {{최대 약 12억 달러}} 규모의 {{비만약 계약}}을 잇따라 맺으면서, {{페트렐린타이드}}를 함께 개발하는 두 회사의 {{비만 파이프라인}}이 {{중국 신약}}과 {{AI 설계 단백질}}로 {{넓어지고}} 있다",
 "facts": [
  "무엇이: 질랜드파마가 10월 13일 제너레이트 바이오메디슨과 AI로 설계한 비만·대사질환용 다중특이 단백질 치료제를 개발하는 협력·라이선스 계약을 맺었고, 제너레이트가 후보 선정까지 연구를, 질랜드가 임상·허가·전 세계 판매를 맡는다 [사실]",
  "조건: 제너레이트는 선급금 3,000만 달러와 초기 전임상 마일스톤 최대 3,500만 달러를 포함해 최대 약 12억 달러의 마일스톤과 단계별 로열티를 받으며, 대상은 2개 프로그램(3번째 추가 선택권)이다 [사실]",
  "로슈: 로슈가 중국 로나 테라퓨틱스와 최대 11억 6,000만 달러 규모의 비만약 기술도입 계약을 맺었다 [제목]",
  "로슈 세부: 선급금 1억 달러와 마일스톤 최대 10억 6,000만 달러, 대상은 ALK7을 겨냥한 RNAi 후보물질이라는 내용은 로이터 전재본에서만 봤다 [미확인]",
  "기존: 질랜드·로슈의 페트렐린타이드는 2형 당뇨 환자 2상에서 28주간 체중을 최대 9.2% 줄였고, 두 회사는 3상 3건을 시작했다 [사실]"
 ],
 "basis": "partial",
 "check": "질랜드–제너레이트 계약(10월 13일, 선급금 3,000만 달러·초기 마일스톤 최대 3,500만 달러·최대 약 12억 달러, 2개 프로그램, 역할 분담)은 두 회사 보도자료(글로브뉴스와이어) 검색 결과 요약으로 확인. 로슈–로나 계약은 로이터 전재본(야후·유로넥스트·KSL·마켓스크리너)만 검색돼 독립 출처로 확인 못 함(금액은 제목 근거, 선급금·ALK7 RNAi는 미확인).",
 "src": [
  {"o": "글로브뉴스와이어(제너레이트·질랜드 보도자료)", "d": "2026-10-13", "u": "https://www.globenewswire.com/news-release/2026/10/13/3380182/0/en/generate-biomedicines-and-zealand-pharma-enter-collaboration-and-license-agreement-to-develop-protein-therapeutics-engineered-with-ai-for-metabolic-diseases.html"}
 ],
 "inds": ["pharma"], "nodes": [],
 "added": "이번 로이터 2건·블룸버그 1건으로 {{로슈}}가 {{中 로나}}에서, {{질랜드}}가 {{제너레이트}}에서 각각 {{최대 11억 6,000만 달러}}·{{최대 약 12억 달러}} 규모로 {{비만약 후보를 들여오는 계약}}이 추가됐다",
 "items": [
  {"t": "로슈, 中 로나와 최대 11억 6,000만 달러 비만약 기술도입 계약", "o": "로이터", "d": "2026-10-13",
   "u": "https://www.reuters.com/business/healthcare-pharmaceuticals/roche-strikes-obesity-drug-licensing-deal-worth-up-116-bln-with-chinese-rona-2026-10-13/",
   "s": "{{로슈}}가 {{중국 로나 테라퓨틱스}}와 {{최대 11억 6,000만 달러}} 규모의 {{비만약 기술도입 계약}}을 맺으면서 비만 파이프라인에 {{중국 후보물질}}을 {{더한}}다 (제목 기준)"},
  {"t": "질랜드파마, 제너레이트와 최대 12억 달러 규모 계약", "o": "블룸버그", "d": "2026-10-14",
   "u": "https://www.bloomberg.com/news/articles/2026-10-13/zealand-pharma-makes-deal-with-generate-worth-up-to-1-2-billion",
   "s": "{{질랜드파마}}가 {{제너레이트}}와 {{최대 약 12억 달러}} 규모 계약을 맺으면서 {{AI로 설계한 다중특이 단백질}}을 {{비만·대사질환}} 신약 후보로 {{확보}}하게 됐다"},
  {"t": "질랜드파마·제너레이트, 최대 12억 달러 비만약 계약(블룸버그 인용)", "o": "로이터", "d": "2026-10-14",
   "u": "https://www.reuters.com/legal/litigation/zealand-pharma-generate-strike-obesity-drug-deal-worth-up-12-billion-bloomberg-2026-10-13/",
   "s": "{{질랜드}}가 {{선급금 3,000만 달러}}를 내고 {{제너레이트}}는 {{후보 선정까지 연구}}를 맡는 구조여서, {{임상·허가·전 세계 판매}}는 {{질랜드}}가 {{전담}}한다"}
 ]
})

# ---------------- C012 ----------------
ITEMS.append({
 "cid": "C012", "attachTo": "",
 "title": "{{바이오엔텍}} mRNA {{두경부암 치료제}}, 2/3상 {{첫 목표 실패}}…{{생존기간 평가}}는 계속",
 "one": "{{바이오엔텍}}의 mRNA 면역치료제 {{BNT113}}이 HPV16 양성 {{두경부암 2/3상}}에서 {{무진행생존기간}}을 {{유의하게 늘리지 못하}}면서, 시험은 {{전체생존기간 평가}}로 이어지지만 {{미국 상장 주식}}이 {{개장 전 6% 가까이 떨어지}}는 등 {{mRNA 암 백신의 잇단 차질}}이 {{부각됐}}다",
 "facts": [
  "무엇이: 바이오엔텍이 10월 13일 HPV16 양성 전이성 두경부암 2/3상 AHEAD-MERIT에서 BNT113과 펨브롤리주맙 병용이 펨브롤리주맙 단독보다 무진행생존기간(PFS)을 통계적으로 유의하게 늘리지 못했다고 밝혔다 [사실]",
  "다음 단계: 독립 데이터모니터링위원회 권고로 시험은 두 번째 1차 평가변수인 전체생존기간(OS)을 보기 위해 계속되고, OS가 유의하게 좋아지면 PFS 실패와 관계없이 성공으로 본다 [사실]",
  "시장: 미국 상장 주식이 개장 전 거래에서 6% 가까이 떨어졌다는 보도가 나왔다 [사실]",
  "평가: BMO캐피털마켓은 오토진 세부메란의 방광암·대장암 개발 중단에 이어 mRNA 암 백신 차질 목록에 이번 결과가 더해졌다고 봤다 [사실]"
 ],
 "basis": "verified",
 "check": "BNT113·AHEAD-MERIT의 PFS 미달, 독립 데이터모니터링위원회 권고로 OS 평가 계속, 개장 전 주가 약 6% 하락, BMO 평가는 검색 결과 요약(바이오엔텍 보도자료·바이오스페이스·인베스팅닷컴 자체 기사)으로 확인.",
 "src": [
  {"o": "바이오엔텍 보도자료(글로브뉴스와이어)", "d": "2026-10-13", "u": "https://www.globenewswire.com/news-release/2026/10/13/3379487/0/en/biontech-provides-update-on-phase-2-3-clinical-trial-for-mrna-cancer-immunotherapy-candidate-bnt113-in-metastatic-hpv16-positive-head-and-neck-cancer.html"},
  {"o": "바이오스페이스", "d": "2026-10", "u": "https://www.biospace.com/drug-development/biontech-faces-3rd-mrna-setback-as-head-and-neck-cancer-therapy-fails-to-improve-survival"},
  {"o": "인베스팅닷컴", "d": "2026-10", "u": "https://www.investing.com/news/company-news/biontech-cancer-drug-misses-key-trial-endpoint-93CH-4946149"}
 ],
 "inds": ["pharma"], "nodes": [],
 "added": "이번 로이터 1건으로 {{실패한 시험}}이 {{HPV16 양성 두경부암 2/3상}}이고 {{놓친 목표}}는 {{두 1차 평가변수 중 무진행생존기간}}이라는 점이 추가됐다",
 "items": [
  {"t": "바이오엔텍 '암 치료제, 초기 분석에서 효과 확인 못 해'", "o": "블룸버그", "d": "2026-10-13",
   "u": "https://www.bloomberg.com/news/articles/2026-10-13/biontech-says-cancer-treatment-didn-t-help-in-early-analysis",
   "s": "{{바이오엔텍}}이 mRNA 암 치료제 {{BNT113}}의 {{초기 분석}}에서 {{펨브롤리주맙 단독 대비 효과}}를 {{입증하지 못하}}면서 미국 상장 {{주가}}가 {{개장 전 6% 가까이 떨어졌}}다"},
  {"t": "바이오엔텍 mRNA 항암제, 두경부암 임상서 첫 목표 달성 실패", "o": "로이터", "d": "2026-10-14",
   "u": "https://www.reuters.com/legal/litigation/biontechs-mrna-cancer-therapy-misses-first-goal-head-neck-trial-2026-10-13/",
   "s": "{{BNT113}}이 HPV16 양성 {{두경부암 2/3상}}의 첫 1차 목표인 {{무진행생존기간}}을 {{놓쳤}}지만, {{독립위원회 권고}}로 {{전체생존기간 평가}}가 {{계속}}돼 {{최종 성패}}는 {{남아}} 있다"}
 ]
})

# ---------------- C016 ----------------
ITEMS.append({
 "cid": "C016", "attachTo": "n-tg-0214",
 "title": "{{구글}}, 기업 에이전트 이어 {{'제미나이 4 아르곤'}} 출시…{{바이브코딩 앱}} {{플레이스토어 허용}}",
 "one": "{{구글}}이 {{기업용 범용 에이전트}}에 이어 플래그십 모델 {{'제미나이 4 아르곤'}}을 {{개발자·기업}}에 내놓고, AI 스튜디오로 만든 {{바이브코딩 앱}}을 {{유료 개발자 계정 없이}} {{플레이스토어에 비공개로 올리게}} 하면서, {{AI로 만든 앱}}을 {{쓰는 문턱}}이 {{낮아지고}} 있다",
 "facts": [
  "무엇이: 구글이 10월 13일 플래그십 모델 '제미나이 4 아르곤'을 내놓고 Gemini API 유료 등급(Google AI Studio)과 안드로이드 스튜디오에서 개발자가 바로 쓸 수 있게 했다 [사실]",
  "용도: 구글은 아르곤을 실제 소프트웨어 개발, 기업 지식 업무, 사이버보안 방어의 복잡한 작업을 위한 최전선 모델로 소개했고, AI 울트라 구독자는 AI Studio와 에이전트 개발 플랫폼 '안티그래비티'에서 써 볼 수 있다 [사실]",
  "플레이스토어: AI 스튜디오로 만든 바이브코딩 안드로이드 앱을 등록비 25달러의 개발자 계정 없이 개인 라이브러리에 비공개로 올릴 수 있고, 검색·추천에는 뜨지 않으며 미국 등 일부 시장의 18세 이상부터 적용된다 [사실]",
  "가격: 출시 API 가격은 입력 100만 토큰당 2달러·출력 10달러이고 11월 30일 뒤 두 배가 된다고 전해졌다 [미확인]",
  "기존: 구글 클라우드는 10월 8일 제미나이와 앤스로픽 클로드를 작업별로 골라 쓰는 기업용 범용 에이전트 'Gemini Agent'를 공개했다 [사실]"
 ],
 "basis": "verified",
 "check": "제미나이 4 아르곤 출시일·제공처(Gemini API 유료 등급·AI Studio·안드로이드 스튜디오, AI 울트라 구독자용 안티그래비티)·용도는 구글 블로그 본문으로 확인. 플레이스토어 비공개 등록(개발자 계정·25달러 등록비 불요, 검색·추천 비노출, 미국 등 일부 시장 18세 이상)은 검색 결과 요약(안드로이드폴리스·데이터코노미·테크브리플리)으로 확인. API 가격은 로이터 전재본에서만 봐 미확인.",
 "src": [
  {"o": "구글 블로그", "d": "2026-10-13", "u": "https://blog.google/innovation-and-ai/technology/developers-tools/build-with-gemini-4-argon/"},
  {"o": "안드로이드폴리스", "d": "2026-10", "u": "https://www.androidpolice.com/your-vibe-coded-android-apps-home-on-google-play/"},
  {"o": "데이터코노미", "d": "2026-10-14", "u": "https://dataconomy.com/2026/10/14/google-play-private-vibe-coded-android-apps/"},
  {"o": "테크브리플리", "d": "2026-10-14", "u": "https://techbriefly.com/2026/10/14/google-play-private-vibe-coded-android-apps/"}
 ],
 "inds": ["macro", "tech"], "nodes": ["macro/semis"],
 "added": "이번 로이터·블룸버그 각 1건으로 {{구글}}의 {{플래그십 모델 '제미나이 4 아르곤'}} {{출시}}와 {{바이브코딩 앱}}의 {{플레이스토어 비공개 등록 허용}}이 추가됐다",
 "items": [
  {"t": "구글, 개발자·기업용 플래그십 AI 모델 '제미나이 4 아르곤' 출시", "o": "로이터", "d": "2026-10-14",
   "u": "https://www.reuters.com/business/google-launches-flagship-ai-model-gemini-4-argon-developers-businesses-2026-10-13/",
   "s": "{{구글}}이 플래그십 모델 {{'제미나이 4 아르곤'}}을 {{Gemini API}} 유료 등급과 {{안드로이드 스튜디오}}에 {{출시}}하면서 {{코딩·기업 지식 업무·보안}}의 복잡한 작업을 {{겨냥}}했다"},
  {"t": "구글, 바이브코딩 앱 누구나 플레이스토어에 비공개 등록 허용", "o": "블룸버그", "d": "2026-10-14",
   "u": "https://www.bloomberg.com/news/articles/2026-10-13/google-will-let-anyone-publish-privately-listed-vibe-coded-apps-on-play-store",
   "s": "{{구글}}이 {{바이브코딩 앱}}을 25달러 {{개발자 계정 없이}} {{플레이스토어}}에 {{비공개로 올리게}} 하면서 AI로 만든 {{개인용 앱}}의 {{배포 문턱}}이 {{낮아졌}}다"}
 ]
})

# ---------------- C020 ----------------
ITEMS.append({
 "cid": "C020", "attachTo": "",
 "title": "{{머크 황반부종 신약}} 2b/3상, {{비열등성 충족}}했지만 {{우월성 못 보이고}} {{중단}} 많아",
 "one": "{{머크}}의 황반부종 신약 {{레미그로미그}}가 2b/3상에서 {{라니비주맙 대비 시력 개선 비열등성}}은 {{충족}}했지만 {{우월성}}을 {{보이지 못하}}고 {{투약 중단}}도 {{더 많아}}, {{규제 당국 협의}}와 진행 중인 {{3상}} 결과가 {{허가 가능성}}을 {{가를}} 전망이다",
 "facts": [
  "무엇이: 머크가 10월 10일 미국안과학회(AAO 2026)에서 당뇨병성 황반부종 성인 984명을 대상으로 한 2b/3상 BRUNELLO의 1년 결과를 발표했다 [사실]",
  "약물: 레미그로미그(MK-3000)는 Wnt 경로를 활성화해 혈액-망막 장벽을 복구하는 4가·삼중특이 항체로, 눈 속(유리체강 내)에 주사한다 [사실]",
  "결과: 52주 최대교정시력이 0.5mg 9.1글자, 0.8mg 8.7글자 늘어 라니비주맙(11.8글자) 대비 비열등성을 충족했지만, 이차 평가변수에서는 우월성을 보이지 못했다 [사실]",
  "안전성: 이상반응에 따른 투약 중단은 4.9%·4.5%로 라니비주맙(0.9%)보다 많았고, 증식성 당뇨망막병증 관련 이상반응도 6.7%·6.1%(라니비주맙 0.9%)였다 [사실]",
  "다음 단계: 머크는 결과를 규제 당국과 논의할 예정이며, 당뇨병성 황반부종 3상 BAROLO가 진행 중이다 [사실]"
 ],
 "basis": "verified",
 "check": "약물(레미그로미그, MK-3000)·시험 규모(984명)·52주 시력 개선 수치·비열등성 충족·이차 평가변수 우월성 미달·투약 중단률·증식성 망막병증 이상반응·발표일(10월 10일 AAO)·후속 3상은 텔레그램 글이 연결한 머크 보도자료(스톡타이탄 게재) 본문으로 확인.",
 "src": [
  {"o": "머크 보도자료(스톡타이탄 게재)", "d": "2026-10-10", "u": "https://www.stocktitan.net/news/MRK/merck-presents-one-year-results-from-the-pivotal-phase-2b-3-brunello-binqe12p7z4h.html"}
 ],
 "inds": ["pharma"], "nodes": [],
 "items": [
  {"t": "머크, 황반부종 신약 2b/3상 브루넬로 1년 결과 발표…비열등성 충족", "o": "텔레그램 트릴리온", "d": "2026-10-13",
   "u": "https://t.me/Trillion_labs/10412"}
 ]
})

# ---------------- C022 ----------------
ITEMS.append({
 "cid": "C022", "attachTo": "",
 "title": "{{아스트라제네카}}, 골질환 신약 {{3상 실패}}는 '{{임상 설계 탓}}'…{{성인 시장 확대}} {{차질}}",
 "one": "{{아스트라제네카}}가 저포스파타제증 신약 {{에프짐포타제 알파}}의 {{3상 실패}}를 {{성인 하위군 불균형}}과 {{높은 위약 반응}} 등 {{임상 설계}} 탓으로 {{돌리}}면서, 기존 약 {{스트렌식}}이 쓰이는 {{소아}}를 넘어 {{성인으로 시장을 넓히려던 계획}}에 {{차질}}이 {{생겼}}다",
 "facts": [
  "무엇이: 아스트라제네카가 저포스파타제증(HPP) 치료제 후보 에프짐포타제 알파의 3상 HICKORY 실패 원인으로 성인 하위군 불균형과 예상보다 좋았던 위약군 결과 등 임상 설계를 지목했다 [사실]",
  "수치: 6분 걷기 거리의 위약 대비 차이는 17.05m(p=0.1675)로 유의하지 않았고, 사후 분석에서 최소 임상 의미 개선에 이른 비율은 투약군 45.2%, 위약군 30% 이상이었다 [사실]",
  "소아: 스트렌식을 쓴 적 없는 소아 대상 3상 MULBERRY에서는 25주차 뼈 건강 개선이 위약 대비 통계적으로 유의했다 [사실]",
  "의미: 미 식품의약국(FDA)이 이 약을 심사하는 가운데, 성인 실패로 기존 약 스트렌식이 쓰이는 소아를 넘어선 시장 확대 계획에 의문이 생겼다는 평가가 나왔다 [사실]"
 ],
 "basis": "verified",
 "check": "HICKORY 실패와 회사 설명(성인 하위군 불균형·높은 위약 반응), 6분 걷기 차이 17.05m(p=0.1675)·사후 분석 비율, MULBERRY 성공, FDA 심사 중, 시장 확대 차질 평가는 검색 결과 요약(엔드포인츠·클리니컬트라이얼스아레나·피어스바이오텍·메드패스)으로 확인. HICKORY 실패를 처음 공개한 날짜는 확인 못 함.",
 "src": [
  {"o": "엔드포인츠뉴스", "d": "2026-10", "u": "https://endpoints.news/astrazeneca-blames-trial-design-for-phase-3-failure-of-bone-disease-drug/"},
  {"o": "클리니컬트라이얼스아레나", "d": "2026", "u": "https://www.clinicaltrialsarena.com/news/astrazeneca-efzimfotase-alfa-hypophosphatase-phase-iii-hickory/"},
  {"o": "피어스바이오텍", "d": "2026", "u": "https://www.fiercebiotech.com/biotech/astrazenecas-phase-3-rare-disease-trial-misses-goal-denting-market-expansion-plan"}
 ],
 "inds": ["pharma"], "nodes": [],
 "items": [
  {"t": "아스트라제네카, 골질환 신약 3상 실패를 임상 설계 탓으로 돌려", "o": "텔레그램 트릴리온", "d": "2026-10-13",
   "u": "https://t.me/Trillion_labs/10416"}
 ]
})

# ---------------- C026 ----------------
ITEMS.append({
 "cid": "C026", "attachTo": "n-rtr-0111",
 "title": "{{아시아}}, {{코코아 수요 회복}} 주도…{{가나}}는 수매 자금 {{2억 8,800만 달러}} {{조달}}",
 "one": "{{가나 코코아위원회}}가 단기 국내 채권으로 {{33억 9,000만 세디}}를 {{조달}}해 {{막혔던 농가 수매 대금}}을 풀 길을 연 가운데, {{불확실한 시장}}에서도 {{아시아}}가 {{코코아 수요 회복}}을 {{주도}}하는 자리를 {{굳히}}면서 {{수요 회복의 무게중심}}이 {{아시아}}로 옮겨 가고 있다 (제목 기준)",
 "facts": [
  "무엇이: 불확실한 시장 속에서 아시아가 코코아 수요 회복을 주도하는 자리를 굳혔다 [제목]",
  "전망: 블룸버그가 9명에게 물은 결과 3분기 아시아 분쇄량은 약 20만 8,412톤으로 1년 전보다 약 15% 늘어 2011년 이후 3분기 최대 증가가 예상됐고, 유럽은 약 3.9% 감소, 북미는 보합이 예상됐다 [미확인]",
  "가나: 가나 코코아위원회가 10월 5일 금리 11%의 단기 국내 채권으로 33억 9,000만 세디(약 2억 8,800만 달러)를 조달했다 [사실]",
  "가나 배경: 163억 세디 국내 조달 계획의 첫 회차로, 9월 25일 시즌이 열렸지만 수매업체들이 자기 돈으로 사들이길 거부해 수매가 지연됐다 [사실]"
 ],
 "basis": "title",
 "check": "블룸버그 설문(아시아 3분기 분쇄 약 20만 8,412톤·약 15% 증가, 유럽 약 3.9% 감소)은 블룸버그 기사 전재본(비즈니스미러)과 이를 옮긴 요약(briefs.co)으로만 검색돼 독립 출처로 확인 못 함. 분쇄 통계 페이지(코코아인텔)는 유료라 수치가 없었고 XTB 분석은 열리지 않음(403). 가나 수매 자금 내용은 기존 문서 근거.",
 "src": [],
 "inds": ["agri"], "nodes": [],
 "added": "이번 블룸버그 1건으로 {{불확실한 시장}}에서도 {{아시아}}가 {{코코아 수요 회복}}을 {{주도}}하는 {{자리를 굳혔다}}는 {{수요 쪽 흐름}}이 추가됐다 (제목 기준)",
 "items": [
  {"t": "불확실한 시장 속 아시아, 코코아 수요 회복 주도권 굳혀", "o": "블룸버그", "d": "2026-10-13",
   "u": "https://www.bloomberg.com/news/articles/2026-10-13/asia-cements-lead-in-cocoa-demand-revival-in-uncertain-market",
   "s": "{{아시아}}가 {{불확실한 시장}} 속에서도 {{코코아 수요 회복}}을 {{주도}}하는 자리를 {{굳히}}면서 {{세계 코코아 수요}}의 {{무게중심}}이 {{아시아}}로 옮겨 가고 있다 (제목 기준)"}
 ]
})

# ---------------- C030 ----------------
ITEMS.append({
 "cid": "C030", "attachTo": "",
 "title": "{{멜로즈}} GKN {{가든그로브 공장}}, {{4분기}} 단계적 {{재가동}}…{{1억 2,500만 달러}} 민사 합의",
 "one": "{{멜로즈}}가 {{화학물질 사고}}로 멈춘 GKN에어로스페이스 {{가든그로브 공장}}을 {{당국 승인}}을 전제로 {{4분기 단계적 재가동}}하겠다고 밝히고 {{1억 2,500만 달러 민사 합의안}}이 {{법원에 제출}}되면서, {{공장 정상화}}와 {{주민 보상}}의 길이 {{열리고}} 있다",
 "facts": [
  "무엇이: 멜로즈가 10월 13일 자회사 GKN에어로스페이스의 미국 가든그로브 공장이 당국 승인을 전제로 4분기 중 단계적으로 전면 가동에 복귀할 것으로 본다고 밝혔다 [사실]",
  "합의: 오렌지카운티 지방검찰청이 10월 12일 민사 조사를 끝내는 합의 문서를 법원에 냈고, 민사 제재금 1,500만 달러, 소방 등 당국 청구 1,000만 달러, 주민·사업자 보상 프로그램 최대 1억 달러로 구성되며 법원 승인이 남았다 [사실]",
  "일정 변화: GKN은 8월에는 9월 28일 전면 재가동을 목표로 했었다 [사실]",
  "남은 과제: 별도 집단소송은 조정 협의 중이고, 멜로즈는 보험 처리 여부를 검토하고 있다 [사실]"
 ],
 "basis": "verified",
 "check": "4분기 단계적 전면 가동 복귀(당국 승인 전제), 10월 12일 오렌지카운티 지검 합의 문서 제출, 제재금 1,500만·당국 청구 1,000만·보상 프로그램 최대 1억 달러, 8월 목표(9월 28일), 집단소송 조정·보험 검토는 검색 결과 요약(셰어캐스트·칼킨미디어·팁랭크스)으로 확인. 공장 2025년 매출은 출처마다 통화 단위가 달라 쓰지 않음.",
 "src": [
  {"o": "셰어캐스트", "d": "2026-10-13", "u": "https://www.sharecast.com/news/news-and-announcements/ftse-ftse-100-melrose-industries-gkn-aerospace-garden-grove--23835654.html"},
  {"o": "칼킨미디어", "d": "2026-10-13", "u": "https://kalkinemedia.com/uk/news/announcements/melrose-industries-mro-provides-update-on-gkn-aerospace-garden-grove-civil-settlement-and-plans-for-gradual-operational-resumption"},
  {"o": "팁랭크스", "d": "2026-10-13", "u": "https://www.tipranks.com/news/company-announcements/melrose-moves-toward-civil-settlement-and-restart-at-gkns-garden-grove-plant"}
 ],
 "inds": ["aero"], "nodes": [],
 "items": [
  {"t": "멜로즈 '가든그로브 공장, 4분기까지 가동 재개 순항'", "o": "로이터", "d": "2026-10-13",
   "u": "https://www.reuters.com/legal/litigation/melrose-says-garden-grove-plant-track-resume-operations-by-fourth-quarter-2026-10-13/"}
 ]
})

# ---- MORE ----

if __name__ == '__main__':
    validate(ITEMS)
    if '--write' in sys.argv:
        out = {"agent": "W1", "searches_used": 16, "fetches_used": 4, "items": ITEMS, "skipped": SKIPPED}
        with open(OUT, 'w', encoding='utf-8') as f:
            json.dump(out, f, ensure_ascii=False, indent=1)
        print('written', OUT, len(ITEMS))
