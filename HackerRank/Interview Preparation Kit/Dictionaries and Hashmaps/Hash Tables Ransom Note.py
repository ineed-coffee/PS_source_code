#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    from collections import defaultdict
    
    m_dict=defaultdict(int)
    for word in magazine:
        m_dict[word]+=1
    for word in note:
        if m_dict[word]:
            m_dict[word]-=1
            continue
        return "No"
    return "Yes"
    
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    print(checkMagazine(magazine, note))
