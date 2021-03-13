class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        subs = set(range(2**k))

        for i in range(len(s)-k+1):
            subs.discard(int(s[i:i+k],2))
        return True if not subs else False
        


# Rolling - hash (Bitwise Op used)
class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        subs = set()
        compare=None
        splitter,L=2**k-1,2**k
        for i in range(len(s)-k+1):
            if compare==None:
                compare=int(s[i:i+k],2)
            else:
                compare=((compare<<1)&splitter)|int(s[i+k-1])
            if compare not in subs:
                subs.add(compare)
                L-=1
                if not L:
                    return True
        return False
