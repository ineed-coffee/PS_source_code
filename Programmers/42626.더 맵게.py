def solution(scoville, K):
    from heapq import heappush,heappop,heapify
    
    answer = 0
    heapify(scoville)
    
    while scoville:
        lowest=heappop(scoville)
        if lowest>=K:
            heappush(scoville,lowest)
            break
        if not scoville: continue
        second_lowest=heappop(scoville)
        heappush(scoville,lowest+(2*second_lowest))
        answer+=1
    
    if not scoville:
        answer=-1
    
    return answer
