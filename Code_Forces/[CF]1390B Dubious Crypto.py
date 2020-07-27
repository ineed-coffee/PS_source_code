from sys import stdin

input = stdin.readline

t = int(input())

for case in range(t):
    l,r,m = map(int,input().split())
    diff=r-l
    for i in range(l,r+1):
        Q=m//i
        R=m%i

        if Q and R<=diff:
            print(i,l+R,l)
            break
        elif (i-R)<=diff:
            print(i,r-(i-R),r)
            break
