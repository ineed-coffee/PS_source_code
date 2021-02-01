from sys import *
from collections import deque
#setrecursionlimit(10000)


def bfs_s(start):
    global Visited,Coords
    
    Visited[start] = True
    que = deque([Coords[start]])

    while que:
        c_xy = que.popleft()
        
        for i in range(conv_n+2):
            if c_xy != Coords[i]:
                if not Visited[i]:
                    if abs(c_xy[0]-Coords[i][0])+abs(c_xy[1]-Coords[i][1]) <=1000:
                        Visited[i]=True
                        que.append(Coords[i])
                        if i == conv_n+1:
                            return True
    
    return False

test_case = int(input())

for case in range(test_case):
    conv_n = int(stdin.readline())

    Coords=[]
    for c in range(conv_n+2):
        Coords.append(list(map(int,stdin.readline().split())))
        
    Visited=[False]*(conv_n+2)
    
    if bfs_s(0):
        print('happy')
    else :
        print('sad')
