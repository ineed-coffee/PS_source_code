class Solution:
    def isValid(self, s: str) -> bool:        
        # open_ = ['[','{','(']
        # close_ = [']','}',')']
        
        bracket_map = {"(": ")", "[": "]",  "{": "}"}
        open_par = set(["(", "[", "{"])
        
        stack = []
        point_idx=-1
        
        for i in range(len(s)):
            
            if s[i] in open_par:
                if point_idx == len(stack)-1:
                    stack.append(s[i])
                    point_idx+=1
                else:
                    point_idx+=1
                    stack[point_idx]=s[i]
                    
            else:
                
                if (point_idx<0) or s[i] != bracket_map[stack[point_idx]]:
                    return False
                
                point_idx-=1

        return True if point_idx==-1 else False
