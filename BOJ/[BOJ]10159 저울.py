from sys import *

input = stdin.readline

MS = maxsize
N = int(input())
M = int(input())

adj = [[MS for i in range(N+1)]for j in range(N+1)]
for m in range(M):
    a,b = map(int,input().split())
    adj[a][b]=1
    adj[b][a]=-1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if adj[i][j]!=MS:
                continue
            if adj[i][k]==1 and adj[k][j]==1:
                adj[i][j]=1
            elif adj[i][k]==-1 and adj[k][j]==-1:
                adj[i][j]=-1

for i in range(1,N+1):
    cnt=0
    for j in range(1,N+1):
        if i==j:continue
        if adj[i][j] not in [1,-1]:
            cnt+=1
    print(cnt)
