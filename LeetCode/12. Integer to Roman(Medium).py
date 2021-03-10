class Solution:
    def intToRoman(self, num: int) -> str:
        
        num2str={"1":"I","5":"V","10":"X","50":"L","100":"C","500":"D","1000":"M"}
        L=len(str(num))
        answer=""
        for i,n in enumerate(list(str(num))):
            if (n=="4") or (n=="9"):
                if n=="4":
                    back=num2str["5"+"0"*(L-i-1)]
                    front=num2str["1"+"0"*(L-i-1)]
                    answer+=front+back
                else:
                    back=num2str["1"+"0"*(L-i)]
                    front=num2str["1"+"0"*(L-i-1)]
                    answer+=front+back
            
            else:
                if int(n)<4:
                    answer+=num2str["1"+"0"*(L-i-1)]*int(n)
                else:
                    answer+=num2str["5"+"0"*(L-i-1)]
                    answer+=num2str["1"+"0"*(L-i-1)]*(int(n)-5)
                    
        return answer
