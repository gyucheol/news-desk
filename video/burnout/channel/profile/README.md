# 채널 프로필 사진 시안 (「INFJ입니다.」, 2026-10-24)

사용자 요청(2026-10-24): "채널 프로필 사진은 또 뭐로할지 알려줘". 채널 문서(handoff_INFJ-imnida_final.md)에는 프로필 사진에 대해 정해 둔 것이 없습니다.

1. 1_text.png: 검은 배경에 흰 "INFJ"와 노란 마침표
   - 마침표는 채널 이름 "INFJ입니다."의 마침표이고, 색은 자막 강조색(#F2C94C)입니다.
   - 글꼴은 썸네일 주제 단어와 같은 Noto Sans KR 굵기 800(OFL)입니다.
2. 2_bulb.png: 영상의 '작은 힌트' 아이콘 화면(scripts/render.py의 bulb, 켜진 상태)에서 전구 둘레를 정사각형으로 자른 그림
3. review_sheet.png: 두 시안을 원형으로 잘라 300px, 98px, 40px로 줄여 밝은 화면과 어두운 화면 위에 놓고 비교한 그림

규격
- 800×800 PNG입니다. 유튜브는 원형으로 잘라 보여 주므로 글자와 그림을 가운데 원 안에 두었습니다.
- 유튜브 도움말(2026-10-24 확인, "Manage your channel branding"): 98×98px로 보이고, JPG·GIF·BMP·PNG(움직이는 GIF 제외), 15MB 이하입니다. "Channel banner & profile picture tips"는 정사각형이나 원형 그림을 권합니다.

다시 만들기
- `venv/bin/python scripts/profile_pic.py channel/profile` (fonts/NotoSansKR-VF.ttf 필요, setup.sh가 받습니다. 글꼴이 다른 폴더에 있으면 VIDEO_ROOT로 그 폴더를 줍니다)

남은 것
- 사용자 선택: 아직 없습니다.
- 감자 캐릭터 INFJ를 프로필로 쓰는 안은 캐릭터를 사용자와 함께 만든 뒤에 만들 수 있습니다(HANDOFF_VIDEO.md 16장).
