class RecentCounter:

    def __init__(self):
        self.requests=[0]*3002
        self.insert_idx=-1
        self.pop_idx=0
        
        return self.ping(-1)        

    def ping(self, t: int) -> int:
        
        if t<0:
            return None
        
        self.insert_idx = (self.insert_idx+1)%3002
        self.requests[self.insert_idx]=t
        
        while (self.requests[self.pop_idx]<t-3000):
            
            self.pop_idx = (self.pop_idx+1)%3002
        
        if self.pop_idx<=self.insert_idx:
            ret_val = self.insert_idx-self.pop_idx +1
        elif self.pop_idx>self.insert_idx:
            ret_val = 3002 - (self.pop_idx-self.insert_idx) +1
        
        return ret_val
