class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        from heapq import heapify,heappop
        dists=[(((x**2)+(y**2))**0.5,i) for i,(x,y) in enumerate(points)]
        heapify(dists)
        return [points[heappop(dists)[1]] for _ in range(K)]
        
