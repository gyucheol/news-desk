# 03편 「퇴근 후 의지력」 v1 영상 제작 기록

작성 2026-10-29. 결과 파일: 03_의지력_v1.mp4 (1920×1080, 30fps, H.264 + AAC 320kbps 48kHz 스테레오, 9분 20.0초, 307MB, 소리 크기 -14.0 LUFS, 최고 -1.5 dBTP). 운영자 목소리와 사용자가 만든 사진이 들어 있어 영상, 녹음, 사진은 저장소에 올리지 않았습니다(SendUserFile로 전달).

## 1. 사용자 요청 (2026-10-29)

- "대본 및 녹음본, 그리고 ai 사진 전달드림. ai 사진을 사용한 부분은 "<"자막">숫자" 이렇게 표시해놨음. 예를 들면 "사진 1"은 "<자막>1"에 사용해주면 됨."
- "[대본] * "/"이 표시는 스톡 영상을 앞 뒤로 다르게 써달라는 의미임."
- 표시한 대본 전체는 user_script_marked.txt, 사진은 메시지 15개(각 5장)로 75장이 왔습니다.

## 2. 정한 것과 이유

- 녹음: 이번 메시지에는 녹음 파일이 따로 없었고, 표시한 대본의 문장이 10월 28일 녹음에 맞춘 2판 자막과 같아서(parse_marks.py 글자 대조, 대본 3,926자 중 3,922자 일치) 그 녹음을 그대로 썼습니다. 자르거나 속도를 바꾸지 않았고, 말 사이 쉼도 녹음 그대로입니다. 다른 네 글자는 '자 그렇다면'의 '자'(대본대로 자막에 넣음), 'a그룹'(자막은 A그룹), 겹쳐 쓴 '고른 고른'(자막은 한 번)입니다. 마지막 '댓글로 공유해 주세요.'는 표시한 대본에는 없지만 녹음에 있어 자막과 함께 두었습니다(9장 질문 9).
- 사진: '<문장>N' 표시 구간에는 사진 N을 띄웠습니다. 한 문장 안에서 표시가 바뀌는 곳은 그 말의 목소리가 시작하는 때 바꿨습니다. 31, 68, 69는 대본에 두 번씩 표시되어 있어 두 곳에 썼습니다.
- 번호 없는 표시 하나('<오늘은 정말 가야겠다고 생각했죠.>')에는 사진 3을 넣었습니다. 추론(순서에 따른 추론): 앞 표시가 2, 뒤 표시가 4이고, 대본에 3번 표시가 따로 없습니다.
- 스톡: 표시가 없는 구간은 Mixkit 무료 라이선스 영상이고, '/'가 있는 곳에서 다른 영상으로 바꿨습니다(93구간, 영상 86개).
- 검은 화면: 2판에서 검은 화면이던 질문·전환 문장 11곳(사진 표시가 없는 곳)은 그대로 두었습니다.
- 가운데 자막과 큰 글씨(2018년, 회복의 역설, 2002년, 실행 의도), 가운데 자막 동안 뒤 그림을 흐리게 하는 방식은 2판 그대로입니다.
- '<< >>'로 감싼 존넨탁 문장은 뜻을 확실히 알 수 없어, 2판처럼 오래된 책 스톡에 큰 글씨 '2018년', '회복의 역설'을 띄웠습니다(9장 질문 1).
- 자막과 장면은 목소리가 시작하는 때에만 바뀝니다(onsets_v2.py). 사진은 아주 천천히 확대만 하고(초당 0.8%), 효과음은 없습니다.
- 스톡의 읽히는 글자와 상표는 잘라내거나 흐렸습니다(5장 메모). 밝은 낮 영상은 어둡게 맞췄습니다.
- 소리: 목소리 -14 LUFS(녹음 전체에 같은 크기), 배경음악은 장면 분위기에 따라 8곡을 이어 붙였습니다(6장).

## 3. 사용자 사진

- 받은 사진 75장 중 74장을 썼습니다. 55번째로 온 사진(in55)은 54번과 같은 장면의 다른 버전으로 보여 쓰지 않았습니다(9장 질문 3).
- 첫 메시지는 5, 1, 2, 3, 4번, 둘째 메시지는 7, 8, 9, 10, 6번 순서로 온 것으로 보여, 번호는 사진 내용과 대본 문장을 맞춰 정했습니다(추론: 내용 대조). 번호를 붙인 전체 사진은 photo_map.jpg로 보냈습니다.
- 대본에 71번, 73번 표시는 없고 사진도 없었습니다. 77번은 대본에 표시가 있지만 사진이 오지 않아 임시로 스톡(Mixkit 87, 숲길을 걷는 사람)을 넣었습니다.
- 오른쪽 아래 별 표시는 지웠습니다(F의 연애와 같은 방식). 사진 크기 세 가지(2000×1116, 1376×768, 1024×572)마다 표시의 위치와 모양을 따로 구해 원래 색을 되살리고, 둘레를 채웠습니다. 어두운 바탕에서 흔적이 남은 7장(14, 22, 28, 34, 35, 37, 39번)은 주변에서 메우는 방식으로, 54번은 모서리 방향을 따라, 61번은 비슷한 무늬를 옮겨 채웠습니다.
- 상표처럼 보이는 곳은 흐렸습니다: 65번 운동화 옆 로고 두 곳, 70번 라켓 줄의 로고, 75번 벽 포스터 글씨 세 곳.
- 색은 거의 그대로이고(채도 0.95), 가운데 자막이 나오는 동안만 약간 어둡고 흐리게 했습니다.

## 4. 장면 목록

시각은 영상 안에서 장면이 시작하는 때, 괄호는 길이(초)입니다. ' / '는 자막 하나의 끝, (가)는 가운데 자막입니다.

