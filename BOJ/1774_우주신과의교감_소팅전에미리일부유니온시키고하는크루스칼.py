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

def union(a_n,b_n,dist=-1):
    global Ans
    h_a,h_b = find(a_n),find(b_n)
    if rank[h_a]>rank[h_b]:
        parent[h_b]=h_a
    else:
        parent[h_a]=h_b
        if rank[h_a]==rank[h_b]:
            rank[h_b]+=1
    if dist!=-1:
        Ans+=dist
    

input = stdin.readline
N,M = map(int,input().split())

Cords = [0]+[[*map(int,input().split())] for _ in range(N)]
parent=[i for i in range(N+1)]
rank=[0]*(N+1)
for m in range(M):
    a,b = map(int,input().split())
    if find(a)!=find(b):
        union(a,b)

Ans=float(0)
adj_list=[]
for i in range(1,N+1):
    for j in range(i+1,N+1):
        if find(i)!=find(j):
            del_x,del_y = Cords[i][0]-Cords[j][0],Cords[i][1]-Cords[j][1]
            d = float((del_x**2+del_y**2)**0.5)
            adj_list.append((d,i,j))

adj_list.sort(key=lambda x:x[0])

for i in range(len(adj_list)):
    dist,a,b = adj_list[i]
    if find(a)!=find(b):
        union(a,b,dist)
print(f'{Ans:0.2f}')

    
