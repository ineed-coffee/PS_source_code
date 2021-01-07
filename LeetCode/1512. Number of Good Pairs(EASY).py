class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        L=len(nums)
        cnt=0
        for i in range(L):
            for j in range(i+1,L):
                if nums[i]==nums[j]:
                    cnt+=1
        return cnt
