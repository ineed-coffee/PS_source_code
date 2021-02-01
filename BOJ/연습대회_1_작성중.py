from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
from heapq import *

def G_fall(t,x,y):

    if t==1:
        cx,cy = 0,y
        while True:
            nx=cx+1
            if nx==6 or G_board[nx][cy]:
                G_board[cx][cy]=1
                    G_score(G_full_line)
            else:
                cx=nx
    
    elif t==2:
        pass
    elif t==3:
        pass


    if 1 in G_board[0]:
        G_board=[[0]*4,[0]*4]+G_board[:4]
    elif 1 in G_board[1]:
        G_board=[[0]*4]+G_board[:5]

def G_full_line():
    ret_list = []
    for i in range(4):
        if sum(G_board[i])==4:
            ret_list.append(i)
    return ret_list


def G_score(cand_list):
    global Score

    if not cand_list:
        return

    for idx in cand_list:
        Score+=1
        for i in range(4):
            if G_board[idx][i]==3:
                G_board[idx][i]=0
                if idx-1>=0 and G_board[idx-1][i]==3:
                    G_board[idx-1][i]=1
                elif idx+1<6 and G_board[idx+1][i]==3:
                    G_board[idx+1][i]=1
            else:
                G_board[idx][i]=0

    for i in range(4,-1,-1):
        for j in range(4):
            if G_board[i][j]==1:
                tmp=i
                while G_board[tmp+1][j]==0 :
                    G_board[tmp+1][j]==1
                    G_board[tmp][j]=0
                    tmp+=1
            elif G_board[i][j]==2 and j<3 and G_board[i][j+1]==2:
                tmp=i
                while G_board[tmp+1][j]==0 and G_board[tmp+1][j+1]==0:
                    G_board[tmp+1][j]==2
                    G_board[tmp][j]=0
                    tmp+=1
                G_board[tmp][j+1]=2
                
            elif G_board[i][j]==3 and i>=1 and G_board[][]:
                pass
                
    

    
#---------------------------------------------
input = stdin.readline
N = int(input())
G_board=[[0]*4 for _ in range(6)]
B_board=[[0]*4 for _ in range(6)]
G_cnt,B_cnt=0,0
Score=0

for n in range(N):
    t,x,y = map(int,input().split())
    G_fall(t,x,y)
    B_fall(t,x,y)
