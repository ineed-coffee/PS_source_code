from sys import *

test_case = int(input().strip())

test=[int(stdin.readline().strip()) for _ in range(test_case)]

def Fib_count(N):
    if N==0:
        print('1 0')
        return 
    elif N==1:
        print('0 1')
        return
    else:
        fib=[0,1]+[0]*(N-1)
        for i in range(2,N+1):
            fib[i]=fib[i-1]+fib[i-2]
        print(fib[-2],fib[-1])
        return

for out in test:
    Fib_count(out)
