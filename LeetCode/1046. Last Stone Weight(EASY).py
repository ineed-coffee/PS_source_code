class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        from heapq import heappush,heappop,heapify
        
        heap=[*map(lambda x :-x , stones)]
        heapify(heap)
        
        while len(heap)>1:
            stone1=-1*heappop(heap)
            stone2=-1*heappop(heap)
            
            if stone1==stone2:
                continue
            else:
                heappush(heap,-1*abs(stone1-stone2))
                
        if not heap:
            return 0
        else:
            return -1*heap[0]
            
        
