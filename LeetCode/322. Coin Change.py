class Solution:
    def coinChange(self, coins, amount: int) -> int:
        
        L=len(coins)
        dp=[0]+[-1]*amount
        for coin in coins:
            for i in range(coin,amount+1):
                if (dp[i]==-1) and (dp[i-coin]!=-1):
                    dp[i]=dp[i-coin]+1

                elif dp[i-coin]!=-1:
                    dp[i]=min(dp[i],dp[i-coin]+1)
        
        return dp[-1]
