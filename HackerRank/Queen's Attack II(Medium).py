#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the queensAttack function below.
def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles=set([tuple(ele) for ele in obstacles])
    dx=[1,1,0,-1,-1,-1,0,1]
    dy=[0,1,1,1,0,-1,-1,-1]
    
    squares=0
    for i in range(8):
        nx,ny=r_q+dx[i],c_q+dy[i]
        while ((nx,ny) not in obstacles) and (0<=nx<n) and (0<=ny<n):
            squares+=1
            nx+=dx[i]
            ny+=dy[i]
        print(i,squares)
    return squares
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    r_qC_q = input().split()

    r_q = int(r_qC_q[0])-1

    c_q = int(r_qC_q[1])-1

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(lambda x:int(x)-1, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
