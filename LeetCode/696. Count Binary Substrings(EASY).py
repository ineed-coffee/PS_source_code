class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        answer=0
        cnts=[]
        for i,str_ in enumerate(s):
            if not i:
                cur_str=str_
                cur_num=1
            elif str_==cur_str:
                cur_num+=1
            else:
                cur_str=str_
                cnts.append(cur_num)
                cur_num=1
        cnts.append(cur_num)
                
        for i in range(len(cnts)-1):
            answer+=min(cnts[i],cnts[i+1])

        return answer
