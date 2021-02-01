from sys import *
#from collections import deque
#from itertools import combinations
#setrecursionlimit(10000)

input = stdin.readline

N = int(input())

Attendence = list(map(int,input().split()))

B,C = map(int,input().split())

for i in range(N):

    if Attendence[i]-B > 0:
        if (Attendence[i]-B)%C == 0:
            Attendence[i] = (Attendence[i]-B)//C + 1
        else :
            Attendence[i] = (Attendence[i]-B)//C + 2
    else:
        Attendence[i]=1

print(sum(Attendence))

