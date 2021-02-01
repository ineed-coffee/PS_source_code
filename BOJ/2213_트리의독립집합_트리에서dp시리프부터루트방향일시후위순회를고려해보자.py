from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)
#from heapq import *

def make_tree(node):
    global parent
    p = parent[node]
    for ch in adj_list[node]:
        if ch!=p:
            parent[ch]=node
            make_tree(ch)
            dp_include[node]+=dp_exclude[ch]
            dp_exclude[node]+=max(dp_include[ch],dp_exclude[ch])

def get_set(node,con_before):
    global idp
    p=parent[node]

    if con_before:
        for ch in adj_list[node]:
            if ch!=p:
                get_set(ch,False)
    else:
        if dp_include[node]>dp_exclude[node]:
            idp.append(node)
            for ch in adj_list[node]:
                if ch!=p:
                    get_set(ch,True)
        else:
            for ch in adj_list[node]:
                if ch!=p:
                    get_set(ch,False)
    
input = stdin.readline
n = int(input())
Weights=[0]+[*map(int,input().split())]

adj_list = [[] for _ in range(n+1)]
for line in range(n-1):
    a,b = map(int,input().split())
    adj_list[a].append(b)
    adj_list[b].append(a)
    
parent=[0]*(n+1)
dp_include=Weights[:]
dp_exclude=[0]*(n+1)
root=1
make_tree(root)
print(max(dp_include[root],dp_exclude[root]))
idp = []
get_set(root,False)
idp.sort()
print(*idp)
'''
idp_set=[]
for i in range(1,n+1):
    if dp_exclude[i]>dp_include[i]:
        continue
    idp_set.append(i)
idp_set.sort()
print(*idp_set)
'''
