from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)

def Game(idx,cnt):
    global Done,Board,row,col,block

    if Done:
        return

    if not cnt:
        Done=True
        for r in range(1,10):
            print(*Board[r][1:])
        return

    x,y = empty[idx]
    c = 3*((x-1)//3)+(((y-1)//3)+1)

    for num in range(1,10):
        if Done:
            return
        if not row[x][num] and not col[y][num] and not block[c][num]:
            row[x][num]=True
            col[y][num]=True
            block[c][num]=True
            Board[x][y]=num
            Game(idx+1,cnt-1)
            Board[x][y]=0
            row[x][num]=False
            col[y][num]=False
            block[c][num]=False
    return
            
input = stdin.readline
Board=[[0]*10]
for _ in range(9):
    Board.append([0]+[*map(int,input().split())])
empty=[]
row = [[False]*10 for _ in range(10)]
col = [[False]*10 for _ in range(10)]
block = [[False]*10 for _ in range(10)]

for i in range(1,10):
    for j in range(1,10):
        val = Board[i][j]
        if val:
            center = 3*((i-1)//3)+(((j-1)//3)+1)
            row[i][val]=True
            col[j][val]=True
            block[center][val]=True
        else:
            empty.append([i,j])
Done =False
Game(0,len(empty))
