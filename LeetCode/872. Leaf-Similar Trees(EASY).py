# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:           
        self.seq1=[]
        self.seq2=[]
        self.dfs(root1,1)
        self.dfs(root2,2)
        return True if self.seq1==self.seq2 else False
    
    def dfs(self,node,num):
        
        if (not node.left) and (not node.right):
            if num==1:
                self.seq1.append(node.val)
            else:
                self.seq2.append(node.val)
                
        if node.left:
            self.dfs(node.left,num)
        if node.right:
            self.dfs(node.right,num)
        return 
        
