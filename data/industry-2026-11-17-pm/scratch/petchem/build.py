import json
B='/home/user/news-desk'
p=json.load(open(f'{B}/work/nightly-2026-11-17/chains/petchem.json'))
ids=[json.loads(l)['id'] for l in open(f'{B}/data/industry-2026-11-17-pm/news/petchem.jsonl')]
def S(d,o,u,nid,t): return dict(d=d,o=o,u=u,nid=nid,t=t)
BR='https://www.bloomberg.com/news/articles/2026-11-16/braskem-creditors-shun-company-s-latest-offer-discuss-new-plan'
BI='https://t.me/kyobofnbcosmetic/2618'
state={
 'cracker':[S('2026-11-16','블룸버그',BR,'n-bbg-0087','브라스켐 채권단은 약 109억 달러 채무 조정에서 회사의 최신안도 거부하고 새 계획을 논의하고 있으며, 채권단 과반 동의 시한은 11월 22일입니다 [제목]')],
 'specialty':[S('2026-10-21','텔레그램 교보 음식료/화장품 권우정',BI,'n-tg-0863','HDC현대EP·CJ제일제당의 생분해 플라스틱 합작사 비오솔이 수요 부진과 일회용품 규제 후퇴로 4년 만에 해산을 추진하며, 진천에 약 240억 원을 들인 연 1만 1,000톤 라인의 처리 방안은 공개되지 않았습니다 [사실]')],
}
IS=[
 dict(d='2026-11-16',kind='supply',o='블룸버그',u=BR,nid='n-bbg-0087',t='브라스켐이 법정 밖 회생으로 조정하려는 무담보 금융채무는 564억 8,000만 헤알(약 109억 달러)이고, 채권단은 대주주에 30억 달러 자본 투입을 요구해 왔으며 과반 동의 시한은 11월 22일입니다 [사실]'),
 dict(d='2026-11-17',kind='supply',o='텔레그램 교보 음식료/화장품 권우정',u=BI,nid='n-tg-0863',t='비오솔은 지난해 매출 43억 원·순손실 31억 원, 올해 3분기 누적 매출 26억 원·순손실 22억 원을 냈고 해산을 추진합니다 [사실]'),
]
gaps=p['gaps']+' 11월 17일 저녁 업데이트도 검색·열람 없이 입력 뉴스 2건으로만 반영했습니다. 브라스켐 채권단이 거부한 최신안의 내용과 새 계획은 기사 제목뿐이라 확인하지 못했고, 11월 22일 시한을 넘길 때 법정 회생으로 갈지와 설비 가동 영향도 아직 모릅니다. 비오솔의 임시주총 일정과 진천 설비 처리 방안은 공개되지 않았습니다.'
out=dict(id='petchem',summary='',state=state,industryState=IS,flags=[],insight={},cycle=None,nodeStage={},gaps=gaps,
 note='뉴스 2건 반영: 브라스켐 채권단 최신 채무조정안 거부(109억 달러, 11월 22일 시한), HDC현대EP·CJ제일제당 생분해 합작사 비오솔 해산 추진. 국면 ⑥ 그대로, 근거 2줄, 수치 2줄, 재검토 신호 0건, 검색 0회',
 applied=ids,searches=0,fetches=0)
json.dump(out,open(f'{B}/data/industry-2026-11-17-pm/out/petchem.json','w'),ensure_ascii=False,indent=1)
