import cv2
import numpy as np
import sys
from collections import deque
import sys
from collections import deque
from scipy.optimize import curve_fit

# image setting with cv2
oriImg = cv2.imread("src/img/test.JPG")
oriImg = cv2.cvtColor(oriImg, cv2.COLOR_BGR2GRAY)
ih, iw = oriImg.shape[:2]
# cv2.imshow("img", oriImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(iw,ih)
# find that color(brightness) Algorithm

#-----------------------------------------------------
# 0~255 해당하는 좌표값 찾아서 리스트로 구성예정
def findThatColor(cnum, ih, iw):
    # use bfs
    visited = [[0]*(ih+1) for _ in range(iw+1)]

    # print(visited)
    dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
    q = deque()
    q.append([0, 0])
    visited[0][0] = 1
    while q:
        # print("hi")
        cx, cy = q.popleft()
        for dx,dy in dir:
            # print("hi")
            nx=cx+dx
            ny=cy+dy
            # print(nx,ny)
            if 0<=nx<=iw-1 and 0<=ny<=ih-1 and visited[nx][ny]==0:
                q.append([nx,ny])
                # print("hi")
                if oriImg[ny][nx] == cnum:
                    print("(",nx,ny,")")
                visited[nx][ny] = 1

#-----------------------------------------------------
# 커브 그리기
# left는 right 보다 무조건 작다가정
# def cubic_function(x, a, b, c, d):
#     return a * x**3 + b * x**2 + c * x + d

#-----------------------------------------------------
# 방정식을 찾고 left dot pos, right dot pos, cur pos를 지나는 이차함수를 알아내 곡선을 그림
def find_eq(x, a, b, c):
    return a * x**2 + b * x + c

#-----------------------------------------------------
# curve의 Y값 이 변하면 지금 찍힌 점의 왼쪽, 오른쪽 점을 파악하고 선을 부드러운 곡선으로 만들기위해 변경되는 Y값을 반환함
def transCurve(X, Y, userX, userY):
    # left는 right 보다 무조건 작다가정
    # X = [0, 63, 127, 191, 255]
    X.append(userX)
    X.sort()
    # Y = [0, 63, 127, 191, 255]
    Y.append(userY)
    Y.sort()
    xIdx = X.index(userX)
    yIdx = Y.index(userY)

    newX = [X[xIdx-1], userX, X[xIdx+1]]
    newY = [Y[yIdx - 1], userY, Y[yIdx + 1]]
    # print(newX,newY)

    # lDotPos = [X.index(userX)-1,X.index(userY)-1]
    # rDotPos = [X.index(userX)+1,X.index(userY)+1]
    coef, _ = curve_fit(find_eq, newX, newY)
    x_range = np.linspace(X[xIdx-1], X[xIdx+1], X[xIdx+1]-X[xIdx-1]+1)
    x_range = np.round(x_range)
    # print("x",x_range)
    y_predicted = find_eq(x_range, *coef)
    y_predicted = np.round(y_predicted)
    # midIdx = len(x_range) // 2
    # x_range = np.delete(x_range, midIdx)
    # y_predicted = np.delete(y_predicted, midIdx)

    # X.extend(x_range.tolist())
    # Y.extend(y_predicted.tolist())

    # print("y:",y_predicted)  # 추정된 모델을 이용하여 y 예측

    # print("rX",X,"rY",Y)
    # leftDotPos ~ curPos ~ rightDotPos 구간까지의 X에 대응하는 Y 를 반환하여
    # 해당하는 컬러를 가진 픽셀의 컬러 변경
    # return leftDotX, rightDotX, y_predicted
    # lDot~rDot 사이의 길이를 알면 변경해야되는 컬러의 개수를 알수 있음.
    return X[xIdx-1], X[xIdx+1], y_predicted

#-----------------------------------------------------
# 원래 curveList와 변경되는 changedColorList를 가져와 색을 변환함.
def changeCurve(curveList, changedColorList, lDotX, rDotX):
    count=0
    # colorRangeLen = rDotX - lDotX + 1
    for colorIdx in range(lDotX+1, rDotX, 1):
        curveList[colorIdx] = changedColorList[count]
        count += 1
    print(curveList)

#-----------------------------------------------------
curveList = [i for i in range(0,256,1)] # CurveList x좌표: idx | y좌표: idx에 해당하는 값
X = [0, 63, 127, 191, 255]
Y = [0, 63, 127, 191, 255]
# print(transCurve(X, Y, 150,170))
# print(findThatColor(157, ih, iw))
# print(oriImg[1140][1279])

lDotX, rDotX, changedColorList = transCurve(X,Y,150,170) # X: 150인 값을 170으로 바꿨을 때
changeCurve(curveList, changedColorList, lDotX, rDotX)
# print(lDotX,rDotX,changedColor)
# print(len(changedColor))
# print(colorRangeLen)

