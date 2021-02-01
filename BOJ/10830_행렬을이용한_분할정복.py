from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)

def Get_square(times):

    if times==1:
        return_list=A[:]
        for i in range(N):
            for j in range(N):
                return_list[i][j]%=1000
        return return_list

    if not times%2:
        before=Get_square(times//2)
        return_list=Dot(before,before)
        for i in range(N):
            for j in range(N):
                return_list[i][j]%=1000
        return return_list

    else:
        before=Get_square(times//2)
        return_list=Dot(before,Dot(before,A))
        for i in range(N):
            for j in range(N):
                return_list[i][j]%=1000
        return return_list

def Dot(a,b):

    b_T=[*map(list,zip(*b[:]))]
    return_mat=[[0]*N for _ in range(N)]
    for n in range(N):
        for k in range(N):
            num=0
            for m in range(N):
                num+=a[n][m]*b_T[k][m]
            return_mat[n][k]=num
    return return_mat

input = stdin.readline
N,B=map(int,input().split())
A=[[*map(int,input().split())] for _ in range(N)]
Ans=Get_square(B)
for row in Ans:
    print(*row)
