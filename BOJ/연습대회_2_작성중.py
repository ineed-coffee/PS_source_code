from sys import *
from collections import deque
#from itertools import *
from copy import *
#setrecursionlimit(300000)
#from heapq import *

def get_spot(info_list):

    x,y = info_list[0]
    idx = info_list[1]

    for i in range(8):
        d = D[idx]
        if not((0<=x+d[0]<4)and(0<=y+d[1]<4)):
            continue
        if c_br[x+d[0]][y+d[1]]!=-1:
            return [[x+d[0],y+d[1]],idx]
        idx=(idx+1)%8

    return []

input = stdin.readline
D = [[-1,1],[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1]]
Board = [[0]*4 for _ in range(4)]
Fish_info=[0]*16
Shark_info=[[0,0],-1]
for i in range(4):
    line = [*map(int,input().split())]
    for j in range(0,8,2):
        num=line[j]-1
        Board[i][j//2]=num
        Fish_info[num]=[[i,j//2],(line[j+1])%8]

Ans=Board[0][0]
Shark_info[1]=Fish_info[Ans][1]
Fish_info[Ans]=[]
Board[0][0]=-1

que = deque([[Board,Shark_info,Fish_info,Ans]])

while que:

    c_br , c_sh , c_fi , c_cnt = que.popleft()

    for i in range(16):
        if not c_fi[i]:
            continue
        cord = get_spot(c_fi[i])
        if cord :
            x1,y1 = c_fi[i][0]
            x2,y2 = cord[0]
            if c_br[x2][y2]==0:
                c_br[x1][y1],c_br[x2][y2] = c_br[x1][y1],c_br[x2][y2]
                c_fi[i]=[[x2,y2],cord[1]]  
            else:
                c_br[x1][y1],c_br[x2][y2] = c_br[x1][y1],c_br[x2][y2]
                c_fi[i]=[[x2,y2],cord[1]]
                c_fi[c_br[x2][y2]][0]=[x1,y1]

    sx,sy = c_sh[0]
    sd = D[c_sh[1]]
    nx,ny = sx,sy
    flag = False
    while True:

        nx+=sd[0]
        ny+=sd[1]
        
        if not (0<=nx<4 and 0<=ny<4):
            break

        if c_br[nx][ny]>0:
            if not flag:
                flag=True
            print(1)
            a,b,c,d = c_br[sx][sy],c_br[nx][ny],c_fi[c_br[nx][ny]][1],c_sh[1]
            c_br[sx][sy],c_br[nx][ny]=0,-1
            c_sh=[[nx,ny],c]
            c_fi[b]=[]
            que.append([deepcopy(c_br),deepcopy(c_sh),deepcopy(c_fi),c_cnt+b])
            c_fi[b]=[[nx,ny],c]
            c_sh=[[sx,sy],d]
            c_br[sx][sy],c_br[nx][ny]=-1,b

    if not flag:
        Ans = max(Ans,c_cnt)

print(Ans)
