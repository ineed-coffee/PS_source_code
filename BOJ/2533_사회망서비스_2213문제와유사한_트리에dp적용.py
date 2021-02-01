from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

def make_tree(node):
    p = parent[node]
    for ch in adj_list[node]:
        if ch!=p:
            parent[ch]=node
            make_tree(ch)
            dp_late[node]+=dp_early[ch]
            dp_early[node]+=min(dp_early[ch],dp_late[ch])

input = stdin.readline
N = int(input())
adj_list = [[] for _ in range(N+1)]
for line in range(N-1):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    
parent=[0]*(N+1)
dp_early = [1]*(N+1)
dp_late = [0]*(N+1)
root=1
make_tree(root)
print(min(dp_early[1],dp_late[1]))
