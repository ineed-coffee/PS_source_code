class Solution:
    def minOperations(self, n: int) -> int:
        D,R=n//2,n%2
        return D*(D +int(R!=0))
