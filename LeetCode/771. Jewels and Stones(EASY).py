class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jewel_set = set(jewels)
        Answer=0
        
        for stone in stones:
            if stone in jewel_set:
                Answer+=1
        return Answer
