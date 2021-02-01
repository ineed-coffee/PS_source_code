from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

def spring():
    global Ans
    
    dead ={}

    for key in tree_info.keys():

        if not tree_info[key]:
            #del tree_info[key]
            continue
        x,y = key
        dead[key]=[]
        flag = False
        split=-1
        for idx in range(len(tree_info[key])-1,-1,-1):
            age = tree_info[key][idx]
            if not flag:
                if Ground[x][y] >= age :
                    Ground[x][y]-=age
                    tree_info[key][idx]+=1
                    if tree_info[key][idx] % 5 == 0:
                        global spread

                        try:
                            spread[key]+=1
                        except KeyError:
                            spread[key]=1
                else:
                    split=idx
                    flag=True
                    dead[key].append(age//2)
                    Ans-=1

            else:
                dead[key].append(age//2)
                Ans-=1
   
        tree_info[key]=tree_info[key][split+1:] if split+1<=len(tree_info[key])-1 else []

    return dead


def summer(dead):

    for pos in dead.keys():

        for i in range(len(dead[pos])):

            Ground[pos[0]][pos[1]]+=dead[pos][i]

    return
        

def fall(spread_dict):
    global Ans

    for key in spread_dict.keys():
        x,y = key
        
        for d in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]:
            nx,ny = x+d[0], y+d[1]
            if (0<nx<=N) and (0<ny<=N):
                Ans += spread_dict[key]
                for num in range(spread_dict[key]):
                    try:
                        tree_info[(nx,ny)].append(1)
                    except KeyError:
                        tree_info[(nx,ny)] = [1]

    return



def winter():
    global Ground,Add_nut

    for i in range(1,N+1):
        for j in range(1,N+1):
            Ground[i][j]+=Add_nut[i][j]

    return


def q_sort(part):

    if len(part)<=1:
        return part

    r_part,l_part = [],[]
    piv = part[0]

    for i in range(len(part)):

        if part[i]< piv:
            r_part.append(part[i])
        else :
            l_part.append(part[i])

    l_part = q_sort(l_part)
    r_part = q_sort(r_part)
    return l_part+[piv]+r_part


def age_sorting(info_dict):

    for key in info_dict.keys():
        info_dict[key] = q_sort(info_dict[key])



input = stdin.readline
dx = [0,1,0,-1]
dy = [1,0,-1,0]
N,M,K = map(int,input().split())                        
Add_nut =[[0]*(N+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]
Ground = [[5]*(N+1) for _ in range(N+1)]

tree_info ={}
for _ in range(M):

    tree_x,tree_y,tree_age = map(int,input().split())

    try :
        tree_info[(tree_x,tree_y)].append(tree_age)
    except KeyError:
        tree_info[(tree_x,tree_y)] = [tree_age]
        

Ans =M

for grow in range(K):   
    spread = {}
    dead_tree = spring()
    summer(dead_tree)
    fall(spread)
    winter()
    if not Ans:break

print(Ans)

'''
age_sorting(tree_info)
for i in range(1,N+1):
    print(Ground[i][1:])
print(tree_info)
'''
