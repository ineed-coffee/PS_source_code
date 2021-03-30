#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the getMinimumCost function below.
def getMinimumCost(k, c):
    L=len(c)
    c.sort(reverse=True)
    mul,check=1,0
    ret=0
    for i in range(L):
        ret+=c[i%L]*mul
        check+=1
        if check==k:
            mul+=1
            check=0
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    minimumCost = getMinimumCost(k, c)

    fptr.write(str(minimumCost) + '\n')

    fptr.close()
