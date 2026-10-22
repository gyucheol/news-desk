# 번아웃 편 썸네일

2026-10-22 사용자 지시로 「F의 연애」 썸네일 틀을 적용했습니다. 가운데 그림은 좌절하거나 지친 사람이고, 얼굴은 보이지 않게 했습니다(HANDOFF_VIDEO.md 18장).

- drafts/A_head_in_hands.jpg: 두 손으로 얼굴을 감싼 남성 + "번아웃". 추천안
  - 장면: Mixkit 4701 "Worried and sad man with his head down"의 1.4초(https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/), 라이선스 Free(2026-10-22 영상 페이지에서 확인)
  - 밝은 창가 배경은 --bg-dark로 눌러 어두운 방처럼 만들었습니다.
- drafts/B_face_in_pillow.jpg: 어두운 방에서 베개에 얼굴을 묻은 사람 + "번아웃"
  - 장면: Mixkit 51394 "Woman with insomnia lying in her bed trying to sleep"의 32.0초(https://mixkit.co/free-stock-video/woman-with-insomnia-lying-in-her-bed-trying-to-sleep-51394/), 라이선스 Free(2026-10-22 확인)
  - 휴대폰 피드 크기에서는 사람으로 알아보기 어렵습니다.
- drafts/review_sheet.png: 두 시안을 640px와 휴대폰 피드 크기(360px)로 비교
- AI 시안은 두 장 모두 얼굴이 보여 쓰지 않았습니다(HANDOFF_VIDEO.md 18-5).
- 사용자가 고르면 thumbnail.jpg로 확정합니다.

다시 만드는 명령(저장소 맨 위 폴더에서. news-desk 저장소에서는 video/burnout/에서 실행하고 경로의 episodes/burnout/을 뺍니다)
```
episodes/burnout/sample30/fetch_stock.sh    # 4701.mp4, 51394.mp4 받기(30초 예시와 같은 파일)
ffmpeg -ss 1.4 -i work/stock/full/4701.mp4 -frames:v 1 work/f4701_1.4.png
venv/bin/python scripts/thumb.py photo episodes/burnout/thumbnail/drafts/A_head_in_hands.jpg work/f4701_1.4.png --box 920,60,1900,1040 --height 460 --gamma 1.35 --bg-dark 0.85
ffmpeg -ss 32.0 -i work/stock/full/51394.mp4 -frames:v 1 work/f51394_32.0.png
venv/bin/python scripts/thumb.py photo episodes/burnout/thumbnail/drafts/B_face_in_pillow.jpg work/f51394_32.0.png --box 380,40,1480,1000 --height 470 --gamma 0.95
```
