from sys import stdin

input = stdin.readline

T = int(input())

for case in range(T):
    n = int(input())
    perm = [*map(int,input().split())]

    flag=False
    for i in range(1,n-1):
        if perm[i-1]<perm[i] and perm[i]>perm[i+1]:
            flag=True
            break
    if flag:
        print('YES')
        print(i,i+1,i+2)
    else:
        print('NO')
