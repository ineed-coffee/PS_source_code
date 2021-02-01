class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        
        drank=0
        
        while numBottles:
            if numBottles<numExchange:
                drank+=numBottles
                numBottles=0
                break
                
            exchanges = numBottles//numExchange
            numBottles-=(exchanges*numExchange-exchanges)
            drank+=exchanges*numExchange
            
        
        return drank
