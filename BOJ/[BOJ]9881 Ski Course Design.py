from sys import *

input = stdin.readline

N = int(input())
hills = [int(input()) for _ in range(N)]
hills.sort()
cost=0
if hills[-1]-hills[0]>17:    
    start=hills[0]  
    end=hills[-1]-16
    for h in range(start,end):
        c_h=0
        for i in range(N):
            if hills[i]<h:
                c_h+=(h-hills[i])**2
            elif hills[i]>h+17:
                c_h+=(hills[i]-(h+17))**2
        cost = c_h if not cost else min(cost,c_h)

print(cost)
