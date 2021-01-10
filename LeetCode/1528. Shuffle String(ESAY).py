class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        Answer = [0]*len(s)
        
        for i in range(len(s)):
            Answer[indices[i]]=s[i]
        return "".join(Answer)
        
