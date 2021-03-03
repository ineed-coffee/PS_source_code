class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        from heapq import heapify,heappush,heappop
        
        N=len(matrix)
        as_heap = [[row[0],(i,0)] for i,row in enumerate(matrix)]
        heapify(as_heap)
        
        count=0
        while count<k:
            cur_element,(cur_x,cur_y)=heappop(as_heap)
            count+=1
            nxt_y=cur_y+1
            if nxt_y<N:
                heappush(as_heap,[matrix[cur_x][nxt_y],(cur_x,nxt_y)])
        return cur_element
                
        
