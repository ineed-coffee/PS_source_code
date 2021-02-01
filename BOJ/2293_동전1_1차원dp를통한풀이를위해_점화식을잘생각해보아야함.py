from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *



input = stdin.readline
N,K = map(int,input().split())
Coins=[]
for _ in range(N):
    num = int(input())
    if num<=K:
        Coins.append(num)
dp=[1]+[0]*K

for c in Coins:
    for value in range(c,K+1):
        dp[value]+=dp[value-c]

print(dp[-1])
