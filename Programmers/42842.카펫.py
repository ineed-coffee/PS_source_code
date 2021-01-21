def solution(brown, yellow):
    answer = []
 
    for i in range(1,int(yellow**0.5)+2):
        if not yellow%i:
            l1,l2 = i,yellow//i
            if (l1+2)*(l2+2)==brown+yellow:
                return [l1+2,l2+2] if l1>=l2 else [l2+2,l1+2]
