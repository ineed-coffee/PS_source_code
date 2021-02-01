from sys import *
#setrecursionlimit(10000)

from itertools import combinations


while True:

    case = list(map(int,stdin.readline().split()))
    if case[0] ==0:
        break
    k = case[0]
    S = case[1:]

    Combs = list(combinations(S,6))
    for c in Combs:
        print(*c)
    print()
