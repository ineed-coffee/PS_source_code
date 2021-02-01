from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def calc(visit):
    global Ans

    copied = equation[:]
    for v in range(N):
        if visit[v]:
            cal_num = eval(''.join(copied[v:v+3]))
            copied[v]='('
            copied[v+1]=str(cal_num)
            copied[v+2]=')'

    if copied[0]=='(':
        start = copied[1]
        i=3
    else:
        start=copied[0]
        i=1

    while True:

        if i>=N:
            Ans = max(int(start),Ans)
            return

        if copied[i+1]=='(':
            num = eval(start+copied[i]+copied[i+2])
            start = str(num)
            i+=4
        else:
            num = eval(start+copied[i]+copied[i+1])
            start = str(num)
            i+=2

    
def back_track(idx,u):

    u[idx]=True
    calc(u)

    if idx+4>=N-2:
        return
    for i in range(idx+4,N-2,2):
        if not u[i]:
            u[i]=True
            back_track(i,u)
            u[i]=False
    
#--------------------------------------------------------------

input = stdin.readline

N = int(input())

equation = list(input().strip())

if N<=3:
    Ans = eval(''.join(equation))
else:
    Ans = -(2**31)
    calc([False]*N)
    
    for i in range(0,N-2,2):
        Used = [False]*N
        back_track(i,Used)

print(Ans)
