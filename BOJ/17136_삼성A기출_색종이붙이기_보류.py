from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def bfs(x,y):
    global Visited

    Visited[x][y]=True
    que = deque([[x,y]])
    group=[[x,y]]
    while que:
        cx,cy=que.popleft()

        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx,ny=cx+d[0],cy+d[1]
            if (0<=nx<10) and (0<=ny<10) and not Visited[nx][ny] and Board[nx][ny]:
                Visited[nx][ny]=True
                que.append([nx,ny])
                group.append([nx,ny])
    return group


def Fill(parts):
    global Imp,Ans,Board
    for size in range(5,0,-1):
        for cord in parts:
            x,y=cord
            if not Board[x][y]:
                continue

            Flag=True
            for row in range(size):
                if not Flag:
                    break
                for col in range(size):
                    if not((0<=x+row<10) and (0<=y+col<10)) or not Board[x+row][y+col]:
                        Flag=False
                        break
            if Flag:
                if Quan[size]== 0 :
                    Imp=True
                    Ans=-1
                    return
                else:
                    Quan[size]-=1
                    Ans+=1
                    print(f'x={x},y={y},size={size}')
                    print('---------------------------------------')
                    print('before')
                    for l in Board:
                        print(l)
                    print('---------------------------------------')
                    for row in range(size):
                        for col in range(size):
                            Board[x+row][y+col]=0
                    print('after')
                    for l in Board:
                        print(l)
                    print('---------------------------------------')
#--------------------------------------------------------------

input = stdin.readline
Board = [list(map(int,input().split())) for _ in range(10)]
Group=[]
Ans =0
Imp=False
Quan={1:5,2:5,3:5,4:5,5:5}
Visited=[[False]*10 for _ in range(10)]
for i in range(10):
    for j in range(10):
        if not Visited[i][j] and Board[i][j]:
            Group.append(bfs(i,j))


for g in Group:
    if Imp:
        break
    Fill(g)

print(Ans)
