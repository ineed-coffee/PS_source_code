from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)
 
input = stdin.readline
N = int(input())
Arr = [-10000]+[*map(int,input().split())]
a
for i in range(1,N+1):
    Arr[i]=max(Arr[i],Arr[i-1]+Arr[i])
    
print(max(Arr))
