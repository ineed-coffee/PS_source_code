class Solution:
    def longestIncreasingPath(self, matrix):
        
        def traverse(coords,cnt):
            nonlocal cache,answer,visited,dx,dy,m,n
            i,j=coords
            if cache[i][j]>=cnt:
                return
            
            visited[i][j]=True
            cache[i][j]=cnt
            answer=max(answer,cnt)
            
            for k in range(4):
                ni,nj=i+dx[k],j+dy[k]
                if (0<=ni<m) and (0<=nj<n):
                    if (not visited[ni][nj]) and (matrix[i][j]<matrix[ni][nj]):
                        traverse((ni,nj),cnt+1)
            visited[i][j]=False
            return
        
        m,n=len(matrix),len(matrix[0])
        answer=0
        cache=[[0]*n for _ in range(m)]
        dx=[0,-1,0,1]
        dy=[1,0,-1,0]
        for i in range(m):
            for j in range(n):
                visited=[[False]*n for _ in range(m)]
                traverse((i,j),1)
        return answer
                
        
