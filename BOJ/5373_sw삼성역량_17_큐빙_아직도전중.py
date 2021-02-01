from sys import *
from collections import deque
#from itertools import *
from copy import *
#setrecursionlimit(10000)

def chicken_distance(group):


    return distance

Up = [['w']*3 for _ in range(3)]       #0
Down = [['y']*3 for _ in range(3)]     #1
Front = [['r']*3 for _ in range(3)]    #2
Back = [['o']*3 for _ in range(3)]     #3
Left = [['g']*3 for _ in range(3)]     #4
Right = [['b']*3 for _ in range(3)]    #5

command_store = {['U','+']:[0,0,[[2,0],[4,0],[3,0],[5,0]],
                 ['U','-']:[0,1,[[2,0],[5,0],[3,0],[4,0]],
                 ['D','+']:[1,0,[[2,2],[4,2],[3,2],[5,2]],
                 ['D','-']:[1,1,[[2,2],[5,2],[3,2],[4,2]],
                 ['F','+']:[2,0,[[0,2],[5,3],[1,0],[4,5]],
                 ['F','-']:[2,1,[[0,2],[4,5],[1,0],[5,3]],
                 ['B','+']:[3,0,[[],[],[],[]]],
                 ['B','-']:[3,1,[2,5,3,4]],
                 ['L','+']:[4,0,[2,5,3,4]],
                 ['L','-']:[4,1,[2,5,3,4]],
                 ['R','+']:[5,0,[2,5,3,4]],
                 ['R','-']:[5,1,[2,5,3,4]],
                            }
input = stdin.readline
test_case = int(input())

for case in range(test_case):
    n = int(input())
    commands =[]
    cube = deepcopy([Up,Down,Front,Back,Left,Right])
    for com in range(n):
        commands.append(input().strip().split())

    

