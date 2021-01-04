def solution(priorities, location):
    answer = 0
    pop_idx = 0
    current_prior = max(priorities[pop_idx:])
    
    while True:
        if priorities[pop_idx]==current_prior:
            answer+=1
            if pop_idx == location:
                break
            else:
                pop_idx+=1
                current_prior = max(priorities[pop_idx:])          
        else:
            priorities.append(priorities[pop_idx])
            if pop_idx == location:
                location = len(priorities)-1
            pop_idx+=1
    return answer
