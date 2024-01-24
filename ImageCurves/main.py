from color_detection import Detect_color
from color_set_creator import Color_set_creator
import cv2

X = [0, 63, 127, 191, 255]
curveList = [i for i in range(0,256,1)] # CurveList x좌표: idx | y좌표: idx에 해당하는 값
DC = Detect_color("src/img/test.JPG")
X, Y, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,150,170) # X: 150인 값을 170으로 바꿨을 때
curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)

X, Y, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,100,200) # X: 150인 값을 170으로 바꿨을 때
curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)

X, Y, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,40,200) # X: 150인 값을 170으로 바꿨을 때
curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)
print(curveList)
# DC.drawCurve(curveList, X)

Cs = Color_set_creator()
oriImg = DC.getOriImg()
ih, iw = DC.getHW()
board = Cs.setImg(ih, iw, oriImg)
s=40
e=200
# cM = [0] * 256
cM = curveList
# # print(cM)
changedBoard = Cs.processImg(board, s, e, cM)
print(changedBoard[0])
reImg = Cs.reloadImg(ih, iw, oriImg, s, e, board=changedBoard, dims=1)
cv2.imshow('tmp',reImg)
cv2.waitKey(0)
cv2.destroyAllWindows()