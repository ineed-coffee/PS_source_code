class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        max_init = max(candies)
        L = len(candies)
        
        Answer = [True]*L
        
        for child in range(L):
            if candies[child]+extraCandies>=max_init:
                continue
            Answer[child]=False
            
        return Answer
