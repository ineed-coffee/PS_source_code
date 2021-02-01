from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *


def bfs(x,y):
    Visited[x][y]=True
    Room[x][y]=r_cnt
    que = deque([[x,y]])
    size=1
    while que:
        cx,cy = que.popleft()
        for d in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx,ny = cx+d[0],cy+d[1]
            if not((0<=nx<m)and(0<=ny<n)):
                continue
            if not blocked(cx,cy,nx,ny) and not Visited[nx][ny]:
                Visited[nx][ny]=True
                Room[nx][ny]=r_cnt
                size+=1
                que.append([nx,ny])
        
    return size

def blocked(x1,y1,x2,y2):

    if x2==x1+1 and Castle[x1][y1][0] =='0':
        return False
    elif x2==x1-1 and Castle[x1][y1][2]=='0':
        return False
    elif y2==y1+1 and Castle[x1][y1][1]=='0':
        return False
    elif y2==y1-1 and Castle[x1][y1][3]=='0':
        return False

    return True
    
input = stdin.readline

n,m = map(int,input().split())

Castle = []
for i in range(m):
    line = [*map(lambda x: '0'*(4-(len(bin(int(x)))-2))+bin(int(x))[2:],input().split())]
    Castle.append(line)

Room = [[0]*n for _ in range(m)]
Visited=[[False]*n for _ in range(m)]
r_cnt=0
r_max=0
r_wall_max = 0
Sizes = {}
for i in range(m):
    for j in range(n):
        if not Visited[i][j]:
            r_cnt+=1
            c_size = bfs(i,j)
            Sizes[r_cnt]=c_size
            r_max = max(r_max,c_size)

for i in range(m):
    for j in range(n):
        for d in [[1,0],[0,1],[-1,0],[0,-1]]:
            ni,nj = i+d[0],j+d[1]
            if not ((0<=ni<m)and(0<=nj<n)):
                continue
            if Room[i][j]!=Room[ni][nj]:
                r_wall_max = max(r_wall_max,Sizes[Room[i][j]]+Sizes[Room[ni][nj]])

print(r_cnt)
print(r_max)
print(r_wall_max)

