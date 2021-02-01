from sys import *
from collections import deque
from heapq import heappush,heappop
#setrecursionlimit(10000)

def dij(mode,start,goal):

    global Visited

    Path = [inf]*N
    Path[start]=0
    que_f = []
    heappush(que_f,[0,start])

    while que_f:

        c_cost,c_point = heappop(que_f)

        for n_point,n_cost in Adj_forward[c_point]:
            if not Visited[c_point][n_point] and n_cost+c_cost < Path[n_point]:
                Path[n_point] = c_cost+n_cost
                heappush(que_f,[c_cost+n_cost,n_point])

    if mode==1:
        que_b = deque([goal])

        while que_b:
            c_point = que_b.popleft()
            if c_point!=start:
                for p_point,p_cost in Adj_backward[c_point]:
                    if Path[c_point] == Path[p_point]+p_cost:
                        Visited[p_point][c_point]=True
                        que_b.append(p_point)
    elif mode==2:
        print(Path[goal] if Path[goal]!=inf else -1)

                    

inf = maxsize


while True:

    N,M = map(int,stdin.readline().split())

    if not N and not M:
        break

    S,D = map(int,stdin.readline().split())
    Adj_forward = [[]*N for _ in range(N)]
    Adj_backward = [[]*N for _ in range(N)]
    for _ in range(M):
        U,V,P = map(int,stdin.readline().split())

        Adj_forward[U].append([V,P])
        Adj_backward[V].append([U,P])
        
    Visited = [[False]*N for _ in range(N)]

    dij(1,S,D)
    dij(2,S,D)
