from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

def bfs():
    global Visited,Ans
    
    que=deque([[0,0,False]])
    return_cnt=1
    while que:

        L = len(que)
        for l in range(L):
            cx,cy,cbroke=que.popleft()
            if cx==N-1 and cy==M-1:
                Ans=return_cnt
                return
            for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                nx,ny=cx+d[0],cy+d[1]
                
                if not((0<=nx<N)and(0<=ny<M)):
                    continue

                if not cbroke and not Visited[0][nx][ny]:
                    if Map[nx][ny]=='0':
                        Visited[0][nx][ny]=True
                        que.append([nx,ny,cbroke])
                    elif Map[nx][ny]=='1':S
                        Visited[1][nx][ny]=True
                        que.append([nx,ny,True])

                elif cbroke and not Visited[1][nx][ny]:
                    if Map[nx][ny]=='0':
                        Visited[1][nx][ny]=True
                        que.append([nx,ny,cbroke])

        return_cnt+=1

    return


input = stdin.readline
N,M = map(int,input().split())
Map=[list(input().strip()) for _ in range(N)]
Visited=[[[False]*M for i in range(N)] for j in range(2)]
Ans=-1
bfs()
print(Ans)
   

