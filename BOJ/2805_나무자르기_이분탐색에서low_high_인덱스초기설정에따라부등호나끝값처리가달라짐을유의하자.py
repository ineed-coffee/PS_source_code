from sys import *
#from collections import deque
#from itertools import *
#from copy import *
#setrecursionlimit(300000)

def cut_it(sub):
    return_val=0
    for tree in Trees:
        return_val+=max(0,tree-sub)

    if return_val>=M:
        return True

    return False

input = stdin.readline
N,M=map(int,input().split())
Trees=[*map(int,input().split())]
ordered_Trees=[*set(Trees)]
ordered_Trees.sort()
O=len(ordered_Trees)

init_low,init_high=0,O-1
while init_low<=init_high:
    init_mid=(init_low+init_high)//2
    if cut_it(ordered_Trees[init_mid]):
        init_low=init_mid+1
    else:
        init_high=init_mid-1

if init_mid==init_high:
    main_low=ordered_Trees[init_mid]
    if init_high==O-1:
        main_high=ordered_Trees[-1]
    else:
        main_high=ordered_Trees[init_mid+1]
elif init_mid==init_low:
    main_high=ordered_Trees[init_mid]
    if not init_low:
        main_low=0
    else:
        main_low=ordered_Trees[init_mid-1]


while main_low<=main_high:
    main_mid=(main_low+main_high)//2
    if cut_it(main_mid):
        main_low=main_mid+1
    else:
        main_high=main_mid-1

if main_mid==main_high:
    print(main_mid)
else:
    print(main_mid-1)

'''
4 10
1 4 5 7
2

6 6
5 5 4 4 1 1
3

2 3
2 2
0

4 6
6 6 6 6
4

4 8
2 2 2 2
0

2 7
1 7
0

4 10
2 3 4 5
1

3 1
1 2 2
1

1 1
1000000000
999999999

2 6
8 8
5

1 1
1
0

6 6
6 6 6 6 6 6
5

5 100
99 1 1 1 1
0

2 50
51 1

6 1
0 2 0 0 0 2
1

4 1
20 15 10 17
19
'''

