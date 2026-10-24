# 01편 장면 명세 (2026-10-24): lines.json + the material plan below -> spec.json (paths relative to VIDEO_ROOT) and
# work/spec_abs.json (absolute paths, for build_timeline.py).
# Materials, in the owner's order of preference (HANDOFF_FEEDBACK.md 5-1 6): stock that shows the line as it is
# (Mixkit, Free license checked on each item page), then AI photos (RealVisXL, work/img, ai_images.json) where no Free
# stock fits, and icon screens / black cards for diagrams, inner thoughts and questions. No abstract stock.
# Lines are named by the start of their text (robust to renumbering). Every scene starts on its first line's voice
# onset (sub_lead 0); centre lines are whole sentences; lines shown only in a picture (◆) get no subtitle.
# usage: build_spec.py <episode folder> <VIDEO_ROOT>
import json, os, re, sys

F, VR = sys.argv[1], sys.argv[2]
lines = json.load(open(f"{F}/lines.json"))
plain = lambda s: re.sub(r"[\[\]]", "", s).replace("\n", " ")


def L(prefix, after=-1):
    """The first line at or after index `after` whose text starts with prefix (lines repeat words, so the plan is read
    in order: each scene searches from the previous scene's line on)."""
    for k, o in enumerate(lines):
        if k >= after and (plain(o["text"]).startswith(prefix) or o["spoken"].startswith(prefix)):
            return o["id"]
    raise AssertionError(("line not found", prefix, after))


DARK = {"sat": 0.85, "black": 0.05, "gamma": 1.3, "vignette": 0.5}
BRIGHT = {"sat": 0.8, "black": 0.06, "gamma": 1.45, "vignette": 0.55}
VBRIGHT = {"sat": 0.78, "black": 0.08, "gamma": 1.6, "vignette": 0.6}     # white sofa / white room shots
PAST = {"sat": 0.0, "black": 0.06, "gamma": 1.25, "vignette": 0.6}       # 1952: a black-and-white film
LIFT = {"sat": 0.9, "black": 0.0, "gamma": 0.85, "vignette": 0.3}        # a very dark night shot (51397)
ZOOM = {"z0": 1.0, "zoom_rate": 0.008}                                   # photos: slow zoom in only (owner)

