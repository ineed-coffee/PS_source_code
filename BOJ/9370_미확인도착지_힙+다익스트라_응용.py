from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
from heapq import *

#---------------------------------------------
input = stdin.readline

T = int(input())
for case in range(T):
    n,m,t=map(int,input().split())
    s,g,h=map(lambda x:int(x)-1,input().split())
    Adj_list=[{} for _ in range(n)]
    for _ in range(m):
        a,b,d = map(int,input().split())
        Adj_list[a-1][b-1]=d
        Adj_list[b-1][a-1]=d
        
    destinations = [int(input())-1 for _ in range(t)]

    Dist_s = [maxsize]*n
    Dist_s[s]=0
    que_s=[]
    heappush(que_s,[0,s])
    while que_s:
        c_dist,c_node=heappop(que_s)
        if Dist_s[c_node]<c_dist:
            continue
        for n_node,n_dist in Adj_list[c_node].items():
            if c_dist+n_dist < Dist_s[n_node]:
                Dist_s[n_node]=c_dist+n_dist
                heappush(que_s,[c_dist+n_dist,n_node])

    Dist_g = [maxsize]*n
    Dist_g[g]=0
    que_g=[]
    heappush(que_g,[0,g])
    while que_g:
        c_dist,c_node=heappop(que_g)
        if Dist_g[c_node]<c_dist:
            continue
        for n_node,n_dist in Adj_list[c_node].items():
            if c_dist+n_dist < Dist_g[n_node]:
                Dist_g[n_node]=c_dist+n_dist
                heappush(que_g,[c_dist+n_dist,n_node])

    Dist_h = [maxsize]*n
    Dist_h[h]=0
    que_h=[]
    heappush(que_h,[0,h])
    while que_h:
        c_dist,c_node=heappop(que_h)
        if Dist_h[c_node]<c_dist:
            continue
        for n_node,n_dist in Adj_list[c_node].items():
            if c_dist+n_dist < Dist_h[n_node]:
                Dist_h[n_node]=c_dist+n_dist
                heappush(que_h,[c_dist+n_dist,n_node])
    Ans=[]
    for des in destinations:
        route1 = Dist_s[g]+Adj_list[g][h]+Dist_h[des]
        route2 = Dist_s[h]+Adj_list[g][h]+Dist_g[des]
        short = Dist_s[des]
        if route1>short and route2>short:
            pass
        else:
            Ans.append(des+1)
    Ans.sort()
    print(*Ans)
