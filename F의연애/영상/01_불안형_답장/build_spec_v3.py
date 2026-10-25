# 01편 장면 명세 v3 (2026-10-25, the owner's v3 request): lines_v3.json + the plan below -> spec_v3.json (paths relative
# to VIDEO_ROOT) and work/v3/spec_abs.json (absolute paths, for build_timeline.py).
# The plan is v2's (build_spec_v2.py) with the owner's own AI photos put where the script marks them: "<대사>(N)" ->
# photo N (work/owner_v3/NN.png from make_photos_v3.py; the owner: "내가 만든 ai 그림으로 대체하는 대사 부분은 < >으로
# 묶은 다음 옆에 (1), (2)이런식으로 번호를 매겨놨어. 바꿔주면 돼"). A photo shows from the first marked line until the
# next scene (the next marked line, or the scene v2 had after the marked words). Lines without a mark keep v2's
# picture. Comments "(N)" below are the owner's photo numbers.
# New in v3:
# - photo 4 (brain) explains its sentence: a '?' over the brain at '알 수 없는 상태를', growing and settling onto the
#   brain at '훨씬 더 무겁고', turning red with the brain at '위협적으로' (icons_photo.brain_unknown, render.py "mix");
# - "뱀이 나와서 … 반반이라고 느낄 때였을까요?" is a split screen: photo 15 on the right from the first line, photo 13
#   on the left from '아니면 나올지 안 나올지' (render.py "split"; each panel is the middle of its photo, around the
#   monitor, at the panel's 956x1080 shape);
# - centre text over an owner's photo (3, 22): the photo lightly blurred and darker under the text (v2 rule: "가운데
#   글씨 뒤에 … 흐리고 약간 어둡게"), less blurred than stock (sigma 6, not 14) so the photo is still seen; photo 3 comes
#   into focus at the bottom line '자신을 탓합니다.'
# usage: build_spec_v3.py <episode folder> <VIDEO_ROOT>
import json, os, re, sys

F, VR = sys.argv[1], sys.argv[2]
lines = json.load(open(f"{F}/lines_v3.json"))
T = {a["id"]: a["start"] for a in json.load(open(f"{F}/lines_align_v3.json"))}
plain = lambda s: re.sub(r"[\[\]]", "", s).replace("\n", " ")


def L(prefix, after=-1):
    """The first line at or after index `after` whose text starts with prefix (the plan is read in order)."""
    for k, o in enumerate(lines):
        if k >= after and (plain(o["text"]).startswith(prefix) or o["spoken"].startswith(prefix)):
            return o["id"]
    raise AssertionError(("line not found", prefix, after))


DARK = {"sat": 0.85, "black": 0.05, "gamma": 1.3, "vignette": 0.5}
BRIGHT = {"sat": 0.8, "black": 0.06, "gamma": 1.45, "vignette": 0.55}
VBRIGHT = {"sat": 0.78, "black": 0.08, "gamma": 1.6, "vignette": 0.6}
PAST = {"sat": 0.0, "black": 0.06, "gamma": 1.25, "vignette": 0.6}
LIFT = {"sat": 0.9, "black": 0.0, "gamma": 0.85, "vignette": 0.3}
ZOOM = {"z0": 1.0, "zoom_rate": 0.008}
# v2: background under centre text, "흐릿하고 약간 어둡게" (blurred and a little darker)
BLURBG = {"sat": 0.8, "black": 0.07, "gamma": 1.65, "vignette": 0.6}
BLUR = 14
PAST_DIM = {"sat": 0.0, "black": 0.08, "gamma": 1.6, "vignette": 0.65}
# v3: the owner's photos are already dark and muted; only a light touch so they sit with the graded stock
OWN = {"sat": 0.95, "black": 0.01, "gamma": 1.05, "vignette": 0.3}
OWN_DIM = {"sat": 0.85, "black": 0.05, "gamma": 1.45, "vignette": 0.55}      # under centre text, with blur OWN_BLUR
OWN_BLUR = 6
OWN_ZOOM = {"z0": 1.0, "zoom_rate": 0.008}

