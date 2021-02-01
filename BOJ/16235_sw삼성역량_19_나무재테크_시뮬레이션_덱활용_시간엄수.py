from sys import *
from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

input = stdin.readline

N,M,K = map(int,input().split())                        
Add_nut =[[0]*(N+1)] + [[0]+list(map(int,input().split())) for _ in range(N)]
Ground = [[5]*(N+1) for _ in range(N+1)]

tree_info ={}
for _ in range(M):
    tree_x,tree_y,tree_age = map(int,input().split())
    tree_info[(tree_x,tree_y)] = deque([tree_age])
        

Ans =M

for grow in range(K):   
    spread = {}
#--------------------------------------------------    
    for key,ages in tree_info.items():

        if not ages:
            continue

        x,y = key
        from_dead = 0
        survived=deque([])
        flag = False
        split=-1
        while ages:
            age = ages.popleft()
            if not flag:
                if Ground[x][y]>=age:
                    Ground[x][y]-=age
                    survived.append(age+1)
                    if (age+1)%5==0:
                        try:
                            spread[key]+=1
                        except KeyError:
                            spread[key]=1
                else:
                    flag=True
                    from_dead+=age//2
                    Ans-=1
            else:
                from_dead+=age//2
                Ans-=1
                            
        tree_info[key]=survived
        Ground[x][y]+=from_dead

#--------------------------------------------------
    for center,quantity in spread.items():
        x,y = center
        
        for d in [(0,1),(1,0),(0,-1),(-1,0),(-1,-1),(1,1),(1,-1),(-1,1)]:
            nx,ny = x+d[0], y+d[1]
            if (0<nx<=N) and (0<ny<=N):
                Ans += quantity
                for _ in range(quantity):
                    try:
                        tree_info[(nx,ny)].appendleft(1)
                    except KeyError:
                        tree_info[(nx,ny)] = deque([1])

#--------------------------------------------------
    for i in range(1,N+1):
        for j in range(1,N+1):
            Ground[i][j]+=Add_nut[i][j]

#--------------------------------------------------
            
    if not Ans:break

print(Ans)

'''
age_sorting(tree_info)
for i in range(1,N+1):
    print(Ground[i][1:])
print(tree_info)
'''
