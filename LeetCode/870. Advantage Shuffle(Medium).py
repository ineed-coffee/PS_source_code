clclass Solution:
    def advantageCount(self, A: List[int], B: List[int]) -> List[int]:
        from collections import deque
        
        L=len(A)
        if L==1: return A
        
        A_s=deque(sorted(A))
        B_s=sorted([(i,v) for i,v in enumerate(B)],key=lambda x:x[1])
        
        answer=[-1]*L
        ptr=L-1
        while A_s :
            a=A_s.pop()
            
            while (ptr>=0) and ((B_s[ptr][1]>=a) or (answer[B_s[ptr][0]]!=-1)):
                answer[B_s[ptr][0]]=A_s.popleft()
                ptr -= 1
                
            if ptr>=0 :
                idx,_=B_s[ptr]
                answer[idx]=a
                ptr-=1

        return answer
