from sys import *
#from collections import deque
#setrecursionlimit(10000)

M = maxsize

n,k = map(int,stdin.readline().split())

Adj = [[M]*(n+1) for _ in range(n+1)]

for i in range(k):
    a,b = map(int,stdin.readline().split())
    Adj[a][b] = 1

for j in range(n+1):
    Adj[j][j] = 0

for i in range(1,n+1):
    for j in range(1,n+1):
        for k in range(1,n+1):
            Adj[j][k] = min(Adj[j][k],Adj[j][i]+Adj[i][k])

s = int(input())
Ans=[]

for j in range(s):
    c,d = map(int,stdin.readline().split())

    if Adj[c][d]!= M:
        print(-1)
    else:
        if Adj[d][c]!=M:
            print(1)
        else:
            print(0)
    
