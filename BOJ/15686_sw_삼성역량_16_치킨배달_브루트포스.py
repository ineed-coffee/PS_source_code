from sys import *
#from collections import deque
from itertools import *
#from copy import *
#setrecursionlimit(10000)

def chicken_distance(group):

    distance=0
    
    for h_x,h_y in House:
        sub_dist=1000
        for c_x,c_y in group:
            sub_dist = min(sub_dist , abs(h_x-c_x)+abs(h_y-c_y))
        distance+=sub_dist
        
    return distance


input = stdin.readline

N,M = map(int,input().split())

House,Chicken=[],[]

for i in range(N):
    row = list(map(int,input().split())) 
    for j in range(N):
        if row[j]==1:
            House.append([i,j])
        elif row[j]==2:
            Chicken.append([i,j])
        
Ans = maxsize


comb = combinations(Chicken,M)

for choice in comb:

    comp_distance = chicken_distance(list(choice))
    
    Ans = min(Ans,comp_distance)


print(Ans)
