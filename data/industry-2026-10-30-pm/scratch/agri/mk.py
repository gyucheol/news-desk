import json
P='/home/user/news-desk/'
old=json.load(open(P+'work/nightly-2026-10-30/chains/agri.json'))
W='https://www.bloomberg.com/news/articles/2026-10-29/china-makes-first-inquiry-for-us-wheat-since-trump-xi-summit'
B='https://www.bloomberg.com/news/articles/2026-10-30/bayer-wins-st-louis-roundup-trial-bolstering-settlement-push'
out={"id":"agri","summary":"",
"state":{
 "demand":[
  {"d":"2026-10-29","o":"블룸버그","u":W,"nid":"n-bbg-0794","t":"중국이 트럼프-시진핑 정상회담 이후 처음 미국산 밀 구매를 문의했지만 물량·밀 종류·구매 주체는 공개되지 않았고, 2026~27년산 옥수수·밀 대중 판매는 0이었습니다 [사실]"}],
 "inputs":[
  {"d":"2026-10-29","o":"블룸버그","u":B,"nid":"n-bbg-0846","t":"몬산토가 6월 연방대법원 판결 뒤 첫 라운드업 재판인 세인트루이스 소송에서 이겼고, 72억 5,000만 달러 집단 합의안은 미주리주 법원의 최종 승인 결정을 기다립니다 [사실]"}]},
"industryState":[
  {"d":"2026-10-29","kind":"demand","o":"블룸버그","u":W,"nid":"n-bbg-0794","t":"미 농무부 자료상 2026~27년산 옥수수·밀의 대중 판매는 0이었고, 중국은 정상회담 뒤 처음 미국산 밀 구매를 문의했습니다 [사실]"}],
"flags":[],"insight":{},"cycle":None,"nodeStage":{},
"gaps":old['gaps']+" (11) 10월 30일 저녁 업데이트도 검색·열람 없이 입력 뉴스 3건으로만 반영했습니다. 중국의 미국산 밀 구매 문의가 실제 계약으로 이어졌는지(미 수출 판매 통계·플래시 판매)와 물량, 미국 농업 기업 비용 급등의 내용(기사 제목만 봄), 로벤사 대주단의 대출채권 매각 규모와 회사 사업 내용은 확인하지 못해 로벤사는 근거로 쓰지 않았습니다.",
"note":"뉴스 3건 반영: 중국의 회담 뒤 첫 미국산 밀 구매 문의, 라운드업 재판 바이엘 승소. 국면 ④(분할) 그대로, 근거 2줄, 수치 1줄, 재검토 신호 0건, 검색 0회",
"applied":["n-bbg-0794","n-bbg-0810","n-bbg-0846"],"searches":0,"fetches":0}
json.dump(out,open(P+'data/industry-2026-10-30-pm/out/agri.json','w'),ensure_ascii=False,indent=1)
