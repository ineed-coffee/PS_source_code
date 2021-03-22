class Solution:
    def spellchecker(self, wordlist: List[str], queries: List[str]) -> List[str]:
        
        def devowel(str_):
            return "".join([s if s not in 'aeiou' else "a" for s in str_.lower()])
        
        case_dict=[]
        case_dict.append(set(wordlist))
        
        decaped,devoweled={},{}
        for w in wordlist:
            if not decaped.get(w.lower(),0):
                decaped[w.lower()]=w
            if not devoweled.get(devowel(w.lower()),0):
                devoweled[devowel(w.lower())]=w
                
        case_dict.append(decaped)
        case_dict.append(devoweled)
        
        for i,q in enumerate(queries):
            if q in case_dict[0]:
                pass
            elif q.lower() in case_dict[1]:
                queries[i]=case_dict[1][q.lower()]
            else:
                d=devowel(q)
                if d in case_dict[2]:
                    queries[i]=case_dict[2][d]
                else:
                    queries[i]=""
        return queries
