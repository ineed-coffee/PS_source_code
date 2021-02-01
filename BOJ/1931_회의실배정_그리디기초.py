from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(100000)
 
input = stdin.readline
N = int(input())
Dict={}
for _ in range(N):
    s,e=map(int,input().split())
    try:
        Dict[e].append(s)
    except KeyError:
        Dict[e]=[s]

Meetings=[]
for endtime in sorted(Dict.keys()):
    meets = sorted(Dict[endtime])
    for m in meets:
        Meetings.append([m,endtime])

endtime=-1
Ans=0
for m in range(len(Meetings)):
    if Meetings[m][0]>=endtime:
        Ans+=1
        endtime=Meetings[m][1]
print(Ans)

