from sys import *

class apartment():
    def __init__(self,matrix,num):
        self.Visited=[[0]*num for _ in range(num)]
        self.Cluster_num=0
        self.Cluster_sort = []
        self.dx=[-1,0,1,0]
        self.dy=[0,-1,0,1]
        self.N=num
        self.mat=matrix
        self.cnt=0

    def dfs_s(self,x,y):
        self.Visited[x][y]=1
        self.cnt+=1
        for idx in range(4):
            self.nx = x + self.dx[idx]
            self.ny = y + self.dy[idx]
            if self.nx<0 or self.nx>=self.N or self.ny<0 or self.ny>=self.N:
                continue
            if self.mat[self.nx][self.ny]=='1' and not self.Visited[self.nx][self.ny]:
                self.dfs_s(self.nx,self.ny)
        return

    def solve(self):
        for i in range(self.N):
            for j in range(self.N):
                if self.mat[i][j]=='1' and not self.Visited[i][j]:
                    self.cnt=0
                    self.Cluster_num+=1
                    self.dfs_s(i,j)
                    self.Cluster_sort.append(self.cnt)
        return
    
    def show(self):
        print(self.Cluster_num)
        self.Cluster_sort.sort()
        for order in self.Cluster_sort:
            print(order)
        return

    
N = int(input())

Map=[list(stdin.readline().strip()) for _ in range(N)]

Apart = apartment(Map,N)

Apart.solve()

Apart.show()
