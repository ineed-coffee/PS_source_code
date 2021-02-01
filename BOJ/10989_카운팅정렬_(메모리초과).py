import sys

N=int(input())
data=[0]*10001
for i in range(N):
    data[int(sys.stdin.readline())]+=1
    
for i in range(len(data)):
    if data[i]:
        for j in range(data[i]):
            print(i)
