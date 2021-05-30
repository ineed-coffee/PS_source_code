class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        L=len(nums)
        if L<2: return 0
        
        nums.sort()
        ret=-1
        for i in range(L-1):
            ret = max(ret,nums[i+1]-nums[i])
        return ret
