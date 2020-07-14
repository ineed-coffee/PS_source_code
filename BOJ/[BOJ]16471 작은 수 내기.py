from sys import *

input = stdin.readline

N = int(input())

Chall = [*map(int,input().split())]
Owner = [*map(int,input().split())]

if N==1:
    if Chall[0]<Owner[0]:
        print('Yes')
    else:
        print('No')
else:
    Chall.sort()
    Owner.sort()

    possible=True
    for i in range(N//2+1):
        if Chall[i]>=Owner[i+(N//2)]:
            possible =False
            break
    if possible:
        print('YES')
    else:
        print('NO')
