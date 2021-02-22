class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        from collections import defaultdict
        
        letters=defaultdict(int)
        for letter in tiles:
            letters[letter]+=1
            
        def backtrack(str_seq):
            nonlocal letters,seq_len,answer
            
            if len(str_seq)==seq_len:
                answer+=1
                return
            for letter in letters:
                if letters[letter]:
                    letters[letter]-=1
                    backtrack(str_seq+letter)
                    letters[letter]+=1
            return
        
        answer=0
        for seq_len in range(1,len(tiles)+1):
            backtrack("")   
        return answer
