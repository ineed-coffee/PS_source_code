class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        dp = [0]*len(nums)
        equal_tmp = 0
        ordered = sorted(nums)
        
        for i in range(len(nums)-1):
            
            if ordered[i]< ordered[i+1]:
                dp[i+1]=dp[i]+1+equal_tmp
                equal_tmp=0
            else:
                dp[i+1]=dp[i]
                equal_tmp+=1
                        
        return [dp[ordered.index(val)] for val in nums]
