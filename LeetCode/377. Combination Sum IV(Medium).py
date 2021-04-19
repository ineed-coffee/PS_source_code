class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp={0:1}
        nums.sort()
        
        def TD_dp(left):
            nonlocal dp,nums
            
            if left in dp : return dp[left]

            combs = sum([TD_dp(left-i) for i in [n for n in nums if n<=left]])    
            dp[left]=combs
            
            return dp[left]
        
        return TD_dp(target)
        
        
