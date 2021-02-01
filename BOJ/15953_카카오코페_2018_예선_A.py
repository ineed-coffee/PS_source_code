from sys import *

K_17_price=[0,5000000,3000000,2000000,500000,300000,100000]
K_17_to=[1,2,3,4,5,6]
K_18_price=[0,5120000,2560000,1280000,640000,320000]
K_18_to=[1,2,4,8,16]
A,B=[0],[0]

for i in range(len(K_17_to)):
    for j in range(K_17_to[i]):
        A.append(i+1)
    
for i in range(len(K_18_to)):
    for j in range(K_18_to[i]):
        B.append(i+1)
        
def Solve(a,b):
    try:
        return K_17_price[A[a]]+K_18_price[B[b]]
    except:
        if a>=len(A):
            return K_18_price[B[b]] if b<len(B) else 0
        elif b>=len(B):
            return K_17_price[A[a]]

T=int(input())
for _ in range(T):
    a,b=map(int,stdin.readline().split())
    print(Solve(a,b))
