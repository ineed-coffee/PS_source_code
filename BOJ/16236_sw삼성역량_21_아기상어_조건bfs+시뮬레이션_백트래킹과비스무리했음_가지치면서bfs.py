from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def bfs(xy):
    global Visited

    Visited[xy[0]][xy[1]]=True
    que = deque([[xy,0]])
    return_list=[]
    min_move=0
    while que:

        [c_x,c_y],c_move = que.popleft()
        if min_move and c_move>min_move:
            continue
        for i in range(4):
            n_x,n_y = c_x+dx[i],c_y+dy[i]
            if (0<=n_x<N) and (0<=n_y<N) and not Visited[n_x][n_y]:
                
                if not Under_water[n_x][n_y] or Under_water[n_x][n_y]==shark_size:
                    Visited[n_x][n_y]=True
                    que.append([[n_x,n_y],c_move+1])

                elif Under_water[n_x][n_y] < shark_size:
                    Visited[n_x][n_y]=True
                    if not min_move:
                        min_move = c_move+1
                        return_list=[[n_x,n_y]]
                    elif c_move+1 < min_move:
                        min_move = c_move+1
                        return_list=[[n_x,n_y]]
                    elif c_move+1 == min_move:
                        return_list.append([n_x,n_y])

    return [return_list,min_move]        


input = stdin.readline

N = int(input())                        
Under_water=[]
shark_size = 2
ate_fish=0
time = 0
dx,dy = [0,1,0,-1],[1,0,-1,0]
for i in range(N):
    line = list(map(int,input().split()))
    if 9 in line:
        shark_pos =[i,line.index(9)]
    Under_water.append(line)

while True:
    
    Visited=[[False]*N for _ in range(N)]
    fish_list,move_cnt = bfs(shark_pos)

    if not fish_list:
        print(time)
        break

    else:
        fish_to_eat = fish_list[0]
        if len(fish_list)>1:
            for fish in fish_list:
                if fish[0]<fish_to_eat[0]:
                    fish_to_eat=fish
                elif fish[0] == fish_to_eat[0]:
                    if fish[1]<fish_to_eat[1]:
                        fish_to_eat = fish
                        
        Under_water[shark_pos[0]][shark_pos[1]]=0    
        time+=move_cnt
        shark_pos = fish_to_eat
        Under_water[shark_pos[0]][shark_pos[1]]=9
        ate_fish+=1
        if ate_fish == shark_size:
            ate_fish=0
            shark_size+=1

# for row in Under_water:
#    print(row)
#print(f'fish list = {fish_list}')
#print(f'size={shark_size}, time = {time} , ate = {ate_fish}')
#print('---------------------------')
