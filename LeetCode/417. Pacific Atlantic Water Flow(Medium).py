class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:return []    
        
        def dfs(stack_):
            nonlocal dx,dy,M,N,matrix
            
            stack=stack_
            visited=set(stack)
            ret=set()
            while stack:
                cx,cy=stack.pop()
                ret.add((cx,cy))    
                for i in range(4):
                    nx,ny=cx+dx[i],cy+dy[i]
                    if (0<=nx<M) and (0<=ny<N) and (matrix[cx][cy]<=matrix[nx][ny]):
                        if (nx,ny) not in visited:
                            visited.add((nx,ny))
                            stack.append((nx,ny))
            return ret
        
        M,N=len(matrix),len(matrix[0])
        dx=[0,1,0,-1]
        dy=[-1,0,1,0]
        P_side=[(0,i) for i in range(N)]+[(i,0) for i in range(M)]
        A_side=[(M-1,i) for i in range(N)]+[(i,N-1) for i in range(M)]
        reach_P= dfs(P_side)
        reach_A= dfs(A_side)
        answer=reach_P&reach_A
        return [list(el) for el in answer]
