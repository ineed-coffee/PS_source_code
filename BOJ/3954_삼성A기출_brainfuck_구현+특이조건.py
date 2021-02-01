from sys import *
#from collections import deque
#from itertools import *
#from itertools import permutations
#from copy import *
#setrecursionlimit(10000)


#-------------------------------------------------------------------------
Limit=5*(10**7)
input = stdin.readline
Test_case = int(input())
for case in range(Test_case):
    M,C,I = map(int,input().split())                                       
    Mem = [0]*M
    idx=0
    Commands = list(input().strip())
    c_idx=0
    Inp = list(input().strip())
    in_idx=0
    
    Loop_info={}
    stack=[]
    ignored={}
    for i in range(C):
        if Commands[i]=='[':
            stack.append(i)
        elif Commands[i]==']':
            j = stack.pop()
            Loop_info[i]=j
            Loop_info[j]=i
            ignored[i]=False

    looped=True
    tried=0
    while tried<Limit:
        com = Commands[c_idx]

        if com=='+':
            Mem[idx]= (Mem[idx]+1)%256
            c_idx+=1

        elif com=='-':
            Mem[idx]= (Mem[idx]-1)%256
            c_idx+=1

        elif com=='<':
            idx = (idx-1)%M
            c_idx+=1

        elif com=='>':
            idx = (idx+1)%M
            c_idx+=1

        elif com=='[' :
            if not Mem[idx]:
                c_idx = Loop_info[c_idx]
            else:
                c_idx+=1

        elif com==']':
            if Mem[idx]:
                c_idx = Loop_info[c_idx]
            elif not ignored[c_idx]:
                ignored[c_idx]=True
            else:
                c_idx+=1

        elif com==',':
            if in_idx<I:
                Mem[idx] = ord(Inp[in_idx])%256
                in_idx+=1
                c_idx+=1
            else:
                Mem[idx] = 255
                c_idx+=1
        else:
            c_idx+=1

        tried+=1

        if c_idx>=C:
            print('Terminates')
            looped=False
            break

    if looped:
        for k,v in ignored.items():
            if not v:
                print(f'Loops {Loop_info[k]} {k}')
                break