1. 0:00.0 (1.3) 사용자 사진 1: 당신은 오늘 퇴근하고
2. 0:01.3 (2.0) 스톡 st01 Mixkit 100530 (People running on treadmills at the gym): 미뤄 왔던 헬스장에 가려고 합니다.
3. 0:03.3 (1.7) 사용자 사진 2: 아침에 운동복도 챙겼습니다.
4. 0:05.0 (2.2) 사용자 사진 3: 오늘은 정말 / 가야겠다고 생각했죠.
5. 0:07.2 (2.1) 사용자 사진 4: 그런데 하루 일을 마치고 / 집에 돌아오니
6. 0:09.4 (1.9) 사용자 사진 5: 신발을 벗는 것도 귀찮습니다.
7. 0:11.3 (0.9) 사용자 사진 6: 가방을 내려놓고
8. 0:12.2 (1.2) 사용자 사진 7: 침대에 눕습니다.
9. 0:13.4 (2.3) 사용자 사진 8: 운동은 조금만 쉬었다가 / 가기로 합니다.
10. 0:15.7 (3.0) 스톡 st02 Mixkit 31411 (Sleeping boy moves in bed): 30분이 지났습니다. / 몸은 여전히 무겁습니다.
11. 0:18.8 (1.8) 사용자 사진 9: 지금 나가려면 / 옷부터 갈아입고
12. 0:20.5 (1.7) 사용자 사진 10: 헬스장까지 걸어가야 합니다.
13. 0:22.2 (2.4) 사용자 사진 11: 운동하고 씻고 / 돌아올 생각을 하니
14. 0:24.5 (3.3) 스톡 st03 Mixkit 51395 (Girl using her cell phone in her bed waiting to sleep): 그냥 오늘은 / 여기 누워 있고 싶습니다. / 결국 오늘만 쉬고
15. 0:27.9 (2.1) 사용자 사진 12: 내일은 꼭 운동하겠다고 다짐합니다.
16. 0:30.0 (0.9) 스톡 st04 Mixkit 31412 (Boy puts his cell phone aside so he can go to sleep): 휴대폰을 보다가
17. 0:30.9 (3.1) 사용자 사진 13: 퇴근 후에 운동도 하고 / 외국어도 배우는 사람을 발견합니다.
18. 0:34.0 (4.1) 스톡 st05 Mixkit 31412 (Boy puts his cell phone aside so he can go to sleep): (가)저 사람도 일하고 왔을 텐데 / (가)안 피곤한가? / 생각합니다. / 그러면서 문득
19. 0:38.1 (3.0) 사용자 사진 14: (가)나는 왜 아무것도 안 하고 / (가)쉬고만 싶을까? / 생각합니다.
20. 0:41.1 (3.0) 스톡 st06 Mixkit 42834 (Hands of a guitarist changing chords): 하고 싶은 게 / 없는 것도 아닙니다. / 배워 보고 싶은 악기도 있고
21. 0:44.1 (1.4) 스톡 st07 Mixkit 50723 (A young student woman searches for a book in the library): 읽고 싶은 책도 있습니다.
22. 0:45.6 (1.6) 스톡 st08 Mixkit 4832 (Man dressed in suit crossing the street): 그런데 출근했다가 돌아오면
23. 0:47.2 (1.5) 스톡 st09 Mixkit 25579 (Sad and desperate man lying on a sofa): 그걸 할 힘이 없습니다.
24. 0:48.7 (2.2) 스톡 st10 Mixkit 39841 (Young man working in an office overtime): 회사에서는 어떻게든 / 하루를 버텼는데
25. 0:50.9 (3.7) 스톡 st11 Mixkit 25586 (Sad girl sitting on the floor): 정작 나를 위해 / 쓰고 싶은 시간에는 / 아무것도 남아 있지 않은 기분입니다.
26. 0:54.6 (2.8) 검은 화면: (가)하지만 이게 정말 / (가)내가 게을러서 생기는 일일까요?
27. 0:57.5 (4.0) 사용자 사진 15: 오늘은 퇴근 후 / 하고 싶은 일이 있어도 / 시작하기 어려운 이유를 살펴보고
28. 1:01.5 (4.5) 스톡 st12 Mixkit 1737 (Writing notes at a cafe): 지친 하루 뒤에도 / 내 생활을 조금씩 이어 갈 / 방법 3가지를 / 이야기해 보겠습니다.
29. 1:05.9 (1.6) 사용자 사진 16: 수요일 저녁 8시입니다.
30. 1:07.5 (1.3) 사용자 사진 17: 씻고 밥을 먹고 나니
31. 1:08.8 (2.3) 사용자 사진 18: 잠들기 전까지 / 2시간 정도가 남았습니다.
32. 1:11.1 (2.7) 스톡 st13 Mixkit 28886 (Analog wall clock on a black background in a closed socket): 시계만 보면 / 뭔가 하나쯤은 / 할 수 있을 것 같습니다.
33. 1:13.8 (1.9) 사용자 사진 19: 주말에 산 영어책이 / 눈에 들어옵니다.
34. 1:15.7 (1.8) 스톡 st14 Mixkit 50110 (Student draws a mathematical chart over a squared notebook w): 영어 공부를 해 보고 싶기는 합니다.
35. 1:17.5 (3.4) 사용자 사진 20: 그런데 책상에 앉아서 / 공부할 생각을 하니 / 손이 가지 않습니다.
36. 1:20.9 (2.0) 스톡 st15 Mixkit 25596 (Young man lays on a bed with a strong stomach ache): 그래서 조금만 쉬었다 하자는 생각으로
37. 1:23.0 (1.8) 사용자 사진 21: 침대에 누워서 / 유튜브를 켭니다.
38. 1:24.7 (2.2) 사용자 사진 22: 쇼츠 화면을 넘기는 정도는 / 할 수 있습니다.
39. 1:26.9 (5.4) 스톡 st16 Mixkit 51400 (Portrait of a woman trying to sleep in her bed): 하지만 몸을 일으켜 / 뭔가를 시작하는 건 / 전혀 다른 일처럼 느껴집니다. / 그러다 이런 생각이 듭니다.
40. 1:32.3 (1.6) 사용자 사진 23: (가)휴대폰 볼 힘은 있으면서
41. 1:33.9 (2.5) 사용자 사진 24: (가)영어 공부할 힘은 없다는 건 / (가)핑계 아닐까?
42. 1:36.4 (2.8) 검은 화면: (가)하지만 두 행동에 필요한 수고는 / (가)같지 않습니다.
43. 1:39.2 (2.5) 스톡 st17 Mixkit 51397 (Young woman using her cell phone lying in her bed): 누운 채로 아무 생각 없이 / 화면을 넘기는 일과
44. 1:41.7 (4.0) 스톡 st18 Mixkit 50133 (A young man wearing a hoodie studying at night in the librar): 책상에 앉아 머리를 쓰며 / 공부하는 일을 / 같은 기준으로 / 비교할 수는 없죠.
45. 1:45.7 (4.0) 스톡 st19 Mixkit 51397 (Young woman using her cell phone lying in her bed): (가)휴대폰을 보고 있다는 사실만으로 / (가)피곤하지 않다는 결론을 / (가)내릴 수는 없습니다.
46. 1:49.7 (1.7) 사용자 사진 25: 우리는 달력에 빈칸이 있으면
47. 1:51.4 (1.5) 사용자 사진 26: 그 시간에 할 일을 넣습니다.
48. 1:52.9 (4.1) 사용자 사진 27: 그런데 달력에는 / 그때 내가 얼마나 지쳐 있을지가 / 표시돼 있지 않습니다.
49. 1:57.0 (2.6) 사용자 사진 28: 저녁 8시부터 9시까지 / 비어 있다는 것과
50. 1:59.7 (3.4) 사용자 사진 29: 그 1시간에 / 영어 공부를 할 힘이 있다는 것은 / 다른 문제입니다.
51. 2:03.1 (3.9) 스톡 st20 Mixkit 99909 (Close up of a hand writing to do list on a yellow paper note): (가)퇴근 후 계획이 자꾸 무너진다면 / (가)이 차이부터 / (가)살펴볼 필요가 있습니다.
52. 2:07.0 (3.9) 검은 화면: (가)그렇다면 하루 동안 쌓인 피로는 / (가)이후의 활동에 / (가)어떤 영향을 줄까요?
53. 2:10.9 (3.2) 스톡 st21 Mixkit 4733 (Scientist observing through a microscope): 이를 알아보고자 / 마코라 연구팀은 / 한 실험을 진행했습니다.
54. 2:14.1 (3.4) 사용자 사진 30: 실험에 참가한 16명의 사람들 앞에는 / 수학 문제집이 있고
55. 2:17.5 (3.4) 사용자 사진 31: 직원의 안내에 따라 / 그들은 90분 동안 / 수학 문제를 풀었습니다.
56. 2:20.9 (2.3) 스톡 st22 Mixkit 50958 (A young woman pedaling on a static bike): 그리고 나서 / 실내 자전거를 타게 했습니다.
57. 2:23.2 (3.2) 스톡 st23 Mixkit 26091 (Man eats watching television on a rainy night): 그다음 날에는 / 같은 시간 동안 / 차분한 다큐멘터리를 본 뒤
58. 2:26.4 (1.1) 스톡 st24 Mixkit 50961 (A young athlete woman pedaling on a stationary bike over a b): 자전거를 탔습니다.
59. 2:27.5 (3.0) 검은 화면: (가)과연 이들은 / (가)두 날에 탄 자전거 시간이 / (가)똑같았을까요?
60. 2:30.5 (3.1) 스톡 st25 Mixkit 50980 (A stationary bike at the center of a pristine illuminated ba): 다큐멘터리를 본 뒤에는 / 평균 약 12분을 버텼지만
61. 2:33.6 (2.6) 스톡 st26 Mixkit 50983 (A visibly tired young black man exercising on a stationary b): 수학 문제를 푼 뒤에는 / 약 9분에 멈췄습니다.
62. 2:36.3 (2.0) 검은 화면: (가)더 눈여겨볼 점은 그다음입니다.
63. 2:38.3 (3.2) 스톡 st27 Mixkit 32796 (Woman starting her stopwatch before running): 두 날 모두 / 운동 중의 심폐 반응에는 / 큰 차이가 없었지만
64. 2:41.5 (2.0) 사용자 사진 31: 그들은 모두 / 수학 문제를 풀었던 날
65. 2:43.5 (3.8) 사용자 사진 32: 즉 정신적으로 피곤한 날에 / 한 운동이 / 더 힘들었다고 답했습니다.
66. 2:47.3 (4.6) 스톡 st28 Mixkit 4701 (Worried and sad man with his head down): (가)한마디로 머리를 오래 쓴 뒤에는 / (가)몸으로 하는 일도 / (가)더 버거워질 수 있다는 뜻입니다.
67. 2:51.9 (4.7) 스톡 st29 Mixkit 39840 (Young man in front of the computer in an office): 주로 앉아서 일했다고 해서 / 퇴근 후 운동할 힘이 / 그대로 남아 있다고 / 볼 수는 없는 것이죠.
68. 2:56.6 (4.0) 사용자 사진 33: 하루 종일 서 있거나 / 물건을 옮기며 일했다면 / 몸을 쓴 부담도 있습니다.
69. 3:00.6 (2.0) 사용자 사진 34: 출퇴근길에 오래 서 있었을 수도 있고
70. 3:02.6 (2.3) 스톡 st30 Mixkit 31414 (Man lying down moving a lot because of not being able to sle): 전날 잠을 충분히 못 잤을 수도 있습니다.
71. 3:04.9 (3.2) 스톡 st31 Mixkit 31410 (Man setting his alarm clock before going to sleep): (가)퇴근했다는 이유만으로 / (가)이런 피로가 / (가)초기화되지는 않습니다.
72. 3:08.1 (3.8) 사용자 사진 35: 그런데 우리는 저녁의 자신에게 / 아침에 세운 계획을 / 그대로 건넵니다.
73. 3:11.9 (4.8) 스톡 st32 Mixkit 3525 (Feet of a young man with red tennis shoes): 그래서 아침에는 할 만해 보였던 / 1시간 운동이 / (가)저녁에는 / (가)너무 큰 일로 느껴지는 겁니다.
74. 3:16.7 (1.7) 검은 화면: (가)여기서 이상한 점이 있습니다.
75. 3:18.4 (5.3) 스톡 st33 Mixkit 40754 (Man and woman jogging through a park in the city): 적당한 운동과 / 취미 생활이 / 피로 회복에 도움이 된다는 건 / 여러 연구를 통해 / 증명된 사실입니다.
76. 3:23.7 (4.0) 사용자 사진 36: 그런데 정작 지친 날에는 / 그 활동을 시작하는 것 자체가 / 힘듭니다.
77. 3:27.7 (3.6) 스톡 st34 Mixkit 4534 (Worried woman sitting in an armchair): (가)회복이 필요할수록 / (가)회복을 위한 행동에 / (가)들어가기 어려워지는 것이죠.
78. 3:31.3 (6.3) 스톡 st35 Mixkit 4723 (Person flipping through a book looking for a page): 조직심리학자 / 자비네 존넨탁은 / 2018년 논문에서 / 이런 문제를 / 회복의 역설이라는 개념으로 / 정리했습니다.
79. 3:37.6 (4.9) 스톡 st36 Mixkit 100528 (Woman running on treadmill in gym fitness session): 그래서 / (가)운동하면 덜 피곤해진다는데 / (가)일단 해 / (가)라는 말만으로는 / (가)충분하지 않습니다.
80. 3:42.6 (8.9) 스톡 st37 Mixkit 40251 (Portrait of a tired fitness man resting at a gym): 운동이 좋다는 사실은 / 이미 알고 있습니다. / (가)지금 막힌 곳은 / (가)운동의 필요성을 이해하는 단계가 / (가)아닙니다. / (가)지친 몸으로 그 활동을 / (가)시작하고 이어 가는 / (가)단계입니다.
81. 3:51.4 (7.7) 검은 화면: (가)그런데 왜 좋아하는 취미까지 / (가)이렇게 부담스러울까요? / (가)좋아한다는 마음이 있어도 / (가)그 일을 하는 데 필요한 수고가 / (가)없어지지는 않기 때문입니다.
82. 3:59.1 (1.0) 사용자 사진 37: 여행을 좋아해도
83. 4:00.1 (3.2) 사용자 사진 38: 여행 가기 전에 짐을 싸고 / 여행지까지 가는 데 / 힘이 듭니다.
84. 4:03.3 (4.9) 사용자 사진 39: 기타 연주를 좋아해도 / 등을 세우고 앉아 / 손가락을 움직이며 / 연습하는 일에는 / 힘이 듭니다.
85. 4:08.2 (3.5) 스톡 st38 Mixkit 100529 (People exercising on treadmills in a gym): 헬스장에 가는 일도 / 자세히 보면 / 운동 하나로 끝나지 않습니다.
86. 4:11.7 (0.8) 사용자 사진 40: 준비하고
87. 4:12.5 (0.7) 사용자 사진 41: 이동하고
88. 4:13.2 (1.3) 사용자 사진 42: 운동하고 씻고
89. 4:14.5 (1.0) 사용자 사진 43: 돌아와야 합니다.
90. 4:15.5 (1.1) 스톡 st39 Mixkit 25585 (Frustrated boy throws a tantrum while working on his compute): 이미 지친 저녁에는
91. 4:16.6 (3.3) 스톡 st40 Mixkit 4596 (Man bandaging his hand before boxing): 운동 시간 앞뒤로 붙어 있는 과정까지 / 크게 느껴질 수 있습니다.
92. 4:19.9 (9.3) 스톡 st41 Mixkit 42845 (Man playing guitar in the dark): 그러니 / (가)내가 정말 좋아하는 일이었다면 / (가)피곤해도 했겠지 / (가)라고 너무 빨리 결론 내리지 / (가)않았으면 합니다. / (가)좋아하는 마음과 / (가)지금 할 수 있는 상태는 / (가)서로 다를 수 있습니다.
93. 4:29.2 (3.4) 스톡 st42 Mixkit 100555 (Woman exercising on treadmill in gym.): 이 문제를 풀려면 / 피곤함을 무시한 채 / 계획을 밀어붙이기보다
94. 4:32.6 (3.7) 사용자 사진 44: (가)지친 날에도 들어갈 수 있도록 / (가)활동의 문턱을 / (가)바꿔 볼 필요가 있습니다.
95. 4:36.3 (2.9) 검은 화면: (가)자 그렇다면 / (가)무엇부터 해 보면 좋을까요? / (가)첫째
96. 4:39.2 (3.4) 사용자 사진 45: (가)남는 시간에 쉬려고 하지 말고 / (가)쉴 시간을 미리 정해 두세요.
97. 4:42.6 (2.6) 사용자 사진 46: 퇴근하고 집에 오자마자 / 운동을 해야 한다고 생각하면
98. 4:45.2 (4.1) 사용자 사진 47: 소파에 잠깐 앉는 순간부터 / 자괴감이 들고 / 실패한 기분이 들 수 있습니다.
99. 4:49.4 (3.5) 스톡 st43 Mixkit 8744 (Young man upset and frustrated receiving a message): 하지만 하루를 보내고 / 무언가를 바로 할 수 없는 / 지친 상태라면
100. 4:52.9 (2.8) 스톡 st44 Mixkit 43386 (Woman enjoying music while resting): 쉬는 시간이 / 저녁 계획에 / 무조건 들어가야 합니다.
101. 4:55.7 (1.9) 스톡 st45 Mixkit 26085 (Girl eating salad in her kitchen dining room): 밥을 먹어야 하는데 미루고 있는지
102. 4:57.5 (3.6) 스톡 st46 Mixkit 31413 (Young man lying on his bed checking his smartphone): 잠이 부족한데 / 또 취침 시간을 늦추려는지 / 먼저 살펴보세요.
103. 5:01.1 (1.4) 스톡 st47 Mixkit 4806 (Young woman writes a list on her work schedule): 운동과 취미를 넣기 위해
104. 5:02.5 (3.0) 스톡 st48 Mixkit 49918 (Close shot of a woman underlining notes with bookmarks): 이미 필요한 휴식까지 / 빼고 있지는 않은지 / 보는 겁니다.
105. 5:05.5 (4.0) 스톡 st49 Mixkit 52072 (A young man arrive to the comfy couch in the contemporary de): 그리고 집에 돌아와서는 / 당장 뭔가를 시작할 수 있는지부터 / 시험하지 말고
106. 5:09.5 (4.5) 스톡 st50 Mixkit 250 (Woman sits on a couch drinking coffee): (가)먼저 편히 쉬어 보세요. / 쉬고 나서 / 오늘 할 수 있는 활동의 크기를 / 정하는 겁니다.
107. 5:14.1 (1.4) 스톡 st51 Mixkit 3210 (Couple sleeps on couch): 물론 잠깐 쉬었다고
108. 5:15.4 (4.0) 스톡 st52 Mixkit 25579 (Sad and desperate man lying on a sofa): 아침처럼 기운이 / 돌아오는 것은 아닙니다. / 만약 쉬었는데도 여전히 지치면
109. 5:19.4 (2.0) 사용자 사진 48: (가)오늘은 더 쉬어야 하는 / (가)날일 수 있습니다.
110. 5:21.5 (3.5) 검은 화면: (가)여기서 중요한 것은 / (가)매일 저녁에 / (가)무엇이든 해내는 것이 아닙니다.
111. 5:25.0 (4.5) 사용자 사진 49: (가)내가 실제로 쓸 수 있는 힘이 / (가)어느 정도인지 살핀 다음 / (가)그 안에서 선택하는 겁니다.
112. 5:29.4 (4.3) 스톡 st53 Mixkit 52110 (A young woman clad in black workout attire exercise at the g): 하지만 조금 쉬고 나서도 / 원래 계획한 1시간 운동은 / 부담스러울 수 있습니다.
113. 5:33.7 (2.6) 검은 화면: (가)그래서 / (가)두 번째 방법이 필요합니다. / (가)둘째
114. 5:36.3 (2.3) 사용자 사진 50: (가)피곤한 날에 할 수 있는 분량을 / (가)따로 만들고
115. 5:38.6 (1.9) 사용자 사진 51: (가)준비 과정도 / (가)함께 줄여 보세요.
116. 5:40.5 (2.6) 사용자 사진 52: 2002년 / 밀른 연구팀이 발표한 연구에서는
117. 5:43.0 (2.5) 사용자 사진 53: 248명을 / 두 그룹으로 나누었습니다.
118. 5:45.5 (2.8) 사용자 사진 54: A그룹은 / 운동 동기를 높이는 설명을 들었습니다.
119. 5:48.3 (1.6) 스톡 st54 Mixkit 4851 (Girl running during sunset ties her shoelaces): 운동하려는 마음은 강해졌지만
120. 5:49.9 (2.8) 스톡 st55 Mixkit 26092 (Young man eating while watching television): 이후 운동 행동이 / 유의하게 늘지는 않았습니다.
121. 5:52.7 (3.4) 사용자 사진 55: 같은 설명에 / 구체적인 실행 계획까지 / 듣고 정리한 B그룹은
122. 5:56.1 (2.0) 스톡 st56 Mixkit 40881 (Man and woman jogging together on the street): 운동 행동이 / 눈에 띄게 늘었습니다.
123. 5:58.1 (1.1) 스톡 st57 Mixkit 51393 (Sleepy woman looking out the window at night): (가)하고 싶다는 마음과
124. 5:59.1 (3.3) 스톡 st58 Mixkit 42655 (A woman writing in her spiral notebook): (가)실제로 무엇을 할지 정하는 일 사이에는 / (가)차이가 있다는 뜻입니다.
125. 6:02.5 (4.4) 사용자 사진 56: 언제 어디서 행동할지를 / 구체화하는 이런 방식을 / 실행 의도라고 부릅니다.
126. 6:06.8 (2.9) 스톡 st59 Mixkit 99890 (Close up a hand writing notes on a notebook with a pen): 그러면 / 오늘의 피로를 고려한 / 선택지를 만들어 봅시다.
127. 6:09.7 (1.6) 스톡 st60 Mixkit 100530 (People running on treadmills at the gym): 평소에는 헬스장에 가더라도
128. 6:11.3 (3.4) 사용자 사진 57: 많이 지친 날에는 / 집 앞을 잠깐 걷는 것으로 / 바꿀 수 있습니다.
129. 6:14.7 (2.2) 스톡 st61 Mixkit 2858 (The hand of a person drawing): 그림을 그린다면 / 한 장을 완성하는 대신
130. 6:16.9 (2.3) 사용자 사진 58: 식탁에 놓인 컵 하나만 / 그려 볼 수 있겠죠.
131. 6:19.2 (5.0) 스톡 st62 Mixkit 99909 (Close up of a hand writing to do list on a yellow paper note): 계획은 / 이렇게 적어 볼 수 있습니다. / (가)수요일 저녁에는 / (가)밥 먹고 / (가)집 앞을 5분 걷는다.
132. 6:24.2 (5.1) 사용자 사진 59: 그림이라면 / (가)목요일 저녁에는 / (가)쉬고 나서 / (가)펼쳐 둔 스케치북에 / (가)컵 하나를 그린다 / (가)가 되겠죠.
133. 6:29.3 (2.6) 사용자 사진 60: 5분이 특별한 효과를 보장하는 / 숫자는 아닙니다.
134. 6:31.9 (3.7) 스톡 st63 Mixkit 50759 (A young man stretches his arms on the balcony): 지친 날에도 선택할 수 있는 / 작은 활동을 정하기 위한 / 예시입니다.
135. 6:35.6 (4.1) 사용자 사진 61: 평소 운동량을 채우는 목표와 / 오늘 조금 움직이는 목표를 / 구분하는 것이죠.
136. 6:39.8 (2.2) 스톡 st64 Mixkit 101368 (Close-Up of Girl Tying Sneakers): (가)여기서 / (가)준비 과정도 같이 줄여 보세요.
137. 6:42.0 (2.2) 사용자 사진 62: 그림을 그릴 때마다 / 가방을 뒤져야 한다면
138. 6:44.2 (2.2) 사용자 사진 63: 스케치북과 연필을 / 한곳에 두는 겁니다.
139. 6:46.4 (2.5) 사용자 사진 64: 걷는 날에는 / 멀리 있는 공원까지 이동하기보다
140. 6:48.8 (1.7) 사용자 사진 65: 집 근처에서 / 시작할 수 있겠죠.
141. 6:50.6 (3.5) 스톡 st65 Mixkit 52136 (A young runner woman dressed in a black sports outfit starts): 그리고 5분만 하기로 했다면 / (가)정말 5분 만에 / (가)끝내도 됩니다.
142. 6:54.0 (5.2) 스톡 st66 Mixkit 723 (Jogger stopping to take a breath): 일단 시작했으니 / 30분은 해야 한다고 요구하면 / 다음번의 5분도 / 무겁게 느껴질 수 있으니까요.
143. 6:59.2 (4.4) 사용자 사진 66: 그런데 분량을 줄여도 / 활동 자체가 내내 괴롭기만 하다면 / 손이 가지 않겠죠.
144. 7:03.6 (5.0) 검은 화면: (가)그래서 마지막으로 바꿔 볼 것은 / (가)그 시간 안에서 / (가)내가 무엇을 얻는가입니다. / (가)셋째
145. 7:08.6 (2.8) 스톡 st67 Mixkit 40012 (Two excited girls during a pottery class): (가)지금 조금이라도 더 즐거운 활동을 / (가)골라 보세요.
146. 7:11.4 (2.6) 사용자 사진 67: 독서를 즐겨 하는 60명을 / 두 그룹으로 나누어
147. 7:14.0 (3.2) 사용자 사진 68: A그룹에게는 / 자신이 즐겨 읽는 장르의 책을 / 고르게 했고
148. 7:17.2 (3.6) 사용자 사진 69: B그룹에게는 / 본인의 인생에 도움이 될 것 같은 책을 / 고르게 했습니다.
149. 7:20.8 (4.2) 사용자 사진 68: 본인이 즐겨 읽는 장르의 책을 / 고른 사람들은 / 평균 약 50페이지를 읽었고
150. 7:25.0 (3.9) 사용자 사진 69: 인생에 도움이 될 것 같은 책을 / 고른 사람들은 / 약 20페이지를 읽었습니다.
151. 7:28.9 (5.6) 스톡 st68 Mixkit 574 (A woman reading a book on her bed): (가)미래에 얻을 결과뿐 아니라 / (가)지금 하는 과정의 즐거움도 / (가)행동을 이어 가는 데 / (가)도움이 될 수 있다는 것입니다.
152. 7:34.5 (5.3) 사용자 사진 70: (가)퇴근 후 활동을 고를 때도 / (가)이 질문을 더해 보세요. / (가)지금의 내가 / (가)그나마 하고 싶은 건 / (가)무엇일까?
153. 7:39.8 (1.1) 스톡 st69 Mixkit 608 (Silhouette of a runner in the city): 혼자 달리는 것보다
154. 7:40.9 (2.9) 사용자 사진 72: 친구와 가볍게 / 배드민턴을 치는 편이 / 좋을 수 있습니다.
155. 7:43.8 (1.8) 스톡 st70 Mixkit 5172 (Woman painting in her studio while watching a tutorial on he): 강의를 따라 그림을 배우는 것보다
156. 7:45.6 (3.2) 사용자 사진 74: 좋아하는 캐릭터를 그리는 편이 / 오늘은 더 끌릴 수도 있죠.
157. 7:48.7 (6.8) 스톡 st71 Mixkit 662 (Woman playing an acoustic guitar in her living room): 기타를 배우고 있다면 / 늘 새 진도를 나갈 필요는 없습니다. / 이미 칠 줄 아는 좋아하는 곡의 / 한 부분을 / 다시 연주해 봐도 됩니다.
158. 7:55.6 (2.1) 스톡 st72 Mixkit 50126 (A young student wearing a hoodie hilight texts on a book whi): 책도 오늘은 / 공부해야 하는 책보다
159. 7:57.7 (2.3) 스톡 st73 Mixkit 42741 (Girl reading a book sitting near a window): 다음 이야기가 궁금한 소설을 / 고를 수 있고요.
160. 8:00.0 (6.9) 스톡 st74 Mixkit 42188 (Young woman putting together a puzzle): 이런 선택이 / 피로를 없애 주는 것은 아닙니다. / (가)다만 힘을 들여 하는 그 시간 안에 / (가)내가 좋아하는 경험을 / (가)함께 넣어 보는 겁니다.
161. 8:06.9 (4.3) 스톡 st75 Mixkit 1781 (Typing on a laptop, close up.): 그리고 세 방법을 써 봐도 / 평일 저녁에는 / 도저히 여유가 생기지 않을 수 있습니다.
162. 8:11.3 (2.8) 사용자 사진 75: 그렇다면 / 활동을 배치한 시간도 / 바꿔 볼 수 있습니다.
163. 8:14.1 (3.7) 사용자 사진 76: 평일에 운동과 취미를 전부 넣기보다 / 한 번씩 나눠 두거나
164. 8:17.8 (3.1) 스톡 st76 Mixkit 87 (Tracking a man through the forest): 긴 활동은 / 상대적으로 여유 있는 휴일에 / 하는 것이죠.
165. 8:20.9 (2.2) 스톡 st77 Mixkit 52119 (A young beautiful woman clad in black sportswear stretch her): 아침도 괜찮다면 / 옮겨 볼 수 있겠지만
166. 8:23.1 (3.0) 스톡 st78 Mixkit 28899 (Woman turning off her alarm clock in the morning): 잠을 줄여서까지 / 새 시간을 만들 필요는 없습니다.
167. 8:26.2 (5.3) 스톡 st79 Mixkit 99834 (Raindrops on glass with blurred city lights in the backgroun): (가)내 생활을 갖는다는 것이 / (가)꼭 매일 퇴근 후 2시간을 / (가)알차게 써야 한다는 뜻은 / (가)아니니까요.
168. 8:31.5 (5.3) 스톡 st80 Mixkit 660 (Woman sipping from a mug at home): 어떤 날은 짧게 하고 / 어떤 날은 길게 하고 / 어떤 날은 쉬면서 / 이어 갈 수도 있습니다.
169. 8:36.8 (3.7) 스톡 st81 Mixkit 39779 (Hand of a man looking at his smart watch): 생각해 보면 / 우리는 퇴근 뒤의 시간을 / 꽤 쉽게 계산합니다.
170. 8:40.5 (1.9) 스톡 st82 Mixkit 28887 (Top of a wall clock in a close-up shot): 9시까지 2시간이 남았으니
171. 8:42.4 (0.9) 스톡 st83 Mixkit 5048 (Young man doing push-ups on the floor): 운동도 하고
172. 8:43.3 (2.1) 스톡 st84 Mixkit 1724 (A person reading a book, close up): 책도 조금 읽을 수 있을 것 같습니다.
173. 8:45.4 (2.2) 스톡 st85 Mixkit 924 (Silhouette of woman opening a window): (가)하지만 그 2시간을 살아갈 사람은
174. 8:47.6 (2.4) 스톡 st86 Mixkit 134 (A man being followed walking in a city): (가)하루를 이미 보내고 돌아온 / (가)나입니다.
175. 8:50.0 (2.1) 스톡 st87 Mixkit 2848 (Marking Christmas day on the calendar): (가)시간표에 빈칸이 있다는 이유만으로
176. 8:52.1 (3.4) 스톡 st88 Mixkit 4701 (Worried and sad man with his head down): (가)그 빈칸을 전부 채울 힘까지 / (가)남아 있는 것은 아닙니다.
177. 8:55.5 (5.6) 스톡 st89 Mixkit 40242 (Fitness man throwing dumbbells to the floor): 오늘 너무 피곤해서 / 운동 가방을 내려놓았다고 해서 / (가)하고 싶은 마음까지 / (가)없었던 것은 아닐 겁니다.
178. 9:01.1 (6.0) 스톡 st90 Mixkit 42904 (Woman meditating and breathing deeply): (가)내일도 똑같은 크기의 계획을 / (가)건네기 전에 / (가)오늘의 내가 어떤 상태였는지 / (가)먼저 살펴봐 주세요.
179. 9:07.0 (2.8) 스톡 st91 Mixkit 4596 (Man bandaging his hand before boxing): (가)어쩌면 필요한 것은 / (가)더 단단한 결심보다
180. 9:09.8 (3.9) 스톡 st92 Mixkit 40136 (Woman tying shoelaces during a training): (가)조금 더 쉴 자리와 / (가)조금 더 작은 시작인지도 / (가)모르겠습니다.
181. 9:13.7 (6.3) 스톡 st93 Mixkit 43444 (Artist painting painting on a canvas): (가)여러분은 퇴근하고 / (가)즐겨 하는 취미가 있나요? / (가)댓글로 공유해 주세요.

