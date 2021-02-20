class Solution:
    
    def divisorGame(self, N: int) -> bool:
        if N<3:
            return True if N==2 else False
        
        dp=[False]*(N+1)
        dp[0]=True
        dp[1]=False
        dp[2]=True
        
        for i in range(3,N+1):
            
            for j in range(1,int(i**0.5)+1):
                if (not i%j) and ((dp[i-j]==False) or (dp[i-(i//j)]==False)):
                    dp[i]=True
                    break
            
            # for j in range(1,i):
            #     if (not i%j) and (dp[i-j]==False):
            #         dp[i]=True
            #         break
        
        return dp[-1]
        
        
#         F,T,F,T,F,T,F,T,F,
        
#         1 2 3 4 5 6 7,8,9,10
