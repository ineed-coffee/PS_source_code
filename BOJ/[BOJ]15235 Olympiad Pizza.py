from sys import stdin
from collections import deque

input = stdin.readline

N = int(input())
Needs = [*map(int,input().split())]

N_que = deque(zip(Needs,[i for i in range(N)]))
Fed = [0]*(N)
time=0
while N_que:
    time+=1
    c_need,c_idx = N_que.popleft()
    if c_need==1:
        Fed[c_idx]=time
    else:
        N_que.append(tuple([c_need-1,c_idx]))
print(*Fed)
