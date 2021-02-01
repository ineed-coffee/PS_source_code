from sys import *
setrecursionlimit(10000)

def dfs_s(x,y,h):

    Visited[x][y]=True

    for i in range(4):
        new_x= x+dx[i]
        new_y= y+dy[i]
        if new_x<0 or new_y<0 or new_x >=N or new_y >=N:
            continue
        if not Visited[new_x][new_y] and Heights[new_x][new_y]>h:
            dfs_s(new_x,new_y,h)
    return


def Solve(h):

    cnt=0
    for i in range(N):
        for j in range(N):
            if not Visited[i][j] and Heights[i][j]>h:
                cnt+=1
                dfs_s(i,j,h)
    return cnt





dx=[-1,0,1,0]
dy=[0,-1,0,1]
N = int(input())

Mx = 0
Mn = 101
Heights=[]
Safe_zone=0

for _ in range(N):
    a= list(map(int,stdin.readline().split()))
    Mn = min(Mn,*a)
    Mx = max(Mx,*a)
    Heights.append(a)

for h in range(Mn-1,Mx+1):
    Visited=[[False]*N for _ in range(N)]
    comp = Solve(h)
    Safe_zone = max(comp,Safe_zone)

print(Safe_zone)
