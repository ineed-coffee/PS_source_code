from sys import *

test_case=int(input())
for _ in range(test_case):
    N,M=map(int,stdin.readline().split())
    Weights=list(map(int,stdin.readline().split()))
    idx=list(range(N))
    order=1
    while order<N:
        if Weights[0]==max(Weights):
            if idx[0]==M:
                break
            else:
                Weights.pop(0)
                idx.pop(0)
                order+=1
        else:
            Weights.append(Weights.pop(0))
            idx.append(idx.pop(0))
    
    print(order)   


