def solution(n, results):
    winloss = {key:[[],[]] for key in range(1,n+1)}
    
    for a,b in results:
        winloss[a][0].append(b)
        winloss[b][1].append(a)
    
    answer=0
    for node in winloss:
        win = dfs(node,winloss,n,0)
        lost = dfs(node,winloss,n,1)
        if win+lost==n-1:
            answer+=1
    return answer
    
def dfs(node,adj,n,W_L):
    ret=0
    stack=adj[node][W_L][:]
    visited=[False]*(n+1)
    for _ in stack:
        visited[_]=True
    while stack:
        current_node=stack.pop()
        ret+=1
        for next_node in adj[current_node][W_L]:
            if (not visited[next_node]) and (next_node!=node):
                visited[next_node]=True
                stack.append(next_node)
    return ret
