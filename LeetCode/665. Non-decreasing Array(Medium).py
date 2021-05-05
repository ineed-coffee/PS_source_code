class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        
        dec_point = []
        for i in range(n-1):
            if nums[i]>nums[i+1]:
                dec_point.append(i)
        
        L = len(dec_point) 
        if L  >= 2:
            return False
        elif L == 0:
            return True
        else:
            cnt1 = sum([num for num in nums[:dec_point[0]] if num > nums[dec_point[0]+1]])
            cnt2 = sum([num for num in nums[dec_point[0]+2:] if num < nums[dec_point[0]]])
            
            if cnt1 and cnt2:
                return False
            else:
                return True
        
