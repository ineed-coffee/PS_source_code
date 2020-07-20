from sys import *
setrecursionlimit(10**6)


def make_good(string,cnt,piv):
    global Move
    L = len(string)

    if L==1:
        if string== chr(piv):
            Move = min(Move,cnt)
            return
        else:
            Move = min(Move,cnt+1)
            return

    mid = L//2
    l_cnt=0
    h_cnt=0
    for i in range(L):
        if string[i]!=chr(piv):
            if i<mid:
                l_cnt+=1
            else:
                h_cnt+=1
    make_good(string[mid:],cnt+l_cnt,piv+1)
    make_good(string[:mid],cnt+h_cnt,piv+1)
    

input = stdin.readline
t = int(input())
for case in range(t):
    n = int(input())
    s = input().rstrip()
    Move = n+1
    make_good(s,0,97)
    print(Move)
