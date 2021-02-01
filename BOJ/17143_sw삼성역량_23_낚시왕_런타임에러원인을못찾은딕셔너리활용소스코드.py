from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

input = stdin.readline

R,C,M = map(int,input().split())

Shark_info={}
Pool = [[0]*(C+1) for _ in range(R+1)]
Dir = {1:[-1,0] , 2:[1,0] , 3:[0,1] , 4:[0,-1]}
for m in range(1,M+1):
    name = 'shark'+str(m)
    x,y,*info = list(map(int,input().split()))
    Pool[x][y]=m
    Shark_info[name] = [[x,y]]+info

    
Caught=0
for col in range(1,C+1):
#----------------------------------------------------------------------
    for row in range(1,R+1):

        if Pool[row][col]:

            name = 'shark'+str(Pool[row][col])                      # Fisher's move

            Caught+=Shark_info[name][3]

            del Shark_info[name]
            Pool[row][col]=0
            break

#----------------------------------------------------------------------
    if not Shark_info:
        break
    new_Pool = [[0]*(C+1) for _ in range(R+1)]
    key_to_remove = []
    for name,info in Shark_info.items():
        num = int(name[-1])
        x,y = info[0]
        sustain = info[1]
        
        while sustain:
            
            dx,dy = Dir[info[2]]
            nx,ny = x+dx , y+dy
            if not ((0<nx<=R) and (0<ny<=C)):
                switch = 1 if info[2]%2 else -1
                info[2] = info[2]+switch
                continue
            x,y  = nx,ny
            sustain-=1                                              # Shark's move

        if not new_Pool[x][y]:
            new_Pool[x][y] = num
            info[0]=[x,y]

        else:
            if Shark_info['shark'+str(new_Pool[x][y])][3] > info[3]:
                key_to_remove.append(name)
            else:
                key_to_remove.append('shark'+str(new_Pool[x][y]))
                new_Pool[x][y] = num
                info[0]=[x,y]

    Pool = new_Pool
    
    if key_to_remove:
        for key in key_to_remove:
            del Shark_info[key]

    for row in Pool:
        print(row)
#----------------------------------------------------------------------
print(Caught)
