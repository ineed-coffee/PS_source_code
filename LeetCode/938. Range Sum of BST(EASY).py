# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    
    def __init__(self):
        self.range_sum=0
    
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        
        self.low_bound = low
        self.high_bound = high
        self.Traversal(root)
        
        return self.range_sum
        
    def Traversal(self,node):
        
        if self.is_between(node.val):
            self.range_sum+=node.val
        if node.left:
            self.Traversal(node.left)
        if node.right:
            self.Traversal(node.right)
        return
    
    def is_between(self,value):
        
        if (value>=self.low_bound)and(value<=self.high_bound):
            return True
        return False
