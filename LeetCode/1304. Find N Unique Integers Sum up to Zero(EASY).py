class Solution:
    def sumZero(self, n: int) -> List[int]:
        
        Answer=[]
        D,R = n//2,n%2
        
        for i in range(1,D+1):
            Answer+=[i,-i]
        if R:
            Answer+=[0]
        return Answer
        
