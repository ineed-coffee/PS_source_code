from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

def make_tree(node):
    global size
    p=parent[node]
    for ch in adj_list[node]:
        if ch!=p:
            parent[ch]=node
            make_tree(ch)
            size[node]+=size[ch]
            
input = stdin.readline
N,R,Q = map(int,input().split())
adj_list = [[] for _ in range(N)]
parent=[-1]*N
size=[1]*N
for n in range(N-1):
    a,b = map(lambda x:int(x)-1,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

make_tree(R-1)
for q in range(Q):
    query = int(input())-1
    print(size[query])
    
