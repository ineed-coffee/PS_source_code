from sys import *

input = stdin.readline

T = int(input())
for case in range(T):
    n = int(input())
    Arr = [*map(int,input().split())]
    if Arr[0]<Arr[-1]:
        print('YES')
    else:
        print('NO')
