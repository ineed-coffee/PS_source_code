class Solution:
    def maximumUnits(self, boxTypes: List[List[int]], truckSize: int) -> int:
        answer=0
        boxTypes.sort(key=lambda x:x[-1],reverse=True)
        
        for N,U in sorted(boxTypes,key=lambda x:(x[1],x[0]),reverse=True):
            cur_bn = min(truckSize,N)
            answer+= cur_bn*U
            truckSize-=cur_bn
            
            if not truckSize: break
                
        return answer