# (first line, kind, material, extra)   kind: v = Mixkit clip id, card, icon, ai = AI photo id (work/img/<id>_s1.png)
PLAN = [
 # ① 도입: 금요일 저녁 7시, 세 가지 반응
 ("금요일 저녁 7시 퇴근길에,", "v", "4822", {"in": 1.0}),
 ("당신은 애인에게 카톡을 보냅니다.", "v", "4915", {"in": 2.0, "grade": DARK}),
 ("오늘 퇴근하고 뭐할꺼야?", "icon", "kakao", {"args": {"msgs": [
     {"me": True, "text": "오늘 퇴근하고 뭐할꺼야?", "time": "오후 7:00", "show": 0}]},
     "at": ["오늘 퇴근하고 뭐할꺼야?"]}),
 ("먼저 첫 번째,", "icon", "kakao", {"args": {"title": "첫 번째", "msgs": [
     {"me": True, "text": "오늘 퇴근하고 뭐할꺼야?", "time": "오후 7:00", "read": 0},
     {"me": False, "text": "뭐 할껀 없어, 같이 저녁 먹을까?", "time": "오후 7:05", "show": 1}]},
     "at": ["상대방의 답장이 옵니다.", "뭐 할껀 없어, 같이 저녁 먹을까?"]}),
 ("두 번째,", "icon", "kakao", {"args": {"title": "두 번째", "msgs": [
     {"me": True, "text": "오늘 퇴근하고 뭐할꺼야?", "time": "오후 7:00", "read": 0},
     {"me": False, "text": "헉 미안해, 회식 와서 연락을 이제 받네.", "time": "오후 10:14", "show": 1}]},
     "at": ["뒤늦게 답장이 도착합니다.", "헉 미안해, 회식 와서 연락을 이제 받네."]}),
 ("그리고 마지막 세 번째,", "icon", "kakao", {"args": {"title": "세 번째", "msgs": [
     {"me": True, "text": "오늘 퇴근하고 뭐할꺼야?", "time": "오후 7:00"}], "glow_one": 0},
     "at": ["메시지 옆의 노란 숫자 '1'이,"]}),
 ("자, 여러분은 어떤 상황에,", "card", None, {}),
 ("아마 대부분,", "icon", "panels3", {"args": {"focus": [[0, 2], [1, 1], [2, 2]]},
     "at": ["아마 대부분,", "두 번째는,", "세 번째는"]}),
 ("문제는, 이 침묵이 길어질 때입니다.", "card", None, {}),
 ("처음 1~2시간은,", "v", "4548", {"in": 2.0, "grade": VBRIGHT}),
 ("'야근이 길어지나?'", "card", None, {}),
 ("하며, 대수롭지 않게 넘깁니다.", "v", "26092", {"in": 1.0, "grade": DARK}),
 ("하지만 3시간, 4시간이 넘어가면,", "icon", "clock_run", {"args": {"from": 19.0, "to": 23.0, "night_word": True}}),
 ("5분마다 습관처럼", "v", "51397", {"in": 1.0, "grade": LIFT}),   # was 39789: Apple logo on the phone back (39789p is used at 9시 반)
 ("'이제 퇴근해서 집 갔을 텐데,", "card", None, {}),
 ("하고, 온갖 부정적인 상상을 펼칩니다.", "v", "51394", {"in": 12.0}),
 ("그러다 문득,", "v", "51399", {"in": 2.0}),
 ("'고작 연락 몇 시간 안 된다고,", "card", None, {}),
 ("하며, 자신을 탓합니다.", "v", "4513", {"in": 1.0, "grade": BRIGHT}),
 ("하지만 이게 정말,", "card", None, {}),
 ("원래 인간의 뇌는,", "icon", "brain_q", {"at": ["위협적으로 받아들이도록"]}),
 ("오늘은 답장이 늦어질 때,", "v", "4733", {"in": 1.0, "grade": DARK}),
 ("답장을 기다리는 시간을", "v", "4897", {"in": 1.0, "grade": BRIGHT}),
 ("3가지 현실적인 방법을", "icon", "three", {}),
 # ② 공감 사례: 지우
 ("지우는 2주째,", "v", "100050", {"in": 1.0, "grade": BRIGHT}),
 ("오후 6시 30분,", "v", "4333", {"in": 1.0}),
 ("휴대폰을 꺼내,", "v", "4915", {"in": 6.0, "grade": DARK}),
 ("오늘 하루 어땠어요?", "icon", "kakao", {"args": {"msgs": [
     {"me": True, "text": "오늘 하루 어땠어요?", "time": "오후 6:30", "show": 0}]},
     "at": ["오늘 하루 어땠어요?"]}),
 ("집에 도착해 저녁을 먹고,", "v", "42982", {"in": 1.0, "crop": [0.4, 0.25, 1.0, 0.85]}),
 ("7시가 훌쩍 넘었는데도,", "icon", "kakao", {"args": {"msgs": [
     {"me": True, "text": "오늘 하루 어땠어요?", "time": "오후 6:30"}], "glow_one": 0},
     "at": ["메시지 옆 숫자 '1'은 그대로입니다."]}),
 ("8시가 되자,", "v", "100053", {"in": 1.0, "grade": BRIGHT}),
 ("이미 수십 번은 본", "v", "4911", {"in": 1.0}),
 ("그렇게 9시가 되고,", "icon", "clock_run", {"args": {"from": 20.0, "to": 21.0, "night_word": True}}),
 ("메시지 하나를 더 보냅니다.", "v", "43381", {"in": 8.0}),
 ("바쁘세요??", "icon", "kakao", {"args": {"msgs": [
     {"me": True, "text": "오늘 하루 어땠어요?", "time": "오후 6:30"},
     {"me": True, "text": "바쁘세요??", "time": "오후 9:00", "show": 0}]}, "at": ["바쁘세요??"]}),
 ("전송 버튼을 누르자마자,", "v", "4708", {"in": 1.0, "grade": BRIGHT}),
 ("'아, 내가 연락을 너무", "card", None, {}),
 ("9시 반이 되자,", "v", "39789p", {"in": 0.0}),   # 39789 from 0 s (neutral face; she laughs from ~7 s), logo painted out
 ("'어제 내가 한 그 농담이,", "card", None, {}),
 ("밤 11시 50분,", "v", "51394", {"in": 3.0}),
 ("자요..?", "icon", "kakao", {"args": {"msgs": [
     {"me": True, "text": "오늘 하루 어땠어요?", "time": "오후 6:30"},
     {"me": True, "text": "바쁘세요??", "time": "오후 9:00"},
     {"me": True, "text": "자요..?", "time": "오후 11:50", "show": 0}], "glow_one": 1},
     "at": ["자요..?", "숫자 '1' 3개가,"]}),
 ("아마 많은 분들이,", "v", "51399", {"in": 8.0}),
 ("도대체 왜, 작은 숫자 '1' 하나에,", "card", None, {}),
 # ③ 원인 1: 유니버시티 칼리지 런던, 뱀과 바위
 ("그 이유를 찾기 위해,", "v", "4457", {"in": 1.0, "grade": DARK, "title": "영국", "title_sub": "유니버시티 칼리지 런던",
     "title_size": 150, "title_at": "영국 유니버시티 칼리지 런던의"}),
 ("지금 여러분은,", "ai", "B09c_s2", {"grade": DARK}),   # B09: odd skull-like picture on a monitor; B09b: no person
 ("여러분의 왼쪽 손등에는,", "icon", "hand_electrode", {"at": ["꽤나 따끔한 전기가 흐르는 장치죠."]}),
 ("눈앞의 큰 화면에", "icon", "rocks2", {"at": ["밑에 뱀이 없는 바위를 골라야 합니다."]}),
 ("만약 바위 밑에서 뱀이 나오면,", "icon", "rock_snake", {"at": ["만약 바위 밑에서 뱀이 나오면,",
     "손등에 따끔한 전기가 흐릅니다."], "at_shift": [0.9, 0.0]}),
 ("이 과정을 무려,", "icon", "counter320", {}),
 ("연구진은", "ai", "B09c_s2", {"grade": DARK, "z0": 1.03}),
 ("긴장할 때 저절로 커지는", "icon", "measures3", {"at": ["긴장할 때 저절로 커지는", "손끝에 맺히는",
     "그리고 참가자들이 스스로 매긴"]}),
 ("과연 참가자들은,", "card", None, {}),
 ("뱀이 나와서", "icon", "choice2", {"at": ["아니면 나올지 안 나올지,"]}),
 ("놀랍게도 정답은,", "card", None, {}),
 ("우리 몸의 긴장도는,", "icon", "curve", {"at": ["100% 확실할 때는,"]}),
 ("한마디로 우리의 뇌는,", "card", None, {}),
 ("심리학에서는 이처럼,", "v", "51399", {"in": 14.0, "title": "불확실성", "title_size": 200,
     "title_at": "'불확실성'이라고 부릅니다."}),
 ("비록 카톡을 주고받는 실험은 아니었지만,", "icon", "chat1", {}),
 ("이 실험 속 바위와", "icon", "rocks2", {"at": ["답장을 기다리는 우리는,"]}),
 ("상대가 그저", "v", "4809", {"in": 1.0, "grade": BRIGHT}),
 ("나에 대한 마음이", "v", "101412", {"in": 1.0}),
 ("답장을 기다리는 우리는,", "v", "51429", {"in": 2.0}),
 ("몇 시간 내내", "v", "31413", {"in": 1.0}),
 # ④ 원인 2: 매쿼리 대학교, 노키아 3310
 ("게다가 이렇게", "icon", "blank_bubble", {"at": ["그 빈칸을 채우기 시작합니다."]}),
 ("2004년", "v", "AUS", {"in": 1.0, "grade": DARK, "title": "2004년", "title_sub": "호주 매쿼리 대학교",
     "title_size": 170, "title_at": "2004년"}),
 ("실험에 참가한 학생은,", "v", "4519", {"in": 1.0, "grade": BRIGHT}),
 ("당시 유행하던 '노키아 3310' 휴대폰으로", "icon", "oldphone", {"args": {"lines": ["운동은 얼마나 자주 해요?"]},
     "at": ["\"운동은 얼마나 자주 해요?\""]}),
 ("곧 편하게 이야기를 나누는,", "v", "4519", {"in": 6.0, "grade": BRIGHT}),
 ("그런데 어떤 학생들에게는,", "v", "28321", {"in": 1.0, "grade": DARK}),
 ("장장 8분 동안,", "icon", "oldphone", {"args": {"timer": "8:00"}}),
 ("사실 대화 상대였던 두 사람은,", "v", "39958", {"in": 1.0, "grade": BRIGHT}),
 ("그 정적 같은 8분이 흐른 뒤,", "card", None, {}),
 ("계속 대화를 이어 간 학생들에 비해,", "v", "4560", {"in": 1.0, "grade": BRIGHT}),
 ("무리에 받아들여졌다는", "icon", "drops3", {"at": ["'소속감' 점수가,", "'통제감',", "'자존감'까지,"]}),
 ("더 눈여겨볼 점은 그다음입니다.", "card", None, {}),
 ("실험이 끝난 뒤,", "v", "99890", {"in": 1.0}),
 ("'휴대폰 고장' 같은", "icon", "phone_off", {}),
 ("'내가 말을 재미없게 했나?'", "card", None, {}),
 ("하며, 자기 자신을 탓한 학생이", "v", "4701", {"in": 1.0, "grade": BRIGHT}),
 ("생판 처음 본 사람에게,", "v", "8743", {"in": 1.0, "grade": DARK}),
 ("사람의 마음은", "v", "8739", {"in": 1.0}),
 ("지우가 지난 대화창을", "v", "51395", {"in": 15.0}),
 ("'어제 내 농담이 별로였나?'", "card", None, {}),
 ("하고 자책했던 것과,", "v", "4513", {"in": 6.0, "grade": BRIGHT}),
 # ⑤ 심층 원인: 1952년 로라, 애착
 ("도대체 왜 우리의 뇌는,", "card", None, {}),
 ("그 깊은 뿌리를 따라가 보면,", "ai", "B01", {"grade": PAST, "title": "1952년", "title_sub": "영국",
     "title_size": 170, "title_at": "1952년 영국에서 공개된,"}),
 ("영화의 주인공은,", "icon", "profile", {"args": {"name": "로라", "line1": "1952년 기록 영화의 주인공",
     "line2": "태어난 지 2년 5개월", "kid": True}}),
 ("로라는 작은 수술을 받기 위해,", "ai", "B02", {"grade": PAST}),
 ("당시 병원들은,", "icon", "door_closed", {"at": ["부모의 면회를 엄격하게 금지했습니다."]}),
 ("심리학자 존 볼비 연구팀은,", "icon", "profile", {"args": {"name": "존 볼비", "line1": "John Bowlby",
     "line2": "영국 · 애착 이론"}}),
 ("엄마와 연락이 완전히 끊긴 채", "icon", "film_camera", {}),
 ("입원 첫날,", "ai", "B05", {"grade": PAST}),
 ("그런데 사흘째가 되자,", "ai", "B06", {"grade": PAST}),
 ("간호사들 눈에는,", "ai", "B07", {"grade": PAST}),
 ("하지만 그건 적응한 게 아니라,", "ai", "B02", {"grade": PAST, "z0": 1.03}),
 ("실제로 간호사가 다정하게 다가와 말을 걸자,", "ai", "B08b", {"grade": PAST}),   # B08 showed her face
 ("존 볼비는,", "v", "40421", {"in": 1.0, "grade": BRIGHT, "title": "애착", "title_size": 230,
     "title_at": "'애착'이라는 개념으로 설명했습니다."}),
 ("인간의 마음속에는,", "icon", "siren", {}),
 ("내가 의지하는 사람이", "v", "939", {"in": 1.0, "grade": DARK}),
 ("뇌는 즉시 비상벨을 울립니다.", "icon", "siren", {}),
 ("처음에는 로라가 울부짖었듯,", "v", "51429", {"in": 8.0}),
 ("침묵이 길어지면", "v", "4500", {"in": 1.0, "grade": BRIGHT}),
 ("문제는,", "v", "51395", {"in": 1.5}),
 ("이 마음속 경보 장치가", "icon", "siren", {}),
 ("성인이 된 후에는,", "v", "PARENT", {"in": 1.0, "grade": BRIGHT}),
 ("고스란히 '연인'이나,", "v", "4624", {"in": 1.0, "grade": BRIGHT}),
 ("지우가 줄어들지 않는 숫자 '1'을 보며,", "v", "51394", {"in": 20.0}),
 ("결국 불 꺼진 방에서", "v", "43381", {"in": 1.0}),
 ("어릴 적 로라의 마음속에서", "icon", "siren", {}),
 # ⑥ 개인차: 경보 장치의 예민함
 ("그런데 참 신기하죠.", "card", None, {}),
 ("모든 사람에게", "v", "4401", {"in": 2.65, "grade": DARK, "crop": [0.075, 0.15, 0.925, 1.0]}),  # in 2.65: the boy-band ad truck (Sexy Zone) is in view until ~1.8 s, a bus with text from 6.75 s
 ("누군가는 편하게 쉬며 일상을 보내고,", "v", "26091", {"in": 1.0}),
 ("누군가는 지우처럼 피 말리는 밤을", "v", "51394", {"in": 32.5}),
 ("그 이유는,", "icon", "siren", {}),
 ("심리학 연구들을 살펴보면,", "icon", "people5", {"at": ["성인 5명 중 1명꼴로는,"]}),
 ("이런 분들은,", "v", "8739", {"in": 6.0}),
 ("실제로 몸속 스트레스 호르몬 수치가", "icon", "gauge", {}),
 ("밤잠까지 설치는", "v", "51394", {"in": 28.0}),
 ("상대의 의도를 알 수 없는", "icon", "chat1", {}),
 ("예민한 경보 장치가", "icon", "siren", {}),
 ("'왜 연락이 없지?", "card", None, {}),
 ("하는, 최악의 시나리오를", "v", "4700", {"in": 1.0, "grade": BRIGHT}),
 # ⑦ 희망과 해결책 소개
 ("하지만, 괜찮습니다.", "card", None, {}),
 ("수십 년간", "icon", "graph_down", {}),
 ("또 나와 잘 맞는", "v", "4764", {"in": 1.0, "grade": BRIGHT}),
 ("타고난 마음의 경보 장치가,", "v", "4800", {"in": 1.0}),
 ("우리가 어떻게 다루느냐에 따라,", "v", "4897", {"in": 8.0, "grade": BRIGHT}),
 ("자, 그렇다면", "icon", "chat1", {}),
 ("과학적으로 검증된,", "icon", "three", {}),
 # ⑧ 해결책 1: 이름 붙이기 (거미는 아이콘으로만, 2026-10-23 사용자 결정)
 ("첫째, 애써 '괜찮아'라고", "card", None, {"label": "1 / 3"}),
 ("2012년 키르칸스키 연구팀은,", "icon", "spider_title", {"at": ["거미를 끔찍이 무서워하는 참가자,"]}),
 ("그리고는 살아 움직이는 거대한 독거미,", "icon", "spider_60", {"at": ["불과 60cm 떨어진 자리에 앉혔죠."]}),
 ("참가자들에게", "icon", "groups3", {"args": {"mode": "intro"}}),
 ("첫 번째 그룹은,", "icon", "groups3", {"args": {"mode": "focus", "i": 0}}),
 ("\"저 징그러운 타란툴라가", "card", None, {}),
 ("두 번째 그룹은,", "icon", "groups3", {"args": {"mode": "focus", "i": 1}}),
 ("\"저 작은 거미는 날 해치지 않아,", "card", None, {}),
 ("세 번째 그룹은,", "icon", "groups3", {"args": {"mode": "focus", "i": 2}}),
 ("\"우리 집 거실 소파 앞에는", "card", None, {}),
 ("일주일 뒤,", "icon", "groups3", {"args": {"mode": "intro"}}),
 ("스스로를 달랜 그룹도,", "icon", "groups3", {"args": {"mode": "answer"}, "at": ["'불안해'라고"]}),
 ("내 감정에 정확한 이름을 붙이는 순간,", "icon", "siren_calm", {"at": ["흥분해 있던 뇌의 경보 장치가,"]}),
 ("답장이 없어 마음이 요동칠 땐,", "v", "42270", {"in": 1.0, "grade": BRIGHT}),
 ("휴대폰 메모장을 열어", "v", "4915", {"in": 14.0, "grade": DARK}),
 ("\"6시 30분에 보낸 카톡이", "icon", "memo", {"args": {
     "text": "6시 30분에 보낸 카톡이 아직 안 읽혀서, 지금 내가 많이 불안하구나."},
     "at": ["\"6시 30분에 보낸 카톡이"]}),
 # ⑨ 해결책 2: 확인 시간의 주도권, 만약-그러면
 ("둘째, 휴대폰을 언제 확인할지,", "card", None, {"label": "2 / 3"}),
 ("행동경제학자", "icon", "profile", {"args": {"name": "댄 애리얼리", "line1": "Dan Ariely", "line2": "행동경제학자"}}),
 ("스마트폰 사용자를 대상으로,", "v", "39780", {"in": 1.0, "grade": BRIGHT, "blur_box": [[0.75, 0.24, 0.935, 0.67, 8]]}),   # lock-screen text readable at full size
 ("흔히 알림을 아예 꺼 두면", "icon", "bell_off", {"at": ["흔히 알림을 아예 꺼 두면"], "at_shift": [0.8]}),
 ("알림을 완전히 끈 사람들은,", "v", "8744", {"in": 1.0, "grade": BRIGHT}),
 ("대신 오전 9시,", "icon", "clocks3", {"at": ["대신 오전 9시,", "오후 3시,", "밤 9시."], "at_shift": [0.3, 0, 0]}),
 ("휴대폰 화면을 열어 보는 횟수가", "v", "4938", {"in": 1.0, "grade": BRIGHT}),
 ("일상에 더 깊이 집중할 수 있었고,", "v", "4761", {"in": 1.0, "grade": BRIGHT}),
 ("하지만 막상 시간을 정해 둬도,", "v", "41638", {"in": 1.0, "grade": DARK}),
 ("휴대폰을 확인하고 싶은 유혹이,", "v", "100053", {"in": 6.0, "grade": BRIGHT}),
 ("이럴 땐, '만약-그러면' 공식을", "card", None, {}),
 ("막연하게 '참아야지' 다짐하는 것보다,", "v", "4517", {"in": 1.0, "grade": BRIGHT}),
 ("'만약 어떤 상황이 오면,", "card", None, {}),
 ("구체적인 규칙을 미리 정해 두면,", "icon", "ifthen", {"at": ["성공 확률이 비약적으로 높아집니다."]}),
 ("예를 들어, 이렇게 정해 두는 겁니다.", "v", "42655", {"in": 1.0}),
 ("\"만약 30분이 지나도", "card", None, {}),
 # ⑩ 해결책 3: 든든한 사람의 사진
 ("셋째, 이미 마음이 무겁게 가라앉았다면,", "card", None, {"label": "3 / 3"}),
 ("코넬 대학교에서", "v", "4560", {"in": 8.0, "grade": BRIGHT, "title": "코넬 대학교", "title_size": 150,
     "title_at": "코넬 대학교에서"}),
 ("과거에 속상했던 기억을", "v", "4708", {"in": 6.0, "grade": BRIGHT}),
 ("화면에 띄운 사진을,", "v", "41180", {"in": 1.0}),
 ("그 결과,", "icon", "bars_mood", {"at": ["자신의 어머니 사진을 본 학생들의"]}),
 ("여기서 주목할 점은,", "icon", "order2", {"at": ["사진을 먼저 본 그룹에서는,"]}),
 ("즉, 이 방법은", "icon", "medkit", {"at": ["예방주사가 아니라,", "'마음의 응급약'으로 써야"]}),
 ("만약 기다림에 지쳐", "v", "4511", {"in": 1.0, "grade": BRIGHT}),
 ("답장 없는 그 사람의 프로필 사진을", "v", "4911", {"in": 8.0}),
 ("부모님이나 오랜 친구,", "v", "4656", {"in": 1.0, "grade": BRIGHT}),
 ("혹은 반려동물처럼,", "v", "101233", {"in": 1.0, "grade": BRIGHT}),
 ("내 마음을 무조건적으로", "v", "4644", {"in": 1.0}),
 # ⑪ 마무리
 ("생각해 보면,", "v", "4840", {"in": 1.0}),
 ("어쩌면", "v", "52419", {"in": 1.0, "grade": DARK}),
 ("예상치 못하게 길어진 회의,", "v", "4547", {"in": 1.0, "grade": BRIGHT}),
 ("발 디딜 틈 없는 퇴근길 지하철,", "v", "1623", {"in": 1.0, "grade": DARK}),
 ("갑자기 꺼져 버린 휴대폰 배터리 같은,", "icon", "phone_off", {}),
 ("일상의 바람 말이에요.", "v", "4231", {"in": 1.0, "grade": DARK}),
 ("물론, 때로는 아무리 기다려도,", "v", "25592", {"in": 1.0, "grade": BRIGHT}),
 ("하지만 그건,", "v", "51395", {"in": 8.0}),
 ("어쩌면 답장 하나에,", "v", "4664", {"in": 1.0, "grade": {"sat": 0.7, "black": 0.1, "gamma": 1.9, "vignette": 0.7},
     "blur": 6}),
 ("여러분들만의", "v", "100067", {"in": 1.0}),
 ("댓글로 공유해 주세요.", "v", "100050", {"in": 6.0, "grade": BRIGHT}),
]
# materials still to be decided after the second licence check (placeholders above)
# clips made from a Mixkit clip by a script in this folder (prep_patches.sh)
PATCHED = {"39789p": "Mixkit 39789, phone logo painted out (logo_patch.py via prep_patches.sh)"}
SUBST = json.load(open(f"{F}/stock_choices.json")) if os.path.exists(f"{F}/stock_choices.json") else {}

