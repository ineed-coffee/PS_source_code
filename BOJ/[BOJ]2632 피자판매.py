from sys import *

input = stdin.readline

Size = int(input())
m,n = map(int,input().split())
A_case,A_slices={},[]
B_case,B_slices={},[]
A_case[0]=1
B_case[0]=1
for _ in range(m):
    num = int(input())
    try:
        A_case[num]+=1
    except KeyError :
        A_case[num]=1
    A_slices.append(num)

Asum = sum(A_slices)
A_case[Asum]=1

for _ in range(n):
    num = int(input())
    try:
        B_case[num]+=1
    except KeyError :
        B_case[num]=1
    B_slices.append(num)

Bsum = sum(B_slices)
B_case[Bsum]=1

for i in range(m):
    tmp=A_slices[i]
    for j in range(1,m-1):
        k = (i+j)%m
        tmp+=A_slices[k]
        try:
            A_case[tmp]+=1
        except KeyError:
            A_case[tmp]=1

for i in range(n):
    tmp=B_slices[i]
    for j in range(1,n-1):
        k = (i+j)%n
        tmp+=B_slices[k]
        try:
            B_case[tmp]+=1
        except KeyError:
            B_case[tmp]=1

Ans=0
for i in A_case.keys():
    try:
        Ans+=A_case[i]*B_case[Size-i]
    except KeyError:
        pass
print(Ans)


