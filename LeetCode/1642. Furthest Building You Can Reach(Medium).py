class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        from heapq import heapify,heappush,heappop
        
        low,high = 0 , len(heights)
        
        while low<high:
            mid = (low+high)//2
            #print(mid)
            cur_bricks,cur_ladders=bricks,ladders
            
            required=[]
            heapify(required)
            for idx in range(mid+1):
                if not idx:
                    cur_H = heights[idx]
                    continue
                if heights[idx]>cur_H:
                    heappush(required,heights[idx]-cur_H)
                cur_H = heights[idx]
            #print(required)
            
            while cur_bricks or cur_ladders:
                if not required:
                    break
                cur_min = heappop(required)
                if cur_bricks>=cur_min:
                    cur_bricks-=cur_min
                else:
                    if cur_bricks:
                        cur_bricks=0
                    cur_ladders-=1
                
            if not required:
                #print("possible")
                low=mid+1
            else:
                #print("impossible")
                high=mid
        return low-1
