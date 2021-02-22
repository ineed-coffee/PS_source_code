class Solution:
    def letterCasePermutation(self, S: str):
        self.L=len(S)
        self.answer=[]
                    
        def backtrack(cur_str,cur_idx):
            nonlocal S
            
            if len(cur_str)==self.L:
                self.answer.append(cur_str)
                return
            
            for i in range(cur_idx,self.L):
                if not S[i].isalpha():
                    cur_str+=S[i]
                    
                else:
                    backtrack(cur_str+S[i].lower(),i+1)
                    backtrack(cur_str+S[i].upper(),i+1)
                    
            if len(cur_str)==self.L:
                self.answer.append(cur_str)
            return
                    
        backtrack("",0)
        return self.answer
            
        
        
