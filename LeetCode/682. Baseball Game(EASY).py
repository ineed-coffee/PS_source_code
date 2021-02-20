class Solution:
    def calPoints(self, ops: List[str]) -> int:
        
        Scores=[]
        for operation in ops:
            if operation == "+":
                Scores.append(Scores[-1]+Scores[-2])
            elif operation == "D":
                Scores.append(Scores[-1]*2)
            elif operation == "C":
                Scores.pop()
            else:
                Scores.append(int(operation))
                
        return sum(Scores)
        
