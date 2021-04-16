class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        
        flag=1
        while flag:
            cnt=0
            flag=False
            adj=set()
            for i,letter in enumerate(s):
                if (not i) or (letter!=cur):
                    cur=letter
                    cnt=1
                else:
                    cnt+=1
                    if cnt==k:
                        flag=True
                        adj.add(letter)
                        cnt=0
                        cur=None
       
            for let in adj:
                s=s.replace(let*k,"")
        return s
