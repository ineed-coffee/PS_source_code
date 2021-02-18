class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        
        self.graph=graph
        self.routes=[]
        self.visited=[False]*len(graph)
        self.N=len(graph)-1
        
        def backtrack(node,route):
            if node==self.N:
                self.routes.append(route)
                return
            
            for next_node in self.graph[node]:
                if not self.visited[next_node]:
                    self.visited[next_node]=True
                    backtrack(next_node,route+[next_node])
                    self.visited[next_node]=False    
            return
        
        backtrack(0,[0])
        return self.routes
