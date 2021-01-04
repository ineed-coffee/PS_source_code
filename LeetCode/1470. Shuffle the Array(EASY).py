class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        
        return_list = []
        
        for i in range(n):  
            return_list.append(nums[i])
            return_list.append(nums[i+n])
        
        return return_list
