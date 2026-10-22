# 샘플 폴더

01편 「불안형이 답장 늦을 때 머릿속에서 일어나는 일」 훅 30초를 VOX 스타일로 만든 무음 샘플입니다(1920×1080).

- F의연애_VOX샘플_v3_30초.mp4: 최신. 구김 종이 톤을 유지하면서 단순하고 또렷하게 만든 판(30fps). 원본은 v3/, 설명은 ../VOX스타일_분석.md 11-9
- F의연애_VOX샘플_v2_30초.mp4: 구김 종이·뉴스레터 콜라주, 12fps 스톱모션(흔들림과 흐릿한 글씨 때문에 v3로 대체). 원본은 v2/, 설명은 11장
- F의연애_VOX샘플_30초.mp4: 첫 시안 v1(AI처럼 보여 v2로 대체). 설명은 10장

## v1 원본 파일
- sample.html: 샘플의 장면과 애니메이션 원본(브라우저 코드). 글꼴은 Noto Sans KR, Noto Serif KR, Nanum Pen Script(OFL)를 시스템에 설치해야 같은 모양이 나옵니다.
- render.js: HTML 장면을 프레임 단위로 캡처해 MP4로 묶는 스크립트(Playwright + ffmpeg 필요). v2, v3도 이 스크립트를 씁니다.
- make_textures.py: 종이 질감·그레인 이미지(tex/)를 다시 만드는 스크립트

v1 다시 만드는 순서: python3 make_textures.py → node render.js "$(pwd)/sample.html" "$(pwd)/out.mp4" 30
