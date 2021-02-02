class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort(reverse=True)
        S=sum(nums)
        for i in range(1,len(nums)+1):
            if sum(nums[:i])>S//2:
                return nums[:i]
