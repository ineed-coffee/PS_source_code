from sys import *
from collections import deque
#from itertools import *
#from itertools import permutations
from copy import *
#setrecursionlimit(10000)

def back_track(depth,idx,arrows):
    global Placed
    if depth==3:
        Game(arrows)
        return

    for i in range(idx,M):
        if not Placed[i]:
            Placed[i]=True
            back_track(depth+1,i,arrows+[i])
            Placed[i]=False


def Game(index_list):
    global Ans,test
    
    tmp_board = deque(deepcopy(Board))
    tmp_cnt = Enemy
    destroyed=0
    up = max(N-D,0)
    while tmp_cnt>0:
    #---------------------------------------------------------------------
        target=[]
        for k in index_list:
            target_cand=[]

            if tmp_board[N-1][k]:
                target_cand.append([N-1,k])                # find targets_1: if '1' right above 
            else:
                que = deque([[N-1,k]])
                Flag=False
                Visited=[False]*(N*M)
                Visited[M*(N-1)+k]=True
                dist=1
                while dist<D:                              # find targets_2: bfs , till dist<D
                    dist+=1
                    L = len(que)
                    
                    for l in range(L):
                        cx,cy = que.popleft()
                        for d in [[0,1],[-1,0],[0,-1]]:
                            nx,ny=cx+d[0],cy+d[1]                       
                            if not((0<=nx<N)and(0<=ny<M)):
                                continue
                            if not Visited[M*nx+ny]:
                                Visited[M*nx+ny]=True
                                if tmp_board[nx][ny]:
                                    target_cand.append([nx,ny])
                                    if not Flag:
                                        Flag=True
                                else:
                                    que.append([nx,ny])

                    if Flag:
                        break
                    
            if not target_cand:
                continue
            left=target_cand[0]
            for t in target_cand:
                if t[1]<left[1]:
                    left = t
            target.append(left)
    #---------------------------------------------------------------------
        for t in target:
            if tmp_board[t[0]][t[1]]:
                tmp_board[t[0]][t[1]]=0                                    # destroy targets       
                destroyed+=1
                tmp_cnt-=1
    #---------------------------------------------------------------------         
        endline = tmp_board[-1]
        tmp_cnt-=endline.count(1)
        tmp_board.pop()                                                    # enemy move
        tmp_board.appendleft([0]*M)

    #---------------------------------------------------------------------

    Ans = max(Ans,destroyed)
    return

            

#-------------------------------------------------------------------------

input = stdin.readline
N,M,D = map(int,input().split())                                       
Board=[]
Enemy = 0
for i in range(N):
    line = [*map(int,input().split())]                                     # Input, Param set
    Enemy+=line.count(1)
    Board.append(line)
    
Ans=0
#-------------------------------------------------------------------------
Placed=[False]*M 
back_track(0,0,[])                                                         # Make combinations using back-tracking
#Game([0,1,2])
#-------------------------------------------------------------------------
print(Ans)
