from sys import *

setrecursionlimit(10**6)

from sys import *

class cab_farm():
    def __init__(self,matrix,row,col):
        self.Visited=[[0]*row for ex in range(col)]
        self.Cluster_num=0
        self.dx=[-1,0,1,0]
        self.dy=[0,-1,0,1]
        self.R=row
        self.C=col
        self.mat=matrix

    def dfs_s(self,x,y):
        self.Visited[x][y]=1
        for idx in range(4):
            self.nx = x + self.dx[idx]
            self.ny = y + self.dy[idx]
            if self.nx<0 or self.nx>=self.C or self.ny<0 or self.ny>=self.R:
                continue
            if self.mat[self.nx][self.ny]==1 and not self.Visited[self.nx][self.ny]:
                self.dfs_s(self.nx,self.ny)
        return

    def solve(self):
        for i in range(self.C):
            for j in range(self.R):
                if self.mat[i][j]==1 and not self.Visited[i][j]:
                    self.Cluster_num+=1
                    self.dfs_s(i,j)
        return
    
    def show(self):
        print(self.Cluster_num)
        return

    
Test_case = int(input())

for _ in range(Test_case):
    M,N,K=map(int,stdin.readline().split())
    test = [[0]*M for col in range(N)]
    for pos in range(K):
        i,j=map(int,stdin.readline().split())
        test[j][i]=1
    Cab= cab_farm(test,M,N)
    Cab.solve()
    Cab.show()
