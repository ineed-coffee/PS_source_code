from sys import *

H_num = int(input())
Cost=[]

for _ in range(H_num):
    r,g,b=map(int,stdin.readline().split())
    Cost.append([r,g,b])


for i in range(1,H_num):
    Cost[i][0]=min(Cost[i][0]+Cost[i-1][1],Cost[i][0]+Cost[i-1][2])
    Cost[i][1]=min(Cost[i][1]+Cost[i-1][0],Cost[i][1]+Cost[i-1][2])
    Cost[i][2]=min(Cost[i][2]+Cost[i-1][0],Cost[i][2]+Cost[i-1][1])


print(min(Cost[-1]))
