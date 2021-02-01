from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *
    

def find(node):
    if parent[node]==node:
        return node
    parent[node]=find(parent[node])
    return parent[node]

def union(a_n,b_n):
    global Ans
    h_a,h_b = find(a_n),find(b_n)
    if rank[h_a]>rank[h_b]:
        parent[h_b]=h_a
    else:
        parent[h_a]=h_b
        if rank[h_a]==rank[h_b]:
            rank[h_b]+=1

input = stdin.readline
N = int(input())
Cords = [[*map(int,input().split())]+[i] for i in range(N)]
adj_list=[]
for xyz in range(3):
    Cords.sort(key=lambda x:x[xyz])
    for point in range(N-1):
        s_idx=Cords[point][-1]
        e_idx=Cords[point+1][-1]
        d = abs(Cords[point][xyz]-Cords[point+1][xyz])
        adj_list.append((s_idx,e_idx,d))
        
adj_list.sort(key=lambda x:x[-1])
Ans=0
parent=[i for i in range(N)]
rank=[0]*(N)
cnt=N-1
for i in range(len(adj_list)):
    if not cnt:
        break
    a,b,dist = adj_list[i]
    if find(a)!=find(b):
        Ans+=dist
        cnt-=1
        union(a,b)
print(Ans)

    
