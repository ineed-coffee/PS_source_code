def solution(prices):
    L = len(prices)
    answer = [-1]*L
    
    for i in range(L):
        non_desc=0
        for j in range(i+1,L):
            non_desc+=1
            if prices[i]<=prices[j]:
                continue
            break
        answer[i]=non_desc
            
    return answer
