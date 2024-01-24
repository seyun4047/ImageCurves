import numpy as np
import cv2

# 1. 이미지를 array로 받아들임
# 2. List[0-255] = [xn,yn]
# 3. 색상변환: k->i
# 4. tmp = list[k].좌표모두빼기(); list[i] = tmp;
# 5. array재구성: List[0-255: t] -> xn,yn = t
# 6. opencv로 반환

# 1. 이미지를 array로 받아들임: oriImg
# 2. List[0-255] = [xn,yn]
class Color_set_creator:
    def setImg(self, ih, iw, oriImg):
        board = [[] for _ in range(256)]

        for x in range(iw):
            for y in range(ih):
                pixColor = oriImg[y][x]
                board[pixColor].append([x,y])

        return board

    # 3. 색상변환: x->t
    # corlorMapped: 컬러
    # s: 변환 시작 포인트
    # e: 변환 종료 포인트
    # colorMapped[x] = y
    # board[color] = [[x1,y1], ... [xn, yn]]
    def processImg(self, board, s, e, colorMapped):
        for x in range(s, e+1, 1):
            t = colorMapped[x]
            tLst = board[x]
            board[x] = []
            board[t] += (tLst)
        return board

    # oriImg: 초기 이미지
    # s: 변환 시작 포인트
    # e: 변환 종료 포인트
    # board 변환된 이미지
    # dims: 컬러 채널수(지금은 흑백으로 진행하기때문에 1, rgb->3)
    def reloadImg(self, ih, iw, oriImg, s, e, board, dims):
        # reImg = np.zeros((ih, iw, dims), dtype=np.uint8)
        reImg = oriImg
        for clrNum in range(s, e+1, 1):
            tLst = board[clrNum]
            for x, y in tLst:
                reImg[y][x] = clrNum
        # 재구성된 이미지 반환
        return reImg

#---------------------------------------------------
# test

# Cs = Color_set_creator()
# oriImg = cv2.imread("src/img/test2.png")
# oriImg = cv2.cvtColor(oriImg, cv2.COLOR_BGR2GRAY)
# ih, iw = oriImg.shape[:2]
# board = Cs.setImg(ih, iw, oriImg)
# s=0
# e=100
# cM = [0] * 256
# # print(cM)
# changedBoard = Cs.processImg(board, s, e, cM)
# print(changedBoard[0])
# reImg = Cs.reloadImg(ih, iw, oriImg, s, e, board=changedBoard, dims=1)
# cv2.imshow('tmp',reImg)
# cv2.waitKey(0)
# cv2.destroyAllWindows()