class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        
        ret=[]
        
        def possible(ccols,col):
            L = len(ccols)
            for i,idx in enumerate(ccols):
                if (idx==col) or abs(idx-col)==(L-i):
                    return False
            return True
        
        def backtrack(crow,ccols):
            nonlocal n,ret
            
            if crow == n:
                ret.append(ccols[:])
                return
            
            for col in range(n):
                if possible(ccols,col):
                    ccols.append(col)
                    backtrack(crow+1,ccols)
                    ccols.pop()
            return
        
        backtrack(0,[])
        
        answer=[]
        for comb in ret:
            board = [["."]*n for _ in range(n)]
            for i in range(n):
                board[i][comb[i]]="Q"
            answer.append(["".join(row) for row in board])
        
        return answer
