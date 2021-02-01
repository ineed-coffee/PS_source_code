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
            dp_selected[node]+=dp_n_selected[ch]
            dp_n_selected[node]+=max(dp_selected[ch],dp_n_selected[ch])

input = stdin.readline
N = int(input())
dp_selected = [0]+[*map(int,input().split())]
adj_list = [[] for _ in range(N+1)]
for line in range(N-1):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    
parent=[0]*(N+1)
dp_n_selected=[0]*(N+1)
root=1
make_tree(root)
print(max(dp_selected[root],dp_n_selected[root]))
