#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countSwaps function below.
def countSwaps(a):
    L=len(a)
    swaps=0
    
    for i in range(L):
        for j in range(L-1):
            if a[j]>a[j+1]:
                swaps+=1
                a[j],a[j+1]=a[j+1],a[j]
    print(f"Array is sorted in {swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[-1]}")
    return

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
