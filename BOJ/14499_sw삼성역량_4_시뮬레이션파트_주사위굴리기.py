from sys import *
from collections import deque
#from itertools import combinations
#setrecursionlimit(10000)


def dice_move(move_dir):
    global dice_x,dice_y,vertical,horizontal

    if (0<=dice_x+dx[move_dir]<N) and (0<=dice_y+dy[move_dir]<M):
        dice_x+=dx[move_dir]
        dice_y+=dy[move_dir]

        if move_dir == 1:
            horizontal.appendleft(horizontal.pop())
            vertical[1]=horizontal[1]
            if Map_info[dice_x][dice_y]:
                horizontal[-1] = Map_info[dice_x][dice_y]
                Map_info[dice_x][dice_y]=0
            else:
                Map_info[dice_x][dice_y]=horizontal[-1]
            vertical[-1] = horizontal[-1]

        elif move_dir == 2:
            horizontal.append(horizontal.popleft())
            vertical[1]=horizontal[1]
            if Map_info[dice_x][dice_y]:
                horizontal[-1] = Map_info[dice_x][dice_y]
                Map_info[dice_x][dice_y]=0
            else:
                Map_info[dice_x][dice_y]=horizontal[-1]
            vertical[-1] = horizontal[-1]

        elif move_dir == 3:
            vertical.append(vertical.popleft())
            horizontal[1]=vertical[1]
            if Map_info[dice_x][dice_y]:
                vertical[-1] = Map_info[dice_x][dice_y]
                Map_info[dice_x][dice_y]=0
            else:
                Map_info[dice_x][dice_y]=vertical[-1]
            horizontal[-1] = vertical[-1]

        elif move_dir == 4:
            vertical.appendleft(vertical.pop())
            horizontal[1]=vertical[1]
            if Map_info[dice_x][dice_y]:
                vertical[-1] = Map_info[dice_x][dice_y]
                Map_info[dice_x][dice_y]=0
            else:
                Map_info[dice_x][dice_y]=vertical[-1]
            horizontal[-1] = vertical[-1]

        print(vertical[1])
        return

dx = [0,0,0,-1,1]
dy = [0,1,-1,0,0]
vertical = deque([0,0,0,0])
horizontal = deque([0,0,0,0])

input = stdin.readline

N,M,dice_x,dice_y,commands= map(int,input().split())

Map_info = [list(map(int,input().split())) for _ in range(N)]

command = list(map(int,input().split()))


for com in command:
    dice_move(com)

