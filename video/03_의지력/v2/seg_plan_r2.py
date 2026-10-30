# 03편 v2 장면 계획 = v1(seg_plan.py) + 사용자 수정 요청(2026-10-30):
# "좋아한다는 마음이 있어도 ~ 없어지지는 않기 때문입니다"(65번 문장)에 뒷배경 넣기 -> 검은 화면에서 떼어 스톡 st94로.
# 앞 질문(64번 문장)은 검은 화면 그대로.
from seg_plan import SEG as SEG_V1, K_SENTS as K_V1
NEW = ((65, 0), 'S', 'st94', '자전거를 들고 계단을 오르는 사람(좋아하는 일에도 따르는 수고, 가운데 자막 뒤라 흐리게)', 'bike stairs', '')
SEG = []
for s in SEG_V1:
    SEG.append(s)
    if s[0] == (64, 0):
        SEG.append(NEW)
assert NEW in SEG
K_SENTS = K_V1 - {65}
