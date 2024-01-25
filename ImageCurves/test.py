from color_detection import Detect_color
from color_set_creator import Color_set_creator
import cv2

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


def win_con():
    cv2.namedWindow('before', cv2.WINDOW_NORMAL)
    cv2.namedWindow('before[grayScale]', cv2.WINDOW_NORMAL)
    cv2.namedWindow('after', cv2.WINDOW_NORMAL)

    cv2.resizeWindow('before', 500, 500)
    cv2.resizeWindow('before[grayScale]', 500, 500)
    cv2.resizeWindow('after', 500, 500)

    cv2.moveWindow('before', 0, 0)
    cv2.moveWindow('before[grayScale]', 500, 0)
    cv2.moveWindow('after', 1000, 0)

    cv2.imshow('before', realImg)
    cv2.imshow('before[grayScale]', oriImg)
    cv2.imshow('after', reImg)


print(curveList)
DC.drawCurve(curveList, X)
#
Cs = Color_set_creator()
oriImg = DC.getOriImg() # grayScale
realImg = DC.getRealImg() # Real Original Image
ih, iw = DC.getHW()
board = Cs.setImg(ih, iw, oriImg)
s=0
e=255
# cM = [0] * 256
cM = curveList
# # print(cM)
changedBoard = Cs.processImg(board, s, e, cM)
reImg = Cs.reloadImg(ih, iw, oriImg, s, e, board=changedBoard, dims=1)

win_con()

cv2.waitKey(0)
cv2.destroyAllWindows()