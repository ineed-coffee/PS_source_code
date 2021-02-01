from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)
    
input = stdin.readline

N,K = map(int,input().split())
Board = [list(map(int,input().split())) for _ in range(N)]
Piece_info = []
Placed = [[[] for i in range(N)] for j in range(N)]
for p in range(K):
    line = list(map(int,input().split()))
    Piece_info.append([line[0]-1,line[1]-1,line[-1]])
    Placed[line[0]-1][line[1]-1].append(p)

Direction = {1:[0,1],2:[0,-1],3:[-1,0],4:[1,0]}

Turn=0
Flag=False

while True:

    if Turn >1000:
        Turn = -1
        break
    
    Turn+=1

    for num,piece in enumerate(Piece_info):
        x,y,d=piece
        nx,ny = x+Direction[d][0] , y+Direction[d][1]
#--------------------------------------------------------------------------------------
        if not((0<=nx<N)and(0<=ny<N)) or Board[nx][ny]==2:  
            opp = 1 if d%2 else -1
            d+=opp
            piece[-1]=d
            nnx,nny = nx+(2*Direction[d][0]),ny+(2*Direction[d][1])

            if not((0<=nnx<N)and(0<=nny<N)) or Board[nnx][nny]==2:

                pass

            elif Board[nnx][nny] == 1:        
                idx = Placed[x][y].index(num)
                part = reversed(Placed[x][y][idx:])
                Placed[x][y]=Placed[x][y][:idx]
                for p in part:
                    Piece_info[p][0]=nnx
                    Piece_info[p][1]=nny                                     #blue
                    Placed[nnx][nny].append(p)
                    if len(Placed[nnx][nny])>=4:
                        Flag=True
                        break

            elif not Board[nnx][nny]:        
                idx = Placed[x][y].index(num)
                part = Placed[x][y][idx:]
                Placed[x][y]=Placed[x][y][:idx]
                for p in part:
                    Piece_info[p][0]=nnx
                    Piece_info[p][1]=nny
                    Placed[nnx][nny].append(p)
                    if len(Placed[nnx][nny])>=4:
                        Flag=True
                        break

#--------------------------------------------------------------------------------------            

        elif Board[nx][ny] == 1:        
            idx = Placed[x][y].index(num)
            part = reversed(Placed[x][y][idx:])
            Placed[x][y]=Placed[x][y][:idx]
            for p in part:                                                    #red
                Piece_info[p][0]=nx
                Piece_info[p][1]=ny
                Placed[nx][ny].append(p)
                if len(Placed[nx][ny])>=4:
                    Flag=True
                    break
#--------------------------------------------------------------------------------------
        elif not Board[nx][ny]:        
            idx = Placed[x][y].index(num)
            part = Placed[x][y][idx:]
            Placed[x][y]=Placed[x][y][:idx]
            for p in part:                                                    #white
                Piece_info[p][0]=nx
                Piece_info[p][1]=ny
                Placed[nx][ny].append(p)
                if len(Placed[nx][ny])>=4:
                    Flag=True
                    break
#--------------------------------------------------------------------------------------
        if Flag:
            break
    
    if Flag:
        break

print(Turn)
