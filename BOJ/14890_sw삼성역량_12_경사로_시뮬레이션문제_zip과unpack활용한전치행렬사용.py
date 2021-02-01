from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)


def Take_road(road):
    global Route
    comp=road[0]
    deployed=[False]*N
    
    for k in range(N):
        if abs(road[k]-comp)>1:
            return

        elif road[k] == comp-1:
            for l in range(L):
                if k+L >N or road[k+l]!=road[k] or deployed[k+l]:
                    return
                deployed[k+l]=True
            comp = road[k]
            
        elif road[k] == comp+1:
            for l in range(1,L+1):
                if k-l <0 or road[k-l]!=road[k-1] or deployed[k-l]:
                    return
                deployed[k-l]=True
            comp = road[k]
    print(road)
    Route+=1
    return


input = stdin.readline

N,L= map(int,input().split())

map_info_row = [list(map(int,input().split())) for _ in range(N)]

map_info_col = list(zip(*map_info_row))

map_info = map_info_row+map_info_col

Route=0

for path in map_info:

    Take_road(path)

print(Route)
