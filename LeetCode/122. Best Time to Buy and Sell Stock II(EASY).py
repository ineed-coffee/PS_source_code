class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit=0
        buy_price,sell_price=-1,-1
        stack,cursor=[],0
        
        while cursor<len(prices):
            if buy_price==-1:
                if not stack:
                    stack.append(prices[cursor])
                    cursor+=1
                    continue
                if stack[-1]<prices[cursor]:
                    buy_price=stack[-1]
                else:
                    stack.pop()
                    stack.append(prices[cursor])
                    cursor+=1
            else:
                if sell_price==-1:
                    sell_price=prices[cursor]
                    cursor+=1
                    continue
                if sell_price<prices[cursor]:
                    sell_price=prices[cursor]
                    cursor+=1
                else:
                    if buy_price<sell_price:
                        profit+=sell_price-buy_price
                    stack.pop()
                    buy_price,sell_price=-1,-1
        
        if buy_price<sell_price:
            profit+=sell_price-buy_price
        
        return profit
                    
                
        
