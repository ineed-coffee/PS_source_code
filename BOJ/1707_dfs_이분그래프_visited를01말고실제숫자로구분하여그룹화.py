from sys import *
setrecursionlimit(10000)

def dfs_s(group_type,idx):
    global Flag
    Visited[idx]=group_type

    for nxt in Adj[idx]:
        if not Visited[nxt]:
            dfs_s(3-group_type,nxt)
        elif Visited[idx]==Visited[nxt]:
            Flag=False
            break

    return

def solve():

    for i in range(1,V+1):
        if not Visited[i]:
            dfs_s(1,i)
    
    return


test_case = int(input())

for case in range(test_case):
    V,E=map(int,stdin.readline().split())
    Adj=[[] for _ in range(V+1)]
    Visited = [0]*(V+1)

    for line in range(E):
        a,b = map(int,stdin.readline().split())
        Adj[a].append(b)
        Adj[b].append(a)

    Flag = True
    solve()
    print('YES' if Flag else 'NO')
