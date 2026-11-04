# 수면 대본에 AI 사진 번호 넣기. 대본 글자는 그대로 두고, 정한 자리(앞 글귀 바로 뒤)에만 번호를 넣는다.
# 번호는 처음 나오는 순서대로 1부터. 같은 장면은 같은 번호(사용자 04편 표시 방식).
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', '대본_원본.txt'), encoding='utf-8').read()

# (이 글귀 바로 뒤에, 장면 이름) - 대본 앞에서부터 차례로 찾는다
INS = [
 ("일어나야 합니다.", "alarm7"),
 ("새벽 한 시입니다.", "phone1am"),
 ("괜찮다고 생각합니다.", "lieceiling"),
 ("일어나기 힘들어도", "hardwake"),
 ("씻고 출근해서", "commute"),
 ("일할 만해집니다.", "coffee"),
 ("머리가 멍하지만", "blank"),
 ("알람 없이 잠들었는데", "satsleep"),
 ("낮 열두 시입니다.", "noon"),
 ("벌써 오후입니다.", "lunch"),
 ("이제 괜찮겠지.”", "content"),
 ("다시 일어나기가 힘듭니다.", "hardwake"),
 ("괜찮은 사람일까요?", "lieceiling"),
 ("피곤함은 반복될까요?", "satsleep"),
 ("이메일을 읽고 있습니다.", "email"),
 ("몇 번이나 읽고,", "reread"),
 ("앞의 화면으로 돌아갑니다.", "backscreen"),
 ("졸리지는 않습니다.", "blank"),
 ("세 집단으로 나누고", "vd_groups"),
 ("여덟 시간으로 정했습니다.", "vd_468"),
 ("반복해서 받았습니다.", "vd_tests"),
 ("검사 등이었습니다.", "vd_pvt"),
 ("졸림도 기록했습니다.", "vd_sleepy"),
 ("검사 결과와 비교했습니다.", "vd_allnight"),
 ("경우가 늘었습니다.", "vd_miss"),
 ("수준까지 떨어졌습니다.", "vd_same"),
 ("그만큼 심해지지 않았습니다.", "vd_sleepy"),
 ("집중할 수 있다는 뜻일까요?", "focused"),
 ("버틸 수 있다는 뜻일까요?", "coffee"),
 ("상태였을 수 있습니다.", "yesterday"),
 ("주말에 많이 자잖아.”", "satsleep"),
 ("세 집단으로 나눴습니다.", "dp_groups"),
 ("수면 기회를 줬고,", "dp_9h"),
 ("다섯 시간만 줬습니다.", "dp_5h"),
 ("자도록 한 뒤,", "dp_5h"),
 ("잠을 보충하게 했습니다.", "dp_weekend"),
 ("짧게 자도록 했고요.", "dp_5h"),
 ("달라지는지 확인했습니다.", "dp_measure"),
 ("먹는 양이 줄었습니다.", "dp_lesssnack"),
 ("먹는 양이 늘었고,", "dp_moresnack"),
 ("주말에 푹 자면 되니까.”", "phone1am"),
 ("일주일 정도 기록해 보세요.", "diary"),
 ("시각을 적어 보는 겁니다.", "diary_write"),
 ("확인하는 겁니다.", "phone1am"),
 ("패턴이 더 잘 보일 수 있습니다.", "diary_pattern"),
 ("시작할 시간을 정하고,", "prep_time"),
 ("즐길 시간도 남겨 두세요.", "enjoy"),
 ("언제 가져요?”", "mytime"),
 ("퇴근하고 밥을 먹고", "dinner"),
 ("벌써 밤입니다.", "chores"),
 ("자려고 하니 아쉽습니다.", "mytime"),
 ("드라마 한 편을 봅니다.", "enjoy"),
 ("하루를 마무리합니다.", "wash"),
 ("쉬어도 좋습니다.", "music"),
 ("다시 늦어집니다.", "latewash"),
 ("함께 앞당겨 보세요.", "wash"),
 ("크게 달라지지 않도록 해 보세요.", "weekend_wake"),
 ("열두 시에 일어난 뒤,", "noon"),
 ("장면을 떠올려 보세요.", "sun11pm"),
 ("바로 오지 않을 수 있습니다.", "cantsleep"),
 ("자연광을 쬐고,", "sunlight"),
 ("잠들 준비를 해 보세요.", "dimlight"),
 ("낮 열두 시입니다.", "noon"),
 ("한 편 더 볼 수 있습니다.", "onemore"),
]

