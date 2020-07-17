from sys import *
from itertools import combinations
input = stdin.readline

N = int(input())
Teachers,Students,Empty=[],[],[]
Room=[]
for i in range(N):
    line = input().rstrip().split()
    for j in range(N):
        if line[j]=='T':
            Teachers.append([i,j])
        elif line[j]=='S':
            Students.append([i,j])
        else:
            Empty.append([i,j])
    Room.append(line)
    
Combs = combinations(Empty,3)
flag=True
for bomb1,bomb2,bomb3 in Combs:
    
    x1,y1=bomb1
    x2,y2=bomb2
    x3,y3=bomb3

    Room[x1][y1]='O'
    Room[x2][y2]='O'
    Room[x3][y3]='O'
    flag=True    
    for tx,ty in Teachers:
        for d in [[1,0],[0,1],[-1,0],[0,-1]]:
            nx,ny=tx+d[0],ty+d[1]
            while ((0<=nx<N)and(0<=ny<N)):
                if Room[nx][ny]=='O':
                    break
                if Room[nx][ny]=='S':
                    flag=False
                    break
                nx+=d[0]
                ny+=d[1]

            if not flag:
                break
        if not flag:
            break
    if flag:
        break
    else:
        Room[x1][y1]='X'
        Room[x2][y2]='X'
        Room[x3][y3]='X'
if not flag:
    print('NO')
else:
    print('YES')


#Brute Force #Combinations #Simulation
