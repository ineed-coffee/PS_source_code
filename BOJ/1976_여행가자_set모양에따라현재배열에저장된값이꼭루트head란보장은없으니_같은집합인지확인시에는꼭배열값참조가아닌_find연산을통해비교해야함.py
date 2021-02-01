from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

from sys import *
setrecursionlimit(10000)

def find_head(node):
    if head[node]==node:
        return node
    head[node]=find_head(head[node])
    return head[node]

def union(a_node,b_node):
    head_a = find_head(a_node)
    head_b = find_head(b_node)
    if head_a!=head_b:
        head[head_b]=head_a
    return

input = stdin.readline
N = int(input())
M = int(input())
head = [h for h in range(N)]
for i in range(N):
    info = [*map(int,input().split())]
    for j in range(N):
        if info[j]:
            union(i,j)
Route = [*map(lambda x:int(x)-1,input().split())]
possible=True
standard = find_head(Route[0])
for m in range(M):
    if find_head(Route[m])!=standard:
        possible=False
        break
if possible:
    print('YES')
else:
    print('NO')
