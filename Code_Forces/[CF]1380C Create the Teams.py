from sys import *

input = stdin.readline

T= int(input())

for case in  range(T):
    n,x = map(int,input().split())
    Skills = [*map(int,input().split())]
    Skills.sort(reverse=True)

    cnt=0
    Ans=0
    for i in range(n):
        cnt+=1
        if cnt*Skills[i]>=x:
            Ans+=1
            cnt=0
    print(Ans)
    










#11 9 7 5 2 
