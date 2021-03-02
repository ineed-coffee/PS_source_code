class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        from heapq import heapify,heappush,heappop,heappushpop
        self.hf=heapify
        self.hps=heappush
        self.hpp=heappop
        self.hpsp=heappushpop
        self.heap=nums
        self.k=k
        self.hf(self.heap)
        while len(self.heap)>self.k:
            self.hpp(self.heap)
        return
    
    def add(self, val: int) -> int:
        if len(self.heap)<self.k:
            self.hps(self.heap,val)
        else:
            self.hpsp(self.heap,val)
        return self.heap[0]
        
# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
