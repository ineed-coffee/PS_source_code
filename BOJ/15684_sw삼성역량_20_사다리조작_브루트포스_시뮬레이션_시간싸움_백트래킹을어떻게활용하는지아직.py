from sys import *
from collections import deque
from itertools import *
#from copy import *
#setrecursionlimit(10000)

def is_matched():
    
    for start in range(1,N+1):
        step , fin = 0,start
        downward =True
        direction = down
        while True:
            step+=direction[0]
            fin+=direction[1]
            if step > H:
                if fin == start:
                    break
                else:
                    return False 
            if downward and not init_ladder[step][fin]:
                direction=down
            elif downward and init_ladder[step][fin]:
                direction=init_ladder[step][fin]
                downward=False
            elif not downward and init_ladder[step][fin]:
                direction=down
                downward=True

    return True 

def is_placeable(xy_list):

    global init_ladder
    
    for idx,xy in enumerate(xy_list):

        if (xy[1]-1>0 and init_ladder[xy[0]][xy[1]-1]) and init_ladder[xy[0]][xy[1]]:
            return [False,idx]

        if (xy[1]+1<=N and init_ladder[xy[0]][xy[1]+1]):
            return [False,idx]

        init_ladder[xy[0]][xy[1]]=right
        init_ladder[xy[0]][xy[1]+1]=left

    return [True,idx+1]

input = stdin.readline

N,M,H = map(int,input().split())                        
down,right,left = [1,0],[0,1],[0,-1]
init_ladder = [[0]*(N+1) for _ in range(H+2)]
cord_map = [[(i//(N-1))+1,(i%(N-1))+1] for i in range(H*(N-1))]

for _ in range(M):
    a,b = map(int,input().split())
    init_ladder[a][b]=right
    init_ladder[a][b+1]=left
    cord_map.remove([a,b])
    if b+1 < N:
        cord_map.remove([a,b+1])

if is_matched():
    print(0)
else:
    Available=False
    for cnt in range(1,len(cord_map)+1):

        if cnt ==4 or Available:
            break
        comb = combinations(cord_map,cnt)
        for cords in comb:
            cords = list(cords)
            flag,idx = is_placeable(cords)
            if flag:
                if is_matched():
                    Available=True
                    print(cnt)
                    break

            for i in range(idx):
                xy=cords[i]
                init_ladder[xy[0]][xy[1]]=0
                init_ladder[xy[0]][xy[1]+1]=0

    if not Available:
        print(-1)
