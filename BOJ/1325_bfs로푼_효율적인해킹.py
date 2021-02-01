from sys import *
from collections import deque
#setrecursionlimit(100000)




def bfs_s(start):
    global Hacked

    Hacked[start] =True
    que = deque([start])
    group=[start]

    while que:
        parent = que.popleft()
        for child in Adj[parent]:
            if not Hacked[child]:
                Hacked[child]=True
                que.append(child)
                group.append(child)
    
    return len(group)
                    
                

    


max_hack,max_num = [],0
N,M = map(int,stdin.readline().split())

Adj = [[] for _ in range(N+1)]

for i in range(M):
    a,b = map(int,stdin.readline().split())

    Adj[b].append(a)

for j in range(1,N+1):
    if Adj[j]:
        Hacked=[False]*(N+1)
        cnt = bfs_s(j)
        if cnt > max_num:
            max_hack = [j]
            max_num=cnt
        elif cnt == max_num:
            max_hack.append(j)
max_hack.sort()
print(*max_hack)
