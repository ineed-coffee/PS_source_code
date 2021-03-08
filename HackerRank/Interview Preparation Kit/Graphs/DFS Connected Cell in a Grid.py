#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxRegion function below.
def maxRegion(grid,n,m):
    
    def dfs(start):
        nonlocal visited,size,n,m,grid
        
        visited[start[0]][start[1]]=True
        dx=[0,-1,-1,-1,0,1,1,1]
        dy=[1,1,0,-1,-1,-1,0,1]
        stack=[start]
        
        while stack:
            cx,cy=stack.pop()
            for i in range(8):
                nx,ny=cx+dx[i],cy+dy[i]
                if (0<=nx<n) and (0<=ny<m) and (not visited[nx][ny]) and (grid[nx][ny]):
                    visited[nx][ny]=True
                    stack.append((nx,ny))
                    size+=1
    
    visited=[[False]*m for _ in range(n)]
    max_size=0
    for i in range(n):
        for j in range(m):
            if (grid[i][j]) and (not visited[i][j]):
                size=1
                dfs((i,j))
                max_size=max(max_size,size)
                
    return max_size

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    m = int(input())

    grid = []

    for _ in range(n):
        grid.append(list(map(int, input().rstrip().split())))

    res = maxRegion(grid,n,m)

    fptr.write(str(res) + '\n')

    fptr.close()
