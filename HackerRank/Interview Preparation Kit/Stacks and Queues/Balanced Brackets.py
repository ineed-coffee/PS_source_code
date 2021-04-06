#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the isBalanced function below.
def isBalanced(s):
    match={
        "(":")",
        "[":"]",
        "{":"}"
    }
    stack=[]
    for s_ in s:
        if s_ in match:
            stack.append(s_)
            continue
        if (not stack) or (s_!=match[stack[-1]]):
            return "NO"
        stack.pop()
    return "YES" if not stack else "NO"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        s = input()

        result = isBalanced(s)

        fptr.write(result + '\n')

    fptr.close()
