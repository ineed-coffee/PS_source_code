class Solution:
    def balancedStringSplit(self, s: str) -> int:
        
        return_val=0
        L_cnt,R_cnt=0,0
        for character in s:
            
            if character=="L":
                L_cnt+=1
            elif character=="R":
                R_cnt+=1
            
            if (L_cnt*R_cnt) and (L_cnt==R_cnt):
                return_val+=1
                L_cnt,R_cnt=0,0
            
        return return_val
        
