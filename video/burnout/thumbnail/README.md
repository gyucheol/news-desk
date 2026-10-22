# 번아웃 편 썸네일

2026-10-22 사용자 지시로 「F의 연애」 썸네일 틀을 적용했습니다. 가운데 그림은 좌절하거나 지친 사람이고, 얼굴은 보이지 않게 했습니다. 그림에는 그라데이션이나 효과를 넣지 않았고, 배경이 있는 그림이라 두 판으로 만들었습니다(HANDOFF_VIDEO.md 18장).

- drafts/1_background_kept.jpg: 배경을 다 살린 판. 장면이 화면 전체를 채우고, 글자는 손을 가리지 않게 왼쪽에 둠
- drafts/2_background_removed.jpg: 배경을 다 지우고 사람만 남긴 판. 검은 배경, 글자는 가운데 아래
- 장면: Mixkit 4701 "Worried and sad man with his head down"의 1.4초(https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/), 라이선스 Free(2026-10-22 영상 페이지에서 확인)
- drafts/review_sheet.png: 두 판을 640px와 휴대폰 피드 크기(360px)로 비교
- 사용자가 고르면 thumbnail.jpg로 확정합니다.

다시 만드는 명령(저장소 맨 위 폴더에서. news-desk 저장소에서는 video/burnout/에서 실행하고 경로의 episodes/burnout/을 뺍니다)
```
episodes/burnout/sample30/fetch_stock.sh    # 4701.mp4 받기(30초 예시와 같은 파일)
ffmpeg -ss 1.4 -i work/stock/full/4701.mp4 -frames:v 1 work/f4701_1.4.png
venv/bin/python scripts/thumb.py full episodes/burnout/thumbnail/drafts/1_background_kept.jpg work/f4701_1.4.png --word-cx 410
venv/bin/python scripts/cutout.py work/f4701_1.4.png work/f4701_1.4_cut.png      # 첫 실행 때 모델 약 970MB 받음
venv/bin/python scripts/thumb.py photo episodes/burnout/thumbnail/drafts/2_background_removed.jpg work/f4701_1.4_cut.png
venv/bin/python scripts/thumb.py preview episodes/burnout/thumbnail/drafts/review_sheet.png episodes/burnout/thumbnail/drafts/1_background_kept.jpg episodes/burnout/thumbnail/drafts/2_background_removed.jpg --labels 1,2
```
