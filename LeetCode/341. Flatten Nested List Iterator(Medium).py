# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger:
#    def isInteger(self) -> bool:
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        """
#
#    def getInteger(self) -> int:
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        """
#
#    def getList(self) -> [NestedInteger]:
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        """

class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.flat=self.flatten(nestedList)
        self.L=len(self.flat)
        self.ptr=0
        return
                
    def flatten(self,element):
        ret=[]
        for sub in element:
            if sub.getInteger()!=None:
                ret.append(sub.getInteger())
            else:
                ret+=self.flatten(sub.getList())
        return ret
    
    def next(self) -> int:
        self.ptr+=1
        return self.flat[self.ptr-1]
        
    def hasNext(self) -> bool:
        return self.ptr<self.L
         

# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())
