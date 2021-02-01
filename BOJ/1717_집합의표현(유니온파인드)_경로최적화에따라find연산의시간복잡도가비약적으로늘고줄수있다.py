from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

def find_head(node):

    if head[node]==node:
        return node
    head[node]=find_head(head[node])
    return head[node]

def union(command,a_node,b_node):
    head_a = find_head(a_node)
    head_b = find_head(b_node)

    if command == 0:
        if head_a == head_b:
            return
        else:
            head[head_b]=head_a
            
    elif command == 1:
        if head_a == head_b :
            print('YES')
        else:
            print('NO')

input = stdin.readline
n,m = map(int,input().split())
commands = [[*map(int,input().split())] for _ in range(m)]
head = [i for i in range(n+1)]

for com in commands:
    union(*com)
