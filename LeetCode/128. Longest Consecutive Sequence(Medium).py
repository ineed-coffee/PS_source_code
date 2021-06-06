class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums : return 0
        
        nset = set(nums)
        LCE=0
        
        for n in nset:
            if (n-1) not in nset:
                
                cur_num,cur_len=n,1
                
                while (cur_num+1) in nset:
                    cur_num+=1
                    cur_len+=1
                
                LCE = max(LCE,cur_len)
                
        return LCE
