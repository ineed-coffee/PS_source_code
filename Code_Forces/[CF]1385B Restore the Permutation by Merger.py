from sys import stdin
 
input = stdin.readline
 
T = int(input())
for case in range(T):
    n = int(input())
    Visited=[False]*(n+1)
    line = [*map(int,input().split())]
    Ans=[]
    for idx in line:
        if not Visited[idx]:
            Visited[idx]=True
            Ans.append(idx)
    print(*Ans)
