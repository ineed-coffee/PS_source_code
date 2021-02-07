def solution(numbers, target):
    from collections import deque
    
    answer = 0
    que = deque([[0,0]])
    idx,L=0,len(numbers)
    
    while que:
        for _ in range(len(que)):
            current_num,used_num = que.popleft()
            if current_num==target and used_num==L:
                answer+=1
            if idx<=L-1:
                que.append([current_num+numbers[idx],used_num+1])
                que.append([current_num-numbers[idx],used_num+1])
        idx+=1
    
    return answer
