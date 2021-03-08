class Solution:
    def removePalindromeSub(self, s: str) -> int:
        if not s: return 0
        return int(s==s[::-1])*(-1)+2
