from sys import *
from collections import deque
from itertools import combinations
from copy import *
#setrecursionlimit(10000)


def solve(d,matrix):
    global Max_val
    
    if not d: # 좌
        for i in range(N):
            new = []
            valid=0
            for j in range(N):
                if matrix[i][j]:
                    if not valid:
                        if not new or matrix[i][j] != new[-1]:
                            new.append(matrix[i][j])
                        else:
                            new[-1]+=matrix[i][j]
                            Max_val = max(Max_val,new[-1])
                            valid=1
                    else:
                        new.append(matrix[i][j])
                        valid=0

            matrix[i]=new+[0]*(N-len(new))                  

    elif d==1: # 상                    
        for j in range(N):
            new = []
            valid=0
            for i in range(N):
                if matrix[i][j]:
                    if not valid:
                        if not new or matrix[i][j] != new[-1]:
                            new.append(matrix[i][j])
                        else:
                            new[-1]+=matrix[i][j]
                            Max_val = max(Max_val,new[-1])
                            valid=1
                    else:
                        new.append(matrix[i][j])
                        valid=0
                        
            new=new+[0]*(N-len(new))
            for k in range(N):
                matrix[k][j]=new[k]

    elif d==2: # 우
        for i in range(N):
            new = deque([])
            valid=0
            for j in reversed(range(N)):
                if matrix[i][j]:
                    if not valid:
                        if not new or matrix[i][j] != new[0]:
                            new.appendleft(matrix[i][j])
                        else:
                            new[0]+=matrix[i][j]
                            Max_val = max(Max_val,new[0])
                            valid=1
                    else:
                        new.appendleft(matrix[i][j])
                        valid=0

            matrix[i]=[0]*(N-len(new))+list(new)

    elif d==3: # 하
        for j in range(N):
            new = deque([])
            valid=0
            for i in reversed(range(N)):
                if matrix[i][j]:
                    if not valid:
                        if not new or matrix[i][j] != new[0]:
                            new.appendleft(matrix[i][j])
                        else:
                            new[0]+=matrix[i][j]
                            Max_val = max(Max_val,new[0])
                            valid=1
                    else:
                        new.appendleft(matrix[i][j])
                        valid=0

            new=[0]*(N-len(new))+list(new)
            for k in range(N):
                matrix[k][j]=new[k]


input = stdin.readline

N = int(input())
board = []
Max_val = 2

for _ in range(N):
    line = list(map(int,input().split()))
    Max_val = max(Max_val,*line)
    board.append(line)

move_choice = combinations(range(16),5)

for move in move_choice:
    copyboard = deepcopy(board)
    for direction in move:
        cur = direction%4
        solve(cur,copyboard)

print(min(Max_val,1024))
