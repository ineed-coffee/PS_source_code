# BFS------------------------------------------
def solution(n, computers):
    from collections import deque
    
    connects = 0
    visited = [False for _ in range(n)]
            
    for i in range(n):
        if not visited[i]:
            connects+=1
            
            que = deque([i])
            while que:
                current_node = que.popleft()
                visited[current_node]=True
                for j in range(n):
                    if (not visited[j]) and (computers[current_node][j]==1):
                        que.append(j)
          
    return connects

# DFS------------------------------------------
def solution(n, computers):
    from collections import deque
    
    connects = 0
    visited = [False for _ in range(n)]
            
    for i in range(n):
        if not visited[i]:
            connects+=1
            
            stack=[i]
            while stack:
                current_node=stack.pop()
                visited[current_node]=True
                for j in range(n):
                    if (not visited[j]) and (computers[current_node][j]==1):
                        stack.append(j)
          
    return connects
