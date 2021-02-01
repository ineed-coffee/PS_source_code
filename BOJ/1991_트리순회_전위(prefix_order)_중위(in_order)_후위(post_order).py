from sys import *
from collections import deque
#from itertools import *
from copy import *
#setrecursionlimit(300000)
from heapq import *

def Traversal(node,ty):
    ret_list = []
    if ty=='pre':
        ret_list.append(node)
    if adj_l[node][0]>=0:
        ret_list+=Traversal(adj_l[node][0],ty)
    if ty=='in':
        ret_list.append(node)
    if adj_l[node][1]>=0:
        ret_list+=Traversal(adj_l[node][1],ty)
    if ty=='post':
        ret_list.append(node)
    return ret_list

input = stdin.readline
N=int(input())
adj_l = [[] for _ in range(N)]
for n in range(N):
    parent,left,right = map(lambda x:ord(x)-ord('A'),input().split())
    adj_l[parent]=[left,right]

print(''.join([*map(lambda x:chr(x+65),Traversal(0,'pre'))]))
print(''.join([*map(lambda x:chr(x+65),Traversal(0,'in'))]))
print(''.join([*map(lambda x:chr(x+65),Traversal(0,'post'))]))

