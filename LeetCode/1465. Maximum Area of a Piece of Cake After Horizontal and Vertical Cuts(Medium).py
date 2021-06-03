class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        
        horizontalCuts=sorted(horizontalCuts)+[h]
        verticalCuts=sorted(verticalCuts)+[w]
        mod=10**9+7

        h_max,w_max = -1,-1
        
        for i,h in enumerate(horizontalCuts):
            if not i:
                h_max = max(h_max,h)
            else:
                h_max = max(h_max,h-horizontalCuts[i-1])

                
        for j,w in enumerate(verticalCuts):
            if not j:
                w_max = max(w_max,w)
            else:
                w_max = max(w_max,w-verticalCuts[j-1])

        return (h_max*w_max)%mod
        
