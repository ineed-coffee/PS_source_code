class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        answer=[-1]*len(A)
        even_idx=0
        odd_idx=1
        
        for num in A:
            if not num%2:
                answer[even_idx]=num
                even_idx+=2
            else:
                answer[odd_idx]=num
                odd_idx+=2
        return answer
        
