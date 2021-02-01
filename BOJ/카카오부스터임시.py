from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def Game(A,B,X):
    global Visited,Result
    Visited[A]=True

    que = deque([[A,X,False,True]])

    while que:

        c_pos, c_health, can_boost, is_cp = que.popleft()

        if c_pos == B:
            Result = 'YES'
            return

        if is_cp and not can_boost:
            que.append([c_pos,c_health,True,True])

        if can_boost:

            if is_cp:

                for cp in Checkpoints:
                    if c_pos[0]==cp[0] and c_pos[1]!=cp[1]:
                        que.
                        
            else:

def Game(current_pos,final,current_health,can_boost,is_cp):
    global Result,Visited

    if not can_boost and is_cp:
        Game(current_pos,final,current_health,True,is_cp)
        return

    if current_pos == final:
        Result='YES'
        return

    if is_cp:

        for i in range(len(Checkpoints)):
            if current_pos[0]==Checkpoints[i][0] and current_pos[1]!=Checkpoints[i][1]:
                Visited[i]=True
                Game(Checkpoints[i],final,current_health,False,True)
                Visited[i]=False
            elif current_pos[1]==Checkpoints[i][1] and current_pos[0]!=Checkpoints[i][0]:
                Visited[i]=True
                Game(Checkpoints[i],final,current_health,False,True)
                Visited[i]=False

        for d in [[-1,0],]

    else:
    
        

#--------------------------------------------------------------

input = stdin.readline
N,Q = map(int,input())

Checkpoints = []

for _ in range(N):
    xy = list(map(int,input().split()))
    Checkpoints.append(xy)

for case in range(Q):

    A,B,X=map(int,input().split())

    Visited=[False]*N

    Result='NO'

    Game(Checkpoints[A],Checkpoints[B],X,False,True)

    print(Result)
