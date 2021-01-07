class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        
        Answer = 0
        
        for customer in accounts:
            Answer = max(Answer,sum(customer))
            
        return Answer
