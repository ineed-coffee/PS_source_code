class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        max_range=10**6
        self.L=int(max_range**0.5)
        self.hashmap=[0]*self.L
        return
    
    def _get_address(self,key_val):
        return key_val%self.L
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        hash_address=self._get_address(key)
        if self.hashmap[hash_address]:
            for i,(key_,_) in enumerate(self.hashmap[hash_address]):
                if key_==key:
                    self.hashmap[hash_address][i][1]=value
                    return
            self.hashmap[hash_address].append([key,value])
        else:
            self.hashmap[hash_address]=[[key,value]]
        return
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        hash_address=self._get_address(key)
        if not self.hashmap[hash_address]: return -1
        for key_,val_ in self.hashmap[hash_address]:
            if key_==key:
                return val_
        return -1
        
    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        hash_address=self._get_address(key)
        if not self.hashmap[hash_address]: return
    
        for i,(key_,_) in enumerate(self.hashmap[hash_address]):
            if key_==key:
                self.hashmap[hash_address][i][1]=-1
        return


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)
