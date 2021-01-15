def solution(clothes):
    from collections import defaultdict
    
    answer = 0
    
    cloth_dict=defaultdict(int)
    for cloth in clothes:
        cloth_dict[cloth[1]]+=1
       
    for val in cloth_dict.values():
        if not answer:
            answer = val+1
        else:
            answer = answer*(val+1)

    return answer-1