KAKAO_ME = lambda text, time, **k: dict(me=True, text=text, time=time, **k)
MY1 = "오늘 퇴근하고 뭐할꺼야?"
MY2 = "오늘 하루 어땠어요?"

# (first line, kind, material, extra)   kind: v = Mixkit clip id, vb = clip as a blurred, darker background under
# centre text, card, icon, ai = AI photo id (work/img/<id>_s1.png), photo = work/img/<name>.png,
# own = the owner's photo number (work/owner_v3/NN.png), split = two owner's photos side by side ("panels")
# split screen panels: 956x1080 (render.py panel_size) cut from the middle of the 1984x1116 photo, around the monitor
# (its centre measured at x 996): 988 x 1116 has the panel's shape
PANEL_CROP = [502, 0, 1490, 1116]
PLAN = [
 # ① 도입
 ("금요일 저녁 7시 퇴근길에", "v", "4822", {"in": 1.0}),
 ("당신은 애인에게 카톡을 보냅니다.", "v", "4915", {"in": 2.0, "grade": DARK}),
 # kakao (1, 2, 20, 22): no entrance effect and no yellow glow behind the 1 (icons_chat.py v2); titles white, larger
 ("오늘 퇴근하고 뭐할꺼야?", "icon", "kakao", {"args": {"msgs": [KAKAO_ME(MY1, "오후 7:00", show=0)]},
     "at": ["오늘 퇴근하고 뭐할꺼야?"]}),
 ("먼저 첫 번째", "icon", "kakao", {"args": {"title": "첫 번째", "msgs": [
     KAKAO_ME(MY1, "오후 7:00", read=0),
     {"me": False, "text": "뭐 할껀 없어, 같이 저녁 먹을까?", "time": "오후 7:05", "show": 1}]},
     "at": ["상대방의 답장이 옵니다.", "뭐 할껀 없어"]}),
 ("두 번째", "icon", "kakao", {"args": {"title": "두 번째", "msgs": [
     KAKAO_ME(MY1, "오후 7:00", read=0),
     {"me": False, "text": "헉 미안해..ㅜ회식 와서 연락을 이제 봤네", "time": "오후 10:14", "show": 1}]},   # (1)
     "at": ["뒤늦게 답장이 도착합니다.", "헉 미안해"]}),
 ("그리고 마지막 세 번째", "icon", "kakao", {"args": {"title": "세 번째", "msgs": [KAKAO_ME(MY1, "오후 7:00")]}}),
 ("여러분은 어떤 상황에", "card", None, {}),                                                        # (3)
 ("아마 대부분", "icon", "panels3", {"args": {"focus": [[0, 2], [1, 1], [2, 2]]},                  # (6, 7)
     "at": ["아마 대부분", "두 번째는", "세 번째는"]}),
 ("문제는", "card", None, {}),
 ("처음 1~2시간은", "v", "4548", {"in": 2.0, "grade": VBRIGHT}),
 ("야근이 길어지나?", "card", None, {}),                                                          # (8)
 ("대수롭지 않게 넘깁니다.", "v", "26092", {"in": 1.0, "grade": DARK}),
 ("하지만 3시간 4시간이 넘어가면", "own", 1, {}),                                               # (1) wall clock
 ("5분마다 습관처럼", "own", 2, {}),                                                            # (2) phone at night
 ("이제 퇴근해서 집 갔을 텐데", "card", None, {}),
 ("온갖 부정적인 상상을 펼칩니다.", "v", "51394", {"in": 12.0}),
 ("그러다 문득", "v", "51399", {"in": 0.0}),       # 51399 tosses and turns fast at 3.5-6.0 and 11.5-15.5 s (see 26)
 ("고작 연락 몇 시간 안 된다고", "own", 3, {"grade": OWN_DIM, "blur": OWN_BLUR,                 # (3) centre text over
     "mix": {"at": "자신을 탓합니다.", "grade": OWN, "blur": 0, "dur": 0.5}}),                   # it, then in focus
 ("하지만 이게 정말", "card", None, {}),                                                         # (15)
 ("원래 인간의 뇌는", "own", 4, {"cy0": 0.47, "cy1": 0.47,                                       # (4) brain explainer
     "overlay": {"kind": "brain_unknown", "at": ["'알 수 없는 상태'를", "훨씬 더 무겁고", "위협적으로 받아들이도록"]},
     "mix": {"at": "위협적으로 받아들이도록", "image": "work/owner_v3/04_red.png", "dur": 0.6}}),
 ("오늘은 답장이 늦어질 때", "v", "4733", {"in": 1.0, "grade": DARK}),
 ("답장을 기다리는 시간을", "v", "4897", {"in": 1.0, "grade": BRIGHT}),   # (23) runs on through 알려드리겠습니다
 # ② 공감 사례: 지우
 ("지우는 2주째", "own", 5, {}),                                                                # (5)
 ("오후 6시 30분", "own", 6, {}),                                                                # (6)
 ("휴대폰을 꺼내", "own", 7, {}),                                                                # (7)
 ("오늘 하루 어땠어요?", "icon", "kakao", {"args": {"msgs": [KAKAO_ME(MY2, "오후 6:30", show=0)]},
     "at": ["오늘 하루 어땠어요?"]}),
 ("집에 도착해 저녁을 먹고", "own", 8, {}),                                                       # (8)
 ("7시가 훌쩍 넘었는데도", "v", "39826", {"in": 0.0, "crop": [0.15, 0.3, 0.85, 1.0]}),   # (19) the hands run on past 7:55
 ("메시지 옆 숫자 '1'은 그대로입니다.", "icon", "kakao", {"args": {"msgs": [KAKAO_ME(MY2, "오후 6:30")]}}),   # (20)
 ("8시가 되자", "own", 9, {}),                                                                   # (9) profile photo
 ("그렇게 9시가 되고", "own", 10, {}),                                                           # (10) 9:00
 ("메시지 하나를 더 보냅니다.", "v", "43381", {"in": 8.0}),
 ("바쁘세요??", "icon", "kakao", {"args": {"msgs": [KAKAO_ME(MY2, "오후 6:30"),
     KAKAO_ME("바쁘세요??", "오후 9:00", show=0)]}, "at": ["바쁘세요??"]}),
 ("전송 버튼을 누르자마자", "v", "4708", {"in": 2.5, "grade": BRIGHT}),
 ("내가 연락을 너무 재촉하는 것처럼", "card", None, {}),                                         # (21)
 ("9시 반이 되자", "v", "39789p", {"in": 0.0}),
 ("어제 내가 한 그 농담이", "card", None, {}),
 ("밤 11시 50분", "v", "51394", {"in": 3.0}),
 ("자요..?", "icon", "kakao", {"args": {"msgs": [KAKAO_ME(MY2, "오후 6:30"), KAKAO_ME("바쁘세요??", "오후 9:00"),
     KAKAO_ME("자요..?", "오후 11:50", show=0)]}, "at": ["자요..?"]}),                         # (22)
 ("아마 많은 분들이", "v", "51399", {"in": 7.8}),                     # 7.8-11.3 s: inside the calm stretch 6.0-11.4
 ("도대체 왜", "card", None, {}),                                                                # (24)
 # ③ 원인 1: 유니버시티 칼리지 런던, 뱀과 바위
 ("그 이유를 찾기 위해", "v", "4457", {"in": 1.0, "grade": DARK, "title": "영국", "title_sub": "유니버시티 칼리지 런던",
     "title_size": 150, "title_at": "영국 유니버시티 칼리지 런던의"}),
 ("지금 여러분은", "own", 11, {}),                                                               # (11) the lab
 ("여러분의 왼쪽 손등에는", "own", 12, {}),                                                      # (12) the electrode
 ("이건 실험 전에", "card", None, {}),                                         # (owner, added: centre text)
 ("눈앞의 큰 화면에", "own", 13, {"zoom_rate": 0.005}),                                          # (13) two rocks; 13-14-15
 ("여러분은 그중", "own", 14, {"zoom_rate": 0.005, "cont_zoom": True}),                          # (14) are one framing:
 ("만약 바위 밑에서 뱀이 나오면", "own", 15, {"zoom_rate": 0.005, "cont_zoom": True}),           # (15) one slow zoom
 ("이 과정을 무려", "icon", "counter320", {}),
 ("연구진은", "ai", "B09c_s2", {"grade": DARK, "z0": 1.03}),
 ("긴장할 때 저절로 커지는", "own", 17, {}),                                                      # (17) the eye
 ("손끝에 맺히는", "own", 18, {}),                                                               # (18) sweaty hand
 ("그리고 참가자들이 스스로 매긴", "own", 19, {}),                                               # (19) stress score
 ("과연 참가자들은", "card", None, {}),                                                         # (25)
 ("뱀이 나와서", "split", None, {"panels": [                                                    # (15) right, then
     {"side": "right", "own": 15, "crop": PANEL_CROP, "cx": 0.5, "cy": 0.32},                     # (13) left
     {"side": "left", "own": 13, "crop": PANEL_CROP, "cx": 0.5, "cy": 0.32, "at": "아니면 나올지 안 나올지"}]}),
 ("놀랍게도 정답은", "card", None, {}),
 ("우리 몸의 긴장도는", "icon", "curve", {"at": ["100% 확실할 때는"]}),
 ("한마디로 우리의 뇌는", "card", None, {}),
 ("심리학에서는 이처럼", "v", "51390", {"in": 5.0, "grade": LIFT, "title": "불확실성", "title_size": 200,   # (26)
     "title_at": "'불확실성'이라고 부릅니다."}),
 ("비록 카톡을 주고받는 실험은 아니었지만", "v", "43381", {"in": 10.0}),                          # (27)
 ("이 실험 속 바위와", "own", 13, {}),                                                            # (13) again
 ("상대가 그저", "v", "4809", {"in": 1.0, "grade": BRIGHT}),
 ("나에 대한 마음이", "v", "101412", {"in": 1.0}),
 ("답장을 기다리는 우리는", "v", "51429", {"in": 2.0}),
 ("몇 시간 내내", "v", "31413", {"in": 1.0}),
 # ④ 원인 2: 매쿼리 대학교, 노키아 3310
 ("게다가 이렇게", "v", "51389", {"in": 0.0}),                                                  # (28)
 ("우리의 뇌는", "v", "51390", {"in": 16.0}),
 ("2004년", "v", "AUS", {"in": 1.0, "grade": DARK, "title": "2004년", "title_sub": "호주 매쿼리 대학교",
     "title_size": 170, "title_at": "2004년"}),
 ("실험에 참가한 학생은", "own", 20, {}),                                                         # (20) Nokia 3310
 ("운동은 얼마나 자주 해요?", "vb", "100530", {"in": 1.0}),                                     # (29)
 ("곧 편하게 이야기를 나누는", "v", "51121", {"in": 0.5}),                                     # (30)
 ("그런데 어떤 학생들에게는", "v", "28321", {"in": 1.0, "grade": DARK}),
 ("장장 8분 동안", "icon", "oldphone", {"args": {"timer": "8:00"}}),
 ("사실 대화 상대였던 두 사람은", "v", "39958", {"in": 1.0, "grade": BRIGHT}),
 ("그 정적 같은 8분이 흐른 뒤", "vb", "8757", {"in": 0.0}),                                   # (31)
 ("계속 대화를 이어 간 학생들에 비해", "v", "4560", {"in": 1.0, "grade": BRIGHT}),
 ("무리에 받아들여졌다는", "icon", "drops3", {"at": ["'소속감' 점수가", "'통제감'", "'자존감'까지"]}),
 ("더 눈여겨볼 점은 그다음입니다.", "card", None, {}),
 ("실험이 끝난 뒤", "v", "99890", {"in": 1.0}),
 ("'휴대폰 고장' 같은", "own", 21, {}),                                                           # (21) broken phone
 ("내가 말을 재미없게 했나?", "own", 22, {"grade": OWN_DIM, "blur": OWN_BLUR}),                  # (22) centre text
 ("자기 자신을 탓한 학생이", "v", "4701", {"in": 1.0, "grade": BRIGHT}),
 ("생판 처음 본 사람에게", "v", "8743", {"in": 1.0, "grade": DARK}),
 ("사람의 마음은", "v", "8739", {"in": 1.0}),
 ("지우가 지난 대화창을", "v", "51395", {"in": 15.0}),            # (32) '어제 내 농담이 별로였나?' is a bottom line here
 ("하고 자책했던 것과", "v", "4513", {"in": 6.0, "grade": BRIGHT}),
 # ⑤ 심층 원인: 1952년 로라, 애착
 ("도대체 왜 우리의 뇌는", "card", None, {}),
 ("그 깊은 뿌리를 따라가 보면", "ai", "B01", {"grade": PAST, "title": "1952년", "title_sub": "영국",
     "title_size": 170, "title_at": "1952년 영국에서 공개된"}),
 ("영화의 주인공은", "own", 23, {}),                                                              # (23) Laura
 ("로라는 작은 수술을 받기 위해", "ai", "B02", {"grade": PAST}),
 ("당시 병원들은", "own", 24, {}),                                                                # (24) no visitors
 ("심리학자 존 볼비 연구팀은", "photo", "bowlby_v2", {"grade": PAST}),             # (34) the owner's photo
 ("엄마와 연락이 완전히 끊긴 채", "own", 25, {}),                                                  # (25) the camera
 ("입원 첫날", "own", 23, {}),                                       # "(23)" again in the script (no photo 26 was sent)
 ("그런데 사흘째가 되자", "own", 27, {}),                                                        # (27)
 ("간호사들 눈에는", "ai", "B07", {"grade": PAST}),
 ("하지만 그건 적응한 게 아니라", "ai", "B02", {"grade": PAST, "z0": 1.03}),
 ("아무리 불러도 엄마가 오지 않자", "ai", "B02", {"grade": PAST_DIM, "blur": 10, "cont_zoom": True}),   # (35)
 ("실제로 간호사가 다정하게 다가와 말을 걸자", "own", 28, {}),                                    # (28)
 ("존 볼비는", "v", "40421", {"in": 1.0, "grade": BRIGHT, "title": "애착", "title_size": 230,
     "title_at": "'애착'이라는 개념으로 설명했습니다."}),
 ("인간의 마음속에는", "icon", "siren", {}),
 ("내가 의지하는 사람이", "v", "939", {"in": 1.0, "grade": DARK}),
 ("뇌는 즉시 비상벨을 울립니다.", "icon", "siren", {}),
 ("처음에는 로라가 울부짖었듯", "v", "51429", {"in": 8.0}),
 ("침묵이 길어지면", "v", "4500", {"in": 1.0, "grade": BRIGHT}),
 ("문제는", "card", None, {}),                                                                  # (36)
 ("성인이 된 후에는", "v", "PARENT", {"in": 1.0, "grade": BRIGHT}),
 ("고스란히 '연인'이나", "v", "4624", {"in": 1.0, "grade": BRIGHT}),
 ("지우가 줄어들지 않는 숫자 '1'을 보며", "v", "51394", {"in": 20.0}),
 ("결국 불 꺼진 방에서", "v", "25586", {"in": 0.5, "grade": DARK}),         # (37) alone on the floor of a dark room
 ("어릴 적 로라의 마음속에서", "icon", "siren", {}),
 # ⑥ 개인차: 경보 장치의 예민함
 ("그런데 참 신기하죠.", "card", None, {}),
 ("모든 사람에게", "v", "4401", {"in": 2.65, "grade": DARK, "crop": [0.075, 0.15, 0.925, 1.0]}),
 ("누군가는 편하게 쉬며 일상을 보내고", "v", "26091", {"in": 1.0}),
 ("누군가는 지우처럼 피 말리는 밤을", "v", "51394", {"in": 32.5}),
 ("그 이유는", "card", None, {}),                                                               # (38)
 ("심리학 연구들을 살펴보면", "icon", "people5", {"at": ["성인 5명 중 1명꼴로는"]}),
 ("이런 분들은", "v", "8739", {"in": 6.0}),
 ("실제로 몸속 스트레스 호르몬 수치가", "icon", "gauge", {}),
 ("밤잠까지 설치는", "v", "51394", {"in": 28.0}),
 ("상대의 의도를 알 수 없는", "card", None, {}),                                                # (39)
 ("예민한 경보 장치가", "icon", "siren", {}),
 ("왜 연락이 없지?", "card", None, {}),
 ("최악의 시나리오를", "v", "4700", {"in": 1.0, "grade": BRIGHT}),
 # ⑦ 희망과 해결책 소개
 ("하지만", "card", None, {}),                                                                   # (40)
 ("수십 년간", "icon", "graph_down", {}),
 ("나이가 들고 경험이 쌓일수록", "own", 29, {}),                                                 # (29)
 ("또 나와 잘 맞는", "v", "4764", {"in": 1.0, "grade": BRIGHT}),
 ("타고난 마음의 경보 장치가", "v", "4800", {"in": 1.0}),
 ("우리가 어떻게 다루느냐에 따라", "v", "4897", {"in": 8.0, "grade": BRIGHT}),
 ("자 그렇다면", "v", "31413", {"in": 7.5}),                          # (41) tonight, in bed, the phone in his hand
 ("요동치는 우리 마음을", "v", "42904", {"in": 6.0}),                  #      ... and a slow breath (다독여야)
 ("과학적으로 검증된", "card", None, {}),                                                       # (42)
 # ⑧ 해결책 1: 이름 붙이기
 ("첫째", "card", None, {"label": "1 / 3"}),
 ("2012년 키르칸스키 연구팀은", "v", "43846", {"in": 0.0}),       # (43) a face frozen in fear, hand shadows creeping
 ("그리고는 살아 움직이는 거대한 독거미", "icon", "spider_60", {"at": ["불과 60cm 떨어진 자리에 앉혔죠."]}),
 ("참가자들에게", "card", None, {}),                                                            # (44)
 ("그룹마다 각기 다른 말을", "v", "43396", {"in": 2.0}),                                        # (45)
 ("첫 번째 그룹은", "vb", "43404", {"in": 0.0}),                                                # (46)
 ("두 번째 그룹은", "vb", "42903", {"in": 17.0}),                                               # (47)
 ("세 번째 그룹은", "vb", "3110", {"in": 7.9}),                                                 # (48)
 ("일주일 뒤", "v", "3132", {"in": 0.0}),                                                       # (49)
 ("참가자들이 다시 거미를 마주했을 때", "v", "8736", {"in": 0.0}),
 ("스스로를 달랜 그룹도", "v", "42904", {"in": 9.8}),                                           # (50)
 ("딴생각을 한 그룹도 아닌", "v", "26090", {"in": 8.4}),
 ("불안해라고", "card", None, {}),                                                               # (51)
 ("내 감정에 정확한 이름을 붙이는 순간", "icon", "siren_calm", {"at": ["흥분해 있던 뇌의 경보 장치가"]}),
 ("답장이 없어 마음이 요동칠 땐", "v", "42270", {"in": 1.0, "grade": BRIGHT}),
 ("휴대폰 메모장을 열어", "v", "4915", {"in": 14.0, "grade": DARK}),
 ("6시 30분에 보낸 카톡이", "card", None, {}),                                                 # (52)
 # ⑨ 해결책 2: 확인 시간의 주도권, 만약-그러면
 ("둘째", "card", None, {"label": "2 / 3"}),
 ("행동경제학자", "photo", "ariely_v2", {}),                                         # (53) the owner's photo
 ("스마트폰 사용자를 대상으로", "v", "39780", {"in": 1.0, "grade": BRIGHT, "blur_box": [[0.75, 0.24, 0.935, 0.67, 8]]}),
 ("흔히 알림을 아예 꺼 두면", "icon", "bell_off", {"at": ["흔히 알림을 아예 꺼 두면"], "at_shift": [0.8]}),
 ("알림을 완전히 끈 사람들은", "v", "8744", {"in": 1.0, "grade": BRIGHT}),
 ("대신 오전 9시", "icon", "clocks3", {"at": ["대신 오전 9시", "오후 3시", "밤 9시."], "at_shift": [0.3, 0, 0]}),
 ("휴대폰 화면을 열어 보는 횟수가", "v", "4938", {"in": 1.0, "grade": BRIGHT}),
 ("일상에 더 깊이 집중할 수 있었고", "v", "4761", {"in": 1.0, "grade": BRIGHT}),
 ("하지만 막상 시간을 정해 둬도", "v", "41638", {"in": 1.0, "grade": DARK}),
 ("휴대폰을 확인하고 싶은 유혹이", "v", "100053", {"in": 6.0, "grade": BRIGHT}),
 ("이럴 땐", "card", None, {}),
 ("막연하게 '참아야지' 다짐하는 것보다", "v", "4517", {"in": 1.0, "grade": BRIGHT}),
 ("만약 어떤 상황이 오면", "card", None, {}),
 ("구체적인 규칙을 미리 정해 두면", "icon", "ifthen", {"at": ["성공 확률이 비약적으로 높아집니다."]}),
 ("예를 들어 이렇게 정해 두는 겁니다.", "v", "42655", {"in": 0.0}),
 ("만약 30분이 지나도", "vb", "42655", {"cont": True}),            # (55) the same shot runs on behind the rule
 # ⑩ 해결책 3: 든든한 사람의 사진
 ("셋째", "card", None, {"label": "3 / 3"}),
 ("코넬 대학교에서", "v", "4560", {"in": 8.0, "grade": BRIGHT, "title": "코넬 대학교", "title_size": 150,
     "title_at": "코넬 대학교에서"}),
 ("과거에 속상했던 기억을", "v", "4708", {"in": 6.0, "grade": BRIGHT}),
 ("화면에 띄운 사진을", "v", "41180", {"in": 1.0}),
 ("그 결과", "icon", "bars_mood", {"at": ["자신의 어머니 사진을 본 학생들의"]}),
 ("여기서 주목할 점은", "icon", "order2", {"at": ["사진을 먼저 본 그룹에서는"]}),
 ("즉 이 방법은", "icon", "medkit", {"at": ["예방주사가 아니라", "'마음의 응급약'으로 써야"]}),
 ("만약 기다림에 지쳐", "v", "4511", {"in": 1.0, "grade": BRIGHT}),
 ("답장 없는 그 사람의 프로필 사진을", "v", "4911", {"in": 8.0}),
 ("부모님이나 오랜 친구", "v", "4656", {"in": 1.0, "grade": BRIGHT}),
 ("혹은 반려동물처럼", "v", "101233", {"in": 1.0, "grade": BRIGHT}),
 ("내 마음을 무조건적으로", "v", "4644", {"in": 1.0}),
 # ⑪ 마무리
 ("생각해 보면", "v", "4840", {"in": 1.0}),
 ("어쩌면", "v", "52419", {"in": 1.0, "grade": DARK}),
 ("예상치 못하게 길어진 회의", "v", "4547", {"in": 1.0, "grade": BRIGHT}),
 ("발 디딜 틈 없는 퇴근길 지하철", "v", "1623", {"in": 1.0, "grade": DARK}),
 ("갑자기 꺼져 버린 휴대폰 배터리 같은", "own", 30, {}),                                          # (30) phone off
 ("물론 때로는 아무리 기다려도", "v", "25592", {"in": 1.0, "grade": BRIGHT}),
 ("하지만 그건", "v", "51395", {"in": 8.0}),
 ("어쩌면 답장 하나에", "card", None, {}),                                                      # (56) no background
 ("여러분들만의", "vb", "100067", {"in": 1.0}),                                                 # (57)
 ("댓글로 공유해 주세요.", "vb", "100050", {"in": 6.0}),
]
PATCHED = {"39789p": "Mixkit 39789, phone logo painted out (logo_patch.py via prep_patches.sh)"}
OWNER = {"bowlby_v2": "owner's photo of John Bowlby (make_photos_v2.py, not committed)",
         "ariely_v2": "owner's photo of Dan Ariely (make_photos_v2.py, not committed)"}
