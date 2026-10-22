# 샘플 v2 원본 (구김 종이·뉴스레터 콜라주)

결과 영상: ../F의연애_VOX샘플_v2_30초.mp4
설명: ../../VOX스타일_분석.md 11장

## 파일
- scene2.html: 장면 배치와 12fps 스톱모션 애니메이션. `__META__` 자리에 assets/meta.json 내용을 넣어 사용합니다.
- assets2.py: 구김 종이 배경, 신문 조각, 찢은 메모, 도장, 테이프, 압정, 시계, 연구 카드, 색인 카드, 제호, 감자 스티커와 인장을 만드는 스크립트
- potato_render.js: 감자 캐릭터를 표정별 투명 PNG로 뽑는 스크립트(Playwright)

## 다시 만드는 순서
1. 글꼴 설치(모두 Google Fonts, 상업적 이용 가능): Hahmlet, Song Myung, Black Han Sans, Nanum Gothic Coding, Nanum Myeongjo, Nanum Pen Script, Special Elite, Noto Sans KR
2. CC0 종이 질감 내려받기(ambientCG, 출처 표기 의무 없음): Paper003, Paper004, Paper006의 2K-JPG zip을 받아 각각 `cc0tex/<ID>/` 폴더에 풉니다.
   - https://ambientcg.com/get?file=Paper003_2K-JPG.zip
   - https://ambientcg.com/get?file=Paper004_2K-JPG.zip
   - https://ambientcg.com/get?file=Paper006_2K-JPG.zip
3. `node potato_render.js raw` → `python3 assets2.py assets raw cc0tex`
4. scene2.html의 `__META__`를 assets/meta.json 내용으로 바꿔 scene2_built.html로 저장합니다.
5. `node ../render.js "$(pwd)/scene2_built.html" "$(pwd)/raw12.mp4" 12` 후 `ffmpeg -i raw12.mp4 -vf fps=30 -c:v libx264 -crf 22 -pix_fmt yuv420p out.mp4`
   - 필름 그레인 이미지는 ../make_textures.py로 만든 tex/grain*.png를 씁니다(scene2.html 안 경로는 ../sample/tex/).
