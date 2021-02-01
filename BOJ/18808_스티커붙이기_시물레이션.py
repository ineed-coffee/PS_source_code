from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)

def Rotate(matrix):

    matrix = list(zip(*reversed(matrix)))
    return matrix

def fill(w,h):
    global Board,Ans
    
    for i in range(N):
        for j in range(M):
            
            if not ((i+h<=N) and (j+w<=M)):
                continue

            flag=False
            for ii in range(i,i+h):
                for jj in range(j,j+w):
                    if Board[ii][jj] and cur_shape[ii-i][jj-j]:
                        flag=True
                        break
                if flag:
                    break
            if flag:
                continue
            
            for ii in range(i,i+h):
                for jj in range(j,j+w):
                    if cur_shape[ii-i][jj-j]:
                        Board[ii][jj]=1
                        Ans+=1
            return True

    return False

N,M,K = map(int,input().split())
Ans = 0
Board=[[0]*M for _ in range(N)]
Sticker=[]

for k in range(K):
    r,c=map(int,input().split())    
    s=[]
    for row in range(r):
        s.append([*map(int,input().split())])

    Sticker.append(s)


for sticker in Sticker:
    w,h=len(sticker[0]),len(sticker)

    for shape in range(4):
        if not shape:
            cur_shape=sticker
        else:
            cur_shape=Rotate(cur_shape)

        width,height=len(cur_shape[0]),len(cur_shape)
        if fill(width,height):
            break

print(Ans)


'''
    for i in range(N):
        for j in range(M):
            if Board[i][j]:
                continue
            if not ((i+h<=N) and (j+w<=M)):
                continue
            flag=False
            for ii in range(i,i+h):
                for jj in range(j,j+w):
                    if Board[ii][jj]:
                        flag=True
                        break
                if flag:
                    break
            if flag:
                continue

            for ii in range(i,i+h):
                for jj in range(j,j+w):
                    Board[ii][jj]=sticker[ii-i][jj-j]
                    if sticker[ii-i][jj-j]:
                        Ans-=1
'''                      
    
