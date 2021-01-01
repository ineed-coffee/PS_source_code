class Solution:
    
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked={}
        for i in range(len(nums)):
            remain = target - nums[i]
            if remain in checked:
                return [i,checked[remain]]
            checked[nums[i]]=i
        return None
