from sys import *
from collections import deque
from heapq import heappop,heappush,heapify
input = stdin.readline

T = int(input())

for case in range(T):
    N = int(input())
    Arr = [*map(int,input().split())]

    A_set = set(Arr)
    A_exc = set(range(N+1))-A_set
    A=list(A_exc)
    heapify(A)

    idx=0
    comp=heappop(A)
    cnt=0
    pos=[]
    while idx<N:
        print(Arr)
        if idx==N-1 or comp<Arr[idx+1]:
            tmp,Arr[idx]=Arr[idx],comp
            cnt+=1
            pos.append(idx)
            heappush(A,tmp)
            comp=heappop(A)
            if idx==N-1:
                break
            else:
                idx=0
        else:
            idx+=1

    print(cnt)
    print(*pos)
