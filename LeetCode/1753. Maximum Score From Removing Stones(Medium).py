class Solution:
    def maximumScore(self, a: int, b: int, c: int) -> int:
        stones=sorted([a,b,c])
        answer=stones[0]
        answer+=min(stones[1],(stones[1]+stones[2]-stones[0])//2)
        return answer
        
