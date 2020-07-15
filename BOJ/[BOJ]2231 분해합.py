from sys import *

input = stdin.readline

N = int(input())

Ans=0
if len(str(N))>2:
    start = N -1 -(9*len(str(N)))
    for i in range(start,N+1):
        tmp = [*map(int,list(str(i)))]
        S = sum(tmp)
        if S+i == N:
            Ans = i
            break
else:
    for i in range(1,N+1):
        tmp = [*map(int,list(str(i)))]
        S = sum(tmp)
        if S+i == N:
            Ans = i
            break

print(Ans)

