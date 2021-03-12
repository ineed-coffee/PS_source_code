class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        subs = set(range(2**k))

        for i in range(len(s)-k+1):
            subs.discard(int(s[i:i+k],2))
        return True if not subs else False
        
