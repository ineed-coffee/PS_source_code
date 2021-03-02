class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        from heapq import heapify,heappop
        
        nums = [(-i,i) for i in nums]
        heapify(nums)
        return [heappop(nums) for _ in range(k)][-1][-1]
        
