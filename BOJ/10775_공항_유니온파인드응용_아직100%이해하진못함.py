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
        head[head_a]=head_b
    return

input = stdin.readline
G = int(input())
P = int(input())
plane_info = [int(input()) for p in range(P)]
head = [i for i in range(G+1)]
Ans=0
for i in range(P):
    head_i = find_head(plane_info[i])
    if head_i==0:
        break
    union(head_i,head_i-1)
    Ans+=1
print(Ans)
