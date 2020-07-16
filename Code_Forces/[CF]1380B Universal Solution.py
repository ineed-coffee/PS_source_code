from sys import *

input = stdin.readline

T= int(input())

for case in  range(T):
    Combs = list(input().rstrip())
    L = len(Combs)
    r,s,p=0,0,0
    for i in Combs:
        if i=='R':
            p+=1
        elif i=='S':
            r+=1
        elif i=='P':
            s+=1

    if p == max([r,s,p]):
        Ans = 'P'*L
    elif r == max([r,s,p]):
        Ans = 'R'*L
    elif s == max([r,s,p]):
        Ans = 'S'*L

    print(Ans)
