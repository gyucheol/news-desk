# 03편과 04편 사용자 표시 대본에서 AI 사진이 덮는 글자 비율을 구간별로 센다.
# 04편: 숫자가 문장 뒤나 문장 사이에 붙음. 문단 처음(또는 앞 숫자 다음)부터 그 숫자까지가 그 사진 구간.
# 03편: "<자막>숫자" 형식. 꺾쇠 안이 사진 구간. "<< >>"는 카드라 사진에서 뺌.
import os, re
V = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..')
def nc(t): return len(re.sub(r'[\s/\*]', '', t))

u4 = open(os.path.join(V, '좋아하는것', 'v1', 'user_script_marked.txt'), encoding='utf-8').read().split('[대본]', 1)[1]
tok = re.compile(r'(?<=[가-힣\.\?\!”,])\s?(\d{1,2})(?=\s|$)')
rows4 = []; nums = []
for p in [p.strip() for p in u4.split('\n') if p.strip()]:
    last = 0; c = 0
    for m in tok.finditer(p):
        c += nc(p[last:m.start()]); last = m.end(); nums.append(int(m.group(1)))
    rows4.append((c, nc(tok.sub('', p)), p))
c = sum(r[0] for r in rows4); t = sum(r[1] for r in rows4)
print(f'04편: 사진 {len(set(nums))}장, 표시 {len(nums)}곳, 사진이 덮는 글자 {c}/{t} = {c / t * 100:.0f}%')

u3 = open(os.path.join(V, '03_의지력', 'v1', 'user_script_marked.txt'), encoding='utf-8').read().split('* 대본', 1)[1]
u3 = u3.replace('<<', '').replace('>>', '')
rows3 = []
for p in [p.strip() for p in u3.split('\n') if p.strip()]:
    rows3.append((sum(nc(x) for x in re.findall(r'<([^<>]*)>', p)), nc(re.sub(r'[<>]|\d', '', p)), p.lstrip('* ')))
inside = re.findall(r'<([^<>]*)>', u3, flags=re.S)
c3 = sum(nc(x) for x in inside)
body = re.sub(r'(?<=[가-힣\.\?\!”,\s])\s?\d{1,2}(?=\s|$|\.)', '', re.sub(r'[<>]', '', u3))
print(f'03편: 표시 {len(inside)}곳, 사진이 덮는 글자 {c3}/{nc(body)} = {c3 / nc(body) * 100:.0f}%')

def report(name, rows, bounds):
    idx = [next(i for i, r in enumerate(rows) if k in r[2]) for _, k in bounds] + [len(rows)]
    for j, (lab, _) in enumerate(bounds):
        c = sum(r[0] for r in rows[idx[j]:idx[j + 1]]); t = sum(r[1] for r in rows[idx[j]:idx[j + 1]])
        print(f'  {name} {lab}: {c}/{t} = {c / t * 100:.0f}%')
report('04편', rows4, [('도입', '당신은 오늘 소개팅'), ('공감 장면', '주말 오후입니다'), ('블랙홀 실험', '여러분이 새로운 관심사'),
    ('적용', '이 관점을 앞서'), ('원인 2와 상 실험 설정', '그렇다고 관심이 생긴'), ('상 실험 결과와 해석', '상을 받은 아이들이'),
    ('호출기 실험 설정', '지금 여러분이 작은 호출기'), ('호출기 결과부터', '결과는 조금 의외'), ('해결책 1', '첫째.'),
    ('해결책 2', '둘째.'), ('해결책 3', '셋째.'), ('마무리', '즉, 취미가')])
report('03편', rows3, [('도입', '<당신은 오늘 퇴근하고'), ('공감 장면', '<수요일 저녁'), ('실험 1', '그렇다면 하루 동안'),
    ('설명', '한마디로 머리를'), ('해결책 1', '첫째.'), ('해결책 2', '둘째.'), ('해결책 3', '셋째.'), ('마무리', '내 생활을 갖는다는')])
