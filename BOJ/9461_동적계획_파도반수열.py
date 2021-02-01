from sys import *

test_case = int(input())

Case=[int(input()) for _ in range(test_case)]

Max = max(Case)
Out=[0]*Max

for i in range(Max):
    if i<3:
        Out[i]=1
    elif i<5:
        Out[i]=2
    else:
        Out[i]=Out[i-1]+Out[i-5]

for case in Case:
    print(Out[case-1])