num = {}
out = []
pos = 0
marks = []  # (번호, 장면, 끝 위치 in src)
for anchor, key in INS:
    i = src.find(anchor, pos)
    if i < 0:
        sys.exit(f'글귀를 못 찾음: {anchor}')
    end = i + len(anchor)
    # 같은 문단 안에서 다음 글자가 번호를 붙여도 되는 자리인지(문장 끝, 쉼표, 띄어쓰기 앞)
    nxt = src[end:end+1]
    if nxt not in ('', ' ', '\n'):
        sys.exit(f'번호 뒤에 바로 글자가 붙음: {anchor!r} 다음 {nxt!r}')
    if key not in num:
        num[key] = len(num) + 1
    out.append(src[pos:end]); out.append(str(num[key]))
    marks.append((num[key], key, end))
    pos = end
out.append(src[pos:])
marked = ''.join(out)

# 확인 1: 넣은 번호만 빼면 원문과 같다
chk = []; p = 0
for n, key, end in marks:
    chk.append(src[p:end]); p = end
chk.append(src[p:])
assert ''.join(chk) == src
# 확인 2: 표시 대본에서 넣은 번호 자리를 다시 지우면 원문(글자 하나 차이도 없음)
r = marked
offset = 0
for n, key, end in marks:
    s = end + offset
    assert r[s:s+len(str(n))] == str(n)
    r = r[:s] + r[s+len(str(n)):]
assert r == src, '원문과 다름'
open(os.path.join(HERE, 'marked.txt'), 'w', encoding='utf-8').write(marked)
json.dump({'num': num, 'marks': [(n, k, e) for n, k, e in marks]}, open(os.path.join(HERE, 'marks.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 통계: 사진이 덮는 글자(문단 처음 또는 앞 번호부터 번호까지)
def nc(t): return len(re.sub(r'\s', '', t))
paras = []
start = 0
for m in re.finditer(r'\n\s*\n|\Z', src):
    paras.append((start, m.start())); start = m.end()
cov = 0
for a, b in paras:
    last = a
    for n, k, e in marks:
        if a < e <= b:
            cov += nc(src[last:e]); last = e
print('사진', len(num), '장 / 표시', len(marks), '곳 / 다시 씀', len(marks) - len(num), '곳')
print('사진이 덮는 글자', cov, '/', nc(src), f'{cov/nc(src)*100:.0f}%')
from collections import Counter
c = Counter(k for _, k, _ in marks)
print('여러 번 쓰는 사진:', ', '.join(f'{num[k]}({k})x{v}' for k, v in c.items() if v > 1))

# 구간별(구간 첫 문단의 첫 글귀로 나눔)
rows = []
for a, b in paras:
    last = a; c = 0
    for n, k, e in marks:
        if a < e <= b:
            c += nc(src[last:e]); last = e
    rows.append((c, nc(src[a:b]), src[a:b]))
bounds = [('도입', '당신은 내일도'), ('공감 장면', '평일 오후'), ('반 동겐 실험', '2003년'), ('해석 1', '이 결과를 생각하면'),
          ('데프너 실험', '그러면 이렇게 생각할'), ('해석 2', '이 연구에서는'), ('해결책 1', '첫째.'), ('해결책 2', '둘째.'),
          ('해결책 3', '셋째.'), ('마무리', '이제 처음의 토요일')]
idx = [next(i for i, r in enumerate(rows) if r[2].startswith(k)) for _, k in bounds] + [len(rows)]
for j, (lab, _) in enumerate(bounds):
    c = sum(r[0] for r in rows[idx[j]:idx[j + 1]]); tt = sum(r[1] for r in rows[idx[j]:idx[j + 1]])
    print(f'{lab}: {c}/{tt} = {c / tt * 100:.0f}%')
