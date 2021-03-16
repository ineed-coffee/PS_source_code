class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        
        L=len(prices)
        
        profit=[0]*L
        last_buy=[0]*L
        
        profit[0]=0
        last_buy[0]=-1*prices[0]
        
        for i in range(1,L):
            last_buy[i]=max(last_buy[i-1],profit[i-1]-prices[i])
            profit[i]=max(profit[i-1],(prices[i]-fee)+last_buy[i])
            
        return profit[-1]
