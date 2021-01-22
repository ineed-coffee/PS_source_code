class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        
        weak_order = []
        L=len(mat[0])
        for i,row in enumerate(mat):
            
            low,high=0,L-1
            
            while low<high:
                
                mid=(low+high)//2
                if row[mid]:
                    low=mid+1
                else:
                    high=mid
            
            low = low if row[low] else low-1
            weak_order.append((low,i))
            
        weak_order.sort()
        
        return [idx[1] for idx in weak_order[:k]]
    
