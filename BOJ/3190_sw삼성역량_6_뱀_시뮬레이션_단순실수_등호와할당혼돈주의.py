from sys import *
from collections import deque
#from itertools import combinations
#setrecursionlimit(10000)


input = stdin.readline

N = int(input())
K = int(input())

Board = [[0]*N for _ in range(N)]
for apple in range(K):
    i,j = map(int,input().split())
    Board[i-1][j-1]=1

L = int(input())
Move_dir = []
time_stamp=[]
dir_stamp = []
for _ in range(L):
    x,c = input().strip().split()
    Move_dir.append([int(x),c])
    time_stamp.append(int(x))
    dir_stamp.append(c)

Flag,idx,stamp = True,0,0
snake = deque([[0,0]])
dx = [0,1,0,-1]
dy = [1,0,-1,0]
Available = [[True]*N for _ in range(N)]
Available[0][0]=False
Ans = 0

while True:
    Ans+=1
    hx = snake[-1][0]+dx[idx]
    hy = snake[-1][1]+dy[idx]
    if (0<=hx<N) and (0<=hy<N) and Available[hx][hy]:
            Available[hx][hy]=False
            snake.append([hx,hy])
            if Board[hx][hy]:
                Board[hx][hy]=0
            else:
                tx,ty = snake.popleft()
                Available[tx][ty]=True
    else:
        print(Ans)
        break
    if stamp<L and Ans == time_stamp[stamp]:
        if dir_stamp[stamp] == 'L':
            idx = (idx-1)%4
        elif dir_stamp[stamp] == 'D':
            idx = (idx+1)%4
        stamp+=1


