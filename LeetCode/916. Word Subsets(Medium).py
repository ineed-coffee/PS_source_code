class Solution:
    def wordSubsets(self, A: List[str], B: List[str]) -> List[str]:
        
        required={}
        for b in B:
            tmp={}
            for char_ in b:
                tmp[char_]=tmp.get(char_,0)+1
            for k,v in tmp.items():
                required[k]=max(required.get(k,0),v)
               
        answer=[]
        for a in A:
            match=True
            for k,v in required.items():
                if a.count(k)<v:
                    match=False
                    break
            if match:
                answer.append(a)
        return answer
