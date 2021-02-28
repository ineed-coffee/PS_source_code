#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the arrayManipulation function below.
def arrayManipulation(n, queries):
    arr=[0]*n
    for a,b,k in queries:
        arr[a-1]+=k
        if b<n:
            arr[b]-=k
            
    max_=arr[0]
    compare=arr[0]
    for i in range(1,n):
        compare+=arr[i]
        max_=max(max_,compare)
    return max_

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    queries = []

    for _ in range(m):
        queries.append(list(map(int, input().rstrip().split())))

    result = arrayManipulation(n, queries)

    fptr.write(str(result) + '\n')

    fptr.close()
