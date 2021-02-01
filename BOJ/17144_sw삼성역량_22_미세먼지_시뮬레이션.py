from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def bfs(xy):
    return     


input = stdin.readline
clockwise=0
R,C,T = map(int,input().split())                        
Room = []
for i in range(R):
    dust = list(map(int,input().split()))

    if not clockwise and -1 in dust:
        counter_clockwise = [i,dust.index(-1)]
        clockwise = [i+1,dust.index(-1)]

    Room.append(dust)

clockwise_dir = [[0,1],[1,0],[0,-1],[-1,0]]
counter_clockwise_dir = [[0,1],[-1,0],[0,-1],[1,0]]

for time in range(T):
#--------------------------------------------------------------------    
    Spread = [[0]*C for _ in range(R)]

    for i in range(R):
        for j in range(C):
            if Room[i][j]>0:
                cnt=0
                for d in [[1,0],[0,1],[-1,0],[0,-1]]:
                    ni,nj = i+d[0],j+d[1]
                    if (0<=ni<R) and (0<=nj<C)and Room[ni][nj]!=-1:   # Dust spread
                        cnt+=1
                        Spread[ni][nj]+=Room[i][j]//5

                Spread[i][j]-= cnt*(Room[i][j]//5)
    for i in range(R):
        for j in range(C):
            Room[i][j]+=Spread[i][j]

#---------------------------------------------------------------------
    
    idx1,idx2 = 0,0
    tmp1,tmp2 = 0,0
    cw_x,cw_y = clockwise
    ccw_x,ccw_y = counter_clockwise
    done_c , done_cc = False , False
    
    while not done_c or not done_cc:

        if not done_c:
            dx,dy = clockwise_dir[idx1]
            cw_x += dx
            cw_y += dy
            tmp1,Room[cw_x][cw_y] = Room[cw_x][cw_y],tmp1
            if [cw_x + dx,cw_y + dy] == clockwise:           # Circulate
                done_c = True
            elif not ((0<=cw_x + dx<R)and(0<=cw_y + dy<C)):
                idx1+=1

        if not done_cc:
            dx,dy = counter_clockwise_dir[idx2]
            ccw_x += dx
            ccw_y += dy
            tmp2,Room[ccw_x][ccw_y] = Room[ccw_x][ccw_y],tmp2
            if [ccw_x + dx,ccw_y + dy]==counter_clockwise:
                done_cc = True
            elif not ((0<=ccw_x + dx<R)and(0<=ccw_y + dy<C)):
                idx2+=1   

#----------------------------------------------------------------------
Ans=0
for row in Room:
    Ans+=sum(row)
print(Ans+2)

