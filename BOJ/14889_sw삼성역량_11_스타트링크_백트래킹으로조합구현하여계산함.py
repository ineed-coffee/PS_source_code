from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)


def calculate(comp):
    global min_diff

    team1 = comp[:]
    team2 = list(set(range(N)) - set(team1))
    t1_score=0
    t2_score=0
    
    for i in range(len(team1)-1):
        for j in range(i+1,len(team1)):
            t1_score+=Potential[team1[i]][team1[j]]
            t1_score+=Potential[team1[j]][team1[i]]
            t2_score+=Potential[team2[i]][team2[j]]
            t2_score+=Potential[team2[j]][team2[i]]

    min_diff = min(min_diff, abs(t1_score-t2_score))

    return


def split_team(group,cnt,idx):
    global picked
    
    if cnt == N/2:
        calculate(group)
        return

    for i in range(idx+1,N):
        if not picked[i]:
            group.append(i)
            picked[i]=True
            split_team(group,cnt+1,i)
            group.pop()
            picked[i]=False
            if not group:
                return
    
    

input = stdin.readline

N= int(input())
Potential = [list(map(int,input().split())) for _ in range(N)]
min_diff = 10**9
picked= [False]*(N)
split_team([],0,-1)
print(min_diff)
