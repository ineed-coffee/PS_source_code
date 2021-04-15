class Solution:
    def fib(self, n: int) -> int:
        if n<=1:
            return n
        dp=[i for i in range(n+1)]
        for i in range(2,n+1):
            dp[i]=dp[i-1]+dp[i-2]
        return dp[-1]
