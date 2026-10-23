# 샘플 v3 원본 (단순하고 또렷한 VOX)

결과 영상: ../F의연애_VOX샘플_v3_30초.mp4
설명: ../../VOX스타일_분석.md 11-9

## v2와 다른 점
- 카메라 고정. 흔들기, 선 일렁임, 필름 입자, 깜빡임 없음
- 초당 30장의 부드러운 등장 효과(0.4초 동안 24픽셀 올라오며 나타남, 도장은 0.18초)
- 글씨에 닳은 효과 없음. 글씨가 든 소재는 원래 크기 이하로만 띄우고 화면에서 기울이지 않음
- 한 화면에 핵심 하나. 신문 조각, 테이프, 압정 같은 장식 없음

## 파일
- scene3.html: 장면 배치와 애니메이션. `__META__` 자리에 assets3/meta.json 내용을 넣어 사용합니다.
- assets3.py: 구김 종이 배경, 메모, 도장, 휴대폰 화면, 시계, 연구 카드, 방법 카드, 제호, 감자 스티커를 만드는 스크립트(v2의 assets2.py를 또렷하게 고친 판)
- 감자 PNG는 ../v2/potato_render.js로 만듭니다.

## 다시 만드는 순서
1. 글꼴 설치(모두 Google Fonts, 상업적 이용 가능): Hahmlet(SemiBold, ExtraBold), Black Han Sans, Gaegu, Noto Sans KR. assets3.py는 v3 화면에 쓰지 않는 소재(신문 조각, 타자기 띠)도 함께 만들기 때문에 Song Myung, Nanum Gothic Coding, Nanum Myeongjo, Special Elite도 있어야 돌아갑니다. 글꼴 파일은 assets3.py 맨 위 FONTS 목록의 파일 이름으로 ~/.fonts/에 두거나, 목록을 가진 파일 이름에 맞게 고쳐 주세요.
2. CC0 종이 질감(ambientCG Paper003, Paper004, Paper006)을 `cc0tex/<ID>/`에 풉니다. 받는 주소는 ../v2/README.md에 있습니다.
3. `node ../v2/potato_render.js raw` → `python3 assets3.py assets3 raw cc0tex`
4. scene3.html의 `__META__`를 assets3/meta.json 내용으로 바꿔 scene3_built.html로 저장합니다.
5. `node ../render.js "$(pwd)/scene3_built.html" "$(pwd)/out.mp4" 30` (H.264, CRF 20, 30fps)
