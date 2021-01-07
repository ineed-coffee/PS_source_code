class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        
        Answer = 0
        
        for element in nums:
            if not len(str(element))%2:
                Answer+=1
                
        return Answer
