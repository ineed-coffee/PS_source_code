from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

input = stdin.readline

R,C,M = map(int,input().split())

Shark_info=[[i]+[0]*M for i in range(2)]
Pool = [[0]*(C+1) for _ in range(R+1)]
Dir = {1:[-1,0] , 2:[1,0] , 3:[0,1] , 4:[0,-1]}

for m in range(1,M+1):
    x,y,*info = list(map(int,input().split()))
    Shark_info[0][m] = [[x,y]]+info
    Pool[x][y]=m


cmp_cnt=0  
Caught=0
for col in range(1,C+1):
#----------------------------------------------------------------------
    for row in range(1,R+1):

        if Pool[row][col]:          

            shark_num=Pool[row][col]                                      # Fisher's move
            if not Shark_info[1][shark_num]:                   
                Caught+=Shark_info[0][shark_num][3]
                Pool[row][col]=0
                Shark_info[1][shark_num]=1
                break

#----------------------------------------------------------------------
    if cmp_cnt == M:
        break
    
    new_Pool = [[0]*(C+1) for _ in range(R+1)]
    for m in range(1,M+1):
        if not Shark_info[1][m]:
            info = Shark_info[0][m]
            x,y = info[0]
            sustain = info[1]
            if info[2]<3:
                sustain = sustain%((R-1)*2)
            else:
                sustain = sustain%((C-1)*2)
            while sustain:
                dx,dy = Dir[info[2]]
                nx,ny = x+dx , y+dy
                if not ((0<nx<=R) and (0<ny<=C)):
                    switch = 1 if info[2]%2 else -1                        # Fisher's move
                    info[2] = info[2]+switch
                    continue
                x,y  = nx,ny
                sustain-=1 

            if not new_Pool[x][y]:
                new_Pool[x][y] = m
                info[0]=[x,y]

            else:
                cmp_shark_info = Shark_info[0][new_Pool[x][y]]
                if cmp_shark_info[3] > info[3]:
                    Shark_info[1][m]=1
                else:
                    Shark_info[1][new_Pool[x][y]]=1
                    new_Pool[x][y] = m
                    info[0]=[x,y]

    Pool = new_Pool

#----------------------------------------------------------------------
print(Caught)
