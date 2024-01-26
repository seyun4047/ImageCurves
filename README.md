# ImageCurves
## 여러 이미지 편집 프로그램의 Image Curve를 본인만의 방식으로 구현하기 위해 프로젝트를 시작함.

------------------
------------------
#구현 곡선
## S자 커브 곡선
<img width="1322" alt="스크린샷 2024-01-25 02 38 54" src="https://github.com/seyun4047/ImageCurves/assets/73819780/0722bc39-77cd-4f18-ab50-635f957af52f">

63구간(shadow, 50)을 낮추고 191구간(highlight, 220)을 높여 이미지의 중간톤 콘트라스트를 높이는 기법을 구현함.

------------------
------------------
# 모듈 소개

color_detection
변화된 커브를 감지하고
변화된 list를 반환

color_set _creator
1. 이미지를 array로 받아들임
2. List[0-255] = [xn,yn]
3. 색상변환: k->i
4. tmp = list[k].좌표모두빼기(); list[i] = tmp;
5. array재구성: List[0-255: t] -> xn,yn = t
6. opencv로 재구성 이미지 반환

------------------
------------------
# 개선이 요구되는 점

<img width="861" alt="스크린샷 2024-01-26 20 45 36" src="https://github.com/seyun4047/ImageCurves/assets/73819780/fa89735e-7ff6-41b8-be6b-ab9ce121bcbb">

<img width="1151" alt="스크린샷 2024-01-26 20 44 19" src="https://github.com/seyun4047/ImageCurves/assets/73819780/8bed5c94-9c0b-4b04-8293-02381d0a5edb">

255로 몰리는 현상
-> eq 알고리즘 개선 필요

------------------
------------------
# Principal Update List

20/01
find_thatcolor_def 구현-bfs
테스트를위한 resize_img 구현

21/01
transCurve 구현: curve의 Y값 이 변하면 지금 찍힌 점의 왼쪽, 오른쪽 점을 파악하고 선을 부드러운 곡선으로 만들기위해 변경되는 Y값을 반환함
changeCurve 구현: curveList와 변경되는 changedColorList를 가져와 색을 변환함.

25/01
color_set_creator
변화한 곡선 colorMapped: (list[x] = y) 를 기반으로 reImg(재구성 이미지)를 구성하고 반환

모든 모듈 class화

모듈이름 변경 find_thatcolor_func -> color_detection
test code 작성

------------------
------------------
