from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)

def split_count(div):
    return_val=0
    for wire in Wires:
        return_val+=wire//div

    if return_val>=N:
        return True

    return False

input = stdin.readline
K,N=map(int,input().split())
Wires=[int(input()) for _ in range(K)]
low=1
high=max(Wires)
while low<high:
    mid=(low+high)//2
    if split_count(mid):
        low=mid+1
    else:
        high=mid-1

mid=low
if split_count(mid):
    print(mid)
else:
    print(mid-1)



