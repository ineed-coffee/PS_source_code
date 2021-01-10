def solution(progresses, speeds):
    answer = []
    
    pop_idx , L = 0 , len(progresses)
    
    while True:
        
        work_done=0
        flag=False
        while progresses[pop_idx]==100:
            pop_idx+=1
            work_done+=1
            if pop_idx>=L:
                flag=True
                break
                
        if work_done: answer.append(work_done)
        if flag: return answer
        
        for i in range(pop_idx,L):
            progresses[i]=min(100,progresses[i]+speeds[i])

    return None
