class Solution:
    def reverse(self, x: int) -> int:
        
        if x>=0:
            x_reversed = int(str(x)[::-1])
        else:
            x_reversed = -int(str(abs(x))[::-1])
            
        if (x_reversed<-2**31) or (x_reversed>2**31-1):
            return 0
        
        return x_reversed
