from sys import *

setrecursionlimit(10**6)

def bfs_s(x,y):
    if 1 not in Adj[x]:
        return 0
    else :
        queue=[x]
        visit=[]
    while queue:
        c_node=queue.pop(0)
        for k in range(len(Adj[c_node])):
            if Adj[c_node][k] and k not in queue and k not in visit :
                if k==y:
                    return 1
                else:
                    queue.append(k)
                    visit.append(k)
    return 1 if y in visit else 0
    
N = int(input())

Adj = [list(map(int,stdin.readline().split())) for _ in range(N)]

Result=[[0]*N for _ in range(N)]

for i in range(N):
    for j in range(N):
        Result[i][j] = bfs_s(i,j)

for row in Result:
    print(*row)
