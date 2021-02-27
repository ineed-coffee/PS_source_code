#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr):
    arr_dict = {}
    for i,num in enumerate(arr):
        arr_dict[num]=i
    
    swaps,idx=0,0
    
    while idx<len(arr):
        if arr[idx]==(idx+1):
            idx+=1
            continue
        
        swap1,swap2 = idx,arr_dict[(idx+1)]
        arr_dict[(idx+1)],arr_dict[arr[idx]]=arr_dict[arr[idx]],arr_dict[(idx+1)]
        arr[swap1],arr[swap2]=arr[swap2],arr[swap1]
        swaps+=1
        idx+=1
    return swaps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = minimumSwaps(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
