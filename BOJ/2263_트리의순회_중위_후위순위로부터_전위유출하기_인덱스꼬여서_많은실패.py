from sys import *
from collections import deque
#from itertools import *
from copy import *
#setrecursionlimit(300000)
from heapq import *


from sys import *
setrecursionlimit(200000)

def Get_pre_order(in_idx,post_idx):
    in_s,in_e = in_idx
    post_s,post_e = post_idx

    root = post_order[post_e-1]
    r_idx = idx_dict[root]
    diff = r_idx-in_s
    ret_list = [root]
    print(root,end=' ')
    if in_s<r_idx:
        Get_pre_order([in_s,r_idx],[post_s,post_s+diff])
    if r_idx+1<in_e:
        Get_pre_order([r_idx+1,in_e],[post_s+diff,post_e-1])
    return

input = stdin.readline
N=int(input())
in_order = [*map(int,input().split())]
post_order = [*map(int,input().split())]
idx_dict = {}
for idx,num in enumerate(in_order):
    idx_dict[num]=idx
Get_pre_order([0,N],[0,N])
