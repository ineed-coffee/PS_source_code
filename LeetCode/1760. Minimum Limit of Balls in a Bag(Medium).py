class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        from heapq import heapify , heappop , heappush
        
        nums.sort(reverse=True)
        low=1
        high=max(nums)
        while low<high:
            mid=(low+high)>>1
            required_ops=0
            
            for num in nums:
                if num<=mid:
                    break
                required_ops+=(num//mid)-int(num%mid==0)
            if required_ops>maxOperations:
                low=mid+1
            else:
                high=mid
        return low
                        
                
        
