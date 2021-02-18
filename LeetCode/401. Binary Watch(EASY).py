class Solution:
    def readBinaryWatch(self, num: int) -> List[str]:

        self.visited=[False]*10
        self.idx_to_hour = {i:2**(3-i) for i in range(4)}
        self.idx_to_min = {i:2**(9-i) for i in range(4,10)}
        self.answer=[]
        
        self.backtrack(num,0)
        
        return self.answer
    
    def backtrack(self,used_led,current_idx):
        
        if not used_led:
            time = self.as_time()
            if time : self.answer.append(time)
            return
        
        for idx in range(current_idx,10):
            if not self.visited[idx]:
                self.visited[idx]=True
                self.backtrack(used_led-1,idx)
                self.visited[idx]=False
        return
    
    def as_time(self):
        
        hour,minute=0,0
        for i,on_off in enumerate(self.visited[:4]):
            if on_off: hour+=self.idx_to_hour[i]
        
        for i,on_off in enumerate(self.visited[4:]):
            if on_off: minute+=self.idx_to_min[i+4]
                
        if not (0<=hour<12): return []
        if not (0<=minute<60): return []
                
        return str(hour)+":"+str(minute).zfill(2)
