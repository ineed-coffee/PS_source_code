from sys import *

stair_num = int(input())
stair,point=[],[[0,0]]
for _ in range(stair_num):
    stair.append(int(stdin.readline()))
    point.append([0,0])

for i in range(1,stair_num+1):
    if i==1:
        point[i]=[stair[i-1],stair[i-1]]
    else:
        point[i][0]=point[i-1][1]+stair[i-1]
        point[i][1]=stair[i-1]+max(point[i-2])

print(max(point[-1]))
