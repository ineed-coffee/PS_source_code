class Solution:
    def numberOfSteps (self, num: int) -> int:
        Answer = 0
        
        while True:
            D,R = num//2,num%2
            
            if R:
                Answer+=1
                num-=1
                
            if not D:
                return Answer
            num = D
            Answer+=1
