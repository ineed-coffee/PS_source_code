class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s: return True
        s_cursor=0
        for i in range(len(t)):
            if t[i]==s[s_cursor]:
                s_cursor+=1
                if s_cursor==len(s):
                    break
        return True if s_cursor==len(s) else False
        
