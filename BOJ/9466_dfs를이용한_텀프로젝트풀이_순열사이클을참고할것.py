from sys import *
from collections import deque
setrecursionlimit(100000)

def dfs_s(start,group):
    global picked
    
    picked[start]=1
    group.append(start)

    if not picked[choice[start]]:
        dfs_s(choice[start],group)
    else:
        if choice[start]==start:
            picked[start]=2
            group.pop()
            for i in group:
                picked[i]=-1
                
        elif picked[choice[start]]== -1 or picked[choice[start]]== 2:
            for i in group:
                picked[i]=-1
        
        elif picked[choice[start]]== 1:
            idx = group.index(choice[start])
            for i in range(len(group)):
                if i<idx:
                    picked[group[i]]=-1
                else:
                    picked[group[i]]=2

    return



test_case = int(input())

for case in range(test_case):
    n = int(stdin.readline())
    choice = [0]+list(map(int,stdin.readline().split()))
    picked=[0]*(n+1)
    for student in range(1,n+1):
        if not picked[student]:
            dfs_s(student,[])
    print(picked.count(-1))
