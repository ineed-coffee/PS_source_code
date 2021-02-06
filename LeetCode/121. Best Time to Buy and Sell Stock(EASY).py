class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        bought=prices[0]
        max_profit=0
        for i in range(1,len(prices)):
            if bought>prices[i]:
                bought=prices[i]
            elif prices[i]-bought>max_profit:
                max_profit=prices[i]-bought
        return max_profit
        