## 5. 스톡 영상 (Mixkit, 모두 무료 라이선스)

영상 페이지의 구조화 데이터(JSON-LD) copyrightNotice가 "Free"인 것만 썼습니다(stock/tools/mk.py lic, 확인 기록은 stock/items/lic_*.json). 같은 영상을 두 곳에 쓴 것은 한 줄에 적었습니다. '대신함'은 원하던 장면의 무료 영상이 없어 비슷한 장면을 쓴 곳입니다.

- 100530 People running on treadmills at the gym: https://mixkit.co/free-stock-video/people-running-on-treadmills-at-the-gym-100530/ | 라이선스 Free (확인 2026-10-29) | st01 0:01.3부터(2.0초, 원본 0.5초부터), 원하던 장면: 헬스장 안, 러닝머신이 줄지어 선 곳 / st60 6:09.7부터(1.6초, 원본 4.0초부터), 원하던 장면: 평소처럼 헬스장에서 운동하는 사람
- 31411 Sleeping boy moves in bed: https://mixkit.co/free-stock-video/sleeping-boy-moves-in-bed-31411/ | 라이선스 Free (확인 2026-10-29) | st02 0:15.7부터(3.0초, 원본 4.6초부터), 원하던 장면: 어두운 방 침대에 꼼짝 않고 누워 있는 사람(시간이 지나도 그대로)
- 51395 Girl using her cell phone in her bed waiting to sleep: https://mixkit.co/free-stock-video/girl-using-her-cell-phone-in-her-bed-waiting-to-51395/ | 라이선스 Free (확인 2026-10-29) | st03 0:24.5부터(3.3초, 원본 10.0초부터), 원하던 장면: 침대에 편히 누워 눈을 감고 쉬는 사람
- 31412 Boy puts his cell phone aside so he can go to sleep: https://mixkit.co/free-stock-video/boy-puts-his-cell-phone-aside-so-he-can-go-31412/ | 라이선스 Free (확인 2026-10-29) | st04 0:30.0부터(0.9초, 원본 0.0초부터), 원하던 장면: 밤에 침대에 누워 휴대폰을 넘겨 보는 손(st05와 같은 영상의 앞부분) / st05 0:34.0부터(4.1초, 원본 1.5초부터), 원하던 장면: 침대에서 휴대폰을 보다 생각에 잠긴 사람(st04와 같은 영상의 뒷부분, 앞 두 줄은 가운데 기울임 자막)
- 42834 Hands of a guitarist changing chords: https://mixkit.co/free-stock-video/hands-of-a-guitarist-changing-chords-42834/ | 라이선스 Free (확인 2026-10-29) | st06 0:41.1부터(3.0초, 원본 1.0초부터), 원하던 장면: 어두운 방에 세워 둔 기타, 또는 기타 줄을 만지기만 하는 손(배워 보고 싶은 악기), 손본 것: 처음 고른 42845는 흑백이라 다른 장면과 색이 맞지 않아 같은 내용의 컬러 영상으로 바꿈
- 50723 A young student woman searches for a book in the library: https://mixkit.co/free-stock-video/a-young-student-woman-searches-for-a-book-in-the-50723/ | 라이선스 Free (확인 2026-10-29) | st07 0:44.1부터(1.4초, 원본 10.5초부터), 원하던 장면: 책장에 꽂힌 책, 책을 꺼내는 손(읽고 싶은 책), 손본 것: 처음 고른 50714는 책등 제목(WHY CIVIL RESISTANCE, PSICOLOGÍA 등)이 크게 읽혀서 바꿈
- 4832 Man dressed in suit crossing the street: https://mixkit.co/free-stock-video/man-dressed-in-suit-crossing-the-street-4832/ | 라이선스 Free (확인 2026-10-29) | st08 0:45.6부터(1.6초, 원본 1.0초부터), 원하던 장면: 저녁에 퇴근해 집으로 걸어가는 사람(뒷모습)
- 25579 Sad and desperate man lying on a sofa: https://mixkit.co/free-stock-video/sad-and-desperate-man-lying-on-a-sofa-25579/ | 라이선스 Free (확인 2026-10-29) | st09 0:47.2부터(1.5초, 원본 4.5초부터), 원하던 장면: 지쳐서 소파나 침대에 털썩 쓰러지는 사람, 대신함: 쓰러지는 순간은 없고, 쓰러진 뒤 소파에 누워 팔로 눈을 가린 모습 / st52 5:15.4부터(4.0초, 원본 8.6초부터), 원하던 장면: 쉬고 나서도 여전히 지쳐 눈을 비비는 사람
- 39841 Young man working in an office overtime: https://mixkit.co/free-stock-video/young-man-working-in-an-office-overtime-39841/ | 라이선스 Free (확인 2026-10-29) | st10 0:48.7부터(2.2초, 원본 6.4초부터), 원하던 장면: 사무실 책상에서 지친 얼굴로 버티는 직장인(눈을 비빔 등)
- 25586 Sad girl sitting on the floor: https://mixkit.co/free-stock-video/sad-girl-sitting-on-the-floor-25586/ | 라이선스 Free (확인 2026-10-29) | st11 0:50.9부터(3.7초, 원본 0.5초부터), 원하던 장면: 밤에 불 꺼진 방에 혼자 멍하니 앉아 있는 사람
- 1737 Writing notes at a cafe: https://mixkit.co/free-stock-video/writing-notes-at-a-cafe-1737/ | 라이선스 Free (확인 2026-10-29) | st12 1:01.5부터(4.5초, 원본 2.0초부터), 원하던 장면: 스탠드 불빛 아래 수첩에 목록을 적는 손
- 28886 Analog wall clock on a black background in a closed socket: https://mixkit.co/free-stock-video/analog-wall-clock-on-a-black-background-in-a-closed-28886/ | 라이선스 Free (확인 2026-10-29) | st13 1:11.1부터(2.7초, 원본 0.5초부터), 원하던 장면: 벽시계 초침이 도는 모습
- 50110 Student draws a mathematical chart over a squared notebook with a book on the side: https://mixkit.co/free-stock-video/student-draws-a-mathematical-chart-over-a-squared-notebook-with-50110/ | 라이선스 Free (확인 2026-10-29) | st14 1:15.7부터(1.8초, 원본 0.3초부터), 원하던 장면: 공부하려고 책과 공책을 펴는 손(글자는 읽히지 않게), 대신함: 책을 펴는 장면이 아니라 모눈 공책을 펴고 쓰기 시작하는 손
- 25596 Young man lays on a bed with a strong stomach ache: https://mixkit.co/free-stock-video/young-man-lays-on-a-bed-with-a-strong-stomach-25596/ | 라이선스 Free (확인 2026-10-29) | st15 1:20.9부터(2.0초, 원본 8.4초부터), 원하던 장면: 침대에 털썩 눕는 사람
- 51400 Portrait of a woman trying to sleep in her bed: https://mixkit.co/free-stock-video/portrait-of-a-woman-trying-to-sleep-in-her-bed-51400/ | 라이선스 Free (확인 2026-10-29) | st16 1:26.9부터(5.4초, 원본 0.2초부터), 원하던 장면: 침대에 누워 천장만 바라보며 일어나지 못하는 사람
- 51397 Young woman using her cell phone lying in her bed: https://mixkit.co/free-stock-video/young-woman-using-her-cell-phone-lying-in-her-bed-51397/ | 라이선스 Free (확인 2026-10-29) | st17 1:39.2부터(2.5초, 원본 0.5초부터), 원하던 장면: 누워서 아무 생각 없이 휴대폰 화면을 넘기는 손(st19와 같은 영상) / st19 1:45.7부터(4.0초, 원본 4.0초부터), 원하던 장면: st17과 같은 영상의 다른 구간(가운데 자막 뒤라 흐리게)
- 50133 A young man wearing a hoodie studying at night in the library with a calculator: https://mixkit.co/free-stock-video/a-young-man-wearing-a-hoodie-studying-at-night-in-50133/ | 라이선스 Free (확인 2026-10-29) | st18 1:41.7부터(4.0초, 원본 0.0초부터), 원하던 장면: 책상에 앉아 집중해서 공부하며 필기하는 사람, 손본 것: 후드티 가슴 글씨와 왼쪽 끝 책 표지 숫자 흐림
- 99909 Close up of a hand writing to do list on a yellow paper notebook: https://mixkit.co/free-stock-video/close-up-of-a-hand-writing-to-do-list-on-99909/ | 라이선스 Free (확인 2026-10-29) | st20 2:03.1부터(3.9초, 원본 6.0초부터), 원하던 장면: 계획을 적은 플래너·달력 위에서 멈춘 지친 손(가운데 자막 뒤라 흐리게) / st62 6:19.2부터(5.0초, 원본 0.5초부터), 원하던 장면: 공책에 계획을 적는 손 클로즈업(뒷줄은 가운데 자막)
- 4733 Scientist observing through a microscope: https://mixkit.co/free-stock-video/scientist-observing-through-a-microscope-4733/ | 라이선스 Free (확인 2026-10-29) | st21 2:10.9부터(3.2초, 원본 1.0초부터), 원하던 장면: 연구실·실험실(장비와 화면, 얼굴이 또렷하지 않게), 대신함: 화면이 있는 연구실 영상은 모두 제한 라이선스라 현미경을 보는 연구자
- 50958 A young woman pedaling on a static bike: https://mixkit.co/free-stock-video/a-young-woman-pedaling-on-a-static-bike-50958/ | 라이선스 Free (확인 2026-10-29) | st22 2:20.9부터(2.3초, 원본 0.0초부터), 원하던 장면: 실내 자전거(고정식 자전거) 페달을 밟는 다리, 흑백 영상
- 26091 Man eats watching television on a rainy night: https://mixkit.co/free-stock-video/man-eats-watching-television-on-a-rainy-night-26091/ | 라이선스 Free (확인 2026-10-29) | st23 2:23.2부터(3.2초, 원본 5.2초부터), 원하던 장면: 차분히 TV(자연 다큐멘터리)를 보는 사람, 화면 속 로고 없이, 대신함: TV 화면은 보이지 않고, 밤 거실에서 TV 쪽을 보며 먹는 사람
- 50961 A young athlete woman pedaling on a stationary bike over a black background: https://mixkit.co/free-stock-video/a-young-athlete-woman-pedaling-on-a-stationary-bike-over-50961/ | 라이선스 Free (확인 2026-10-29) | st24 2:26.4부터(1.1초, 원본 0.5초부터), 원하던 장면: 실내 자전거를 타는 사람(st22와 다른 영상), 흑백 영상
- 50980 A stationary bike at the center of a pristine illuminated backdrop with a young athlete training: https://mixkit.co/free-stock-video/a-stationary-bike-at-the-center-of-a-pristine-illuminated-50980/ | 라이선스 Free (확인 2026-10-29) | st25 2:30.5부터(3.1초, 원본 1.0초부터), 원하던 장면: 실내 자전거를 꾸준히 오래 타는 사람, 흑백 영상, 손본 것: 흰 배경 스튜디오(흑백)라 많이 어둡게
- 50983 A visibly tired young black man exercising on a stationary bike over a white backdrop: https://mixkit.co/free-stock-video/a-visibly-tired-young-black-man-exercising-on-a-stationary-50983/ | 라이선스 Free (확인 2026-10-29) | st26 2:33.6부터(2.6초, 원본 3.0초부터), 원하던 장면: 자전거를 타다 지쳐 멈추고 고개를 숙이는 사람, 흑백 영상, 손본 것: 흰 배경 스튜디오(흑백)라 많이 어둡게
- 32796 Woman starting her stopwatch before running: https://mixkit.co/free-stock-video/woman-starting-her-stopwatch-before-running-32796/ | 라이선스 Free (확인 2026-10-29) | st27 2:38.3부터(3.2초, 원본 2.2초부터), 원하던 장면: 운동 중 심박수를 보여 주는 스마트워치·심박 측정 화면
- 4701 Worried and sad man with his head down: https://mixkit.co/free-stock-video/worried-and-sad-man-with-his-head-down-4701/ | 라이선스 Free (확인 2026-10-29) | st28 2:47.3부터(4.6초, 원본 0.0초부터), 원하던 장면: 머리를 오래 써서 지친 사람(관자놀이를 누름, 가운데 자막 뒤라 흐리게) / st88 8:52.1부터(3.4초, 원본 5.0초부터), 원하던 장면: 머리를 감싸 쥔 지친 사람(가운데 자막 뒤라 흐리게)
- 39840 Young man in front of the computer in an office: https://mixkit.co/free-stock-video/young-man-in-front-of-the-computer-in-an-office-39840/ | 라이선스 Free (확인 2026-10-29) | st29 2:51.9부터(4.7초, 원본 1.0초부터), 원하던 장면: 하루 종일 앉아서 컴퓨터로 일하는 직장인, 손본 것: 모니터 화면(바탕화면과 아이콘 줄) 흐림
- 31414 Man lying down moving a lot because of not being able to sleep: https://mixkit.co/free-stock-video/man-lying-down-moving-a-lot-because-of-not-being-31414/ | 라이선스 Free (확인 2026-10-29) | st30 3:02.6부터(2.3초, 원본 4.8초부터), 원하던 장면: 밤에 잠들지 못하고 뒤척이는 사람
- 31410 Man setting his alarm clock before going to sleep: https://mixkit.co/free-stock-video/man-setting-his-alarm-clock-before-going-to-sleep-31410/ | 라이선스 Free (확인 2026-10-29) | st31 3:04.9부터(3.2초, 원본 0.0초부터), 원하던 장면: 퇴근 후 지쳐 침대 끝에 걸터앉은 사람(가운데 자막 뒤라 흐리게)
- 3525 Feet of a young man with red tennis shoes: https://mixkit.co/free-stock-video/feet-of-a-young-man-with-red-tennis-shoes-3525/ | 라이선스 Free (확인 2026-10-29) | st32 3:11.9부터(4.8초, 원본 1.0초부터), 원하던 장면: 저녁에 운동화나 운동 가방을 앞에 두고 망설이는 지친 사람, 대신함: 운동화나 운동 가방 앞에서 망설이는 영상이 없어 길가에 앉아 발만 움직이는 사람, 손본 것: 운동화의 상표 꼬리표 흐림
- 40754 Man and woman jogging through a park in the city: https://mixkit.co/free-stock-video/man-and-woman-jogging-through-a-park-in-the-city-40754/ | 라이선스 Free (확인 2026-10-29) | st33 3:18.4부터(5.3초, 원본 1.0초부터), 원하던 장면: 공원에서 가볍게 달리거나 운동하는 사람들
- 4534 Worried woman sitting in an armchair: https://mixkit.co/free-stock-video/worried-woman-sitting-in-an-armchair-4534/ | 라이선스 Free (확인 2026-10-29) | st34 3:27.7부터(3.6초, 원본 0.5초부터), 원하던 장면: 안락의자에 지쳐 늘어진 사람(가운데 자막 뒤라 흐리게)
- 4723 Person flipping through a book looking for a page: https://mixkit.co/free-stock-video/person-flipping-through-a-book-looking-for-a-page-4723/ | 라이선스 Free (확인 2026-10-29) | st35 3:31.3부터(6.3초, 원본 0.0초부터), 원하던 장면: 오래된 책을 넘기는 손 + 큰 글씨 2018년, 회복의 역설(2판 그대로)
- 100528 Woman running on treadmill in gym fitness session: https://mixkit.co/free-stock-video/woman-running-on-treadmill-in-gym-fitness-session-100528/ | 라이선스 Free (확인 2026-10-29) | st36 3:37.6부터(4.9초, 원본 0.3초부터), 원하던 장면: 러닝머신에서 힘겹게 뛰는 사람(가운데 자막 뒤라 흐리게)
- 40251 Portrait of a tired fitness man resting at a gym: https://mixkit.co/free-stock-video/portrait-of-a-tired-fitness-man-resting-at-a-gym-40251/ | 라이선스 Free (확인 2026-10-29) | st37 3:42.6부터(8.9초, 원본 0.5초부터), 원하던 장면: 운동화를 든 채 앉아 시작하지 못하는 지친 사람(뒤 두 문장은 가운데 자막), 대신함: 운동화를 들고 있지 않음. 헬스장에서 지쳐 앉아 있는 사람, 손본 것: 티셔츠 가슴의 상표 흐림
- 100529 People exercising on treadmills in a gym: https://mixkit.co/free-stock-video/people-exercising-on-treadmills-in-a-gym-100529/ | 라이선스 Free (확인 2026-10-29) | st38 4:08.2부터(3.5초, 원본 0.6초부터), 원하던 장면: 헬스장 안으로 걸어 들어가는 사람, 헬스장 입구, 대신함: 헬스장 입구 영상이 없어 러닝머신에 올라서는 사람, 손본 것: 러닝머신 계기판 위 작은 상표 흐림
- 25585 Frustrated boy throws a tantrum while working on his computer: https://mixkit.co/free-stock-video/frustrated-boy-throws-a-tantrum-while-working-on-his-computer-25585/ | 라이선스 Free (확인 2026-10-29) | st39 4:15.5부터(1.1초, 원본 0.0초부터), 원하던 장면: 밤에 소파에 지쳐 앉아 있는 사람
- 4596 Man bandaging his hand before boxing: https://mixkit.co/free-stock-video/man-bandaging-his-hand-before-boxing-4596/ | 라이선스 Free (확인 2026-10-29) | st40 4:16.6부터(3.3초, 원본 1.0초부터), 원하던 장면: 운동 가방을 싸는 손(준비 과정), 대신함: 운동 가방을 싸는 영상이 없어 권투 전에 손에 붕대를 감는 손 / st91 9:07.0부터(2.8초, 원본 14.5초부터), 원하던 장면: 주먹을 꽉 쥐는 손(단단한 결심, 가운데 자막 뒤라 흐리게)
- 42845 Man playing guitar in the dark: https://mixkit.co/free-stock-video/man-playing-guitar-in-the-dark-42845/ | 라이선스 Free (확인 2026-10-29) | st41 4:19.9부터(9.3초, 원본 1.0초부터), 원하던 장면: 기타를 안고 앉아 있지만 치지 않는 지친 사람(가운데 자막 뒤라 흐리게), 대신함: 치지 않고 안고만 있는 장면이 아니라 어두운 방에서 기타를 치는 손(흑백, 가운데 자막 뒤라 흐림), 손본 것: 42834는 st06에서 같은 구간을 써서 겹치지 않게 바꿈
- 100555 Woman exercising on treadmill in gym.: https://mixkit.co/free-stock-video/woman-exercising-on-treadmill-in-gym-100555/ | 라이선스 Free (확인 2026-10-29) | st42 4:29.2부터(3.4초, 원본 3.6초부터), 원하던 장면: 지쳤는데도 억지로 운동하다 고개를 떨군 사람, 손본 것: 러닝머신 계기판 위 작은 상표 흐림
- 8744 Young man upset and frustrated receiving a message: https://mixkit.co/free-stock-video/young-man-upset-and-frustrated-receiving-a-message-8744/ | 라이선스 Free (확인 2026-10-29) | st43 4:49.4부터(3.5초, 원본 10.0초부터), 원하던 장면: 퇴근해 들어와 소파에 쓰러지듯 앉는 지친 사람
- 43386 Woman enjoying music while resting: https://mixkit.co/free-stock-video/woman-enjoying-music-while-resting-43386/ | 라이선스 Free (확인 2026-10-29) | st44 4:52.9부터(2.8초, 원본 1.0초부터), 원하던 장면: 소파에서 눈을 감고 편히 쉬는 사람
- 26085 Girl eating salad in her kitchen dining room: https://mixkit.co/free-stock-video/girl-eating-salad-in-her-kitchen-dining-room-26085/ | 라이선스 Free (확인 2026-10-29) | st45 4:55.7부터(1.9초, 원본 3.2초부터), 원하던 장면: 혼자 저녁밥을 차리거나 먹는 모습
- 31413 Young man lying on his bed checking his smartphone: https://mixkit.co/free-stock-video/young-man-lying-on-his-bed-checking-his-smartphone-31413/ | 라이선스 Free (확인 2026-10-29) | st46 4:57.5부터(3.6초, 원본 1.5초부터), 원하던 장면: 밤늦게 침대에서 휴대폰 불빛을 보는 사람, 손본 것: 휴대폰 뒷면의 빛나는 표시 흐림
- 4806 Young woman writes a list on her work schedule: https://mixkit.co/free-stock-video/young-woman-writes-a-list-on-her-work-schedule-4806/ | 라이선스 Free (확인 2026-10-29) | st47 5:01.1부터(1.4초, 원본 2.0초부터), 원하던 장면: 주간 플래너에 운동·취미 일정을 적는 손
- 49918 Close shot of a woman underlining notes with bookmarks: https://mixkit.co/free-stock-video/close-shot-of-a-woman-underlining-notes-with-bookmarks-49918/ | 라이선스 Free (확인 2026-10-29) | st48 5:02.5부터(3.0초, 원본 2.2초부터), 원하던 장면: 달력·플래너의 칸을 지우거나 줄을 긋는 손
- 52072 A young man arrive to the comfy couch in the contemporary decorated living room and puts on a virtual reality headset: https://mixkit.co/free-stock-video/a-young-man-arrive-to-the-comfy-couch-in-the-52072/ | 라이선스 Free (확인 2026-10-29) | st49 5:05.5부터(4.0초, 원본 0.3초부터), 원하던 장면: 집에 돌아와 문을 열고 열쇠를 내려놓는 모습, 대신함: 문을 열고 열쇠를 내려놓는 영상은 모두 제한 라이선스라 집에 들어와 소파에 앉는 사람
- 250 Woman sits on a couch drinking coffee: https://mixkit.co/free-stock-video/woman-sits-on-a-couch-drinking-coffee-250/ | 라이선스 Free (확인 2026-10-29) | st50 5:09.5부터(4.5초, 원본 4.0초부터), 원하던 장면: 소파에서 따뜻한 차를 마시며 쉬는 사람(첫 줄은 가운데 자막), 손본 것: 4~9초는 컵을 입에 대고 마셔서 컵 글씨가 안 보임(2.5초부터는 컵 글씨가 보임), 밝은 창가라 많이 어둡게
- 3210 Couple sleeps on couch: https://mixkit.co/free-stock-video/couple-sleeps-on-couch-3210/ | 라이선스 Free (확인 2026-10-29) | st51 5:14.1부터(1.4초, 원본 2.4초부터), 원하던 장면: 소파에서 잠깐 조는 사람
- 52110 A young woman clad in black workout attire exercise at the gym does lunges with dumbbells on her hands: https://mixkit.co/free-stock-video/a-young-woman-clad-in-black-workout-attire-exercise-at-52110/ | 라이선스 Free (확인 2026-10-29) | st53 5:29.4부터(4.3초, 원본 2.0초부터), 원하던 장면: 어두운 체육관에서 덤벨 운동을 하는 사람
- 4851 Girl running during sunset ties her shoelaces: https://mixkit.co/free-stock-video/girl-running-during-sunset-ties-her-shoelaces-4851/ | 라이선스 Free (확인 2026-10-29) | st54 5:48.3부터(1.6초, 원본 9.0초부터), 원하던 장면: 의욕적으로 운동복을 입거나 운동화 끈을 단단히 묶는 사람
- 26092 Young man eating while watching television: https://mixkit.co/free-stock-video/young-man-eating-while-watching-television-26092/ | 라이선스 Free (확인 2026-10-29) | st55 5:49.9부터(2.8초, 원본 0.3초부터), 원하던 장면: 소파에서 TV만 보는 사람(운동 가방은 그대로)
- 40881 Man and woman jogging together on the street: https://mixkit.co/free-stock-video/man-and-woman-jogging-together-on-the-street-40881/ | 라이선스 Free (확인 2026-10-29) | st56 5:56.1부터(2.0초, 원본 1.0초부터), 원하던 장면: 활발하게 운동하는 사람들(달리기, 헬스장)
- 51393 Sleepy woman looking out the window at night: https://mixkit.co/free-stock-video/sleepy-woman-looking-out-the-window-at-night-51393/ | 라이선스 Free (확인 2026-10-29) | st57 5:58.1부터(1.1초, 원본 0.8초부터), 원하던 장면: 창밖을 보며 무언가를 바라는 사람(가운데 자막 뒤라 흐리게)
- 42655 A woman writing in her spiral notebook: https://mixkit.co/free-stock-video/a-woman-writing-in-her-spiral-notebook-42655/ | 라이선스 Free (확인 2026-10-29) | st58 5:59.1부터(3.3초, 원본 0.5초부터), 원하던 장면: 공책에 계획을 적는 손(가운데 자막 뒤라 흐리게)
- 99890 Close up a hand writing notes on a notebook with a pen: https://mixkit.co/free-stock-video/close-up-a-hand-writing-notes-on-a-notebook-with-99890/ | 라이선스 Free (확인 2026-10-29) | st59 6:06.8부터(2.9초, 원본 0.3초부터), 원하던 장면: 포스트잇이나 수첩에 선택지를 적는 손
- 2858 The hand of a person drawing: https://mixkit.co/free-stock-video/the-hand-of-a-person-drawing-2858/ | 라이선스 Free (확인 2026-10-29) | st61 6:14.7부터(2.2초, 원본 2.0초부터), 원하던 장면: 그림 한 장을 공들여 완성하는 손(그림 그리기, 채색)
- 50759 A young man stretches his arms on the balcony: https://mixkit.co/free-stock-video/a-young-man-stretches-his-arms-on-the-balcony-50759/ | 라이선스 Free (확인 2026-10-29) | st63 6:31.9부터(3.7초, 원본 3.0초부터), 원하던 장면: 집에서 가볍게 스트레칭하는 사람
- 101368 Close-Up of Girl Tying Sneakers: https://mixkit.co/free-stock-video/close-up-of-girl-tying-sneakers-101368/ | 라이선스 Free (확인 2026-10-29) | st64 6:39.8부터(2.2초, 원본 1.5초부터), 원하던 장면: 현관에 운동화를 미리 꺼내 두는 손(가운데 자막 뒤라 흐리게), 대신함: 현관에 운동화를 꺼내 두는 영상이 없어 운동화 끈을 묶는 손(가운데 자막 뒤라 흐림)
- 52136 A young runner woman dressed in a black sports outfit starts a countdown on her smartwatch: https://mixkit.co/free-stock-video/a-young-runner-woman-dressed-in-a-black-sports-outfit-52136/ | 라이선스 Free (확인 2026-10-29) | st65 6:50.6부터(3.5초, 원본 1.5초부터), 원하던 장면: 손목의 스마트워치를 눌러 운동을 끝내는 손
- 723 Jogger stopping to take a breath: https://mixkit.co/free-stock-video/jogger-stopping-to-take-a-breath-723/ | 라이선스 Free (확인 2026-10-29) | st66 6:54.0부터(5.2초, 원본 2.0초부터), 원하던 장면: 달리다 멈춰 숨을 고르는 사람
- 40012 Two excited girls during a pottery class: https://mixkit.co/free-stock-video/two-excited-girls-during-a-pottery-class-40012/ | 라이선스 Free (확인 2026-10-29) | st67 7:08.6부터(2.8초, 원본 3.7초부터), 원하던 장면: 즐거운 얼굴로 취미를 하는 사람(그림, 뜨개질 등, 가운데 자막 뒤라 흐리게)
- 574 A woman reading a book on her bed: https://mixkit.co/free-stock-video/a-woman-reading-a-book-on-her-bed-574/ | 라이선스 Free (확인 2026-10-29) | st68 7:28.9부터(5.6초, 원본 4.5초부터), 원하던 장면: 침대에서 즐겁게 책을 읽는 사람(가운데 자막 뒤라 흐리게)
- 608 Silhouette of a runner in the city: https://mixkit.co/free-stock-video/silhouette-of-a-runner-in-the-city-608/ | 라이선스 Free (확인 2026-10-29) | st69 7:39.8부터(1.1초, 원본 3.0초부터), 원하던 장면: 혼자 달리는 사람
- 5172 Woman painting in her studio while watching a tutorial on her laptop: https://mixkit.co/free-stock-video/woman-painting-in-her-studio-while-watching-a-tutorial-on-5172/ | 라이선스 Free (확인 2026-10-29) | st70 7:43.8부터(1.8초, 원본 3.5초부터), 원하던 장면: 노트북의 그림 강의를 보며 따라 그리는 사람, 손본 것: 위쪽 벽의 신문 제목이 읽혀 위 25%를 잘라 냄, 노트북 덮개의 사과 로고는 흐림
- 662 Woman playing an acoustic guitar in her living room: https://mixkit.co/free-stock-video/woman-playing-an-acoustic-guitar-in-her-living-room-662/ | 라이선스 Free (확인 2026-10-29) | st71 7:48.7부터(6.8초, 원본 3.0초부터), 원하던 장면: 집에서 편하게 기타를 치는 사람
- 50126 A young student wearing a hoodie hilight texts on a book while atuding in the: https://mixkit.co/free-stock-video/a-young-student-wearing-a-hoodie-hilight-texts-on-a-50126/ | 라이선스 Free (확인 2026-10-29) | st72 7:55.6부터(2.1초, 원본 4.5초부터), 원하던 장면: 두꺼운 공부 책에 형광펜을 긋는 손, 손본 것: 후드티 가슴의 글씨 흐림
- 42741 Girl reading a book sitting near a window: https://mixkit.co/free-stock-video/girl-reading-a-book-sitting-near-a-window-42741/ | 라이선스 Free (확인 2026-10-29) | st73 7:57.7부터(2.3초, 원본 7.0초부터), 원하던 장면: 소설에 빠져 읽는 사람
- 42188 Young woman putting together a puzzle: https://mixkit.co/free-stock-video/young-woman-putting-together-a-puzzle-42188/ | 라이선스 Free (확인 2026-10-29) | st74 8:00.0부터(6.9초, 원본 0.5초부터), 원하던 장면: 편하게 취미를 즐기는 사람(뒷문장은 가운데 자막)
- 1781 Typing on a laptop, close up.: https://mixkit.co/free-stock-video/typing-on-a-laptop-close-up-1781/ | 라이선스 Free (확인 2026-10-29) | st75 8:06.9부터(4.3초, 원본 0.5초부터), 원하던 장면: 밤늦게 노트북으로 일하는 사람
- 87 Tracking a man through the forest: https://mixkit.co/free-stock-video/tracking-a-man-through-the-forest-87/ | 라이선스 Free (확인 2026-10-29) | st76 8:17.8부터(3.1초, 원본 1.0초부터), 원하던 장면: 77번 사진 자리(임시): 휴일에 길게 하는 활동(자전거, 등산 등 낮 야외), 대신함: 77번 사진이 오지 않아 넣은 임시 장면
- 52119 A young beautiful woman clad in black sportswear stretch her hands before the morning jog: https://mixkit.co/free-stock-video/a-young-beautiful-woman-clad-in-black-sportswear-stretch-her-52119/ | 라이선스 Free (확인 2026-10-29) | st77 8:20.9부터(2.2초, 원본 0.3초부터), 원하던 장면: 아침 햇살 속에서 스트레칭하는 사람
- 28899 Woman turning off her alarm clock in the morning: https://mixkit.co/free-stock-video/woman-turning-off-her-alarm-clock-in-the-morning-28899/ | 라이선스 Free (확인 2026-10-29) | st78 8:23.1부터(3.0초, 원본 4.2초부터), 원하던 장면: 이른 아침 알람을 끄는 졸린 손
- 99834 Raindrops on glass with blurred city lights in the background: https://mixkit.co/free-stock-video/raindrops-on-glass-with-blurred-city-lights-in-the-background-99834/ | 라이선스 Free (확인 2026-10-29) | st79 8:26.2부터(5.3초, 원본 1.0초부터), 원하던 장면: 밤 창밖의 도시 불빛(가운데 자막 뒤라 흐리게)
- 660 Woman sipping from a mug at home: https://mixkit.co/free-stock-video/woman-sipping-from-a-mug-at-home-660/ | 라이선스 Free (확인 2026-10-29) | st80 8:31.5부터(5.3초, 원본 1.0초부터), 원하던 장면: 저녁에 창가에서 차를 마시며 쉬는 사람
- 39779 Hand of a man looking at his smart watch: https://mixkit.co/free-stock-video/hand-of-a-man-looking-at-his-smart-watch-39779/ | 라이선스 Free (확인 2026-10-29) | st81 8:36.8부터(3.7초, 원본 0.0초부터), 원하던 장면: 퇴근길에 손목시계를 보는 사람, 대신함: 퇴근길이 아니라 실내 소파에서 스마트워치를 보는 손목
- 28887 Top of a wall clock in a close-up shot: https://mixkit.co/free-stock-video/top-of-a-wall-clock-in-a-close-up-shot-28887/ | 라이선스 Free (확인 2026-10-29) | st82 8:40.5부터(1.9초, 원본 3.0초부터), 원하던 장면: 시계(7시 무렵), 대신함: 7시를 가리키는 무료 영상이 없어 시계 윗부분(11~1)만 보이는 장면
- 5048 Young man doing push-ups on the floor: https://mixkit.co/free-stock-video/young-man-doing-push-ups-on-the-floor-5048/ | 라이선스 Free (확인 2026-10-29) | st83 8:42.4부터(0.9초, 원본 1.4초부터), 원하던 장면: 집에서 팔굽혀펴기 등 운동하는 사람
- 1724 A person reading a book, close up: https://mixkit.co/free-stock-video/a-person-reading-a-book-close-up-1724/ | 라이선스 Free (확인 2026-10-29) | st84 8:43.3부터(2.1초, 원본 1.0초부터), 원하던 장면: 책을 읽는 사람, 손본 것: 책 글씨 몇 줄과 BIB 도장이 원래 크기에서 거의 읽혀 살짝 흐림
- 924 Silhouette of woman opening a window: https://mixkit.co/free-stock-video/silhouette-of-woman-opening-a-window-924/ | 라이선스 Free (확인 2026-10-29) | st85 8:45.4부터(2.2초, 원본 0.5초부터), 원하던 장면: 밤 창가에 선 사람의 실루엣(가운데 자막 뒤라 흐리게), 손본 것: 낮 창가의 실루엣이라 많이 어둡게(가운데 자막 뒤라 흐림)
- 134 A man being followed walking in a city: https://mixkit.co/free-stock-video/a-man-being-followed-walking-in-a-city-134/ | 라이선스 Free (확인 2026-10-29) | st86 8:47.6부터(2.4초, 원본 1.0초부터), 원하던 장면: 밤길을 걸어 집으로 돌아오는 지친 사람(가운데 자막 뒤라 흐리게), 대신함: 밤길 영상이 없어 맑은 낮 거리를 걷는 뒷모습을 어둡게(가운데 자막 뒤라 흐림), 손본 것: 한낮 거리라 많이 어둡게(가운데 자막 뒤라 흐림)
- 2848 Marking Christmas day on the calendar: https://mixkit.co/free-stock-video/marking-christmas-day-on-the-calendar-2848/ | 라이선스 Free (확인 2026-10-29) | st87 8:50.0부터(2.1초, 원본 0.0초부터), 원하던 장면: 빈 칸이 많은 플래너·달력(가운데 자막 뒤라 흐리게), 대신함: 빈 플래너 영상이 없어 달력의 25에 동그라미를 치는 장면(HOLIDAY 글씨는 흐림), 손본 것: 달력의 손글씨 HOLIDAY가 가운데 자막 뒤 흐림으로도 읽혀서 그 자리를 따로 더 흐림
- 40242 Fitness man throwing dumbbells to the floor: https://mixkit.co/free-stock-video/fitness-man-throwing-dumbbells-to-the-floor-40242/ | 라이선스 Free (확인 2026-10-29) | st89 8:55.5부터(5.6초, 원본 0.0초부터), 원하던 장면: 운동 가방을 바닥에 내려놓는 모습, 대신함: 운동 가방 대신 덤벨을 바닥에 내려놓고 지쳐 앉는 사람, 손본 것: 보라색 조명이 강해 채도를 낮춤
- 42904 Woman meditating and breathing deeply: https://mixkit.co/free-stock-video/woman-meditating-and-breathing-deeply-42904/ | 라이선스 Free (확인 2026-10-29) | st90 9:01.1부터(6.0초, 원본 5.0초부터), 원하던 장면: 눈을 감고 깊게 숨을 쉬며 쉬는 사람(가운데 자막 뒤라 흐리게)
- 40136 Woman tying shoelaces during a training: https://mixkit.co/free-stock-video/woman-tying-shoelaces-during-a-training-40136/ | 라이선스 Free (확인 2026-10-29) | st92 9:09.8부터(3.9초, 원본 2.8초부터), 원하던 장면: 포근한 소파에서 쉬다 운동화 끈을 묶는 사람(가운데 자막 뒤라 흐리게), 대신함: 소파 장면은 없고, 낮 공원에서 운동화 끈을 묶는 사람(마스크를 씀, 가운데 자막 뒤라 흐림)
- 43444 Artist painting painting on a canvas: https://mixkit.co/free-stock-video/artist-painting-painting-on-a-canvas-43444/ | 라이선스 Free (확인 2026-10-29) | st93 9:13.7부터(6.3초, 원본 1.0초부터), 원하던 장면: 저녁에 편하게 취미를 즐기는 모습이나 밤의 도시(가운데 자막 뒤라 흐리게)

