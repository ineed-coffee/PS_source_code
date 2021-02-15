# BFS---------------------------------
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


# DFS---------------------------------
def solution(numbers, target):
    answer=0
    numbers=[0]+numbers
    N = len(numbers)
    stack=[(0,numbers[0],1)]
    
    while stack:
        cur_idx,cur_num,used_cnt=stack.pop()
        if (cur_num==target) and (used_cnt==N):
            answer+=1
            continue
        if cur_idx<N-1:
            stack.append((cur_idx+1,cur_num-numbers[cur_idx+1],used_cnt+1))
            stack.append((cur_idx+1,cur_num+numbers[cur_idx+1],used_cnt+1))
            
    return answer
