from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)
 
input = stdin.readline
N,K = map(int,input().split())
info =[[0,0]]+[[*map(int,input().split())] for _ in range(N)]
info.sort(key=lambda x:x[0])

dp=[[0]*(K+1) for _ in range(N+1)]

for i in range(1,N+1):
    for k in range(1,K+1):
        if info[i][0]<=k:
            flag=True
            left=k-info[i][0]
            dp[i][k]=max(dp[i-1][k],info[i][1]+dp[i-1][left])
        else:
            dp[i][k]=dp[i-1][k]

print(dp[i][-1])
