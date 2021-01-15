# class Solution:
#     def numIdenticalPairs(self, nums: List[int]) -> int:
#         L=len(nums)
#         cnt=0
#         for i in range(L):
#             for j in range(i+1,L):               
#                 if nums[i]==nums[j]:
#                     cnt+=1
#         return cnt
    
#------------------------------------------------------------

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:

        num_dict = {}
        Answer=0
        
        for num in nums:
            try:
                num_dict[num]+=1
            except KeyError:
                num_dict[num]=1
            
        for value in num_dict.values():
            Answer += (value*(value-1))/2
                    
        return int(Answer)
