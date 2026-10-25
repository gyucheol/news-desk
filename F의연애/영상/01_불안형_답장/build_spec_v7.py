# 01편 장면 명세 v7 (2026-10-25, the owner's v7 list 1-12): v6's plan (notes below) with the owner's changes, placed on
# the v7 lines and times (lines_v7.json, lines_align_v7.json). Comments "(v7 N)" give the item. What changes:
# - (v7 1) "먼저 첫 번째" 대본 나올 때 배경은 없고 중앙에 자막 뜨게: a black card with the line in the centre; the first
#   chat screen (title 첫 번째, as the other two screens) comes with the next line.
# - (v7 3) "아마 세번째 였을 겁니다~ 기약없이 기다리고 있으니까요" 대본 나올 때 세번째 카톡창만 노란색으로: the third of the
#   three chats has the yellow outline (panels3 "focus") for the whole scene, '아마 대부분' to '…기다리고 있으니까요.'.
#   The other two keep their grey outline and nothing moves (v4 5 asked to take out the outline that went from chat to
#   chat: "카톡바 선택되는 효과 다 지워줘").
# - (v7 4) the scenes of '밤 11시 50분 … 나란히 떠 있습니다.' are gone with their lines (edit_narration_v7.py).
# - (v7 5) the centre lines '도대체 왜 / 작은 숫자 1 하나에' over the owner's attached "0-6" photo and '우리의 평온했던
#   일상이 / 이토록 쉽게 무너져 내리는 걸까요?' over the attached "7" (they were on a black card). The attached files are
#   the same files as photo 9 of the first set (the v4 list called it "첨부 0-6") and photo 7 of the second set (md5
#   checked, credits_v7.md 3장). Centre text over a photo: softened (DIMMED), as everywhere since v3.
# - (v7 6) '몇 시간 내내' takes the photo of '홀로 들여다보고 있는 셈입니다.' (second set 18) instead of the clip 31413.
# - (v7 7) the subtitles of '무리에 받아들여졌다는 … 무너져 내렸습니다.' are bottom lines now (subtitles_v7.txt), so the
#   소속감/통제감/자존감 drawing goes back to its own place and size in the middle (v3's, no lift; the arrows full size,
#   "너가 만들어준 자료는 중앙에 올 수 있도록"). '절반 이하' stays out (the subtitle says it, CLAUDE.md rule 15).
# - (v7 8) '하지만 그건 적응한 게 아니라' takes the photo of '아무리 불러도 엄마가 오지 않자' (second set 21) instead of the
#   AI picture B02.
# - (v7 10) photo 7 of the first set (지우 on the subway): the typed words in the chat's input box are softened
#   (make_photos_v7.py, work/owner_v7/07.png), "그게 약간 ai티가 많이 나. 그거를 약간 뿌옇게". The owner pointed at
#   '지우가 줄어들지 않는 숫자 1을 보며'; the same photo also shows at '휴대폰을 꺼내', so it is the softened one there too.
# - (v7 11) '어쩌면 답장 하나에 / 이토록 쉽게 불안해지는 마음은' over the attached "28" (= photo 28 of the second set, md5
#   checked) instead of the black card. The centre lines after them keep the photo, softened, as v4 did wherever centre
#   text followed a picture (CLAUDE.md rule 15: carry the previous picture on under centre text).
# usage: build_spec_v7.py <episode folder> <VIDEO_ROOT>
# --- v6 notes ---
# 01편 장면 명세 v6 (2026-10-25, the owner's new recordings 1-8): v5's plan unchanged (notes below), placed on the v6
# lines and times (lines_v6.json, lines_align_v6.json). Every scene starts at a line, so the scenes follow the new
# narration; fit_clips.py then fits the clips to the new scene lengths.
# (v6 usage: build_spec_v6.py <episode folder> <VIDEO_ROOT>)
# --- v5 notes ---
# 01편 장면 명세 v5 (2026-10-25, the owner's v5 request): v4's plan (build_spec_v4.py, its notes are kept below) with
# the owner's second set of AI photos put where the script of this request marks them: "<대사>(N)" -> photo N of the
# new set (work/owner_v5/NN.png from make_photos_v5.py, kind "own5"; the first set from v3 stays "own",
# work/owner_v3/NN.png). The owner: "대본 중에 여러 부분을 너가 만든 ai 그림 및 스톡 영상말고, 내가 만든 ai 사진으로
# 대체 할꺼야. … 대체하는 대사 부분은 < >으로 묶은 다음 옆에 (1), (2)이런식으로 번호를 매겨놨어. 바꿔주면 돼."
# As in v3, a photo shows from its first marked line until the next scene (the next marked line, or the scene v4 had
# after the marked words); lines without a mark keep v4's picture. Comments "(v5 N)" give the owner's new photo
# number (1-30; there is no 14, and 27 is used twice: "(27 사진 재사용)").
# - Centre text over a new photo: the photo lightly blurred and darker (OWN_DIM, blur 6), as for the first set.
#   Photo 27, the owner: "27번 사진이 나올때는 사진 약간 흐리게 +자막 중앙에 나오게 편집": both of its places are
#   centre text ('참가자들에게 …' already was; '일주일 뒤 … 어디였을까요?' moved to the centre in subtitles_v5.txt).
# - (2) runs on, softened, under '오늘 퇴근하고 뭐할꺼야?' (v4 1: that line keeps the previous picture).
# - (29) is soft under the two centre lines of the if-then rule and comes into focus at '구체적인 규칙을' (bottom).
# (v5 usage: build_spec_v5.py <episode folder> <VIDEO_ROOT>)
# --- v4 notes ---
# 01편 장면 명세 v4 (2026-10-25, the owner's v4 list 1-52): lines_v4.json + the plan below -> spec_v4.json (paths
# relative to VIDEO_ROOT) and work/v4/spec_abs.json (absolute paths, for build_timeline.py).
# The plan is v3's (build_spec_v3.py) with the owner's v4 list; comments "(v4 N)" give the item. What is new:
# - "soft": the scene's own shot (stock or photo) runs on under centre text, softened (blurred and a little darker, as
#   under all centre text since v2) from that line and, with "until", sharp again from the next bottom line
#   (render.py "mix" on a video or photo scene). The owner: "바로 앞 장면에서 사용한 사진을 그대로 이어받아서 화면
#   중앙에 대본 적는 걸로 편집" (v4 1, 7, 8, 9, 10, 11, 20, 21, 24, 25, 52);
# - lines moved to the centre over a stock shot ("자막을 중앙에 위치하게 편집") keep their shot, softened in the same
#   way ("vs" for a whole scene, "soft" from the first centre line);
# - "icon_overlay": an icon screen drawn over the softened shot (v4 20: 소속감 / 통제감 / 자존감 with the centre text,
#   the words and arrows lifted above the text; its yellow '절반 이하' is left out: it fell right under the centre
#   subtitle and read as the yellow subtitle emphasis the owner asked to remove, v4 35);
# - the owner's photos sent again with this list ("첨부 0" .. "첨부 0-6") are photos they had already sent (same
#   files): 0-5 = photo 30, 0-6 = photo 9 (sent in that order in a second message); the first message's five came in
#   the order 22, 3, 2, 28, 7 and are read by what they show and where they go (credits_v4.md 5장): 0 = photo 7
#   (지우 with the chat on the subway, for '지우가 … 카톡창을 들락날락'), 0-1 = photo 28 (nurse holding a child, for
#   '어릴 적 로라의 마음속에서'), 0-2 = photo 2 (phone in the dark), 0-3 = photo 3 (on the floor, head in hands, for
#   '우울해지는'/'가라앉았다면'), 0-4 = photo 22 (head in hand by a phone, for '왜 연락이 없지?');
# - centre text over an owner's photo: OWN_DIM + blur 6 as in v3.
# (v4 usage: build_spec_v4.py <episode folder> <VIDEO_ROOT>)
import json, os, re, sys

