#!/bin/python3

import math
import os
import random
import re
import sys
from collections import defaultdict

# Complete the missingNumbers function below.
def missingNumbers(arr, brr):
    b_cnt = defaultdict(int)
    ret=[]
    for num in brr:
        b_cnt[num]+=1
    for num in arr:
        b_cnt[num]-=1
    for k,v in b_cnt.items():
        if v>0:
            ret.append(k)
    ret.sort()
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    m = int(input())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
