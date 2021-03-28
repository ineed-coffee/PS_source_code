class Solution:
    def countSubstrings(self, s: str) -> int:
        S=len(s)
        cnt=0
        for i in range(S):
            for l,r in [(i-1,i),(i,i)]:
                while (0<=l) and (r<S) and s[l]==s[r]:
                    cnt+=1
                    l-=1
                    r+=1
        return cnt
