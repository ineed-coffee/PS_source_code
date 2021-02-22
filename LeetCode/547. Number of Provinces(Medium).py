class Solution:

    # DFS approach using set
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        answer,visited,to_visit=0,{},set(range(len(isConnected)))
        
        while to_visit:
            answer+=1
            visiting=set([to_visit.pop()])
            while visiting:
                cur_node=visiting.pop()
                for i,val in enumerate(isConnected[cur_node]):
                    if val and (i in to_visit):
                        visiting.add(i)
                        to_visit.remove(i)
        return answer
                
        
    # DFS approach using stack
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        
        L=len(isConnected)
        visited=[False]*L
        answer=0
    
        for i in range(L):
            if not visited[i]:
                answer+=1
                stack=[i]
                visited[i]=True
                
                while stack:
                    cur_node=stack.pop()
                    for nxt_node,val in enumerate(isConnected[cur_node]):
                        if val and (not visited[nxt_node]):
                            visited[nxt_node]=True
                            stack.append(nxt_node)
        return answer
        

    # Union-Find approach
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        def find(node):
            nonlocal parent
            if parent[node]==node:
                return node
            parent[node]=find(parent[node])
            return parent[node]
        
        def union(node_a,node_b):
            head_a,head_b=find(node_a),find(node_b)
            
            if rank[head_a]>rank[head_b]:
                parent[head_b]=head_a
            else:
                parent[head_a]=head_b
                if rank[head_a]==rank[head_b]:
                    rank[head_b]+=1
            return
        
        L=len(isConnected)
        parent=list(range(L))
        rank=[0]*L
        
        for i,row in enumerate(isConnected):
            for j,val in enumerate(row):
                if (i!=j) and val:
                    if find(i)!=find(j):
                        union(i,j)
                
        heads=[find(i) for i in range(L)]
        return len(set(heads))
