#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the encryption function below.
def encryption(s):
    s = s.strip()
    s = s.replace(" ","")
    L = len(s)
    
    floor_ = int(L**0.5)
    ceil_ = int(L**0.5)+1 if int(L**0.5)!=(L**0.5) else (L**0.5)
    
    if floor_*floor_ >= L:
        row,col=floor_,floor_
    elif floor_*ceil_ >= L:
        row,col=floor_,ceil_
    else:
        row,col=ceil_,ceil_
        
    matrix = [["" for _ in range(col)] for __ in range(row)]
    for i,letter in enumerate(s):
        matrix[i//col][i%col]=letter
    
    return_string = ""
    
    for col in zip(*matrix):
        return_string+="".join(col)
        return_string+=" "
    return_string.strip()
    return return_string
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()
