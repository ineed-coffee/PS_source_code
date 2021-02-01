from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)

def Queen(idx,cnt):
    global Ans

    if not cnt:
        Ans+=1
        return

    for j in range(N):
            if Board[idx][j]:
                back = fill(idx,j,[])
                Queen(idx+1,cnt-1)
                fill(idx,j,back)

    return
                
def fill(x,y,back_l):
    global Board

    if back_l:
        for xy in back_l:
            Board[xy[0]][xy[1]]=True
        return
    
    return_list=[]
    for d in [[1,-1],[1,1],[1,0]]:
        nx,ny = x,y
        while (0<=nx<N)and(0<=ny<N):
            if Board[nx][ny]:
                Board[nx][ny]=False
                return_list.append([nx,ny])
            nx+=d[0]
            ny+=d[1]

    return return_list
            
input = stdin.readline
N = int(input())
Board=[[True]*N for _ in range(N)]
Ans = 0
Queen(0,N)
print(Ans)
