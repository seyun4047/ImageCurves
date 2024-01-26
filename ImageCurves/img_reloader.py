import numpy as np

from color_detection import Detect_color
from color_set_creator import Color_set_creator
import cv2
import matplotlib.pylab as plt


X = [0, 63, 127, 191, 255]
src = "src/img/test.JPG"
DC = Detect_color(src)
curveList = [i for i in range(0, 256, 1)]  # CurveList x좌표: idx | y좌표: idx에 해당하는 값


def img_reload(src, X, rootX, changedValue, curveList):
    # S자 곡선
    X, curveList, lDotX, rDotX, changedColorList = DC.transCurve(X,curveList,rootX,changedValue)
    curveList = DC.changeCurve(curveList, changedColorList, lDotX, rDotX)

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

    return reImg, X, curveList, realImg

reImg, X, curveList, realImg = img_reload(src, X, 191, 220, curveList)
# reImg, X, curveList = img_reload(src, X, 63, 50, curveList)

# cv2.resizeWindow('after', 500, 500)
cv2.imshow('after', reImg)



# show histogram
channels = cv2.split(realImg)
channelsAfter = cv2.split(reImg)

colors = ('b', 'g', 'r')
for (ch, chA, color) in zip (channels,channelsAfter, colors):
    plt.figure(1)
    hist = cv2.calcHist([ch], [0], None, [256], [0,256])
    plt.plot(hist, color=color, label="before")
    plt.figure(2)
    hist2 = cv2.calcHist([chA], [0], None, [256], [0,256])
    plt.plot(hist2, color=color, label="after")

plt.legend()
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()