class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums)==1:
            return 1
        
        L=len(nums)
        start=0
        while (start<L-1) and (nums[start]==nums[start+1]):
            start+=1
            
        if start==L-1:
            return 1
            
        if nums[start]>nums[start+1]:
            pos=False
        else:
            pos=True
        
        seq_len=2
        for i in range(start,L-1):
            if (not pos) and (nums[i]<nums[i+1]):
                seq_len+=1
                pos= not pos
            elif pos and (nums[i]>nums[i+1]):
                seq_len+=1
                pos= not pos
        return seq_len
