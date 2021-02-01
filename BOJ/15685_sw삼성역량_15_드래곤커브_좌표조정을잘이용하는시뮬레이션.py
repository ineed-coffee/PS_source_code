from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)


def draw(x,y,trace,gen,cur_gen):

    global Axis

    Axis[x][y]=True

    if cur_gen == gen+1:
        return
    
    if type(trace) == type(3):

        nx,ny = x+dx[trace],y+dy[trace]
        if (0<=nx<=100) and (0<=ny<=100):
            draw(nx,ny,[trace],gen,cur_gen+1)

    elif type(trace) == type([]):
        tmp=[]
        
        for direction in trace:
            nx,ny = x+dx[(direction+1)%4],y+dy[(direction+1)%4]
            if (0<=nx<=100) and (0<=ny<=100):
                Axis[nx][ny]=True
                x,y = nx,ny
                tmp.append((direction+1)%4)
        tmp.reverse()
        draw(x,y,tmp+trace,gen,cur_gen+1)


input = stdin.readline

N = int(input())
Curve_info = [list(map(int,input().split())) for _ in range(N)]

Axis = [[False]*101 for _ in range(101)]
dx = [0,-1,0,1]
dy = [1,0,-1,0]
Ans = 0


for curve in Curve_info:
    x,y,d,g = curve
    draw(y,x,d,g,0)
    
for i in range(100):
    for j in range(100):
        if Axis[i][j] and Axis[i+1][j] and Axis[i][j+1] and Axis[i+1][j+1]:
            Ans+=1
print(Ans)
