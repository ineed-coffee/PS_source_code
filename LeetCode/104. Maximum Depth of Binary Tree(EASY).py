# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:return 0
        
        self.Answer=0
        self.dfs(root,1)
        return self.Answer
    
    def dfs(self,node,cur_depth):
        
        if (not node.left) and (not node.right):
            self.Answer = max(self.Answer,cur_depth)
        
        if node.left:
            self.dfs(node.left,cur_depth+1)
        if node.right:
            self.dfs(node.right,cur_depth+1)
    
        return 
        
