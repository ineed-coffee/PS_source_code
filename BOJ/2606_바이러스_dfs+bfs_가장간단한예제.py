from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

input = stdin.readline
N = int(input())
adj_list=[[] for i in range(N+1)]
info_cnt=int(input())
for i in range(info_cnt):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

Visited=[False]*(N+1)
Visited[1]=True
Ans=0
que=deque([1])

while que:
    c_com=que.popleft()

    for nxt in adj_list[c_com]:
        if not Visited[nxt]:
            Visited[nxt]=True
            que.append(nxt)
            print(nxt)
            Ans+=1

print(Ans)



'''
-----bfs+adjoint_matrix-------------

input = stdin.readline
N = int(input())
Adj=[[0]*(N+1) for _ in range(N+1)]
info_cnt=int(input())
for i in range(info_cnt):
    a,b=map(int,input().split())
    Adj[a][b]=1
    Adj[b][a]=1

Visited=[False]*(N+1)
Visited[1]=True
Ans=0
que=deque([1])

while que:
    c_com=que.popleft()

    for n in range(1,N+1):
        if Adj[c_com][n] and not Visited[n]:
            Visited[n]=True
            que.append(n)
            Ans+=1

print(Ans)


-----bfs+adjoint_list-------------

input = stdin.readline
N = int(input())
adj_list=[[] for i in range(N+1)]
info_cnt=int(input())
for i in range(info_cnt):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

Visited=[False]*(N+1)
Visited[1]=True
Ans=0
que=deque([1])

while que:
    c_com=que.popleft()

    for nxt in adj_list[c_com]:
        if not Visited[nxt]:
            Visited[nxt]=True
            que.append(nxt)
            Ans+=1

print(Ans)

-----dfs+adjoint_list-------------

def dfs(node):
    global Visited,Ans

    Visited[node]=True
    Ans+=1

    for nxt in adj_list[node]:
        if not Visited[nxt]:
            dfs(nxt)


input = stdin.readline
N = int(input())
adj_list=[[] for i in range(N+1)]
info_cnt=int(input())
for i in range(info_cnt):
    a,b=map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)

Visited=[False]*(N+1)
Visited[1]=True
Ans=0
dfs(1)
print(Ans-1)
'''
