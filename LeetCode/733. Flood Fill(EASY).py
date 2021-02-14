class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, newColor: int) -> List[List[int]]:
        self.R,self.C = len(image),len(image[0])
        self.image=image
        self.color=newColor
        self.visited=[[False]*self.C for _ in range(self.R)]
        self.dx=[0,1,0,-1]
        self.dy=[1,0,-1,0]
        
        self.dfs(sr,sc)
        
        return self.image
    
    def dfs(self,x,y):
        self.visited[x][y]=True
        
        for i in range(4):
            new_x=x+self.dx[i]
            new_y=y+self.dy[i]
            if (0<=new_x<self.R) and (0<=new_y<self.C) and (not self.visited[new_x][new_y]):
                if self.image[x][y]==self.image[new_x][new_y]:
                    self.dfs(new_x,new_y)
        self.image[x][y]=self.color
        return
        
        
        