scenes, pos = [], -1
idx = {o["id"]: k for k, o in enumerate(lines)}
for i, (first, kind, mat, extra) in enumerate(PLAN):
    sid = f"{i + 1:03d}"
    x = {k: v for k, v in extra.items() if k not in ("at", "title_at")}
    sc = {"id": sid, "from": L(first, pos + 1)}
    pos = idx[sc["from"]]
    if kind == "v":
        mat = SUBST.get(mat, mat)
        sc.update(type="video", src=f"work/stock/full/{mat}.mp4", note=PATCHED.get(mat, f"Mixkit {mat}"), **x)
    elif kind == "ai":
        sc.update(type="photo", image=f"work/img/{mat}.png" if "_s" in mat else f"work/img/{mat}_s1.png", note=f"AI {mat} (ai_images.json)", **{**ZOOM, **x})
    elif kind == "icon":
        sc.update(type="icon", icon=mat, **x)
        if "at" in extra:
            sc["at"] = [L(a, pos) for a in extra["at"]]
    else:
        sc.update(type="card", **x)
    if "title_at" in extra:
        sc["title_at"] = L(extra["title_at"], pos)
    scenes.append(sc)
order = {o["id"]: k for k, o in enumerate(lines)}
starts = [order[s["from"]] for s in scenes]
assert starts == sorted(starts) and len(set(starts)) == len(starts), "scenes out of order"


