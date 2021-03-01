class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        from heapq import heapify,heappop
        freq_dict={}
        for num in nums:
            if num not in freq_dict:
                freq_dict[num]=-1
            freq_dict[num]-=1
        freq_list=[(cnt,num) for num,cnt in freq_dict.items()]
        heapify(freq_list)
        return [heappop(freq_list)[1] for _ in range(k)]
        
