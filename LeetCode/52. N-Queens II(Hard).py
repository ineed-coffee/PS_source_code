class Solution:
    def totalNQueens(self, n: int) -> int:
        
        def valid_place(col,ccols):
            L=len(ccols)
            for idx,ccol in enumerate(ccols):
                if (col==ccol) or (abs(ccol-col)==(L-idx)):
                    return False
            return True
        
        def backtrack(crow,ccols):
            nonlocal n,sols
            
            if crow==n:
                sols+=1
                return
            
            for col in range(n):
                if valid_place(col,ccols):
                    ccols.append(col)
                    backtrack(crow+1,ccols)
                    ccols.pop()
            return
        
        sols = 0
        backtrack(0,[])
        
        return sols
        
