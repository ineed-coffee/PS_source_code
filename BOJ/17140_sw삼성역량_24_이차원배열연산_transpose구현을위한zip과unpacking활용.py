from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(10000)

input = stdin.readline

R,C,K = map(int,input().split())

Matrix = [list(map(int,input().split())) for _ in range(3)]
Time = 0

while True:

    try :
        if Matrix[R-1][C-1]==K:
            break

    except IndexError :
        pass

    if Time >100:
        Time=-1
        break
#-------------------------------------------------
    is_R = True
    
    if len(Matrix) < len(Matrix[0]):
        Matrix = [list(x) for x in zip(*Matrix)]
        is_R=False

    max_L=0
    for r in range(len(Matrix)):

        tmp = Matrix[r][:]
        cnt_dict ={}
        sort_dict={}
        tmp2 = []
        for t in tmp:
            if t:
                try :
                    cnt_dict[t]+=1
                except KeyError:
                     cnt_dict[t]=1
        for num,cnt in cnt_dict.items():
            try :
                sort_dict[cnt].append(num)

            except KeyError:
                sort_dict[cnt]=[num]

        Key = list(sort_dict.keys())
        Key.sort()
        for k in Key:
            Sort = sort_dict[k]
            Sort.sort()
            for s in Sort:
                tmp2.append(s)
                tmp2.append(k)

        if len(tmp2)>100:
            tmp2 = tmp2[:100]
                
        Matrix[r] = tmp2
        max_L = max(max_L,len(tmp2))
        
    for row in Matrix:
        if len(row)<max_L:
            row+=[0]*(max_L-len(row))

    if not is_R:
        Matrix = [list(x) for x in zip(*Matrix)]

    Time+=1
#-------------------------------------------------
    
print(Time)


