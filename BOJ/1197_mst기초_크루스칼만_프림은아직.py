from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *
    

input = stdin.readline

V,E = map(int,input().split())
graph = [[*map(int,input().split())] for _ in range(E)]

# Kruskal---------------------------------------

parent = [i for i in range(V+1)]
rank=[0]*(V+1)

def find(node):
    if parent[node]==node:
        return node
    parent[node]=find(parent[node])
    return parent[node]

def union(a_node,b_node):
    a_head,b_head = find(a_node),find(b_node)

    if rank[a_node]>rank[b_node]:
        parent[b_node]=a_node
    else:
        parent[a_node]=b_node
        if rank[a_node]==rank[b_node]:
            rank[b_node]+=1

graph.sort(key = lambda x:x[-1])
Ans=0
for info in graph:
    a,b,w = info
    if find(a)!=find(b):
        union(a,b)
        Ans+=w
print(Ans)
# Prim-------------------------------------------
