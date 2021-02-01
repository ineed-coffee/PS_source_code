from sys import *
from collections import deque
from itertools import *
#from copy import *
#setrecursionlimit(100000)

def Combinations(matrix,cnt):

    L=len(matrix)
    return_list=[]

    if cnt==1:
        for i in matrix:
            return_list.append([i])
        return return_list

    for i in range(L-cnt+1):
        for part in Combinations(matrix[i+1:],cnt-1):
            return_list.append([matrix[i]]+part)

    return return_list

def bfs(Ggroup,Rgroup):

    global G_visited,R_visited,Comp

    for g in Ggroup:
        G_visited[g]=1
    for r in Rgroup:
        R_visited[r]=1
        
    que1 = deque(Ggroup)
    que2 = deque(Rgroup)
    mark=1
    while que1 or que2:
        mark+=1

        if que1:
            L1 = len(que1)
            ad_dq1=[]
            for l in range(L1):
                c = que1.popleft()
                cx,cy=c//M,c%M
                for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nx,ny = cx+d[0] , cy+d[1]
                    if not((0<=nx<N) and (0<=ny<M)):
                        continue
                    if not G_visited[nx*M+ny] and Garden[nx][ny]:
                        G_visited[nx*M+ny]=mark
                        ad_dq1.append(nx*M+ny)
        

        if que2:
            L2 = len(que2)
            ad_dq2=[]
            for l in range(L2):
                c = que2.popleft()
                cx,cy=c//M,c%M
                for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                    nx,ny = cx+d[0] , cy+d[1]
                    if not((0<=nx<N) and (0<=ny<M)):
                        continue
                    if not R_visited[nx*M+ny] and Garden[nx][ny]:
                        R_visited[nx*M+ny]=mark
                        ad_dq2.append(nx*M+ny)

        part1=deque(set(ad_dq1)-set(ad_dq2))
        part2=deque(set(ad_dq2)-set(ad_dq1))
        overlap=len(ad_dq1)-len(part1)
        Comp+=overlap
        que1+=part1
        que2+=part2

    return

N,M,G,R = map(int,input().split())
Ans = 0

Garden = []
Seed=[]
for i in range(N):
    line = list(map(int,input().split()))

    for j in range(M):
        if line[j]==2:
            Seed.append(i*M+j)

    Garden.append(line)

for comb in combinations(Seed,G+R):
    
    for G_comb in combinations(comb,G):

        R_comb = list(set(comb)-set(G_comb))
        G_visited=[0]*(N*M)
        R_visited=[0]*(N*M)
        Comp=0
        bfs(G_comb,R_comb)
        Ans = max(Ans,Comp)

print(Ans)
