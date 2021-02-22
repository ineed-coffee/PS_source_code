class CombinationIterator:

    def __init__(self, characters: str, combinationLength: int):
        self.pointer=0
        self.combs=[]
        self.L = len(characters)
        visited=[False]*self.L
        
        def backtrack(current_comb,current_idx):
            nonlocal characters,combinationLength,visited
            
            if len(current_comb)==combinationLength:
                self.combs.append(current_comb)
                return
            
            for i in range(current_idx+1,self.L):
                if not visited[i]:
                    visited[i]=True
                    backtrack(current_comb+characters[i],i)
                    visited[i]=False
            return

        for i in range(len(characters)-combinationLength+1):
            backtrack(characters[i],i)        

    def next(self) -> str:
        ret=self.combs[self.pointer]
        self.pointer+=1
        return ret
        
    def hasNext(self) -> bool:
        return self.pointer<len(self.combs)
