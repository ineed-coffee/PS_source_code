class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        ret_list=[nums[0]]
        
        for i in range(1,len(nums)):
            ret_list.append(nums[i]+ret_list[-1])
            
        return ret_list
