from sys import *

input = stdin.readline

T = int(input())
for case in range(T):
    n,m = map(int,input().split())
    Grid = []
    for i in range(n):
        Grid.append([*map(int,input().split())])

    corner = [[0,0],[0,m-1],[n-1,0],[n-1,m-1]] 
    flag=True
    for i in range(n):
        for j in range(m):
            if [i,j] in corner and Grid[i][j]>2:
                flag=False
                break
            elif (i in [0,n-1] or j in [0,m-1]) and Grid[i][j]>3:
                flag=False
                break
            elif Grid[i][j]>4:
                flag=False
                break
        if not flag:
            break

    if not flag:
        print('NO')
    else:
        print('YES')
        for i in range(n):
            for j in range(m):
                if [i,j] in corner:
                    print(2,end=' ')
                elif i in [0,n-1] or j in [0,m-1]:
                    print(3,end=' ')
                else:
                    print(4,end=' ')
            print()
