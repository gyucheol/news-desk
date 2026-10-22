# 샘플 폴더

- F의연애_VOX샘플_30초.mp4: 01편 훅을 VOX 스타일로 만든 30초 무음 샘플(1920×1080, 30fps)
- sample.html: 샘플의 장면과 애니메이션 원본(브라우저 코드). 글꼴은 Noto Sans KR, Noto Serif KR, Nanum Pen Script(OFL)를 시스템에 설치해야 같은 모양이 나옵니다.
- render.js: sample.html을 프레임 단위로 캡처해 MP4로 묶는 스크립트(Playwright + ffmpeg 필요)
- make_textures.py: 종이 질감·그레인 이미지(tex/)를 다시 만드는 스크립트

다시 만드는 순서: python3 make_textures.py → node render.js "$(pwd)/sample.html" "$(pwd)/out.mp4" 30
장면 설명과 근거는 ../VOX스타일_분석.md 10장에 있습니다.
