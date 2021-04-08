class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dig2ch = {
            "2":["a","b","c"],
            "3":["d","e","f"],
            "4":["g","h","i"],
            "5":["j","k","l"],
            "6":["m","n","o"],
            "7":["p","q","r","s"],
            "8":["t","u","v"],
            "9":["w","x","y","z"]
        }
        
        answer=[]
        for dig in digits:
            if not answer:
                for letter in dig2ch[dig]:
                    answer.append(letter)
            else:
                tmp=[]
                for letter in dig2ch[dig]:
                    tmp+=[ch+letter for ch in answer]
                answer=tmp
        return answer
