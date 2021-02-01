from sys import *


def Split(part,size):
    if size==1:
        if part[0][0]==1:
            return '1'
        elif part[0][0]==0:
            return '0'
    else:
        Sum=0
        for i in range(size):
            Sum+=sum(part[i])
                    
        if Sum==0 or Sum==size*size:
            if part[0][0]==1:
                return '1'
            elif part[0][0]==0:
                return '0'
        else:
            size=size//2
            left=[l[:size] for l in part]
            right=[r[size:] for r in part]
            part1=left[:size]
            part2=right[:size]
            part3=left[size:]
            part4=right[size:]
            a1=Split(part1,size)
            a2=Split(part2,size)
            a3=Split(part3,size)
            a4=Split(part4,size)
            return '('+a1+a2+a3+a4+')'

N=int(input())
sample=[list(map(int,list(stdin.readline().strip()))) for _ in range(N)]
print(Split(sample,N))
'''
8
11110000
11110000
00011100
00011100
11110000
11110000
11110011
11110011
'''
