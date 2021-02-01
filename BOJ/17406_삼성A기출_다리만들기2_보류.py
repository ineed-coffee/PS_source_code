from sys import *
from collections import deque
#from itertools import *
#from itertools import permutations
#from copy import *
#setrecursionlimit(10000)

def bfs(x,y):
    global Visited

    Visited[x][y]=True
    que = deque([[x,y]])
    group=[[x,y]]

    while que:

        cx,cy = que.popleft()
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx,ny = cx+d[0],cy+d[1]
            if not((0<=nx<N) and (0<=ny<M)):
                continue
            if not Visited[nx][ny] and Island[nx][ny]:
                Visited[nx][ny]=True
                que.append([nx,ny])
                group.append([nx,ny])

    return group

def back_track(depth,idx,cnt):
    global Ans,Connected
    
    if depth == G:
        print(Connected,cnt)
        if Ans==-1 or (Ans>0 and cnt<Ans):
            Ans=cnt
            return
    
    if not depth:
        Connected[0]=True
        back_track(depth+1,0,0)
        return
    
    for g in range(G):

        if not Connected[g]:
            bridge=Available(idx,g)
            print(f'start={idx} , end={g} , bridge = {bridge} , depth={depth}')
            if bridge:
                Connected[g]=True
                back_track(depth+1,idx,cnt+bridge)
                back_track(depth+1,g,cnt+bridge)
                Connected[g]=False
    return


def Available(s_idx,e_idx):
    dist=0
    for s in Group[s_idx]:
        for e in Group[e_idx]:
            if s[0]==e[0] and abs(s[1]-e[1])>=3:
                Valid=True
                L,R=min(s[1],e[1]),max(s[1],e[1])
                for j in range(L+1,R):
                    if Island[s[0]][j]:
                        Valid=False
                        break
                if Valid:
                    dist = min(dist,abs(s[1]-e[1])-1) if dist else abs(s[1]-e[1])-1
                    
            elif s[1]==e[1] and abs(s[0]-e[0])>=3:
                Valid=True
                U,D=min(s[0],e[0]),max(s[0],e[0])
                for i in range(U+1,D):
                    if Island[i][s[1]]:
                        Valid=False
                        break
                if Valid:
                    dist = min(dist,abs(s[0]-e[0])-1) if dist else abs(s[0]-e[0])-1
    return dist
#--------------------------------------------------------------

input = stdin.readline
N,M = map(int,input().split())

Island = [[*map(int,input().split())] for _ in range(N)]

Ans=-1
Visited=[[False]*M for _ in range(N)]
Group=[]
for i in range(N):
    for j in range(M):
        if not Visited[i][j] and Island[i][j]:
            Group.append(bfs(i,j))
G=len(Group)
Connected=[False]*G

back_track(0,0,0)

print(Ans)
