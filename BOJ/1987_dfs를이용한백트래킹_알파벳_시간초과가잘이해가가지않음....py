from sys import *
setrecursionlimit(10000)


def dfs_backtrack(x,y,cnt):
    global Track
    
    Track = max(Track,cnt)
    
    for i in range(4):
        new_x= x+dx[i]
        new_y= y+dy[i]
        
        if new_x<0 or new_y<0 or new_x >=R or new_y >=C:
            continue

        CN=ord(Board[new_x][new_y])-ord('A')
        if not Alphaset[CN]:
            Alphaset[CN]=1
            dfs_backtrack(new_x,new_y,cnt+1)
            Alphaset[CN]=0

    return


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]
Track=1

R,C = map(int,input().split())

Board = [list(stdin.readline().strip()) for _ in range(R)]

Alphaset=[0]*26

Alphaset[ord(Board[0][0])-ord('A')]=1

dfs_backtrack(0,0,1)
print(Track)

