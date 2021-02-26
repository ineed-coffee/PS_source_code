#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c):
    idx=0
    steps=0
    
    while True:
        if (idx+2<len(c)) and (not c[idx+2]):
            steps+=1
            idx+=2
        elif (idx+1<len(c)) and (not c[idx+1]):
            steps+=1
            idx+=1
        if idx==len(c)-1:
            break
    return steps
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