## 6. 배경음악 (Mixkit Stock Music Free License)

AI는 소리를 들을 수 없어서, 곡의 태그와 소리 크기 변화(3초 창 RMS)로 골랐습니다. 곡마다 한 가지 크기로 맞추고(-36 LUFS, 곡 사이 3초 겹침), 목소리와 섞은 전체는 -14 LUFS입니다.

- 0:00.0~1:05.5 Classical 7 / Jonny S. (곡 714, 0초부터): ① 도입: 퇴근 뒤 지친 저녁 (Film Score, Reflective, Piano, Soft, Human Drama)
- 1:05.5~2:06.6 Staring at the Night Sky / Alejandro Magaña (A. M.) (곡 168, 0초부터): ② 수요일 저녁 8시: 조용한 밤 (Mysterious, Atmospheric, Cello, Piano, Relaxation)
- 2:06.6~3:16.3 Tapis / Eugenio Mininni (곡 615, 0초부터): ③ 마코라 실험: 차분한 궁금증 (Film Score, Mysterious, Atmospheric, Synth)
- 3:16.3~4:38.2 Classical 2 / Jonny S. (곡 709, 0초부터): ④ 회복의 역설과 좋아하는 일의 수고: 생각에 잠김 (Hopeful, Reflective, Piano, Melodic)
- 4:38.2~5:35.3 Alignment / Arulo (곡 310, 0초부터): ⑤-1 쉴 시간을 먼저: 다정한 위로 (Hopeful, Reflective, Piano, Relaxation)
- 5:35.3~7:07.6 Classical 6 / Jonny S. (곡 713, 0초부터): ⑤-2 작은 분량과 짧은 준비: 차분한 희망 (Hopeful, Reflective, Piano, Documentary)
- 7:07.6~8:36.4 Classical vibes 2 / Grigoriy Nuzhny (곡 682, 5초부터): ⑤-3 즐거운 쪽 고르기: 가벼운 밝음 (Uplifting, Hopeful, Piano, Slow)
- 8:36.4~9:20.0 A New Life / Eugenio Mininni (곡 543, 22초부터): ⑥ 마무리: 따뜻한 끝 (Hopeful, Reflective, Strings, Cinematic, Documentary)

