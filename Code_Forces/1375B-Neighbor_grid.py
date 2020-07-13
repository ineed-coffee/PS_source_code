from sys import *

input = stdin.readline

D = [[0,-1],[-1,0],[0,1],[1,0]]

T = int(input())
for case in range(T):
    n,m = map(int,input().split())
    Grid = []
    for i in range(n):
        Grid.append([*map(int,input().split())])

    for i in range(n):
        for j in range(m):
            cnt = Grid[i][j]
            flag = True
            if not cnt: continue
            for di,dj in D:
                ni,nj = i+di , j+dj
                if not ((0<=ni<n)and(0<=nj<m)): continue
                if cnt and Grid[ni][nj]: cnt-=1
                elif cnt and not Grid[ni][nj]:
                    Grid[ni][nj]+=1
                    cnt-=1
                elif not cnt and Grid[ni][nj]:
                    flag = False
                    break
            if cnt: flag=False
            if not flag: break
        if not flag: break
    if flag:
        print('YES')
        for row in Grid:
            print(*row)
    else:
        print('NO')
