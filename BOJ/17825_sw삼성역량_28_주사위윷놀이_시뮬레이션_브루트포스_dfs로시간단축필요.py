from sys import *
#from collections import deque
from itertools import *
#from copy import *
#setrecursionlimit(10000)


#--------------------------------------------------------------

input = stdin.readline
Moves = list(map(int,input().split()))
Ans=0
Combs = product([1,2,3,4],repeat=10)

Board=[[0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,34,36,38],
       [10,13,16,19],
       [20,22,24],
       [30,28,27,26],
       [25,30,35,40]]

for order in Combs:
    
    Piece = {1:[0,0],2:[0,0],3:[0,0],4:[0,0]}
    Done = [False]*5
    Valid=True
    Score=0
    Placed = [[False]*20,
              [False]*4,
              [False]*3,
              [False]*4,
              [False]*4]

    for i in range(10):
        move = Moves[i]
        piece = order[i]
#--------------------------------------------------------------------------
        if Done[piece]:
            Valid=False                            # if trying to move fisnished piece
            break
#--------------------------------------------------------------------------        
        category,start_idx = Piece[piece]
        land_idx = start_idx+move

        if land_idx >=len(Board[category]):        

            if category == 4:
                Done[piece]=True
                Placed[category][start_idx]=False
                continue

            elif not category:
                if land_idx >=len(Board[category])+1:
                    Done[piece]=True
                    Placed[category][start_idx]=False
                    continue
                else:
                    if Placed[4][3]:
                        Valid=False
                        break
                    else:                                   # enter end route(25-30-35-40) or finished
                        Placed[category][start_idx]=False
                        Piece[piece]=[4,3]
                        Placed[4][3]=True
                        Score+=40
                        continue

            else :
                if land_idx >=len(Board[category])+4:
                    Done[piece]=True
                    Placed[category][start_idx]=False
                    continue
                else:
                    land_idx-=len(Board[category])
                    if Placed[4][land_idx]:
                        Valid=False
                        break
                    else:
                        Placed[category][start_idx]=False
                        if (0<category<4) and not start_idx:             
                            Placed[0][5*category]=False
                        Piece[piece]=[4,land_idx]
                        Placed[4][land_idx]=True
                        Score+=Board[4][land_idx]
                        continue

#--------------------------------------------------------------------------

        if Placed[category][land_idx]:
            Valid=False
            break

        if not Board[category][land_idx]%10 and not category:
            Placed[category][start_idx]=False
            Score+=Board[category][land_idx]
            new_category = Board[category][land_idx]//10          # Route change
            Piece[piece]=[new_category,0]
            Placed[new_category][0]=True
            Placed[0][5*new_category]=True

#--------------------------------------------------------------------------

        else:
            Placed[category][start_idx]=False
            if (0<category<4) and not start_idx:              # Normal move
                Placed[0][5*category]=False
            Score+=Board[category][land_idx]
            Piece[piece]=[category,land_idx]
            Placed[category][land_idx]=True
#--------------------------------------------------------------------------

    if Valid:
        Ans = max(Ans,Score)

#--------------------------------------------------------------------------

print(Ans)

        
