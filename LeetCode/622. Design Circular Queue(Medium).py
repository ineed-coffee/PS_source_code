class MyCircularQueue:

    def __init__(self, k: int):
        self.size=k
        self.que = [None]*self.size
        self.pop_ptr=0
        self.ins_ptr=0
        self.cnt=0
    def enQueue(self, value: int) -> bool:
        if self.que[self.ins_ptr]==None:
            self.que[self.ins_ptr]=value
            self.cnt+=1
            self.ins_ptr=(self.ins_ptr+1)%self.size
            return True
        return False
        
    def deQueue(self) -> bool:
        if self.que[self.pop_ptr]!=None:
            self.que[self.pop_ptr]=None
            self.cnt-=1
            self.pop_ptr=(self.pop_ptr+1)%self.size
            return True
        return False

    def Front(self) -> int:
        return self.que[self.pop_ptr] if self.que[self.pop_ptr]!=None else -1
        

    def Rear(self) -> int:
        return self.que[self.ins_ptr-1] if self.que[self.ins_ptr-1]!=None else -1
        

    def isEmpty(self) -> bool:
        return self.cnt==0
        
    def isFull(self) -> bool:
        return self.cnt==self.size
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
