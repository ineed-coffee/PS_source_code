class Solution:
    def minimumLengthEncoding(self, words: List[str]) -> int:
        answer=0
        word_set=set()
        words.sort(key=lambda x:len(x),reverse=True)
        for word in words:
            L=len(word)
            if any([element[-L:]==word for element in word_set]):
                continue
            word_set.add(word)
            answer+=(L+1)
        return answer
