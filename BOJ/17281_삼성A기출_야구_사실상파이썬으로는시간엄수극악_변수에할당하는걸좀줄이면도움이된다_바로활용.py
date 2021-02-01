#from sys import *
from sys import stdin
#from collections import deque
#from itertools import *
from itertools import permutations
#from copy import *
#setrecursionlimit(10000)


#--------------------------------------------------------------

#input = stdin.readline
#N = int(input())
#Result = [[*map(int,input().split())] for _ in range(N)]
N = int(stdin.readline())
Result = [[*map(int,stdin.readline().split())] for _ in range(N)]
#Orders = permutations(range(1,9))
Ans=0

for o in permutations(range(1,9)):
#    order = list(o)
    order = list(o[:3])+[0]+list(o[3:])
    idx=0
    Total_score=0
    for round_ in Result:

#        Base = deque([-1,-1,-1,-1])
        b1,b2,b3 = 0,0,0
        Out=0

        while Out <3:

            player = order[idx]
#            perform = Result[round][player]

            if not round_[player]:
                Out+=1
                idx=((idx+1)%9)
                continue
            else:
                if round_[player]==1:
                    Total_score+=b3
                    b1,b2,b3 = 1,b1,b2
                elif round_[player]==2:
                    Total_score+=(b2+b3)
                    b1,b2,b3 = 0,1,b1
                elif round_[player]==3:
                    Total_score+=(b1+b2+b3)
                    b1,b2,b3 = 0,0,1
                elif round_[player]==4:
                    Total_score+=(1+b1+b2+b3)
                    b1,b2,b3 = 0,0,0
                
                idx=((idx+1)%9)

    Ans = max(Total_score,Ans)

print(Ans)