SUBST = json.load(open(f"{F}/stock_choices.json")) if os.path.exists(f"{F}/stock_choices.json") else {}

scenes, pos = [], -1
idx = {o["id"]: k for k, o in enumerate(lines)}
for i, (first, kind, mat, extra) in enumerate(PLAN):
    sid = f"{i + 1:03d}"
    x = {k: v for k, v in extra.items() if k not in ("at", "title_at", "cont_zoom", "overlay", "mix", "panels")}
    sc = {"id": sid, "from": L(first, pos + 1)}
    pos = idx[sc["from"]]
    if kind in ("v", "vb"):
        mat = SUBST.get(mat, mat)
        sc.update(type="video", src=f"work/stock/full/{mat}.mp4", note=PATCHED.get(mat, f"Mixkit {mat}"), **x)
        if kind == "vb":
            sc.update(grade=BLURBG, blur=BLUR, use="blurred background under centre text")
    elif kind in ("ai", "photo", "own"):
        if kind == "own":
            img, note, base = f"work/owner_v3/{mat:02d}.png", f"owner's photo {mat} (make_photos_v3.py, not committed)", \
                {"grade": OWN, **OWN_ZOOM}
        else:
            img = f"work/img/{mat}.png" if (kind == "photo" or "_s" in mat) else f"work/img/{mat}_s1.png"
            note, base = OWNER.get(mat, f"AI {mat} (ai_images.json)"), ZOOM
        sc.update(type="photo", image=img, note=note, **{**base, **x})
        if "overlay" in extra:
            sc["overlay"] = dict(extra["overlay"], at=[L(a, pos) for a in extra["overlay"]["at"]])
        if "mix" in extra:
            sc["mix"] = dict(extra["mix"], at=L(extra["mix"]["at"], pos))
        if extra.get("cont_zoom"):              # the same photo goes on: start where the previous scene's zoom ended
            p = scenes[-1]
            d = T[sc["from"]] - T[p["from"]]
            sc["z0"] = round(min(1.05, p.get("z0", 1.0) * (1 + p["zoom_rate"] * d)), 4)
    elif kind == "split":
        panels = []
        for p in extra["panels"]:
            q = {k: v for k, v in p.items() if k not in ("own", "at")}
            q.update(image=f"work/owner_v3/{p['own']:02d}.png", grade=p.get("grade", OWN))
            if "at" in p:
                q["at"] = L(p["at"], pos)
            panels.append(q)
        sc.update(type="split", panels=panels, note="owner's photos " + " + ".join(str(p["own"]) for p in extra["panels"]))
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
    if o["kind"] == "bubble":            # shown only inside the picture (chat bubble): no subtitle, but the
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
# sub_lead 0.017 s = half a frame: render.py shows a line from the first frame at or after its start, so a line now
# appears on the frame nearest to the first sound of its first syllable (onsets_v2.py) instead of up to 33 ms after
spec = {"note": "paths are relative to VIDEO_ROOT (venv/, models/, work/); build_spec_v3.py also writes work/v3/spec_abs.json",
        "fade_in": 0.3, "fade_out": 0.5, "sub_lead": 0.017, "scenes": scenes, "subs": subs}
json.dump(spec, open(f"{F}/spec_v3.json", "w"), ensure_ascii=False, indent=1)
missing = []
spec = json.loads(json.dumps(spec))      # deep copy: the absolute paths go only into spec_abs.json
for sc in spec["scenes"]:
    holders = [sc] + sc.get("panels", []) + ([sc["mix"]] if "mix" in sc else [])
    for h in holders:
        for k in ("src", "image"):
            if k in h:
                h[k] = os.path.join(VR, h[k])
                if not os.path.exists(h[k]):
                    missing.append(h[k])
os.makedirs(f"{VR}/work/v3", exist_ok=True)
json.dump(spec, open(f"{VR}/work/v3/spec_abs.json", "w"), ensure_ascii=False, indent=1)
kinds = {}
for sc in spec["scenes"]:
    kinds[sc["type"]] = kinds.get(sc["type"], 0) + 1
print(len(scenes), "scenes", kinds, "|", len(subs), "subtitle lines |", len(missing), "files missing")
for m in missing:
    print("  missing", m)
