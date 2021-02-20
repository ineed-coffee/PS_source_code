class Solution:
    # back-tracking sol.
    def countVowelStrings(self, n: int) -> int:
        
         def backtrack(used_cnt,idx):
             if used_cnt==self.n:
                 self.answer+=1
                 return
             for i in range(idx,5):
                 backtrack(used_cnt+1,i)
             return
        
         self.answer=0
         self.n = n
         backtrack(0,0)
        
         return self.answer

    # dynamic programming sol.
    def countVowelStrings(self, n: int) -> int:
        dp = [[0,0,0,0,0] for _ in range(n)]
        dp[0]=[1,1,1,1,1]
        for i in range(1,n):
            for j in range(5):
                dp[i][j]=sum(dp[i-1][j:])
        
        return sum(dp[-1])
