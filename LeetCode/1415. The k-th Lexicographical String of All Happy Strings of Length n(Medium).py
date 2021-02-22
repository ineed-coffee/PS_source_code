class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.bag=["a","b","c"]
        self.happy_strings=[]
        
        def backtrack(cur_str):
            nonlocal n
            if len(cur_str)==n:
                self.happy_strings.append(cur_str)
                return
            
            for letter in self.bag:
                if (not cur_str) or (letter!=cur_str[-1]):
                    backtrack(cur_str+letter)
        backtrack("")
        if k>len(self.happy_strings):
            return ""
        return self.happy_strings[k-1]
        