F, VR = sys.argv[1], sys.argv[2]
lines = json.load(open(f"{F}/lines_v7.json"))
T = {a["id"]: a["start"] for a in json.load(open(f"{F}/lines_align_v7.json"))}
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
# v3: the owner's photos are already dark and muted; only a light touch so they sit with the graded stock
OWN = {"sat": 0.95, "black": 0.01, "gamma": 1.05, "vignette": 0.3}
OWN_DIM = {"sat": 0.85, "black": 0.05, "gamma": 1.45, "vignette": 0.55}      # under centre text, with blur OWN_BLUR
OWN_BLUR = 6
OWN_ZOOM = {"z0": 1.0, "zoom_rate": 0.008}
DIMMED = {"grade": OWN_DIM, "blur": OWN_BLUR}
# v4 "soft": the change starts 0.25 s before the centre line's voice and takes 0.5 s (and the same back at "until").
# On a stock shot the softened look is the shot's own grade a little darker (gamma x1.15, black +0.02) and blurred 10:
# with BLURBG (v2's blurred background) the dark shot under '바쁘세요??' went nearly black, and the owner asked for the
# same picture to run on ("그대로 이어받아서"), so it has to stay recognisable.
SOFT_TIME = {"dur": 0.5, "shift": -0.25, "until_shift": -0.25}
SOFT_P = dict(SOFT_TIME, grade=OWN_DIM, blur=OWN_BLUR)
DEFAULT_GRADE = {"sat": 0.88, "black": 0.02, "gamma": 1.12, "vignette": 0.35}      # render.py's, when a scene has none


def soft_v(g):
    g = g or DEFAULT_GRADE
    return dict(SOFT_TIME, blur=10, grade={"sat": round(g["sat"] * 0.95, 3), "black": round(g["black"] + 0.02, 3),
                                           "gamma": round(g["gamma"] * 1.15, 3), "vignette": max(g["vignette"], 0.5)})

KAKAO_ME = lambda text, time, **k: dict(me=True, text=text, time=time, **k)
MY1 = "오늘 퇴근하고 뭐할꺼야?"
MY2 = "오늘 하루 어땠어요?"

