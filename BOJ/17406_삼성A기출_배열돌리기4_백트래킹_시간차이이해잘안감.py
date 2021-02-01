from sys import *
#from collections import deque
#from itertools import *
#from itertools import permutations
#from copy import *
#setrecursionlimit(10000)

def back_track(depth):

    if depth == K:
        Calc()
        return

    for k in range(K):
        if not Used[k]:
            Rotate(0,Spins[k])
            Used[k]=True
            back_track(depth+1)
            Used[k]=False
            Rotate(1,Spins[k])
    return

def Rotate(mode,info):
    global Matrix

    r,c,s=info
    if not mode:
        D=[[0,1],[1,0],[0,-1],[-1,0]]
    else:
        D=[[1,0],[0,1],[-1,0],[0,-1]]
        
    for ss in range(1,s+1):
        tmp = Matrix[r-ss][c-ss]
        d=0
        x,y=r-ss,c-ss
        
        while True:
            nx,ny=x+D[d][0],y+D[d][1]
            if not((r-ss<=nx<=r+ss) and (c-ss<=ny<=c+ss)):
                d+=1
                continue
            x,y = nx,ny
            tmp ,Matrix[x][y]=Matrix[x][y],tmp
            if x==r-ss and y==c-ss:
                break

    

def Calc():
    global Ans

    for row in Matrix:
        Ans = min(Ans,sum(row))


#--------------------------------------------------------------

input = stdin.readline
N,M,K = map(int,input().split())

Matrix = [[*map(int,input().split())] for _ in range(N)]

Spins =[]
for _ in range(K):
    r,c,s = map(int,input().split())
    Spins.append([r-1,c-1,s])

Ans = maxsize
Used = [False]*K
back_track(0)
print(Ans)
'''
Rotate(0,Spins[0])
for row in Matrix:
    print(row)
print('----------------------')
Rotate(1,Spins[1])
for row in Matrix:
    print(row)
'''
