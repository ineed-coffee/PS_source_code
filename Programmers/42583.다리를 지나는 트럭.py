def solution(bridge_length, weight, truck_weights):
    from collections import deque
    
    answer = 0
    current_idx=0
    que = deque()
    que_total_weight=0
    
    while True:

        for truck in que:
            truck[1]+=1
            
        if (not que) and (current_idx == len(truck_weights)):
            break
            
        if (que) and (que[0][1]>bridge_length):
            w,d = que.popleft()
            que_total_weight-=w
        
        if current_idx < len(truck_weights):
            if que_total_weight+truck_weights[current_idx]<=weight:
                que.append([truck_weights[current_idx],1])
                que_total_weight+=truck_weights[current_idx]
                current_idx+=1
                
        answer+=1
            
    return answer
