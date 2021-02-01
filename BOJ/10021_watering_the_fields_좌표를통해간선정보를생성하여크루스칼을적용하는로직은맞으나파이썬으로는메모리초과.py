from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

def find(node):
    if parent[node]==node:
        return node
    parent[node]=find(parent[node])
    return parent[node]

def union(na,nb):

    ha,hb = find(na),find(nb)
    if rank[ha]>rank[hb]:
        parent[hb]=ha
    else:
        parent[ha]=hb
        if rank[ha]==rank[hb]:
            rank[hb]+=1

from sys import *
input = stdin.readline

N,C = map(int,input().split())
field = [[*map(int,input().split())] for _ in range(N)]
adj = []
for i in range(N-1):
    for j in range(i+1,N):
        dx = field[i][0]-field[j][0]
        dy = field[i][1]-field[j][1]
        d=dx**2+dy**2 
        if d>= C:
            adj.append([d,i,j])
adj.sort(key=lambda x:x[0])
parent = [i for i in range(N)]
rank = [0 for i in range(N)]
Ans=0
for dist,sn,en in adj:
    if find(sn)!=find(en):
        Ans+=dist
        union(sn,en)
print(Ans)




'''
T = int(input())
for case in range(T):
    N = int(input())
    Ans = float(0)
    for n in range(N):
        p,x = map(float,input().split())
        Ans+=float(p*x)
        
    print(f'#{case+1} {Ans:0.6f}')  
'''
