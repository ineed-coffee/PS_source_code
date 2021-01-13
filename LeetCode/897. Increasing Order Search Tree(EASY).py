# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        
        self.root = None
        self.in_order(root)
        return self.root
    
    def in_order(self,node):
        
        if node.left:
            self.in_order(node.left)
        
        if not self.root:
            self.root=node
            self.current=self.root
        else:
            self.current.right=TreeNode(val=node.val)
            self.current = self.current.right
        
        if node.right:
            self.in_order(node.right)
        
        return
