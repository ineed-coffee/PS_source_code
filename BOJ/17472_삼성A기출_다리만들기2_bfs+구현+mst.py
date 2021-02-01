from sys import *
from collections import deque
#from itertools import *
#from itertools import permutations
#from copy import *
#setrecursionlimit(10000)

def bfs(x,y):
    global Visited,Island

    Visited[x][y]=True
    que = deque([[x,y]])
    group=[]
    while que:
        cx,cy = que.popleft()
        edge=False
        for d in [[0,1],[1,0],[0,-1],[-1,0]]:
            nx,ny = cx+d[0],cy+d[1]
            if not((0<=nx<N) and (0<=ny<M)):
                continue
            
            if not Visited[nx][ny]:
                if Island[nx][ny]:
                    Visited[nx][ny]=True
                    que.append([nx,ny])

                elif not edge:
                    group.append([cx,cy])
                    edge=True

    return group

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

def find_parent(node):
    global parent

    if parent[node]==node:
        return node
    else :
        return find_parent(parent[node])

def union_find(st,ed):
    start_head,end_head = find_parent(st),find_parent(ed)
#    print(f'start={st}(p={start_head}) , end={ed}(p={end_head})')
    if start_head!=end_head:
        parent[end_head]=start_head
        return True
    else:
        return False

#--------------------------------------------------------------

input = stdin.readline
N,M = map(int,input().split())                                       # Input, Param set
Island = [[*map(int,input().split())] for _ in range(N)]
Ans=-1

#--------------------------------------------------------------
Visited=[[False]*M for _ in range(N)]
Group=[]
for i in range(N):
    for j in range(M):                                               # Get edge part of each Island   (BFS)
        if not Visited[i][j] and Island[i][j]:
            Group.append(bfs(i,j))

#--------------------------------------------------------------

G=len(Group)
dist_graph = []                                                      # Get distances of one to another
for i in range(G):
    for j in range(i+1,G):
        bridge=Available(i,j)
        if bridge:
            dist_graph.append([bridge,i,j])

#--------------------------------------------------------------
E = len(dist_graph)
parent=[i for i in range(G)]
dist_graph.sort(key=lambda x:x[0])
connected=0
for i in range(E):
    dist = dist_graph[i][0]
    s = dist_graph[i][1]
    e = dist_graph[i][2]                                             # Search MST (Kruskal)
    if union_find(s,e):
        Ans = Ans+dist if Ans!=-1 else dist
        connected+=1
#    print(parent)
    if connected==G-1:
        break

#--------------------------------------------------------------
if connected ==G-1:
    print(Ans)
else:
    print(-1)
