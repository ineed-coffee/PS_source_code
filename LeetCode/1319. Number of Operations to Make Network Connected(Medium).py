class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        parent=[i for i in range(n)]
        rank,size=[0]*n,[1]*n
        used_cable=[0]*n
        
        def find(node):
            nonlocal parent
            if parent[node]==node:
                return node
            parent[node]=find(parent[node])
            return parent[node]
        
        def union(node_a,node_b):
            nonlocal parent,rank,size,used_cable
            
            head_a,head_b=find(node_a),find(node_b)
            if rank[head_a]>rank[head_b]:
                parent[head_b]=head_a
                size[head_a]+=size[head_b]
                used_cable[head_a]+=used_cable[head_b]
                size[head_b],used_cable[head_b]=0,0
            else:
                parent[head_a]=head_b
                size[head_b]+=size[head_a]
                used_cable[head_b]+=used_cable[head_a]
                size[head_a],used_cable[head_a]=0,0
                if rank[head_a]==rank[head_b]:
                    rank[head_b]+=1
            return
        
        for a,b in connections:
            if find(a)!=find(b):
                union(a,b)
            used_cable[find(a)]+=1
        
        cables_left,heads=0,0
        for node in range(n):
            if size[node]:
                cables_left+=used_cable[node]-size[node]+1
                heads+=1
        
        if cables_left>=heads-1:
            return heads-1
        else:
            return -1
