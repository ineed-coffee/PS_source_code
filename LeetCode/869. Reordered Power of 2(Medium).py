class Solution:
    def reorderedPowerOf2(self, N: int) -> bool:
        digits = list(map(int,list(str(N))))
        max_possible=int("".join(list(map(str,sorted(digits,reverse=True)))))
        
        digits_dict={}
        for d in digits:
            digits_dict[d]=digits_dict.get(d,0)+1
        
        power_2=1
        answer=False
        while power_2<=max_possible:
            power_2_digit = list(map(int,list(str(power_2))))
            match=True
            for k,v in digits_dict.items():
                if power_2_digit.count(k)!=v:
                    match=False
                    break
            if match:
                answer=True
                break
            power_2=power_2*2
        return answer
