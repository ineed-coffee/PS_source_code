def solution(board):
    min_cost=None
    N=len(board)
    visited=[[False]*N for _ in range(N)]
    accum_min_mat=[[[-1]*4 for _ in range(N)] for _ in range(N)]
    dx,dy=[1,0,-1,0],[0,-1,0,1]

    def backtrack(c_node,c_cost,p_dir):
        nonlocal N,dx,dy,visited,accum_min_mat,min_cost,board
        cx,cy=c_node
        if (cx,cy)==(N-1,N-1):
            if min_cost==None:
                min_cost=c_cost
            else:
                min_cost=min(min_cost,c_cost)
            return
        
        for i in range(4):
            nx,ny=cx+dx[i],cy+dy[i]
            if (0<=nx<N) and (0<=ny<N) and (not visited[nx][ny]):
                if (not board[nx][ny]):
                    if (i==p_dir) or (p_dir==-1):
                        n_cost=c_cost+100
                    else:
                        n_cost=c_cost+600
                        
                    if (accum_min_mat[nx][ny][i]==-1) or (n_cost<accum_min_mat[nx][ny][i]):
                        accum_min_mat[nx][ny][i]=n_cost
                        visited[nx][ny]=True
                        backtrack((nx,ny),n_cost,i)
                        visited[nx][ny]=False

        return
    
    visited[0][0]=True
    accum_min_mat[0][0]=0
    backtrack((0,0),0,-1)
    
    return min_cost
