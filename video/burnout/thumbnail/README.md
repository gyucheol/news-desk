# 번아웃 편 썸네일

2026-10-22 사용자 지시로 「F의 연애」 썸네일 틀을 적용했습니다. 가운데 그림은 좌절하거나 지친 사람이고, 얼굴은 보이지 않게 했습니다. 그림에는 그라데이션이나 효과를 넣지 않고 원본 그대로 넣었습니다(HANDOFF_VIDEO.md 18장).

- drafts/1_full_frame.jpg: 두 손으로 얼굴을 감싼 남성, 원본 화면 전체(16:9) + "번아웃"
- drafts/2_person_crop.jpg: 같은 장면을 사람 중심으로 자른 4:3 + "번아웃". 추천안(휴대폰 크기에서 사람이 더 크게 보임)
- 장면: Mixkit 4701 "Worried and sad man with his head down"의 1.4초(https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/), 라이선스 Free(2026-10-22 영상 페이지에서 확인)
- drafts/review_sheet.png: 두 시안을 640px와 휴대폰 피드 크기(360px)로 비교
- 이전 시안(가장자리를 검게 녹인 판, 베개 장면)은 '효과 없이' 지시로 지웠습니다. 커밋 8e035d4에 남아 있습니다.
- 사용자가 고르면 thumbnail.jpg로 확정합니다.

다시 만드는 명령(저장소 맨 위 폴더에서. news-desk 저장소에서는 video/burnout/에서 실행하고 경로의 episodes/burnout/을 뺍니다)
```
episodes/burnout/sample30/fetch_stock.sh    # 4701.mp4 받기(30초 예시와 같은 파일)
ffmpeg -ss 1.4 -i work/stock/full/4701.mp4 -frames:v 1 work/f4701_1.4.png
venv/bin/python scripts/thumb.py photo episodes/burnout/thumbnail/drafts/1_full_frame.jpg work/f4701_1.4.png --box 0,0,1920,1080
venv/bin/python scripts/thumb.py photo episodes/burnout/thumbnail/drafts/2_person_crop.jpg work/f4701_1.4.png --box 533,40,1920,1080
venv/bin/python scripts/thumb.py preview episodes/burnout/thumbnail/drafts/review_sheet.png episodes/burnout/thumbnail/drafts/1_full_frame.jpg episodes/burnout/thumbnail/drafts/2_person_crop.jpg --labels 1,2
```
