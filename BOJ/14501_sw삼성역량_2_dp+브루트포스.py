from sys import *
#from collections import deque
#from itertools import combinations
#setrecursionlimit(10000)

input = stdin.readline

N = int(input())
schedule = [[0,0]]+[list(map(int,input().split())) for _ in range(N)]+[[0,0]]

dp = [[0,0] for _ in range(N+2)]

for i in range(1,N+2):
    if i ==1:
        dp[i][0]=schedule[i][0]
        dp[i][1] = 0

    else:
        comp = 0
        dp[i][0]=schedule[i][0]
        for j in range(1,i):
            if j+dp[j][0] <= i:
                comp = max(comp,dp[j][1]+schedule[j][1])
        dp[i][1] = comp

print(dp[-1][1])
