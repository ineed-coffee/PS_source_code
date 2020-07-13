from sys import *
setrecursionlimit(10000)

def match(x,y,cnt):
    global flag
    
    for dx,dy in D:
        nx,ny = x+dx , y+dy
        if not ((0<=nx<n)and(0<=ny<m)):
            continue
        
        if cnt and Grid[nx][ny]:
            cnt-=1
        elif cnt and not Grid[nx][ny]:
            Grid[nx][ny]+=1
            cnt-=1
            match(nx,ny,Grid[nx][ny])
        elif not cnt and Grid[nx][ny]:
            Grid[x][y]+=1

    if cnt:
        flag=False
    return



input = stdin.readline

D = [[0,-1],[-1,0],[0,1],[1,0]]

T = int(input())
for case in range(T):
    n,m = map(int,input().split())
    Grid = []
    for i in range(n):
        Grid.append([*map(int,input().split())])

    Visited=[[False]*m for _ in range(n)]
    flag=True
    for i in range(n):
        for j in range(n):
            if Grid[i][j]:
                match(i,j,Grid[i][j])
            if not flag:
                break
        if not flag:
            break

    if not flag:
        print('NO')
    else:
        print('YES')
        for row in Grid:
            print(*row)

