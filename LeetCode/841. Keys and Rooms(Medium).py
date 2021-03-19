class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        L=len(rooms)
        visited=[False]*L
        start=0
        stack=[start]
        visited[start]=True
        while stack:
            c_node=stack.pop()
            for n_node in rooms[c_node]:
                if not visited[n_node]:
                    visited[n_node]=True
                    stack.append(n_node)
        return sum(visited)==L
        
