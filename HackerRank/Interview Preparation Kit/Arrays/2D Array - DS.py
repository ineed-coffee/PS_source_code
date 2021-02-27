#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hourglassSum function below.
def hourglassSum(arr):
    max_val=-70
    for i in range(1,5):
        for j in range(1,5):
            center=arr[i][j]
            center+=arr[i-1][j-1]
            center+=arr[i-1][j]
            center+=arr[i-1][j+1]
            center+=arr[i+1][j-1]
            center+=arr[i+1][j]
            center+=arr[i+1][j+1]
            max_val=max(max_val,center)
    return max_val
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

    result = hourglassSum(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
