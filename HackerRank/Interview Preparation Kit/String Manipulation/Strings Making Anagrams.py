#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the makeAnagram function below.
def makeAnagram(a, b):
    a_dict,b_dict={},{}
    for letter in a:
        a_dict[letter]=a_dict.get(letter,0)+1
    for letter in b:
        b_dict[letter]=b_dict.get(letter,0)+1
    
    answer=0
    for k_a,v_a in a_dict.items():
        if b_dict.get(k_a,0):
            answer+=abs(v_a-b_dict.get(k_a))
        else:
            answer+=v_a
    for k_b,v_b in b_dict.items():
        if not a_dict.get(k_b,0):
            answer+=v_b
    return answer
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    a = input()

    b = input()

    res = makeAnagram(a, b)

    fptr.write(str(res) + '\n')

    fptr.close()
