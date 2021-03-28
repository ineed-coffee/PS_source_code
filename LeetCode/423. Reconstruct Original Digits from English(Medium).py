class Solution:
    def originalDigits(self, s: str) -> str:
        digits =[
            ('w','two',2),
            ('u','four',4),
            ('x','six',6),
            ('f','five',5),
            ('z','zero',0),
            ('r','three',3), 
            ('t','eight',8),
            ('s','seven',7),
            ('i','nine',9),
            ('n','one',1)
        ]

        s_set={}
        for s_ in s:
            s_set[s_]=s_set.get(s_,0)+1
        
        answer_gen = []
        for d in digits:
            unique,full,num=d
            cnt = s_set.get(unique,0)
            if not cnt : continue
            answer_gen.append((num,cnt))
            for char_ in set(full):
                s_set[char_] -= cnt*full.count(char_)

        return ''.join([str(k)*v for k,v in sorted(answer_gen)])
