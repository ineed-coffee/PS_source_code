from sys import *
#from collections import deque
#from itertools import combinations
#from copy import *
#setrecursionlimit(10000)

def Clean(bot_x,bot_y,direction):

    global Ans,board
    while True:
        
        if board[bot_x][bot_y]!=2:
            board[bot_x][bot_y]=2
            Ans+=1

        cleaned=False
        for i in range(1,5):
            if not board[bot_x+dx[(direction-i)%4]][bot_y+dy[(direction-i)%4]]:
                bot_x += dx[(direction-i)%4]
                bot_y += dy[(direction-i)%4]
                direction = (direction-i)%4
                cleaned=True
                break

        if cleaned:
            continue

        if board[bot_x+dx[(direction-2)%4]][bot_y+dy[(direction-2)%4]] == 2:
            bot_x += dx[(direction-2)%4]
            bot_y += dy[(direction-2)%4]      
            continue

        if board[bot_x+dx[(direction-2)%4]][bot_y+dy[(direction-2)%4]] == 1:
            print(Ans)
            return
        

input = stdin.readline

dx = [-1,0,1,0]
dy = [0,1,0,-1]
N,M = map(int,input().split())
r,c,d = map(int,input().split())
board = [list(map(int,input().split())) for _ in range(N)]

Ans=0
Clean(r,c,d)
