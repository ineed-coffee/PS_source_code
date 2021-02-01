from sys import *
#from collections import deque
#from itertools import combinations
#setrecursionlimit(10000)

def roate(deg , shape):

    if not deg:
        return shape
    elif deg ==1:
        return list(map(lambda x:[x[1],-x[0]],shape))
    elif deg ==2:
        return list(map(lambda x:[-x[0],-x[1]],shape))
    elif deg ==3:
        return list(map(lambda x:[-x[1],x[0]],shape))

def tetro(idx,shape,x,y):
    global Ans
    
    for i in range(rot_dif[idx]):
        Flag = True
        Sum = Board[x][y]
        for cord in roate(i,shape):
            nx = x + cord[0]
            ny = y + cord[1]
            if (0<=nx<N) and (0<=ny<M):
                Sum+=Board[nx][ny]
            else:
                Flag = False
        if Flag:
            Ans = max(Ans,Sum)
        



input = stdin.readline

N,M= map(int,input().split())

Board = [list(map(int,input().split())) for _ in range(N)]


shape1 = [[0,1],[0,2],[0,3]] #----
shape2 = [[1,0],[0,1],[1,1]] # ㅁ
shape3 = [[1,0],[2,0],[2,1]] # ㄴ
shape4 = [[1,0],[1,1],[2,1]] # ㄹ
shape5 = [[0,1],[0,2],[1,1]] # ㅜ
shape6 = [[1,0],[2,0],[2,-1]] # ㄱ
shape7 = [[1,0],[1,-1],[2,-1]] # *ㄹ
shape = [shape1,shape2,shape3,shape4,shape5,shape6,shape7]
rot_dif = [2,1,4,4,4,4,4]
Ans = 0

for i in range(N):
    for j in range(M):
        for idx,s in enumerate(shape):
                tetro(idx,s,i,j)
print(Ans)