## 7. 점검

- 파일: h264 1920×1080 30fps yuv420p, 프레임 16800개 (560.0초×30 = 16800), 소리 aac(320kbps로 인코딩, 실제 평균 302kbps) 48000Hz 2채널, 길이 560.00초.
- 소리 크기: 전체 -14.0 LUFS, 최고 -1.5 dBTP, 크기 변화 폭(LRA) 3.1 LU.
- 장면 182개(스톡 94, 사진 77, 검은 화면 11), 자막 450줄. 장면과 자막은 목소리 시작 시각에 바뀝니다.
- 스톡 라이선스: 쓴 영상 86개 모두 영상 페이지의 copyrightNotice가 Free(2026-10-29 확인, stock/items/lic_*.json). 음악 8곡은 Mixkit Stock Music Free License.
- 스톡 화면 점검: 스톡 장면 94개를 실제 화면(색, 흐림, 자막 포함)으로 한 장씩, 흐림 상자나 잘라내기가 있는 10개는 처음·가운데·끝 세 장씩 뽑아 봤습니다(checkframes.py, 114장). 후드티 글씨(st18)와 달력 HOLIDAY(st87)가 읽혀서 흐림 자리를 옮기고 더 흐리게 한 뒤 다시 확인했습니다. 운동화 VANS(st32), 티셔츠 Nike(st37), 노트북 사과 로고(st70), 후드티 글씨(st72)는 원래 크기에서 흐림이 덮는 것을 확인했습니다.
- 글자 검사(tesseract, 스톡은 초당 2장, 사진은 1장씩, 711장): 글자로 잡힌 18장면을 눈으로 봤습니다. 스톡 10장면은 무늬를 글자로 잘못 읽은 것이고, 사진 8장면은 사진 속 일반 낱말(WED, ENGLISH, PASSPORT, Workout Schedule, British Journal of Psychology, Group A/B, WEEKLY PLANNER)이었습니다. 상표는 없었습니다(checks/ocr_hits.json).
- 720p로만 받을 수 있던 스톡 6개(100530, 100528, 100529, 100555, 101368, 99834)는 1080p로 키워서 다른 장면보다 조금 덜 선명합니다.
- 완성 파일에서 뽑은 화면(15장)으로 처음과 끝이 서서히 밝아지고 어두워지는 것, 사진, 검은 화면, 큰 글씨를 확인했습니다. 큰 글씨 네 개(2018년, 회복의 역설, 2002년, 실행 의도)는 그 말이 나올 때 나타납니다.

