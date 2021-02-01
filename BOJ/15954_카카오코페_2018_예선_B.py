from sys import *
from math import *

N,K=map(int,stdin.readline().split())

Dolls=list(map(int,stdin.readline().split()))
#Dolls.sort()
Stan=int(sqrt(maxsize))

for i in range(N-K+1):
    for j in range (K,N-i+1):
        Avg=sum(Dolls[i:i+j])/j
        Variance=0
        for k in range(i,i+j):
            Variance+=(Dolls[k]-Avg)**2
        Variance=Variance/j
        if Variance < Stan**2:
            Stan = sqrt(Variance)
print(round(Stan,12))
