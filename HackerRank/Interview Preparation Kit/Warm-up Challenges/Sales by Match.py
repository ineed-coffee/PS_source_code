#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sockMerchant function below.
def sockMerchant(n, ar):
    from collections import defaultdict
    ret=0
    color_dict=defaultdict(int)
    for color in ar:
        color_dict[color]+=1
        if color_dict[color]==2:
            ret+=1
            color_dict[color]=0
    return ret

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
