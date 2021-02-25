class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        from collections import defaultdict
        from heapq import heapify,heappop
        
        word_dict=defaultdict(int)
        for word in words:
            word_dict[word]-=1
        word_heap=[(y,x) for x,y in word_dict.items()]
        heapify(word_heap)
        return [heappop(word_heap)[1] for _ in range(k)]
        
