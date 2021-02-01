from sys import *
setrecursionlimit(10000)

def dfs_s(x):

    Visited[x]=True
    
    for k in Adj[x]:
        if not Visited[k] :
            dfs_s(k)
    return


def Solve(N):
    cnt=0
    for v in range(1,N+1):
       if not Visited[v]:
           cnt+=1
           dfs_s(v)
           #bfs_s(v)
           
    print(cnt)
    return


N,M= map(int,input().split())

Adj = [[] for _ in range(N+1)]
Visited = [False for _ in range(N+1)]

for line in range(M):
    a,b=map(int,stdin.readline().split())
    Adj[a].append(b)
    Adj[b].append(a)

Solve(N)
