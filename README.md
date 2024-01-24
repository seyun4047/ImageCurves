# ImageCurves

여러 이미지 편집 프로그램의 Image Curve를 본인만의 방식으로 구현하기 위해 프로젝트를 시작함.

------------------
**모듈 소개**

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
**Principal Update List**

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