## 8. 다시 만드는 순서

run_v1.sh 순서대로입니다. 커밋하지 않은 준비물(녹음, 사진, 스톡 원본, 음악 원본, 모델, 글꼴)은 그 파일 첫머리에 적었습니다.

## 9. 사용자 확인이 필요한 것

1. '<< >>' 표시(존넨탁 문장)의 뜻을 알려 주세요. 지금은 2판처럼 오래된 책 스톡과 큰 글씨입니다.
2. 77번 사진을 보내 주시면 임시 스톡(긴 활동은 휴일에 하는 것이죠 부분) 자리에 넣겠습니다.
3. 54번 자리에 쓸 사진: 지금은 먼저 온 것(in54)입니다. 다음에 온 다른 버전(in55)이 맞으면 알려 주세요.
4. photo_map.jpg에서 사진 번호가 맞는지 봐 주세요. 특히 1~10번(순서가 바뀌어 온 것으로 보인 두 메시지)입니다.
5. 검은 화면 11곳을 그대로 둘지, 스톡이나 사진으로 바꿀지 알려 주세요.
6. 배경음악은 AI가 들을 수 없어 곡의 태그와 소리 크기 변화로 골랐습니다. 들어 보시고 바꿀 곡을 알려 주세요.
7. 맞는 무료 영상이 없어 비슷한 장면으로 대신한 스톡 17곳과 77번 자리의 임시 스톡 1곳이 있습니다(5장의 '대신함'). 바꾸고 싶은 곳을 알려 주세요.
8. 사진풍 AI 사진을 썼으므로, 업로드할 때 '변경되거나 합성된 콘텐츠'를 '예'로 체크해 주세요(채널 작업 문서의 업로드 항목).
9. 마지막 '댓글로 공유해 주세요.'는 표시한 대본에 없지만 녹음에 있어 넣었습니다. 빼야 하면 알려 주세요.
10. 52번 사진(2002년 밀른 연구 부분)의 책에 'British Journal of Psychology'라는 글씨가 작게 보입니다. 이 연구가 실린 학술지는 British Journal of Health Psychology입니다(plan/fact.md). 사진은 그대로 두었습니다. 흐리거나 바꿀지 알려 주세요.
