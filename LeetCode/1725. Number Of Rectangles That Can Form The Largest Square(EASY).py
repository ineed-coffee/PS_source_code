class Solution:
    def countGoodRectangles(self, rectangles: List[List[int]]) -> int:
        k_s = [min(lengths) for lengths in rectangles]
        maxLen = max(k_s)
        k_s.sort(reverse=True)
        
        i=0
        while (i<=len(k_s)-1) and (k_s[i]==maxLen):
            i+=1
        
        return i
