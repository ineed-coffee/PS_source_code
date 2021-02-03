def solution(number, k):
    stack=[number[0]]
    L=len(number)
    selects=L-k-1
    
    for i,num in enumerate(number):
        if not i:continue
                        
        while stack and int(stack[-1])<int(num) and (L-i)>selects:
            stack.pop()
            selects+=1
            
        if selects:
            stack.append(num)
            selects-=1
    
    return "".join(stack)
