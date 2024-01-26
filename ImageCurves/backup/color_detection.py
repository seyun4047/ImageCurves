import cv2
import sys
import sys
import numpy as np
import matplotlib.pyplot as plt
from collections import deque
from scipy.optimize import curve_fit
# image setting with cv2
# oriImg = cv2.imread("src/img/test.JPG")
# oriImg = cv2.cvtColor(oriImg, cv2.COLOR_BGR2GRAY)
# ih, iw = oriImg.shape[:2]
# cv2.imshow("img", oriImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()
# print(iw,ih)
# find that color(brightness) Algorithm

#-----------------------------------------------------
class Detect_color:
    # oriImg = cv2.imread("")
    # ih = 0
    # iw = 0
# 0~255 해당하는 좌표값 찾아서 리스트로 구성예정
    def __init__(self, src):
        self.realImg = cv2.imread(src)
        self.oriImg = cv2.cvtColor(self.realImg, cv2.COLOR_BGR2GRAY)
        self.ih, self.iw = self.oriImg.shape[:2]

    def getOriImg(self):
        return self.oriImg
    def getRealImg(self):
        return self.realImg
    def getHW(self):
        return self.ih, self.iw
    def findThatColor(self, cnum, ih, iw):
        # use bfs
        visited = [[0]*(ih+1) for _ in range(iw+1)]

        # print(visited)
        dir = [[-1, 0], [1, 0], [0, -1], [0, 1]]
        q = deque()
        q.append([0, 0])
        visited[0][0] = 1
        while q:
            cx, cy = q.popleft()
            for dx,dy in dir:
                nx=cx+dx
                ny=cy+dy
                if 0<=nx<=iw-1 and 0<=ny<=ih-1 and visited[nx][ny]==0:
                    q.append([nx,ny])
                    if self.oriImg[ny][nx] == cnum:
                        print("(",nx,ny,")")
                    visited[nx][ny] = 1

    #-----------------------------------------------------
    # 방정식을 찾고 left dot pos, right dot pos, cur pos를 지나는 이차함수를 알아내 곡선을 그림
    def find_eq(self, x, a, b, c):
        return a * x**2 + b * x + c

    #-----------------------------------------------------
    # curve의 Y값 이 변하면 지금 찍힌 점의 왼쪽, 오른쪽 점을 파악하고 선을 부드러운 곡선으로 만들기위해 변경되는 Y값을 반환함
    def transCurve(self, X, Y, userX, userY):
        if userX in X:
            xIdx = X.index(userX)
            Y[xIdx] = userY
        else:
            X.append(userX)
            X.sort()
            xIdx = X.index(userX)
        tmpX = [i for i in range(X[xIdx-1]+1, X[xIdx+1], 1)]
        newX = [X[xIdx-1], userX, X[xIdx+1]]
        newY = [Y[X[xIdx-1]], userY, Y[X[xIdx+1]]]

        coef, _ = curve_fit(self.find_eq, newX, newY)
        x_range = np.round(tmpX)
        y_predicted = self.find_eq(x_range, *coef)
        y_predicted = np.round(y_predicted)

        return X, Y, X[xIdx-1], X[xIdx+1], y_predicted
        # leftDotPos ~ curPos ~ rightDotPos 구간까지의 X에 대응하는 Y 를 반환하여
        # 해당하는 컬러를 가진 픽셀의 컬러 변경
        # lDot~rDot 사이의 길이를 알면 변경해야되는 컬러의 개수를 알수 있음.
    #-----------------------------------------------------
    # 원래 curveList와 변경되는 changedColorList를 가져와 색을 변환함.
    def changeCurve(self, curveList, changedColorList, lDotX, rDotX):
        count=0
        # colorRangeLen = rDotX - lDotX + 1
        for colorIdx in range(lDotX+1, rDotX, 1):
            c = changedColorList[count]
            if c>255:
                curveList[colorIdx] = 255
            elif c<0:
                curveList[colorIdx] = 0
            else:
                curveList[colorIdx] = int(c)
            count += 1
        # print(curveList)
        return curveList

    def drawCurve(self, curveList, X):

        plt.axis([0, 255, 0, 255])


        # plt.xticks([0,63,127,191,255], labels=[])
        # plt.yticks([0,63,127,191,255], labels=[])

        plt.xticks([0, 63, 127, 191, 255])
        plt.yticks([0, 63, 127, 191, 255])

        # 가로선
        plt.axhline(y=63, color='black', linestyle='-', linewidth=0.7)
        plt.axhline(y=127, color='black', linestyle='-', linewidth=0.7)
        plt.axhline(y=191, color='black', linestyle='-', linewidth=0.7)

        # 세로선
        plt.axvline(x=63, color='black', linestyle='-', linewidth=0.7)
        plt.axvline(x=127, color='black', linestyle='-', linewidth=0.7)
        plt.axvline(x=191, color='black', linestyle='-', linewidth=0.7)

        tmp_x = [i for i in range(0, 256, 1)]
        tmp_y = curveList
        clickedY = [tmp_y[i] for i in X]
        plt.plot(X, clickedY, "r.")
        plt.plot(tmp_x, tmp_y, "b-")
        plt.show()

#-----------------------------------------------------
# settings
# curveList = [i for i in range(0,256,1)] # CurveList x좌표: idx | y좌표: idx에 해당하는 값
# # print(curveList)
# X = [0, 63, 127, 191, 255]
# fT = Detect_color("src/img/test.JPG")
# #-----------------------------------------------------
# # test
# X, Y, lDotX, rDotX, changedColorList = fT.transCurve(X,curveList,150,170) # X: 150인 값을 170으로 바꿨을 때
# curveList = fT.changeCurve(curveList, changedColorList, lDotX, rDotX)
#
# X, Y, lDotX, rDotX, changedColorList = fT.transCurve(X,curveList,100,200) # X: 150인 값을 170으로 바꿨을 때
# curveList = fT.changeCurve(curveList, changedColorList, lDotX, rDotX)
#
# X, Y, lDotX, rDotX, changedColorList = fT.transCurve(X,curveList,40,200) # X: 150인 값을 170으로 바꿨을 때
# curveList = fT.changeCurve(curveList, changedColorList, lDotX, rDotX)
# #-----------------------------------------------------
# # Image Curve 시각화
# fT.drawCurve(curveList, X)