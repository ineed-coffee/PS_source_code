from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
from heapq import *

#---------------------------------------------
input = stdin.readline
V,E = map(int,input().split())
K=int(input())-1
Adj_list = [{} for _ in range(V)]
for _ in range(E):
    s,e,w=map(int,input().split())
    try:
        Adj_list[s-1][e-1]=min(Adj_list[s-1][e-1],w)
    except KeyError:
        Adj_list[s-1][e-1]=w
#---------------------------------------------
Dist = [maxsize]*V
Dist[K]=0
que=[]
heappush(que,[0,K])

while que:
    c_dist,c_node = heappop(que)
    if Dist[c_node]<c_dist:
        continue

    for n_node,n_dist in Adj_list[c_node].items():
        if c_dist + n_dist < Dist[n_node]:
            Dist[n_node]= c_dist + n_dist
            heappush(que,[c_dist+n_dist,n_node])

#---------------------------------------------
for v in range(V):
    if Dist[v]!=maxsize:
        print(Dist[v])
    else:
        print('INF')
#---------------------------------------------
