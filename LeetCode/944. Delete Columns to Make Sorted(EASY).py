class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        sorted_col_idx=set(range(len(strs[0])))
        cnt=0
        for row in range(len(strs)):
            if not row:continue
            
            remove_col=[]
            for col in sorted_col_idx:
                if ord(strs[row-1][col]) <= ord(strs[row][col]):
                    continue
                remove_col.append(col)
                
            for col in remove_col:
                sorted_col_idx.remove(col)
                cnt+=1
                
        return cnt
            
        
