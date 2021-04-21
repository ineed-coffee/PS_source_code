class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        
        for i,row in enumerate(triangle):
            if not i: continue
            for j,col in enumerate(row):
                if not j:
                    triangle[i][j]+=triangle[i-1][j]
                elif j==i:
                    triangle[i][j]+=triangle[i-1][j-1]
                else:
                    triangle[i][j]+=min(triangle[i-1][j],triangle[i-1][j-1])
        return min(triangle[-1])
