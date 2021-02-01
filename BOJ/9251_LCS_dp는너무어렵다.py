from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)
 
input = stdin.readline
A = list(input().strip())
B = list(input().strip())

a=len(A)
b=len(B)
dp=[[0]*(b+1) for _ in range(a+1)]

for i in range(1,a+1):
    for j in range(1,b+1):
        if A[i-1]!=B[j-1]:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
        elif A[i-1]==B[j-1]:
            dp[i][j]=dp[i-1][j-1]+1

print(dp[-1][-1])
                




'''
if len(A)<len(B):
    dp=[0]*len(B)
    for i in range(len(A)):
        tmp=[]
        for j in range(len(B)):
            if A[i]==B[j]:
                val=0
                for k in range(j):
                    if dp[k]>val:
                        val=dp[k]
                if val>=dp[j]:
                    tmp.append([j,val])

        if tmp:
            for t in tmp:
                idx,val=t
                dp[idx]=val+1

    print(max(dp))

else:
    dp=[0]*len(A)
    for i in range(len(B)):
        tmp=[]
        for j in range(len(A)):
            if B[i]==A[j]:
                val=0
                for k in range(j):
                    if dp[k]>val:
                        val=dp[k]
                if val>=dp[j]:
                    tmp.append([j,val])

        if tmp:
            for t in tmp:
                idx,val=t
                dp[idx]=val+1

    print(max(dp))


else:
            if A[i]!=B[j]:
                dp[i][j]=dp[i-1][j]
            elif A[i]==B[j]:
                for k in range(j):
                    if dp[i-1][k]>dp[i][j]:
                        dp[i][j]= dp[i-1][k]
                dp[i][j]+=1
'''                    
