def solution(operations):
    from heapq import heappush , heappop , heapify
    answer = []
    heapify(answer)
    
    for op in operations:
        command,detail = op.split()
        if command == "I":
            heappush(answer,int(detail))
        else:
            if not answer:
                continue
            if int(detail)==1:
                max_list = [(-i,i) for i in answer]
                #print("m:",max_list)
                heapify(max_list)
                _,current_max=heappop(max_list)
                answer.remove(current_max)
            else:
                heappop(answer)
        #print(answer)
                
    if not answer: return [0,0]
    return [max(answer),min(answer)]
