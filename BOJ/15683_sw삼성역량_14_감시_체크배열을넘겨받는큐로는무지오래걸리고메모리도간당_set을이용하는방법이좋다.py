from sys import *
from collections import deque
#from itertools import *
from copy import *
#setrecursionlimit(10000)


def spread(xy,cam,watch,covered):

    copy_watch = deepcopy(watch)
    cam_types = cam_rotate[cam]
    for spread in cam_types:
        dx,dy = spread
        x,y = cam_info[xy][1],cam_info[xy][2]
        while True :
            nx,ny = x+dx,y+dy
            if nx<0 or nx>=N or ny<0 or ny>=M:
                break

            elif Office[nx][ny]==6:
                break

            x+=dx
            y+=dy
            
            if not Office[x][y] and not copy_watch[x][y] :
                covered+=1
                copy_watch[x][y]=True
                
    return [copy_watch,covered]


def Set_cam(start):
    global Ans

    if not cam_info:
        return
    
    on_watch = [[False]*M for _ in range(N)]

    que = deque([[start,on_watch,0]])

    while que:

        idx,cur_watch,cur_covered = que.pop()
        [cur_type,cur_x,cur_y] = cam_info[idx]
        
        for i in range(cam_case[cur_type]):

            next_watch,next_covered = spread(idx,(cur_type,i),cur_watch,cur_covered)

            if idx+1 == len(cam_info):
                Ans = min(Ans,Unsupervised-next_covered)

            else:
                que.append([idx+1,next_watch,next_covered])


    return

input = stdin.readline

N,M = map(int,input().split())

Unsupervised = 0
Office =[]

cam_case = [0,4,2,4,4,1]
cam_rotate = {(1,0):[[0,1]] , (1,1):[[1,0]] , (1,2):[[0,-1]] , (1,3):[[-1,0]],
              (2,0):[[0,1],[0,-1]] , (2,1):[[1,0],[-1,0]],
              (3,0):[[0,1],[1,0]] , (3,1):[[1,0],[0,-1]],
              (3,2):[[0,-1],[-1,0]] , (3,3):[[-1,0],[0,1]],
              (4,0):[[0,1],[1,0],[0,-1]] , (4,1):[[1,0],[0,-1],[-1,0]],
              (4,2):[[0,-1],[-1,0],[0,1]] , (4,3):[[-1,0],[0,1],[1,0]],
              (5,0):[[0,1],[1,0],[0,-1],[-1,0]]}

cam_info = []
for i in range(N):

    line = list(map(int,input().split()))
    for j in range(M):
        if not line[j]:
            Unsupervised+=1
        elif line[j]<6:
            cam_info.append([line[j],i,j])

    Office.append(line)

Ans = Unsupervised
Set_cam(0)

print(Ans)
