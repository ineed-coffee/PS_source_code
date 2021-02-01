from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def split_group(n):
    que = deque([[0,0,[]]])
    return_list=[]

    while que:
        c_idx,c_n,c_group = que.popleft()

        if c_n == n:
            return_list.append(c_group)
            continue
        
        for i in range(c_idx+1,N+1):
            que.append([i,c_n+1,c_group+[i]])

    return return_list

def bfs(group):
    start = group[0]
    que = deque([start])
    population=0
    Connect_dict={}
    for g in group:
        if g ==start:
            Connect_dict[g]=True
        else:
            Connect_dict[g]=False
        population+=People[g]
            
    while que:
        c_node = que.popleft()        
        for n_node in Adj_dict[c_node]:
            if n_node in group and not Connect_dict[n_node]:
                Connect_dict[n_node]=True
                que.append(n_node)

    if False in Connect_dict.values():
        return 0

    return population

#--------------------------------------------------------------

input = stdin.readline
N=int(input())
People = [0]+[*map(int,input().split())] 

Adj_dict={}
isolated=0
for i in range(1,N+1):
    info= [*map(int,input().split())]
    if not info[0]:
        isolated+=1
    Adj_dict[i]=info[1:]

Ans=-1

if isolated==1:

    for k,v in Adj_dict.items():
        if not v:
            group_a=k
            p_a = People[k]
            break
    group_b = list(range(1,N+1))
    group_b.remove(group_a)
    p_b = bfs(group_b)
    if p_b:
        Ans = abs(p_b-p_a)
    else:
        pass
elif isolated>1:
    if N==2:
        Ans = abs(People[1]-People[2])
    else:
        pass
else:
    for num in range(1,N//2+1):
        comb = split_group(num)

        for c in comb:
            group_a = c
            group_b = list(set(range(1,N+1))-set(c))
            p_a,p_b = bfs(group_a),bfs(group_b)
            if p_a and p_b:
                Ans = min(Ans,abs(p_a-p_b)) if Ans!=-1 else abs(p_a-p_b) 
                    
print(Ans)