# (first line, kind, material, extra)   kind: v = Mixkit clip id, vb = clip as a blurred, darker background under
# centre text, vs = clip softened (its own grade a little darker, blur 10) under centre text (v4), card, icon,
# ai = AI photo id (work/img/<id>_s1.png), photo = work/img/<name>.png,
# own = the owner's photo number (work/owner_v3/NN.png), own5 = the owner's second set (v5, work/owner_v5/NN.png), split = two owner's photos side by side ("panels")
# split screen panels: 956x1080 (render.py panel_size) cut from the middle of the 1984x1116 photo, around the monitor
# (its centre measured at x 996): 988 x 1116 has the panel's shape
PANEL_CROP = [502, 0, 1490, 1116]
PLAN = [
 # ① 도입
 ("금요일 저녁 7시 퇴근길에", "own5", 1, {}),                                           # (v5 1) a crosswalk at dusk
 # (v5 2) typing the message; (v4 1) the message is centre text over the same picture, softened
 ("당신은 애인에게 카톡을 보냅니다.", "own5", 2, {"soft": "오늘 퇴근하고 뭐할꺼야?"}),
 ("이 메시지를 보낸 뒤", "own5", 3, {}),                                                # (v5 3) three phones
 ("먼저 첫 번째", "card", None, {}),                         # (v7 1) black, the line in the centre
 # kakao (1, 2, 20, 22): no entrance effect and no yellow glow behind the 1 (icons_chat.py v2); titles white, larger
 ("당신이 카톡을 보낸 지", "icon", "kakao", {"args": {"title": "첫 번째", "msgs": [
     KAKAO_ME(MY1, "오후 7:00", read=0),
     {"me": False, "text": "뭐 할껀 없어, 같이 저녁 먹을까?", "time": "오후 7:05", "show": 1}]},
     "at": ["상대방의 답장이 옵니다.", "뭐 할껀 없어"]}),
 ("두 번째", "icon", "kakao", {"args": {"title": "두 번째", "msgs": [
     KAKAO_ME(MY1, "오후 7:00", read=0),
     {"me": False, "text": "헉 미안해..ㅜ회식 와서 연락을 이제 봤네", "time": "오후 10:14", "show": 1}]},
     "at": ["뒤늦게 답장이 도착합니다.", "헉 미안해"]}),
 # (v4 3) laid out as two messages, so the title and the bubble stand where they stand on the first two screens
 ("그리고 마지막 세 번째", "icon", "kakao", {"args": {"title": "세 번째", "slots": 2,
     "msgs": [KAKAO_ME(MY1, "오후 7:00")]}}),
 ("여러분은 어떤 상황에", "own5", 4, dict(DIMMED)),                                     # (v5 4) a hand on the third phone
 # (v4 4, 5) the three chats only: no 첫 번째/두 번째/세 번째 above, no '5분 만에 답장'/'3시간 뒤 답장'; (v7 3) the third
 # chat outlined in yellow from the first line of the scene to its end (v4 5: no outline moving from chat to chat)
 ("아마 대부분", "icon", "panels3", {"args": {"titles": False, "labels": False, "focus": [[0, 2]]}, "at": ["아마 대부분"]}),
 ("문제는", "card", None, {}),
 ("처음 1~2시간은", "v", "4548", {"in": 2.0, "grade": VBRIGHT}),
 ("야근이 길어지나?", "own5", 5, dict(DIMMED)),                                         # (v5 5) late at the office
 ("배터리가 없나?", "own5", 6, dict(DIMMED)),                                           # (v5 6) a flat battery
 ("대수롭지 않게 넘깁니다.", "v", "26092", {"in": 1.0, "grade": DARK}),
 ("하지만 3시간 4시간이 넘어가면", "own", 1, {}),                                               # (1) wall clock
 ("5분마다 습관처럼", "own", 2, {}),                                                            # (2) phone at night
 ("이제 퇴근해서 집 갔을 텐데", "card", None, {}),
 ("온갖 부정적인 상상을 펼칩니다.", "v", "51394", {"in": 12.0}),
 ("그러다 문득", "own5", 7, {}),                                                       # (v5 7) in bed, the phone on the face
 # (3) centre text over it; (v4 6) '자신을 탓합니다.' is centre text too, so the photo stays soft to the end
 ("고작 연락 몇 시간 안 된다고", "own", 3, dict(DIMMED)),
 ("하지만 이게 정말", "card", None, {}),
 ("심리학은 아니라고 대답합니다.", "own5", 8, dict(DIMMED)),                             # (v5 8) a psychology book
 ("원래 인간의 뇌는", "own", 4, {"cy0": 0.47, "cy1": 0.47,                                       # (4) brain explainer
     "overlay": {"kind": "brain_unknown", "at": ["'알 수 없는 상태'를", "훨씬 더 무겁고", "위협적으로 받아들이도록"]},
     "mix": {"at": "위협적으로 받아들이도록", "image": "work/owner_v3/04_red.png", "dur": 0.6}}),
 ("오늘은 답장이 늦어질 때", "own5", 9, {}),                                           # (v5 9) ripples in a glass of water
 ("답장을 기다리는 시간을", "v", "4897", {"in": 1.0, "grade": BRIGHT}),
 ("3가지 현실적인 방법을", "own5", 10, {}),                                            # (v5 10) the desk: memo, phone, photo
 # ② 공감 사례: 지우
 ("지우는 2주째", "own", 5, {}),                                                                # (5)
 ("오후 6시 30분", "own", 6, {}),                                                                # (6)
 ("휴대폰을 꺼내", "own", 7, {"soft": "오늘 하루 어땠어요?"}),                                  # (7), (v4 7)
 ("집에 도착해 저녁을 먹고", "own", 8, {}),                                                       # (8)
 ("7시가 훌쩍 넘었는데도", "v", "39826", {"in": 0.0, "crop": [0.15, 0.3, 0.85, 1.0],             # (v4 8)
     "soft": "메시지 옆 숫자 1은 그대로입니다."}),
 ("8시가 되자", "own", 9, {}),                                                                   # (9) profile photo
 ("그렇게 9시가 되고", "own", 10, {}),                                                           # (10) 9:00
 ("메시지 하나를 더 보냅니다.", "v", "43381", {"in": 8.0, "soft": "바쁘세요??"}),                 # (v4 9)
 ("전송 버튼을 누르자마자", "v", "4708", {"in": 2.5, "grade": BRIGHT,                            # (v4 10)
     "soft": "내가 연락을 너무 재촉하는 것처럼"}),
 ("9시 반이 되자", "v", "39789p", {"in": 0.0}),
 ("어제 내가 한 그 농담이", "own5", 11, dict(DIMMED)),                                  # (v5 11) scrolling back the chat
 # (v7 4) '밤 11시 50분' (v4 11, clip 51394) and '그렇게 보낸 3줄의 메시지 옆에' (v5 12) are gone with their lines
 ("아마 많은 분들이", "v", "51399", {"in": 7.8}),                     # 7.8-11.3 s: inside the calm stretch 6.0-11.4
 ("도대체 왜", "own", 9, dict(DIMMED)),                    # (v7 5) attached "0-6" = photo 9 (profile photo), centre
 ("우리의 평온했던 일상이", "own5", 7, dict(DIMMED)),       # (v7 5) attached "7" = second set 7 (in bed), centre
 # ③ 원인 1: 유니버시티 칼리지 런던, 뱀과 바위
 ("그 이유를 찾기 위해", "v", "4457", {"in": 1.0, "grade": DARK, "title": "영국", "title_sub": "유니버시티 칼리지 런던",
     "title_size": 150, "title_at": "영국 유니버시티 칼리지 런던의"}),
 ("지금 여러분은", "own", 11, {}),                                                               # (11) the lab
 ("여러분의 왼쪽 손등에는", "own", 12, {}),                                                      # (12) the electrode
 ("이건 실험 전에", "own5", 13, dict(DIMMED)),                                          # (v5 13) the shock box being set
 ("눈앞의 큰 화면에", "own", 13, {"zoom_rate": 0.005}),            # (13) two rocks, (v4 12) on through 여러분은 그중
 ("밑에 뱀이 없는 바위를 골라야 합니다.", "own", 14, {"zoom_rate": 0.005, "cont_zoom": True}),   # (14) 13-14-15 are
 ("만약 바위 밑에서 뱀이 나오면", "own", 15, {"zoom_rate": 0.005, "cont_zoom": True}),           # (15) one slow zoom
 ("이 과정을 무려", "own5", 15, {}),                                                   # (v5 15) the rocks on a monitor, 320
 ("연구진은", "own5", 16, {}),                                                        # (v5 16) a researcher, eye and traces
 ("긴장할 때 저절로 커지는", "own", 17, {}),                                                      # (17) the eye
 ("손끝에 맺히는", "own", 18, {}),                                                               # (18) sweaty hand
 ("그리고 참가자들이 스스로 매긴", "own", 19, {}),                                               # (19) stress score
 ("과연 참가자들은", "card", None, {}),                                                         # (25)
 # (v4 13) sides swapped, the left first: photo 15 on the left from 뱀이 나와서, photo 13 on the right from 아니면
 ("뱀이 나와서", "split", None, {"panels": [
     {"side": "left", "own": 15, "crop": PANEL_CROP, "cx": 0.5, "cy": 0.32},
     {"side": "right", "own": 13, "crop": PANEL_CROP, "cx": 0.5, "cy": 0.32, "at": "아니면 나올지 안 나올지"}]}),
 ("놀랍게도 정답은", "card", None, {}),
 ("우리 몸의 긴장도는", "own5", 17, {}),                                               # (v5 17) the curve, highest at 50%
 ("한마디로 우리의 뇌는", "own", 4, dict(DIMMED, cy0=0.47, cy1=0.47)),                            # (v4 14) the brain
 ("아플지 안 아플지 모르는 상태를", "own", 13, dict(DIMMED)),                                     # (v4 15) photo 13
 ("심리학에서는 이처럼", "v", "51390", {"in": 5.0, "grade": LIFT, "title": "불확실성", "title_size": 200,   # (26)
     "title_at": "'불확실성'이라고 부릅니다."}),
 ("비록 카톡을 주고받는 실험은 아니었지만", "v", "43381", {"in": 10.0}),                          # (27)
 ("이 실험 속 바위와", "own", 13, {}),                                                            # (13) again
 ("상대가 그저", "vs", "4809", {"in": 1.0, "grade": BRIGHT}),   # (v4 16) centre
 ("나에 대한 마음이", "vs", "101412", {"in": 1.0}),
 ("답장을 기다리는 우리는", "v", "51429", {"in": 2.0}),
 ("밑에 뱀이 있을지 없을지 모르는 바위를", "own", 13, {}),                                         # (v4 17) photo 13
 ("몇 시간 내내", "own5", 18, {}),        # (v5 18) alone before a rock; (v7 6) from '몇 시간 내내' (was clip 31413)
 # ④ 원인 2: 매쿼리 대학교, 노키아 3310
 ("게다가 이렇게", "own5", 19, {}),                                                    # (v5 19) an empty bed, the phone
 ("우리의 뇌는", "vs", "51390", {"in": 16.0}),   # (v4 18) centre
 ("2004년", "v", "AUS", {"in": 1.0, "grade": DARK, "title": "2004년", "title_sub": "호주 매쿼리 대학교",
     "title_size": 170, "title_at": "2004년"}),
 ("실험에 참가한 학생은", "own", 20, {}),                                                         # (20) Nokia 3310
 ("운동은 얼마나 자주 해요?", "vb", "100530", {"in": 1.0}),                                     # (29)
 ("곧 편하게 이야기를 나누는", "v", "51121", {"in": 0.5}),                                     # (30)
 ("그런데 어떤 학생들에게는", "vs", "28321", {"in": 1.0, "grade": DARK}),   # (v4 19) centre
 ("장장 8분 동안", "own5", 20, {}),                                                    # (v5 20) Nokia 3310 and a stopwatch
 ("사실 대화 상대였던 두 사람은", "v", "39958", {"in": 1.0, "grade": BRIGHT}),
 ("그 정적 같은 8분이 흐른 뒤", "vb", "8757", {"in": 0.0}),                                   # (31)
 # (v4 20) the shot runs on, softened, with the 소속감/통제감/자존감 drawing over it; (v7 7) the subtitles at the bottom,
 # the drawing in the middle at v3's place and size (no lift, full arrows), still without '절반 이하'
 ("계속 대화를 이어 간 학생들에 비해", "v", "4560", {"in": 1.0, "grade": BRIGHT, "soft": "무리에 받아들여졌다는",
     "icon_overlay": {"kind": "drops3", "from": "무리에 받아들여졌다는", "at": ["'소속감' 점수가", "'통제감'", "'자존감'까지"],
                      "args": {"note": False}}}),
 ("더 눈여겨볼 점은 그다음입니다.", "card", None, {}),
 ("실험이 끝난 뒤", "v", "99890", {"in": 1.0}),
 ("'휴대폰 고장' 같은", "own", 21, {}),                                                           # (21) broken phone
 ("내가 말을 재미없게 했나?", "own", 22, dict(DIMMED)),                    # (22) centre text, (v4 21) on through 가장
 ("생판 처음 본 사람에게", "v", "8743", {"in": 1.0, "grade": DARK}),       #      많았습니다 (centre text too)
 ("사람의 마음은", "vs", "8739", {"in": 1.0}),   # (v4 22) centre
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
 # (v4 23) '아무리 불러도 엄마가 오지 않자 …' are bottom lines again: the picture runs on as it is (v3 blurred it)
 # (v5 21) Laura alone on the bed; (v7 8) from '하지만 그건 적응한 게 아니라' (was the AI picture B02)
 ("하지만 그건 적응한 게 아니라", "own5", 21, {}),
 ("실제로 간호사가 다정하게 다가와 말을 걸자", "own", 28, {}),                                    # (28)
 ("존 볼비는", "v", "40421", {"in": 1.0, "grade": BRIGHT, "title": "애착", "title_size": 230,
     "title_at": "'애착'이라는 개념으로 설명했습니다."}),
 ("인간의 마음속에는", "icon", "siren", {}),
 ("내가 의지하는 사람이", "v", "939", {"in": 1.0, "grade": DARK,                                  # (v4 24) no siren
     "soft": "뇌는 즉시 비상벨을 울립니다."}),
 ("처음에는 로라가 울부짖었듯", "v", "51429", {"in": 8.0}),
 ("침묵이 길어지면", "v", "4500", {"in": 1.0, "grade": BRIGHT, "soft": "결국 깊은 무기력과 우울함에"}),   # (v4 25)
 ("문제는", "card", None, {}),                                                                  # (36), (v4 26)
 ("성인이 된 후에는", "v", "PARENT", {"in": 1.0, "grade": BRIGHT}),
 ("고스란히 '연인'이나", "v", "4624", {"in": 1.0, "grade": BRIGHT}),
 ("지우가 줄어들지 않는 숫자 '1'을 보며", "own", 7, {}),                       # (v4 27) 첨부 0 = photo 7 (지우)
 ("결국 불 꺼진 방에서", "v", "25586", {"in": 0.5, "grade": DARK}),         # (37) alone on the floor of a dark room
 ("어릴 적 로라의 마음속에서", "own", 28, dict(DIMMED)),           # (v4 28) 첨부 0-1 = photo 28, centre, no siren
 # ⑥ 개인차: 경보 장치의 예민함
 ("그런데 참 신기하죠", "card", None, {}),                                                        # (v4 29)
 ("모든 사람에게", "v", "4401", {"in": 2.65, "grade": DARK, "crop": [0.075, 0.15, 0.925, 1.0]}),
 ("누군가는 편하게 쉬며 일상을 보내고", "v", "26091", {"in": 1.0}),
 ("누군가는 지우처럼 피 말리는 밤을", "v", "51394", {"in": 32.5}),
 ("그 이유는", "card", None, {}),                                                               # (38)
 ("심리학 연구들을 살펴보면", "icon", "people5", {"args": {"caption": False},                     # (v4 30)
     "at": ["성인 5명 중 1명꼴로는"]}),
 ("이런 분들은", "own", 2, {}),                                                   # (v4 31) 첨부 0-2 = photo 2
 ("단순히 기분만 우울해지는 게 아니라", "own", 3, {}),                            # (v4 32) 첨부 0-3 = photo 3
 ("실제로 몸속 스트레스 호르몬 수치가", "icon", "gauge", {}),
 ("밤잠까지 설치는", "v", "51394", {"in": 28.0}),
 ("상대의 의도를 알 수 없는", "own5", 22, dict(DIMMED)),                                # (39), (v5 22) a cafe, the empty chair
 ("예민한 경보 장치가", "icon", "siren", {}),
 ("왜 연락이 없지?", "own", 22, dict(DIMMED)),                                    # (v4 33) 첨부 0-4 = photo 22
 ("최악의 시나리오를", "v", "4700", {"in": 1.0, "grade": BRIGHT}),
 # ⑦ 희망과 해결책 소개
 ("하지만", "card", None, {}),                                                                   # (40)
 ("수십 년간", "own5", 23, {}),                                                        # (v5 23) an archive of dated files
 ("나이가 들고 경험이 쌓일수록", "own", 29, dict(DIMMED)),                         # (29), (v4 34) centre
 ("또 나와 잘 맞는", "vs", "4764", {"in": 1.0, "grade": BRIGHT}),
 ("타고난 마음의 경보 장치가", "v", "4800", {"in": 1.0}),
 ("우리가 어떻게 다루느냐에 따라", "v", "4897", {"in": 8.0, "grade": BRIGHT}),
 ("그렇다면", "vs", "31413", {"in": 7.5}),   # v6: read without 자   # (41), (v4 36) centre: tonight, in bed, the phone
 ("요동치는 우리 마음을", "vs", "42904", {"in": 6.0}),   #      ... and a slow breath (다독여야)
 ("과학적으로 검증된", "card", None, {}),                                                       # (42)
 # ⑧ 해결책 1: 이름 붙이기 (v4 45: no '1 / 3' label on the item cards)
 ("첫째", "card", None, {}),                                                                     # (v4 37) 첫째,
 ("애써 괜찮아라고 본인을 다독이는 대신", "own5", 24, dict(DIMMED)),                     # (v5 24) a hand on the chest
 ("차라리 나 지금 불안해라고", "own5", 25, dict(DIMMED)),                                 # (v5 25) open hands
 ("2012년 키르칸스키 연구팀은", "own5", 26, {}),                                       # (v5 26) the covered box in a lab
 ("그리고는 살아 움직이는 거대한 독거미", "icon", "spider_60", {"at": ["불과 60cm 떨어진 자리에 앉혔죠."]}),
 ("참가자들에게", "own5", 27, dict(DIMMED)),                                           # (44), (v5 27) facing the tarantula
 ("그룹마다 각기 다른 말을", "vs", "43396", {"in": 2.0}),   # (45), (v4 38)
 ("첫 번째 그룹은", "vb", "43404", {"in": 0.0}),                                                # (46)
 ("두 번째 그룹은", "vb", "42903", {"in": 17.0}),                                               # (47)
 ("세 번째 그룹은", "vb", "3110", {"in": 7.9}),                                                 # (48)
 ("일주일 뒤", "own5", 27, dict(DIMMED)),                                              # (v5 27 again) centre text
 ("스스로를 달랜 그룹도", "v", "42904", {"in": 9.8}),                                           # (50)
 ("딴생각을 한 그룹도 아닌", "v", "26090", {"in": 8.4}),
 ('"불안해"라고', "card", None, {}),                                                             # (51), (v4 39)
 ("내 감정에 정확한 이름을 붙이는 순간", "own5", 28, {}),                               # (v5 28) a tag that says 불안
 ("답장이 없어 마음이 요동칠 땐", "v", "42270", {"in": 1.0, "grade": BRIGHT}),
 ("휴대폰 메모장을 열어", "vs", "4915", {"in": 14.0, "grade": DARK}),   # (v4 40) centre
 ("6시 30분에 보낸 카톡이", "own", 2, dict(DIMMED)),                              # (52), (v4 41) 첨부 0-2 = photo 2
 # ⑨ 해결책 2: 확인 시간의 주도권, 만약-그러면
 ("둘째", "card", None, {}),
 ("휴대폰을 언제 확인할지", "own", 30, dict(DIMMED)),                             # (v4 42) 첨부 0-5 = photo 30
 ("행동경제학자", "photo", "ariely_v2", {}),                                         # (53) the owner's photo
 ("스마트폰 사용자를 대상으로", "v", "39780", {"in": 1.0, "grade": BRIGHT, "blur_box": [[0.75, 0.24, 0.935, 0.67, 8]]}),
 ("흔히 알림을 아예 꺼 두면", "icon", "bell_off", {"at": ["흔히 알림을 아예 꺼 두면"], "at_shift": [0.8]}),
 ("알림을 완전히 끈 사람들은", "vs", "8744", {"in": 1.0, "grade": BRIGHT}),   # (v4 43) centre
 ("대신 오전 9시", "icon", "clocks3", {"at": ["대신 오전 9시", "오후 3시", "밤 9시."], "at_shift": [0.3, 0, 0]}),
 ("휴대폰 화면을 열어 보는 횟수가", "vs", "4938", {"in": 1.0, "grade": BRIGHT}),   # (v4 44) centre
 ("일상에 더 깊이 집중할 수 있었고", "v", "4761", {"in": 1.0, "grade": BRIGHT}),
 ("하지만 막상 시간을 정해 둬도", "v", "41638", {"in": 1.0, "grade": DARK}),
 ("휴대폰을 확인하고 싶은 유혹이", "v", "100053", {"in": 6.0, "grade": BRIGHT}),
 ("이럴 땐", "card", None, {}),
 ("막연하게 '참아야지' 다짐하는 것보다", "v", "4517", {"in": 1.0, "grade": BRIGHT}),
 # (v5 29) the phone going into a drawer: soft under the two centre lines, in focus from the bottom lines
 ("만약 어떤 상황이 오면", "own5", 29, dict(DIMMED, mix={"at": "구체적인 규칙을 미리 정해 두면", "grade": OWN,
     "blur": 0, "dur": 0.5, "shift": -0.25})),
 ("예를 들어 이렇게 정해 두는 겁니다.", "v", "42655", {"in": 0.0}),
 ("만약 30분이 지나도", "vb", "42655", {"cont": True}),            # (55) the same shot runs on behind the rule
 # ⑩ 해결책 3: 든든한 사람의 사진
 ("셋째", "card", None, {}),
 ("이미 마음이 무겁게 가라앉았다면", "own", 3, dict(DIMMED)),                     # (v4 46) 첨부 0-3 = photo 3
 ("나를 무조건적으로 편안하게 해 주는", "own5", 30, dict(DIMMED)),                       # (v5 30) a dog on the phone
 ("코넬 대학교에서", "v", "4560", {"in": 8.0, "grade": BRIGHT, "title": "코넬 대학교", "title_size": 150,
     "title_at": "코넬 대학교에서"}),
 ("과거에 속상했던 기억을", "v", "4708", {"in": 6.0, "grade": BRIGHT}),
 ("화면에 띄운 사진을", "v", "41180", {"in": 1.0}),
 ("그 결과", "icon", "bars_mood", {"at": ["자신의 어머니 사진을 본 학생들의"]}),
 ("여기서 주목할 점은", "icon", "order2", {"at": ["사진을 먼저 본 그룹에서는"]}),
 ("즉 이 방법은", "icon", "medkit", {"at": ["예방주사가 아니라", "'마음의 응급약'으로 써야"]}),
 ("만약 기다림에 지쳐", "v", "4511", {"in": 1.0, "grade": BRIGHT}),
 ("답장 없는 그 사람의 프로필 사진을", "own", 9, {}),                              # (v4 47) 첨부 0-6 = photo 9
 ("부모님이나 오랜 친구", "v", "4656", {"in": 1.0, "grade": BRIGHT}),
 ("혹은 반려동물처럼", "v", "101233", {"in": 1.0, "grade": BRIGHT}),
 ("내 마음을 무조건적으로", "vs", "4644", {"in": 1.0}),   # (v4 48) centre
 # ⑪ 마무리
 ("생각해 보면", "v", "4840", {"in": 1.0, "soft": "나를 향한 마음이 변해서가 아니라"}),           # (v4 49)
 ("어쩌면", "vs", "52419", {"in": 1.0, "grade": DARK}),   # (v4 49) centre
 ("예상치 못하게 길어진 회의", "v", "4547", {"in": 1.0, "grade": BRIGHT}),
 ("발 디딜 틈 없는 퇴근길 지하철", "v", "1623", {"in": 1.0, "grade": DARK}),
 ("갑자기 꺼져 버린 휴대폰 배터리 같은", "own", 30, {"soft": "일상의 바람 말이에요."}),           # (30), (v4 50)
 ("물론 때로는 아무리 기다려도", "v", "25592", {"in": 1.0, "grade": BRIGHT}),
 ("하지만 그건", "v", "51395", {"in": 8.0}),
 # (56) was a black card; (v4 51) its first two lines at the bottom; (v7 11) attached "28" = second set 28 (the tag
 # 불안) under them, softened under the centre lines that follow
 ("어쩌면 답장 하나에", "own5", 28, {"soft": "내가 나약하고 못나서가 아니라"}),
 ("여러분들만의", "vb", "100067", {"in": 1.0}),                    # (57), (v4 52) on through 댓글로 공유해 주세요
]
PATCHED = {"39789p": "Mixkit 39789, phone logo painted out (logo_patch.py via prep_patches.sh)"}
OWN_V7 = {7: ("work/owner_v7/07.png", "owner's photo 7, the typed words in the chat's input box softened (make_photos_v7.py, "
              "not committed)")}