def scene_at(k):
    j = max(i for i, s in enumerate(starts) if s <= k)
    return scenes[j]


subs = []
for k, o in enumerate(lines):
    sc = scene_at(k)
    on_black = sc["type"] in ("icon", "card")
    if o["kind"] == "bubble":            # shown only inside the picture (chat bubble, memo): no subtitle, but the
        subs.append({"unit": o["id"], "text": "", "box": False})          # previous one ends when this is spoken
        continue
    s = {"unit": o["id"], "text": o["text"]}
    if o["kind"] in ("center", "italic"):
        s["pos"] = "center"
        if o["kind"] == "italic":
            s["italic"] = True
        if not on_black:
            s["shadow"] = True
    elif on_black:
        s["box"] = False
    subs.append(s)
spec = {"note": "paths are relative to VIDEO_ROOT (venv/, models/, work/); build_spec.py also writes work/spec_abs.json",
        "fade_in": 0.3, "fade_out": 0.5, "sub_lead": 0, "scenes": scenes, "subs": subs}
json.dump(spec, open(f"{F}/spec.json", "w"), ensure_ascii=False, indent=1)
missing = []
for sc in scenes:
    for k in ("src", "image"):
        if k in sc:
            sc[k] = os.path.join(VR, sc[k])
            if not os.path.exists(sc[k]):
                missing.append(sc[k])
json.dump(spec, open(f"{VR}/work/spec_abs.json", "w"), ensure_ascii=False, indent=1)
kinds = {}
for sc in scenes:
    kinds[sc["type"]] = kinds.get(sc["type"], 0) + 1
print(len(scenes), "scenes", kinds, "|", len(subs), "subtitle lines |", len(missing), "files missing")
for m in missing:
    print("  missing", m)
