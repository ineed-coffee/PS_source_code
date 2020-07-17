from sys import *
from itertools import combinations
input = stdin.readline


def dfs(mark,c_pos):

    for n_pos in travel[c_pos]:
        des[n_pos].append(mark)
        dfs(mark,n_pos)
    
    return

N = int(input())
des = [[] for _ in range(N+1)]
travel=[[] for _ in range(N+1)]
for i in range(N-1):
    a,b = map(int,input().split())
    travel[a].append(b)

for start in range(N+1):
    if travel[start]:
        dfs(start,start)

Ans=-1
for i in range(1,N+1):
    if len(des[i])==N-1:
        Ans=i
        break

print(Ans)


# greedy-dfs



'''
#---------- Using Floyd Warshall--------------------
Dist = [[maxsize]*(N+1) for _ in range(N+1)]
for i in range(1,N+1):
    Dist[i][i]=0
for i in range(N-1):
    a,b = map(int,input().split())
    Dist[a][b]=0
for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            Dist[i][j]=min(Dist[i][j],Dist[i][k]+Dist[k][j])

Ans=-1
for j in range(1,N+1):
    flag=True
    for i in range(1,N+1):
        if Dist[i][j]==maxsize:
            flag=False
            break
    if flag:
        Ans=j
        break

print(Ans)
#----------------------------------------------------
'''
