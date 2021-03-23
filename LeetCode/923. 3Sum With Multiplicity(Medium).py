class Solution:
    def threeSumMulti(self, arr, target: int) -> int:
        L=len(arr)
        mod=10**9 + 7
        answer=0
        
        single={}
        double={}
        
        for n in arr:
        
            answer+=double.get(target-n,0)
            answer=answer%mod
            
            for k,v in single.items():
                double[n+k]=double.get(n+k,0)+v
            
            single[n]=single.get(n,0)+1
            
        return answer%mod
