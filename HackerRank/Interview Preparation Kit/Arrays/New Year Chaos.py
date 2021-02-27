#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    from collections import deque
    L = len(q)
    initial=deque(list(range(1,L+1)))
    left=[2]*(L+1)
    pointer=0
    bribes=0
    while initial:
        if initial[0]==q[pointer]:
            pointer+=1
            initial.popleft()
        elif initial[0]<q[pointer]:
            if (len(initial)>1) and (initial[1]==q[pointer]):
                if left[q[pointer]]<1:
                    return "Too chaotic"
                fst=initial.popleft()
                snd=initial.popleft()
                initial.appendleft(fst)
                bribes+=1
                left[q[pointer]]-=1
                pointer+=1
            elif (len(initial)>2) and (initial[2]==q[pointer]):
                if left[q[pointer]]<2:
                    return "Too chaotic"
                fst=initial.popleft()
                snd=initial.popleft()
                thd=initial.popleft()
                initial.appendleft(snd)
                initial.appendleft(fst)
                bribes+=2
                left[q[pointer]]-=2
                pointer+=1
            else:
                return "Too chaotic"
        
    return bribes

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        q = list(map(int, input().rstrip().split()))

        print(minimumBribes(q))
