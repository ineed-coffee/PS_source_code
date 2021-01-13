# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        
        self.parent=None
        self.is_left_child=False
        self.current_node = root
        self.found_node=False
        
        while self.current_node:
            
            if self.current_node.val == val:
                self.found_node=True
                if self.parent:
                    if self.is_left_child:
                        self.parent.left=None
                    else:
                        self.parent.right=None
                break
            
            elif self.current_node.val < val:
                self.is_left_child=False
                self.parent=self.current_node
                self.current_node = self.current_node.right
            else:
                self.is_left_child=True
                self.parent=self.current_node
                self.current_node = self.current_node.left
                
        return self.current_node if self.found_node else None
                
        
