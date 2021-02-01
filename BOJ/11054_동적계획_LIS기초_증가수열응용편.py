from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)
 
input = stdin.readline
N = int(input())
Arr = [0]+[*map(int,input().split())]
if N<2:
    print(1)
else:
    
    inc_dp=[0]+[1]*N
    for i in range(2,N+1):
        for j in range(1,i):
            if Arr[j]<Arr[i]:
                inc_dp[i]=max(inc_dp[i],inc_dp[j]+1)

    dec_dp=[0]+[1]*N
    for i in range(N-1,0,-1):
        for j in range(N,i,-1):
            if Arr[j]<Arr[i]:
                dec_dp[i]=max(dec_dp[i],dec_dp[j]+1)
    half=1
    for i in range(1,N+1):
        half=max(half,dec_dp[i]+inc_dp[i]-1)

    print(half)
