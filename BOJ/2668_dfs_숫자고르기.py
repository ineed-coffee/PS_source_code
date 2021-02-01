from sys import *
#from collections import deque
setrecursionlimit(10000)

def dfs_s(start,cycle):
    global Visited,Cycle
    
    Visited[start]=True
    cycle.append(start)
    
    if Adj[start]:
        new_start = Adj[start]
        if not Visited[new_start]:
            dfs_s(new_start,cycle)
        elif new_start in cycle:
            idx = cycle.index(new_start)
            Cycle += cycle[idx:]





N = int(input())
Adj = [0 for _ in range(N+1)]
for i in range(1,N+1):
    a = int(stdin.readline())
    Adj[i]=a

Cycle=[]
Visited=[False]*(N+1)
for j in range(1,N+1):
    if not Visited[j] and Adj[j]:
        dfs_s(j,[])

Cycle.sort()
print(len(Cycle))
for num in Cycle:
    print(num)
