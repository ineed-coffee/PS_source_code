def solution(people, limit):
    answer = 0
    match=len(people)-1
    people.sort()
    survived=[False]*len(people)
    for (i,weight) in enumerate(people):
        if survived[i]:
            break
            
        while (match>i) and weight+people[match]>limit:
            survived[match]=True
            match-=1
            answer+=1
        
        if match>i:
            survived[match]=True
            match-=1
        survived[i]=True
        answer+=1
    
    return answer
