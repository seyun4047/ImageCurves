import numpy as np

from color_detection import Detect_color
from color_set_creator import Color_set_creator
import cv2
import matplotlib.pylab as plt
# Window setting
def win_con():
    cv2.namedWindow('before', cv2.WINDOW_NORMAL)
    # cv2.namedWindow('before[grayScale]', cv2.WINDOW_NORMAL)
    cv2.namedWindow('after', cv2.WINDOW_NORMAL)

    cv2.resizeWindow('before', 500, 500)
    # cv2.resizeWindow('before[grayScale]', 500, 500)
    cv2.resizeWindow('after', 500, 500)

    cv2.moveWindow('before', 0, 0)
    # cv2.moveWindow('before[grayScale]', 500, 0)
    cv2.moveWindow('after', 1000, 0)

    cv2.imshow('before', realImg)
    # cv2.imshow('before[grayScale]', oriImg)
    cv2.imshow('after', reImg)


X = [0, 63, 127, 191, 255]
curveList = [i for i in range(0,256,1)] # CurveList x좌표: idx | y좌표: idx에 해당하는 값
DC = Detect_color("src/img/test.JPG")
#----------------------------------------
# test
# X, Y, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,150,170) # X: 150인 값을 170으로 바꿨을 때
# curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)
#
# X, Y, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,100,200) # X: 150인 값을 170으로 바꿨을 때
# curveList = DC.changeCurve(curveList, changedColorList, lDostX, rDotX)
#
# X, Y, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,40,200) # X: 150인 값을 170으로 바꿨을 때
# curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)
#----------------------------------------
# S자 곡선
X, curveList, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,191,220)
curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)

X, curveList, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,63,50)
curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)



print(curveList)
DC.drawCurve(curveList, X)

Cs = Color_set_creator()
# oriImg = DC.getOriImg() # grayScale
realImg = DC.getRealImg() # Real Original Image
# seperate r, g, b
b, g, r = realImg[:,:,0], realImg[:,:,1], realImg[:,:,2]
ih, iw = DC.getHW()
boardB = Cs.setImg(ih, iw, b)
boardG = Cs.setImg(ih, iw, g)
boardR = Cs.setImg(ih, iw, r)

# setting range
s=0
e=255
# cM = [0] * 256

# get last curveList
cM = curveList
# # print(cM)

# get each Color List and change Color
changedBoardB = Cs.processImg(boardB, s, e, cM)
changedBoardG = Cs.processImg(boardG, s, e, cM)
changedBoardR = Cs.processImg(boardR, s, e, cM)

reImgB = Cs.reloadImg(ih, iw, b, s, e, board=changedBoardB, dims=1)
reImgG = Cs.reloadImg(ih, iw, g, s, e, board=changedBoardG, dims=1)
reImgR = Cs.reloadImg(ih, iw, r, s, e, board=changedBoardR, dims=1)

# set reImg(changed Image)
reImg = np.zeros_like(realImg)
reImg[:,:,0] = reImgB
reImg[:,:,1] = reImgG
reImg[:,:,2] = reImgR

# 변경색상 검증
# DC.findThatColor(63,0) # -> Blue: 63 좌표반환0> [4,1].........
# print("reImg: ", reImg[1][4][0]) # -> 변환된 이미지의 [4,1],Blue 색상-> 50

# show histogram
channels = cv2.split(realImg)
channelsAfter = cv2.split(reImg)

colors = ('b', 'g', 'r')
for (ch, chA, color) in zip (channels,channelsAfter, colors):
    plt.figure(1)
    hist = cv2.calcHist([ch], [0], None, [256], [0,256])
    plt.plot(hist, color=color, label="before")
    # plt.figure(2)
    # hist2 = cv2.calcHist([chA], [0], None, [256], [0,256])
    # plt.plot(hist2, color=color, label="after")

plt.legend()
plt.show()

# Window setting
win_con()
cv2.waitKey(0)
cv2.destroyAllWindows()