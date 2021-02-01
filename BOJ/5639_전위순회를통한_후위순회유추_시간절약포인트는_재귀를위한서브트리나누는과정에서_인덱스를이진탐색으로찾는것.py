from sys import *
from collections import deque
#from itertools import *
from copy import *
#setrecursionlimit(300000)
from heapq import *

def get_post(s_idx,e_idx):

    if not (s_idx<e_idx):
        return
    
    right_fg=False
    right=0
    root=pre_order[s_idx]

    low = s_idx+1
    high = e_idx-1
    mid=(low+high)//2
    while low<=high:
        mid = (low+high)//2
        if pre_order[mid]>root:
            high=mid-1
        else:
            low=mid+1

    if pre_order[mid]>root:
        right_fg=True
        right=mid
    else:
        if mid+1==e_idx:
            pass
        else:
            right_fg=True
            right=mid+1
            
    if right_fg:
        get_post(s_idx+1,right)
        get_post(right,e_idx)
    else:
        get_post(s_idx+1,e_idx)

    print(root)
    return
            

input = stdin.readline
pre_order = [int(input()) for i in range(9)]
get_post(0,len(pre_order))



'''
pre_order=[]
while True:
    try:
        node=int(input())
        pre_order.append(node)
    except:
        get_post(0,len(pre_order))
        break
'''
