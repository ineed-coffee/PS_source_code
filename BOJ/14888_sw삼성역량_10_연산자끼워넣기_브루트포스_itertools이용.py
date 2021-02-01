from sys import *
#from collections import deque
from itertools import *
#from copy import *
#setrecursionlimit(10000)


def Calculate(comb):
    global max_val,min_val
    
    Out = A[0]

    for i in range(N-1):

        if comb[i] == 0:

            Out += A[i+1]

        elif comb[i] == 1:

            Out -= A[i+1]

        elif comb[i] == 2:

            Out = Out*A[i+1]

        elif comb[i] == 3:

            if Out >=0:
                Out = Out//A[i+1]
            else:
                Out = -((-Out)//A[i+1])
    max_val = max(Out,max_val)
    min_val = min(Out,min_val)
    return
        

input = stdin.readline

N= int(input())
A = list(map(int,input().split()))
Symbols = list(map(int,input().split()))
Arithmetic = []
for idx,num in enumerate(Symbols):
    for sym in range(num):
        Arithmetic.append(idx)
        
Arrange = permutations(Arithmetic,N-1)

Arrange = list(set(Arrange))

max_val = -(10**9)
min_val = 10**9

for comb in Arrange:
    Calculate(comb)

print(max_val)
print(min_val)
