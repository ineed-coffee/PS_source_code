class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        S=len(s)
        vowels=set(["a","e","i","o","u",
                   "A","E","I","O","U"])
        h1,h2=0,0
        L,R=0,S-1
        while L<R:
            if s[L] in vowels: h1+=1
            if s[R] in vowels: h2+=1
            L+=1
            R-=1
        return h1==h2
