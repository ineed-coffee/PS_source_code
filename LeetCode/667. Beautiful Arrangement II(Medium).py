class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        if n==1: return [1]
        
        answer=[1]
        mul=1
        for diff in range(k,0,-1):
            answer.append(answer[-1]+mul*diff)
            mul*=-1
    
        return answer if n==k+1 else answer+[i for i in range(k+2,n+1)]
