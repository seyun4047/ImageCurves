import cv2
import numpy as np
import sys
from collections import deque
import sys
from collections import deque

# image setting with cv2
oriImg = cv2.imread("src/img/test.JPG")
oriImg = cv2.cvtColor(oriImg, cv2.COLOR_BGR2GRAY)
ih, iw = oriImg.shape[:2]
cv2.imshow("img", oriImg)
cv2.waitKey(0)
cv2.destroyAllWindows()
print(iw,ih)
# find that color(brightness) Algorithm
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


# print(findThatColor(157, ih, iw))
print(oriImg[1140][1279])