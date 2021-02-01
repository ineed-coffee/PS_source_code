from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def bfs(x,y,num):
    global Visited,removed_any,seperate_nums

    Visited[x][y]=True
    que = deque([[x,y]])
    group =[[x,y]]

    while que:

        cx,cy = que.popleft()

        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]

            if not (0<=nx<N):
                continue
            if not (0<=ny<M):
                if ny<0:
                    ny+=M
                else:
                    ny-=M
            if not Visited[nx][ny] and Board[nx][ny]==num:
                Visited[nx][ny]=True
                group.append([nx,ny])
                que.append([nx,ny])

    if len(group)==1:
        seperate_nums.append(num)
        return

    if not removed_any:
        removed_any=True
        
    for xy in group:
        tx,ty = xy[0],xy[1]
        Board[tx][ty]=0
    return

        
input = stdin.readline

N,M,T = map(int,input().split())
Board = [deque(map(int,input().split())) for _ in range(N)]
Commands = [list(map(int,input().split())) for _ in range(T)]
dx,dy = [0,1,0,-1],[1,0,-1,0]
no_num=False
for com in Commands:

    std,direction,cnt = com
#--------------------------------------------------------------
    for i in range(N):
        if not (i+1)%std:
            if direction:
                for c in range(cnt):
                    Board[i].append(Board[i].popleft())         # spin
            else:
                for c in range(cnt):
                    Board[i].appendleft(Board[i].pop())

#--------------------------------------------------------------
    removed_any = False
    seperate_nums = []
    Visited = [[False]*M for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if Board[i][j] and not Visited[i][j]:              # remove adj nums
                n = Board[i][j]
                bfs(i,j,n)
    
#--------------------------------------------------------------

    if removed_any:
        continue
    
    if not seperate_nums:
        no_num =True
        break
        
    Ave = sum(seperate_nums)/len(seperate_nums)
    for i in range(N):
        for j in range(M):
            if Board[i][j]:                                    # +1,-1 if not removed any
                if Board[i][j]>Ave:  
                    Board[i][j]-=1
                elif Board[i][j]<Ave:
                    Board[i][j]+=1

#--------------------------------------------------------------

Ans =0
if not no_num:
    for i in range(N):
        Ans+=sum(Board[i])
print(Ans)
