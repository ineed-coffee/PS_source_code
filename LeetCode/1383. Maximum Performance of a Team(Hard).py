class Solution:
    def maxPerformance(self, n: int, speed: List[int], efficiency: List[int], k: int) -> int:
        from heapq import heappop,heappush
        
        mod = 10**9 + 7
        answer=0

        zipped = sorted([*zip(speed,efficiency)],key=lambda x:x[-1],reverse=True)
        hp,cur_sum,L=[],0,0
        
        for cspeed,ceff in zipped:
            if L>=k:
                cur_sum-=heappop(hp)
            heappush(hp,cspeed)
            L = min(k,L+1)
            cur_sum+=cspeed
            answer = max(answer,(cur_sum*ceff))
            
        return answer%mod
