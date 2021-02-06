class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.dp(nums)
        
    def dp(self,nums):
        if len(nums)==1: return nums[0]
        
        for i in range(1,len(nums)):
            if nums[i] >= nums[i]+nums[i-1]:
                continue
            else:
                nums[i]+=nums[i-1]
        return max(nums)
