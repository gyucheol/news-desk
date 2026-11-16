# 살걸·팔걸 대본(사용자 최종본)에 AI 사진 번호 넣기. 대본 글자는 그대로 두고, 정한 자리(앞 글귀 바로 뒤)에만 번호를 넣는다.
# 번호는 처음 나오는 순서대로 1부터. 같은 장면은 같은 번호(사용자 03·04편 표시 방식, 수면 편과 같은 도구).
# 이 대본은 한 줄이 한 문단이므로, 줄 처음(또는 앞 번호 다음)부터 번호까지가 그 사진 구간이다.
import json, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
src = open(os.path.join(HERE, '..', '대본_최종_사용자.txt'), encoding='utf-8').read()

# (이 글귀 바로 뒤에, 장면 이름) - 대본 앞에서부터 차례로 찾는다
INS = [
 ("주식 앱을 엽니다.", "lunch_app"),
 ("30% 넘게 벌었을 겁니다.", "chart_up"),
 ("그때 살걸.”", "regret_buy"),
 ("연달아 올라옵니다.", "chat_profit"),
 ("폭등했다고 나옵니다.", "news_surge"),
 ("매수 버튼을 누릅니다.", "subway_buy"),
 ("5% 떨어져 있습니다.", "morning_drop"),
 ("일주일 내내 내려갑니다.", "week_down"),
 ("팔기로 합니다.", "sell_btn"),
 ("다시 오르기 시작합니다.", "rebound"),
 ("처음부터 사지 말걸.”", "head_hold"),
 ("맞지 않는 사람일까요?", "self_doubt"),
 ("거래한 기록을 살펴봤습니다.", "odean_records"),
 ("낮은 수익을 냈습니다.", "two_lines"),
 ("다시 떠올려 보겠습니다.", "subway_buy"),
 ("하필 그날 샀습니다.", "chart_up"),
 ("수익 인증이 올라오고", "chat_profit"),
 ("회사 이름이 나온 날이었죠.", "news_surge"),
 ("가구의 거래 기록을 분석했습니다.", "odean_records"),
 ("크게 움직인 날이었죠.", "attention_days"),
 ("누가 파는지 살펴봤습니다.", "buy_sell_piles"),
 ("두 배 가까이 많이 샀습니다.", "twice_bars"),
 ("종목도 마찬가지였습니다.", "buy_the_drop"),
 ("가능성이 크다는 점입니다.", "same_news"),
 ("습관처럼 주식 앱을 엽니다.", "night_app"),
 ("관심 목록에 그대로 있습니다.", "watchlist"),
 ("들여다본 종목입니다.", "peek"),
 ("속이 쓰립니다.", "sting"),
 ("모의 주식 거래를 하게 했습니다.", "fmri"),
 ("규칙을 미리 들었습니다.", "rule_brief"),
 ("다시 사는 편이 유리했습니다.", "screen_rise"),
 ("알고 있었는데도요.", "hesitate"),
 ("화면을 보는 순간,", "screen_rise"),
 ("활발해지는 부위였습니다.", "brain_signal"),
 ("다시 사기를 더 꺼렸습니다.", "hesitate"),
 ("두 사람이 있습니다.", "two_people"),
 ("고민했지만 그대로 뒀습니다.", "you_hold_a"),
 ("벌었을 겁니다.", "you_miss_b"),
 ("A 회사 주식으로 바꿨습니다.", "sc_switch"),
 ("벌었을 겁니다.", "sc_regret"),
 ("상철이라고 답했습니다.", "vote92"),
 ("두 학생의 이야기를 들려줬습니다.", "lecture_story"),
 ("케빈이 있습니다.", "two_students"),
 ("답한 람이 76%였습니다.", "kevin_regret"),
 ("답한 사람이 64%였습니다.", "dave_later"),
 ("당장 쓰리고,", "sting"),
 ("마음에 남는 셈입니다.", "regret_buy"),
 ("한 줄로 적어 두세요.", "memo_before"),
 ("채점하기 쉽습니다.", "grading"),
 ("잘한 결정 같고", "grading"),
 ("어리석은 결정 같습니다.", "self_doubt"),
 ("미리 남겨 두는 겁니다.", "memo_before"),
 ("보고 산다.”", "memo_close"),
 ("틀렸다고 본다.”", "memo_close"),
 ("다시 꺼내 보세요.", "memo_reread"),
 ("자주 들여다보지 마세요.", "phone_down"),
 ("후회할 수도 있습니다.", "peek"),
 ("정해 두는 겁니다.", "remove_watch"),
 ("주말 아침에만 확인하는 식입니다.", "weekend_check"),
 ("판단할까?라고요.", "fresh_look"),
 ("오답노트를 작성하세요", "wrong_note"),
 ("판단할 수 있었어.”", "wrong_note"),
 ("같애\"", "look_back"),
 ("이유부터 적어 보자.”", "memo_before"),
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

# 확인: 표시 대본에서 넣은 번호 자리를 다시 지우면 원문(글자 하나 차이도 없음)
r = marked; offset = 0
for n, key, end in marks:
    s = end + offset
    assert r[s:s+len(str(n))] == str(n)
    offset += len(str(n))
r2 = marked
for n, key, end in reversed(marks):
    pass
chk = []; p = 0; q = 0
for n, key, end in marks:
    chk.append(src[p:end]); p = end
chk.append(src[p:])
rebuilt = ''; p = 0; off = 0
for n, key, end in marks:
    s = end + off
    rebuilt += marked[p:s]; p = s + len(str(n)); off += len(str(n))
rebuilt += marked[p:]
assert rebuilt == src, '원문과 다름'
open(os.path.join(HERE, 'marked.txt'), 'w', encoding='utf-8').write(marked)
json.dump({'num': num, 'marks': [(n, k, e) for n, k, e in marks]}, open(os.path.join(HERE, 'marks.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

# 통계: 사진이 덮는 글자(줄 처음 또는 앞 번호부터 번호까지)
def nc(t): return len(re.sub(r'\s', '', t))
paras = []; start = 0
for m in re.finditer(r'\n|\Z', src):
    if src[start:m.start()].strip():
        paras.append((start, m.start()))
    start = m.end()
rows = []
for a, b in paras:
    last = a; c = 0
    for n, k, e in marks:
        if a < e <= b:
            c += nc(src[last:e]); last = e
    rows.append((c, nc(src[a:b]), src[a:b]))
cov = sum(r[0] for r in rows); tot = sum(r[1] for r in rows)
print('사진', len(num), '장 / 표시', len(marks), '곳 / 다시 씀', len(marks) - len(num), '곳')
print('사진이 덮는 글자', cov, '/', tot, f'{cov/tot*100:.0f}%')
from collections import Counter
c = Counter(k for _, k, _ in marks)
print('여러 번 쓰는 사진:', ', '.join(f'{num[k]}({k})x{v}' for k, v in c.items() if v > 1))
bounds = [('도입', '당신은 오늘 점심을'), ('원인 1: 오딘 1999', '먼저 조금 뜻밖의'), ('원인 1: 바버와 오딘 2008', '그렇다면 우리는 언제'),
          ('원인 2: 장면', '그렇다면 내가 팔면'), ('원인 2: 프리드먼과 캐머러', '* 016년'), ('원인 3: 카너먼과 트버스키', '그런데 같은 후회라도'),
          ('원인 3: 길로비치와 메드벡', '또 다른 실험 하나를'), ('해결책 1', '그렇다면 살걸 팔걸 하는'), ('해결책 2', '둘째.'),
          ('해결책 3', '하지만 이미 지나간'), ('마무리', '이렇게 후회를 다음에')]
idx = [next(i for i, r in enumerate(rows) if r[2].startswith(k)) for _, k in bounds] + [len(rows)]
for j, (lab, _) in enumerate(bounds):
    cc = sum(r[0] for r in rows[idx[j]:idx[j + 1]]); tt = sum(r[1] for r in rows[idx[j]:idx[j + 1]])
    print(f'{lab}: {cc}/{tt} = {cc / tt * 100:.0f}%')
