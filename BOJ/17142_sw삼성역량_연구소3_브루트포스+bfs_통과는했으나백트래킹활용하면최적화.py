from sys import *
from collections import deque
from itertools import *
#from copy import *
#setrecursionlimit(10000)

def bfs(list_of_v):
    global Got_virus,Done
    if not empty:
        return [True,0]
    que = deque([])
    cap=0
    
    for v in list_of_v:
        que.append([v,0])
      
    while que:
        [cx,cy],stamp = que.popleft()
        
        for i in range(4):
            nx,ny = cx+dx[i],cy+dy[i]
            if (0<=nx<N) and (0<=ny<N) and not Got_virus[nx][ny] and Lab[nx][ny]!=1:
                if Lab[nx][ny]==0:
                    Got_virus[nx][ny]=True
                    que.append([[nx,ny],stamp+1])
                    cap +=1
                    if cap == empty:
                        return [True,stamp+1]
                    
                elif Lab[nx][ny]==2:
                    Got_virus[nx][ny]=True
                    que.append([[nx,ny],stamp+1])

    return [False,stamp]
    
input = stdin.readline

N,M = map(int,input().split())
empty = 0
Lab = []
V_cords=[]
dx,dy = [0,1,0,-1],[1,0,-1,0]
Time = maxsize
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(N):
        if line[j]==2:
            V_cords.append([i,j])
        elif not line[j]:
            empty+=1
    Lab.append(line)

Combs = combinations(V_cords,M)
for c in Combs:
    Got_virus = [[False]*N for _ in range(N)]

    for xy in c:
        Got_virus[xy[0]][xy[1]]=True

    flag,time = bfs(c)

    if flag:
        Time = min(Time,time)

print(Time if Time!=maxsize else -1)

