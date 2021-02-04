def solution(m, n, puddles):
    answer = 0
    
    grid=[[0]*m for _ in range(n)]
    pud = set([(x[1]-1,x[0]-1) for x in puddles])
    grid[0][0]=1
    
    for i in range(n):
        for j in range(m):
            if (i-1>=0) and ((i-1,j) not in pud):
                grid[i][j]+=grid[i-1][j]
            if (j-1>=0) and ((i,j-1) not in pud):
                grid[i][j]+=grid[i][j-1]
                        
    answer=grid[-1][-1]%(1000000007)
    return answer
