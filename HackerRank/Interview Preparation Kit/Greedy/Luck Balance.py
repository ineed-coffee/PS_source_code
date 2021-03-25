#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the luckBalance function below.
def luckBalance(k, contests):
    contests.sort(key=lambda x : (-x[1],x[0]))
    luck=0
    while contests:
        cur_luck,cur_imp=contests.pop()
        if not cur_imp:
            luck+=cur_luck
        elif k:
            luck+=cur_luck
            k-=1
        else:
            luck-=cur_luck
    return luck

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    contests = []

    for _ in range(n):
        contests.append(list(map(int, input().rstrip().split())))

    result = luckBalance(k, contests)

    fptr.write(str(result) + '\n')

    fptr.close()
