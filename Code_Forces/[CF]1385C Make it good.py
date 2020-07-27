from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

input  = stdin.readline

T = int(input())
for case in range(T):
    N = int(input())
    Nums = [*map(int,input().split())]

    flip=False
    Ans=0

    for i in range(N-1,0,-1):
        if not flip and Nums[i]>Nums[i-1]:
            flip=True
        elif flip and Nums[i]<Nums[i-1]:
            flip=False
            Ans=i
            break
    print(Ans)
