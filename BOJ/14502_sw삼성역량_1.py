from sys import *
from collections import deque
from itertools import combinations
#setrecursionlimit(10000)

def spread():

    for i in range(N):
        for j in range(M):
            if Adj[i][j]==2 and not Visited[i][j]:
                bfs_s(i,j)


def bfs_s(x,y):
    global Visited,cnt

    Visited[x][y] = True
    que = deque([[x,y]])

    while que:
        [cx,cy] = que.pop()
        
        for k in range(4):
            nx = cx + dx[k]
            ny = cy + dy[k]

            if (0<=nx<N) and (0<=ny<M) and Adj[nx][ny]==0 and not Visited[nx][ny]:
                Visited[nx][ny] = True
                cnt+=1
                que.append([nx,ny])

dx = [-1,0,1,0]
dy = [0,-1,0,1]
input = stdin.readline
N,M = map(int,input().split())

Adj = [[]*M for _ in range(N)]
extra_wall = []
for i in range(N):
    line = list(map(int,input().split()))
    for j in range(M):
        if not line[j]:
            extra_wall.append([i,j])
    Adj[i] = line

empty = len(extra_wall)
cand = combinations(extra_wall,3)
Ans = 0
for comb in cand:
    cnt = 0
    Visited = [[False]*M for _ in range(N)]
    for k in range(3):
        Visited[comb[k][0]][comb[k][1]]=True
        
    spread()
    Ans = max(Ans,empty-3-cnt)

print(Ans)


# combiantions 메서드를 직접 구현하려면 for문 2번으로 재귀문을 작성하여 벽을
# 하나씩 선택하는 방법으로 구현 가능함

