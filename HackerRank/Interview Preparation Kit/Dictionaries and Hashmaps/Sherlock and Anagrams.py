#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    cur_len = 1
    answer=0
    
    checked_pattern=set()
    while cur_len<len(s):
        for i in range(len(s)-cur_len):
            pattern="".join(sorted(s[i:i+cur_len]))
            pattern_cnt=1
            if pattern in checked_pattern:
                continue
            checked_pattern.add(pattern)
            for j in range(i+1,len(s)-cur_len+1):
                if "".join(sorted(s[j:j+cur_len]))==pattern:
                    pattern_cnt+=1
            answer+=((pattern_cnt)*(pattern_cnt-1))//2
        cur_len+=1
    print(checked_pattern)
    return answer

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        fptr.write(str(result) + '\n')

    fptr.close()
