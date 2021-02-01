from sys import *
from collections import deque
setrecursionlimit(100000)




def dfs_s(r,c,l,cnt):
    global Visited,Escaped
    
    Visited[l][r][c] = True

    for i in range(6):
        nr = r + dx[i]
        nc = c + dy[i]
        nh = l + dh[i]

        if (0<=nr<R) and (0<=nc<C) and (0<=nh<L):
            if not Visited[nh][nr][nc] and building[nh][nr][nc]=='.':
                dfs_s(nr,nc,nh,cnt+1)
                Visited[nh][nr][nc]=False
                
            elif not Visited[nh][nr][nc] and building[nh][nr][nc]=='E':
                Escaped.append(cnt+1)
                
def bfs_s(r,c,l):
    global Visited,Escaped

    Visited[l][r][c] = True
    que = deque([[r,c,l,0]])

    while que :
        cr,cc,ch,cnt = que.popleft()

        for i in range(6):
            nr = cr + dx[i]
            nc = cc + dy[i]
            nh = ch + dh[i]

            if (0<=nr<R) and (0<=nc<C) and (0<=nh<L):
                if not Visited[nh][nr][nc] and building[nh][nr][nc]=='.':
                    Visited[nh][nr][nc]=True
                    que.append([nr,nc,nh,cnt+1])
                
                elif not Visited[nh][nr][nc] and building[nh][nr][nc]=='E':
                    Escaped = cnt+1
                    return

dx = [-1,0,1,0,0,0]
dy = [0,-1,0,1,0,0]
dh = [0,0,0,0,-1,1]
while True:
    L,R,C = map(int,stdin.readline().split())

    if not L and not R and not C:
        break
    
    building = [[0]*R for _ in range(L)]
    for floor in range(L):
        for row in range(R+1):
            line = list(stdin.readline().strip())
            if row!=R:
                if 'S' in line :
                    sh,sr,sc = floor,row,line.index('S')
                    
                building[floor][row] = line
    Visited=[[[False]*C for i in range(R)] for j in range(L)]
        
    Escaped=0

    bfs_s(sr,sc,sh)

    if Escaped:
        print(f'Escaped in {Escaped} minute(s).')
    else:
        print('Trapped!')
    
