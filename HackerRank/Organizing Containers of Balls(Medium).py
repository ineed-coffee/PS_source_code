#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the organizingContainers function below.
def organizingContainers(container):
    row_sum=[]
    for row in container:
        row_sum.append(sum(row))
    col_sum=[]
    for col in zip(*container):
        col_sum.append(sum(col))
    return "Possible" if sorted(row_sum)==sorted(col_sum) else "Impossible"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        n = int(input())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()
