from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)


def move(gear_num,direction):
    global Moved
    
    Moved[gear_num]=True
    
    if gear_num-1>0 and gear[gear_num][6]-gear[gear_num-1][2] and not Moved[gear_num-1]:
        move(gear_num-1,-direction)

    if gear_num+1<5 and gear[gear_num][2]-gear[gear_num+1][6] and not Moved[gear_num+1]:
        move(gear_num+1,-direction)

    if direction == 1:
        gear[gear_num].appendleft(gear[gear_num].pop())

    elif direction == -1:
        gear[gear_num].append(gear[gear_num].popleft())

    return


input = stdin.readline

gear = [[0]*8]+[deque(list(map(int,list(input().strip())))) for _ in range(4)]

K = int(input())

commands = [list(map(int,input().split())) for _ in range(K)]

for com in commands:

    Moved=[False]*5

    move(com[0],com[1])

Ans=0
for g in range(1,5):
    Ans = Ans + (2**(g-1))*gear[g][0]

print(Ans)
