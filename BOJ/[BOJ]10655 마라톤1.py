from sys import *

input = stdin.readline

N = int(input())
Cords=[]
for i in range(N):
    x,y = map(int,input().split())
    Cords.append([x,y])

dist_n=[]
dist_nn=[]
for i in range(N-1):
    dist1 = abs(Cords[i][0]-Cords[i+1][0])+abs(Cords[i][1]-Cords[i+1][1])
    dist_n.append(dist1)
    if i+2<=N-1:
        dist2 = abs(Cords[i][0]-Cords[i+2][0])+abs(Cords[i][1]-Cords[i+2][1])
        dist_nn.append(dist2)
D = sum(dist_n)
Ans = D-dist_n[0]-dist_n[1]+dist_nn[0]
for i in range(N-2):
    Ans = min(Ans,D-dist_n[i]-dist_n[i+1]+dist_nn[i])
print(Ans)
