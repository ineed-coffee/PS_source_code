from sys import *
from collections import deque
#setrecursionlimit(100000)

def bfs_s(x,y):
    global Visited

    Visited[x][y] = True
    que = deque()
    que.append([x,y])
    chunk=[[x,y]]
    while que :
        r,c = que.popleft()
        for i in range(4):
            nr = r+ dx[i]
            nc = c+ dy[i]
            if (0<=nr<N)and(0<=nc<N)and Island[nr][nc] and not Visited[nr][nc]:
                Visited[nr][nc]=True
                que.append([nr,nc])
                chunk.append([nr,nc])
    return chunk




N = int(input())

Island = [list(map(int,stdin.readline().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
Joint_land=[]
bridge=[]
Visited=[[False]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        if Island[i][j] and not Visited[i][j]:
            temp = bfs_s(i,j)
            Joint_land.append(temp)

for k in range(len(Joint_land)):
    for l in range(k+1,len(Joint_land)):
        for m in Joint_land[k]:
            for n in Joint_land[l]:
                bridge.append(abs(m[0]-n[0])+abs(m[1]-n[1])-1)

print(min(bridge))
