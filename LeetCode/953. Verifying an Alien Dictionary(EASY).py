class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        ch2idx={}
        for o in order:
            ch2idx[o]=len(ch2idx)
        return words==sorted(words,key=lambda x:[ch2idx[i] for i in x])
        
        
