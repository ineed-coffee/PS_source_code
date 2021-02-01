from sys import *
setrecursionlimit(100000)

def all_zero():
    global Flag,no_melt
    Sum=0
    for row in Ice_burg:
        Sum += sum(row)
    if not Sum:
        Flag = False
        no_melt = True
    return 

def dfs_s(x,y):
    global Visited
    Visited[x][y] = True

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if Ice_burg[nx][ny] and not Visited[nx][ny]:
            dfs_s(nx,ny)

def split_search():
    global Flag
    cnt=0
    for i in range(1,N-1):
        for j in range(1,M-1):
            if Ice_burg[i][j] and not Visited[i][j]:
                cnt+=1
                if cnt>=2:
                    Flag=False
                    return
                dfs_s(i,j)


N,M = map(int,stdin.readline().split())

Ice_burg = [list(map(int,stdin.readline().split())) for _ in range(N)]
dx = [-1,0,1,0]
dy = [0,-1,0,1]
Flag = True
no_melt=False
year = 0

while Flag :
    Visited = [[False]*M for _ in range(N)]
    Melt_matrix = [[0]*M for _ in range(N)]
    if year:
        all_zero()
        split_search()
        if not Flag:
            break
    year+=1
    for i in range(1,N-1):
        for j in range(1,M-1):
            if Ice_burg[i][j]:
                for k in range(4):
                    ni= i + dx[k]
                    nj= j + dy[k]
                    if not Ice_burg[ni][nj]:
                        Melt_matrix[i][j]+=1

    for i in range(1,N-1):
        for j in range(1,M-1):
            Ice_burg[i][j]=max(0,Ice_burg[i][j]-Melt_matrix[i][j])


print(year if not no_melt else 0)
