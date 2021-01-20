def solution(citations):
    from collections import defaultdict
    cite_dict = defaultdict(int)
    answer = 0
    
    for cite in citations:
        cite_dict[cite]+=1
        
    h_max = max(cite_dict.keys())
    
    H=[-1]*(h_max+1)
    
    for i in range(h_max,-1,-1):
        if i in cite_dict:
            if i==h_max:
                H[i]=cite_dict[i]
            else:
                H[i]=H[i+1]+cite_dict[i]
        else:
            H[i]=H[i+1]
        
        if i<=H[i]:
            answer=i
            break
    
    return answer
