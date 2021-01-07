class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        
        Answer=0
        
        max_odd = len(arr) if len(arr)%2 else len(arr)-1
        
        for current_sub_len in range(1,max_odd+1,2):
            i=0
            while i+current_sub_len<=len(arr):
                Answer+=sum(arr[i:i+current_sub_len])
                i+=1
                
        return Answer