OWNER = {"bowlby_v2": "owner's photo of John Bowlby (make_photos_v2.py, not committed)",
         "ariely_v2": "owner's photo of Dan Ariely (make_photos_v2.py, not committed)"}
SUBST = json.load(open(f"{F}/stock_choices.json")) if os.path.exists(f"{F}/stock_choices.json") else {}
LOCAL = ("at", "title_at", "cont_zoom", "overlay", "mix", "panels", "soft", "icon_overlay")

scenes, pos = [], -1
idx = {o["id"]: k for k, o in enumerate(lines)}
for i, (first, kind, mat, extra) in enumerate(PLAN):
    sid = f"{i + 1:03d}"
    x = {k: v for k, v in extra.items() if k not in LOCAL}
    sc = {"id": sid, "from": L(first, pos + 1)}
    pos = idx[sc["from"]]
    if kind in ("v", "vb", "vs"):
        mat = SUBST.get(mat, mat)
        sc.update(type="video", src=f"work/stock/full/{mat}.mp4", note=PATCHED.get(mat, f"Mixkit {mat}"), **x)
        if kind == "vb":
            sc.update(grade=BLURBG, blur=BLUR, use="blurred background under centre text")
        if kind == "vs":                    # v4: lines moved to the centre keep their shot, softened as under "soft"
            g = soft_v(sc.get("grade"))
            sc.update(grade=g["grade"], blur=g["blur"], use="the shot softened under centre text")
    elif kind in ("ai", "photo", "own", "own5"):
        if kind == "own":
            img, note, base = f"work/owner_v3/{mat:02d}.png", f"owner's photo {mat} (make_photos_v3.py, not committed)", \
                {"grade": OWN, **OWN_ZOOM}
            if mat in OWN_V7:                   # (v7 10) a photo changed in v7
                img, note = OWN_V7[mat]
        elif kind == "own5":                    # v5: the owner's second set, treated as the first
            img, base = f"work/owner_v5/{mat:02d}.png", {"grade": OWN, **OWN_ZOOM}
            note = f"owner's photo {mat}, second set (make_photos_v5.py, not committed)"
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
    if "soft" in extra:                         # v4: the scene's shot softened under its centre line(s)
        s = extra["soft"] if isinstance(extra["soft"], dict) else {"at": extra["soft"]}
        mx = dict(soft_v(sc.get("grade")) if sc["type"] == "video" else SOFT_P, at=L(s["at"], pos))
        if s.get("until"):
            mx["until"] = L(s["until"], pos)
        assert "mix" not in sc, sid
        sc["mix"] = mx
    if "icon_overlay" in extra:                 # v4: an icon screen drawn over the scene from a line on
        ov = extra["icon_overlay"]
        sc["icon_overlay"] = dict(ov, **{"from": L(ov["from"], pos), "at": [L(a, pos) for a in ov.get("at", [])]})
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
spec = {"note": "paths are relative to VIDEO_ROOT (venv/, models/, work/); build_spec_v7.py also writes work/v7/spec_abs.json",
        "fade_in": 0.3, "fade_out": 0.5, "sub_lead": 0.017, "scenes": scenes, "subs": subs}
json.dump(spec, open(f"{F}/spec_v7.json", "w"), ensure_ascii=False, indent=1)
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
os.makedirs(f"{VR}/work/v7", exist_ok=True)
json.dump(spec, open(f"{VR}/work/v7/spec_abs.json", "w"), ensure_ascii=False, indent=1)
kinds = {}
for sc in spec["scenes"]:
    kinds[sc["type"]] = kinds.get(sc["type"], 0) + 1
print(len(scenes), "scenes", kinds, "|", len(subs), "subtitle lines |", len(missing), "files missing")
for m in missing:
    print("  missing", m)
