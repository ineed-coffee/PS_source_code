def solution(answers):

    A = [1,2,3,4,5]
    A_L = len(A)
    B = [2,1,2,3,2,4,2,5]
    B_L = len(B)
    C = [3,3,1,1,2,2,4,4,5,5]
    C_L = len(C)
    
    scores={"A":0,"B":0,"C":0}
    
    for i,answer in enumerate(answers):
        if A[i%A_L]==answer:
            scores["A"]+=1
        if B[i%B_L]==answer:
            scores["B"]+=1
        if C[i%C_L]==answer:
            scores["C"]+=1
            
    high_score = max(scores.values())
    return_list=[]
    for i,supo in enumerate(["A","B","C"]):
        if scores[supo]==high_score:
            return_list.append(i+1)
    return return_list
    
    
    return answer
