from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def population_change(group_list):
    global Area

    for g in group_list:
        unit = g[0]
        Sum=g[1]

        new_pop = Sum//len(unit)
        for u in range(len(unit)):
            Area[unit[u][0]][unit[u][1]] = new_pop


def bfs_s(x,y):
    global Visited

    Visited[x][y]=True
    que = deque([[x,y]])
    return_list = [[x,y]]
    return_sum=Area[x][y]
    while que:
        cx,cy = que.pop()

        for i in range(4):
            nx = cx+dx[i]
            ny = cy+dy[i]
            if (0<=nx<N) and (0<=ny<N):
                if not Visited[nx][ny] and (L<=abs(Area[cx][cy]-Area[nx][ny])<=R):
                    Visited[nx][ny]=True
                    que.append([nx,ny])
                    return_list.append([nx,ny])
                    return_sum+=Area[nx][ny]

    if len(return_list)==1:
        Visited[x][y]=False
        return [0,0]

    else:
        return [return_list,return_sum]
        

def find_units():

    units = []
    
    for i in range(N):
        for j in range(N):
            if not Visited[i][j]:
                tmp_list,tmp_sum= bfs_s(i,j)
                if tmp_list:
                    units.append([tmp_list,tmp_sum])

    return units

            
input = stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]
N,L,R = map(int,input().split())                        
Area = [list(map(int,input().split())) for _ in range(N)]
Ans =0

while True:
    
    Visited = [[False]*N for _ in range(N)]
    groups = find_units()

    if groups:

        population_change(groups)
        Ans+=1

    else:

        break
    
print(Ans)
