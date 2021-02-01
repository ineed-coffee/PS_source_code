from sys import *
from collections import deque
#from itertools import combinations
from copy import *
#setrecursionlimit(10000)

def move(map_info,d,r,b):
    
    delta = [dx[d],dy[d]]
    [red_x,red_y] = r
    [blue_x,blue_y] = b
    red_done,blue_done = False,False
    while not red_done or not blue_done :
        if not red_done:
            n_rx,n_ry = red_x+delta[0],red_y+delta[1]

            if (0<n_rx<N-1) and (0<n_ry<M-1):
                if map_info[n_rx][n_ry]=='.':
                    map_info[n_rx][n_ry]='R'
                    map_info[red_x][red_y]='.'
                    red_x,red_y=n_rx,n_ry
                elif map_info[n_rx][n_ry]=='O':
                    map_info[red_x][red_y]='.'
                    red_x,red_y=n_rx,n_ry
                    red_done=True
                elif map_info[n_rx][n_ry]=='#':
                    red_done=True
                elif map_info[n_rx][n_ry]=='B' and blue_done:
                    red_done=True
            else:
                red_done=True

        if not blue_done:
            n_bx,n_by = blue_x+delta[0],blue_y+delta[1]
            
            if (0<n_bx<N-1) and (0<n_by<M-1):
                if map_info[n_bx][n_by]=='.':
                    map_info[n_bx][n_by]='B'
                    map_info[blue_x][blue_y]='.'
                    blue_x,blue_y=n_bx,n_by
                elif map_info[n_bx][n_by]=='O':
                    map_info[blue_x][blue_y]='.'
                    blue_x,blue_y=n_bx,n_by
                    blue_done=True
                elif map_info[n_bx][n_by]=='#':
                    blue_done=True
                elif map_info[n_bx][n_by]=='R' and red_done:
                    blue_done=True
            else:
                blue_done=True

    return [map_info,[red_x,red_y],[blue_x,blue_y]]



def bfs(matrix,r,b):

    global Ans

    que = deque([[0,matrix,r,b,-1]])
    while que :

        size = len(que)
        for i in range(size):
            [trial,cur_board,c_red,c_blue,prev_dir] = que.popleft()

            if trial >= 10:
                Ans= -1
                return
            
            for direction in range(4):
                if direction!= prev_dir:
                    cop = deepcopy(cur_board)
                    [next_board,n_red,n_blue] = move(cop,direction,c_red,c_blue)
                    if cur_board != next_board:
                        if n_red == Hole and n_blue != Hole:
                            Ans = trial+1
                            return
                        elif n_blue != Hole:
                            que.append([trial+1,next_board,n_red,n_blue,direction])



input = stdin.readline

dx = [0,-1,0,1]
dy = [1,0,-1,0]
N,M = map(int,input().split())
board = []
for i in range(N):
    line = list(input().strip())
    for j in range(M):
        if line[j] == 'R':
            red = [i,j]
        elif line[j] == 'B':
            blue = [i,j]
        elif line[j] == 'O':
            Hole = [i,j]
    board.append(line)
    
Ans = -1

bfs(board,red,blue)

print(Ans)
