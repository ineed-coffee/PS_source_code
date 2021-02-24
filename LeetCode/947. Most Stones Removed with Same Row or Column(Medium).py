class Solution:

    # DFS approach
    def removeStones(self, stones: List[List[int]]) -> int:
        from collections import defaultdict
        adj=defaultdict(list)
        L=len(stones)
        
        for i in range(L):
            for j in range(i+1,L):
                if (stones[i][0]==stones[j][0]) or (stones[i][1]==stones[j][1]):
                    adj[i].append(j)
                    adj[j].append(i)
                    
        def dfs(start):
            nonlocal visited,adj
            
            visited[start]=True
            stack,size=[start],1
            
            while stack:
                cur_node=stack.pop()
                for nxt_node in adj[cur_node]:
                    if not visited[nxt_node]:
                        visited[nxt_node]=True
                        stack.append(nxt_node)
                        size+=1
            return size
                    
        Answer=0
        visited=[False]*L
        for i in range(L):
            if not visited[i]:
                size=dfs(i)
                Answer+=(size-1)

        return Answer
    
    # Union-Find approach
    def removeStones(self, stones: List[List[int]]) -> int:
        parent,rank,size,adj=[],[],[],[]
        
        for i in range(len(stones)):
            parent+=[len(parent)]
            rank+=[0]
            size+=[1]
            for j in range(i+1,len(stones)):
                node1,node2=stones[i],stones[j]
                if (node1[0]==node2[0]) or (node1[1]==node2[1]):
                    adj.append([i,j])
                    
        def find(node):
            nonlocal parent
            if parent[node]==node:
                return node
            parent[node]=find(parent[node])
            return parent[node]
        
        def union(n_a,n_b):
            nonlocal parent,rank,size
            
            h_a,h_b=find(n_a),find(n_b)
            if rank[h_a]>rank[h_b]:
                parent[h_b]=h_a
                size[h_a]+=size[h_b]
                size[h_b]=0
            else:
                parent[h_a]=h_b
                size[h_b]+=size[h_a]
                size[h_a]=0
                if rank[h_a]==rank[h_b]:
                    rank[h_b]+=1
            return
        
        for n1,n2 in adj:
            if find(n1)!=find(n2):
                union(n1,n2)
        
        return sum([chunk-1 for chunk in size if chunk])
