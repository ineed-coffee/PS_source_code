from sys import *


def backtrack(pos,cnt,cost):
    global Ans

    if cnt==N:
        Ans = min(Ans,cost)
        return

    for nxt in range(N):
        if not Visited[nxt]:
            Visited[nxt]=True
            backtrack(nxt,cnt+1,cost+adj[pos][nxt])
            Visited[nxt]=False

input = stdin.readline

N,K = map(int,input().split())

adj = [[*map(int,input().split())] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            adj[i][j] = min(adj[i][j],adj[i][k]+adj[k][j])

Visited = [False]*N

Ans = maxsize
Visited[K]=True
backtrack(K,1,0)

print(Ans)
