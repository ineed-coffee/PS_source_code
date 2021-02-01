from sys import *

Num_for1 = int(input())
Calc=[[0,0,0] for _ in range(Num_for1+1)]

for i in range(2,Num_for1+1):
    Calc[i][2]=min(Calc[i-1])+1

    Calc[i][0] = min(Calc[i//3])+1 if i%3==0 else i

    Calc[i][1] = min(Calc[i//2])+1 if i%2==0 else i








print(min(Calc[-1]))
