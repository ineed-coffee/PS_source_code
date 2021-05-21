class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        
        def encode(word):
            cur=96
            marked={}
            ret=''
            for w in word:
                if w not in marked:
                    cur+=1
                    marked[w]=cur
                ret+=chr(marked[w])
            return ret
        
        encoded_pattern = encode(pattern)
        
        encoded_words = [encode(word) for word in words]
        
        ret=[]
        for ew,w in zip(encoded_words,words):
            if ew == encoded_pattern:
                ret.append(w)
        
        return ret
