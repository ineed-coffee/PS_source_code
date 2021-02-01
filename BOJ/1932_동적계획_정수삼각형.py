from sys import *

stair_num = int(input())
stair=[]

for _ in range(stair_num):
    stair.append(list(map(int,stdin.readline().split())))


for i in range(1,stair_num):
    for j in range(len(stair[i])):
        if j==0:
            stair[i][j]=stair[i-1][j]+stair[i][j]
        elif j==len(stair[i])-1:
            stair[i][j]=stair[i-1][-1]+stair[i][j]
        else:
            stair[i][j]=stair[i][j]+max(stair[i-1][j-1],stair[i-1][j])


print(max(stair[-1]))
