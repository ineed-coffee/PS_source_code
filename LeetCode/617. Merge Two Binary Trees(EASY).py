# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        
        if not t1: return t2
        if not t2: return t1
        
        self.Traversal(t1,t2)
        return t1
    
    def Traversal(self,current_node,compare_node):

        current_node.val = current_node.val + compare_node.val
        
        if compare_node.left:
            if not current_node.left:
                current_node.left = compare_node.left
            else:
                self.Traversal(current_node.left,compare_node.left)
            
        if compare_node.right:
            if not current_node.right:
                current_node.right = compare_node.right
            else:
                self.Traversal(current_node.right,compare_node.right)
            
        return
